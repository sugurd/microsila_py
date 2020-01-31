from microsila_py import demo
from microsila_py.demo import MyDemoClass


def test_cmp():
    assert demo.cmp(2, 2)
    assert not demo.cmp(2, 3)


def test_get_friends():
    dc = MyDemoClass()
    friends = dc.get_friends()
    print(f"My friends: {friends!r}")
    assert len(friends) >= 3
