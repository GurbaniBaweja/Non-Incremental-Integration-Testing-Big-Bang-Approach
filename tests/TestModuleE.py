import unittest
from modules.ModuleE import ModuleE

class TestModuleE(unittest.TestCase):

    def testExitProgram(self):
        self.E = ModuleE()
        self.E.exitProgram()

if __name__ =='__main__':
    unittest.main()




