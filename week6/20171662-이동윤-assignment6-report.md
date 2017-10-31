```
	vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(h2box)
        vbox.addLayout(h3box)
        vbox.addLayout(h4box)
        vbox.addLayout(h5box)
```

HBoxLayout���� �������� hbox���� ������ְ�
���������� VBoxLayout���� hbox�� ���� gui�� ������־���.


```
	self.keyt = self.keys.currentText()
	self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()
```

combobox�� ���� ���� �������ִ� currentText�� ����� �ʱ� ��������
showScoreDB�� �ҷ���������, �̸� scoredb �ӿ� ����־���.


```
	self.amount = QLabel("Amount :")
	self.amountt = QLineEdit(self)
 	self.amountt.setFixedSize(100, 25)

	h2box.addStretch(1)
```

amount�� PDF�� ����ó�� ��Ÿ���� ���� setFixedSize�� ���� ũ�⸦ �Ҵ����ְ� addStretch�� ���� �Ÿ��� �������־���.


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

clicked.connect�� ���� ������ �����ϴ� �Լ��� ȣ�����־���


```
	name = self.namet.text()
        age = self.aget.text()
        score = self.scoret.text()
```

text()�� ���� LineEdit�� ���� �޾ƿԴ�.

���������� 


```
    def closeEvent(self, event):

        self.writeScoreDB()
```

������ ������ ������ ������ ��ȭ���� ����Ǵ� ����̴�.
