import unittest
from modules.ModuleG import ModuleG

class TestModuleG(unittest.TestCase):

    def testUpdateData(self):
        self.G = ModuleG()
        openF = "data.txt"
        dataT = ["Jacob,5656"]
        self.G.updateData(openF,dataT)

if __name__ =='__main__':
    unittest.main()

