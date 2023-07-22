import json
import os
import requests
import time

from scripts.build_api_json import verify_claims


BIN_ID = "64bbb1639d312622a382f7ed"
TEST = "0x17e33637f6B64E9082Ea499481b6e6EbAE7EEA23"


def main():
    # this works but the json that can be uploaded is size limited; 100kb or
    # 1mb on the pro program
    # ref: https://jsonbin.io/app/bins
    req = requests.get(
        os.path.join("https://api.jsonbin.io/v3/b/", BIN_ID, "latest"),
        headers={"X-Master-Key": os.environ["JSONBIN_MASTER_KEY"]},
    )

    # does the job, not sure about any limits
    # ref: https://www.jsonkeeper.com/b/RI3Q
    req = requests.get("https://www.jsonkeeper.com/b/RI3Q")

    # grab json locally to simulate api call
    req = json.load(open("result.json"))

    if verify_claims(TEST, req[TEST]):
        print("Success!")
    else:
        print("Failed!")

    # give brownie time to close connection
    time.sleep(1)
