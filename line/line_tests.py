import unittest
import line

class LineTests(unittest.TestCase):
  def test_line(self):
    testLine = line.Line(0, 0, 1, 1)
    self.assertEqual(testLine.x1,0)
    self.assertEqual(testLine.x2,0)
    self.assertEqual(testLine.y1,1)
    self.assertEqual(testLine.y2,1)
    

      # 1) Create a Line with x1, y1, x2, y2 values of your choice.
      # 2) Use assertEqual on each field in the new Line to verify
      #    that it holds the expected value.

# Run the unit tests.
if __name__ == '__main__':
    unittest.main()

