team_name = "Solo Project"
team_members = ["Ahmed Moalla"]

def count_members(members):
    return len(members)


def format_greeting(name):
    return f"Hello, {name}!"


def display_team(name, members):
    print("Team name:", name)
    print("Team members:")
    for member in members:
        print("-", member)


if __name__ == "__main__":
    display_team(team_name, team_members)
    print("Number of members:", count_members(team_members))
    print(format_greeting("Ahmed"))
    print("The project runs correctly.")
