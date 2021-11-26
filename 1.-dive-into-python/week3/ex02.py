import csv
import os
from posixpath import split

class CarBase:
	def __init__(self, brand, photo_file_name, carrying):
		ext = {'.jpg', '.jpeg', '.png', '.gif'}
		_, file_extension = os.path.splitext(photo_file_name)
		try:
			if file_extension in ext:
				self.photo_file_name = photo_file_name
			else:
				raise ValueError
		except ValueError as err:
			print("Некорректное расширение имени файла")
			self.photo_file_name = None
		self.brand = brand
		self.carrying = float(carrying)

	def get_photo_file_ext(self):
		_, file_extension = os.path.splitext(self.photo_file_name)
		return file_extension


class Car(CarBase):
	def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
		super().__init__(brand, photo_file_name, carrying)
		self.car_type = "car"
		self.passenger_seats_count = int(passenger_seats_count)



class Truck(CarBase):
	def __init__(self, brand, photo_file_name, carrying, body_whl):
		super().__init__(brand, photo_file_name, carrying)
		self.car_type = "truck"
		sizes = body_whl.split('x')
		try:
			if len(sizes) == 3:
				self.body_length = float(sizes[0])
				self.body_width = float(sizes[1])
				self.body_height = float(sizes[2])
			else:
				raise
		except:
			self.body_length = 0.0
			self.body_width = 0.0
			self.body_height = 0.0
	
	def get_body_volume(self):
		return self.body_height * self.body_width * self.body_length


class SpecMachine(CarBase):
	def __init__(self, brand, photo_file_name, carrying, extra):
		super().__init__(brand, photo_file_name, carrying)
		self.car_type = "spec_machine"
		self.extra = extra

def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

def get_car_list(csv_filename):
	car_list = []
	with open(csv_filename) as csv_fd:
		reader = csv.reader(csv_fd, delimiter=';')
		next(reader)
		for row in reader:
			if row[1] != "":
				brand = row[1]
			else:
				continue
			if row[3] != "":
				ext = {'.jpg', '.jpeg', '.png', '.gif'}
				_, file_extension = os.path.splitext(row[3])
				if file_extension in ext:
					photo_file_name = row[3]
				else:
					continue
			else:
				continue
			if row[5] != "" and is_digit(row[5]):
				carrying = float(row[5])
			else:
				continue
			if row[0] == "car":
				if row[2] != "" and row[2].isdigit():
					passenger_seats_count = row[2]
					car = Car(brand, photo_file_name, carrying, passenger_seats_count)
					car_list.append(car)
				else:
					continue
			elif row[0] == "truck":
				body_whl = row[4]
				car = Truck(brand, photo_file_name, carrying, body_whl)
				car_list.append(car)
			elif row[0] == "spec_machine":
				if row[6] != "":
					extra = row[6]
					car = SpecMachine(brand, photo_file_name, carrying, extra)
					car_list.append(car)
				else:
					continue
	return car_list


def main():
	cars = get_car_list("cars.csv")
	print(len(cars))
	for car in cars:
		print(type(car))
	print(cars[0].passenger_seats_count)
	print(cars[1].get_body_volume())


if __name__ == "__main__":
	main()
