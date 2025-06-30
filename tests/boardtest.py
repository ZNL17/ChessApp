from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPainter, QColor, QFont
from PySide6.QtCore import Qt, QRect
import sys


class BoardWidget(QWidget):
    def __init__(self, rows=8, cols=8, cell_size=80):
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.setFixedSize(cols * cell_size, rows * cell_size)

        # Piece positions: (row, col) -> piece (e.g. "♞")
        self.pieces = {(0, 1): "♞", (0, 6): "♞", (7, 1): "♘", (7, 6): "♘"}

        self.selected_piece = None  # (row, col) when a piece is selected

    def paintEvent(self, event):
        painter = QPainter(self)
        font = QFont("Arial", int(self.cell_size / 2))
        painter.setFont(font)

        for row in range(self.rows):
            for col in range(self.cols):
                # Draw square
                color = QColor("white") if (row + col) % 2 == 0 else QColor("gray")
                rect = QRect(
                    col * self.cell_size,
                    row * self.cell_size,
                    self.cell_size,
                    self.cell_size,
                )
                painter.fillRect(rect, color)
                painter.drawRect(rect)

                # Draw piece (if any)
                piece = self.pieces.get((row, col))
                if piece:
                    painter.drawText(rect, Qt.AlignCenter, piece)

    def mousePressEvent(self, event):
        row, col = event.y() // self.cell_size, event.x() // self.cell_size
        if (row, col) in self.pieces:
            self.selected_piece = (row, col)
        else:
            self.selected_piece = None

    def mouseReleaseEvent(self, event):
        if self.selected_piece:
            new_row, new_col = event.y() // self.cell_size, event.x() // self.cell_size
            piece = self.pieces.pop(self.selected_piece)
            self.pieces[(new_row, new_col)] = piece
            self.selected_piece = None
            self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    board = BoardWidget()
    board.setWindowTitle("Draggable Board with Pieces")
    board.show()
    sys.exit(app.exec())
