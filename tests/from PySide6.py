from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPainter, QPixmap
from PySide6.QtCore import QPoint
import sys


class DragImageWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.piece = QPixmap("wp.png")  # Make sure this path is correct
        self.piece_pos = QPoint(100, 100)  # Initial position on screen
        self.dragging = False
        self.offset = QPoint()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.piece_pos, self.piece)

    def mousePressEvent(self, event):
        click_pos = event.position().toPoint()
        rect = self.piece.rect().translated(self.piece_pos)
        if rect.contains(click_pos):
            self.dragging = True
            self.offset = click_pos - self.piece_pos

    def mouseMoveEvent(self, event):
        if self.dragging:
            self.piece_pos = event.position().toPoint() - self.offset
            self.update()

    def mouseReleaseEvent(self, event):
        self.dragging = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DragImageWidget()
    window.setWindowTitle("Drag PNG Example")
    window.resize(400, 400)
    window.show()
    sys.exit(app.exec())
