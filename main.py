import os
from templater import generate_html_template
from utils.codes import get_qualifications
from utils.process_data import process_qualifications_export
import argparse

# Add argument parser
parser = argparse.ArgumentParser("member_capability")
parser.add_argument("-p", "--path", help="The path of the member capability CSV export", type=str, required=False)
parser.add_argument("-o", "--output", help="The filename of file outputted", type=str, required=False, default="generated-gap.html")
args = parser.parse_args()

def generate():
	""" Process all data and generate the HTML template
	"""
	qualifications = get_qualifications()

	# Request path of qualifications csv
	path = load_csv_path()

	# Process qualifications csv
	members = process_qualifications_export(path)

	# Generate HTML template
	generate_html_template(members, qualifications, args.output)

def load_csv_path() -> str:
	""" Load the path of the qualifications csv file and ensure it exists

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

if __name__ == "__main__":
	generate()
