from dataclasses import dataclass, field

from models.qualification import Qualification


@dataclass
class Member:
	id: int
	name: str
	qualfications: list[Qualification] = field(default_factory=lambda: [])

	def has_qual(self, code: str) -> bool:
		""" Checks if the member has specific qualification assigned to them

		Args:
			code (str): Qualification accreditation code to check for e.g. "CFR-ACC"

		Returns:
			bool: True if the member has the qualification, False if not
		"""
		found = next(filter(lambda i: i.code == code, self.qualfications), None)

		if found == None:
			return False

		return True

	def get_qual(self, code: str) -> Qualification:
		""" Returns the qualification object for the given code

		Args:
			code (str): Qualification accreditation code to check for e.g. "CFR-ACC"

		Returns:
			Qualification: Member qualification object that was found or None
		"""
		if self.has_qual(code) == False:
			return None

		return next(filter(lambda i: i.code == code, self.qualfications), None)

if __name__ == "__main__":
    pass
