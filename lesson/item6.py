# Команды if
	# Результатом выполнения условия if является либо True, либо False
	# Если нужно выполнять проверку с учётом регистра нужно приводить данные к одному типу

	# Синтаксис команд

		# if условие:
			# действие

		# if условие:
			# действие
		# else:
			# действие

		# if условие:
			# действие
		# elif условие:
			# действие
		# else:
			# действие



	# Простой пример
cars = ['bmw', 'nissan', 'audi', 'subaru']
for cars_item in cars:
	if cars_item == 'bmw':
		print(cars_item.upper())
	else:
		print(cars_item.title())

	# Проверка равенства
car = 'Audi';
if car == 'bmw':
	print('верно')
else:
	print('не верно')

	# Проверка неравенства
car = 'Audi';
if car != 'bmw':
	print('верно')

	# Проверка нескольких условий (AND)
car = 'Audi'
if (car != 'subaru') and (car != 'bmw'):
	print('верно')

	# Проверка нескольких условий (OR)
car = 'Audi'
if (car != 'subaru') or (car != 'bmw'):
	print('верно')

	# Проверка вхождения значений в список
cars_list = ['bmw', 'nissan', 'audi', 'subaru']
if 'bmw' in cars_list:
	print('True, bmw входит в список')

	# Проверка отсутствия значний в списке
cars_list = ['bmw', 'nissan', 'audi', 'subaru']
car = 'mitsubishi'
if car not in cars_list:
	print('True, mitsubishi не в этом списке')