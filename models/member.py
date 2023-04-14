from dataclasses import dataclass, field

from models.qualification import Qualification


@dataclass
class Member:
	id: int
	name: str
	qualfications: list[Qualification] = field(default_factory=lambda: [])

	def has_qual(self, code: str) -> bool:
		found = next(filter(lambda i: i.code == code, self.qualfications), None)

		if found == None:
			return False

		return True

	def get_qual(self, code: str) -> Qualification:
		if self.has_qual(code) == False:
			return None

		return next(filter(lambda i: i.code == code, self.qualfications), None)
