from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPainter, QColor, QFont
from PySide6.QtCore import Qt, QRect
import sys


class Board(QWidget):
    def __init__(self, rows=8, cols=8):
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.selected_cell = None
        self.dragging = False
        self.drag_start_cell = None

        # Einfaches Start-Setup: Figuren (weiß und schwarz)
        self.pieces = [[None for _ in range(cols)] for _ in range(rows)]
        self.setup_pieces()

    def setup_pieces(self):
        # Unicode-Schachfiguren (weiß groß, schwarz klein)
        # Reihen 0 und 1 schwarz, 6 und 7 weiß
        # R: Turm, N: Springer, B: Läufer, Q: Dame, K: König, P: Bauer

        # Schwarz (unten, Kleinbuchstaben)
        black_back_row = ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"]
        black_pawns = ["♟"] * 8

        # Weiß (oben, Großbuchstaben)
        white_back_row = ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"]
        white_pawns = ["♙"] * 8

        self.pieces[0] = black_back_row
        self.pieces[1] = black_pawns
        self.pieces[6] = white_pawns
        self.pieces[7] = white_back_row

    def paintEvent(self, event):
        painter = QPainter(self)
        w, h = self.width(), self.height()
        cell_size = min(w // self.cols, h // self.rows)
        x_offset = (w - self.cols * cell_size) // 2
        y_offset = (h - self.rows * cell_size) // 2

        font = QFont("Arial", int(cell_size * 0.7))
        painter.setFont(font)
        painter.setRenderHint(QPainter.TextAntialiasing)

        for row in range(self.rows):
            for col in range(self.cols):
                x = x_offset + col * cell_size
                y = y_offset + row * cell_size
                rect = QRect(x, y, cell_size, cell_size)

                # Feldfarbe und Highlight
                if self.selected_cell == (row, col):
                    painter.fillRect(rect, QColor("#aaddff"))
                elif (row + col) % 2 == 0:
                    painter.fillRect(rect, QColor("white"))
                else:
                    painter.fillRect(rect, QColor("gray"))

                painter.drawRect(rect)

                # Figur zeichnen (zentriert)
                piece = self.pieces[row][col]
                if piece:
                    painter.drawText(rect, Qt.AlignCenter | Qt.AlignVCenter, piece)

    def mousePressEvent(self, event):
        w, h = self.width(), self.height()
        cell_size = min(w // self.cols, h // self.rows)
        x_offset = (w - self.cols * cell_size) // 2
        y_offset = (h - self.rows * cell_size) // 2

        x, y = event.position().x(), event.position().y()

        if (
            x_offset <= x < x_offset + self.cols * cell_size
            and y_offset <= y < y_offset + self.rows * cell_size
        ):
            col = int((x - x_offset) // cell_size)
            row = int((y - y_offset) // cell_size)
            self.selected_cell = (row, col)
            self.dragging = True
            self.drag_start_cell = (row, col)
            self.update()

    def mouseMoveEvent(self, event):
        if self.dragging:
            # Optional: hier kann man z.B. Drag-Visualisierung ergänzen
            pass

    def mouseReleaseEvent(self, event):
        if not self.dragging:
            return

        w, h = self.width(), self.height()
        cell_size = min(w // self.cols, h // self.rows)
        x_offset = (w - self.cols * cell_size) // 2
        y_offset = (h - self.rows * cell_size) // 2

        x, y = event.position().x(), event.position().y()

        if (
            x_offset <= x < x_offset + self.cols * cell_size
            and y_offset <= y < y_offset + self.rows * cell_size
        ):
            col = int((x - x_offset) // cell_size)
            row = int((y - y_offset) // cell_size)

            # Zug ausführen (ohne Validierung)
            from_row, from_col = self.drag_start_cell
            piece = self.pieces[from_row][from_col]
            if piece:
                self.pieces[row][col] = piece
                self.pieces[from_row][from_col] = None

        self.selected_cell = None
        self.dragging = False
        self.drag_start_cell = None
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Board()
    window.setWindowTitle("Schachbrett mit Figuren und Drag & Drop")
    window.resize(600, 600)
    window.show()
    sys.exit(app.exec())
