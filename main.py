# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     w = QWidget()
#     w.resize(300,300)
#     w.setWindowTitle("Guru99")
#     w.show()
#     sys.exit(app.exec_())
#
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox
#
#
# def dialog():
#     mbox = QMessageBox()
#
#     mbox.setText("Your allegiance has been noted")
#     mbox.setDetailedText("You are now a disciple and subject of the all-knowing Guru")
#     mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
#     mbox.exec_()
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     w = QWidget()
#     w.resize(300, 300)
#     w.setWindowTitle('ССНЭ')
#
#     label = QLabel(w)
#     label.setText("label 1")
#     label.move(100, 130)
#     label.show()
#
#     btn = QPushButton(w)
#     btn.setText('ok')
#     btn.move(110, 150)
#     btn.show()
#     btn.clicked.connect(dialog)
#
#     w.show()
#     sys.exit(app.exec_())

# from PyQt5.QtWidgets import *
# import sys
#
#
# class Window(QWidget):
#     def __init__(self):
#         QWidget.__init__(self)
#         self.setWindowTitle("Hello")
#         layout = QGridLayout()
#         self.setLayout(layout)
#         label = QLabel("Hello, World!")
#         layout.addWidget(label, 0, 0)
#
# app = QApplication([])
# screen = Window()
# screen.show()
# sys.exit(app.exec_())


from PyQt5 import QtWidgets, uic
import sys

app = QtWidgets.QApplication([])
win = uic.loadUi("gui.ui")  # расположение вашего файла .ui

win.show()
sys.exit(app.exec())
