```
	vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(h2box)
        vbox.addLayout(h3box)
        vbox.addLayout(h4box)
        vbox.addLayout(h5box)
```

HBoxLayout으로 여러줄의 hbox들을 만들어주고
최종적으로 VBoxLayout으로 hbox를 감싸 gui를 만들어주었다.


```
	self.keyt = self.keys.currentText()
	self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()
```

combobox의 현재 값을 가져와주는 currentText를 사용해 초기 설정에서
showScoreDB를 불러와줬으며, 이를 scoredb 속에 담아주었다.


```
	self.amount = QLabel("Amount :")
	self.amountt = QLineEdit(self)
 	self.amountt.setFixedSize(100, 25)

	h2box.addStretch(1)
```

amount를 PDF속 예제처럼 나타내기 위해 setFixedSize를 통해 크기를 할당해주고 addStretch를 통해 거리를 조절해주었다.


```
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
```

clicked.connect를 통해 각각에 대응하는 함수를 호출해주었고


```
	name = self.namet.text()
        age = self.aget.text()
        score = self.scoret.text()
```

text()를 통해 LineEdit의 값을 받아왔다.

최종적으로 


```
    def closeEvent(self, event):

        self.writeScoreDB()
```

파일이 닫히며 데이터 파일의 변화값이 저장되는 방식이다.
