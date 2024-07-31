class Kalkulator:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
        self.x = a

        pass

    def saberi(self):
        return self.a + self.b

    def oduzmi(self):
        return self.a - self.b

    def pomnozi(self):
        return self.a * self.b

    def podeli(self):
        return self.a / self.b

    def gcd(self):
        a = self.a
        b = self.b
        while b:
            a, b = b, a % b
        return a

    def rezultati(self):
        return
