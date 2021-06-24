# Currency_Converter_

## *Documentation work in progress*
## PyQT5, made by QT Designer for Currency Converter
This application has been created by Nikita Klyuyev (`w61783`)

## Disclaimer
This project was created as part of *Software Engineering* course.

# Purpose of the app
* A fast and reliable solution
* Compact python code
* Open source and accessibility for everyone

# How to use?
1. Download the project from repository
2. Run main.py
3. Use the forms to convert cuurency

# How this program works?
This program made with python module  ```currency converter``` and the default source is the European Central Bank. This is the ECB historical rates for 42 currencies against the Euro since 1999. The converter can use different sources as long as the format is the same.

The code:
```

import sys
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow
from currency_converter import CurrencyConverter


class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
    
    def init_UI(self):
        self.setWindowTitle('Currency Converter') 
        self.setWindowIcon(QIcon('currency-exchange.png'))
        self.ui.input_currency.setPlaceholderText('From:')
        self.ui.input_amount.setPlaceholderText('Amount:')
        self.ui.output_currency.setPlaceholderText('To:')
        self.ui.output_amount.setPlaceholderText('Result:')        
        self.ui.pushButton.clicked.connect(self.converter)

    def converter(self):
        c = CurrencyConverter()
        input_currency = self.ui.input_currency.text()
        output_currency = self.ui.output_currency.text()
        input_amount = int(self.ui.input_amount.text())     
        output_amount = round(c.convert(input_amount, '%s' % (input_currency), '%s' % (output_currency)), 2)
        self.ui.output_amount.setText(str(output_amount))

app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()
 
sys.exit(app.exec())
