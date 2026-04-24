"""Tests for homework1 — LinkedList addSecond / removeSecond.

Run with:
    STUDENT=priansh pytest tests/test_homework1.py -v
    STUDENT=devarshi pytest tests/test_homework1.py -v
"""


def _to_list(ll):
    out = []
    node = ll.head
    while node is not None:
        out.append(node.data)
        node = node.next
    return out


def _build(hw1, values):
    ll = hw1.LinkedList()
    for v in reversed(values):
        ll.addToFront(v)
    return ll


class TestAddSecond:
    def test_into_empty_list(self, hw1):
        ll = hw1.LinkedList()
        ll.addSecond(10)
        assert _to_list(ll) == [10]

    def test_into_single_element_list(self, hw1):
        ll = _build(hw1, [5])
        ll.addSecond(10)
        assert _to_list(ll) == [5, 10]

    def test_into_multi_element_list(self, hw1):
        ll = _build(hw1, [5, 3, 8])
        ll.addSecond(10)
        assert _to_list(ll) == [5, 10, 3, 8]

    def test_preserves_tail(self, hw1):
        ll = _build(hw1, [1, 2, 3, 4])
        ll.addSecond(99)
        assert _to_list(ll) == [1, 99, 2, 3, 4]


class TestRemoveSecond:
    def test_from_empty_list_returns_none(self, hw1):
        ll = hw1.LinkedList()
        assert ll.removeSecond() is None

    def test_from_single_element_returns_none(self, hw1):
        ll = _build(hw1, [5])
        assert ll.removeSecond() is None
        assert _to_list(ll) == [5]

    def test_from_two_element_list(self, hw1):
        ll = _build(hw1, [5, 10])
        assert ll.removeSecond() == 10
        assert _to_list(ll) == [5]

    def test_from_multi_element_list(self, hw1):
        ll = _build(hw1, [5, 10, 3, 8])
        assert ll.removeSecond() == 10
        assert _to_list(ll) == [5, 3, 8]


class TestCombined:
    def test_round_trip_matches_lesson_example(self, hw1):
        ll = _build(hw1, [5, 3, 8])
        assert _to_list(ll) == [5, 3, 8]

        ll.addSecond(10)
        assert _to_list(ll) == [5, 10, 3, 8]

        assert ll.removeSecond() == 10
        assert _to_list(ll) == [5, 3, 8]
