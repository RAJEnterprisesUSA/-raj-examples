"""Owner Oct 25 night: pull the Mannequin Challenge remix (not a current trend) from all four platforms."""
import time
from queue_everywhere_oct24 import gql
DEL = """mutation($input: DeletePostInput!){ deletePost(input:$input){ __typename } }"""
IDS = ["6adea4228b3d437ddc3865ea", "6adea4258b3d437ddc38666e", "6adea4293d5b27036bff6892", "6adea42c8b3d437ddc3869ac"]
for i in IDS:
    d = gql(DEL, {"input": {"id": i}})
    print(i, ((d.get("data") or {}).get("deletePost") or {}).get("__typename"), "" if d.get("data") else str(d)[:200])
    time.sleep(3)
