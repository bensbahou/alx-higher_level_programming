#!/usr/bin/python3
"""Finds all solutions to the N-Queens problem using recursive backtracking.

This program prints the coordinates of all valid solutions to the console
for an nxn grid such that n queens are in non-attacking positions.

Usage:
    python3 101-nqueens.py N

Args:
    N (int): The size of the grid and the number of queens to place.

Returns:
    None. The program prints all valid solutions to the console.
"""


from sys import argv

if __name__ == "__main__":
    a = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if not argv[1].isdigit():
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    a = [[i, None] for i in range(n)]

    def already_exists(y):
        """Checks if a queen already exists in the same column.

        Args:
            y (int): The row index being evaluated.

        Returns:
            bool: True if a queen already exists in the same column,
            False otherwise.
        """
        return y in [a[x][1] for x in range(n)]

    def reject(x, y):
        """Determines whether or not to reject a potential solution.

        Args:
            x (int): The current column being evaluated.
            y (int): The current row being evaluated.

        Returns:
            bool: True if the solution is valid, False otherwise."""
        return not already_exists(y) and all(
            abs(a[i][1] - y) != abs(i - x) for i in range(x)
        )

    def clear_a(x):
        """Clears the answers from the point of failure on.

        Args:
            x (int): The column index from which to clear the answers.

        Returns:
            None. The function modifies the global `a` list in place."""
        for i in range(x, n):
            a[i][1] = None

    def nqueens(x):
        """Finds all solutions to the N-Queens problem
        using recursive backtracking.

        Args:
            x (int): The current column being evaluated.

        Returns:
            None. The function prints all valid solutions to the console.
        """
        for y in range(n):
            clear_a(x)
            if reject(x, y):
                a[x][1] = y
                if x == n - 1:
                    print(a)
                else:
                    nqueens(x + 1)

    # start the recursive process at x = 0
    nqueens(0)
