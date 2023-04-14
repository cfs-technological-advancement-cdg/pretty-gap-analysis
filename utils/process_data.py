import csv
import os

from models.member import Member
from models.qualification import Qualification


def process_qualifications_export(path: str) -> list[Member]:
	# Load CSV file
	if os.path.exists(path) == False:
		print("File does not exist")
		return

	members: list[Member] = []

	with open(path, newline="", encoding="utf-8-sig") as csvfile:
		reader = csv.DictReader(csvfile)

		for row in reader:
			id = get_member_id(row.get('Member Name and Primary Number'))
			member = next(filter(lambda i: i.id == id, members), None)

			if member not in members:
				member = normalise_member(row.get('Member Name and Primary Number'))
				members.append(member)

			member.qualfications.append(normalise_qualification(row))
		csvfile.close()

	members = sorted(members, key=lambda d: d.name)

	return members

def normalise_member(data: str):
	primary_name_num = data.split(" - ")

	assert len(primary_name_num) == 2

	return Member(int(primary_name_num[0]), primary_name_num[1])

def get_member_id(name_and_id: str) -> int:
    name_and_id = name_and_id.split(" - ", 1)

    assert len(name_and_id) == 2

    return int(name_and_id[0])

def normalise_qualification(data: object):
	qual_code = data.get("Capability").split(" - ", 1)

	assert len(qual_code) == 2

	qual = Qualification(qual_code[0], qual_code[1], data.get("Capability Expiry Date"))

	return qual
