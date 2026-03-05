"""
simple pyside 6 based app to remove line breaks created when
copying from pdf files to text files
"""
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from central_widget import central_widget


app=QApplication(sys.argv)
window=QMainWindow()
central =central_widget()
window.setCentralWidget(central)
window.setWindowTitle("PDF Copy Paste Refinery")








central.show()
central.setWindowTitle("PDF Copy Paste Refinery")
central.raise_()
window.show()
app.exec_()