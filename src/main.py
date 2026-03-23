import argparse
from team import get_team, count_members
from utils import format_greeting


def display_team(members):
    for member in members:
        print("-", member["name"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Team CLI")

    parser.add_argument("--show-team", action="store_true", help="Show team members")
    parser.add_argument("--count", action="store_true", help="Count members")
    parser.add_argument("--greet", type=str, help="Greet a person")

    args = parser.parse_args()

    if args.show_team:
        members = get_team()
        display_team(members)

    elif args.count:
        print(count_members())

    elif args.greet:
        print(format_greeting(args.greet))

    else:
        print("No argument provided. Use --help")
