# tests/TestRunner.py
#A new Python file Testrunner.py alongside our tests that contains our runner
import unittest

# import tests modules -  Applying integration testing method
import TestModuleA
import TestModuleB
import TestModuleC
import TestModuleD
import TestModuleE
import TestModuleF
import TestModuleG


# initialize the tests suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# add tests to the tests suite
suite.addTests(loader.loadTestsFromModule(TestModuleA))
suite.addTests(loader.loadTestsFromModule(TestModuleB))
suite.addTests(loader.loadTestsFromModule(TestModuleC))
suite.addTests(loader.loadTestsFromModule(TestModuleD))
suite.addTests(loader.loadTestsFromModule(TestModuleE))
suite.addTests(loader.loadTestsFromModule(TestModuleF))
suite.addTests(loader.loadTestsFromModule(TestModuleG))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=10)
result = runner.run(suite)