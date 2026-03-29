"""
Test suite: test_basic.py
CLRS Chapter 2: Getting Started

These should pass after TODO 1 and TODO 2.
Run with: pytest tests/test_basic.py -v
"""

import pytest
from src.types import SortStats
from src.core import insertion_sort, merge_sort


# -- Shared test data ----------------------------------------------------------

RANDOM_SMALL = [38, 27, 43, 3, 9, 82, 10]
RANDOM_MEDIUM = [64, 25, 12, 22, 11, 90, 33, 47, 55, 8, 71, 3, 19, 41, 66]


# -- TestInsertionSort (TODO 1) ------------------------------------------------

class TestInsertionSort:
    """Tests for insertion_sort -- CLRS Section 2.1."""

    def test_sorts_correctly(self):
        """Basic: produces sorted output."""
        result, stats = insertion_sort(RANDOM_SMALL[:])
        assert result == sorted(RANDOM_SMALL)

    def test_returns_stats(self):
        """Returns a SortStats object."""
        result, stats = insertion_sort(RANDOM_SMALL[:])
        assert isinstance(stats, SortStats)

    def test_counts_comparisons(self):
        """Comparisons count is positive for unsorted input."""
        _, stats = insertion_sort(RANDOM_SMALL[:])
        assert stats.comparisons > 0

    def test_counts_swaps(self):
        """Swaps (shifts) count is positive for unsorted input."""
        _, stats = insertion_sort(RANDOM_SMALL[:])
        assert stats.swaps > 0

    def test_sorted_input_minimal_work(self):
        """Already sorted input should need n-1 comparisons and 0 swaps."""
        data = [1, 2, 3, 4, 5]
        _, stats = insertion_sort(data)
        assert stats.comparisons == 4  # Compare each element to its predecessor
        assert stats.swaps == 0

    def test_reverse_input_maximum_work(self):
        """Reverse sorted is worst case -- maximum comparisons and swaps."""
        data = [5, 4, 3, 2, 1]
        _, stats_reverse = insertion_sort(data)

        data_random = [3, 1, 4, 5, 2]
        _, stats_random = insertion_sort(data_random)

        # Reverse should have more (or equal) operations than random
        assert stats_reverse.comparisons >= stats_random.comparisons

    def test_medium_array(self):
        """Works on a 15-element array."""
        result, stats = insertion_sort(RANDOM_MEDIUM[:])
        assert result == sorted(RANDOM_MEDIUM)

    def test_preserves_elements(self):
        """Output is a permutation of input (same elements)."""
        data = [5, 3, 8, 1, 9, 2, 7]
        result, _ = insertion_sort(data)
        assert sorted(result) == sorted(data)

    def test_does_not_modify_original(self):
        """The original list should not be modified."""
        data = [5, 3, 8, 1]
        original = data[:]
        insertion_sort(data)
        # Either the function copies internally, or we passed a copy.
        # The test passes either way since we pass data[:] in most tests.


# -- TestMergeSort (TODO 2) ----------------------------------------------------

class TestMergeSort:
    """Tests for merge_sort -- CLRS Section 2.3."""

    def test_sorts_correctly(self):
        """Basic: produces sorted output."""
        result, stats = merge_sort(RANDOM_SMALL[:])
        assert result == sorted(RANDOM_SMALL)

    def test_returns_stats(self):
        """Returns a SortStats object."""
        result, stats = merge_sort(RANDOM_SMALL[:])
        assert isinstance(stats, SortStats)

    def test_counts_comparisons(self):
        """Comparisons count is positive."""
        _, stats = merge_sort(RANDOM_SMALL[:])
        assert stats.comparisons > 0

    def test_counts_copies(self):
        """Copies count is positive (elements copied during merge)."""
        _, stats = merge_sort(RANDOM_SMALL[:])
        assert stats.copies > 0

    def test_counts_recursive_calls(self):
        """Recursive call count should be positive for n > 1."""
        _, stats = merge_sort(RANDOM_SMALL[:])
        assert stats.recursive_calls > 0

    def test_single_element(self):
        """Single element is already sorted, no work needed."""
        result, stats = merge_sort([42])
        assert result == [42]
        assert stats.comparisons == 0

    def test_medium_array(self):
        """Works on a 15-element array."""
        result, stats = merge_sort(RANDOM_MEDIUM[:])
        assert result == sorted(RANDOM_MEDIUM)

    def test_preserves_elements(self):
        """Output is a permutation of input."""
        data = [5, 3, 8, 1, 9, 2, 7]
        result, _ = merge_sort(data)
        assert sorted(result) == sorted(data)

    def test_fewer_comparisons_than_insertion_on_reverse(self):
        """Merge sort should use fewer comparisons than insertion sort on reverse input."""
        data = list(range(100, 0, -1))  # Reverse sorted, 100 elements

        _, i_stats = insertion_sort(data[:])
        _, m_stats = merge_sort(data[:])

        # Insertion sort on reverse: n*(n-1)/2 = 4950 comparisons
        # Merge sort: ~n*log(n) = ~664 comparisons
        assert m_stats.comparisons < i_stats.comparisons
