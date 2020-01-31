from microsila_py import demo


def test_cmp():
    assert demo.cmp(2, 2)
    assert not demo.cmp(2, 3)
