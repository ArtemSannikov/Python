# Работа со списками

# 1. Перебор всего списка

magicians_list = ['alice', 'david', 'luke', 'carolina', 'nina', 'ivan', 'stella'];

for magician_name in magicians_list: # берем каждое имя из списка - magicians_list, а затем присваиваем его переменной - magician_name
	print(magician_name)

# 2. Более сложные действия в циклах for

cars_list = ['Honda', 'Mitsubishi', 'Renault', 'Opel'];

for car in cars_list:
	print('Пользователь ездит на: ' + car.title());

# 3. Создание числовых списков

	# 3.1 Функция range() - выводит числовую последовательность От и До
for value in range(0, 10):
	print(value);


	# 3.2 Использование range() для создания числового списка
numbers_example = list(range(0, 10)); # создаём список типа [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers_example);

numbers_example2 = list(range(0, 60, 2)); # создаём список типа От и До, с пропуском нескольких чисел (ОТ, До, Сколько чисел надо пропускать)
print(numbers_example2);

	# Максимум, минимум и сумма числового списка
numbers_example3 = list(range(0,10));
print(numbers_example3);
print(min(numbers_example3));
print(max(numbers_example3));
print(sum(numbers_example3));
	