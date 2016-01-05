__author__ = 'Eivind'


class Sensor:
    def __init__(self, id, channel):
        self.id = id
        self.channel = channel
        self.name = ''

        self.max_temp = -500
        self.min_temp = -500
        self.max_temp_today = -500
        self.min_temp_today = -500
        self.current_temp = -500

        self.max_humidity = -500
        self.min_humidity = -500
        self.max_humidity_today = -500
        self.min_humidity_today = -500
        self.current_humidity = -500

    def set_name(self, name):
        self.name = name

    def set_temp(self, temp):
        self.current_temp = temp
        if temp < self.min_temp or self.min_temp == -500:
            self.min_temp = temp
            self.min_temp_today = temp
        elif temp < self.min_temp_today or self.min_temp_today == -500:
            self.min_temp_today = temp
        elif temp > self.max_temp or self.max_temp == -500:
            self.max_temp = temp
            self.max_temp_today = temp
        elif temp > self.max_temp_today or self.max_temp_today == -500:
            self.max_temp_today = temp

    def set_humidity(self, humidity):
        self.current_humidity = humidity
        if humidity < self.min_humidity or self.min_humidity == -500:
            self.min_humidity = humidity
            self.min_humidity_today = humidity
        elif humidity < self.min_humidity_today or self.min_humidity_today == -500:
            self.min_humidity_today = humidity
        elif humidity > self.max_humidity or self.max_humidity == -500:
            self.max_humidity = humidity
            self.max_humidity_today = humidity
        elif humidity > self.max_humidity_today or self.max_humidity_today == -500:
            self.max_humidity_today = humidity
