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
	

# 4. Генераторы чисел

	# Первый вариант генерации
squares = [];
for value in range(1, 11):
	square = value**2;
	squares.append(square);
print(squares);

	# Второй вариант генерации
squares = [value**2 for value in range(1, 11)];
print(squares);

# 5. Работа с частью списка (работа с конкретным подмножеством элементов списка)

	# 5.1 Создание среза
		# Чтобы создать срез нужно указать индексы первого и последнего элементов, с которыми нужно работать
players = ['mike', 'nina', 'ivan', 'vladimir', 'maxim', 'alex'];
print(players[0:3]); # будет выведено от начала списка['mike', 'nina', 'ivan']
print(players[:4]);  # будет выведено от начала списка ['mike', 'nina', 'ivan', 'vladimir']
print(players[2:]);  # все элементы со 2 и до конца  ['ivan', 'vladimir', 'maxim', 'alex']
print(players[-3:]);  # срез от конца списка  ['vladimir', 'maxim', 'alex']

	# 5.2 перебор содержимого среза (при помощи циклов)
players_list = ['mike', 'nina', 'ivan', 'vladimir', 'maxim', 'alex'];
for name_players in players_list[:3]:
	print(name_players.title());

	# 5.3 Копирование списка
my_foods = ['falafel', 'pizza', 'cake'];
friends_foods = my_foods[:] # создаём копию списка, при помощи среза [:], то есть от начала и до конца

print('My foods:');
my_foods.append('ice cream'); # Добавляем в свой список новый элемент
print(my_foods);

print('Friends food:');
print(friends_foods);

	# 5.2 Кортежи
		# В Python значнеия, которые не могут изменяться называются  - неизменимыми, а неизменяемый список называется - кортежем

		# Кортеж выгляжит как список, но заключается в круглые скобки (), а не как список в []

dimensions = (200, 50); # Создаём кортеж, а затем выводим из него элементы
print(dimensions[0]);
print(dimensions[1]);

	# 5.2.1 Перебор всех значений в кортеже

dimensions_list = (200, 50, 100, 300, 500); # значения в кортеже
for dimensions_item in dimensions_list:
	print(dimensions_item);

	# 5.2.2 Замена кортежа
		# Элементы кортежа нельзя изменить, но можно их заменить

dimensions_old_list = (200, 100, 50);

print('Старый кортеж');
for dimensions_old_item in dimensions_old_list:
		print(dimensions_old_item);

dimensions_old_list = (100, 100, 10);
print('Новый кортеж');
for dimensions_new_item in dimensions_old_list:
		print(dimensions_new_item);