from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QPainter, QColor, QPixmap
from PySide6.QtCore import Qt, QRect
import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

from board import Board
from vector import Vector


class BoardW(QWidget):
    def __init__(self, rows=8, cols=8):
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.rowsOld = -1
        self.colsOld = -1
        self.count = 0
        self.board = Board()
        self.selected_cell = None  # (row, col) der ausgewählten Zelle

    def paintEvent(self, event):
        painter = QPainter(self)
        w, h = self.width(), self.height()
        # print(f"w: {w}, h: {h}")
        cell_size = min(w // self.cols, h // self.rows)
        x_offset = (w - self.cols * cell_size) // 2
        y_offset = (h - self.rows * cell_size) // 2
        # print(f"x_off: {x_offset}, y_off: {y_offset}")
        for row in range(self.rows):
            for col in range(self.cols):
                x = x_offset + col * cell_size
                y = y_offset + row * cell_size
                rect = QRect(x, y, cell_size, cell_size)

                # Highlight, falls ausgewählt
                if self.selected_cell == (row, col):
                    painter.fillRect(rect, QColor("#aaddff"))  # hellblau
                else:
                    color = QColor("white") if (row + col) % 2 == 0 else QColor("gray")
                    painter.fillRect(rect, color)
                painter.drawRect(rect)
                field = self.board.position(row, col)
                if field != "":
                    piece = QPixmap(rf"png\{field.lower()}.png")
                    scaled = piece.scaled(
                        cell_size * 0.8,
                        cell_size * 0.8,
                        Qt.KeepAspectRatio,
                        Qt.SmoothTransformation,
                    )
                    px = x + (cell_size - scaled.width()) // 2
                    py = y + (cell_size - scaled.height()) // 2
                    painter.drawPixmap(px, py, scaled)

    def mousePressEvent(self, event):
        w, h = self.width(), self.height()
        cell_size = min(w // self.cols, h // self.rows)
        # print(f"cell_size: {cell_size}")
        x_offset = (w - self.cols * cell_size) // 2
        y_offset = (h - self.rows * cell_size) // 2

        x, y = event.position().x(), event.position().y()
        # print(x, y)
        # Prüfen ob Klick innerhalb des Boards
        if (
            x_offset <= x < x_offset + self.cols * cell_size
            and y_offset <= y < y_offset + self.rows * cell_size
        ):
            col = int((x - x_offset) // cell_size)
            row = int((y - y_offset) // cell_size)
            self.count += 1
            if self.count == 2:
                self.count = 0
                if (col != self.colsOld or row != self.rowsOld) and self.board.board[
                    self.rowsOld
                ][self.colsOld] != "":
                    if self.board.move(
                        Vector([row, col]) - Vector([self.rowsOld, self.colsOld]),
                        Vector([self.rowsOld, self.colsOld]),
                        self.board.board,
                        self.board.board[self.rowsOld][self.colsOld][1:],
                    ):
                        self.board.board[row][col] = self.board.board[self.rowsOld][
                            self.colsOld
                        ]
                        self.board.board[self.rowsOld][self.colsOld] = ""
                        print("worked")
                # print(f"col: {col}, row: {row}")
            self.colsOld = col
            self.rowsOld = row
            self.selected_cell = (row, col)
            self.update()  # Neuzeichnen


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BoardW()
    window.setWindowTitle("Responsive Board mit Auswahl")
    window.show()
    sys.exit(app.exec())
