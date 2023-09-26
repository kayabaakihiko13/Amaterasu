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
    def persegi(s: float) -> float:
        return s * s
        
    @staticmethod
    def segitiga(a: float, t: float) -> float:
        return 0.5 * a * t
        
    @staticmethod
    def persegiPanjang(p: float, l: float) -> float:
        return p * l
        
    @staticmethod
    def trapesium(a: float, b: float, t: float) -> float:
        return 0.5 * (a + b) * t
    
    @staticmethod
    def layangLayang(d1: float, d2: float) -> float:
        return (d1 * d2) / 2
    
    @staticmethod
    def belahKetupat(d1: float, d2: float) -> float:
        return (d1 * d2) / 2
    
    @staticmethod
    def jajarGenjang(a: float, t: float) -> float:
        return a * t
    
    @staticmethod
    def lingkaran(r: int) -> float:
        if r%7 == 0:
            return 22/7 * r *r
        else:
            return 3.14 * r * r

class KelilingBangunDatar:
    @staticmethod
    def persegi(s: float) -> float:
        return 4 * s
    
    @staticmethod
    def segitigaSamaSisi(s: float) -> float:
        return 3 * s
    
    @staticmethod
    def segitigaSamaKaki(a: float, s: float) -> float:
        return a + s + s
    
    @staticmethod
    def persegiPanjang(p: float, l: float) -> float:
        return (2 * p) + (2 * l)
    
    @staticmethod
    def layangLayang(ab: float, bc: float) -> float:
        return 2 * (ab + bc)
    
    @staticmethod
    def trapesium(ab: float, bc: float, cd: float, da: float) -> float:
        return ab + bc + cd + da
    
    @staticmethod
    def belahKetupat(s: float) -> float:
        return 4 * s
    
    @staticmethod
    def jajarGenjang(ab: float, bc: float, cd: float, ad: float) -> float:
        return ab + bc + cd + ad
    
    @staticmethod
    def lingkaran(d: int) -> float:
        if d%7 == 0:
            return 22/7 * d
        else:
            return 3.14 * d