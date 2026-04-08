from blogger import qmarks


def test_qmarks_int():
    assert qmarks(1) == "?"
    assert qmarks(2) == "?, ?"
    assert qmarks(3) == "?, ?, ?"


def test_qmarks_list():
    assert qmarks(["path", "atime"]) == "?, ?"
    assert qmarks(["a", "b", "c"]) == "?, ?, ?"


def test_qmarks_str():
    assert qmarks("path, atime") == "?, ?"
    assert qmarks("a, b, c") == "?, ?, ?"


def test_qmarks_single_field_str():
    assert qmarks("path") == "?"
