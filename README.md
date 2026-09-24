# Quera

My Python solutions to problems from the [Quera](https://quera.org/problemset) problem set.

## Overview

Quera is an Iranian programming platform with an archive of judged problems. This repository collects the ones I've solved — currently 64 problems, each in its own file with a link back to the original statement.

Most of the collection is programming fundamentals: reading and parsing input, loops and conditionals, integer arithmetic, string handling and formatted output. A smaller part leans on elementary number theory and math (primality, divisors, LCM, digital roots, Fibonacci numbers) or on a bit of simulation and brute-force search. One problem is a small object-oriented exercise with unit tests rather than a stdin/stdout task.

The solutions are short, and where I found a second reasonable approach I left it in as a commented-out alternative.

## Repository Structure

Problems are grouped first by the difficulty Quera assigns them, then by topic:

```
.
├── easy/
│   ├── combinatorics/
│   ├── geometry/
│   ├── greedy/
│   ├── implementation/
│   ├── math/
│   ├── programming fundamentals/
│   ├── school level/
│   ├── search/
│   └── strings/
├── medium/
│   ├── implementation/
│   ├── math/
│   ├── programming fundamentals/
│   ├── python/
│   │   ├── subtraction game.py
│   │   └── digikala/Initial_project/
│   ├── school level/
│   └── strings/
└── hard/
    └── programming fundamentals/
```

| Difficulty | Problems |
| ---------- | -------- |
| `easy/`    | 48       |
| `medium/`  | 15       |
| `hard/`    | 1        |

The difficulty levels are Quera's, not mine. `hard/` holds a single problem — *number printer* — which is really a warm-up exercise; the file itself notes that it's unclear why it was rated hard.

`medium/python/` contains problems that test Python itself rather than an algorithm, and they aren't judged through stdin/stdout:

- **`subtraction game.py`** only defines a function, `game(num)`, which the judge imports and calls.
- **`digikala/Initial_project/`** is a small online-store model (`Product`, `User`, `Comment`, `Store`) where the task is implementing the `Store` methods in `store.py`. It includes `models.py` and a `unittest` suite in `test/sample_test.py`.

## Languages and Tools

- **Python 3** — every solution is Python. Only the standard library is used (`math`, `sys`, `datetime`, `unittest`); there are no third-party dependencies.

Use **Python 3.12 or newer**. A few files rely on recent syntax: `easy/implementation/yellow question.py` reuses the same quote type inside an f-string (3.12+), `easy/implementation/reverse printing.py` uses the walrus operator (3.8+), and `easy/math/weird circle.py` uses `math.lcm` (3.9+).

## Solution Conventions

- **One problem per file**, named after the problem's title in English (a translation or transliteration of the Persian title), e.g. `easy/math/phone charge.py`.
- **The first line links to the problem statement**, e.g. `# link https://quera.org/problemset/17244`. The problem ID in that URL is the reliable way to find the original problem.
- **Input comes from stdin and output goes to stdout**, following the judge's format exactly. No prompts, no extra output.
- **Alternative approaches are kept as comments** in a few files, for example an iterative and a recursive factorial (`easy/programming fundamentals/factorial.py`) or the loop-based and closed-form digital root (`medium/math/one digit.py`).
- **Small helper functions** such as `is_prime` or `generate_pascals_triangle` are defined in the file that uses them rather than shared between files, so every solution stands on its own.

## What's Covered

- **Programming fundamentals** — loops, conditionals, accumulators, reading multi-line input, and ASCII pattern printing (squares, diamonds, star shapes).
- **Strings** — slicing and reversal, palindromes, character counting, substring checks, comparing strings position by position, and reversing word order.
- **Number theory and math** — trial-division primality testing, enumerating divisors and perfect numbers, LCM, powers of two, digital roots, Fibonacci numbers, Pythagorean triples, and simple closed-form formulas such as triangular numbers.
- **Combinatorics and geometry** — counting results with a closed-form expression, generating Pascal's triangle row by row, and an XOR trick for finding the missing corner of an axis-aligned rectangle.
- **Simulation and search** — step-by-step simulation (`easy/greedy/iteration on plates.py`) and brute-force search for a valid combination (`easy/search/cracked a walnut.py`).
- **Built-in data structures** — lists, sets for uniqueness and dicts for counting, used where they fit naturally.
- **Object-oriented Python** — classes, class attributes, `__eq__`/`__hash__` for use as dict keys, and `unittest` in the Digikala project.

This isn't a collection of advanced algorithms. You won't find graph algorithms, dynamic programming or custom data structures here; the problems are mostly introductory to intermediate.

## Running Solutions

There's no build system or test runner. Each file is a standalone script. Since file names contain spaces, quote the paths.

Run a solution and type the input yourself:

```sh
python3 "easy/math/phone charge.py"
```

Or pipe the input in:

```sh
echo 5 | python3 "easy/math/phone charge.py"
# 15
```

`medium/python/subtraction game.py` only defines a function, so load it interactively and call it:

```sh
python3 -i "medium/python/subtraction game.py"
>>> game(52)
3
```

The Digikala tests have to be run from the project directory, because the test file adds `../Initial_project` to `sys.path` relative to the current working directory:

```sh
cd medium/python/digikala/Initial_project
python3 test/sample_test.py
```

## Context

This is ongoing practice alongside my other work. I add solutions as I solve new problems, so the collection grows unevenly across categories.

## License

Released under the [MIT License](LICENSE). Copyright (c) 2025 AFrenchWrench.
