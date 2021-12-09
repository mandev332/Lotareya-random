import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from random import *

class Omad_lotto(QWidget):
    def __init__(self):
        super().__init__()
        self.son=1
        self.s=0
        self.lotto=5
        self.jami=[]
        self.latatron()
        
   
    def latatron(self):
        self.ekran=QLineEdit(self)
        self.ekran.setGeometry(50, 70, 300, 50)
        self.setStyleSheet("background-color: wheat")
        self.ekran.setFont(QFont("PGothic",15))
        self.ekran.setStyleSheet("background-color: white; border : 3px solid blue; border-radius: 15px;")
        
        self.tanla1=QRadioButton(self)
        self.tanla1.move(50, 30)
        self.tanla1.setFont(QFont("PGothic",7))
        self.tanla1.setText("Omad (36/5)")
        self.tanla1.clicked.connect(self.ish)
        
        self.tanla2=QRadioButton(self)
        self.tanla2.move(160, 30)
        self.tanla2.setFont(QFont("PGothic",7))
        self.tanla2.setText("Sharqona (36/6)")
        self.tanla2.clicked.connect(self.ish)
        
        self.tanla3=QRadioButton(self)
        self.tanla3.move(320, 30)
        self.tanla3.setFont(QFont("PGothic",7))
        self.tanla3.setText("Super (36/7)")
        self.tanla3.clicked.connect(self.ish)
        
        self.pushq=QPushButton(self)
        self.pushq.setGeometry(360, 70, 70, 50)
        self.pushq.setStyleSheet("background-color: silver; border : 3px solid red; border-radius: 15px;")
        self.pushq.setFont(QFont("PGothic",20))
        self.pushq.setText("+")
        self.pushq.clicked.connect(self.qoshish)
        
        self.pushs=QPushButton(self)
        self.pushs.setGeometry(480, 20, 70, 40)
        self.pushs.setStyleSheet("background-color: silver; border : 3px solid green; border-radius: 15px;")
        self.pushs.setFont(QFont("PGothic",7))
        self.pushs.setText("Start")
        self.pushs.clicked.connect(self.start)
        
        self.push1=QPushButton(self)
        self.push1.setGeometry(50, 140, 50, 50)
        self.push1.setStyleSheet("background-color: pink; border : 3px solid brown; border-radius: 25px;")
        self.push1.setFont(QFont("PGothic",20))
        self.push1.setText("1")
        self.push1.clicked.connect(self.push_1)
        
        self.push2=QPushButton(self)
        self.push2.setGeometry(115, 140, 50, 50)
        self.push2.setStyleSheet("background-color: pink; border : 3px solid brown; border-radius: 25px;")
        self.push2.setFont(QFont("PGothic",20))
        self.push2.setText("2")
        self.push2.clicked.connect(self.push_2)
        
        self.push3=QPushButton(self)
        self.push3.setGeometry(180, 140, 50, 50)
        self.push3.setStyleSheet("background-color: pink; border : 3px solid brown; border-radius: 25px;")
        self.push3.setFont(QFont("PGothic",20))
        self.push3.setText("3")
        self.push3.clicked.connect(self.push_3)
        
        self.push4=QPushButton(self)
        self.push4.setGeometry(245, 140, 50, 50)
        self.push4.setStyleSheet("background-color: pink; border : 3px solid brown; border-radius: 25px;")
        self.push4.setFont(QFont("PGothic",20))
        self.push4.setText("4")
        self.push4.clicked.connect(self.push_4)
        
        self.push5=QPushButton(self)
        self.push5.setGeometry(310, 140, 50, 50)
        self.push5.setStyleSheet("background-color: pink; border : 3px solid brown; border-radius: 25px;")
        self.push5.setFont(QFont("PGothic",20))
        self.push5.setText("5")
        self.push5.clicked.connect(self.push_5)
        
        self.push6=QPushButton(self)
        self.push6.setGeometry(375, 140, 50, 50)
        self.push6.setStyleSheet("background-color: pink; border : 3px solid brown; border-radius: 25px;")
        self.push6.setFont(QFont("PGothic",20))
        self.push6.setText("6")
        self.push6.clicked.connect(self.push_6)
                
        self.push7=QPushButton(self)
        self.push7.setGeometry(50, 205, 50, 50)
        self.push7.setStyleSheet("background-color: pink; border : 3px solid brown; border-radius: 25px;")
        self.push7.setFont(QFont("PGothic",20))
        self.push7.setText("7")
        self.push7.clicked.connect(self.push_7)
        
        self.push8=QPushButton(self)
        self.push8.setGeometry(115, 205, 50, 50)
        self.push8.setStyleSheet("background-color: pink; border : 3px solid brown; border-radius: 25px;")
        self.push8.setFont(QFont("PGothic",20))
        self.push8.setText("8")
        self.push8.clicked.connect(self.push_8)
        
        self.push9=QPushButton(self)
        self.push9.setGeometry(180, 205, 50, 50)
        self.push9.setStyleSheet("background-color: pink; border : 3px solid brown; border-radius: 25px;")
        self.push9.setFont(QFont("PGothic",20))
        self.push9.setText("9")
        self.push9.clicked.connect(self.push_9)
        
        self.push10=QPushButton(self)
        self.push10.setGeometry(245, 205, 50, 50)
        self.push10.setStyleSheet("background-color: pink; border : 3px solid brown; border-radius: 25px;")
        self.push10.setFont(QFont("PGothic",20))
        self.push10.setText("10")
        self.push10.clicked.connect(self.push_10)
        
        self.push11=QPushButton(self)
        self.push11.setGeometry(310, 205, 50, 50)
        self.push11.setStyleSheet("background-color: pink; border : 3px solid brown; border-radius: 25px;")
        self.push11.setFont(QFont("PGothic",20))
        self.push11.setText("11")
        self.push11.clicked.connect(self.push_11)
        
        self.push12=QPushButton(self)
        self.push12.setGeometry(375, 205, 50, 50)
        self.push12.setStyleSheet("background-color: pink; border : 3px solid brown; border-radius: 25px;")
        self.push12.setFont(QFont("PGothic",20))
        self.push12.setText("12")
        self.push12.clicked.connect(self.push_12)
        
        self.push13=QPushButton(self)
        self.push13.setGeometry(50, 270, 50, 50)
        self.push13.setStyleSheet("background-color: pink; border : 3px solid brown; border-radius: 25px;")
        self.push13.setFont(QFont("PGothic",20))
        self.push13.setText("13")
        self.push13.clicked.connect(self.push_13)
        
        self.push14=QPushButton(self)
        self.push14.setGeometry(115, 270, 50, 50)
        self.push14.setStyleSheet("background-color: pink; border : 3px solid brown; border-radius: 25px;")
        self.push14.setFont(QFont("PGothic",20))
        self.push14.setText("14")
        self.push14.clicked.connect(self.push_14)
        
        self.push15=QPushButton(self)
        self.push15.setGeometry(180, 270, 50, 50)
        self.push15.setStyleSheet("background-color: pink; border : 3px solid brown; border-radius: 25px;")
        self.push15.setFont(QFont("PGothic",20))
        self.push15.setText("15")
        self.push15.clicked.connect(self.push_15)
        
        self.push16=QPushButton(self)
        self.push16.setGeometry(245, 270, 50, 50)
        self.push16.setStyleSheet("background-color: pink; border : 3px solid brown; border-radius: 25px;")
        self.push16.setFont(QFont("PGothic",20))
        self.push16.setText("16")
        self.push16.clicked.connect(self.push_16)
        
        self.push17=QPushButton(self)
        self.push17.setGeometry(310, 270, 50, 50)
        self.push17.setStyleSheet("background-color: pink; border : 3px solid brown; border-radius: 25px;")
        self.push17.setFont(QFont("PGothic",20))
        self.push17.setText("17")
        self.push17.clicked.connect(self.push_17)
        
        self.push18=QPushButton(self)
        self.push18.setGeometry(375, 270, 50, 50)
        self.push18.setStyleSheet("background-color: pink; border : 3px solid brown; border-radius: 25px;")
        self.push18.setFont(QFont("PGothic",20))
        self.push18.setText("18")
        self.push18.clicked.connect(self.push_18)
                
        self.push19=QPushButton(self)
        self.push19.setGeometry(50, 335, 50, 50)
        self.push19.setStyleSheet("background-color: pink; border : 3px solid brown; border-radius: 25px;")
        self.push19.setFont(QFont("PGothic",20))
        self.push19.setText("19")
        self.push19.clicked.connect(self.push_19)
        
        self.push20=QPushButton(self)
        self.push20.setGeometry(115, 335, 50, 50)
        self.push20.setStyleSheet("background-color: pink; border : 3px solid brown; border-radius: 25px;")
        self.push20.setFont(QFont("PGothic",20))
        self.push20.setText("20")
        self.push20.clicked.connect(self.push_20)
        
        self.push21=QPushButton(self)
        self.push21.setGeometry(180, 335, 50, 50)
        self.push21.setStyleSheet("background-color: pink; border : 3px solid brown; border-radius: 25px;")
        self.push21.setFont(QFont("PGothic",20))
        self.push21.setText("21")
        self.push21.clicked.connect(self.push_21)
        
        self.push22=QPushButton(self)
        self.push22.setGeometry(245, 335, 50, 50)
        self.push22.setStyleSheet("background-color: pink; border : 3px solid brown; border-radius: 25px;")
        self.push22.setFont(QFont("PGothic",20))
        self.push22.setText("22")
        self.push22.clicked.connect(self.push_22)
        
        self.push23=QPushButton(self)
        self.push23.setGeometry(310, 335, 50, 50)
        self.push23.setStyleSheet("background-color: pink; border : 3px solid brown; border-radius: 25px;")
        self.push23.setFont(QFont("PGothic",20))
        self.push23.setText("23")
        self.push23.clicked.connect(self.push_23)
        
        self.push24=QPushButton(self)
        self.push24.setGeometry(375, 335, 50, 50)
        self.push24.setStyleSheet("background-color: pink; border : 3px solid brown; border-radius: 25px;")
        self.push24.setFont(QFont("PGothic",20))
        self.push24.setText("24")
        self.push24.clicked.connect(self.push_24)
        
        self.push25=QPushButton(self)
        self.push25.setGeometry(50, 400, 50, 50)
        self.push25.setStyleSheet("background-color: pink; border : 3px solid brown; border-radius: 25px;")
        self.push25.setFont(QFont("PGothic",20))
        self.push25.setText("25")
        self.push25.clicked.connect(self.push_25)
        
        self.push26=QPushButton(self)
        self.push26.setGeometry(115, 400, 50, 50)
        self.push26.setStyleSheet("background-color: pink; border : 3px solid brown; border-radius: 25px;")
        self.push26.setFont(QFont("PGothic",20))
        self.push26.setText("26")
        self.push26.clicked.connect(self.push_26)
        
        self.push27=QPushButton(self)
        self.push27.setGeometry(180, 400, 50, 50)
        self.push27.setStyleSheet("background-color: pink; border : 3px solid brown; border-radius: 25px;")
        self.push27.setFont(QFont("PGothic",20))
        self.push27.setText("27")
        self.push27.clicked.connect(self.push_27)
        
        self.push28=QPushButton(self)
        self.push28.setGeometry(245, 400, 50, 50)
        self.push28.setStyleSheet("background-color: pink; border : 3px solid brown; border-radius: 25px;")
        self.push28.setFont(QFont("PGothic",20))
        self.push28.setText("28")
        self.push28.clicked.connect(self.push_28)
        
        self.push29=QPushButton(self)
        self.push29.setGeometry(310, 400, 50, 50)
        self.push29.setStyleSheet("background-color: pink; border : 3px solid brown; border-radius: 25px;")
        self.push29.setFont(QFont("PGothic",20))
        self.push29.setText("29")
        self.push29.clicked.connect(self.push_29)
        
        self.push30=QPushButton(self)
        self.push30.setGeometry(375, 400, 50, 50)
        self.push30.setStyleSheet("background-color: pink; border : 3px solid brown; border-radius: 25px;")
        self.push30.setFont(QFont("PGothic",20))
        self.push30.setText("30")
        self.push30.clicked.connect(self.push_30)
                
        self.push31=QPushButton(self)
        self.push31.setGeometry(50, 465, 50, 50)
        self.push31.setStyleSheet("background-color: pink; border : 3px solid brown; border-radius: 25px;")
        self.push31.setFont(QFont("PGothic",20))
        self.push31.setText("31")
        self.push31.clicked.connect(self.push_31)
        
        self.push32=QPushButton(self)
        self.push32.setGeometry(115, 465, 50, 50)
        self.push32.setStyleSheet("background-color: pink; border : 3px solid brown; border-radius: 25px;")
        self.push32.setFont(QFont("PGothic",20))
        self.push32.setText("32")
        self.push32.clicked.connect(self.push_32)
        
        self.push33=QPushButton(self)
        self.push33.setGeometry(180, 465, 50, 50)
        self.push33.setStyleSheet("background-color: pink; border : 3px solid brown; border-radius: 25px;")
        self.push33.setFont(QFont("PGothic",20))
        self.push33.setText("33")
        self.push33.clicked.connect(self.push_33)
        
        self.push34=QPushButton(self)
        self.push34.setGeometry(245, 465, 50, 50)
        self.push34.setStyleSheet("background-color: pink; border : 3px solid brown; border-radius: 25px;")
        self.push34.setFont(QFont("PGothic",20))
        self.push34.setText("34")
        self.push34.clicked.connect(self.push_34)
        
        self.push35=QPushButton(self)
        self.push35.setGeometry(310, 465, 50, 50)
        self.push35.setStyleSheet("background-color: pink; border : 3px solid brown; border-radius: 25px;")
        self.push35.setFont(QFont("PGothic",20))
        self.push35.setText("35")
        self.push35.clicked.connect(self.push_35)
        
        self.push36=QPushButton(self)
        self.push36.setGeometry(375, 465, 50, 50)
        self.push36.setStyleSheet("background-color: pink; border : 3px solid brown; border-radius: 25px;")
        self.push36.setFont(QFont("PGothic",20))
        self.push36.setText("36")
        self.push36.clicked.connect(self.push_36)
        
        self.tele=QPushButton(self)
        self.tele.setGeometry(50, 550, 180, 30)
        self.t=QGraphicsColorizeEffect()
        self.tele.setGraphicsEffect(self.t)
        self.tele.setText("Telegramm")
        self.tele.setStyleSheet("background-color: silver; border : 3px solid blue; border-radius: 15px;")
        self.tele.setFont(QFont("PGothic",7))
        self.tele.clicked.connect(self.telegramm)
        
        self.you=QPushButton(self)
        self.you.setGeometry(250, 550, 180, 30)
        self.y=QGraphicsColorizeEffect()
        self.you.setGraphicsEffect(self.y)
        self.you.setText("YOU TUBE")
        self.you.setStyleSheet("background-color: turquoise; border : 3px solid blue; border-radius: 15px;")
        self.you.setFont(QFont("PGothic",7))
        self.you.clicked.connect(self.youtube)
        
        self.lis=QListWidget(self)
        self.lis.setGeometry(480,70, 500, 400)
        self.lis.setFont(QFont("PGothic",20))
        self.lis.setStyleSheet("background-color: white; border : 3px solid black; border-radius: 15px;")
        
        self.num1=QLineEdit(self)
        self.num1.setGeometry(560, 20, 40, 40)
        self.num1.setFont(QFont("PGothic",10))
        self.num1.setStyleSheet("background-color: orange; border : 3px solid black; border-radius: 20px;")
    
        self.num2=QLineEdit(self)
        self.num2.setGeometry(620, 20, 40, 40)
        self.num2.setFont(QFont("PGothic",10))
        self.num2.setStyleSheet("background-color: orange; border : 3px solid black; border-radius: 20px;")
    
        self.num3=QLineEdit(self)
        self.num3.setGeometry(680, 20, 40, 40)
        self.num3.setFont(QFont("PGothic",10))
        self.num3.setStyleSheet("background-color: orange; border : 3px solid black; border-radius: 20px;")
    
        self.num4=QLineEdit(self)
        self.num4.setGeometry(740, 20, 40, 40)
        self.num4.setFont(QFont("PGothic",10))
        self.num4.setStyleSheet("background-color: orange; border : 3px solid black; border-radius: 20px;")
    
        self.num5=QLineEdit(self)
        self.num5.setGeometry(800, 20, 40, 40)
        self.num5.setFont(QFont("PGothic",10))
        self.num5.setStyleSheet("background-color: orange; border : 3px solid black; border-radius: 20px;")
    
        self.num6=QLineEdit(self)
        self.num6.setGeometry(860, 20, 40, 40)
        self.num6.setFont(QFont("PGothic",10))
        self.num6.setStyleSheet("background-color: orange; border : 3px solid black; border-radius: 20px;")
    
        self.num7=QLineEdit(self)
        self.num7.setGeometry(920, 20, 40, 40)
        self.num7.setFont(QFont("PGothic",10))
        self.num7.setStyleSheet("background-color: orange; border : 3px solid black; border-radius: 20px;")
      
        self.yut=QLabel(self)
        self.yut.setGeometry(480, 500, 500, 70)
        self.yut.setText("_______________________________________________________________________")
        
        
    def push_1(self):
        self.toxta()
        son=self.push1.text()
        if self.s<=self.lotto:
            self.ekran.setText(self.ekran.text()+son+" ")
        self.push1.setEnabled(False)
        self.s+=1
        
    def push_2(self):
        self.toxta()
        son=self.push2.text()
        if self.s<=self.lotto:
            self.ekran.setText(self.ekran.text()+son+" ")        
        self.push2.setEnabled(False)
        self.s+=1
        
    def push_3(self):
        self.toxta()
        son=self.push3.text()
        if self.s<=self.lotto:
            self.ekran.setText(self.ekran.text()+son+" ")
        self.push3.setEnabled(False)
        self.s+=1
        
    def push_4(self):
        self.toxta()
        son=self.push4.text()
        if self.s<=self.lotto:
            self.ekran.setText(self.ekran.text()+son+" ")
        self.push4.setEnabled(False)
        self.s+=1
        
    def push_5(self):
        self.toxta()
        son=self.push5.text()
        if self.s<=self.lotto:
            self.ekran.setText(self.ekran.text()+son+" ")
        self.push5.setEnabled(False)
        self.s+=1
    def push_6(self):
        self.toxta()
        son=self.push6.text()
        if self.s<=self.lotto:
            self.ekran.setText(self.ekran.text()+son+" ")
        self.push6.setEnabled(False)
        self.s+=1
        
    def push_7(self):
        self.toxta()
        son=self.push7.text()
        if self.s<=self.lotto:
            self.ekran.setText(self.ekran.text()+son+" ")
        self.push7.setEnabled(False)
        self.s+=1
        
    def push_8(self):
        self.toxta()
        son=self.push8.text()
        if self.s<=self.lotto:
            self.ekran.setText(self.ekran.text()+son+" ")
        self.push8.setEnabled(False)
        self.s+=1
        
    def push_9(self):
        self.toxta()
        son=self.push9.text()
        if self.s<=self.lotto:
            self.ekran.setText(self.ekran.text()+son+" ")
        self.push9.setEnabled(False)
        self.s+=1
        
    def push_10(self):
        self.toxta()
        son=self.push10.text()
        if self.s<=self.lotto:
            self.ekran.setText(self.ekran.text()+son+" ")
        self.push10.setEnabled(False)
        self.s+=1
        
    def push_11(self):
        self.toxta()
        son=self.push11.text()
        if self.s<=self.lotto:
            self.ekran.setText(self.ekran.text()+son+" ")
        self.push11.setEnabled(False)
        self.s+=1
        
    def push_12(self):
        self.toxta()
        son=self.push12.text()
        if self.s<=self.lotto:
            self.ekran.setText(self.ekran.text()+son+" ")
        self.push12.setEnabled(False)
        self.s+=1
        
    def push_13(self):
        self.toxta()
        son=self.push13.text()
        if self.s<=self.lotto:
            self.ekran.setText(self.ekran.text()+son+" ")
        self.push13.setEnabled(False)
        self.s+=1
        
    def push_14(self):
        self.toxta()
        son=self.push14.text()
        if self.s<=self.lotto:
            self.ekran.setText(self.ekran.text()+son+" ")
        self.push14.setEnabled(False)
        self.s+=1
        
    def push_15(self):
        self.toxta()
        son=self.push15.text()
        if self.s<=self.lotto:
            self.ekran.setText(self.ekran.text()+son+" ")
        self.push15.setEnabled(False)
        self.s+=1
        
    def push_16(self):
        self.toxta()
        son=self.push16.text()
        if self.s<=self.lotto:
            self.ekran.setText(self.ekran.text()+son+" ")
        self.push16.setEnabled(False)
        self.s+=1
        
    def push_17(self):
        self.toxta()
        son=self.push17.text()
        if self.s<=self.lotto:
            self.ekran.setText(self.ekran.text()+son+" ")
        self.push17.setEnabled(False)
        self.s+=1
        
    def push_18(self):
        self.toxta()
        son=self.push18.text()
        if self.s<=self.lotto:
            self.ekran.setText(self.ekran.text()+son+" ")
        self.push18.setEnabled(False)
        self.s+=1
        
    def push_19(self):
        self.toxta()
        son=self.push19.text()
        if self.s<=self.lotto:
            self.ekran.setText(self.ekran.text()+son+" ")
        self.push19.setEnabled(False)
        self.s+=1
        
    def push_20(self):
        self.toxta()
        son=self.push20.text()
        if self.s<=self.lotto:
            self.ekran.setText(self.ekran.text()+son+" ")
        self.push20.setEnabled(False)
        self.s+=1
        
    def push_21(self):
        self.toxta()
        son=self.push21.text()
        if self.s<=self.lotto:
            self.ekran.setText(self.ekran.text()+son+" ")
        self.push21.setEnabled(False)
        self.s+=1
        
    def push_22(self):
        self.toxta()
        son=self.push22.text()
        if self.s<=self.lotto:
            self.ekran.setText(self.ekran.text()+son+" ")
        self.push22.setEnabled(False)
        self.s+=1
        
    def push_23(self):
        self.toxta()
        son=self.push23.text()
        if self.s<=self.lotto:
            self.ekran.setText(self.ekran.text()+son+" ")
        self.push23.setEnabled(False)
        self.s+=1
        
    def push_24(self):
        self.toxta()
        son=self.push24.text()
        if self.s<=self.lotto:
            self.ekran.setText(self.ekran.text()+son+" ")
        self.push24.setEnabled(False)
        self.s+=1
        
    def push_25(self):
        self.toxta()
        son=self.push25.text()
        if self.s<=self.lotto:
            self.ekran.setText(self.ekran.text()+son+" ")
        self.push25.setEnabled(False)
        self.s+=1
        
    def push_26(self):
        self.toxta()
        son=self.push26.text()
        if self.s<=self.lotto:
            self.ekran.setText(self.ekran.text()+son+" ")
        self.push26.setEnabled(False)
        self.s+=1
        
    def push_27(self):
        self.toxta()
        son=self.push27.text()
        if self.s<=self.lotto:
            self.ekran.setText(self.ekran.text()+son+" ")
        self.push27.setEnabled(False)
        self.s+=1
        
    def push_28(self):
        self.toxta()
        son=self.push28.text()
        if self.s<=self.lotto:
            self.ekran.setText(self.ekran.text()+son+" ")
        self.push28.setEnabled(False)
        self.s+=1
        
    def push_29(self):
        self.toxta()
        son=self.push29.text()
        if self.s<=self.lotto:
            self.ekran.setText(self.ekran.text()+son+" ")
        self.push29.setEnabled(False)
        self.s+=1
        
    def push_30(self):
        self.toxta()
        son=self.push30.text()
        if self.s<=self.lotto:
            self.ekran.setText(self.ekran.text()+son+" ")
        self.push30.setEnabled(False)
        self.s+=1
        
    def push_31(self):
        self.toxta()
        son=self.push31.text()
        if self.s<=self.lotto:
            self.ekran.setText(self.ekran.text()+son+" ")
        self.push31.setEnabled(False)
        self.s+=1
        
    def push_32(self):
        self.toxta()
        son=self.push32.text()
        if self.s<=self.lotto:
            self.ekran.setText(self.ekran.text()+son+" ")
        self.push32.setEnabled(False)
        self.s+=1
        
    def push_33(self):
        self.toxta()
        son=self.push33.text()
        if self.s<=self.lotto:
            self.ekran.setText(self.ekran.text()+son+" ")
        self.push33.setEnabled(False)
        self.s+=1
        
    def push_34(self):
        self.toxta()
        son=self.push34.text()
        if self.s<=self.lotto:
            self.ekran.setText(self.ekran.text()+son+" ")
        self.push34.setEnabled(False)
        self.s+=1
        
    def push_35(self):
        self.toxta()
        son=self.push35.text()
        if self.s<=self.lotto:
            self.ekran.setText(self.ekran.text()+son+" ")
        self.push35.setEnabled(False)
        self.s+=1
        
    def push_36(self):
        self.toxta()
        son=self.push36.text()
        if self.s<=self.lotto:
            self.ekran.setText(self.ekran.text()+son+" ")
        self.push36.setEnabled(False)
        self.s+=1
    
    def qoshish(self):
        if self.s==self.lotto:
            self.s=0      
            self.lis.addItem(f"{self.son})"+self.ekran.text())
            self.jami.append(self.ekran.text())
            self.boshla()
            self.son+=1
        else:
            ch=str(self.lotto)
            xabar=QMessageBox()
            xabar.setText(f"{ch} ta son tanlang!")
            xabar.setIcon(QMessageBox.Critical)
            xabar.setWindowTitle("E'tibor bering!")
            xabar.exec_()
    
    def toxta(self):
        try:    
            if self.s==self.lotto-1:
                self.push1.setEnabled(False); self.push2.setEnabled(False); self.push3.setEnabled(False); self.push4.setEnabled(False) 
                self.push5.setEnabled(False); self.push6.setEnabled(False); self.push7.setEnabled(False); self.push8.setEnabled(False) 
                self.push9.setEnabled(False); self.push10.setEnabled(False);self.push11.setEnabled(False);self.push12.setEnabled(False) 
                self.push13.setEnabled(False);self.push14.setEnabled(False);self.push15.setEnabled(False);self.push16.setEnabled(False) 
                self.push17.setEnabled(False);self.push18.setEnabled(False);self.push19.setEnabled(False);self.push20.setEnabled(False) 
                self.push21.setEnabled(False);self.push22.setEnabled(False);self.push23.setEnabled(False);self.push24.setEnabled(False) 
                self.push25.setEnabled(False);self.push26.setEnabled(False);self.push27.setEnabled(False);self.push28.setEnabled(False) 
                self.push29.setEnabled(False);self.push30.setEnabled(False);self.push31.setEnabled(False);self.push32.setEnabled(False) 
                self.push33.setEnabled(False);self.push34.setEnabled(False);self.push35.setEnabled(False);self.push36.setEnabled(False) 
        
        except :
            
            xabar=QMessageBox()
            xabar.setText("Oyin turini tanlang!")
            xabar.setIcon(QMessageBox.Warning)
            xabar.setWindowTitle("Eslatma!")
            xabar.exec_()
            
    def boshla(self):
        self.ekran.setText("")
        self.push1.setEnabled(True) ; self.push2.setEnabled(True); self.push3.setEnabled(True) ; self.push4.setEnabled(True) 
        self.push5.setEnabled(True) ; self.push6.setEnabled(True); self.push7.setEnabled(True) ; self.push8.setEnabled(True) 
        self.push9.setEnabled(True) ; self.push10.setEnabled(True);self.push11.setEnabled(True); self.push12.setEnabled(True) 
        self.push13.setEnabled(True); self.push14.setEnabled(True);self.push15.setEnabled(True); self.push16.setEnabled(True) 
        self.push17.setEnabled(True); self.push18.setEnabled(True);self.push19.setEnabled(True); self.push20.setEnabled(True) 
        self.push21.setEnabled(True); self.push22.setEnabled(True);self.push23.setEnabled(True); self.push24.setEnabled(True) 
        self.push25.setEnabled(True); self.push26.setEnabled(True);self.push27.setEnabled(True); self.push28.setEnabled(True) 
        self.push29.setEnabled(True); self.push30.setEnabled(True);self.push31.setEnabled(True); self.push32.setEnabled(True) 
        self.push33.setEnabled(True); self.push34.setEnabled(True);self.push35.setEnabled(True); self.push36.setEnabled(True) 
            
    def ish(self):
        if self.tanla1.isChecked():
            self.s=0
            self.lotto=5
            self.ekran.setText("")
            self.boshla()
        if self.tanla2.isChecked():
            self.s=0
            self.lotto=6
            self.ekran.setText("")
            self.boshla()
        if self.tanla3.isChecked():
            self.s=0
            self.lotto=7
            self.ekran.setText("")
            self.boshla()
            
    def start(self):
        sonlar=[]
        for i in range(self.lotto+5):
            shar = randint(1,36)
            if shar not in sonlar:
                sonlar.append(shar)
        if self.lotto==5:
            self.num1.setText(str(sonlar[0])); self.num2.setText(str(sonlar[1]))
            self.num3.setText(str(sonlar[2])); self.num4.setText(str(sonlar[3]))
            self.num5.setText(str(sonlar[4])); 
            self.num6.setText(""); self.num7.setText("")
        elif self.lotto==6:
            self.num1.setText(str(sonlar[0])); self.num2.setText(str(sonlar[1]))
            self.num3.setText(str(sonlar[2])); self.num4.setText(str(sonlar[3]))
            self.num5.setText(str(sonlar[4])); self.num6.setText(str(sonlar[5]))
            self.num7.setText("")
            
        elif self.lotto==7:
            self.num1.setText(str(sonlar[0])); self.num2.setText(str(sonlar[1]))
            self.num3.setText(str(sonlar[2])); self.num4.setText(str(sonlar[3]))
            self.num5.setText(str(sonlar[4])); self.num6.setText(str(sonlar[5]))
            self.num7.setText(str(sonlar[6]))
        else:
            xabar=QMessageBox()
            xabar.setText("Avval raqamlaringizni kiriting!")
            xabar.setIcon(QMessageBox.Information)
            xabar.setWindowTitle("Eslatma!")
            xabar.exec_()
        
        men=[]; x=[]; n=""
        for i in self.jami:
            for j in i:
                if j==" ":
                    x.append(int(n));  n=""
                else:
                    n+=j
            men.append(x); x=[]
        
        for i in men:
            if sorted(i)==sorted(sonlar):
                self.yut.setFont(QFont("PGothic",12))
                self.yut.setStyleSheet("background-color: pink; border : 3px solid green; border-radius: 25px;")
                self.yut.setText("  $$$ JECPOT YUTDINGIZ !!! TABRIKLAYMIZ !!! $$$")
            else:
                self.yut.setFont(QFont("PGothic",12))
                self.yut.setStyleSheet("background-color: green; border : 3px solid red; border-radius: 25px;")
                self.yut.setText("  BU SAFAR YUTILMADI YANA URINIB KO'RING!")

    def telegramm(self):
        os.system("start https://t.me/omadlottouz")
    def youtube(self):
        os.system("start https://www.youtube.com/watch?v=4RVKFW45W8Y")
        

apk=QApplication(sys.argv)
man=Omad_lotto()
man.setGeometry(150, 100, 1000, 600)
man.setWindowTitle("Lotto Show")
man.show()
sys.exit(apk.exec_())



#%% karra rangli
# print(Back.BLACK)
# print(Fore.LIGHTBLUE_EX)
# print(Style.NORMAL)

men=[[1,4,6,2],[1,2,3,4]]
lis=[1,6,4,2]
for i in men:
    if sorted(i)==sorted(lis):
        print("$")


#%%%


import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MyWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.hello = ["Abdurahmon", "Nodirbek", "Azizbek",
            "MuhammadSiddiq", "Asadullo"]

        self.button = QPushButton("Click me!")
        self.text = QLabel("Foundation 10")
        self.text.setAlignment(Qt.AlignCenter)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.magic)


    def magic(self):
        self.text.setText(random.choice(self.hello))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = MyWidget()
    widget.show()

    sys.exit(app.exec_())





