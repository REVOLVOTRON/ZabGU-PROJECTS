class CalculatorLogic:
    def __init__(self, gui):
        self.gui = gui

    def normalize_number(self, text):
        """Нормализует число, удаляя лишние нули"""
        if '.' in text:
            return str(float(text))
        else:
            return str(int(text))

    def on_button_click(self, text):
        """Обрабатывает нажатие кнопки"""
        current_text = self.gui.display.text()

        if text == 'C':
            self.gui.update_display('')
        elif text == '=':
            try:
                # Нормализуем все числа в выражении
                normalized_expression = self.normalize_expression(current_text)
                result = eval(normalized_expression)
                self.gui.update_display(str(result))
            except Exception as e:
                self.gui.update_display('Error')
        elif text == '%':
            try:
                value = float(current_text)
                self.gui.update_display(str(value / 100))
            except ValueError:
                self.gui.update_display('Error')
        else:
            self.gui.update_display(current_text + text)

    def normalize_expression(self, expression):
        """Нормализует все числа в выражении"""
        import re
        parts = re.split(r'([\+\-\*/\(\)])', expression)  # Разделяем выражение по операторам
        normalized_parts = []
        for part in parts:
            if part.isdigit() or (part.replace('.', '', 1).isdigit() and '.' in part):  # Проверяем, является ли часть числом
                normalized_parts.append(self.normalize_number(part))
            else:
                normalized_parts.append(part)
        return ''.join(normalized_parts)