from PyQt6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt6.QtCore import Qt


class CalculatorGUI(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Calculator")
        self.setFixedSize(200, 200)
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        # Поле ввода (теперь редактируемое)
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.returnPressed.connect(self.on_return_pressed)
        self.display.textChanged.connect(self.validate_input)
        self.layout.addWidget(self.display)

        # Сетка для кнопок
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
            button.clicked.connect(lambda _, text=button_text: self.controller.on_button_click(text))
            if colspan:
                grid_layout.addWidget(button, row, col, 1, colspan[0])
            else:
                grid_layout.addWidget(button, row, col)

        self.layout.addLayout(grid_layout)
        self.setLayout(self.layout)

    def on_return_pressed(self):
        # Обрабатывает нажатие клавиши Enter
        self.controller.on_button_click('=')

    def validate_input(self, text):
        # Проверяет введенные символы и удаляет недопустимые
        allowed_chars = "0123456789+-*/().% "
        filtered_text = ''.join([char for char in text if char in allowed_chars])

        # Удаление лишних нулей в начале числа
        if filtered_text and not any(op in filtered_text for op in "+-*/().%"):
            # Если текст не содержит операторов, проверяем только числа
            parts = filtered_text.split('.')
            if len(parts) == 1:  # Целое число
                if parts[0].startswith('0') and len(parts[0]) > 1:
                    filtered_text = '0' + filtered_text[len(parts[0]):]
            elif len(parts) == 2:  # Дробное число
                if parts[0].startswith('0') and len(parts[0]) > 1:
                    filtered_text = '0.' + parts[1]

        if filtered_text != text:
            self.display.setText(filtered_text)

    def update_display(self, text):
        self.display.setText(text)