import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QApplication, QPlainTextEdit, QLabel, QTextEdit, \
    QPushButton


class central_widget(QWidget):
    def __init__(self):
        super().__init__()

        def focusInEvent(self, event):
            self.clear()
            super().focusInEvent(event)
        self.setWindowTitle("Central Widget")
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # self.paste_label = QLabel()
        # self.paste_label.setText("Paste here")
        # self.paste_label.setAlignment(Qt.AlignCenter)
        # self.paste_label.setStyleSheet("font-size:14px;font-weight:bold;font-family:Ubuntu;")
        #
        # self.paste_text_edit=QTextEdit()
        # self.paste_text_edit.textChanged.connect(self.refine)

        self.clipboard = QApplication.clipboard()

        self.quick_refine_button = QPushButton("Refine")
        self.quick_refine_button.clicked.connect(self.quick_refine)

        # self.layout.addWidget(self.paste_label,0,0)
        # self.layout.addWidget(self.paste_text_edit,1,0)
        self.layout.addWidget(self.quick_refine_button, 2, 0)
        # self.setMinimumSize(600,150)




    def refine(self):
        if self.paste_text_edit.toPlainText() != "":
            refined=[]
            for text in self.paste_text_edit.toPlainText().split("\n"):
                if text.endswith("\n") :
                    refined.append(text[:-1])
                else :
                    refined.append(text)
            self.paste_text_edit.blockSignals(True)
            self.paste_text_edit.clear()
            self.paste_text_edit.setPlainText(" ".join(refined))
            self.paste_text_edit.blockSignals(False)
            self.clipboard.setText(self.paste_text_edit.toPlainText())
        else :
            return

    def quick_refine(self):
        if self.clipboard.text() != "":
            refined=[]
            for text in self.clipboard.text().split("\n"):
                if text.endswith("\n") :
                    refined.append(text[:-1])
                else:
                    refined.append(text)
            self.clipboard.setText(" ".join(refined))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = central_widget()
    window.show()
    sys.exit(app.exec())
