import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_data",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (10000, 10000, [2496, 1997]),
        (9999, 9999, [2495, 1997]),
        (-1, 10, [0, 0]),
        (10, -1, [0, 0])
    ]
)
def test_get_human_age_with_correct_data(
        cat_age: int, dog_age: int,
        expected_data: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_data


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("10", 10),
        (10, "10"),
        (None, 10),
        (10, None)
    ]
)
def test_get_human_age_with_invalid_types(
        cat_age: int,
        dog_age: int
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
