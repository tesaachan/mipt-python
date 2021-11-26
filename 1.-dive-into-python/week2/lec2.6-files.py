# Файлы

f = open('filename')

text_modes = ['r', 'w', 'a', 'r+']
binary_modes = ['br', 'bw', 'ba', 'br+']


# Чтение:

f = open('filename', 'w')
f.write("Some text\n")		# 10
f.close()

# Чтение и запись:

f = open('filename', 'r+')
f.read()

# Когда мы прочитали файл, указатель в конце. (tell())
# Чтобы прочитать заново исп.: seek():

f.tell()		# 10
f.seek(0)
f.tell()		# 0


f.readline()	# вернёт строку
f.readlines()	# вернет список строк, разбитых по '\n'

f.close()


# Альтернативный способ работы с файлами (контекстный менеджер):

with open('filename') as f:
	print(f.read())
