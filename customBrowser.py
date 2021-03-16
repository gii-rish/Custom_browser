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

		#navbar
		navBar = QToolBar()
		self.addToolBar(navBar)

		home, back, front, reloadButton = QAction('Home', self), QAction('Back', self), QAction('Forward', self), QAction('Reload', self)
		home.triggered.connect(lambda: self.window.setUrl(QUrl("http://google.com")))
		navBar.addAction(home)

		back.triggered.connect(self.window.back)
		navBar.addAction(back)

		front.triggered.connect(self.window.forward)
		navBar.addAction(front)

		reloadButton.triggered.connect(self.window.reload)
		navBar.addAction(reloadButton)

		# def toHome(self):
		# 	self.window.setUrl(QUrl("http://google.com"))



app = QApplication(sys.argv)
app.setApplicationDisplayName("GfG PyQt5")
browserWindow = Browser()
app.exec()