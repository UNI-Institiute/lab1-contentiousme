import unittest
import line

class LineTests(unittest.TestCase):
  def test_line(self):
    testLine = line.Line(0, 0, 1, 1)
    self.assertEqual(testLine.x1,0)
    self.assertEqual(testLine.x2,0)
    self.assertEqual(testLine.y1,1)
    self.assertEqual(testLine.y2,1)
  
  def test_line2(self):
    testLine = line.Line(25,25,50,50)
    self.assertEqual(testLine.x1,25)
    self.assertEqual(testLine.x2,25)
    self.assertEqual(testLine.y1,50)
    self.assertEqual(testLine.y2,50)

  def test_line3(self):
    testLine = line.Line(1000,2000,3000,4000)
    self.assertEqual(testLine.x1,1000)
    self.assertEqual(testLine.x2,2000)
    self.assertEqual(testLine.y1,3000)
    self.assertEqual(testLine.y2,4000)

  def test_line4(self):
    testLine = line.Line(-456,-333,-567,-897)
    self.assertEqual(testLine.x1,-456)
    self.assertEqual(testLine.x2,-333)
    self.assertEqual(testLine.y1,-567)
    self.assertEqual(testLine.y2,-897)
    

  # 1) Create a Line with x1, y1, x2, y2 values of your choice.
  # 2) Use assertEqual on each field in the new Line to verify
  #    that it holds the expected value.

# Run the unit tests.
if __name__ == '__main__':
    unittest.main()

