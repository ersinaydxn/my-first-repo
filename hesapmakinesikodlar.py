#Hesap Makinesi Kodlama
#Terminalde ui dosyasının konumuna cd ile git.
#pyuic5 hesapmakinesi.ui -o hesapmakinesi.py   terminalde yazarak xml dosyasını py dosyasına çeviriyoruz.
#py dosyasını importluyoruz. ui mainwindowu alsak yetiyor asıl sınıf o

import sys
from PyQt5 import QtWidgets as qtw
from hesapmakinesi import Ui_MainWindow


#Uygulamadaki verileri almak için alttaki classı kurduk
class Uygulama(qtw.QMainWindow):
    sayi=None
    sayi2=False
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.sifir.clicked.connect(self.basmak)                             #self.ui.hangi nesneyi çağırdığın . clicked  buton olduğu için . connect içine fonksiyon çağırıyoruz.
        self.ui.bir.clicked.connect(self.basmak)
        self.ui.iki.clicked.connect(self.basmak)
        self.ui.uc.clicked.connect(self.basmak)
        self.ui.dort.clicked.connect(self.basmak)
        self.ui.bes.clicked.connect(self.basmak)
        self.ui.alti.clicked.connect(self.basmak)
        self.ui.yedi.clicked.connect(self.basmak)
        self.ui.sekiz.clicked.connect(self.basmak)
        self.ui.dokuz.clicked.connect(self.basmak)
        self.ui.yuzde.clicked.connect(self.yuzde)
        self.ui.toplama.clicked.connect(self.matematik)
        self.ui.cikarma.clicked.connect(self.matematik)
        self.ui.carpma.clicked.connect(self.matematik)
        self.ui.bolme.clicked.connect(self.matematik)
        self.ui.sil.clicked.connect(self.temizle)
        self.ui.geri.clicked.connect(self.geri)
        self.ui.virgul.clicked.connect(self.ondalik)
        self.ui.esittir.clicked.connect(self.hesapla)
        self.ui.isaret.clicked.connect(self.isaret)

        self.ui.toplama.setCheckable(True)
        self.ui.cikarma.setCheckable(True)
        self.ui.bolme.setCheckable(True)
        self.ui.carpma.setCheckable(True)
        self.ui.esittir.setCheckable(True)

    def basmak(self):
        buton=self.sender()                                 #Basılan her bilgiyi buton değişkenine gönderdik
        if ((self.sayi2) and (self.ui.esittir.isChecked())):
            self.ui.sonuc.setText(format(float(buton.text()),'.15g'))  # Set text ile ekrana basılan tuşu float ve format şeklinde gönderdik 15g dediğimiz 0'ı kaldırıyor ortadan.
            self.sayi2=True
            self.ui.esittir.setChecked(False)

        elif ((self.ui.toplama.isChecked() or self.ui.cikarma.isChecked() or self.ui.carpma.isChecked() or self.ui.bolme.isChecked()) and (not self.sayi2)):
            self.ui.sonuc.setText(format(float(buton.text()),'.15g'))
            self.sayi2=True

        else:
            if (("." in self.ui.sonuc.text() and buton.text()=="0")):
                self.ui.sonuc.setText(format(float(self.ui.sonuc.text() + buton.text())))
            else:
                self.ui.sonuc.setText(format(float(self.ui.sonuc.text() + buton.text()),'.15g'))


    def ondalik(self):
        if "." not in self.ui.sonuc.text():
            self.ui.sonuc.setText(self.ui.sonuc.text() + ".")

    def isaret (self):
        deger=float(self.ui.sonuc.text())*-1
        self.ui.sonuc.setText(format(deger,'.15g'))

    def yuzde(self):
        deger=float(self.ui.sonuc.text())*0.01
        self.ui.sonuc.setText(format(deger,'.15g'))

    def temizle(self):
        self.sayi=0
        self.sayi2=False
        self.ui.sonuc.setText("0")
        self.ui.toplama.setChecked(False)
        self.ui.cikarma.setChecked(False)
        self.ui.carpma.setChecked(False)                        #Temizleye bastıktan sonra bu işaretlere basarsan o an işlem yapmasın diye döndürdük.
        self.ui.bolme.setChecked(False)
        self.ui.esittir.setChecked(False)

    def matematik(self):
        buton=self.sender()
        self.sayi=float(self.ui.sonuc.text())
        buton.setChecked(True)

    def hesapla(self):
        self.sayi2=float(self.ui.sonuc.text())
        if self.ui.toplama.isChecked():
            yenideger=self.sayi+self.sayi2
            self.ui.sonuc.setText(format(yenideger,".15g"))
            self.ui.toplama.setChecked(False)

        elif self.ui.cikarma.isChecked():
            yenideger=self.sayi-self.sayi2
            self.ui.sonuc.setText(format(yenideger,".15g"))
            self.ui.cikarma.setChecked(False)

        elif self.ui.carpma.isChecked():
            yenideger=self.sayi*self.sayi2
            self.ui.sonuc.setText(format(yenideger,".15g"))
            self.ui.carpma.setChecked(False)

        elif self.ui.bolme.isChecked():
            yenideger=self.sayi/self.sayi2
            self.ui.sonuc.setText(format(yenideger,".15g"))
            self.ui.bolme.setChecked(False)

        self.sayi=yenideger
        self.ui.esittir.setChecked(True)

    def geri(self):
        ekran=self.ui.sonuc.text()
        if len(ekran) > 1:
            self.ui.sonuc.setText(format(float(ekran[:-1]), '.15g'))
        else:
            self.ui.sonuc.setText("0")


#Uygulamanın açılması için yazılan fonksiyon
def app():
    app=qtw.QApplication(sys.argv)
    win=Uygulama()
    win.show()
    sys.exit(app.exec_())
app()
