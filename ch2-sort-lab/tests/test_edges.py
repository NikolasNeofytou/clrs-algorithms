"""
Test suite: test_edges.py
CLRS Chapter 2: Getting Started

These should pass after TODO 3.
Run with: pytest tests/test_edges.py -v
"""

import pytest
from src.types import TraceStep
from src.core import insertion_sort, merge_sort, traced_insertion_sort


# -- Edge cases for sorting (TODOs 1-2 must work first) -----------------------

class TestSortEdgeCases:
    """Edge cases that both algorithms must handle."""

    def test_empty_insertion(self):
        result, stats = insertion_sort([])
        assert result == []

    def test_empty_merge(self):
        result, stats = merge_sort([])
        assert result == []

    def test_single_insertion(self):
        result, _ = insertion_sort([99])
        assert result == [99]

    def test_single_merge(self):
        result, _ = merge_sort([99])
        assert result == [99]

    def test_two_elements_sorted(self):
        result_i, _ = insertion_sort([1, 2])
        result_m, _ = merge_sort([1, 2])
        assert result_i == [1, 2]
        assert result_m == [1, 2]

    def test_two_elements_unsorted(self):
        result_i, _ = insertion_sort([2, 1])
        result_m, _ = merge_sort([2, 1])
        assert result_i == [1, 2]
        assert result_m == [1, 2]

    def test_all_duplicates(self):
        data = [5, 5, 5, 5, 5]
        result_i, _ = insertion_sort(data[:])
        result_m, _ = merge_sort(data[:])
        assert result_i == [5, 5, 5, 5, 5]
        assert result_m == [5, 5, 5, 5, 5]

    def test_negative_numbers(self):
        data = [-3, 1, -7, 4, 0, -1]
        result_i, _ = insertion_sort(data[:])
        result_m, _ = merge_sort(data[:])
        assert result_i == sorted(data)
        assert result_m == sorted(data)

    def test_large_range(self):
        data = [1_000_000, -1_000_000, 0, 500_000, -500_000]
        result_i, _ = insertion_sort(data[:])
        result_m, _ = merge_sort(data[:])
        assert result_i == sorted(data)
        assert result_m == sorted(data)


# -- TestTracedInsertionSort (TODO 3) ------------------------------------------

class TestTracedInsertionSort:
    """Tests for traced_insertion_sort -- step-by-step execution."""

    def test_produces_sorted_output(self):
        """The traced version still sorts correctly."""
        result, trace = traced_insertion_sort([38, 27, 43, 3])
        assert result == [3, 27, 38, 43]

    def test_returns_trace_steps(self):
        """Returns a list of TraceStep objects."""
        result, trace = traced_insertion_sort([3, 1, 2])
        assert isinstance(trace, list)
        assert all(isinstance(step, TraceStep) for step in trace)

    def test_trace_length(self):
        """Should have n-1 trace steps (one per outer loop iteration)."""
        data = [5, 3, 8, 1, 9]
        _, trace = traced_insertion_sort(data)
        assert len(trace) == len(data) - 1

    def test_step_numbers_sequential(self):
        """Step numbers should be 1, 2, 3, ..."""
        _, trace = traced_insertion_sort([4, 2, 7, 1])
        for i, step in enumerate(trace):
            assert step.step_number == i + 1

    def test_final_state_is_sorted(self):
        """The array_state of the last trace step should be sorted."""
        data = [5, 3, 8, 1, 9, 2]
        _, trace = traced_insertion_sort(data)
        assert trace[-1].array_state == sorted(data)

    def test_each_step_has_description(self):
        """Every step should have a non-empty description."""
        _, trace = traced_insertion_sort([3, 1, 4, 1, 5])
        for step in trace:
            assert len(step.description) > 0

    def test_each_step_has_array_state(self):
        """Every step should have an array_state that's a valid permutation."""
        data = [9, 7, 5, 3, 1]
        _, trace = traced_insertion_sort(data)
        for step in trace:
            assert sorted(step.array_state) == sorted(data)

    def test_already_sorted(self):
        """Already sorted input: each step should note 'already in place' or similar."""
        result, trace = traced_insertion_sort([1, 2, 3, 4])
        assert result == [1, 2, 3, 4]
        assert len(trace) == 3

    def test_empty_input(self):
        """Empty input produces empty trace."""
        result, trace = traced_insertion_sort([])
        assert result == []
        assert trace == []

    def test_single_element(self):
        """Single element produces empty trace."""
        result, trace = traced_insertion_sort([42])
        assert result == [42]
        assert trace == []
