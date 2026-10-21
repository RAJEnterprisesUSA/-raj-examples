"""Owner Oct 20 night ("ok add for realistic ai videos"): turn on TikTok's AI-generated label
(Buffer metadata.tiktok.isAiGenerated) for queued posts with realistic AI visuals. Drawn rig
animation (the Chronicles) stays unlabeled. On-screen stamps stay as well."""
import json, subprocess, sys, time

API = "https://api.buffer.com"
REALISTIC = ["6ad80478f9a362e691d01235",   # Thu Hosting Chaos v2 (Veo video, AI people)
             "6ad7e9022b60166c6ac1ac44",   # Sat Guess the Theme Pt. 1 (photoreal AI images)
             "6ad7e9068e50122a680c42d6"]   # Sun Guess the Theme Pt. 2
EDIT = """mutation($input: EditPostInput!){ editPost(input:$input){ __typename
 ... on PostActionSuccess { post { id } } ... on MutationError { message } } }"""

def gql(q, v):
    r = subprocess.run(["curl", "-sS", "--max-time", "60", API, "-H", "Content-Type: application/json",
                        "-d", json.dumps({"query": q, "variables": v})], capture_output=True, text=True)
    d = json.loads(r.stdout)
    if "errors" in d and "RATE_LIMIT" in json.dumps(d["errors"]):
        time.sleep(90); return gql(q, v)
    return d

if __name__ == "__main__":
    rows = {n["id"]: n for n in json.load(open(sys.argv[1]))}
    for pid in REALISTIC:
        n = rows[pid]
        d = gql(EDIT, {"input": {"id": pid, "text": n["text"],
                                 "assets": [{"video": {"url": a["source"]}} for a in n["assets"]],
                                 "metadata": {"tiktok": {"isAiGenerated": True}}}})
        ok = ((d.get("data") or {}).get("editPost") or {}).get("__typename") == "PostActionSuccess"
        print("EDIT" if ok else "FAIL", pid, n["assets"][0]["source"].rsplit("/", 1)[-1], "" if ok else json.dumps(d)[:300])
        time.sleep(3)
