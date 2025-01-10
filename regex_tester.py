import sys
import re

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton


class RegexTester(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Regex Tester')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        # Regex input
        regex_layout = QHBoxLayout()
        regex_label = QLabel('Regex:')
        self.regex_input = QLineEdit()
        regex_layout.addWidget(regex_label)
        regex_layout.addWidget(self.regex_input)
        layout.addLayout(regex_layout)

        # Test string input
        test_string_layout = QHBoxLayout()
        test_string_label = QLabel('Test String:')
        self.test_string_input = QTextEdit()
        test_string_layout.addWidget(test_string_label)
        test_string_layout.addWidget(self.test_string_input)
        layout.addLayout(test_string_layout)

        # Results output
        results_label = QLabel('Results:')
        self.results_output = QTextEdit()
        self.results_output.setReadOnly(True)
        layout.addWidget(results_label)
        layout.addWidget(self.results_output)

        # Test button
        self.test_button = QPushButton('Test Regex')
        self.test_button.clicked.connect(self.test_regex)
        layout.addWidget(self.test_button)

        self.setLayout(layout)

    def test_regex(self):
        regex = self.regex_input.text()
        test_string = self.test_string_input.toPlainText()

        try:
            result = re.findall(regex, test_string)

            if result:
                self.results_output.setPlainText("\n".join(result))
            else:
                self.results_output.setPlainText("No matches found.")
        except re.error as e:
            self.results_output.setPlainText(f"Invalid regex: {str(e)}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RegexTester()
    ex.show()
    sys.exit(app.exec())
