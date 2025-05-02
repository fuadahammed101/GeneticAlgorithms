# N-Queens Problem Solver using Genetic Algorithm

This repository contains a simple Python implementation of the N-Queens problem solved using a Genetic Algorithm (GA). The code is written in a beginner-friendly style to help understand the basic concepts of genetic algorithms applied to this classic problem.

## What is the N-Queens Problem?

The N-Queens problem is a classic puzzle where the goal is to place N chess queens on an N×N chessboard so that no two queens threaten each other. This means no two queens share the same row, column, or diagonal.

## What is a Genetic Algorithm?

A Genetic Algorithm is a search heuristic inspired by the process of natural selection. It uses techniques such as selection, crossover, and mutation to evolve solutions to optimization and search problems.

## How This Code Works

- **Population Initialization:** Randomly generates a population of candidate solutions.
- **Fitness Function:** Measures how good a solution is by counting the number of non-attacking pairs of queens.
- **Selection:** Uses tournament selection to pick parents for reproduction.
- **Crossover:** Combines two parents to produce offspring using a simple crossover method.
- **Mutation:** Randomly swaps two positions in a solution to maintain genetic diversity.
- **Termination:** The algorithm runs for a fixed number of generations or until a solution with no attacks is found.

## How to Run

1. Make sure you have Python installed (tested with Python 3.x).
2. Run the script:

```bash
python GenAl.py
```

3. The program will print the solution board if it finds one within the generation limit.

## Example Output

```
Solution found at generation 123
. Q . . . . . . 
. . . Q . . . . 
Q . . . . . . . 
. . . . . Q . . 
. . Q . . . . . 
. . . . . . . Q 
. . . . Q . . . 
. . . . . . Q . 
```

## Notes

- The code is intentionally written in a simple style to be easy to understand.
- You can change the board size by modifying the `n` variable in the script.
- You can also adjust population size, mutation rate, and generation limit inside the code for experimentation.

## License

This project is open source and free to use.
