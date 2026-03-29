"""
Test suite: test_properties.py
CLRS Chapter 2: Getting Started

The final test: can your toolkit prove that merge sort beats
insertion sort on large inputs, and insertion sort wins on small
or nearly-sorted inputs? These test the full pipeline.

These should pass after TODO 5.
Run with: pytest tests/test_properties.py -v
"""

import pytest
from src.types import ComparisonReport, BenchmarkResult
from src.core import insertion_sort, merge_sort, compare


# -- TestComparisonReport (TODO 5) ---------------------------------------------

class TestComparisonReport:
    """Tests for the compare function -- full pipeline."""

    @pytest.fixture
    def report(self):
        return compare(
            insertion_sort, "insertion",
            merge_sort, "merge",
            sizes=[50, 200],
            input_types=["random", "sorted"],
        )

    def test_returns_comparison_report(self, report):
        """Output is a ComparisonReport instance."""
        assert isinstance(report, ComparisonReport)

    def test_algorithm_names(self, report):
        """Algorithm names are preserved."""
        assert report.algorithm_a == "insertion"
        assert report.algorithm_b == "merge"

    def test_result_counts_match(self, report):
        """Both result lists have the same length."""
        assert len(report.results_a) == len(report.results_b)

    def test_correct_number_of_results(self, report):
        """Should have len(sizes) x len(input_types) results per algorithm."""
        assert len(report.results_a) == 2 * 2  # 2 sizes x 2 types

    def test_same_inputs_tested(self, report):
        """Both algorithms tested on same (size, type) combinations."""
        for ra, rb in zip(report.results_a, report.results_b):
            assert ra.input_size == rb.input_size
            assert ra.input_type == rb.input_type

    def test_results_are_benchmark_results(self, report):
        """All results are BenchmarkResult instances."""
        for r in report.results_a + report.results_b:
            assert isinstance(r, BenchmarkResult)

    def test_both_algorithms_correct(self, report):
        """Both algorithms must have actually sorted (stats show work was done)."""
        for r in report.results_a + report.results_b:
            if r.input_size > 1 and r.input_type == "random":
                assert r.stats.comparisons > 0


class TestComparisonProperties:
    """The real test: do the algorithms behave as CLRS predicts?"""

    def test_merge_fewer_comparisons_on_large_random(self):
        """On large random input, merge sort uses fewer comparisons."""
        report = compare(
            insertion_sort, "insertion",
            merge_sort, "merge",
            sizes=[2000],
            input_types=["random"],
        )
        ins_comps = report.results_a[0].stats.comparisons
        merge_comps = report.results_b[0].stats.comparisons

        assert merge_comps < ins_comps, (
            f"Merge sort ({merge_comps:,} comparisons) should beat "
            f"insertion sort ({ins_comps:,}) on 2000 random elements"
        )

    def test_insertion_fewer_comparisons_on_sorted(self):
        """On already-sorted input, insertion sort uses fewer comparisons."""
        report = compare(
            insertion_sort, "insertion",
            merge_sort, "merge",
            sizes=[1000],
            input_types=["sorted"],
        )
        ins_comps = report.results_a[0].stats.comparisons
        merge_comps = report.results_b[0].stats.comparisons

        # Insertion sort on sorted: n-1 comparisons
        # Merge sort on sorted: ~n*log(n)/2 comparisons
        assert ins_comps < merge_comps, (
            f"Insertion sort ({ins_comps:,} comparisons) should beat "
            f"merge sort ({merge_comps:,}) on sorted input"
        )

    def test_merge_consistent_on_reverse(self):
        """Merge sort shouldn't be much worse on reverse vs random."""
        report = compare(
            insertion_sort, "insertion",
            merge_sort, "merge",
            sizes=[1000],
            input_types=["random", "reverse"],
        )
        merge_random = next(
            r for r in report.results_b if r.input_type == "random"
        )
        merge_reverse = next(
            r for r in report.results_b if r.input_type == "reverse"
        )

        ratio = merge_reverse.stats.comparisons / max(merge_random.stats.comparisons, 1)
        # Should be within 1.5x (merge sort is not very input-sensitive)
        assert ratio < 1.5, f"Merge sort ratio reverse/random = {ratio:.2f}, expected < 1.5"

    def test_insertion_worst_on_reverse(self):
        """Insertion sort is worst on reverse input."""
        report = compare(
            insertion_sort, "insertion",
            merge_sort, "merge",
            sizes=[500],
            input_types=["random", "sorted", "reverse"],
        )
        ins_results = {r.input_type: r for r in report.results_a}

        assert ins_results["reverse"].stats.comparisons > ins_results["random"].stats.comparisons
        assert ins_results["sorted"].stats.comparisons < ins_results["random"].stats.comparisons

    def test_fair_comparison_same_data(self):
        """Both algorithms must get the same input (fairness check).
        We verify indirectly: both should produce the same number of elements."""
        report = compare(
            insertion_sort, "insertion",
            merge_sort, "merge",
            sizes=[100],
            input_types=["random"],
        )
        # Both tested on size 100
        assert report.results_a[0].input_size == 100
        assert report.results_b[0].input_size == 100
