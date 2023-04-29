from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QFrame, QLabel, QHBoxLayout
from fonts import heading_font, sized_font
import data


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app

        # ------------------------------ menus and menu options ------------------------------
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')
        quit_action = file_menu.addAction('Quit')
        quit_action.triggered.connect(self.quit_app)
        town_menu = menu_bar.addMenu('Town')
        for town in data.town_data['towns']:
            selection = town_menu.addAction(town['name'])
            selection.triggered.connect(self.set_labels)
        font_menu = menu_bar.addMenu('Font')
        font_option1 = font_menu.addAction('Small (default)')
        font_option1.triggered.connect(self.change_font)
        font_option2 = font_menu.addAction('Medium')
        font_option2.triggered.connect(self.change_font)
        font_option3 = font_menu.addAction('Large')
        font_option3.triggered.connect(self.change_font)

        # ------------------------------ central widget ------------------------------
        self.main_frame = QFrame()
        self.setCentralWidget(self.main_frame)
        self.main_layout = QVBoxLayout()
        self.main_frame.setLayout(self.main_layout)

        # ------------------------------ heading ------------------------------
        self.town_heading = QLabel('')
        self.town_heading.setFont(heading_font())
        self.main_layout.addWidget(self.town_heading)

        # ------------------------------ population in 2010 ------------------------------
        self.pop_frame = QFrame()
        self.main_layout.addWidget(self.pop_frame)
        self.pop_layout = QHBoxLayout()
        self.pop_frame.setLayout(self.pop_layout)

        self.label1 = QLabel('2010 population: ')
        self.pop_layout.addWidget(self.label1)
        self.label2 = QLabel('')
        self.pop_layout.addWidget(self.label2)

        # ------------------------------ total area (sq mi) ------------------------------
        self.area_frame = QFrame()
        self.main_layout.addWidget(self.area_frame)
        self.area_layout = QHBoxLayout()
        self.area_frame.setLayout(self.area_layout)
        self.label3 = QLabel('Total area (sq mi): ')
        self.area_layout.addWidget(self.label3)
        self.label4 = QLabel('')
        self.area_layout.addWidget(self.label4)

        # ------------------------------ total land (sq mi) ------------------------------
        self.land_frame = QFrame()
        self.main_layout.addWidget(self.land_frame)
        self.land_layout = QHBoxLayout()
        self.land_frame.setLayout(self.land_layout)
        self.label5 = QLabel('Total land (sq mi): ')
        self.land_layout.addWidget(self.label5)
        self.label6 = QLabel('')
        self.land_layout.addWidget(self.label6)

        # ------------------------------ total density (person / sq mi) ------------------------------
        self.dens_frame = QFrame()
        self.main_layout.addWidget(self.dens_frame)
        self.dens_layout = QHBoxLayout()
        self.dens_frame.setLayout(self.dens_layout)
        self.label7 = QLabel('Density (person / sq mi land): ')
        self.dens_layout.addWidget(self.label7)
        self.label8 = QLabel('')
        self.dens_layout.addWidget(self.label8)

        # ------------------------------ total water (sq mi) ------------------------------
        self.wtr_frame = QFrame()
        self.main_layout.addWidget(self.wtr_frame)
        self.wtr_layout = QHBoxLayout()
        self.wtr_frame.setLayout(self.wtr_layout)
        self.label9 = QLabel('Total water (sq mi): ')
        self.wtr_layout.addWidget(self.label9)
        self.label10 = QLabel('')
        self.wtr_layout.addWidget(self.label10)

        # ------------------------------ set default font of non-heading labels ------------------------------
        self.change_font()

    def quit_app(self):
        self.app.quit()

    def set_labels(self):
        sender_text = self.sender().text()
        self.town_heading.setText(sender_text)
        self.label2.setText(data.get_pop(sender_text))
        self.label4.setText(data.get_area(sender_text))
        self.label6.setText(data.get_land(sender_text))
        self.label8.setText(data.get_dens(sender_text))
        self.label10.setText(data.get_wtr(sender_text))

    def change_font(self):
        sender_text = ''
        if self.sender():
            sender_text = self.sender().text()
        if sender_text == 'Large':
            size = 16
        elif sender_text == 'Medium':
            size = 14
        else:
            size = 12
        self.label1.setFont(sized_font(size))
        self.label2.setFont(sized_font(size))
        self.label3.setFont(sized_font(size))
        self.label4.setFont(sized_font(size))
        self.label5.setFont(sized_font(size))
        self.label6.setFont(sized_font(size))
        self.label7.setFont(sized_font(size))
        self.label8.setFont(sized_font(size))
        self.label9.setFont(sized_font(size))
        self.label10.setFont(sized_font(size))
