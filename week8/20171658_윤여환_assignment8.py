from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout, QMessageBox
from keypad import *

class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        # Digit Buttons
        numLayout = QGridLayout()
        opLayout = QGridLayout()
        conLayout = QGridLayout()
        funLayout = QGridLayout()

        buttonGroups = {
            'num' : {'buttons' : numPadList, 'layout' : numLayout, 'columns' : 3},
            'op' : {'buttons' : operatorList, 'layout' : opLayout, 'columns' : 2},
            'con' : {'buttons' : constantList, 'layout' : conLayout, 'columns' : 1},
            'fun' : {'buttons' : functionList, 'layout' : funLayout, 'columns' : 1},
        }

        for label in buttonGroups.keys():
            r = 0; c = 0
            buttonPad = buttonGroups[label]

            for btnText in buttonPad['buttons']:
                button = Button(btnText, self.buttonClicked)
                buttonPad['layout'].addWidget(button, r, c)
                c += 1

                if c >= buttonPad['columns']:
                    c = 0; r += 1

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)
        mainLayout.addLayout(numLayout, 1, 0)
        mainLayout.addLayout(opLayout, 1, 1)
        mainLayout.addLayout(conLayout, 2, 0)
        mainLayout.addLayout(funLayout, 2, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")


    def buttonClicked(self):

        button = self.sender()
        key = button.text()


        if self.display.text() == 'Error!':
            self.display.setText('')

        consList = {'pi' : '3.141592', '빛의 이동 속도 (m/s)' : '3E+8', '소리의 이동 속도 (m/s)' : '340', '태양과의 평균 거리 (km)' : '1.5E+8'}

        if key == '=':
            try:
                result = str(eval(self.display.text()))

            except:
                ErrorMessage = QMessageBox.information(self, 'Error',
                                                       'Input is not correct.')
                result = ''

            self.display.setText(result)

        elif key == 'C':
            self.display.setText('')

        elif key in consList.keys():
            self.display.setText(self.display.text() + consList[key])


        elif key == functionList[0]:
            n = self.display.text()
            value = calcFunctions.factorial(n)
            self.display.setText(str(value))
        elif key == functionList[1]:
            n = self.display.text()
            value = calcFunctions.decToBin(n)
            self.display.setText(str(value))
        elif key == functionList[2]:
            n = self.display.text()
            value = calcFunctions.binToDec(n)
            self.display.setText(str(value))
        elif key == functionList[3]:
            n = self.display.text()
            value = calcFunctions.decToRoman(n)
            self.display.setText(str(value))

        else:
            self.display.setText(self.display.text() + key)





if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
