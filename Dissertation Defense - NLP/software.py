import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton
from PyQt5.QtGui import QFont
from spelling_corrections import Spell_Corrections

class SpellCorrectionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.create_window()

    def create_window(self):
        "Create the GUI Main in Window"
        # Create title of software
        self.setWindowTitle("Vietnamese Speliing Correction Software")
        self.setGeometry(300, 500, 700, 400)

        # Input the sentence is incorrect
        self.label = QLabel("Enter a sentence:")
        self.input_box = QTextEdit()
        self.input_box.setFont(QFont("Segoe UI", 10))

        # Create button for spelling checker and correction
        self.correct_button = QPushButton("Correct")
        self.correct_button.clicked.connect(self.correct_sentence)

        # Create label and result for the sentence has corrected
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input_box)
        layout.addWidget(self.correct_button)

        self.result_label = QLabel("Corrected sentence: ")
        self.output_box = QTextEdit()
        self.output_box.setFont(QFont("Segoe UI", 10))
        layout.addWidget(self.result_label)
        layout.addWidget(self.output_box)
        self.setLayout(layout)

    def correct_sentence(self):
        # Result the sentence in Vietnamese has been corrected
        sentence = self.input_box.toPlainText()
        spell_corrector = Spell_Corrections()
        corrected_sentence = spell_corrector.call(sentence)
        self.output_box.setText(corrected_sentence)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    spell_correction_app = SpellCorrectionApp()
    spell_correction_app.show()
    sys.exit(app.exec_())
