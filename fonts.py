from PySide6.QtGui import QFont


def heading_font():
    heading_font = QFont()
    heading_font.setPointSize(20)
    heading_font.setBold(True)
    return heading_font


def sized_font(size):
    the_font = QFont()
    the_font.setPointSize(size)
    return the_font
