from dataclasses import dataclass
import arrow

@dataclass
class Qualification:
    code: str
    name: str
    expiry: str = None

    def __post_init__(self):

        if self.expiry is not None:
            self.expiry = arrow.get(self.expiry, "D/M/YYYY")



    def in_date(self) -> bool:

        if self.expiry is None:
            return True

        now = arrow.now("Australia/Sydney")

        return self.expiry.timestamp() > now.timestamp()
