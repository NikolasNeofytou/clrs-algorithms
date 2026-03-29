"""
Module: utils
Purpose: Helper functions for benchmarking, formatting, and data generation.
These are provided -- no TODOs here.
"""

import random
import time
from src.types import BenchmarkResult, SortStats, ComparisonReport


# -- Data generators -----------------------------------------------------------

def generate_random(n: int, seed: int = 42) -> list[int]:
    """Generate n random integers in range [0, 10*n]."""
    rng = random.Random(seed)
    return [rng.randint(0, 10 * n) for _ in range(n)]


def generate_sorted(n: int) -> list[int]:
    """Generate a sorted list of n integers."""
    return list(range(n))


def generate_reverse(n: int) -> list[int]:
    """Generate a reverse-sorted list of n integers."""
    return list(range(n, 0, -1))


def generate_duplicates(n: int) -> list[int]:
    """Generate n integers with many duplicates (only 10 distinct values)."""
    rng = random.Random(42)
    return [rng.randint(0, 9) for _ in range(n)]


def generate_nearly_sorted(n: int, swaps: int = None) -> list[int]:
    """Generate a nearly-sorted list (sorted, then a few random swaps)."""
    if swaps is None:
        swaps = max(1, n // 20)  # 5% perturbation
    rng = random.Random(42)
    arr = list(range(n))
    for _ in range(swaps):
        i, j = rng.randint(0, n - 1), rng.randint(0, n - 1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


INPUT_GENERATORS = {
    "random": generate_random,
    "sorted": generate_sorted,
    "reverse": generate_reverse,
    "duplicates": generate_duplicates,
    "nearly_sorted": generate_nearly_sorted,
}


# -- Timing helper -------------------------------------------------------------

def time_sort(sort_func, data: list[int]) -> tuple[list[int], float, SortStats]:
    """
    Time a sort function and return (sorted_result, elapsed_seconds, stats).
    The sort function must return (sorted_list, SortStats).
    """
    arr = data[:]  # Don't modify original
    start = time.perf_counter()
    result, stats = sort_func(arr)
    elapsed = time.perf_counter() - start
    return result, elapsed, stats


# -- Formatting ----------------------------------------------------------------

def format_comparison_table(report: ComparisonReport) -> str:
    """Format a side-by-side comparison of two algorithms."""
    lines = []
    lines.append(f"\n  {report.algorithm_a} vs {report.algorithm_b}")
    lines.append(f"  {'='*70}")
    lines.append(
        f"  {'N':>8}  {'Type':<14}  "
        f"{'Time A':>10}  {'Ops A':>10}  "
        f"{'Time B':>10}  {'Ops B':>10}  "
        f"{'Speedup':>8}"
    )
    lines.append(f"  {'-'*8}  {'-'*14}  {'-'*10}  {'-'*10}  {'-'*10}  {'-'*10}  {'-'*8}")

    for ra, rb in zip(report.results_a, report.results_b):
        speedup = ra.wall_time_seconds / max(rb.wall_time_seconds, 1e-9)
        winner = "<" if speedup > 1 else ">"  # < means B is faster
        lines.append(
            f"  {ra.input_size:>8,}  {ra.input_type:<14}  "
            f"{ra.wall_time_seconds:>9.4f}s  {ra.stats.total_operations:>10,}  "
            f"{rb.wall_time_seconds:>9.4f}s  {rb.stats.total_operations:>10,}  "
            f"{speedup:>6.1f}x {winner}"
        )

    return "\n".join(lines)


def format_trace(trace_steps: list) -> str:
    """Format execution trace steps as readable text."""
    lines = []
    for step in trace_steps:
        lines.append(f"  Step {step.step_number:>3}: {step.description}")
        lines.append(f"           {step.array_state}")
    return "\n".join(lines)


def verify_sorted(original: list[int], result: list[int]) -> tuple[bool, str]:
    """
    Verify that result is a correctly sorted version of original.
    Returns (is_correct, explanation).
    """
    if len(result) != len(original):
        return False, f"Length mismatch: expected {len(original)}, got {len(result)}"

    if sorted(original) != result:
        # Check if it's a permutation issue or ordering issue
        if sorted(original) != sorted(result):
            return False, "Result is not a permutation of input (elements differ)"
        else:
            return False, "Result contains correct elements but is not sorted"

    return True, "Correctly sorted"
