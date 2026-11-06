from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QRadioButton, QHBoxLayout, QVBoxLayout, QButtonGroup
from random import shuffle
app = QApplication([])

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = [
    Question("Переклади англійською слово автомобіль", "car", "bus", "taxi", "ship"),
    Question("Скільки буде 2*2+2?", "6", "10", "2", "8"),
    Question("Якого кольору вода?", "прозорого", "синього", "зеленого", "червоного"),
    Question("Якого кольору небо?", "блакитного", "червоного", "жовтого", "чорного")
]
current_question = -1 

screen = QWidget()
screen.show()
screen.resize(600, 300)
screen.setWindowTitle("Memory Card")

title = QLabel("Переклади англійською слово автомобіль")
ans_btn1 = QRadioButton("car")
ans_btn2 = QRadioButton("bus")
ans_btn3 = QRadioButton("taxi")
ans_btn4 = QRadioButton("ship")
answer_button = QPushButton("Відповідь")

radio_group = QButtonGroup()
radio_group.addButton(ans_btn1)
radio_group.addButton(ans_btn2)
radio_group.addButton(ans_btn3)
radio_group.addButton(ans_btn4)

answers = [ans_btn1, ans_btn2, ans_btn3, ans_btn4]

total_line = QVBoxLayout()
line_1 = QHBoxLayout()
line_2 = QHBoxLayout()
line_3 = QHBoxLayout()
line_4 = QHBoxLayout()

line_1.addWidget(title, alignment=Qt.AlignCenter)

line_2.addWidget(ans_btn1, alignment=Qt.AlignCenter)
line_2.addWidget(ans_btn2, alignment=Qt.AlignCenter)

line_3.addWidget(ans_btn3, alignment=Qt.AlignCenter)
line_3.addWidget(ans_btn4, alignment=Qt.AlignCenter)

line_4.addWidget(answer_button, alignment=Qt.AlignCenter)

total_line.addLayout(line_1)
total_line.addLayout(line_2)
total_line.addLayout(line_3)
total_line.addLayout(line_4)

screen.setLayout(total_line)

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    title.setText(q.question)
    answer_button.setText("Відповідь")

def show_correct(res):
    title.setText(res)
    answer_button.setText("Наступне запитання")

def next_question():
    global current_question
    current_question += 1
    if current_question >= len(questions_list):
        current_question = 0

    q = questions_list[current_question]
    ask(q)

def click_OK():
    if answer_button.text() == "Відповідь":
        if answers[0].isChecked():
            show_correct("Правильно!")
        else:
            if ans_btn1.isChecked() or ans_btn2.isChecked() or ans_btn3.isChecked() or ans_btn4.isChecked():
                show_correct("Неправильно!")
            else:
                title.setText("Не обрана відповідь!")
                QTimer.singleShot(1000, lambda: title.setText(questions_list[current_question].question))
                return
    else:
        radio_group.setExclusive(False)
        ans_btn1.setChecked(False)
        ans_btn2.setChecked(False)
        ans_btn3.setChecked(False)
        ans_btn4.setChecked(False)
        radio_group.setExclusive(True)
        next_question()

answer_button.clicked.connect(click_OK)
next_question()

app.exec_()
