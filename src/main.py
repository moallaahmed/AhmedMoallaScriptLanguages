from team import get_team, count_members
from utils import format_greeting


def display_team(members):
    print("Team members:")
    for member in members:
        print("-", member)


if __name__ == "__main__":
    members = get_team()
    display_team(members)
    print("Number of members:", count_members())
    print(format_greeting("Ahmed"))
