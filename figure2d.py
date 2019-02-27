import math

class Segitiga:

    def __init__(self, nama):
        self.nama = nama
        self.jumlah_sisi = 3
    
    def __str__(self):
        return "Segitiga " + self.nama + " (jumlah sisi = " + str(self.jumlah_sisi) + ")"
    
        
    
    
class Segiempat:

    def __init__(self, nama):
        self.nama = nama
        self.jumlah_sisi = 4

    def __str__(self):
        return "Segiempat " + self.nama + " (jumlah sisi = " + str(self.jumlah_sisi) + ")"

class Samasisi(Segitiga):

    def __init__(self, nama, sisi, tinggi):
        Segitiga.__init__(self, nama)
        self.sisi = sisi
        self.tinggi = tinggi

    def __str__ (self):
        return "Segitiga Samasisi " + self.nama

    def hitung_luas(self):
        return 0.5 * self.sisi * self.tinggi

    def hitung_keliling(self):
        return 3 * self.sisi

class Samakaki(Segitiga):

    def __init__(self, nama, alas, tinggi):
        Segitiga.__init__(self, nama)
        self.alas = alas
        self.tinggi = tinggi

    def __str__ (self):
        return "Segitiga Samakaki " + self.nama

    def hitung_luas(self):
        return 0.5 * self.alas * self.tinggi

    def hitung_keliling(self):
        return 2*math.sqrt(0.25 * self.alas**2 + self.tinggi**2)

class Persegi(Segiempat):

    def __init__(self, nama, panjang, lebar):
        Segiempat.__init__(self, nama)
        self.panjang = panjang
        self.lebar = lebar

    def __str__ (self):
        return "Persegi " + self.nama

    def hitung_luas(self):
        return self.panjang * self.lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

class Trapesium(Segiempat):

    def __init__(self, nama, alas, tutup, tinggi):
        Segiempat.__init__(self, nama)
        self.alas = alas
        self.tinggi = tinggi
        self.tutup = tutup
    
    def __str__ (self):
        return "Trapesium " + self.nama 

    def hitung_luas(self):
        return 0.5 * (self.alas + self.tutup) * self.tinggi

    def hitung_keliling(self):
        return self.alas + self.tutup + self.tinggi + math.sqrt((self.alas - self.tutup)**2 + self.tinggi**2)

class Jajargenjang(Segiempat):

    def __init__(self, nama, alas, tinggi, sudutLancip):
        Segiempat.__init__(self, nama)
        self.alas = alas
        self.tinggi = tinggi
        self.sudutLancip = sudutLancip

    def __str__ (self):
        return "Jajargenjang " + self.nama 

    def hitung_luas(self):
        return self.alas * self.tinggi

    def hitung_keliling(self):
        return 2*(self.alas + self.tinggi / math.sin(self.sudutLancip))


    
