import csv
import os

from models.member import Member
from models.qualification import Qualification


def process_qualifications_export(path: str) -> list[Member]:
    """Processes the qualifications export CSV file and returns an array of Member objects

    Args:
            path (str): Path to the CSV file to process

    Returns:
            list[Member]: List of Member objects and qualifications
    """
    # Load CSV file
    if os.path.exists(path) == False:
        print("File does not exist")
        return

    members: list[Member] = []

    # Parse CSV
    with open(path, newline="", encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            # Get Member ID
            id = get_member_id(row.get("Member Name and Primary Number"))

            # Check if member already exists in array
            member = next(filter(lambda i: i.id == id, members), None)

            if member not in members:
                # Create new member object and add to array
                member = normalise_member(row.get("Member Name and Primary Number"))
                members.append(member)

            # Add qualification to member
            member.qualfications.append(normalise_qualification(row))

        csvfile.close()

    # Sort members by name
    members = sorted(members, key=lambda d: d.name)

    return members


def normalise_member(data: str) -> Member:
    """Convert member data into a member object

    Args:
            data (str): CSV cell data for Member & Primary ID

    Returns:
            Member: Generated member object
    """

    # Export has the Name and Primary ID in the same cell, split them
    primary_name_num = data.split(" - ")

    # Ensure the split was successful
    assert len(primary_name_num) == 2

    # Create member object and return
    return Member(int(primary_name_num[0]), primary_name_num[1])


def get_member_id(name_and_id: str) -> int:
    """Gets the member ID from the name and ID string

    Args:
            name_and_id (str): CSV cell data for Member & Primary ID

    Returns:
            int: Member's ID number
    """

    # Export has the Name and Primary ID in the same cell, split them
    name_and_id = name_and_id.split(" - ", 1)

    # Ensure the split was successful
    assert len(name_and_id) == 2

    # Return the ID as a int
    return int(name_and_id[0])


def normalise_qualification(data: object) -> Qualification:
    """Convert qualification data into a qualification object

    Args:
            data (object): CSV row data for a qualification

    Returns:
            Qualification: _description_
    """

    # Export has the Capability Code and Name in the same cell, split them
    qual_code = data.get("Capability").split(" - ", 1)

    # Ensure the split was successful
    assert len(qual_code) == 2

    # Create qualification object
    qual = Qualification(qual_code[0], qual_code[1], data.get("Capability Expiry Date"))

    return qual


if __name__ == "__main__":
    pass
