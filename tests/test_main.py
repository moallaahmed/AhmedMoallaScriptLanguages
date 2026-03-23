from src.team import count_members, add_member, find_member


def test_count_members():
    assert count_members() >= 1


def test_add_member():
    add_member("Test User")
    assert find_member("Test User") is not None


def test_find_member():
    assert find_member("Ahmed Moalla") is not None


def test_find_nonexistent():
    assert find_member("Unknown") is None
