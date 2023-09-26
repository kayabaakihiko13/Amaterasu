class BasicMath:
    
    @staticmethod
    def penambahan(a: float, b: float) -> float:
        return a + b
    
    @staticmethod
    def pembagian(a: float, b: float) -> float:
        return a / b
    
    @staticmethod
    def perkalian(a: float, b: float) -> float:
        return a * b
    
    @staticmethod
    def pengurangan(a: float, b: float) -> float:
        return a - b
    
class LuasBangunDatar:
    
    @staticmethod
    def luasPersegi(s: float) -> float:
        return s * s
        
    @staticmethod
    def luasSegitiga(a: float, t: float) -> float:
        return 0.5 * a * t
        
    @staticmethod
    def luasPersegiPanjang(p: float, l: float) -> float:
        return p * l
        
    @staticmethod
    def luasTrapesium(a: float, b: float, t: float) -> float:
        return 0.5 * (a + b) * t
    
    @staticmethod
    def luasLayangLayang(d1: float, d2: float) -> float:
        return (d1 * d2) / 2
    
    @staticmethod
    def luasBelahKetupat(d1: float, d2: float) -> float:
        return (d1 * d2) / 2
    
    @staticmethod
    def luasJajarGenjang(a: float, t: float) -> float:
        return a * t
    
    @staticmethod
    def luasLingkaran(r: int) -> float:
        if r%7 == 0:
            return 22/7 * r *r
        else:
            return 3.14 * r * r

class KelilingBangunDatar:
    @staticmethod
    def kelilingPersegi(s: float) -> float:
        return 4 * s
    
    @staticmethod
    def kelilingSegitigaSamaSisi(s: float) -> float:
        return 3 * s
    
    @staticmethod
    def kelilingSegitigaSamaKaki(a: float, s: float) -> float:
        return a + s + s
    
    @staticmethod
    def kelilingPersegiPanjang(p: float, l: float) -> float:
        return (2 * p) + (2 * l)
    
    @staticmethod
    def kelilingLayangLayang(ab: float, bc: float) -> float:
        return 2 * (ab + bc)
    
    @staticmethod
    def kelilingTrapesium(ab: float, bc: float, cd: float, da: float) -> float:
        return ab + bc + cd + da
    
    @staticmethod
    def kelilingBelahKetupat(s: float) -> float:
        return 4 * s
    
    @staticmethod
    def kelilingJajarGenjang(ab: float, bc: float, cd: float, ad: float) -> float:
        return ab + bc + cd + ad
    
    @staticmethod
    def kelilingLingkaran(d: int) -> float:
        if d%7 == 0:
            return 22/7 * d
        else:
            return 3.14 * d