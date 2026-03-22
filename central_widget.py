import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QApplication, QPlainTextEdit, QLabel, QTextEdit, \
    QPushButton, QMenu, QCheckBox

from PySide6.QtGui import QIcon
class central_widget(QWidget):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("PDF Refinery")
        self.layout = QGridLayout()
        self.setLayout(self.layout)


        self.toggle_textbox_checkbox = QCheckBox("Toggle ontop")
        self.toggle_textbox_checkbox.setChecked(False)
        self.toggle_textbox_checkbox.stateChanged.connect(self.toggle_on_top)

        self.label_credit = QLabel(self)
        self.label_credit.setText("M.Soft Mohammed Sami")
        self.label_credit.setAlignment(Qt.AlignCenter)

        self.clipboard = QApplication.clipboard()

        self.quick_refine_button = QPushButton("Click here before U paste")
        self.quick_refine_button.clicked.connect(self.quick_refine)


        self.layout.addWidget(self.quick_refine_button, 0, 0)
        self.layout.addWidget(self.label_credit, 1, 0)
        self.layout.addWidget(self.toggle_textbox_checkbox, 2, 0)

        self.setWindowIcon(QIcon("PDF2TXT.png"))


        self.setFixedSize(250, 130)
        self.move_to_bottom_right()

    def quick_refine(self):
        if self.clipboard.text() != "":
            refined=[]
            for text in self.clipboard.text().split("\n"):
                if text.endswith("\n") :
                    refined.append(text[:-1])
                else:
                    refined.append(text)
            self.clipboard.setText(" ".join(refined))

    def move_to_bottom_right(self):
        screen = self.screen().availableGeometry()

        margin = 35
        x = screen.x() + screen.width() - self.width()
        y = screen.y() + screen.height() - self.height() - margin

        self.move(x, y)
    def toggle_on_top(self):
        if self.toggle_textbox_checkbox.isChecked():
            self.setWindowFlags(
            Qt.Window |
            Qt.CustomizeWindowHint |
            Qt.WindowMinimizeButtonHint |
            Qt.WindowCloseButtonHint |
            Qt.WindowStaysOnTopHint
        )
        else:
            self.setWindowFlags(
                Qt.Window |
                Qt.CustomizeWindowHint |
                Qt.WindowMinimizeButtonHint |
                Qt.WindowCloseButtonHint

            )
        self.show()
        self.raise_()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = central_widget()
    window.show()
    sys.exit(app.exec())
