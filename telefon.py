class Telefon:

    counter = 0

    def __init__(self, number):
        self.number = number
        Telefon.counter += 1

    def apelare(self, numar_apelat):
        mesaj = f'Apelati {numar_apelat} de pe telefonul propriu.'
        return mesaj


class TelefonFix(Telefon):

    last_SN = 0

    def __init__(self, number):
        super().__init__(number)
        TelefonFix.last_SN += 1
        self.SN = f'TF - {TelefonFix.last_SN}'


class TelefonMobil(Telefon):

    last_SN = 0

    def __init__(self, number):
        super().__init__(number)
        TelefonMobil.last_SN += 1
        self.SN = f'TM - {TelefonFix.last_SN}'


print('Numarul total de deviceuri create', Telefon.counter)
fix1 = TelefonFix('12718821')
fix2 = TelefonFix('4348821')

mobil1 = TelefonMobil('073627632')
mobil2 = TelefonMobil('077727632')

print('Numarul total de deviceuri create', Telefon.counter)

print(mobil2.SN)
