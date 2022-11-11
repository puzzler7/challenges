# Mazed

**Category:** Category
**Difficulty:** Easy/Medium/Hard
**Author:** Author

## Description

I was making an n-dimensional maze for a different challenge, with the intention for players to exploit the maze. However, it seemed a shame to waste, so here's the raw maze, exploit free.

## Distribution

maze.py, nc

## Deploy notes

Host such that players connect to maze.py, with flag.txt in the same directory.

## Solution

See x.py for a solve script. A simple depth-first search through the maze finds the flag, and the path to it. The shortest path isn't required, so this is sufficient.
