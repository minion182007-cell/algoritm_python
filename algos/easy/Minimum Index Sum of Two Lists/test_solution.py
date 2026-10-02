import pytest


@pytest.mark.parametrize(
    "list1, list2, expected",
    [
        (
            ["Shogun", "Tapioca Express", "Burger King", "KFC"],
            ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"],
            ["Shogun"],
        ),
        (
            ["Shogun", "Tapioca Express", "Burger King", "KFC"],
            ["KFC", "Shogun", "Burger King"],
            ["Shogun"],
        ),
        (["happy", "sad", "good"], ["sad", "happy", "good"], ["sad", "happy"]),
        (["a"], ["a"], ["a"]),
    ],
)
def test_find_restaurant(solution, list1, list2, expected):
    assert sorted(solution.findRestaurant(list1, list2)) == sorted(expected)
