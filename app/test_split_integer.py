from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    function = split_integer(6, 2)
    assert function == [3, 3]


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    function = split_integer(17, 4)
    assert function == [4, 4, 4, 5]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    function = split_integer(8, 1)
    assert function == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    function = split_integer(32, 6)
    assert function == [5, 5, 5, 5, 6, 6]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    function = split_integer(1, 4)
    assert function == [0, 0, 0, 1]
