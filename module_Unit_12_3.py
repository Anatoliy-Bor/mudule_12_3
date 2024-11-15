import unittest
import modul_12_1
import module_Unit_12_2

run_test = unittest.TestSuite()
run_test.addTest(unittest.TestLoader().loadTestsFromTestCase(modul_12_1.RunnerTest))
run_test.addTest(unittest.TestLoader().loadTestsFromTestCase(module_Unit_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(run_test)