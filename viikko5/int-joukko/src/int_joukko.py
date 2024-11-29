KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.ljono = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lkm = 0

    def kuuluu(self, alkio):
        kuuluu = 0

        for i in range(self.alkioiden_lkm):
            if alkio == self.ljono[i]:
                kuuluu += 1
                
        if kuuluu > 0:
            return True
        else:
            return False

    def lisaa(self, alkio):
        if self.alkioiden_lkm == 0:
            self.ljono[0] = alkio
            self.alkioiden_lkm += 1
            return True

        if not self.kuuluu(alkio):
            self.ljono[self.alkioiden_lkm] = alkio
            self.alkioiden_lkm += 1

            if self.alkioiden_lkm == len(self.ljono):
                taulukko_old = self.ljono
                self.kopioi_lista(self.ljono, taulukko_old)
                self.ljono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_lista(taulukko_old, self.ljono)
            return True

        return False

    def poista(self, alkio):

        for i in range(self.alkioiden_lkm):
            if alkio == self.ljono[i]:
                self.ljono[i] = 0
                for j in range(i, self.alkioiden_lkm - 1):
                    apu = self.ljono[j]
                    self.ljono[j] = self.ljono[j + 1]
                    self.ljono[j + 1] = apu
                self.alkioiden_lkm = self.alkioiden_lkm - 1
                return True
            
        return False

    def kopioi_lista(self, copy_from, copy_to):
        for i in range(len(copy_from)):
            copy_to[i] = copy_from[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for i in range(len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(len(a_taulu)):
            for j in range(len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        else:
            tuotos = "{"
            for i in range(self.alkioiden_lkm - 1):
                tuotos += str(self.ljono[i])
                tuotos += ", "
            tuotos += str(self.ljono[self.alkioiden_lkm - 1])
            tuotos += "}"
            return tuotos