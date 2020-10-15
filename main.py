class Polynom:

    def __init__(self, polynom = []):
        self.polynom = polynom
    
    def get_polynom(self):
        return self.polynom

    # polynom je definovan ve formatu, od clena s nejnizsim exponentem po clena s nevyjssim
    # pokud clen neni definovan, napis na jeho misto nulu
    # priklad: polynom 2x^5 + 5x^4 - 3x^3 + 0x^2 + 3x^1 - 2x^0
    # priklad v kodu: [2, 5, -3, 0, 3, -2]

    def __str__(self):
        out = ""
        for i in range(0, len(self.polynom)):
            out += str(self.polynom[i])
            out += "x^" + str(len(self.polynom) - i - 1) + " "
        return out

    """
    Cast kodu, ktera vraci pole s celociselnymi koreny
    ve forme pole
    """

    # najde celocislene delitele zadaneho cisla
    def find_divisor(self):
        number = self.polynom[-1]
        divisor = []
        i = 1
        while i <= abs(number):
            if (abs(number) % i == 0):
                divisor.append(-i)
                divisor.append(i)
            i += 1
        return divisor

    # vyresi rovnici v oboru celych cisel
    # number = cislo, ktere dosazujeme
    def solved_polynom(self, number):
        value = 0
        for i in range (0, len(self.polynom)):
            value += (self.polynom[i] * (number ** (len(self.polynom) - i - 1)))
        return value

    # propocita, pro ktere delitele je rovnice nulova
    def find_meta_number(self):
        divisor = self.find_divisor()
        meta_number = []
        for i in range(0, len(divisor)):
            if(self.solved_polynom(divisor[i]) == 0):
                meta_number.append(divisor[i])
        return meta_number


if __name__ == '__main__':
    c1 = Polynom([1, -4, 2, 2, 1, 6])
    print(c1)

    c2 = c1.find_meta_number()
    print(c2)

# input user polynom
# input specific number type R, C, N, Q, ... (default is R)

# find meta number

# do Horner scheme

# return final value
