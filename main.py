import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QGridLayout
from PyQt5.QtCore import Qt
from dotenv import load_dotenv
import os



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
        background-color: #e0fbfc;
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
            background-color: #2677ad;
            border: 2px solid #cccccc;
            border-radius: 10px;
            padding: 20px;
            border-color: white;
            color: white;
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
        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
            load_dotenv('/Users/jonahtran/Desktop/Github/Python Project/.env')
            api_key = os.getenv('MY_API_KEY')
            print(api_key)
            if not api_key:
                 self.display_error("API Key not found")
                 return
            
            city = self.city_input.text()
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
            response = requests.get(url)
            data = response.json()
            print(data)

            if data["cod"] == 200:
                self.display_weather(data)
            else:
                self.display_error(f"Error: {data['message']}")

    def display_error(self, message):
         self.city_input.setText("Error: No City Found")
    
    def display_weather(self, data):
        location = data["name"]
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        temp_min = data["main"]["temp_min"]
        temp_max = data["main"]["temp_min"]

        temperature_f = self.convert_temperature(temperature)
        temp_min_f = self.convert_temperature(temp_min)
        temp_max_f = self.convert_temperature(temp_max)

        self.location_label.setText(location)
        self.temperature_label.setText(f"{int(temperature_f)}°F")
        self.description_label.setText(description.capitalize())
        self.extremes_label.setText(f"High: {temp_max_f:.1f}°F, Low: {temp_min_f:.1f}°F")

        weather_icon = data["weather"][0]["icon"]
        self.emoji_label.setText(self.get_weather_emoji(weather_icon))

    def get_weather_emoji(self, icon_code):
        # Map OpenWeatherMap icon codes to emojis
        emoji_map = {
            "01d": "☀️",  # Clear sky (day)
            "01n": "🌙",  # Clear sky (night)
            "02d": "⛅",  # Few clouds (day)
            "02n": "⛅",  # Few clouds (night)
            "03d": "☁️",  # Scattered clouds
            "03n": "☁️",  # Scattered clouds
            "04d": "☁️",  # Broken clouds
            "04n": "☁️",  # Broken clouds
            "09d": "🌧️",  # Shower rain
            "09n": "🌧️",  # Shower rain
            "10d": "🌦️",  # Rain (day)
            "10n": "🌧️",  # Rain (night)
            "11d": "⛈️",  # Thunderstorm
            "11n": "⛈️",  # Thunderstorm
            "13d": "❄️",  # Snow
            "13n": "❄️",  # Snow
            "50d": "🌫️",  # Mist
            "50n": "🌫️",  # Mist
        }
        # Return the corresponding emoji or a default emoji if the icon code is not found
        return emoji_map.get(icon_code, "❓")


    def convert_temperature(self, temperature):
         temp = temperature - 273.15
         temp = temp * 9/5
         temp = temp + 32
         return temp



if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("MY_API_KEY")
    print(api_key)
    #app = QApplication(sys.argv)
    #eather_app = WeatherApp()
    #weather_app.show()
    #sys.exit(app.exec_())
