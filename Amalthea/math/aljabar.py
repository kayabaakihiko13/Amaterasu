class BasicOperation:
    @staticmethod
    def penambahan(variabel: str, a: int, b: int):
        return f"{a}{variabel} + {b}{variabel} = {a + b}{variabel}"
    
    @staticmethod
    def pengurangan(variabel: str, a: int, b : int):
        return f"{a}{variabel} - {b}{variabel} = {a - b}{variabel}"
    
    @staticmethod
    def perkalian(variabel: str, a: int, b: int):
        return f"{a}{variabel} x {b}{variabel} = {a * b}{variabel}"
    
    @staticmethod
    def pembagian(variabel: str, a: int, b: int):
        return f"{a}{variabel} / {b}{variabel} = {a / b}{variabel}"