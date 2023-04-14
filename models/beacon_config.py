from dataclasses import dataclass, field

from models.qualification import Qualification


@dataclass
class BeaconConfig:
    username: str
    password: str
    environment: str = "trainbeacon"

    def get_url(self) -> str:
        return f"https://{self.environment}.beacon.ses.nsw.gov.au"

    def get_api_url(self) -> str:
        return f"https://api{self.environment}.beacon.ses.nsw.gov.au"
