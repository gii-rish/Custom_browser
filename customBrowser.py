import sys, os
from PyQt5.QtWidgets  import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

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

		#Initializing home, back, front and reload buttons, and assigning buttons.
		home, back, front, reloadButton = QAction(QIcon(os.path.join('images','home-icon.png')),'Home', self), \
			QAction(QIcon(os.path.join('images','left-arrow.png')), 'Back', self), \
			QAction(QIcon(os.path.join('images','right-arrow.png')),'Forward', self), \
			QAction(QIcon(os.path.join('images','reload-icon.png')), 'Reload', self)

		home.triggered.connect(lambda: self.window.setUrl(QUrl("http://google.com")))
		navBar.addAction(home)

		back.triggered.connect(self.window.back)
		navBar.addAction(back)

		front.triggered.connect(self.window.forward)
		navBar.addAction(front)

		reloadButton.triggered.connect(self.window.reload)
		navBar.addAction(reloadButton)

		#textbox to enter the url
		self.urlBar = QLineEdit()
		self.urlBar.returnPressed.connect(lambda: self.window.setUrl(QUrl(self.urlBar.text())))
		navBar.addWidget(self.urlBar)

		self.window.urlChanged.connect(lambda qurl: self.urlBar.setText(qurl.toString()))

		#styling to make the text-box to have round corners.
		self.urlBar.setStyleSheet(
			"QLineEdit"
				"{"
					"border-radius: 10px;"
					"border: 2px solid #b9b9b9;"
  					"padding: 3px;"

				"}"
			)



app = QApplication(sys.argv)
browserWindow = Browser()
app.exec()