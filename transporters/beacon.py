from models.beacon_config import BeaconConfig
from models.member import Member


def sync_beacon(config: BeaconConfig, members: list[Member], quals: list[object]):
    print(config)

    for member in members:
        print(member.name)
