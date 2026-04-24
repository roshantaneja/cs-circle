# Homework 1 — Dictionaries and Stacks
# Fill in each function/method below. Do not change any function signatures.
# Run your tests with: ./check.sh devarshi

# ── PART 1: DICTIONARIES ────────────────────────────────────────────────────

def word_count(words):
    """Given a list of words, return a dict mapping each word to the number
    of times it appears.

    Examples:
        word_count(["apple", "banana", "apple", "cherry", "banana", "apple"])
        → {"apple": 3, "banana": 2, "cherry": 1}

        word_count([])
        → {}
    """
    pass


def flip(d):
    """Given a dictionary, return a new dict with keys and values swapped.
    You can assume all values are unique (no two keys share the same value).

    Examples:
        flip({"a": 1, "b": 2, "c": 3})
        → {1: "a", 2: "b", 3: "c"}

        flip({})
        → {}
    """
    pass


# ── PART 2: STACKS ──────────────────────────────────────────────────────────

class Stack:
    """A last-in, first-out (LIFO) stack backed by a Python list.

    Think of it like a stack of plates — you always add and remove from the top.
    """

    def __init__(self):
        self._data = []  # store items here — don't add other instance variables

    def push(self, item):
        """Add item to the top of the stack."""
        pass

    def pop(self):
        """Remove and return the top item.
        Raise IndexError("pop from empty stack") if the stack is empty.
        """
        pass

    def peek(self):
        """Return the top item without removing it.
        Raise IndexError("peek at empty stack") if the stack is empty.
        """
        pass

    def is_empty(self):
        """Return True if the stack has no items, False otherwise."""
        pass

    def size(self):
        """Return the number of items in the stack."""
        pass


def is_balanced(s):
    """Return True if every opening bracket in s has a matching closing
    bracket in the correct order, False otherwise.

    Only these bracket pairs count: () [] {}
    All other characters should be ignored.

    Hint: use your Stack class above.

    Examples:
        is_balanced("([]{})")  → True
        is_balanced("([)]")    → False
        is_balanced("")        → True
        is_balanced("hello")   → True   (no brackets — trivially balanced)
        is_balanced("(")       → False
        is_balanced(")")       → False
    """
    pass
