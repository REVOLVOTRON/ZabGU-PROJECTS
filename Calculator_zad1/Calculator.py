import sys
from PyQt6.QtWidgets import QApplication
from gui import CalculatorGUI
from calc_logic import CalculatorLogic

if __name__ == '__main__':
    app = QApplication(sys.argv)

    gui = CalculatorGUI(None)
    logic = CalculatorLogic(gui)
    gui.controller = logic

    gui.show()
    sys.exit(app.exec())
