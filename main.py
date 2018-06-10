import sys

from selenium import webdriver
from qtpy import uic, QtWidgets, QtCore, QtGui
from selenium.webdriver.common.keys import Keys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('demo.ui', self)
        self.architekLink.clicked.connect(self.goarchitek)
        self.openBrowser.clicked.connect(self.launcher)
        self.show()

    def launcher(self):
        ch = webdriver.Chrome()
        nav = self.navBar.text()
        assert isinstance(nav, object)
        ch.get(url=nav)

    def goarchitek(self):
        ch = webdriver.Chrome()
        ch.get('https://architek.co')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
