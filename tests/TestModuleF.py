import unittest
from modules.ModuleF import ModuleF

class TestModuleF(unittest.TestCase):

    def testDisplayData(self):
        self.F = ModuleF()
        dataT = ["Jacob,5656","Joshua,1324"]
        self.F.displayData(dataT)

if __name__ =='__main__':
    unittest.main()




