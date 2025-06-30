import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QTabWidget, 
                            QLabel, QFrame, QHBoxLayout)
from PyQt6.QtCore import Qt
from login_window import LoginWindow
from db import create_connection
from widgets import TableWidget

TABLES = [
    ("Оборудование", "ОБОРУДОВАНИЕ"),
    ("Рабочие места", "РАБОЧЕЕ_МЕСТО"),
    ("Сотрудники", "СОТРУДНИК"),
    ("Выдача техники", "ВЫДАЧА_ТЕХНИКИ"),
    ("Обслуживание", "ОБСЛУЖИВАНИЕ"),
    ("Списание", "СПИСАНИЕ"),
    ("Закупки", "ЗАКУПКИ"),
]

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Учет оборудования и сотрудников")
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)

        # --- Заголовок и подзаголовок по центру с разделителями ---
        header_layout = QHBoxLayout()
        header_layout.setSpacing(10)

        # Левая вертикальная линия
        left_line = QFrame()
        left_line.setFrameShape(QFrame.Shape.VLine)
        left_line.setFrameShadow(QFrame.Shadow.Sunken)
        header_layout.addWidget(left_line)

        # Заголовок и подзаголовок в вертикальном layout по центру
        title_sub_layout = QVBoxLayout()
        title_sub_layout.setSpacing(0)

        title_label = QLabel("ООО «Разработчики Программ»")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("""
            QLabel {
                font-size: 24px;
                font-weight: bold;
                color: #1565c0;
                margin-bottom: 0px;
            }
        """)
        title_sub_layout.addWidget(title_label)

        # Разделительная палка между заголовком и подзаголовком
        center_line = QFrame()
        center_line.setFrameShape(QFrame.Shape.HLine)
        center_line.setFrameShadow(QFrame.Shadow.Sunken)
        center_line.setStyleSheet("color: #1565c0; background: #1565c0; max-height: 2px;")
        title_sub_layout.addWidget(center_line)

        subtitle_label = QLabel("Учет оборудования и сотрудников")
        subtitle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                color: #555;
                font-style: italic;
                margin-top: 0px;
                margin-bottom: 0px;
            }
        """)
        title_sub_layout.addWidget(subtitle_label)

        header_layout.addLayout(title_sub_layout)

        # Правая вертикальная линия
        right_line = QFrame()
        right_line.setFrameShape(QFrame.Shape.VLine)
        right_line.setFrameShadow(QFrame.Shadow.Sunken)
        header_layout.addWidget(right_line)

        main_layout.addLayout(header_layout)

        # --- Табы с таблицами ---
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.TabPosition.North)
        self.tabs.setMovable(True)
        self.tabs.setStyleSheet("""
            QTabWidget::pane { 
                border: 1px solid #1565c0; 
                border-radius: 8px; 
                background: #fff;
            }
            QTabBar::tab {
                background: #e3f2fd;
                color: #1565c0;
                border: 1px solid #90caf9;
                border-bottom: none;
                min-width: 110px;
                min-height: 26px;
                font-size: 13px;
                padding: 6px;
                margin-right: 2px;
                border-radius: 0;
                font-weight: 500;
            }
            QTabBar::tab:first {
                border-top-left-radius: 8px;
                border-top-right-radius: 0;
            }
            QTabBar::tab:last {
                border-top-left-radius: 0;
                border-top-right-radius: 8px;
            }
            QTabBar::tab:selected {
                background: #1565c0;
                color: #fff;
                font-weight: bold;
            }
            QTabBar::tab:hover {
                background: #1976d2;
                color: #fff;
            }
            QWidget {
                background: #fff;
                color: #333;
            }
        """)
        
        for label, table in TABLES:
            self.tabs.addTab(TableWidget(table), label)

        main_layout.addWidget(self.tabs, stretch=1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    create_connection()

    login = LoginWindow()
    if login.exec():
        window = MainWindow()
        window.showMaximized()
        sys.exit(app.exec())
    else:
        sys.exit()