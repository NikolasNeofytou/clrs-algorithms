"""
Test suite: test_hard.py
CLRS Chapter 2: Getting Started

Remember feel_the_problem.py? Selection sort was painfully slow.
These tests verify your benchmark runner can quantify that pain
and prove merge sort's superiority.

These should pass after TODO 4.
Run with: pytest tests/test_hard.py -v
"""

import pytest
from src.types import BenchmarkResult, SortStats
from src.core import insertion_sort, merge_sort, benchmark


# -- TestBenchmark (TODO 4) ----------------------------------------------------

class TestBenchmark:
    """Tests for the benchmark runner."""

    def test_returns_results(self):
        """Benchmark returns a list of BenchmarkResult."""
        results = benchmark(insertion_sort, "insertion", [10, 20], ["random"])
        assert isinstance(results, list)
        assert all(isinstance(r, BenchmarkResult) for r in results)

    def test_correct_count(self):
        """Number of results = len(sizes) x len(input_types)."""
        sizes = [10, 50, 100]
        types = ["random", "sorted"]
        results = benchmark(insertion_sort, "insertion", sizes, types)
        assert len(results) == len(sizes) * len(types)

    def test_algorithm_name(self):
        """Algorithm name is preserved in results."""
        results = benchmark(merge_sort, "merge", [10], ["random"])
        assert all(r.algorithm == "merge" for r in results)

    def test_input_size_recorded(self):
        """Input size is correctly recorded."""
        results = benchmark(insertion_sort, "insertion", [100, 500], ["random"])
        sizes = {r.input_size for r in results}
        assert sizes == {100, 500}

    def test_input_type_recorded(self):
        """Input type is correctly recorded."""
        results = benchmark(
            merge_sort, "merge", [50], ["random", "sorted", "reverse"]
        )
        types = {r.input_type for r in results}
        assert types == {"random", "sorted", "reverse"}

    def test_wall_time_positive(self):
        """Wall time should be positive for non-trivial input."""
        results = benchmark(insertion_sort, "insertion", [1000], ["random"])
        assert results[0].wall_time_seconds > 0

    def test_stats_populated(self):
        """Stats should have non-zero comparisons for unsorted input."""
        results = benchmark(insertion_sort, "insertion", [100], ["random"])
        assert results[0].stats.comparisons > 0

    def test_sorted_input_fast_for_insertion(self):
        """Insertion sort on sorted input should be fast (few operations)."""
        results = benchmark(
            insertion_sort, "insertion", [1000], ["sorted", "reverse"]
        )
        sorted_result = next(r for r in results if r.input_type == "sorted")
        reverse_result = next(r for r in results if r.input_type == "reverse")

        # Sorted input: O(n) comparisons. Reverse: O(n^2).
        assert sorted_result.stats.comparisons < reverse_result.stats.comparisons

    def test_merge_sort_consistent_across_types(self):
        """Merge sort comparison count should be similar regardless of input type."""
        results = benchmark(
            merge_sort, "merge", [1000], ["random", "sorted", "reverse"]
        )
        comp_counts = [r.stats.comparisons for r in results]

        # All within 2x of each other (merge sort is not input-sensitive)
        assert max(comp_counts) < 2 * min(comp_counts)

    def test_growth_rate_insertion(self):
        """Insertion sort on random data: doubling n should ~quadruple comparisons."""
        results = benchmark(
            insertion_sort, "insertion", [500, 1000], ["random"]
        )
        small = next(r for r in results if r.input_size == 500)
        large = next(r for r in results if r.input_size == 1000)

        ratio = large.stats.comparisons / max(small.stats.comparisons, 1)
        # For O(n^2): ratio should be around 4 (2^2). Allow 2.5-6 range.
        assert 2.5 <= ratio <= 6.0, f"Ratio was {ratio:.1f}, expected ~4 for O(n^2)"

    def test_growth_rate_merge(self):
        """Merge sort: doubling n should roughly double comparisons (plus log factor)."""
        results = benchmark(
            merge_sort, "merge", [500, 1000], ["random"]
        )
        small = next(r for r in results if r.input_size == 500)
        large = next(r for r in results if r.input_size == 1000)

        ratio = large.stats.comparisons / max(small.stats.comparisons, 1)
        # For O(n log n): ratio should be around 2.1-2.3. Allow 1.5-3.0.
        assert 1.5 <= ratio <= 3.0, f"Ratio was {ratio:.1f}, expected ~2.2 for O(n log n)"
