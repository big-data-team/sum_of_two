from myproject_eadishchev import diff_of_two


def test_two_minus_two() -> None:
    assert 0 == diff_of_two(2, 2)


def test_ten_minus_one() -> None:
    assert 9 == diff_of_two(10, 1)
