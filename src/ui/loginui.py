from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import sys

# custom modules
from src.ui.registerui import RegisterUI
from src.core.login import Login
from src.ui.popupui import MessageBox


class LoginUI(QtWidgets.QMainWindow):
    """handle login feature"""

    def __init__(self) -> None:
        # load the login ui
        super(LoginUI, self).__init__()
        loadUi("ui\login_page.ui", self)
        self.show()

        # load the fields
        self._loadTheWidgets()

        # making label_or_register clickable
        self._makeRegisterLabelClickable()

        # trigger login button
        self.pushButton_login.clicked.connect(self._loginButtonClicked)

    def _loadTheWidgets(self):
        """load all the input widgets in the login window"""
        # getting username and password
        self.lineEdit_username = self.findChild(
            QtWidgets.QLineEdit, "lineEdit_username"
        )
        self.lineEdit_password = self.findChild(
            QtWidgets.QLineEdit, "lineEdit_password"
        )

        # getting login button
        self.pushButton_login = self.findChild(
            QtWidgets.QPushButton, "pushButton_login"
        )

        # getting register lable
        self.label_or_register = self.findChild(QtWidgets.QLabel, "label_or_register")

    def _makeRegisterLabelClickable(self):
        """make the register button clickable"""
        self.label_or_register.mousePressEvent = self._registerLabelClicked

    def _registerLabelClicked(self, event):
        """Handle click event for the register label"""
        # hide the login window and show register
        # Register(self): creating an object of Register window and giving the instance
        # of the current login window so that when the work of register window is finished
        # it can make the login window visible again.
        r = RegisterUI(self)
        self.hide()

    def _loginButtonClicked(self):
        login_handler = Login(
            self.lineEdit_username, self.lineEdit_password
        )


class HandleLogin:
    def __init__(self) -> None:
        app = QtWidgets.QApplication(sys.argv)
        l = LoginUI()
        sys.exit(app.exec_())
