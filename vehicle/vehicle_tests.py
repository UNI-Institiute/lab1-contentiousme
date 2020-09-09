import unittest
import vehicle

class VehicleTests(unittest.TestCase):
  def test_vehicle(self):
    testVehicle = vehicle.Vehicle(4,40,2,True)
    

# Run the unit tests.
if __name__ == '__main__':
    unittest.main()

