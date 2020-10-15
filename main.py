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

    """
    Hlavni algrotimus tz.n Hronerovo schema v praxi
    """

    # vypise nejmensi tvar polynomu
    def short_polynom(self):
        meta_number = self.find_meta_number()
        new_polynom = []

        # pouyivame k definovani prvniho clenu Hornerova schematu
        is_first = True

        # cyklus se zopakuje podle poctu korenu
        for i in range(0, len(meta_number)):

            # cyklus projizdi jednotlive koeficienty a dopocitava nove pole
            for s in range(0, len(self.polynom)):
                
                if is_first == True:
                    new_polynom.append(self.polynom[s])
                    is_first = False
                else:    
                    new_polynom.append( (meta_number[i] * new_polynom[s-1]) + self.polynom[s] )
            
            is_first = True

            self.polynom = new_polynom
            new_polynom = []

        # cyklus zajistuje vraceni pouze cesti s hodnotami
        part_polynom = []
        for i in range(0, (len(self.polynom)-len(meta_number))):
            part_polynom.append(self.polynom[i])

        # ==========================
        # vypise finalni zkraceny format

        out = ""

        # cast s koreny
        for i in range(0, len(meta_number)):
            if meta_number[i] < 0:
                out += "(x" + str(meta_number[i]) + ")"

            else:
                out += "(x+" + str(meta_number[i]) + ")"
        
        # cast nerozkladatelna
        out += "("
        for i in range(0, len(part_polynom)):
            if part_polynom[i] != 0:
                if part_polynom[i] > 0:
                    out += "+"    
                out += str(part_polynom[i]) + "x^"
                out += str(len(part_polynom)-i-1)
        out += ")"

        return out


if __name__ == '__main__':
    c1 = Polynom([1, -4, 2, 2, 1, 6])
    print(c1)

    c2 = c1.find_meta_number()
    print(c2)

    c3 = c1.short_polynom()
    print(c3)

# input user polynom
# input specific number type R, C, N, Q, ... (default is R)

# find meta number

# do Horner scheme

# return final value
