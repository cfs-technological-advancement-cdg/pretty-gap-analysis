from models.member import Member


def process_ignore_list(members: list[Member], ignore: str) -> list[Member]:
    """Processes the ignore list and removes members from the members list

    Args:
            members (list[Member]): List of members to process
            ignore (str): Comma separated list of member numbers to ignore

    Returns:
            list[Member]: List of members with members removed
    """

    # If ignore list is empty, return members
    if ignore is None:
        return members

    # Split ignore list into array and convert numbers to ints
    ignore_list = ignore.split(",")
    ignore_list = list(map(lambda i: int(i), ignore_list))

    # filter out members that are in the ignore list
    members = list(filter(lambda i: i.id not in ignore_list, members))

    return members
