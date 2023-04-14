from dataclasses import dataclass
import arrow

@dataclass
class Qualification:
    code: str
    name: str
    expiry: str = None

    def __post_init__(self):
        # Convert expiry date to arrow object
        if self.expiry is not None:
            self.expiry = arrow.get(self.expiry, "D/M/YYYY")

    def in_date(self) -> bool:
        """ Check if qualification has expired or not

        Returns:
            bool: Returns True if the qualification is still valid, False if not
        """

        # Only check if there is an expiry date set
        if self.expiry is None:
            return True

        # Get current timestamp in the Sydney timezone
        now = arrow.now("Australia/Sydney")

        # Check if the expiry date is in the future
        return self.expiry.timestamp() > now.timestamp()

if __name__ == "__main__":
    pass
