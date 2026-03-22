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


        # self.toggle_textbox_checkbox = QCheckBox("Toggle Text Box")
        # self.toggle_textbox_checkbox.setChecked(False)
        # self.toggle_textbox_checkbox.stateChanged.connect(self.show_hide_textbox)

        self.label_credit = QLabel(self)
        self.label_credit.setText("M.Soft Mohammed Sami")
        self.label_credit.setAlignment(Qt.AlignCenter)

        self.clipboard = QApplication.clipboard()

        self.quick_refine_button = QPushButton("Click here before U paste")
        self.quick_refine_button.clicked.connect(self.quick_refine)


        self.layout.addWidget(self.quick_refine_button, 0, 0)
        self.layout.addWidget(self.label_credit, 1, 0)

        self.setWindowIcon(QIcon("PDF2TXT.png"))
        # self.layout.addWidget(self.toggle_textbox_checkbox, 0, 0)
        self.setWindowFlags(
            Qt.Window |
            Qt.CustomizeWindowHint |
            Qt.WindowMinimizeButtonHint |
            Qt.WindowCloseButtonHint |
            Qt.WindowStaysOnTopHint
        )
        self.setFixedSize(250, 70)
        self.move_to_bottom_right()
        # def refine(self):
    #     if self.paste_text_edit.toPlainText() != "":
    #         refined=[]
    #         for text in self.paste_text_edit.toPlainText().split("\n"):
    #             if text.endswith("\n") :
    #                 refined.append(text[:-1])
    #             else :
    #                 refined.append(text)
    #         self.paste_text_edit.blockSignals(True)
    #         self.paste_text_edit.clear()
    #         self.paste_text_edit.setPlainText(" ".join(refined))
    #         self.paste_text_edit.blockSignals(False)
    #         self.clipboard.setText(self.paste_text_edit.toPlainText())
    #     else :
    #         return

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
    # def show_hide_textbox(self):
    #     if self.toggle_textbox_checkbox.isChecked():
    #         self.paste_label = QLabel()
    #         self.paste_label.setText("Paste here")
    #         self.paste_label.setAlignment(Qt.AlignCenter)
    #         self.paste_label.setStyleSheet("font-size:14px;font-weight:bold;font-family:Ubuntu;")
    #
    #         self.paste_text_edit=QTextEdit()
    #         self.paste_text_edit.textChanged.connect(self.refine)
    #         self.layout.addWidget(self.paste_label,1,0)
    #         self.layout.addWidget(self.paste_text_edit,2,0)
    #         self.setMinimumSize(600,250)
    #         self.setMaximumSize(700, 400)
    #
    #     elif not self.toggle_textbox_checkbox.isChecked():
    #         if hasattr(self, "paste_text_edit"):
    #             self.layout.removeWidget(self.paste_text_edit)
    #             self.paste_text_edit.setParent(None)
    #             self.paste_text_edit.deleteLater()
    #         if hasattr(self, "paste_label"):
    #             self.layout.removeWidget(self.paste_label)
    #             self.paste_label.setParent(None)
    #             self.paste_label.deleteLater()
    #             self.setMinimumSize(140, 71)
    #             self.setMaximumSize(140,71)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = central_widget()
    window.show()
    sys.exit(app.exec())
