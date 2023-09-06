from lib.factory import serializer


def assert_restored_object(subject):
    for language in serializer.get_formats():
        parser = serializer.get_parser(language)
        serialized = parser.dumps(subject)
        restored = parser.loads(serialized)
        assert restored == subject


def test_none():
    subject = None
    assert_restored_object(subject)


def test_false():
    subject = False
    assert_restored_object(subject)


def test_true():
    subject = True
    assert_restored_object(subject)


def test_int():
    subject = -999
    assert_restored_object(subject)


def test_float():
    subject = 22 / 7
    assert_restored_object(subject)


def test_str():
    subject = "TesT sTriNg3432#"
    assert_restored_object(subject)


def test_list():
    subject = [10, 30, 20]
    assert_restored_object(subject)


def test_dict():
    subject = {10: 20, 30: 40}
    assert_restored_object(subject)
