import unittest
from modules.ModuleA import ModuleA
from unittest.mock import Mock

class TestModuleA(unittest.TestCase):

    def setUp(self):
        self.B = Mock()
        self.C = Mock()
        self.D = Mock()
        self.E = Mock()
        self.A = ModuleA(self.B, self.C, self.D, self.E)

    def testParseDelete(self):
        i = 0
        self.D.deleteData()
        val = self.A.parseDelete(i)
        self.D.deleteData.assert_called()
        self.assertTrue(val)

    def testDisplayHelp(self):
        val = self.A.displayHelp()
        self.assertTrue(val)

    def testParseLoad(self):
        self.B.loadFile()
        f = "data.txt"
        self.B.loadFile.assert_called()
        val = self.A.parseLoad(f)
        self.assertTrue(val)

    def testParseAdd(self):
        n = "Paul"
        num = "1234"
        self.D.insertData()
        self.D.insertData.assert_called()
        val = self.A.parseAdd(n,num)
        self.assertTrue(val)

    def testRunSort(self):
        self.C.sortData()
        self.C.sortData.assert_called()
        val = self.A.runSort()
        self.assertTrue(val)

    def testParseUpdate(self):
        i = 0
        n = "Gurbani"
        num = "8989"
        self.D.updateData()
        self.D.updateData.assert_called()
        val = self.A.parseUpdate(i,n,num)
        self.assertTrue(val)

    def testRunExit(self):
        self.E.exitProgram()
        self.E.exitProgram.assert_called()

if __name__ == '__main__':
        unittest.main()



