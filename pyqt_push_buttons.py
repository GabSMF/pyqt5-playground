# PyQt5 Introduction
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Click me!", self)
        self.label = QLabel("Hello",self)
        self.setWindowTitle("Hello World")
        self.setGeometry(700, 300, 500, 500)
        self.init_ui()

    def init_ui(self):
        self.button.setGeometry(150,200,200,100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click)

        self.label.setGeometry(150,300,200,100)
        self.label.setStyleSheet("font-size: 50px;")

    def on_click(self):
        self.label.setText("Goodbye!")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()