from frontend.parsers import (
    parse_amount,
    parse_choice,
    parse_index,
    parse_list,
    parse_name,
    parse_positive_amount,
    parse_text,
    parse_yes_no,
)

def test_parse_amount_handles_numbers_and_invalid_text():
    assert parse_amount(" 42 ") == 42
    assert parse_amount("abc") is None


def test_parse_list_handles_valid_and_invalid_values():
    assert parse_list("10 5 3") == [10, 5, 3]
    assert parse_list("10 -5 3") is None
    assert parse_list("10 x 3") is None


def test_parse_positive_amount_requires_positive_number():
    assert parse_positive_amount("7") == 7
    assert parse_positive_amount("0") is None
    assert parse_positive_amount("-3") is None


def test_parse_name_rejects_invalid_names():
    assert parse_name("pushups") == "Pushups"
    assert parse_name("push ups") is None
    assert parse_name("pushups1") is None


def test_parse_index_returns_zero_based_or_none():
    assert parse_index("3") == 2
    assert parse_index("0") is None


def test_parse_choice_checks_allowed_choices():
    assert parse_choice("2", [1, 2, 3]) == 2
    assert parse_choice("5", [1, 2, 3]) is None


def test_parse_text_returns_none_for_blank_input():
    assert parse_text("  hello ") == "hello"
    assert parse_text("   ") is None


def test_parse_yes_no_accepts_common_inputs():
    assert parse_yes_no("yes") is True
    assert parse_yes_no("y") is True
    assert parse_yes_no("n") is False
    assert parse_yes_no("maybe") is None
