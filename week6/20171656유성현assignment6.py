import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QGridLayout, QApplication,
                             QLabel, QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()

    def initUI(self):

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')

        # labels
        self.label_Name = QLabel("Name: ")
        self.label_Age = QLabel("Age: ")
        self.label_Score = QLabel("Score: ")
        self.label_Amount = QLabel("Amount: ")
        self.label_Key = QLabel("Key: ")

        # comboBox
        self.combo_Key = QComboBox()
        self.combo_Key.addItem("Name")
        self.combo_Key.addItem("Age")
        self.combo_Key.addItem("Score")

        # lineEdit
        self.lineEdit_Name = QLineEdit()
        self.lineEdit_Age = QLineEdit()
        self.lineEdit_Score = QLineEdit()
        self.lineEdit_Amount = QLineEdit()

        # buttons
        self.button_Add = QPushButton("Add")
        self.button_Del = QPushButton("Del")
        self.button_Find = QPushButton("Find")
        self.button_Inc = QPushButton("Inc")
        self.button_Show = QPushButton("Show")

        # textEdit
        self.qte = QTextEdit()
        layout = QGridLayout()

        # layout
        layout.addWidget(self.label_Name, 0, 0)
        layout.addWidget(self.lineEdit_Name, 0, 1)
        layout.addWidget(self.label_Age, 0, 2)
        layout.addWidget(self.lineEdit_Age, 0, 3)
        layout.addWidget(self.label_Score, 0, 4)
        layout.addWidget(self.lineEdit_Score, 0, 5)

        layout.addWidget(self.label_Amount, 1, 2)
        layout.addWidget(self.lineEdit_Amount, 1, 3)
        layout.addWidget(self.label_Key, 1, 4)
        layout.addWidget(self.combo_Key, 1, 5)

        layout.addWidget(self.button_Add, 2, 1)
        layout.addWidget(self.button_Del, 2, 2)
        layout.addWidget(self.button_Find, 2, 3)
        layout.addWidget(self.button_Inc, 2, 4)
        layout.addWidget(self.button_Show, 2, 5)

        layout.addWidget(self.qte, 3, 0, 3, 6)

        self.str = ""  # show str

        self.setLayout(layout)
        self.show()

        # connect
        self.button_Show.clicked.connect(self.clickedShow)
        self.button_Add.clicked.connect(self.clickedAdd)
        self.button_Find.clicked.connect(self.clickedFind)
        self.button_Del.clicked.connect(self.clickedDel)
        self.button_Inc.clicked.connect(self.clickedInc)

    # method

    # show
    def clickedShow(self):
        self.str = ""  # 화면초기화
        self.showScoreDB()

    # add
    def clickedAdd(self):
        name = self.lineEdit_Name.text()
        age = int(self.lineEdit_Age.text())
        score = int(self.lineEdit_Score.text())
        record = {'Name': name, 'Age': age, 'Score': score}
        self.scoredb += [record]

    # find
    def clickedFind(self):
        for p in self.scoredb:
            if p['Name'] == self.lineEdit_Name.text():
                self.str = ""  # 화면 초기화
                for attr in p:
                    self.str += ("%s = %-20s" % (str(attr), str(p[attr])))
                    self.qte.setText(self.str)
                self.str += "\n"

    # del
    def clickedDel(self):
        for i in self.scoredb:
            for p in self.scoredb:
                if p['Name'] == self.lineEdit_Name.text():
                    self.scoredb.remove(p)

    # inc
    def clickedInc(self):
        for p in self.scoredb:
            if p['Name'] == self.lineEdit_Name.text():
                p['Score'] += int(self.lineEdit_Amount.text())

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            print("New DB: ", self.dbfilename)
            return

        self.scoredb = []
        try:
            self.scoredb = pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()

    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        for p in sorted(self.scoredb, reverse=True, key=lambda person: person[self.combo_Key.currentText()]):
            for attr in sorted(p):
                self.str += ("%s = %-20s" % (str(attr), str(p[attr])))
                self.qte.setText(self.str)
            self.str += "\n"


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
sys.exit(app.exec_())