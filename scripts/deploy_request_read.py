#!/usr/bin/python3
from brownie import Hornet, config, network
from web3 import Web3
from scripts.helpful_scripts import (
    fund_with_link,
    get_account,
    get_contract,
    is_verifiable_contract,
)


def deploy_hornet():
    jobId = config["networks"][network.show_active()]["jobId"]
    fee = config["networks"][network.show_active()]["fee"]

    oracle = get_contract("oracle").address
    link_token = get_contract("link_token").address
    print("Deploying Hornet...")
    Hornet.deploy(
        oracle,
        Web3.toHex(text=jobId),
        fee,
        link_token,
        {"from": get_account()},
        publish_source=is_verifiable_contract(),
    )


def request_api():
    hornet = Hornet[-1]
    print("Funding Hornet with $LINK...")
    tx = fund_with_link(
        hornet.address, amount=config["networks"][network.show_active()]["fee"]
    )
    tx.wait(1)
    print("Requesting volume data...")
    hornet.requestVolumeData({"from": get_account()})


def read_data():
    print(f"Reading data from Hornet...")
    print(Hornet[-1].volume())


def main():
    deploy_hornet()
    request_api()
    read_data()
