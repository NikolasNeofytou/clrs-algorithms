# Sort Lab: Insertion Sort vs Merge Sort

**Textbook**: CLRS -- *Introduction to Algorithms*, Chapter 2: Getting Started
**Language**: Python | **Estimated time**: 2-3 hours

## The Story

You're building a sorting toolkit that implements two fundamental algorithms, instruments them with operation counters, and benchmarks them head-to-head. By the end, you'll have hard data proving when each algorithm wins -- not just the theory, but actual numbers from your own code.

## Getting Started

### Prerequisites

```bash
pip install pytest
```

### 1. Feel the Problem (before reading Chapter 2)

Run the Phase 1 script and watch selection sort struggle:

```bash
python feel_the_problem.py
```

### 2. Read Chapter 2

See `reading_guide.md` for section priorities and questions.

### 3. Build

Work through the TODOs in `src/core.py` in order. Run tests after each:

```bash
# Run all tests (most will fail until you implement the TODOs)
pytest tests/ -v

# Run just the tests for the TODO you're working on
pytest tests/test_basic.py -v      # After TODO 1-2
pytest tests/test_edges.py -v      # After TODO 3
pytest tests/test_hard.py -v       # After TODO 4
pytest tests/test_properties.py -v # After TODO 5
```

## TODO Checklist

- [ ] **TODO 1**: Insertion Sort -- implement with comparison and swap counting -> unlocks `test_basic.py::TestInsertionSort`
- [ ] **TODO 2**: Merge Sort -- implement merge + merge_sort with comparison, copy, and recursion counting -> unlocks `test_basic.py::TestMergeSort`
- [ ] **TODO 3**: Execution Tracer -- traced insertion sort recording every step as a TraceStep -> unlocks `test_edges.py`
- [ ] **TODO 4**: Benchmark Runner -- time a sort on multiple input sizes and types -> unlocks `test_hard.py`
- [ ] **TODO 5**: Comparison Report -- benchmark two algorithms on identical inputs, produce ComparisonReport -> unlocks `test_properties.py`

## Module Map

| File | Purpose | Chapter Concepts |
|------|---------|-----------------| 
| `src/types.py` | Data structures (SortStats, TraceStep, BenchmarkResult) | Operation counting (2.2) |
| `src/core.py` | **Your implementation** -- all 5 TODOs | Insertion sort (2.1), merge sort (2.3), analysis (2.2) |
| `src/utils.py` | Data generators, timing, formatting | Provided helpers |
| `tests/` | Test suite (60 tests) | Verifies correctness and performance properties |
| `feel_the_problem.py` | Phase 1 demo -- why algorithm choice matters | Motivation |
| `reading_guide.md` | Guided reading with concept-to-code mapping | Chapter navigation |

## After You Finish

- [ ] All tests pass (`pytest tests/ -v` shows green)
- [ ] You can explain why insertion sort is O(n) on sorted input but O(n^2) on reverse
- [ ] You can explain why merge sort is always O(n log n) regardless of input
- [ ] Try: find the crossover point where insertion sort beats merge sort on small arrays
- [ ] Try: add a "nearly sorted" input type and see which algorithm wins
