# Числа

# 1. Типы числел

	# integer (int) - целочисленные
	# float - вещественные числа, то есть имеющие дробную часть (числа с плавающей точкой)

# 2. Операции над числами
a = 5;
b = 10;
c = 15;
d = 20;

# Сложение
result = a + b;
print(result);

# Вычитание
result2 = a - b;
print(result2);

# Умножение
result3 = a * b;
print(result3);

# Деление
result4 = d / a;
print(result4);

# Возведение в степень
result5 = a ** b;
print(result5);

# Деление по модулю (возвращает остаток)
result6 = 10 / 3;
print(result6);

# Унарный минус (меняет знак числа)
result7 = d / a;
result7 = -result7;
print(result7);

# Округление (без библиотеки, и с библиотекой MATH)
e = 5.65;

print(round(e));

import math;

# Округление в большую сторону

print(math.floor(e));

# Округление в меньшую сторону
print(math.ceil(e));

	# Число Пи
print(math.pi);


# 3. Приведение числовых типов данных к строковым str()

result8 = 25;
result9 = 'Happy' + ' ' + str(result8) + 'rd Birthday!';
print(result9);