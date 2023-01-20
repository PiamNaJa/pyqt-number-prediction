#นาย กัมปนาท จูพบุตร      63090500402
#นาย กิตติพศ อำนรรฆกิตติกุล 63090500403
#นาย ณชนน นวลเพชร      63090500409
#นาย พีระวัฒน์ มโนปภาพินท์  63090500440

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from collections import Counter                 # Counter เป็นออบเจ็กต์ที่ใช้งานสะดวกในเวลาที่เราต้องการจะนับจำนวนของอะไรบางอย่างว่ามีอะไรอยู่เท่าไร
import random
import sys

app = QApplication(sys.argv)
win = QMainWindow()
icon = QtGui.QIcon()
icon.addPixmap(QtGui.QPixmap("number.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)  # ใส่ icon ของ window
win.setWindowIcon(icon)
win.setWindowTitle("Number Prediction")  # ตั้งชื่อ window
win.setGeometry(0, 0, 1366, 768)
button_Submit = QPushButton('Submit', win)  # สร้างปุ่มที่มีชื่อว่า Submit
button_Submit.move(210, 630)
button_Submit.show()
button_GiveUp = QPushButton('Give Up!', win)  # สร้างปุ่มที่ชื่อ Give Up
button_GiveUp.move(340, 630)
button_GiveUp.show()
label_Heading = QLabel('--- How to play ---', win)  # หัวข้อ วิธีการเล่น
label_Heading.move(850, 20)
label_Heading.setFont(QFont('Frightmare', 20))
label_Heading.adjustSize()
label_How_to_play = QLabel(  # รายละเอียดวิธีการเล่น
    "1. เมื่อกดเริ่มเกมตัวเกมจะสุ่มเลขขึ้นมา 3 ตัวเลข จากนั้น\n"
    "    ให้ผู้ใช้เลือกตัวเลขจาก ComboBox ในแต่ละช่อง หลัง\n"
    "    จากนั้นให้กดยืนยัน\n"
    "2. เมื่อกดยืนยันแล้วระบบจะโชว์ว่าตัวเลขที่เลือกไปนั้น\n"
    "    ถูกต้องกี่ตัว และตำแหน่งถูกต้องกี่ตำแหน่ง\n"
    "3. ทำซ้ำไปเรื่อยๆจนกว่าจะชนะ หรือจะยอมแพ้ก็ได้  ¯\_( ͡° ͜ʖ ͡°)_/¯\n", win)
label_How_to_play.move(750, 70)
label_How_to_play.setFont(QFont('Angsana New', 16))
label_How_to_play.adjustSize()
label_guess1 = QLabel(win)  # label การเดาครั้งที่ 1
label_guess1.setText('Guess1 : ')
label_guess1.move(80, 80)
label_guess1.setFont(QFont('Angsana New', 18))
label_guess1.adjustSize()
label_guess2 = QLabel(win)  # label การเดาครั้งที่ 2
label_guess2.setText('Guess2 : ')
label_guess2.move(80, 130)
label_guess2.setFont(QFont('Angsana New', 18))
label_guess2.adjustSize()
label_guess3 = QLabel(win)  # label การเดาครั้งที่ 3
label_guess3.setText('Guess3 : ')
label_guess3.move(80, 180)
label_guess3.setFont(QFont('Angsana New', 18))
label_guess3.adjustSize()
label_guess4 = QLabel(win)  # label การเดาครั้งที่ 4
label_guess4.setText('Guess4 : ')
label_guess4.move(80, 230)
label_guess4.setFont(QFont('Angsana New', 18))
label_guess4.adjustSize()
label_guess5 = QLabel(win)  # label การเดาครั้งที่ 5
label_guess5.setText('Guess5 : ')
label_guess5.move(80, 280)
label_guess5.setFont(QFont('Angsana New', 18))
label_guess5.adjustSize()
label_guess6 = QLabel(win)  # label การเดาครั้งที่ 6
label_guess6.setText('Guess6 : ')
label_guess6.move(80, 330)
label_guess6.setFont(QFont('Angsana New', 18))
label_guess6.adjustSize()
label_guess7 = QLabel(win)  # label การเดาครั้งที่ 7
label_guess7.setText('Guess7 : ')
label_guess7.move(80, 380)
label_guess7.setFont(QFont('Angsana New', 18))
label_guess7.adjustSize()
label_guess8 = QLabel(win)  # label การเดาครั้งที่ 8
label_guess8.setText('Guess8 : ')
label_guess8.move(80, 430)
label_guess8.setFont(QFont('Angsana New', 18))
label_guess8.adjustSize()
label_guess9 = QLabel(win)  # label การเดาครั้งที่ 9
label_guess9.setText('Guess9 : ')
label_guess9.move(80, 480)
label_guess9.setFont(QFont('Angsana New', 18))
label_guess9.adjustSize()
label_guess10 = QLabel(win)  # label การเดาครั้งที่ 10
label_guess10.setText('Guess10 : ')
label_guess10.move(69, 530)
label_guess10.setFont(QFont('Angsana New', 18))
label_guess10.adjustSize()
label_correct_pos = QLabel(win)  # label คุณเดาตำแหน่งถูกต้อง
label_correct_pos.setText("คุณเดาตำแหน่งถูกต้อง")
label_correct_pos.move(750, 360)
label_correct_pos.setFont(QFont('Book_Akhanake', 12))
label_correct_pos.adjustSize()
label_correct_pos.show()
label_correct_num = QLabel(win)  # label คุณเดาตัวเลขถูกต้อง
label_correct_num.setText("คุณเดาตัวเลขถูกต้อง")
label_correct_num.move(1000, 360)
label_correct_num.setFont(QFont('Book_Akhanake', 12))
label_correct_num.adjustSize()
label_correct_num.show()
label_first = QLabel(win)  # label คำใบ้ครั้งที่ 1
label_first.setText("ครั้งที่ 1")
label_first.move(650, 405)
label_first.setFont(QFont('Book_Akhanake', 12))
label_first.adjustSize()
label_first.show()
label_second = QLabel(win)  # label คำใบ้ครั้งที่ 2
label_second.setText("ครั้งที่ 2")
label_second.move(650, 435)
label_second.setFont(QFont('Book_Akhanake', 12))
label_second.adjustSize()
label_second.show()
label_third = QLabel(win)  # label คำใบ้ครั้งที่ 3
label_third.setText("ครั้งที่ 3")
label_third.move(650, 465)
label_third.setFont(QFont('Book_Akhanake', 12))
label_third.adjustSize()
label_third.show()
label_fourth = QLabel(win)  # label คำใบ้ครั้งที่ 4
label_fourth.setText("ครั้งที่ 4")
label_fourth.move(650, 495)
label_fourth.setFont(QFont('Book_Akhanake', 12))
label_fourth.adjustSize()
label_fourth.show()
label_fifth = QLabel(win)  # label คำใบ้ครั้งที่ 5
label_fifth.setText("ครั้งที่ 5")
label_fifth.move(650, 525)
label_fifth.setFont(QFont('Book_Akhanake', 12))
label_fifth.adjustSize()
label_fifth.show()
label_sixth = QLabel(win)  # label คำใบ้ครั้งที่ 6
label_sixth.setText("ครั้งที่ 6")
label_sixth.move(650, 555)
label_sixth.setFont(QFont('Book_Akhanake', 12))
label_sixth.adjustSize()
label_sixth.show()
label_seventh = QLabel(win)  # label คำใบ้ครั้งที่ 7
label_seventh.setText("ครั้งที่ 7")
label_seventh.move(650, 585)
label_seventh.setFont(QFont('Book_Akhanake', 12))
label_seventh.adjustSize()
label_seventh.show()
label_eighth = QLabel(win)  # label คำใบ้ครั้งที่ 8
label_eighth.setText("ครั้งที่ 8")
label_eighth.move(650, 615)
label_eighth.setFont(QFont('Book_Akhanake', 12))
label_eighth.adjustSize()
label_eighth.show()
label_ninth = QLabel(win)
label_ninth.setText("ครั้งที่ 9")  # label คำใบ้ครั้งที่ 9
label_ninth.move(650, 645)
label_ninth.setFont(QFont('Book_Akhanake', 12))
label_ninth.adjustSize()
label_ninth.show()
label_tenth = QLabel(win)
label_tenth.setText("ครั้งที่ 10")  # label คำใบ้ครั้งที่ 10
label_tenth.move(650, 675)
label_tenth.setFont(QFont('Book_Akhanake', 12))
label_tenth.adjustSize()
label_tenth.show()
numlist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  # กำหนด list ตัวเลข 0 - 9
Combo_1 = QComboBox(win)  # สร้างComboBox อันแรก
Combo_1.move(200, 590)
Combo_1.adjustSize()
Combo_1.addItems(numlist)  # เพิ่ม list ของตัวเลขลง ComboBox อันแรก
Combo_2 = QComboBox(win)  # สร้างComboBox อันที่สอง
Combo_2.move(290, 590)
Combo_2.adjustSize()
Combo_2.addItems(numlist)  # เพิ่ม list ของตัวเลขลง ComboBox อันที่สอง
Combo_3 = QComboBox(win)  # สร้างComboBox อันที่สาม
Combo_3.move(380, 590)
Combo_3.adjustSize()
Combo_3.addItems(numlist)  # เพิ่ม list ของตัวเลขลง ComboBox อันที่สาม
a = random.randint(0, 9)  # โปรแกรมสุ่มตัวเลขตัวแรก
b = random.randint(0, 9)  # โปรแกรมสุ่มตัวเลขตัวที่สอง
c = random.randint(0, 9)  # โปรแกรมสุ่มตัวเลขตัวที่สาม
rdm_list = [a, b, c]  # รวมตัวเลขที่โปรแกรมสุ่มทั้งสามตัวเป็น list


def result_show1():  # ฟังก์ชันโชว์ผลลัพธ์เมื่อชนะ
    Result_1 = str(a)
    Result_2 = str(b)
    Result_3 = str(c)
    label_Result = QLabel(win)  # label แสดงผลลัพธ์ที่โปรแกรมสุ่มได้
    label_Result.setText(
             "Result :       " + '           ' + Result_1 + '                     ' + Result_2 + '                   ' + Result_3)
    label_Result.move(80, 670)
    label_Result.setFont(QFont('Angsana New', 18))
    label_Result.adjustSize()
    label_Result.show()
    Combo_1.setEnabled(False)  # ไม่ให้ ComBoBox_1 ใช้งานได้
    Combo_2.setEnabled(False)  # ไม่ให้ ComBoBox_2 ใช้งานได้
    Combo_3.setEnabled(False)  # ไม่ให้ ComBoBox_3 ใช้งานได้
    button_Submit.setEnabled(False) # ไม่ให้ปุ่ม Submit ใช้งานได้
    button_GiveUp.setEnabled(False) # ไม่ให้ปุ่ม Give up ใช้งานได้


def result_show():  # ฟังก์ชันโชว์ผลลัพธ์เมื่อแพ้
    Result_1 = str(a)
    Result_2 = str(b)
    Result_3 = str(c)
    label_Result = QLabel(win)  # label แสดงผลลัพธ์ที่โปรแกรมสุ่มได้
    label_Result.setText(
        "Result :       " + '           ' + Result_1 + '                     ' + Result_2 + '                    ' + Result_3)
    label_Result.move(80, 670)
    label_Result.setFont(QFont('Angsana New', 18))
    label_Result.adjustSize()
    label_Result.show()
    label_Symbol_lose = QLabel(win) # label แสดงข้อความว่าแพ้
    label_Symbol_lose.setText("You Lose  🏳")
    label_Symbol_lose.move(270, 20)
    label_Symbol_lose.setFont(QFont('Angsana New', 22))
    label_Symbol_lose.adjustSize()
    label_Symbol_lose.show()
    Combo_1.setEnabled(False)
    Combo_2.setEnabled(False)
    Combo_3.setEnabled(False)
    button_Submit.setEnabled(False)
    button_GiveUp.setEnabled(False)


def check(list1, list2): # ฟังก์ชันที่ทำการเชค list ตัวเลขที่ผู้เล่นใส่เข้าไป ว่าเป็น Sublist กับ list ตัวเลขที่โปรแกรมสุ่มได้หรือไม่
    x = len(list1)
    y = len(list2)
    z = 0
    for i in range(x - y + 1):
        if list1[i] == list2[z]:
            while True:
                if y - 1 == z:
                    return True
                i += 1
                z += 1
                if list1[i] != list2[z]:
                    return False
    return False


def Guess1():                                                                                                        # ฟังก์ชันการทายครั้งแรก
    Num_guess1 = Combo_1.currentText()
    Num_guess2 = Combo_2.currentText()
    Num_guess3 = Combo_3.currentText()
    user = [int(Num_guess1), int(Num_guess2), int(Num_guess3)]                        # list ของ ComboBox โดยกำหนดให้เป็นจำนวนเต็ม
    if check(rdm_list, user):                                                                                    # ถ้าเกิดเชคในฟังก์ชันที่เชคว่าเป็น Sublist หรือไม่ ถ้าเป็นจริงจะทำคำสั่งข้างล่างนี้
        label_True = QLabel(win)                                                                               # label กำหนดข้อความเป็น  ✓  เมื่อทายตัวเลขถูกต้องทั้งสามตัว
        label_True.setText("✓")
        label_True.setStyleSheet("color: green")
        label_True.move(500, 80)
        label_True.setFont(QFont('Angsana New', 22))
        label_True.adjustSize()
        label_True.show()
        label_Symbol_win1 = QLabel(win)                                                               # label กำหนดข้อความเป็น  You Win 🚩 เมื่อชนะ
        label_Symbol_win1.setText("ํYou Win 🚩")
        label_Symbol_win1.move(270, 10)                                                        
        label_Symbol_win1.setFont(QFont('Angsana New', 22))                                    
        label_Symbol_win1.adjustSize()                                                         
        label_Symbol_win1.show()                                                               
        Correct = []                                                                                                  # เก็บลิสเปล่าไว้ใน correct
        for i in range(len(rdm_list)):
            if rdm_list[i] == user[i]:                                                                            # เช็คเงื่อนไขว่าคำตอบตำแหน่งที่ i ตรงกับ user_input ตำแหน่งที่ i หรือไหม
                Correct.append(i)                                                                                 # ถ้าเลขไหนตรงก็เก็บค่า i ไว้ใน correct
        label_check_list = QLabel(win)                                                                     # label บอกว่ามีตำแหน่งถูกต้องกี่ตำแหน่ง
        label_check_list.setText(str(len(Correct)))                                                         # แสดงผลออกมาเป็นความยาวของ list correct
        label_check_list.move(840, 405)
        label_check_list.setFont(QFont('Book_Akhanake', 14))
        label_check_list.adjustSize()
        label_check_list.show()
        result_show1()                                                                                                      #แสดงตัวเลขทั้งสามที่ถูกต้อง
        button_GiveUp.setEnabled(False)                                                                         # ไม่ให้ปุ่ม Give up ใช้งานได้
        button_Submit.setEnabled(False)                                                                         # ไม่ให้ปุ่ม Submit ใช้งานได้
    else:                                                                                                                          # ถ้าเกิดไม่เป็นไปตามเงื่อนไขแรก จะทำคำสั่งด้านล่างนี้
        Correct = []
        for i in range(len(rdm_list)):
            if rdm_list[i] == user[i]:
                Correct.append(i)
        label_check_list = QLabel(win)
        label_check_list.setText(str(len(Correct)))
        label_check_list.move(840, 405)
        label_check_list.setFont(QFont('Book_Akhanake', 14))
        label_check_list.adjustSize()
        label_check_list.show()
    label_check_num = QLabel(win)                                                                                            # label บอกว่าเดาตัวเลขถูกต้องกี่ตัว
    label_check_num.setText(str(len((list((Counter(rdm_list) & Counter(user)).elements())))))        # เชค list ที่โปรแกรมสุ่มได้ กับ list ตัวเลขที่ผู้ใช้ป้อนเข้าไปว่าตรงกันกี่ตัว
    label_check_num.move(1075, 405)
    label_check_num.setFont(QFont('Book_Akhanake', 14))
    label_check_num.adjustSize()
    label_check_num.show()
    label_show_list = QLabel(win)                                                                                               # label แสดงตัวเลขที่ผู้ใช้ป้อนเข้าไปทั้ง 3 ตัว
    label_show_list.setText('' + Num_guess1 + '                      ' + Num_guess2 + '                      ' + Num_guess3)
    label_show_list.move(228, 80)
    label_show_list.setFont(QFont('Angsana New', 18))
    label_show_list.adjustSize()
    label_show_list.show()
    button_Submit.clicked.disconnect()
    button_Submit.clicked.connect(Guess2)                                                                                # ปุ่ม Submit จะเชื่อมต่อกับการทายครั้งที่ 2


def Guess2():
    Num_guess1 = Combo_1.currentText()
    Num_guess2 = Combo_2.currentText()
    Num_guess3 = Combo_3.currentText()
    user = [int(Num_guess1), int(Num_guess2), int(Num_guess3)]
    if check(rdm_list, user):
        label_True = QLabel(win)
        label_True.setText("✓")
        label_True.setStyleSheet("color: green")
        label_True.move(500, 130)
        label_True.setFont(QFont('Angsana New', 22))
        label_True.adjustSize()
        label_True.show()
        label_Symbol_win2 = QLabel(win)
        label_Symbol_win2.setText("ํYou Win 🚩")
        label_Symbol_win2.move(270, 10)
        label_Symbol_win2.setFont(QFont('Angsana New', 22))
        label_Symbol_win2.adjustSize()
        label_Symbol_win2.show()
        result_show1()
        Correct = []
        for i in range(len(rdm_list)):
            if rdm_list[i] == user[i]:
                Correct.append(i)
        label_check_list = QLabel(win)
        label_check_list.setText(str(len(Correct)))
        label_check_list.move(840, 435)
        label_check_list.setFont(QFont('Book_Akhanake', 14))
        label_check_list.adjustSize()
        label_check_list.show()
        result_show1()
        button_GiveUp.setEnabled(False)
        button_Submit.setEnabled(False)
    else:
        Correct = []
        for i in range(len(rdm_list)):
            if rdm_list[i] == user[i]:
                Correct.append(i)
        label_check_list = QLabel(win)
        label_check_list.setText(str(len(Correct)))
        label_check_list.move(840, 435)
        label_check_list.setFont(QFont('Book_Akhanake', 14))
        label_check_list.adjustSize()
        label_check_list.show()
    label_check_num = QLabel(win)
    label_check_num.setText(str(len((list((Counter(rdm_list) & Counter(user)).elements())))))
    label_check_num.move(1075, 435)
    label_check_num.setFont(QFont('Book_Akhanake', 14))
    label_check_num.adjustSize()
    label_check_num.show()
    label_show_list = QLabel(win)
    label_show_list.setText('' + Num_guess1 + '                      ' + Num_guess2 + '                      ' + Num_guess3)
    label_show_list.move(228, 130)
    label_show_list.setFont(QFont('Angsana New', 18))
    label_show_list.adjustSize()
    label_show_list.show()
    button_Submit.clicked.disconnect()
    button_Submit.clicked.connect(Guess3)


def Guess3():
    Num_guess1 = Combo_1.currentText()
    Num_guess2 = Combo_2.currentText()
    Num_guess3 = Combo_3.currentText()
    user = [int(Num_guess1), int(Num_guess2), int(Num_guess3)]
    if check(rdm_list, user):
        label_True = QLabel(win)
        label_True.setText("✓")
        label_True.setStyleSheet("color: green")
        label_True.move(500, 180)
        label_True.setFont(QFont('Angsana New', 22))
        label_True.adjustSize()
        label_True.show()
        label_Symbol_win3 = QLabel(win)
        label_Symbol_win3.setText("ํYou Win 🚩")
        label_Symbol_win3.move(270, 10)
        label_Symbol_win3.setFont(QFont('Angsana New', 22))
        label_Symbol_win3.adjustSize()
        label_Symbol_win3.show()
        result_show1()
        Correct = []
        for i in range(len(rdm_list)):
            if rdm_list[i] == user[i]:
                Correct.append(i)
        label_check_list = QLabel(win)
        label_check_list.setText(str(len(Correct)))
        label_check_list.move(840, 465)
        label_check_list.setFont(QFont('Book_Akhanake', 14))
        label_check_list.adjustSize()
        label_check_list.show()
        result_show1()
        button_GiveUp.setEnabled(False)
        button_Submit.setEnabled(False)
    else:
        Correct = []
        for i in range(len(rdm_list)):
            if rdm_list[i] == user[i]:
                Correct.append(i)
        label_check_list = QLabel(win)
        label_check_list.setText(str(len(Correct)))
        label_check_list.move(840, 465)
        label_check_list.setFont(QFont('Book_Akhanake', 14))
        label_check_list.adjustSize()
        label_check_list.show()
    label_check_num = QLabel(win)
    label_check_num.setText(str(len((list((Counter(rdm_list) & Counter(user)).elements())))))
    label_check_num.move(1075, 465)
    label_check_num.setFont(QFont('Book_Akhanake', 14))
    label_check_num.adjustSize()
    label_check_num.show()
    label_show_list = QLabel(win)
    label_show_list.setText('' + Num_guess1 + '                      ' + Num_guess2 + '                      ' + Num_guess3)
    label_show_list.move(228, 180)
    label_show_list.setFont(QFont('Angsana New', 18))
    label_show_list.adjustSize()
    label_show_list.show()
    button_Submit.clicked.disconnect()
    button_Submit.clicked.connect(Guess4)


def Guess4():
    Num_guess1 = Combo_1.currentText()
    Num_guess2 = Combo_2.currentText()
    Num_guess3 = Combo_3.currentText()
    user = [int(Num_guess1), int(Num_guess2), int(Num_guess3)]
    if check(rdm_list, user):
        label_True = QLabel(win)
        label_True.setText("✓")
        label_True.setStyleSheet("color: green")
        label_True.move(500, 230)
        label_True.setFont(QFont('Angsana New', 22))
        label_True.adjustSize()
        label_True.show()
        label_Symbol_win4 = QLabel(win)
        label_Symbol_win4.setText("ํYou Win 🚩")
        label_Symbol_win4.move(270, 10)
        label_Symbol_win4.setFont(QFont('Angsana New', 22))
        label_Symbol_win4.adjustSize()
        label_Symbol_win4.show()
        result_show1()
        Correct = []
        for i in range(len(rdm_list)):
            if rdm_list[i] == user[i]:
                Correct.append(i)
        label_check_list = QLabel(win)
        label_check_list.setText(str(len(Correct)))
        label_check_list.move(840, 495)
        label_check_list.setFont(QFont('Book_Akhanake', 14))
        label_check_list.adjustSize()
        label_check_list.show()
        result_show1()
        button_GiveUp.setEnabled(False)
        button_Submit.setEnabled(False)
    else:
        Correct = []
        for i in range(len(rdm_list)):
            if rdm_list[i] == user[i]:
                Correct.append(i)
        label_check_list = QLabel(win)
        label_check_list.setText(str(len(Correct)))
        label_check_list.move(840, 495)
        label_check_list.setFont(QFont('Book_Akhanake', 14))
        label_check_list.adjustSize()
        label_check_list.show()
    label_check_num = QLabel(win)
    label_check_num.setText(str(len((list((Counter(rdm_list) & Counter(user)).elements())))))
    label_check_num.move(1075, 495)
    label_check_num.setFont(QFont('Book_Akhanake', 14))
    label_check_num.adjustSize()
    label_check_num.show()
    label_show_list = QLabel(win)
    label_show_list.setText('' + Num_guess1 + '                      ' + Num_guess2 + '                      ' + Num_guess3)
    label_show_list.move(228, 230)
    label_show_list.setFont(QFont('Angsana New', 18))
    label_show_list.adjustSize()
    label_show_list.show()
    button_Submit.clicked.disconnect()
    button_Submit.clicked.connect(Guess5)


def Guess5():
    Num_guess1 = Combo_1.currentText()
    Num_guess2 = Combo_2.currentText()
    Num_guess3 = Combo_3.currentText()
    user = [int(Num_guess1), int(Num_guess2), int(Num_guess3)]
    if check(rdm_list, user):
        label_True = QLabel(win)
        label_True.setText("✓")
        label_True.setStyleSheet("color: green")
        label_True.move(500, 280)
        label_True.setFont(QFont('Angsana New', 22))
        label_True.adjustSize()
        label_True.show()
        label_Symbol_win5 = QLabel(win)
        label_Symbol_win5.setText("ํYou Win 🚩")
        label_Symbol_win5.move(270, 10)
        label_Symbol_win5.setFont(QFont('Angsana New', 22))
        label_Symbol_win5.adjustSize()
        label_Symbol_win5.show()
        result_show1()
        Correct = []
        for i in range(len(rdm_list)):
            if rdm_list[i] == user[i]:
                Correct.append(i)
        label_check_list = QLabel(win)
        label_check_list.setText(str(len(Correct)))
        label_check_list.move(840, 525)
        label_check_list.setFont(QFont('Book_Akhanake', 14))
        label_check_list.adjustSize()
        label_check_list.show()
        result_show1()
        button_GiveUp.setEnabled(False)
        button_Submit.setEnabled(False)
    else:
        Correct = []
        for i in range(len(rdm_list)):
            if rdm_list[i] == user[i]:
                Correct.append(i)
        label_check_list = QLabel(win)
        label_check_list.setText(str(len(Correct)))
        label_check_list.move(840, 525)
        label_check_list.setFont(QFont('Book_Akhanake', 14))
        label_check_list.adjustSize()
        label_check_list.show()
    label_check_num = QLabel(win)
    label_check_num.setText(str(len((list((Counter(rdm_list) & Counter(user)).elements())))))
    label_check_num.move(1075, 525)
    label_check_num.setFont(QFont('Book_Akhanake', 14))
    label_check_num.adjustSize()
    label_check_num.show()
    label_show_list = QLabel(win)
    label_show_list.setText('' + Num_guess1 + '                      ' + Num_guess2 + '                      ' + Num_guess3)
    label_show_list.move(228, 280)
    label_show_list.setFont(QFont('Angsana New', 18))
    label_show_list.adjustSize()
    label_show_list.show()
    button_Submit.clicked.disconnect()
    button_Submit.clicked.connect(Guess6)


def Guess6():
    Num_guess1 = Combo_1.currentText()
    Num_guess2 = Combo_2.currentText()
    Num_guess3 = Combo_3.currentText()
    user = [int(Num_guess1), int(Num_guess2), int(Num_guess3)]
    if check(rdm_list, user):
        label_True = QLabel(win)
        label_True.setText("✓")
        label_True.setStyleSheet("color: green")
        label_True.move(500, 330)
        label_True.setFont(QFont('Angsana New', 22))
        label_True.adjustSize()
        label_True.show()
        label_Symbol_win6 = QLabel(win)
        label_Symbol_win6.setText("ํYou Win 🚩")
        label_Symbol_win6.move(270, 10)
        label_Symbol_win6.setFont(QFont('Angsana New', 22))
        label_Symbol_win6.adjustSize()
        label_Symbol_win6.show()
        result_show1()
        Correct = []
        for i in range(len(rdm_list)):
            if rdm_list[i] == user[i]:
                Correct.append(i)
        label_check_list = QLabel(win)
        label_check_list.setText(str(len(Correct)))
        label_check_list.move(840, 555)
        label_check_list.setFont(QFont('Book_Akhanake', 14))
        label_check_list.adjustSize()
        label_check_list.show()
        result_show1()
        button_GiveUp.setEnabled(False)
        button_Submit.setEnabled(False)
    else:
        Correct = []
        for i in range(len(rdm_list)):
            if rdm_list[i] == user[i]:
                Correct.append(i)
        label_check_list = QLabel(win)
        label_check_list.setText(str(len(Correct)))
        label_check_list.move(840, 555)
        label_check_list.setFont(QFont('Book_Akhanake', 14))
        label_check_list.adjustSize()
        label_check_list.show()
    label_check_num = QLabel(win)
    label_check_num.setText(str(len((list((Counter(rdm_list) & Counter(user)).elements())))))
    label_check_num.move(1075, 555)
    label_check_num.setFont(QFont('Book_Akhanake', 14))
    label_check_num.adjustSize()
    label_check_num.show()
    label_show_list = QLabel(win)
    label_show_list.setText('' + Num_guess1 + '                      ' + Num_guess2 + '                      ' + Num_guess3)
    label_show_list.move(228, 330)
    label_show_list.setFont(QFont('Angsana New', 18))
    label_show_list.adjustSize()
    label_show_list.show()
    button_Submit.clicked.disconnect()
    button_Submit.clicked.connect(Guess7)


def Guess7():
    Num_guess1 = Combo_1.currentText()
    Num_guess2 = Combo_2.currentText()
    Num_guess3 = Combo_3.currentText()
    user = [int(Num_guess1), int(Num_guess2), int(Num_guess3)]
    if check(rdm_list, user):
        label_True = QLabel(win)
        label_True.setText("✓")
        label_True.setStyleSheet("color: green")
        label_True.move(500, 380)
        label_True.setFont(QFont('Angsana New', 22))
        label_True.adjustSize()
        label_True.show()
        label_Symbol_win7 = QLabel(win)
        label_Symbol_win7.setText("ํYou Win 🚩")
        label_Symbol_win7.move(270, 10)
        label_Symbol_win7.setFont(QFont('Angsana New', 22))
        label_Symbol_win7.adjustSize()
        label_Symbol_win7.show()
        result_show1()
        Correct = []
        for i in range(len(rdm_list)):
            if rdm_list[i] == user[i]:
                Correct.append(i)
        label_check_list = QLabel(win)
        label_check_list.setText(str(len(Correct)))
        label_check_list.move(840, 585)
        label_check_list.setFont(QFont('Book_Akhanake', 14))
        label_check_list.adjustSize()
        label_check_list.show()
        result_show1()
        button_GiveUp.setEnabled(False)
        button_Submit.setEnabled(False)
    else:
        Correct = []
        for i in range(len(rdm_list)):
            if rdm_list[i] == user[i]:
                Correct.append(i)
        label_check_list = QLabel(win)
        label_check_list.setText(str(len(Correct)))
        label_check_list.move(840, 585)
        label_check_list.setFont(QFont('Book_Akhanake', 14))
        label_check_list.adjustSize()
        label_check_list.show()
    label_check_num = QLabel(win)
    label_check_num.setText(str(len((list((Counter(rdm_list) & Counter(user)).elements())))))
    label_check_num.move(1075, 585)
    label_check_num.setFont(QFont('Book_Akhanake', 14))
    label_check_num.adjustSize()
    label_check_num.show()
    label_show_list = QLabel(win)
    label_show_list.setText('' + Num_guess1 + '                      ' + Num_guess2 + '                      ' + Num_guess3)
    label_show_list.move(228, 380)
    label_show_list.setFont(QFont('Angsana New', 18))
    label_show_list.adjustSize()
    label_show_list.show()
    button_Submit.clicked.disconnect()
    button_Submit.clicked.connect(Guess8)


def Guess8():
    Num_guess1 = Combo_1.currentText()
    Num_guess2 = Combo_2.currentText()
    Num_guess3 = Combo_3.currentText()
    user = [int(Num_guess1), int(Num_guess2), int(Num_guess3)]
    if check(rdm_list, user):
        label_True = QLabel(win)
        label_True.setText("✓")
        label_True.setStyleSheet("color: green")
        label_True.move(500, 430)
        label_True.setFont(QFont('Angsana New', 22))
        label_True.adjustSize()
        label_True.show()
        label_Symbol_win8 = QLabel(win)
        label_Symbol_win8.setText("ํYou Win 🚩")
        label_Symbol_win8.move(270, 10)
        label_Symbol_win8.setFont(QFont('Angsana New', 22))
        label_Symbol_win8.adjustSize()
        label_Symbol_win8.show()
        result_show1()
        Correct = []
        for i in range(len(rdm_list)):
            if rdm_list[i] == user[i]:
                Correct.append(i)
        label_check_list = QLabel(win)
        label_check_list.setText(str(len(Correct)))
        label_check_list.move(840, 615)
        label_check_list.setFont(QFont('Book_Akhanake', 14))
        label_check_list.adjustSize()
        label_check_list.show()
        result_show1()
        button_GiveUp.setEnabled(False)
        button_Submit.setEnabled(False)
    else:
        Correct = []
        for i in range(len(rdm_list)):
            if rdm_list[i] == user[i]:
                Correct.append(i)
        label_check_list = QLabel(win)
        label_check_list.setText(str(len(Correct)))
        label_check_list.move(840, 615)
        label_check_list.setFont(QFont('Book_Akhanake', 14))
        label_check_list.adjustSize()
        label_check_list.show()
    label_check_num = QLabel(win)
    label_check_num.setText(str(len((list((Counter(rdm_list) & Counter(user)).elements())))))
    label_check_num.move(1075, 615)
    label_check_num.setFont(QFont('Book_Akhanake', 14))
    label_check_num.adjustSize()
    label_check_num.show()
    label_show_list = QLabel(win)
    label_show_list.setText('' + Num_guess1 + '                      ' + Num_guess2 + '                      ' + Num_guess3)
    label_show_list.move(228, 430)
    label_show_list.setFont(QFont('Angsana New', 18))
    label_show_list.adjustSize()
    label_show_list.show()
    button_Submit.clicked.disconnect()
    button_Submit.clicked.connect(Guess9)


def Guess9():
    Num_guess1 = Combo_1.currentText()
    Num_guess2 = Combo_2.currentText()
    Num_guess3 = Combo_3.currentText()
    user = [int(Num_guess1), int(Num_guess2), int(Num_guess3)]
    if check(rdm_list, user):
        label_True = QLabel(win)
        label_True.setText("✓")
        label_True.setStyleSheet("color: green")
        label_True.move(500, 480)
        label_True.setFont(QFont('Angsana New', 22))
        label_True.adjustSize()
        label_True.show()
        label_Symbol_win9 = QLabel(win)
        label_Symbol_win9.setText("ํYou Win 🚩")
        label_Symbol_win9.move(270, 10)
        label_Symbol_win9.setFont(QFont('Angsana New', 22))
        label_Symbol_win9.adjustSize()
        label_Symbol_win9.show()
        result_show1()
        Correct = []
        for i in range(len(rdm_list)):
            if rdm_list[i] == user[i]:
                Correct.append(i)
        label_check_list = QLabel(win)
        label_check_list.setText(str(len(Correct)))
        label_check_list.move(840, 645)
        label_check_list.setFont(QFont('Book_Akhanake', 14))
        label_check_list.adjustSize()
        label_check_list.show()
        result_show1()
        button_GiveUp.setEnabled(False)
        button_Submit.setEnabled(False)
    else:
        Correct = []
        for i in range(len(rdm_list)):
            if rdm_list[i] == user[i]:
                Correct.append(i)
        label_check_list = QLabel(win)
        label_check_list.setText(str(len(Correct)))
        label_check_list.move(840, 645)
        label_check_list.setFont(QFont('Book_Akhanake', 14))
        label_check_list.adjustSize()
        label_check_list.show()
    label_check_num = QLabel(win)
    label_check_num.setText(str(len((list((Counter(rdm_list) & Counter(user)).elements())))))
    label_check_num.move(1075, 645)
    label_check_num.setFont(QFont('Book_Akhanake', 14))
    label_check_num.adjustSize()
    label_check_num.show()
    label_show_list = QLabel(win)
    label_show_list.setText('' + Num_guess1 + '                      ' + Num_guess2 + '                      ' + Num_guess3)
    label_show_list.move(228, 480)
    label_show_list.setFont(QFont('Angsana New', 18))
    label_show_list.adjustSize()
    label_show_list.show()
    button_Submit.clicked.disconnect()
    button_Submit.clicked.connect(Guess10)


def Guess10():
    Num_guess1 = Combo_1.currentText()
    Num_guess2 = Combo_2.currentText()
    Num_guess3 = Combo_3.currentText()
    user = [int(Num_guess1), int(Num_guess2), int(Num_guess3)]
    if check(rdm_list, user):
        label_True = QLabel(win)
        label_True.setText("✓")
        label_True.setStyleSheet("color: green")
        label_True.move(500, 530)
        label_True.setFont(QFont('Angsana New', 22))
        label_True.adjustSize()
        label_True.show()
        label_Symbol_win10 = QLabel(win)
        label_Symbol_win10.setText("ํYou Win 🚩")
        label_Symbol_win10.move(270, 10)
        label_Symbol_win10.setFont(QFont('Angsana New', 22))
        label_Symbol_win10.adjustSize()
        label_Symbol_win10.show()
        result_show1()
        Correct = []
        for i in range(len(rdm_list)):
            if rdm_list[i] == user[i]:
                Correct.append(i)
        label_check_list = QLabel(win)
        label_check_list.setText(str(len(Correct)))
        label_check_list.move(840, 675)
        label_check_list.setFont(QFont('Book_Akhanake', 14))
        label_check_list.adjustSize()
        label_check_list.show()
        button_Submit.setEnabled(False)
        button_GiveUp.setEnabled(False)

    else:
        Correct = []
        for i in range(len(rdm_list)):
            if rdm_list[i] == user[i]:
                Correct.append(i)
        label_check_list = QLabel(win)
        label_check_list.setText(str(len(Correct)))
        label_check_list.move(840, 675)
        label_check_list.setFont(QFont('Book_Akhanake', 14))
        label_check_list.adjustSize()
        label_check_list.show()
        label_Symbol_lose = QLabel(win)
        label_Symbol_lose.setText("You Lose  🏳")
        label_Symbol_lose.move(270, 20)
        label_Symbol_lose.setFont(QFont('Angsana New', 22))
        label_Symbol_lose.adjustSize()
        label_Symbol_lose.show()
        button_Submit.setEnabled(False)
        button_GiveUp.setEnabled(False)
        result_show()
    label_check_num = QLabel(win)
    label_check_num.setText(str(len((list((Counter(rdm_list) & Counter(user)).elements())))))
    label_check_num.move(1075, 675)
    label_check_num.setFont(QFont('Book_Akhanake', 14))
    label_check_num.adjustSize()
    label_check_num.show()
    label_show_list = QLabel(win)
    label_show_list.setText('' + Num_guess1 + '                      ' + Num_guess2 + '                      ' + Num_guess3)
    label_show_list.move(228, 530)
    label_show_list.setFont(QFont('Angsana New', 18))
    label_show_list.adjustSize()
    label_show_list.show()


button_GiveUp.clicked.connect(result_show) # ปุ่ม Give up เมื่อกดแล้วจะไปเชื่อมกับฟังก์ชันโชว์ผลลัพธ์
button_Submit.clicked.connect(Guess1) # ปุ่ม Submit เมื่อกดครั้งแรกจะไปเชื่อมกับฟังก์ชันการทายครั้งแรก
win.show()
sys.exit(app.exec_())
