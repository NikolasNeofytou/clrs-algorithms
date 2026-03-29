"""
Module: types
Purpose: Data structures for the sorting lab.
Chapter Reference: CLRS Ch 2 (Insertion Sort, Merge Sort)

All types are defined here. Import and use in core.py.
"""

from dataclasses import dataclass, field


@dataclass
class SortStats:
    """
    Tracks operations performed during a sort.
    This is how you measure an algorithm's actual work,
    not just its wall-clock time.
    """
    comparisons: int = 0
    swaps: int = 0        # For in-place sorts (insertion sort)
    copies: int = 0       # For merge sort (copies to/from temp arrays)
    recursive_calls: int = 0

    @property
    def total_operations(self) -> int:
        return self.comparisons + self.swaps + self.copies


@dataclass
class TraceStep:
    """
    A single step in the execution trace.
    Records what happened and the array state after.
    """
    step_number: int
    operation: str          # e.g., "compare", "swap", "merge"
    description: str        # Human-readable: "Swapped 5 and 3 at positions 2,4"
    array_state: list[int]  # Copy of the array after this step


@dataclass
class BenchmarkResult:
    """
    Result of timing a sort algorithm on a specific input.
    """
    algorithm: str
    input_size: int
    input_type: str         # "random", "sorted", "reverse", "duplicates"
    wall_time_seconds: float
    stats: SortStats


@dataclass
class ComparisonReport:
    """
    Side-by-side comparison of two algorithms.
    """
    algorithm_a: str
    algorithm_b: str
    results_a: list[BenchmarkResult]
    results_b: list[BenchmarkResult]
