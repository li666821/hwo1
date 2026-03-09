def solve_n_queens(n):
    """Solve the N-Queens problem and return all solutions.
    
    Args:
        n: The size of the chessboard (n x n) and the number of queens to place.
        
    Returns:
        A list of solutions, where each solution is a list of column indices representing the position of queens.
    """
    solutions = []
    board = [-1] * n  # board[i] represents the column index of the queen in row i
    
    def is_safe(row, col):
        """Check if placing a queen at (row, col) is safe."""
        for i in range(row):
            # Check if there's a queen in the same column
            if board[i] == col:
                return False
            # Check if there's a queen in the same diagonal
            if abs(board[i] - col) == abs(i - row):
                return False
        return True
    
    def backtrack(row):
        """Backtrack to find all solutions."""
        if row == n:
            # Found a solution, add it to the list
            solutions.append(board.copy())
            return
        
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1  # Backtrack
    
    backtrack(0)
    return solutions


def print_solution(solution):
    """Print a solution in a human-readable format."""
    n = len(solution)
    for row in solution:
        line = ['.'] * n
        line[row] = 'Q'
        print(''.join(line))
    print()


if __name__ == "__main__":
    # Solve 8-Queens problem
    solutions = solve_n_queens(8)
    print(f"Found {len(solutions)} solutions for 8-Queens problem")
    
    # Print the first few solutions
    print("First 3 solutions:")
    for i, solution in enumerate(solutions[:3]):
        print(f"Solution {i+1}:")
        print_solution(solution)