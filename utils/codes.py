import json
import os


def get_qualifications(path: str = "data/qualifications.json") -> list[object]:
    """Return array of qualification data

    Returns:
            list[object]: Array of qualification data
    """

    if os.path.exists(path) == False:
        print("No qualifications.json file found")
        return []

    data = json.load(open(path))

    return data


if __name__ == "__main__":
    pass
