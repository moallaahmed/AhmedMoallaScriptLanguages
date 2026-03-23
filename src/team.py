team_members = [
    {"name": "Ahmed Moalla"}
]


def get_team():
    return team_members


def count_members():
    return len(team_members)


def add_member(name):
    team_members.append({"name": name})


def find_member(name):
    for member in team_members:
        if member["name"] == name:
            return member
    return None
