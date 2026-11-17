# Fantasy Football Team Selection — Greedy Algorithm (HOM Lab 1)

A Python program that selects a fantasy-football squad using a greedy algorithm and then improves it with local search. It was written for the **Heuristic Optimization Methods (HOM)** course at FER, University of Zagreb.

## Problem

Given a list of players with a position, club, price and expected point score, choose:

- a first team of 11 players
- 4 substitutes

while respecting:

- a total budget of 100
- position quotas (goalkeepers, defenders, midfielders, forwards)
- a maximum of 3 players per club

The greedy algorithm builds a valid squad, and the local search then tries to improve the total points of the first team.

## Input format

The program expects a CSV file with one player per row, encoded as `cp1252`:

```text
id,position,name,club,points,price
1,GK,Player One,Club A,42.0,5.5
2,DEF,Player Two,Club B,31.0,4.5
...
```

Positions are `GK`, `DEF`, `MID` and `FW`.

## Requirements

- Python 3.11.9 (pinned in `.tool-versions`; the code requires 3.8 or newer)
- No external packages — only the Python standard library

Install the pinned Python version with asdf:

```bash
asdf install
```

## Run

```bash
python3 main.py path/to/players.csv
```

The program prints the selected squad and writes:

- `greedy_solution.txt` — player IDs after the greedy phase
- `local_optimised.txt` — player IDs after local search

## Project structure

```text
main.py                    # entry point
parser.py                  # CSV instance parser
models.py                  # Player and Squad models
greedy_algorithm.py        # greedy squad construction
local_search_algorithm.py  # local-search improvement
```
