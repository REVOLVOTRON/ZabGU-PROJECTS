import sys
from PyQt6.QtWidgets import QApplication
from gui import CalculatorGUI
from calc_logic import CalculatorLogic

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Создаем GUI
    gui = CalculatorGUI(None)  # Пока передаем None, так как контроллер еще не создан

    # Создаем логику и связываем ее с GUI
    logic = CalculatorLogic(gui)
    gui.controller = logic  # Привязываем контроллер к GUI

    gui.show()
    sys.exit(app.exec())