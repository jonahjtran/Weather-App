import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QGridLayout
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        #Input field for city name
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)

        #weather text box
        self.location_label = QLabel("Chicago", self)
        self.temperature_label = QLabel("60°F", self)
        self.emoji_label = QLabel("☀️", self)
        self.description_label = QLabel("Snowing", self)
        self.extremes_label = QLabel("High: 70°F, Low: 40°F", self)
        
        self.setupUI()

    def setupUI(self):
        self.setGeometry(700,700,500,500)
        self.setWindowTitle("Weather App")

        self.setStyleSheet("""
    QWidget {
        background-color: white;
        color: black;
        font-size: 16px;
    }
    QLabel {
        font-size: 20px;
        color: #333333;
    }
    QLineEdit {
        border: 2px solid #cccccc;
        border-radius: 5px;
        padding: 10px;
        font-size: 18px;
    }
    QPushButton {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        font-size: 18px;
        border-radius: 5px;
    }
    QPushButton:hover {
        background-color: #45a049;
    }
""")
        
        #main layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)

        vbox.setAlignment(Qt.AlignCenter)

        #weather text box
        weather_box = QWidget()
        weather_box.setStyleSheet("""
            background-color: #f0f0f0;
            border: 2px solid #cccccc;
            border-radius: 10px;
            padding: 20px;
            border-color: black
        """)

        grid = QGridLayout()
        grid.addWidget(self.location_label, 0,0,1,2, Qt.AlignCenter)
        grid.addWidget(self.temperature_label, 1, 0, Qt.AlignCenter)
        grid.addWidget(self.emoji_label, 1, 1, Qt.AlignCenter)
        grid.addWidget(self.description_label, 2, 0, 1, 2, Qt.AlignCenter)
        grid.addWidget(self.extremes_label, 3, 0, 1, 2, Qt.AlignCenter)

        weather_box.setLayout(grid)
        vbox.addWidget(weather_box)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignHCenter)

        self.city_input.setGeometry(250,250,50,100)
        self.city_input.setStyleSheet("color: black; border: 1px solid black; font-size: 20px; padding: 10px")
        self.city_input.setAlignment(Qt.AlignTop)

        self.get_weather_button.setStyleSheet("color:black; border: 1px solid black;")

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
