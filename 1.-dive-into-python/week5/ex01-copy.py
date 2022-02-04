import time
import socket
import re


"""
Клиент клиент-серверного приложения по отправке структурированных данных (метрик) и их прёму.
Перед тем как начать реализовывать систему, нужно определить структуру запросов по которым 
будет проходить взаимодействие клиента и сервера:

Клиент поддерживает два вида запросов:
- отправка данных для сохранения на сервер
- получение сохраненных данных

Определим формат запроса клиента:
<команда> <данные><\n>

Определим формат ответа сервера:
<статус ответа><\n><данные><\n\n>

Под тегом <команда> определим 2 варианта: put - загрузить данные, get - получить данные.
Под тегом <статус ответа> определим 2 варианта: ok - команда выполнена, error - ошибка.
Тег <\n> - единичный перенос строки.

Определим тег <данные>:
Для каждой метрики <key> мы будем хранить данные о ее значении <value> и времени, когда производилось измерение <timestamp> (ключ-значение). 
Необходимо различать данные полученные от разных серверов, то есть будем сохранять название конкретного сервера. 
Поэтому метрику <key> мы будем определять по правилу:
<название сервера>.<название данных>

Пример:
key           | value | timestamp  
-----------------------------------

"palm.cpu"    |  2.0  | 1150864247

"palm.cpu"    |  0.5  | 1150864248

"eardrum.cpu" |  3.0  | 1150864250


Пример строки, которая придет на запрос "get palm.cpu\n":
	ok\npalm.cpu 2.0 1150864247\npalm.cpu 0.5 1150864248\n\n

Пример строки, которая придет в ответ на удачный запрос put сохранения данных:
	ok\n\n

Пример строки, которая придет в ответ на запрос невалидных данных:
	error\nwrong command\n\n
"""

"""
Реализация клиента:
"""


"""
Ошибка, выводимая в случае парсинга невалидных данных:
"""
class ClientError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value


"""
Парсинг получаемых данных методом get в абстрактную структуру данных словарь (dict):
"""
def respose_proc(data):
    result1 = re.match(r'^b\'ok\\n\w+.\w+ \d+', str(data))
    result2 = re.match(r'^b\'ok\\n\\n', str(data))
    if not result1 and not result2:
        raise ClientError("ClientError")
        # одноразовый словарь
    data=str(data).split('\\n')

    data.pop(0)
    dict={}
    for i in range(len(data)):
        if data[i]!='' and data[i]!="'":
            metrics=data[i].split(" ")
            try:
                metrics[1]=float(metrics[1])
                metrics[2]=int(metrics[2])
                if metrics[0] not in dict:
                    dict[metrics[0]]=list()
                    dict[metrics[0]].append((metrics[2], metrics[1]))
                else:
                    dict[metrics[0]].append((metrics[2], metrics[1]))
            except:
                raise ClientError("ClientError")

    for value in dict:
        dict[value].sort()
    return dict

"""
Класс Client инкапсулирует соединение с сервером, клиентский сокет и методы для получения (get) и отправки (put) метрик на сервер.
Имеет 2 метода get и put.

Объект класса получает хост и порт сервера, после чего по средствам модуля socket подключается к серверу, 
отправляет запросы и получает ответы:
"""
class Client():
    def __init__(self, host, port, timeout=None):
        self.host=host
        self.port=port
        self.timeout=timeout
        self.timestamp=int(time.time())

    def put(self, metric_name, metric_value, timestamp=False):
        if not timestamp:
            timestamp=self.timestamp
        sock = socket.create_connection((self.host, self.port))
        sock.sendall(str.encode("put {0} {1} {2}\n".format(metric_name, metric_value, timestamp)))

        data = sock.recv(1024)
        respose_proc(data)

        sock.close()

    def get(self, metric_value):
        sock = socket.create_connection((self.host, self.port))
        sock.sendall(str.encode("get {}\n".format(metric_value)))

        data = sock.recv(1024)
        dict=respose_proc(data)

        sock.close()
        return dict

"""
Пример работы клиента:

client = Client("127.0.0.1", 8888, timeout=15)
client.put("palm.cpu", 25.7, timestamp=1150864247)
client.put("palm.cpu", 24.3, timestamp=1150864247)
client.put("123.cpu", 0.3)
client.put("palm.123", 0.3, timestamp=1150864247)

Примечание:
Продемонстрировать работу клиента в данный момент не получится, поскольку у нас не готов сервер,
который необходим для функционирования системы.
"""