from PyQt6.QtWidgets import QApplication
from windows.main import MainWindow

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec()
