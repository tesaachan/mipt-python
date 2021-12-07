"""
Часто при зачислении каких-то средств на счет с нас берут комиссию.
Давайте реализуем похожий механизм с помощью дескрипторов.
Напишите дескриптор Value, который будет использоваться в нашем классе Account.
"""


class Value:
	def __init__(self):
		self.value = 0

	def __get__(self, obj, obj_type):
		return self.value

	def __set__(self, obj, value):
		self.value = (1 - obj.commission) * value


class Account:
    amount = Value()
    
    def __init__(self, commission):
        self.commission = commission

	
if __name__ == "__main__":
	new_account = Account(0.1)
	new_account.amount = 100
	print(new_account.amount)
