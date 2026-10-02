import pytest


@pytest.mark.parametrize(
    "s, expected",
    [
        ("Hello", "hello"),
        ("here", "here"),
        ("LOVELY", "lovely"),
        ("123 ABC!", "123 abc!"),
    ],
)
def test_to_lower_case(solution, s, expected):
    assert solution.toLowerCase(s) == expected
