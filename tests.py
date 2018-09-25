import unittest

from grid import Grid


class GridTest(unittest.TestCase):
    def test_init(self):
        width, height = 3, 4
        Grid.VOID = '$'
        grid = Grid(width, height)
        self.assertEqual(width, grid.width)
        self.assertEqual(height, grid.height)
        self.assertEqual([['$', '$', '$'], ['$', '$', '$'], ['$', '$', '$'], ['$', '$', '$']], grid.data)

    def test_setitem(self):
        width, height = 3, 4
        Grid.VOID = '$'
        p1 = '1'
        p2 = '2'
        grid = Grid(width, height)
        grid[0] = p2
        grid[2] = p1
        grid[2] = p1
        grid[1] = p1
        grid[1] = p2
        grid[1] = p2
        self.assertEqual([['$', '$', '$'], ['$', '2', '$'], ['$', '2', '1'], ['2', '1', '1']], grid.data)

    def test_get_playable_cols(self):
        width, height = 3, 4
        Grid.VOID = '$'
        grid = Grid(width, height)
        self.assertEqual([0, 1, 2], grid.get_playable_cols())
        grid[1] = '0'
        grid[1] = '0'
        grid[1] = '0'
        grid[1] = '0'
        self.assertEqual([0, 2], grid.get_playable_cols())
