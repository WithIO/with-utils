from wutils.iter import n_grams, return_list


def test_n_grams():
    assert [*n_grams(range(1), 2)] == []
    assert [*n_grams(range(3), 2)] == [(0, 1), (1, 2)]
    assert [*n_grams(range(4), 2)] == [(0, 1), (1, 2), (2, 3)]
    assert [*n_grams(range(4), 3)] == [(0, 1, 2), (1, 2, 3)]


def test_return_list():
    @return_list
    def foo():
        yield 1
        yield 2
        yield 3

    assert foo() == [1, 2, 3]
