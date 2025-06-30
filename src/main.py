from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import Qt, QRect
import sys

class BoardWidget(QWidget):
    def __init__(self, rows=8, cols=8, cell_size=60):
        super().__init__()
        self.rows = rows 
        self.cols = cols
        self.cell_size = cell_size
        self.setFixedSize(cols * cell_size, rows * cell_size)

    def paintEvent(self, event):
        painter = QPainter(self)
        for row in range(self.rows):
            for col in range(self.cols):
                color = QColor("white") if (row + col) % 2 == 0 else QColor("gray")
                rect = QRect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                painter.fillRect(rect, color)
                painter.drawRect(rect)
if __name__ == "__main__": 
    app = QApplication(sys.argv)
    board = BoardWidget()
    board.setWindowTitle("Cusom Board")
    board.show()
    sys.exit(app.exec())