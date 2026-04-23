from myproject_eadishchev import sum_of_two


def test_one_plus_zero() -> None:
    assert 1 == sum_of_two(1, 0)


def test_two_plus_two() -> None:
    assert 4 == sum_of_two(2, 2)
