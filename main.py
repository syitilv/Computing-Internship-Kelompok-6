from vehicle import *

P1 = vehicle(2010, 120000000)
C1 = car(4, 6)
C1.data = P1
hasil = C1.pay_tax(C1.data.price)
print ("Pajak dari mobil tahun {} dengan harga Rp {},00 adalah sebesar Rp{},00".format(P1.year, P1.price, hasil))
print ("Mobil ini parkir selama 5 jam, maka harus membayar Rp{},00\n".format(C1.park(5)))

P2 = vehicle(2017, 22000000)
C2 = motorbike(2,2)
C2.data = P2
hasil = C2.pay_tax(C2.data.price)
print ("Pajak dari Sepeda Motor tahun {} dengan harga Rp {},00 adalah sebesar Rp{},00".format(P2.year, P2.price, hasil))
print ("Sepeda Moto ini parkir selama 5 jam, maka harus membayar Rp{},00\n".format(C2.park(5)))

P3 = vehicle(2015, 1500000)
C3 = bicycle(2,1)
C3.data = P3
hasil = C3.pay_tax(C3.data.price)
print ("Pajak dari Sepeda tahun {} dengan harga Rp {},00 adalah sebesar Rp{},00".format(P3.year, P3.price, hasil))
print ("Sepeda ini parkir selama 5 jam, maka harus membayar Rp{},00".format(C3.park(5)))