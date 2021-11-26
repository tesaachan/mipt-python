# Модули

import mypackage.utils
from mypackage.utils import multiply # одно и то же с верхней строкой
# from mypackage.utils import * - неявный вариант (не рекоменд.)

if __name__ == "__main__":
	print(mypackage.utils.multiply(2, 3))

