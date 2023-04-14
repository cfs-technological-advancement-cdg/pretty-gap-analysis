import datetime
from models.member import Member
import jinja2
from models.qualification import Qualification

def generate_html_template(members: list[Member], qualifications: list[object], output: str):
	templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
	env = jinja2.Environment(loader=templateLoader)

	env.filters['cap_class'] = cap_class
	env.filters['expires'] = cap_expires


	TEMPLATE_FILE = "table.html.jinja"
	template = env.get_template(TEMPLATE_FILE)

	content = template.render(members=members, qualifications=qualifications, time= datetime.datetime.now())

	path = f"output/{output}.html"

	output = open(path,"w")
	output.write(content)
	output.close()

	print(f"Generated report saved to '{path}'")


def cap_class(member: Member, qual_code: str):
	"""Custom filter to add a class to the table cell based on the qualification status"""

	qual: Qualification = member.get_qual(qual_code)

	if qual is None:
		return 'no'

	if qual.in_date() == False:
		return 'expired'

	return 'yes'

def cap_expires(member: Member, qual_code: str):
	"""Custom filter to add expiry dates to qualification cell tooltips"""

	qual = member.get_qual(qual_code)

	if qual is None or qual.expiry is None:
		return

	formatted_expiry = qual.expiry.format("DD-MM-YYYY")

	if formatted_expiry == "31-12-9999":
		formatted_expiry = "Never"

	if qual.in_date():
		return f"Expires: {formatted_expiry}"
	else:
		return f"Expired: {formatted_expiry}"
