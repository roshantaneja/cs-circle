"""Tests for homework1 — Dictionaries and Stacks.

Run with:
    STUDENT=priansh pytest tests/test_homework1.py -v
    STUDENT=devarshi pytest tests/test_homework1.py -v
"""
import pytest


# ── helpers ──────────────────────────────────────────────────────────────────

def wc(hw1, words):
    return hw1.word_count(words)

def stack(hw1):
    return hw1.Stack()


# ── Part 1: word_count ───────────────────────────────────────────────────────

class TestWordCount:
    def test_empty_list(self, hw1):
        assert wc(hw1, []) == {}

    def test_single_word(self, hw1):
        assert wc(hw1, ["hello"]) == {"hello": 1}

    def test_all_unique(self, hw1):
        assert wc(hw1, ["a", "b", "c"]) == {"a": 1, "b": 1, "c": 1}

    def test_repeated_word(self, hw1):
        assert wc(hw1, ["x", "x", "x"]) == {"x": 3}

    def test_mixed_counts(self, hw1):
        result = wc(hw1, ["apple", "banana", "apple", "cherry", "banana", "apple"])
        assert result == {"apple": 3, "banana": 2, "cherry": 1}

    def test_case_sensitive(self, hw1):
        # "Apple" and "apple" are different words
        result = wc(hw1, ["Apple", "apple", "APPLE"])
        assert result == {"Apple": 1, "apple": 1, "APPLE": 1}

    def test_returns_new_dict(self, hw1):
        # should return a dict, not None
        result = wc(hw1, ["a"])
        assert isinstance(result, dict)

    def test_does_not_mutate_input(self, hw1):
        words = ["a", "b", "a"]
        original = words[:]
        wc(hw1, words)
        assert words == original


# ── Part 1: flip ─────────────────────────────────────────────────────────────

class TestFlip:
    def test_empty_dict(self, hw1):
        assert hw1.flip({}) == {}

    def test_single_pair(self, hw1):
        assert hw1.flip({"a": 1}) == {1: "a"}

    def test_string_keys_int_values(self, hw1):
        assert hw1.flip({"a": 1, "b": 2, "c": 3}) == {1: "a", 2: "b", 3: "c"}

    def test_int_keys_string_values(self, hw1):
        assert hw1.flip({1: "x", 2: "y"}) == {"x": 1, "y": 2}

    def test_returns_new_dict(self, hw1):
        original = {"a": 1}
        result = hw1.flip(original)
        assert isinstance(result, dict)
        # original should not be modified
        assert original == {"a": 1}

    def test_flipping_twice_is_identity(self, hw1):
        d = {"a": 1, "b": 2, "c": 3}
        assert hw1.flip(hw1.flip(d)) == d


# ── Part 2: Stack ─────────────────────────────────────────────────────────────

class TestStack:
    def test_new_stack_is_empty(self, hw1):
        s = stack(hw1)
        assert s.is_empty() is True

    def test_size_of_new_stack_is_zero(self, hw1):
        s = stack(hw1)
        assert s.size() == 0

    def test_push_makes_nonempty(self, hw1):
        s = stack(hw1)
        s.push(1)
        assert s.is_empty() is False

    def test_size_increases_on_push(self, hw1):
        s = stack(hw1)
        s.push("a")
        assert s.size() == 1
        s.push("b")
        assert s.size() == 2
        s.push("c")
        assert s.size() == 3

    def test_pop_returns_last_pushed(self, hw1):
        s = stack(hw1)
        s.push(10)
        assert s.pop() == 10

    def test_lifo_order(self, hw1):
        s = stack(hw1)
        s.push(1)
        s.push(2)
        s.push(3)
        assert s.pop() == 3
        assert s.pop() == 2
        assert s.pop() == 1

    def test_pop_decreases_size(self, hw1):
        s = stack(hw1)
        s.push("x")
        s.push("y")
        s.pop()
        assert s.size() == 1

    def test_pop_until_empty(self, hw1):
        s = stack(hw1)
        s.push(1)
        s.push(2)
        s.pop()
        s.pop()
        assert s.is_empty() is True
        assert s.size() == 0

    def test_pop_from_empty_raises(self, hw1):
        s = stack(hw1)
        with pytest.raises(IndexError, match="pop from empty stack"):
            s.pop()

    def test_peek_returns_top_without_removing(self, hw1):
        s = stack(hw1)
        s.push(42)
        assert s.peek() == 42
        assert s.size() == 1  # still there

    def test_peek_after_multiple_pushes(self, hw1):
        s = stack(hw1)
        s.push(1)
        s.push(2)
        s.push(3)
        assert s.peek() == 3
        assert s.size() == 3

    def test_peek_from_empty_raises(self, hw1):
        s = stack(hw1)
        with pytest.raises(IndexError, match="peek at empty stack"):
            s.peek()

    def test_uses_data_attribute(self, hw1):
        # implementation must use self._data
        s = stack(hw1)
        s.push("hello")
        assert hasattr(s, "_data")
        assert "hello" in s._data

    def test_push_pop_interleaved(self, hw1):
        s = stack(hw1)
        s.push(1)
        s.push(2)
        assert s.pop() == 2
        s.push(3)
        assert s.pop() == 3
        assert s.pop() == 1
        assert s.is_empty() is True


# ── Part 2: is_balanced ───────────────────────────────────────────────────────

class TestIsBalanced:
    def test_empty_string(self, hw1):
        assert hw1.is_balanced("") is True

    def test_no_brackets(self, hw1):
        assert hw1.is_balanced("hello world") is True

    def test_single_parens(self, hw1):
        assert hw1.is_balanced("()") is True

    def test_single_square(self, hw1):
        assert hw1.is_balanced("[]") is True

    def test_single_curly(self, hw1):
        assert hw1.is_balanced("{}") is True

    def test_nested(self, hw1):
        assert hw1.is_balanced("([{}])") is True

    def test_sequential(self, hw1):
        assert hw1.is_balanced("()[]{}") is True

    def test_complex_valid(self, hw1):
        assert hw1.is_balanced("({[]})([]){()}") is True

    def test_mixed_with_text(self, hw1):
        assert hw1.is_balanced("hello (world [foo] {bar})") is True

    def test_wrong_close_order(self, hw1):
        assert hw1.is_balanced("([)]") is False

    def test_mismatched_types(self, hw1):
        assert hw1.is_balanced("(}") is False

    def test_unmatched_open(self, hw1):
        assert hw1.is_balanced("(") is False

    def test_unmatched_close(self, hw1):
        assert hw1.is_balanced(")") is False

    def test_extra_close(self, hw1):
        assert hw1.is_balanced("())") is False

    def test_extra_open(self, hw1):
        assert hw1.is_balanced("(()") is False

    def test_deeply_nested_valid(self, hw1):
        assert hw1.is_balanced("((((((()))))))") is True

    def test_deeply_nested_invalid(self, hw1):
        assert hw1.is_balanced("(((((())))))") is False  # one extra open

    def test_returns_bool(self, hw1):
        result = hw1.is_balanced("()")
        assert isinstance(result, bool)
