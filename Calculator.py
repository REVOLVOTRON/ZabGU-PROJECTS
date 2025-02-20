import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit


class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setFixedSize(200, 250)

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.layout.addWidget(self.display)

        grid_layout = QGridLayout()

        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
            ('C', 4, 0, 1, 2), ('%', 4, 3)
        ]

        for button_text, row, col, *colspan in buttons:
            button = QPushButton(button_text)
            button.clicked.connect(self.on_button_click)
            if colspan:
                grid_layout.addWidget(button, row, col, 1, colspan[0])
            else:
                grid_layout.addWidget(button, row, col)

        self.layout.addLayout(grid_layout)
        self.setLayout(self.layout)

    def on_button_click(self):
        sender = self.sender()
        text = sender.text()

        if text == 'C':
            self.display.setText('')
        elif text == '=':
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except Exception as e:
                self.display.setText('Error')
        elif text == '%':
            try:
                value = float(self.display.text())
                self.display.setText(str(value / 100))
            except ValueError:
                self.display.setText('Error')
        else:
            self.display.setText(self.display.text() + text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())
