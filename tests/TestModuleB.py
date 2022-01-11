import unittest
from unittest.mock import Mock
from modules.ModuleB import ModuleB

class TestModuleC(unittest.TestCase):

    def setUp(self):
        self.F = Mock()
        self.B = ModuleB(self.F)

    def testLoadFile(self):
        f = "data.txt"
        self.F.displayData()
        val = self.B.loadFile(f)
        self.F.displayData.assert_called()  #Expected to print None
        self.assertEqual(val,[],True)


if __name__ =='__main__':
    unittest.main()




