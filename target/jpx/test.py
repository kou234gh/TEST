import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt6 Sample')
        self.setGeometry(100, 100, 300, 200)

        button = QPushButton('Click me!', self)
        button.move(50, 50)
        button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        print('Button clicked')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
