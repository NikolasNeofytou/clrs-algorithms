# Reading Guide -- Chapter 2: Getting Started

**Textbook**: CLRS, *Introduction to Algorithms*

Read this AFTER running `feel_the_problem.py`.

---

## What You Just Experienced

You saw selection sort struggle on 20,000 elements while Python's built-in sorted it instantly. You saw that 5x more data caused 25x more comparisons -- the quadratic growth signature. The chapter you're about to read teaches you two algorithms: one that's simple but quadratic, and one that's clever and breaks through to O(n log n).

---

## Section Priorities

### Study Carefully

- **2.1 -- Insertion Sort**: The algorithm, the loop invariant, and the analysis. Pay close attention to the "key" variable and how elements shift right. When you implement this, you'll count every comparison and shift -- so understand where they happen in the pseudocode.

- **2.2 -- Analyzing Algorithms**: This is where you learn to count operations formally. The distinction between best case (sorted input: O(n)) and worst case (reverse input: O(n^2)) is exactly what your benchmark will reveal.

- **2.3 -- Designing Algorithms (Merge Sort)**: The divide-and-conquer paradigm. Focus on the MERGE procedure (2.3.1) -- this is the core operation. Understand why merging two sorted lists takes O(n) time, and why the recursion gives O(n log n) total.

### Skim for Context

- **2.3.2 -- Analyzing Divide-and-Conquer**: The recurrence T(n) = 2T(n/2) + O(n). You'll see this proved more formally in Chapter 4. For now, accept that it gives O(n log n) and focus on *why* the recursion structure leads to this.

---

## Questions to Answer While Reading

1. In insertion sort, how many comparisons happen when the input is already sorted? Why?

2. In insertion sort, how many comparisons happen when the input is reverse sorted? Express in terms of n.

3. In the MERGE procedure, what happens when one of the two halves is exhausted? How many comparisons does this save?

4. Why is merge sort not in-place? What extra memory does it need?

5. If insertion sort is O(n) on sorted input and merge sort is always O(n log n), when would you prefer insertion sort?

---

## Concept -> Project Mapping

| Chapter Concept | You'll Build |
|---|---|
| Insertion sort algorithm (2.1) | `src/core.py` -- TODO 1: insertion sort with operation counting |
| Merge procedure (2.3.1) | `src/core.py` -- TODO 2: merge and merge_sort with counting |
| Loop invariant reasoning (2.1) | `src/core.py` -- TODO 3: traced execution showing invariant in action |
| Algorithm analysis (2.2) | `src/core.py` -- TODO 4: benchmark runner proving O(n^2) vs O(n log n) |
| Comparing algorithms | `src/core.py` -- TODO 5: head-to-head comparison report |
