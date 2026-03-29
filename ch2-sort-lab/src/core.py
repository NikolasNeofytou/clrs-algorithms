"""
Module: core
Purpose: Sorting algorithms -- this is where YOU build the logic.
Chapter Reference: CLRS Ch 2 (Sections 2.1, 2.2, 2.3)

This module contains 5 TODOs that progressively build a complete
sorting toolkit. Work through them in order, running tests after each.

Concepts you'll implement:
  - Insertion sort with operation counting (Section 2.1)
  - Merge sort with operation counting (Section 2.3)
  - Execution tracing (step-by-step visualization)
  - Benchmarking on different input types
  - Comparison reporting
"""

from src.types import (
    SortStats,
    TraceStep,
    BenchmarkResult,
    ComparisonReport,
)
from src.utils import (
    time_sort,
    INPUT_GENERATORS,
)


# -- TODO 1: Insertion Sort ----------------------------------------------------
#
# Implement insertion sort as described in CLRS Section 2.1.
#
# The algorithm maintains a sorted subarray in positions [0..i-1].
# For each new element at position i, it "inserts" it into the correct
# position by shifting larger elements to the right.
#
# You MUST count operations:
#   - comparisons: every time you compare two elements
#   - swaps: every time you shift (move) an element one position right
#
# Input: a list of integers (sort in-place or copy -- your choice)
# Output: tuple of (sorted_list, SortStats)
#
# Hint: The inner loop shifts elements right until the correct insertion
#       point is found. Each shift is one "swap" in your count.
#       Each comparison in the while/for condition counts as one comparison.
#
# After this works, tests in test_basic.py::TestInsertionSort should pass.

def insertion_sort(arr: list[int]) -> tuple[list[int], SortStats]:
    """Sort using insertion sort. Return (sorted_list, stats)."""
    # TODO 1: your implementation here
    raise NotImplementedError("TODO 1: implement insertion sort")


# -- TODO 2: Merge Sort --------------------------------------------------------
#
# Implement merge sort as described in CLRS Section 2.3.
#
# The algorithm divides the array in half, recursively sorts each half,
# then merges the two sorted halves.
#
# You MUST count operations:
#   - comparisons: every time you compare elements during merge
#   - copies: every time you copy an element (to temp arrays or back)
#   - recursive_calls: every time merge_sort calls itself
#
# You need TWO functions:
#   1. merge(left, right, stats) -> merged_list
#      Merges two sorted lists into one sorted list, updating stats.
#   2. merge_sort(arr) -> (sorted_list, SortStats)
#      The main function that divides, recurses, and merges.
#
# Hint: The merge step walks through both halves with two pointers.
#       Each element comparison is one comparison; each element placed
#       into the result is one copy.
#
# After this works, tests in test_basic.py::TestMergeSort should pass.

def merge(left: list[int], right: list[int], stats: SortStats) -> list[int]:
    """Merge two sorted lists into one sorted list. Update stats in-place."""
    # TODO 2a: your implementation here
    raise NotImplementedError("TODO 2: implement merge")


def merge_sort(arr: list[int]) -> tuple[list[int], SortStats]:
    """Sort using merge sort. Return (sorted_list, stats)."""
    # TODO 2b: your implementation here
    raise NotImplementedError("TODO 2: implement merge sort")


# -- TODO 3: Execution Tracer --------------------------------------------------
#
# Implement a traced version of insertion sort that records every step.
#
# For each iteration of the outer loop, record a TraceStep with:
#   - step_number: which iteration (1-indexed)
#   - operation: "insert" 
#   - description: what happened, e.g.,
#       "Inserted 3 at position 1 (shifted 2 elements)"
#       or "Element 7 already in place at position 3"
#   - array_state: a COPY of the array after this step
#
# Input: a list of integers
# Output: tuple of (sorted_list, list[TraceStep])
#
# Hint: This is insertion sort again, but with logging. Each outer loop
#       iteration produces one TraceStep. The description should say
#       what element was inserted, where, and how many shifts happened.
#
# After this works, tests in test_edges.py should pass.

def traced_insertion_sort(arr: list[int]) -> tuple[list[int], list[TraceStep]]:
    """Insertion sort with step-by-step trace. Return (sorted_list, trace)."""
    # TODO 3: your implementation here
    raise NotImplementedError("TODO 3: implement traced insertion sort")


# -- TODO 4: Benchmark Runner --------------------------------------------------
#
# Implement a function that benchmarks a sort algorithm on multiple
# input types and sizes.
#
# For each (size, input_type) combination:
#   1. Generate input data using INPUT_GENERATORS[input_type](size)
#   2. Time the sort using time_sort() from utils
#   3. Record a BenchmarkResult
#
# Input:
#   - sort_func: a function with signature (list[int]) -> (list[int], SortStats)
#   - algorithm_name: string name for labeling
#   - sizes: list of input sizes to test, e.g., [100, 1000, 5000]
#   - input_types: list of input type names, e.g., ["random", "sorted", "reverse"]
#
# Output: list of BenchmarkResult (one per size x input_type combination)
#
# Hint: Use INPUT_GENERATORS dict from utils to get the generator function
#       for each input_type. Use time_sort() to handle timing.
#       Iterate sizes first, then input_types within each size (this gives
#       a natural grouping in the output).
#
# After this works, tests in test_hard.py should pass.

def benchmark(
    sort_func,
    algorithm_name: str,
    sizes: list[int],
    input_types: list[str],
) -> list[BenchmarkResult]:
    """Benchmark a sort algorithm on various inputs. Return list of results."""
    # TODO 4: your implementation here
    raise NotImplementedError("TODO 4: implement benchmark runner")


# -- TODO 5: Comparison Report -------------------------------------------------
#
# Implement a function that benchmarks TWO algorithms on the same inputs
# and produces a ComparisonReport.
#
# Input:
#   - sort_a: first sort function
#   - name_a: name of first algorithm
#   - sort_b: second sort function
#   - name_b: name of second algorithm
#   - sizes: list of input sizes
#   - input_types: list of input type names
#
# Output: a ComparisonReport with results from both algorithms
#
# IMPORTANT: Both algorithms must be tested on IDENTICAL input data
# for each (size, input_type) pair. Generate the data once, then pass
# copies to each algorithm. This ensures a fair comparison.
#
# Hint: For each (size, type), generate data, then call time_sort on
#       a copy for each algorithm. Collect results into two parallel
#       lists (one per algorithm) and build the ComparisonReport.
#
# After this works, tests in test_properties.py should pass.

def compare(
    sort_a,
    name_a: str,
    sort_b,
    name_b: str,
    sizes: list[int],
    input_types: list[str],
) -> ComparisonReport:
    """Compare two sort algorithms on identical inputs."""
    # TODO 5: your implementation here
    raise NotImplementedError("TODO 5: implement comparison report")
