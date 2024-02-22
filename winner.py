from PyQt5.QtCore import Qt # layout2 sama window
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout # widget

# import random
from random import randint

def show_winner():
    random_number = randint(0, 99)
    text2.setText(str(random_number)) # mengubah text
    if random_number > 50:
        text1.setText('Winner')
    else:
        text1.setText('Lose')

# bikin window
app = QApplication([])
main_win = QWidget()

# kasih judul 
main_win.setWindowTitle("Winner's determiner")
# ubah ukuran window
main_win.resize(400, 200)

# bikin widget
text1 = QLabel('Click to find out winner')
text2 = QLabel('?')
button = QPushButton('Generate')

v_line = QVBoxLayout()

# nambahin widget ke layout
v_line.addWidget(text1, alignment=Qt.AlignCenter)
v_line.addWidget(text2, alignment=Qt.AlignCenter)
v_line.addWidget(button, alignment=Qt.AlignCenter)

main_win.setLayout(v_line)

# aktifin button --> fungsi show_winner
button.clicked.connect(show_winner)

# nampilin aplikasi
main_win.show()
app.exec_()
