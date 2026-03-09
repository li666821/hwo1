import unittest
from src.n_queens import solve_n_queens


class TestNQueens(unittest.TestCase):
    """Test cases for N-Queens problem solver."""
    
    def test_n_queens_1(self):
        """Test N=1 case."""
        solutions = solve_n_queens(1)
        self.assertEqual(len(solutions), 1)
        self.assertEqual(solutions, [[0]])
    
    def test_n_queens_2(self):
        """Test N=2 case (no solution)."""
        solutions = solve_n_queens(2)
        self.assertEqual(len(solutions), 0)
    
    def test_n_queens_3(self):
        """Test N=3 case (no solution)."""
        solutions = solve_n_queens(3)
        self.assertEqual(len(solutions), 0)
    
    def test_n_queens_4(self):
        """Test N=4 case (2 solutions)."""
        solutions = solve_n_queens(4)
        self.assertEqual(len(solutions), 2)
    
    def test_n_queens_8(self):
        """Test N=8 case (92 solutions)."""
        solutions = solve_n_queens(8)
        self.assertEqual(len(solutions), 92)
    
    def test_solution_validity(self):
        """Test that all solutions are valid."""
        for n in range(1, 6):
            solutions = solve_n_queens(n)
            for solution in solutions:
                # Check that each row has exactly one queen
                self.assertEqual(len(solution), n)
                # Check that no two queens are in the same column
                self.assertEqual(len(set(solution)), n)
                # Check that no two queens are on the same diagonal
                diagonals1 = []  # (row - col)
                diagonals2 = []  # (row + col)
                for row, col in enumerate(solution):
                    diagonals1.append(row - col)
                    diagonals2.append(row + col)
                self.assertEqual(len(set(diagonals1)), n)
                self.assertEqual(len(set(diagonals2)), n)


if __name__ == '__main__':
    unittest.main()