import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QApplication, QPlainTextEdit, QLabel, QTextEdit


class central_widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Central Widget")
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.paste_label = QLabel()
        self.paste_label.setText("Paste here")
        self.paste_label.setAlignment(Qt.AlignCenter)
        self.paste_label.setStyleSheet("font-size:14px;font-weight:bold;font-family:Ubuntu;")

        self.paste_text_edit=QTextEdit()
        self.paste_text_edit.textChanged.connect(self.refine)

        self.clipboard = QApplication.clipboard()

        self.layout.addWidget(self.paste_label,0,0)
        self.layout.addWidget(self.paste_text_edit,1,0)

        self.setMinimumSize(600,150)




    def refine(self):
        if self.paste_text_edit.toPlainText() != "":
            refined=[]
            for text in self.paste_text_edit.toPlainText().split("\n"):
                if text.endswith("\n") :
                    refined.append(text[:-1])
                else :
                    refined.append(text)
            self.paste_text_edit.clear()
            self.paste_text_edit.setPlainText(" ".join(refined))

            self.clipboard.setText(self.paste_text_edit.toPlainText())
        else :
            return





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = central_widget()
    window.show()
    sys.exit(app.exec())
