from PyQt6 import QtWidgets
from siau.siau_controller import SiauController
from siau.siau_model import SiauModel
from siau.siua_view import SiauView
from services.service_generic import Service


class Siau:
    def __init__(self):
        self.window = QtWidgets.QMainWindow()
        self.view = SiauView()
        self.view.setupUi(self.window)
        self.view.connect_signals()
        self.model = SiauModel(Service())
        self.controller = SiauController(self.view, self.model)
