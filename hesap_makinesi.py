
from tkinter import *
pencere = Tk()
pencere.title("CASIO")
pencere.geometry("270x240+300+100")
pencere.resizable(FALSE,FALSE)

depo = ""

def hesapla(tus):
  global depo # tum islemler deponun icersinde gerceklesiyor
  if tus in "0123456789": #kullanici bu rakamlardan bir tusa tikladiginda
    ekran.insert(END, tus) # tiklanilan tusun rakami gorunmesi icin ve her seferinde sonuna eklemeli
    depo = depo + tus # yazilan rakam deponun icersine atilmali
    
  if tus in "+-/*": # burda da matematiksel simgeyi aktive etmek icin
    ekran.insert(END,tus) # ekarnin bosalmasi icin yani islemi devam etmak icin
    depo = depo + tus # bu islemi de deponun icine gonderiyoruz
    
    # esittir simgesine aktive ediyoruz
  if tus == "=": # esittire tiklandiysa esittir demekdir 
    ekran.delete(0,END) # yeni deger geldigi icin ekrani temizlememiz lazim bastan sona kadr
    hesap = eval(depo, {" __builtins__":None},{}) # eval fonks kullanarak hesaplamayi gerceklestiriyoruz
    depo = str(hesap) # islem gerceklestikten sonra deponun icine str olarak attik
    ekran.insert(END,depo) # burda da ekranda gostermesi icin 
  #   # c tusu gercaklestirme yani silme
  if tus == "C": # kullanici c tusuna bastiya 
    ekran.delete(0,END) # ekran temizlenecek
    depo = "" # dogal olarak depoyu da temizliyoruz bu sekilde
    

ekran = Entry(width=25, justify=RIGHT)
ekran.grid(row=0,column=0,columnspan=120,ipady=8)

liste = ["1","2","3","4","5","6","7","8","9","0","+","-","/","*","=","C"]

sira = 1
sutun = 0

for i in liste:
  komut = lambda x=i : hesapla(x)
  Button(text=i, font="verdana 8 bold",width=9,height=2, relief=RAISED,command=komut).grid(row=sira,column=sutun)
  sutun += 1 # sutun degerini 1 artirdik ust uste gelmemesi icin
  if sutun >2: # sutun 2 den buyukse sutunu asdaki sifira esitleyecek yani 2 fazla sutunue gitmeyecek
    sutun = 0 # sifira esitle bir alt satira gectiginde sifinci sutunla baslamali
    sira +=1 # bi alt satira gecmesi icin her seferinde 1 artamasi gerekiyor
    
mainloop()




