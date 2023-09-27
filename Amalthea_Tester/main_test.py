import unittest

from Amalthea_Tester.basic_test import (TestBasicMath,
                                        TestLuasBangunDatar)

if __name__ == "__main__":
    basicMath_suite = unittest.TestLoader().loadTestsFromTestCase(
        TestBasicMath
    )
    luasBangunDatar_suite = unittest.TestLoader().loadTestsFromTestCase(
        TestLuasBangunDatar
    )
    all_tests = unittest.TestSuite(
        [
            basicMath_suite,
            luasBangunDatar_suite
        ]
    )
    
    unittest.TextTestRunner(verbosity=2).run(all_tests)

