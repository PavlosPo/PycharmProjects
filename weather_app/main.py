import requests
from twilio.rest import Client

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "5b0e757ba4fe2da8bf825265b80e00c1"
account_sid = "AC463a166c67762526743c60f2d1246fcf"
auth_token = "d98db09a7fcf54af78f44c9b443d67d9"

weather_params = {
    'lat': 38.246683654246965,
    'lon': 21.733417384813052,
    'appid': api_key,
    'exclude': "current,minutely,daily"
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
data = response.json()

# data = {'cod': '200', 'message': 0, 'cnt': 40, 'list': [{'dt': 1670868000, 'main': {'temp': 286.38, 'feels_like': 285.51, 'temp_min': 286.38, 'temp_max': 287.08, 'pressure': 1007, 'sea_level': 1007, 'grnd_level': 1005, 'humidity': 67, 'temp_kf': -0.7}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'clouds': {'all': 100}, 'wind': {'speed': 0.89, 'deg': 327, 'gust': 1.52}, 'visibility': 10000, 'pop': 0.5, 'rain': {'3h': 0.75}, 'sys': {'pod': 'n'}, 'dt_txt': '2022-12-12 18:00:00'}, {'dt': 1670878800, 'main': {'temp': 286.61, 'feels_like': 285.94, 'temp_min': 286.61, 'temp_max': 287.06, 'pressure': 1007, 'sea_level': 1007, 'grnd_level': 1005, 'humidity': 74, 'temp_kf': -0.45}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'clouds': {'all': 100}, 'wind': {'speed': 0.79, 'deg': 263, 'gust': 1.24}, 'visibility': 10000, 'pop': 0.5, 'rain': {'3h': 0.49}, 'sys': {'pod': 'n'}, 'dt_txt': '2022-12-12 21:00:00'}, {'dt': 1670889600, 'main': {'temp': 287.33, 'feels_like': 286.84, 'temp_min': 287.33, 'temp_max': 287.81, 'pressure': 1007, 'sea_level': 1007, 'grnd_level': 1005, 'humidity': 78, 'temp_kf': -0.48}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'clouds': {'all': 100}, 'wind': {'speed': 2.27, 'deg': 277, 'gust': 2.75}, 'visibility': 10000, 'pop': 0.46, 'rain': {'3h': 0.12}, 'sys': {'pod': 'n'}, 'dt_txt': '2022-12-13 00:00:00'}, {'dt': 1670900400, 'main': {'temp': 287.13, 'feels_like': 286.83, 'temp_min': 287.13, 'temp_max': 287.13, 'pressure': 1007, 'sea_level': 1007, 'grnd_level': 1005, 'humidity': 86, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'clouds': {'all': 100}, 'wind': {'speed': 2.56, 'deg': 299, 'gust': 3.08}, 'visibility': 10000, 'pop': 0.15, 'sys': {'pod': 'n'}, 'dt_txt': '2022-12-13 03:00:00'}, {'dt': 1670911200, 'main': {'temp': 287.19, 'feels_like': 286.9, 'temp_min': 287.19, 'temp_max': 287.19, 'pressure': 1008, 'sea_level': 1008, 'grnd_level': 1006, 'humidity': 86, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 100}, 'wind': {'speed': 2.05, 'deg': 304, 'gust': 3.05}, 'visibility': 10000, 'pop': 0.07, 'sys': {'pod': 'd'}, 'dt_txt': '2022-12-13 06:00:00'}, {'dt': 1670922000, 'main': {'temp': 289.46, 'feels_like': 289.1, 'temp_min': 289.46, 'temp_max': 289.46, 'pressure': 1009, 'sea_level': 1009, 'grnd_level': 1007, 'humidity': 75, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 100}, 'wind': {'speed': 2.77, 'deg': 321, 'gust': 3.81}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2022-12-13 09:00:00'}, {'dt': 1670932800, 'main': {'temp': 288.94, 'feels_like': 288.35, 'temp_min': 288.94, 'temp_max': 288.94, 'pressure': 1008, 'sea_level': 1008, 'grnd_level': 1006, 'humidity': 68, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': {'all': 100}, 'wind': {'speed': 4.6, 'deg': 317, 'gust': 5.69}, 'visibility': 10000, 'pop': 0.2, 'rain': {'3h': 0.14}, 'sys': {'pod': 'd'}, 'dt_txt': '2022-12-13 12:00:00'}, {'dt': 1670943600, 'main': {'temp': 287.21, 'feels_like': 286.6, 'temp_min': 287.21, 'temp_max': 287.21, 'pressure': 1009, 'sea_level': 1009, 'grnd_level': 1007, 'humidity': 74, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': {'all': 100}, 'wind': {'speed': 6.3, 'deg': 317, 'gust': 7.39}, 'visibility': 10000, 'pop': 0.39, 'rain': {'3h': 0.18}, 'sys': {'pod': 'd'}, 'dt_txt': '2022-12-13 15:00:00'}, {'dt': 1670954400, 'main': {'temp': 286.5, 'feels_like': 285.98, 'temp_min': 286.5, 'temp_max': 286.5, 'pressure': 1010, 'sea_level': 1010, 'grnd_level': 1008, 'humidity': 80, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'clouds': {'all': 100}, 'wind': {'speed': 3.29, 'deg': 322, 'gust': 4.26}, 'visibility': 10000, 'pop': 0.27, 'rain': {'3h': 0.25}, 'sys': {'pod': 'n'}, 'dt_txt': '2022-12-13 18:00:00'}, {'dt': 1670965200, 'main': {'temp': 286.33, 'feels_like': 285.82, 'temp_min': 286.33, 'temp_max': 286.33, 'pressure': 1010, 'sea_level': 1010, 'grnd_level': 1009, 'humidity': 81, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'clouds': {'all': 100}, 'wind': {'speed': 2.28, 'deg': 316, 'gust': 2.71}, 'visibility': 10000, 'pop': 0.46, 'rain': {'3h': 0.18}, 'sys': {'pod': 'n'}, 'dt_txt': '2022-12-13 21:00:00'}, {'dt': 1670976000, 'main': {'temp': 286.16, 'feels_like': 285.63, 'temp_min': 286.16, 'temp_max': 286.16, 'pressure': 1010, 'sea_level': 1010, 'grnd_level': 1009, 'humidity': 81, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'clouds': {'all': 100}, 'wind': {'speed': 0.35, 'deg': 250, 'gust': 0.48}, 'visibility': 10000, 'pop': 0.55, 'rain': {'3h': 0.26}, 'sys': {'pod': 'n'}, 'dt_txt': '2022-12-14 00:00:00'}, {'dt': 1670986800, 'main': {'temp': 285.78, 'feels_like': 285.29, 'temp_min': 285.78, 'temp_max': 285.78, 'pressure': 1011, 'sea_level': 1011, 'grnd_level': 1009, 'humidity': 84, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'clouds': {'all': 96}, 'wind': {'speed': 0.84, 'deg': 161, 'gust': 1.29}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2022-12-14 03:00:00'}, {'dt': 1670997600, 'main': {'temp': 286.16, 'feels_like': 285.68, 'temp_min': 286.16, 'temp_max': 286.16, 'pressure': 1012, 'sea_level': 1012, 'grnd_level': 1010, 'humidity': 83, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 98}, 'wind': {'speed': 0.83, 'deg': 131, 'gust': 1.38}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2022-12-14 06:00:00'}, {'dt': 1671008400, 'main': {'temp': 287.16, 'feels_like': 286.71, 'temp_min': 287.16, 'temp_max': 287.16, 'pressure': 1013, 'sea_level': 1013, 'grnd_level': 1011, 'humidity': 80, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 100}, 'wind': {'speed': 2.05, 'deg': 112, 'gust': 2.68}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2022-12-14 09:00:00'}, {'dt': 1671019200, 'main': {'temp': 287.39, 'feels_like': 287.04, 'temp_min': 287.39, 'temp_max': 287.39, 'pressure': 1011, 'sea_level': 1011, 'grnd_level': 1010, 'humidity': 83, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 100}, 'wind': {'speed': 3.01, 'deg': 109, 'gust': 3.53}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2022-12-14 12:00:00'}, {'dt': 1671030000, 'main': {'temp': 287.16, 'feels_like': 286.97, 'temp_min': 287.16, 'temp_max': 287.16, 'pressure': 1012, 'sea_level': 1012, 'grnd_level': 1010, 'humidity': 90, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': {'all': 100}, 'wind': {'speed': 2.92, 'deg': 141, 'gust': 3.8}, 'visibility': 10000, 'pop': 0.58, 'rain': {'3h': 0.67}, 'sys': {'pod': 'd'}, 'dt_txt': '2022-12-14 15:00:00'}, {'dt': 1671040800, 'main': {'temp': 287.15, 'feels_like': 287.01, 'temp_min': 287.15, 'temp_max': 287.15, 'pressure': 1012, 'sea_level': 1012, 'grnd_level': 1010, 'humidity': 92, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'clouds': {'all': 100}, 'wind': {'speed': 3.07, 'deg': 138, 'gust': 4.15}, 'visibility': 10000, 'pop': 0.66, 'rain': {'3h': 1.15}, 'sys': {'pod': 'n'}, 'dt_txt': '2022-12-14 18:00:00'}, {'dt': 1671051600, 'main': {'temp': 287.6, 'feels_like': 287.5, 'temp_min': 287.6, 'temp_max': 287.6, 'pressure': 1012, 'sea_level': 1012, 'grnd_level': 1010, 'humidity': 92, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'clouds': {'all': 100}, 'wind': {'speed': 2.82, 'deg': 143, 'gust': 3.83}, 'visibility': 10000, 'pop': 0.39, 'rain': {'3h': 0.6}, 'sys': {'pod': 'n'}, 'dt_txt': '2022-12-14 21:00:00'}, {'dt': 1671062400, 'main': {'temp': 287.96, 'feels_like': 287.87, 'temp_min': 287.96, 'temp_max': 287.96, 'pressure': 1012, 'sea_level': 1012, 'grnd_level': 1010, 'humidity': 91, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'clouds': {'all': 100}, 'wind': {'speed': 1.45, 'deg': 154, 'gust': 1.89}, 'visibility': 10000, 'pop': 0.43, 'rain': {'3h': 0.25}, 'sys': {'pod': 'n'}, 'dt_txt': '2022-12-15 00:00:00'}, {'dt': 1671073200, 'main': {'temp': 287.53, 'feels_like': 287.4, 'temp_min': 287.53, 'temp_max': 287.53, 'pressure': 1012, 'sea_level': 1012, 'grnd_level': 1010, 'humidity': 91, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'clouds': {'all': 98}, 'wind': {'speed': 0.43, 'deg': 195, 'gust': 0.72}, 'visibility': 10000, 'pop': 0.04, 'sys': {'pod': 'n'}, 'dt_txt': '2022-12-15 03:00:00'}, {'dt': 1671084000, 'main': {'temp': 287.32, 'feels_like': 287.12, 'temp_min': 287.32, 'temp_max': 287.32, 'pressure': 1013, 'sea_level': 1013, 'grnd_level': 1011, 'humidity': 89, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'clouds': {'all': 79}, 'wind': {'speed': 0.65, 'deg': 305, 'gust': 0.87}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2022-12-15 06:00:00'}, {'dt': 1671094800, 'main': {'temp': 290.5, 'feels_like': 290.38, 'temp_min': 290.5, 'temp_max': 290.5, 'pressure': 1014, 'sea_level': 1014, 'grnd_level': 1012, 'humidity': 80, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'clouds': {'all': 66}, 'wind': {'speed': 1.49, 'deg': 26, 'gust': 0.95}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2022-12-15 09:00:00'}, {'dt': 1671105600, 'main': {'temp': 291.08, 'feels_like': 290.97, 'temp_min': 291.08, 'temp_max': 291.08, 'pressure': 1013, 'sea_level': 1013, 'grnd_level': 1012, 'humidity': 78, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'clouds': {'all': 81}, 'wind': {'speed': 2.1, 'deg': 0, 'gust': 2.26}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2022-12-15 12:00:00'}, {'dt': 1671116400, 'main': {'temp': 289.64, 'feels_like': 289.49, 'temp_min': 289.64, 'temp_max': 289.64, 'pressure': 1014, 'sea_level': 1014, 'grnd_level': 1012, 'humidity': 82, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 100}, 'wind': {'speed': 0.22, 'deg': 150, 'gust': 0.45}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2022-12-15 15:00:00'}, {'dt': 1671127200, 'main': {'temp': 289.46, 'feels_like': 289.29, 'temp_min': 289.46, 'temp_max': 289.46, 'pressure': 1016, 'sea_level': 1016, 'grnd_level': 1014, 'humidity': 82, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'clouds': {'all': 100}, 'wind': {'speed': 1.68, 'deg': 186, 'gust': 1.6}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2022-12-15 18:00:00'}, {'dt': 1671138000, 'main': {'temp': 289.22, 'feels_like': 288.95, 'temp_min': 289.22, 'temp_max': 289.22, 'pressure': 1017, 'sea_level': 1017, 'grnd_level': 1015, 'humidity': 79, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'clouds': {'all': 100}, 'wind': {'speed': 1.66, 'deg': 202, 'gust': 1.62}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2022-12-15 21:00:00'}, {'dt': 1671148800, 'main': {'temp': 288.69, 'feels_like': 288.28, 'temp_min': 288.69, 'temp_max': 288.69, 'pressure': 1017, 'sea_level': 1017, 'grnd_level': 1015, 'humidity': 76, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'clouds': {'all': 97}, 'wind': {'speed': 0.98, 'deg': 239, 'gust': 0.97}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2022-12-16 00:00:00'}, {'dt': 1671159600, 'main': {'temp': 288.39, 'feels_like': 287.9, 'temp_min': 288.39, 'temp_max': 288.39, 'pressure': 1017, 'sea_level': 1017, 'grnd_level': 1015, 'humidity': 74, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'clouds': {'all': 57}, 'wind': {'speed': 1.18, 'deg': 217, 'gust': 1.26}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2022-12-16 03:00:00'}, {'dt': 1671170400, 'main': {'temp': 288.46, 'feels_like': 287.9, 'temp_min': 288.46, 'temp_max': 288.46, 'pressure': 1018, 'sea_level': 1018, 'grnd_level': 1016, 'humidity': 71, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'clouds': {'all': 78}, 'wind': {'speed': 0.92, 'deg': 196, 'gust': 1.01}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2022-12-16 06:00:00'}, {'dt': 1671181200, 'main': {'temp': 291.9, 'feels_like': 291.42, 'temp_min': 291.9, 'temp_max': 291.9, 'pressure': 1019, 'sea_level': 1019, 'grnd_level': 1017, 'humidity': 61, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 99}, 'wind': {'speed': 1.1, 'deg': 108, 'gust': 1.14}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2022-12-16 09:00:00'}, {'dt': 1671192000, 'main': {'temp': 292.91, 'feels_like': 292.51, 'temp_min': 292.91, 'temp_max': 292.91, 'pressure': 1017, 'sea_level': 1017, 'grnd_level': 1016, 'humidity': 60, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 100}, 'wind': {'speed': 1.54, 'deg': 28, 'gust': 1.5}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2022-12-16 12:00:00'}, {'dt': 1671202800, 'main': {'temp': 289.9, 'feels_like': 289.59, 'temp_min': 289.9, 'temp_max': 289.9, 'pressure': 1018, 'sea_level': 1018, 'grnd_level': 1016, 'humidity': 75, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 100}, 'wind': {'speed': 0.42, 'deg': 139, 'gust': 0.51}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2022-12-16 15:00:00'}, {'dt': 1671213600, 'main': {'temp': 289.81, 'feels_like': 289.54, 'temp_min': 289.81, 'temp_max': 289.81, 'pressure': 1019, 'sea_level': 1019, 'grnd_level': 1017, 'humidity': 77, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'clouds': {'all': 100}, 'wind': {'speed': 1.79, 'deg': 159, 'gust': 1.96}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2022-12-16 18:00:00'}, {'dt': 1671224400, 'main': {'temp': 289.28, 'feels_like': 288.93, 'temp_min': 289.28, 'temp_max': 289.28, 'pressure': 1019, 'sea_level': 1019, 'grnd_level': 1018, 'humidity': 76, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'clouds': {'all': 100}, 'wind': {'speed': 0.83, 'deg': 173, 'gust': 1.01}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2022-12-16 21:00:00'}, {'dt': 1671235200, 'main': {'temp': 288.93, 'feels_like': 288.52, 'temp_min': 288.93, 'temp_max': 288.93, 'pressure': 1019, 'sea_level': 1019, 'grnd_level': 1018, 'humidity': 75, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'clouds': {'all': 100}, 'wind': {'speed': 0.63, 'deg': 175, 'gust': 0.79}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2022-12-17 00:00:00'}, {'dt': 1671246000, 'main': {'temp': 288.45, 'feels_like': 287.97, 'temp_min': 288.45, 'temp_max': 288.45, 'pressure': 1019, 'sea_level': 1019, 'grnd_level': 1017, 'humidity': 74, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'clouds': {'all': 100}, 'wind': {'speed': 0.56, 'deg': 191, 'gust': 0.68}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2022-12-17 03:00:00'}, {'dt': 1671256800, 'main': {'temp': 288.42, 'feels_like': 287.86, 'temp_min': 288.42, 'temp_max': 288.42, 'pressure': 1020, 'sea_level': 1020, 'grnd_level': 1018, 'humidity': 71, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 100}, 'wind': {'speed': 0.78, 'deg': 229, 'gust': 0.81}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2022-12-17 06:00:00'}, {'dt': 1671267600, 'main': {'temp': 292.52, 'feels_like': 292.03, 'temp_min': 292.52, 'temp_max': 292.52, 'pressure': 1020, 'sea_level': 1020, 'grnd_level': 1019, 'humidity': 58, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 85}, 'wind': {'speed': 0.82, 'deg': 52, 'gust': 0.91}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2022-12-17 09:00:00'}, {'dt': 1671278400, 'main': {'temp': 293.48, 'feels_like': 293.03, 'temp_min': 293.48, 'temp_max': 293.48, 'pressure': 1018, 'sea_level': 1018, 'grnd_level': 1017, 'humidity': 56, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 93}, 'wind': {'speed': 1.35, 'deg': 42, 'gust': 1.55}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2022-12-17 12:00:00'}, {'dt': 1671289200, 'main': {'temp': 290.79, 'feels_like': 290.41, 'temp_min': 290.79, 'temp_max': 290.79, 'pressure': 1018, 'sea_level': 1018, 'grnd_level': 1016, 'humidity': 69, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 100}, 'wind': {'speed': 0.93, 'deg': 135, 'gust': 1.02}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2022-12-17 15:00:00'}], 'city': {'id': 252062, 'name': 'Velo', 'coord': {'lat': 37.9832, 'lon': 22.7661}, 'country': 'GR', 'population': 3018, 'timezone': 7200, 'sunrise': 1670823330, 'sunset': 1670857789}}

data_sliced = data['list'][:12]
will_rain = True

for hourly_data in data_sliced:
    condition_code = hourly_data['weather'][0]['id']
    if condition_code <= 700:
        will_rain = True

if will_rain:
    print('it will rain!')
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="+306940820115",
        from_="+12058557218",
        body="It's going to rain today. Remember to bring on ☂️")
    print(message.status)
