"""_summary_

Equipo:
Christopher Noe Meza Garcia
Claudio Gael Rodriguez Vega
JEZREEL SIGALA HERNANDEZ

Version de Python : 3.10
PYQT6

"""

import sys
from PyQt6 import QtWidgets

from siau.siau import Siau


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Siau()
    ui.window.show()
    app.exec()
