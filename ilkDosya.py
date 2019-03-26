import time
class Makine():
    def __init__(self):
        self.devir = 0
        self.mürekkep = 100
        self.şarj = 100
        self.dergiler = []
    def çalış(self):
        if(self.mürekkep <=0):
            print("Hata! Mürekkep yetersiz.")
            time.sleep(2)
        elif(self.şarj<=0):
            print("Hata şarj yetersiz.")
            time.sleep(2)
        else:
            self.devir += 1
            if(self.mürekkep<6):
                self.mürekkep = 0
            else:
                self.mürekkep -= 3
            if(self.şarj>6):
                self.şarj = 0
            self.şarj -= 6
            print("Makine çalışıyor lütfen bekleyiniz...")
            time.sleep(0.5)
            if(self.devir==20):
                self.devir = 0
                self.yeniDergi()
    def yeniDergi(self):
        print("Yeni dergi çıktı hayırlı olsun.")
        a = input("Derginin ismi ne olsun?")
        self.dergiler.append(a)
        time.sleep(2)

    def şarjDoldur(self):
        if(self.şarj<100):
            self.şarj += 10
            print("Şarj dolduruldu. Mevcut şarj durumu :",self.şarj)
            time.sleep(2)
    def mürekkepDoldur(self):
        if(self.mürekkep<100):
            self.mürekkep +=10
            print("Mürekkep dolduruldu. Mevcut mürekkep :",self.mürekkep)

    def mevcutDurum(self):
        print("Makinenin Mevcut Durumu :")
        print("Kalan Mürekkep Miktarı :",self.mürekkep)
        print("Kalan Şarj Durumu :",self.şarj)
        print("Toplam çıkarılan dergi sayısı :",len(self.dergiler))
        if(len(self.dergiler)>0):
            print("Çıkarılan Dergiler :")
            for i in self.dergiler:
                print(i)
        print("Yeni çıkan derginin %",self.devir*5,"kısmı tamamlandı.")
        time.sleep(4)
makine1 = Makine()


print("Matbaamıza Hoşgeldiniz!")
while True:
    print("-"*15)
    print("Makineyi çalıştırmak için : 1\nMevcut Durumu öğrenmek için : 2\nMakinenin şarjını doldurmak için : 3\nMakinenin mürekkebini doldurmak için : 4")

    komut = input()
    if(komut=="1"):
        makine1.çalış()
    elif(komut=="2"):
        makine1.mevcutDurum()
    elif(komut=="3"):
        makine1.şarjDoldur()
    elif(komut=="4"):
        makine1.mürekkepDoldur()
