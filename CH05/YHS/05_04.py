## shift+alt+e로 특정 라인만 실행 가능

# 5-4. 상승장 알리미 (스레드 버전)
# 5-4-1. 스레드 기본 코드
## 파이썬 인터프리터가 현재가를 조회하고 화면에 GUI를 그리는 두 가지 일을 순차적으로 실행하여, GUI가 버벅대는 현상 발생
from PyQt5.QtCore import *

class Worker(QThread):
    def run(self):
        while True:
            print("안녕하세요")
            self.sleep(1)

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Worker(QThread):
    def run(self):
        while True:
            print("안녕하세요")
            self.sleep(1)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.worker = Worker()
        self.worker.start()

app = QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()


# 5-4-2. 스레드 적용하기
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import pybithumb
import time

tickers = ["BTC", "ETH", "BCH", "ETC"]
form_class = uic.loadUiType("./CH05/YHS/bull.ui")[0]

class Worker(QThread):
    def run(self):
        while True:
            data = {}

            for ticker in tickers:
                data[ticker] = self.get_market_infos(ticker)

            print(data)
            time.sleep(5)

    def get_market_infos(self, ticker):
        try:
            df = pybithumb.get_ohlcv(ticker)
            ma5 = df['close'].rolling(window=5).mean()
            last_ma5 = ma5[-2]
            price = pybithumb.get_current_price(ticker)

            state = None
            if price > last_ma5:
                state = "상승장"
            else:
                state = "하락장"

            return price, last_ma5, state
        except:
            return None, None, None

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.worker = Worker()
        self.worker.start()

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()

## GUI에도 잘 출력되도록 코드 작성
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import pybithumb
import time

tickers = ["BTC", "ETH", "BCH", "ETC"]
form_class = uic.loadUiType("./CH05/YHS/bull.ui")[0]

class Worker(QThread):
    finished = pyqtSignal(dict)

    def run(self):
        while True:
            data = {}

            for ticker in tickers:
                data[ticker] = self.get_market_infos(ticker)

            self.finished.emit(data)
            time.sleep(2)

    def get_market_infos(self, ticker):
        try:
            df = pybithumb.get_ohlcv(ticker)
            ma5 = df['close'].rolling(window=5).mean()
            last_ma5 = ma5[-2]
            price = pybithumb.get_current_price(ticker)

            state = None
            if price > last_ma5:
                state = "상승장"
            else:
                state = "하락장"

            return price, last_ma5, state
        except:
            return None, None, None

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.worker = Worker()
        self.worker.finished.connect(self.update_table_widget)
        self.worker.start()

    @pyqtSlot(dict)
    def update_table_widget(self, data):
        try:
            for ticker, infos in data.items():
                index = tickers.index(ticker)

                self.tableWidget.setItem(index, 0, QTableWidgetItem(ticker))
                self.tableWidget.setItem(index, 1, QTableWidgetItem(str(infos[0])))
                self.tableWidget.setItem(index, 2, QTableWidgetItem(str(infos[1])))
                self.tableWidget.setItem(index, 3, QTableWidgetItem(str(infos[2])))
        except:
            pass

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
