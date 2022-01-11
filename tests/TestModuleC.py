import unittest
from unittest.mock import Mock
from modules.ModuleC import ModuleC

class TestModuleC(unittest.TestCase):

    def setUp(self):
        self.F = Mock()
        self.C = ModuleC(self.F)

    def testSortData(self):
        d = ["Gurbani,1100", "Lincoln,7908"]
        self.F.displayData()
        val = self.C.sortData(d)
        print(self.F.displayData.assert_called())  #Expected to print None
        self.assertEqual(val,d,True)


if __name__ =='__main__':
    unittest.main()




