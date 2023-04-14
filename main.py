import os
from models.beacon_config import BeaconConfig
from models.member import Member
from templater import generate_html_template
from utils.codes import get_qualifications
from utils.ignore import process_ignore_list
from utils.process_data import process_qualifications_export
import argparse

# Add argument parser
parser = argparse.ArgumentParser("member_capability")
parser.add_argument(
    "-p",
    "--path",
    help="The path of the member capability CSV export",
    type=str,
    required=False,
)
parser.add_argument(
    "-o",
    "--output",
    help="The filename of file outputted",
    type=str,
    required=False,
    default="generated-gap.html",
)
parser.add_argument(
    "-i",
    "--ignore",
    help="Commaseparated list of member numbers to ignore",
    type=str,
    required=False,
    default=None,
)

# Add beacon options
parser.add_argument(
    "-b",
    "--beacon",
    help="Sync with beacon",
    action=argparse.BooleanOptionalAction,
    default=False,
)
parser.add_argument(
    "--beacon-env",
    help="The environment to sync with",
    type=str,
    required=False,
    default="trainbeacon",
)
parser.add_argument(
    "--beacon-user",
    help="The username to use for beacon",
    type=str,
    required=False,
    default=None,
)
parser.add_argument(
    "--beacon-pass",
    help="The password to use for beacon",
    type=str,
    required=False,
    default=None,
)

args = parser.parse_args()


def generate():
    """Process all data and generate the HTML template"""
    qualifications = get_qualifications()

    # Request path of qualifications csv
    path = load_csv_path()

    # Process qualifications csv
    members = process_qualifications_export(path)

    # Remove ignored members
    members = process_ignore_list(members, args.ignore)

    # Generate HTML template
    generate_html_template(members, qualifications, args.output)

    if args.beacon:
        transport_beacon(members, qualifications)


def load_csv_path() -> str:
    """Load the path of the qualifications csv file and ensure it exists

    Returns:
            str: valid CSV file path
    """
    file_exists = False

    if args.path is not None:
        if os.path.exists(args.path) == False:
            print("File does not exist")
        else:
            return args.path

    while file_exists == False:
        path = input("Enter path of qualifications csv: ")

        if os.path.exists(path) == False:
            print("File does not exist")
        else:
            file_exists = True
            return path


def transport_beacon(members: list[Member], qualifications: list[object]):
    """Transport data to beacon

    Args:
            members (list[Member]): List of members
            qualifications (list[Qualification]): List of qualifications
    """

    # Check required args set
    req_args = ["beacon_user", "beacon_pass"]
    for arg in req_args:
        if getattr(args, arg) is None:
            print(f"Missing required argument {arg}")
            return

    from transporters import beacon as beacon_transporter

    config = BeaconConfig(
        environment=args.beacon_env,
        username=args.beacon_user,
        password=args.beacon_pass,
    )

    beacon_transporter.sync_beacon(config, members, qualifications)


if __name__ == "__main__":
    generate()
