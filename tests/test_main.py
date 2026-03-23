from src.main import count_members, format_greeting


def test_count_members():
    members = ["Ahmed Moalla"]
    assert count_members(members) == 1


def test_format_greeting():
    assert format_greeting("Ahmed") == "Hello, Ahmed!"
