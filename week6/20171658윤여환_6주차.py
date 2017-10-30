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
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()
        
        
    def initUI(self):

        # 레이아웃 첫째 줄
        Name = QLabel('Name :', self)
        self.NameInput = QLineEdit()
        Age = QLabel('Age :', self)
        self.AgeInput = QLineEdit()
        Score = QLabel('Score :', self)
        self.ScoreInput = QLineEdit()

        hbox = QHBoxLayout()
        hbox.addWidget(Name)
        hbox.addWidget(self.NameInput)
        hbox.addWidget(Age)
        hbox.addWidget(self.AgeInput)
        hbox.addWidget(Score)
        hbox.addWidget(self.ScoreInput)

        # 레이아웃 둘째 줄
        Amount = QLabel('Amount :', self)
        self.AmountInput = QLineEdit()
        Key = QLabel('Key :')
        self.KeyList = QComboBox()
        self.KeyList.addItem("Name")
        self.KeyList.addItem("Score")
        self.KeyList.addItem("Age")

        hbox2 = QHBoxLayout()
        hbox2.addStretch()
        hbox2.addWidget(Amount)
        hbox2.addWidget(self.AmountInput)
        hbox2.addWidget(Key)
        hbox2.addWidget(self.KeyList)

        # 레이아웃 셋째 줄
        AddButton = QPushButton('Add', self)
        DelButton = QPushButton('Del', self)
        FindButton = QPushButton('Find', self)
        IncButton = QPushButton('Inc', self)
        ShowButton = QPushButton('Show', self)

        AddButton.clicked.connect(self.AddButtonClicked)
        DelButton.clicked.connect(self.DelButtonClicked)
        FindButton.clicked.connect(self.FindButtonClicked)
        IncButton.clicked.connect(self.IncButtonClicked)
        ShowButton.clicked.connect(self.ShowButtonClicked)

        hbox3 = QHBoxLayout()
        hbox3.addStretch()
        hbox3.addWidget(AddButton)
        hbox3.addWidget(DelButton)
        hbox3.addWidget(FindButton)
        hbox3.addWidget(IncButton)
        hbox3.addWidget(ShowButton)


        # 레이아웃 넷쨰 줄
        Result = QLabel('Result :')

        hbox4 = QHBoxLayout()
        # hbox4.addStretch()
        hbox4.addWidget(Result)

        # 레이아웃 다섯쨰 줄
        self.ResultBox = QTextEdit(self)

        hbox5 = QHBoxLayout()
        hbox5.addWidget(self.ResultBox)

        # 수평 정렬 레이아웃을 수직 정렬
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')    
        self.show()

    # Show
    def ShowButtonClicked(self):
        self.showScoreDB(self.KeyList.currentText())

    # Add
    def AddButtonClicked(self):
        record = {'Name': self.NameInput.text(), 'Age': int(self.AgeInput.text()), 'Score': int(self.ScoreInput.text())}
        self.scoredb += [record]
        self.showScoreDB()

    # Del
    def DelButtonClicked(self):
        reversed_scdb = sorted(self.scoredb, key = lambda x : ["Name"], reverse = True)
        for p in reversed_scdb:
            if p["Name"] == self.NameInput.text():
                self.scoredb.remove(p)
            self.showScoreDB()

    # Find
    def FindButtonClicked(self):
        temp = ""
        for p in sorted(self.scoredb, key = lambda person : person["Name"]):
            for attr in sorted(p):
                if p["Name"] == self.NameInput.text():
                    temp += attr + "=" + str(p[attr]) + " "
            temp += "\n"
        self.ResultBox.setText(temp)

    # Inc
    def IncButtonClicked(self):
        for p in sorted(self.scoredb, key = lambda person : person["Name"]):
            for attr in sorted(p):
                if p["Name"] == self.NameInput.text():
                    p["Score"] += int(self.AmountInput.text())
                    break
        self.showScoreDB()


    # def keyPressEvent(self, e):
    #     if e.key() == Qt.Key_Escape:
    #         self.close()



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
            for i in self.scoredb:
                i['Age'] = int(i['Age'])
                i['Score'] = int(i['Score'])
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self, keyname = "Score"):
        temp = ""
        for p in sorted(self.scoredb, key = lambda person : person[keyname]):
            for attr in sorted(p):
                temp += attr + "=" + str(p[attr]) + " "

            temp += "\n"
        self.ResultBox.setText(temp)

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())





