import unittest

from Amalthea.basic import (BasicMath,
                            LuasBangunDatar,
                            KelilingBangunDatar,
                            VolumeBangunRuang)

class TestBasicMath(unittest.TestCase):

    def setUp(self) -> None:
        self.basic = BasicMath()

    def test_addition(self):
        input_a = 1.01
        input_b = 2.12
        result = self.basic.penambahan(input_a,
                                       input_b)
        self.assertEqual(result,3.13)
    
    def test_times(self):
        input_a = 10
        input_b = 21.2
        result = self.basic.perkalian(input_a,input_b)
        self.assertEqual(result,212)
    
    def test_division(self):
        input_a = 22
        input_b = 11
        result = self.basic.pembagian(input_a,input_b)
        self.assertEqual(result,2.0)
    
    def test_elimination(self):
        input_a = 10
        input_b = 2
        result = self.basic.pengurangan(input_a,input_b)
        self.assertEqual(result,8.0)
    
class TestLuasBangunDatar(unittest.TestCase):
    
    def setUp(self) -> None:
        self.luasdatar = LuasBangunDatar()
    
    def testLuasPersegi(self):
        input_a = 12
        result = self.luasdatar.luasPersegi(input_a)
        self.assertEqual(result,144)
    
    def testLuasPersegiPanjang(self):
        input_p = 12
        input_l = 9
        result = self.luasdatar.luasPersegiPanjang(input_p,
                                                   input_l)
        self.assertEqual(result,108)
    
    def testTrapesium(self):
        input_p = 5
        input_l = 7
        input_t = 10
        result = self.luasdatar.luasTrapesium(input_p,input_l,
                                     input_t)
        self.assertEqual(result,60)
    
    def testLingkaran(self):
        input_r = 14
        result = self.luasdatar.luasLingkaran(input_r)
        self.assertEqual(result,616.0)
 