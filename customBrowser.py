from PyQt5.QtWidgets  import *
import sys
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *


class Browser(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Customizable Browser")
		self.window = QWebEngineView()
		self.window.setUrl(QUrl("http://google.com"))
		self.setCentralWidget(self.window)
		self.showMaximized()



app = QApplication(sys.argv)
browserWindow = Browser()
app.exec()