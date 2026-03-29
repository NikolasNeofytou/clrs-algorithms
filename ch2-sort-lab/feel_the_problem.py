"""
Chapter 2 -- Feel the Problem: Why Does Algorithm Choice Matter?
================================================================
GOAL: Experience the performance gap between sorting algorithms.

You DON'T need to have read Chapter 2 yet. Just run this and watch.

WHAT TO DO:
  Run this script. It will sort the same data with different algorithms
  and show you exactly how much algorithm choice matters.
"""

import time
import random


def print_header(text):
    print(f"\n{'='*60}")
    print(f"  {text}")
    print(f"{'='*60}\n")


def selection_sort(arr):
    """A simple O(n^2) sort -- provided for comparison."""
    a = arr[:]
    n = len(a)
    comparisons = 0
    swaps = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swaps += 1
    return a, comparisons, swaps


def trace_sort_10(arr):
    """Show selection sort step-by-step on a small array."""
    a = arr[:]
    n = len(a)
    print(f"  Start:  {a}")
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            print(f"  Step {i+1}: {a}  (swapped {a[min_idx]} and {a[i]})")
        else:
            print(f"  Step {i+1}: {a}  ({a[i]} already in place)")
    print()


def main():
    print_header("FEEL THE PROBLEM")
    print("Let's see why algorithm choice matters more than hardware.\n")

    # --- Demo 1: Trace on 10 elements ---
    print_header("DEMO 1: Watching Selection Sort Work")
    small = random.sample(range(10, 100), 10)
    print("Sorting 10 numbers step by step:\n")
    trace_sort_10(small)
    input("Press Enter to continue...\n")

    # --- Demo 2: Time selection sort vs Python built-in ---
    print_header("DEMO 2: Speed Comparison")

    sizes = [1_000, 5_000, 10_000, 20_000]

    print(f"  {'N':>8}  {'Selection Sort':>16}  {'Python sorted()':>16}  {'Speedup':>10}")
    print(f"  {'-'*8}  {'-'*16}  {'-'*16}  {'-'*10}")

    for n in sizes:
        data = [random.randint(0, 1_000_000) for _ in range(n)]

        # Time selection sort
        start = time.perf_counter()
        selection_sort(data)
        slow_time = time.perf_counter() - start

        # Time Python built-in (Timsort -- O(n log n))
        start = time.perf_counter()
        sorted(data)
        fast_time = time.perf_counter() - start

        speedup = slow_time / max(fast_time, 1e-9)
        print(f"  {n:>8,}  {slow_time:>14.3f}s  {fast_time:>14.6f}s  {speedup:>8.0f}x")

    input("\nPress Enter to continue...\n")

    # --- Demo 3: Operation counting ---
    print_header("DEMO 3: Why Is It Slow? Counting Operations")

    data_1k = [random.randint(0, 100_000) for _ in range(1_000)]
    _, comps, swps = selection_sort(data_1k)

    print(f"  Sorting 1,000 elements:")
    print(f"    Comparisons: {comps:,}")
    print(f"    Swaps:       {swps:,}")
    print()

    data_5k = [random.randint(0, 100_000) for _ in range(5_000)]
    _, comps5, swps5 = selection_sort(data_5k)

    print(f"  Sorting 5,000 elements (5x more data):")
    print(f"    Comparisons: {comps5:,}  ({comps5/comps:.1f}x more -- not 5x!)")
    print(f"    Swaps:       {swps5:,}")
    print()

    print("  5x more data caused ~25x more comparisons.")
    print("  That's the signature of O(n^2): double the input, quadruple the work.")
    print()
    print("  Merge sort does the same job in O(n log n):")
    print(f"    1,000 elements: ~10,000 comparisons  (vs {comps:,})")
    print(f"    5,000 elements: ~61,000 comparisons  (vs {comps5:,})")
    print()

    input("Press Enter to see the challenge...\n")

    # --- The challenge ---
    print_header("YOUR CHALLENGE")
    print("""  Chapter 2 teaches you two sorting algorithms:

    1. INSERTION SORT -- simple, fast on small/nearly-sorted data
    2. MERGE SORT -- divide-and-conquer, always O(n log n)

  After reading, you'll implement both, count their operations,
  and benchmark them against each other. You'll discover:

    - Insertion sort beats merge sort on small arrays (low overhead)
    - Merge sort dominates on large arrays (better asymptotics)
    - The crossover point where one beats the other

  This is the fundamental lesson of algorithm design:
  there's no single "best" algorithm -- context matters.
""")
    print("=" * 60)
    print("  Now read Chapter 2. Then come back and BUILD.")
    print("=" * 60)
    print()


if __name__ == "__main__":
    random.seed(42)  # Reproducible for benchmarks
    main()
