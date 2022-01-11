import unittest
from unittest.mock import Mock
from modules.ModuleD import ModuleD


class TestModuleD(unittest.TestCase):

    def setUp(self):
        self.F = Mock()
        self.G = Mock()
        self.D = ModuleD(self.F, self.G)

    def testInsertData(self):
        n = "Gurbani"
        num = "0909"
        d = ["Gurbani,0900"]
        f = "test.txt"

        self.F.displayData()
        self.G.updateData()
        val = self.D.insertData(d, n, num, f)

        print(self.F.displayData.assert_called())  #Expected to print None
        print(self.G.updateData.assert_called())   #Expected to print None
        self.assertEqual(val,d,True)

    def testUpdateData(self):
        n = "Gurbani"
        num = "0909"
        d = ["Gurbani,0900"]
        f = "test.txt"
        i = 0

        self.F.displayData()
        self.G.updateData()
        val = self.D.updateData(d,i,n,num,f)

        print(self.F.displayData.assert_called())  #Expected to print None
        print(self.G.updateData.assert_called())   #Expected to print None
        self.assertEqual(val,d,True)

    def testDeleteData(self):
        d = ["Gurbani,0900"]
        f = "test.txt"
        i = 0

        self.F.displayData()
        self.G.updateData()
        val = self.D.deleteData(d, i,f)

        print(self.F.displayData.assert_called())  # Expected to print None
        print(self.G.updateData.assert_called())  # Expected to print None
        self.assertEqual(val, d, True)

if __name__ =='__main__':
    unittest.main()




