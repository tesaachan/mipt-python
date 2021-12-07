import tempfile
import random
import os

class File:
	def __init__(self, filename):
		self.filename = filename
		path = os.path.dirname(os.path.abspath(filename))
		name = os.path.basename(filename)
		filepath = os.path.join(path, name)
		if not os.path.exists(path):
			os.makedirs(path)
		f = open(filepath, "a")
		f.close()
		with open(filepath, "r") as f:
			self.lines = f.readlines()

	def __str__(self):
		return os.path.abspath(self.filename)

	def __add__(self, obj):
		with open(self.filename, "r") as f:
			sum = f.readline()
		with open(obj.filename, "r") as f:
			sum += f.readline()
		temp = random.randint(1000000, 2000000)
		filepath = os.path.join(tempfile.gettempdir(), str(temp))
		new_file = File(filepath)
		new_file.write(sum)
		return new_file

	def read(self):
		with open(self.filename, "r") as f:
			result = ""
			for l in self.lines:
				result += l
			return result

	def write(self, text):
		sum = 0
		for c in text:
			sum += 1
		with open(self.filename, "w") as f:
			f.writelines(text)
		with open(self.filename, "r") as f:
			self.lines = f.readlines()
		return sum

	def __getitem__(self, index):
		return self.lines[index]
	
	
def main():
	path_to_file = 'ad/a/some_filename'
	print(os.path.exists(path_to_file))
	file_obj = File(path_to_file)
	print(os.path.exists(path_to_file))
	print(file_obj)
	print(file_obj.read())
	print(file_obj.write('some text'))
	print(file_obj.read())
	print(file_obj.write('\ned872df1fd3f4eb096b5beed8f9d31d6 be4f58841dac48ba91062f9ae6da1387\n\n\n887073e6d24746518445c8f6a7f75994\nca91540bca634fa19358ecc53a3cff71\n'))
	print(ascii(file_obj.read()))

	file_obj_1 = File(path_to_file + '_1')
	file_obj_2 = File(path_to_file + '_2')
	print(file_obj_1.write('line 1\n'))
	print(file_obj_2.write('line 2\n'))
	new_file_obj = file_obj_1 + file_obj_2
	print(isinstance(new_file_obj, File))
	print(new_file_obj)
	for line in new_file_obj:
		print(ascii(line))  
	new_path_to_file = str(new_file_obj)
	print(os.path.exists(new_path_to_file))
	file_obj_3 = File(new_path_to_file)
	print(file_obj_3)


if __name__ == "__main__":
	main()