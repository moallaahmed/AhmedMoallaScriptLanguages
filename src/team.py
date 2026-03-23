team_members = ["Ahmed Moalla"]


def get_team():
    return team_members


def count_members():
    return len(team_members)


def add_member(name):
    team_members.append(name)
