"""Owner-approved YouTube queue cleanup (Oct 20 night, "Delete 4 pink, fix 9"): delete the 4
Pink October health Shorts (the charter bans health/awareness Shorts on this channel) and rewrite
the 9 trend + Chronicles descriptions to the charter (one line, max 3 hashtags, no phone, URL or
"free"; episodes end with a light "next episode tomorrow"). Titles and times stay."""
import json, subprocess, sys, time

API = "https://api.buffer.com"
EDIT = """mutation($input: EditPostInput!){ editPost(input:$input){ __typename
 ... on PostActionSuccess { post { id } } ... on MutationError { message } } }"""
DEL = """mutation($input: DeletePostInput!){ deletePost(input:$input){ __typename } }"""
DESC = {
    "6ad57eb50a208cb3238e96d5": "The Big Business Chronicles EP. 29: one masterpiece, one headbutt, and a Halloween pumpkin that carved itself. Next episode tomorrow.\n\n#thebigbusinesschronicles #halloween #comedy",
    "6ad592c58206df0c0fb001e2": "The cat took the candy, the chair took a chair, the ghost took the bowl, and he never looked up.\n\n#halloween #funny #lasvegas",
    "6ad592e1769b457934eee9f4": "The Big Business Chronicles EP. 30: the Halloween invites went out and somehow the villain chair got one. Next episode tomorrow.\n\n#thebigbusinesschronicles #halloween #comedy",
    "6ad59a560a208cb3239362d9": "Instant launch, a lane change over rush hour, a soft landing at the venue, party delivered.\n\n#funny #animation #lasvegas",
    "6ad59a730b0d72757a4f1f42": "The Big Business Chronicles EP. 31: the Halloween finale rehearsal passed inspection, then the cat happened. Next episode tomorrow.\n\n#thebigbusinesschronicles #halloween #comedy",
    "6ad5a07d8206df0c0fb2e2f6": "Budget chair: no. Neighbor's table: insulted. Delivery day: applause. The toughest critic in Las Vegas has spoken.\n\n#blackcat #funny #halloween",
    "6ad5a099938409f1d0fd29b2": "The Big Business Chronicles EP. 32: he ordered the Halloween finale supplies and every single box was a chair. Next episode tomorrow.\n\n#thebigbusinesschronicles #halloween #comedy",
    "6ad5a0a7938409f1d0fd2b50": "Pumpkins, a skeleton, a candy station, and the part everybody forgets: somewhere to sit.\n\n#halloween #porchreveal #lasvegas",
    "6ad5a0c30b0d72757a509b77": "The Big Business Chronicles EP. 33: every light worked, then the cat found the outlet. One light survived and it was the wrong one. Next episode tomorrow.\n\n#thebigbusinesschronicles #halloween #comedy",
}
PINK = ["6ad592d30b0d72757a4dac26", "6ad59a64ae173d6e002e7b7e", "6ad5a08bae173d6e002ff5ee", "6ad5a0b5938409f1d0fd2da6"]

def gql(q, v):
    r = subprocess.run(["curl", "-sS", "--max-time", "60", API, "-H",
                        "Content-Type: application/json", "-d", json.dumps({"query": q, "variables": v})],
                       capture_output=True, text=True)
    d = json.loads(r.stdout)
    if "errors" in d and "RATE_LIMIT" in json.dumps(d["errors"]):
        time.sleep(90); return gql(q, v)
    return d

if __name__ == "__main__":
    rows = {n["id"]: n for n in json.load(open(sys.argv[1]))}
    only = sys.argv[2:]  # optional subset of ids
    for pid, text in DESC.items():
        if only and pid not in only: continue
        n = rows[pid]
        inp = {"id": pid, "text": text,
               "assets": [{"video": {"url": a["source"]}} for a in n["assets"]],
               "metadata": {"youtube": {"title": n["metadata"]["title"], "categoryId": "23",
                                        "privacy": "public", "madeForKids": False}}}
        d = gql(EDIT, {"input": inp})
        ok = ((d.get("data") or {}).get("editPost") or {}).get("__typename") == "PostActionSuccess"
        print("EDIT" if ok else "FAIL", pid, n["metadata"]["title"][:40], "" if ok else json.dumps(d)[:300])
        time.sleep(3)
    for pid in PINK:
        if only and pid not in only: continue
        d = gql(DEL, {"input": {"id": pid}})
        ok = ((d.get("data") or {}).get("deletePost") or {}).get("__typename") == "DeletePostSuccess"
        print("DEL " if ok else "FAIL", pid, rows[pid]["metadata"]["title"][:40], "" if ok else json.dumps(d)[:300])
        time.sleep(3)
