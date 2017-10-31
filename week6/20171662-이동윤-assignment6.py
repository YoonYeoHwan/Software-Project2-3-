import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, 
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    
    def __init__(self):
        super().__init__()

        self.initUI()
        self.keyt = self.keys.currentText()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()
        
        
    def initUI(self):
        self.name = QLabel("Name :")
        self.namet = QLineEdit(self)
        self.age = QLabel("Age :")
        self.aget = QLineEdit(self)
        self.score = QLabel("Score :")
        self.scoret = QLineEdit(self)

        self.amount = QLabel("Amount :")
        self.amountt = QLineEdit(self)
        self.amountt.setFixedSize(100, 25)
        self.key = QLabel("Key :")
        self.keys = QComboBox()
        self.keys.addItems(['Name', 'Age', 'Score'])

        self.addb = QPushButton("Add")
        self.delb = QPushButton("Del")
        self.findb = QPushButton("Find")
        self.incb = QPushButton("Inc")
        self.showb = QPushButton("Show")

        self.result = QLabel("Result :")
        self.resultl = QTextEdit(self)

        hbox = QHBoxLayout()
        h2box = QHBoxLayout()
        h3box = QHBoxLayout()
        h4box = QHBoxLayout()
        h5box = QHBoxLayout()

        hbox.addWidget(self.name)
        hbox.addWidget(self.namet)
        hbox.addWidget(self.age)
        hbox.addWidget(self.aget)
        hbox.addWidget(self.score)
        hbox.addWidget(self.scoret)

        h2box.addStretch(1)
        h2box.addWidget(self.amount)
        h2box.addWidget(self.amountt)
        h2box.addWidget(self.key)
        h2box.addWidget(self.keys)

        h3box.addWidget(self.addb)
        self.addb.clicked.connect(self.addScoreDB)
        h3box.addWidget(self.delb)
        self.delb.clicked.connect(self.delScoreDB)
        h3box.addWidget(self.findb)
        self.findb.clicked.connect(self.findScoreDB)
        h3box.addWidget(self.incb)
        self.incb.clicked.connect(self.incScoreDB)
        h3box.addWidget(self.showb)
        self.showb.clicked.connect(self.showScoreDB)

        h4box.addWidget(self.result)

        h5box.addWidget(self.resultl)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(h2box)
        vbox.addLayout(h3box)
        vbox.addLayout(h4box)
        vbox.addLayout(h5box)

        self.setLayout(vbox)
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()


    def closeEvent(self, event):

        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
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
        self.keyt = self.keys.currentText()
        text = ''
        for p in sorted(self.scoredb, key=lambda person: person[self.keyt]):
            for attr in sorted(p):
                text += attr + "=" + str(p[attr]) + ' '
            text += '\n'
        self.resultl.setText(text)
        pass

    def addScoreDB(self):
        name = self.namet.text()
        age = self.aget.text()
        score = self.scoret.text()

        try:
            record = {'Name': name, 'Age': int(age), 'Score': int(score)}
            self.scoredb += [record]
            self.resultl.setText("추가가 완료되었습니다!")
        except:
            self.resultl.setText("잘못된 명령입니다.")
        pass

    def delScoreDB(self):
        name = self.namet.text()

        try:
            cnt = 0
            for p in self.scoredb:
                if p['Name'] == name:
                    cnt += 1
            while (cnt):
                for p in self.scoredb:
                    if p['Name'] == name:
                        self.scoredb.remove(p)
                        cnt -= 1
                        break
            self.resultl.setText("제거가 완료되었습니다!")
        except:
            self.resultl.setText("잘못된 명령입니다.")

    def findScoreDB(self):
        name = self.namet.text()
        text = ''

        try:
            for p in self.scoredb:
                if p['Name'] == name:
                    for attr in sorted(p):
                        text += attr + "=" + str(p[attr]) + ' '
                    text += '\n'
            self.resultl.setText(text)
        except:
            self.resultl.setText("잘못된 명령입니다.")

    def incScoreDB(self):
        name = self.namet.text()
        amount = self.amountt.text()

        try:
            for p in self.scoredb:
                if p['Name'] == name:
                    p['Score'] = p['Score'] + int(amount)
            self.resultl.setText("추가가 완료되었습니다!")
        except:
            self.resultl.setText("잘못된 명령입니다.")




if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())





