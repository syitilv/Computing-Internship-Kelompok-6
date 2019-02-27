import math

class Kubus:
    jumlah_sisi = 6
    def __init__(self, sisi):
        self.sisi = sisi
        self.luas = 0
        self.volume = 0

    def hitungLuas(self):
        s = self.sisi
        self.luas = 6 * s * s
        return (self.luas)

    def hitungVolume(self):
        s = self.sisi
        self.volume = s * s * s
        return (self.volume)

class Balok:
    jumlah_sisi = 6
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def hitungLuas(self):
        pl = self.panjang * self.lebar
        pt = self.panjang * self.tinggi
        lt = self.lebar * self.tinggi
        self.luas = 2 * (pl+pt+lt)
        return (self.luas)

    def hitungVolume(self):
        p = self.panjang
        l = self.lebar
        t = self.tinggi
        self.volume = p*l*t
        return (self.volume)

class Tabung:
    jumlah_sisi = 3
    def __init__(self, jari2, tinggi):
        self.jari2 = jari2
        self.tinggi = tinggi
    
    def hitungLuas(self):
        r = self.jari2
        t = self.tinggi
        rt = r+t
        self.luas = 2*math.pi*r*rt
        return(self.luas)
    
    def hitungVolume(self):
        r = self.jari2
        t = self.tinggi
        self.volume = math.pi*r*r*t
        return(self.volume)

class Kerucut:
    jumlah_sisi = 2
    def __init__(self, jari2, tinggi):
        self.jari2 = jari2
        self.tinggi = tinggi

    def hitungLuas(self):
        r = self.jari2
        t = self.tinggi
        rr = r * r
        tt = t * t
        sisi = math.sqrt(rr+tt)
        rs = r + sisi
        self.luas = math.pi*r*rs
        return(self.luas)

    def hitungVolume(self):
        r = self.jari2
        t = self.tinggi
        self.volume = 1/3*(math.pi*r*r*t)
        return(self.volume)
