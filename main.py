import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel("70°F")
        self.emoji_label = QLabel("☀️", self)
        self.description_label = QLabel("Sunny", self)

        self.setupUI()

    def setupUI(self):
        self.setGeometry(700,700,500,500)
        self.setStyleSheet("background-color: white; text-color: black")
        self.setWindowTitle("Weather App")
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_label.setStyleSheet("color: black; font-size: 20px")

        #self.city_label.setGeometry(300,300,50,100)

        self.city_input.setGeometry(250,250,50,100)
        self.city_input.setStyleSheet("color: black; border: 1px solid black; font-size: 20px; padding: 10px")

        self.get_weather_button.setStyleSheet("color:black; border: 1px solid black;")
        self.temperature_label.setStyleSheet("color: black")
        self.emoji_label.setStyleSheet("color: black")
        self.description_label.setStyleSheet("color: black")

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
