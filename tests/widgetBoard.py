from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import Qt, QRect
import sys


class Board(QWidget):
    def __init__(self, rows=8, cols=8):
        super().__init__()
        self.rows = rows
        self.cols = cols

    def paintEvent(self, event):
        painter = QPainter(self)

        # Aktuelle Größe des Fensters
        w = self.width()
        h = self.height()

        # Zellengröße (quadratisch, begrenzt durch kürzere Seite)
        cell_size = min(w // self.cols, h // self.rows)

        # Berechne Offset (zum Zentrieren des Boards)
        x_offset = (w - self.cols * cell_size) // 2
        y_offset = (h - self.rows * cell_size) // 2

        for row in range(self.rows):
            for col in range(self.cols):
                x = x_offset + col * cell_size
                y = y_offset + row * cell_size
                rect = QRect(x, y, cell_size, cell_size)

                # Farbe
                if (row + col) % 2 == 0:
                    painter.fillRect(rect, QColor("white"))
                else:
                    painter.fillRect(rect, QColor("gray"))

                painter.drawRect(rect)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Board()
    window.setWindowTitle("Lückenfreies Responsive Board")
    window.show()
    sys.exit(app.exec())
