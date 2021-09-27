from Cats import Cat
Baron = Cat ("Барон", "мальчие", 2)
Sam = Cat ("Сэм", "мальчик", 2)
#print (f'Имя питомца: {Baron.getName()}, Пол питомца: {Baron.getGender()}, Возраст пимца:{Baron.getAge()}')
#print (f'Имя питомца: {Sam.getName()}, Пол питомца: {Sam.getGender()}, Возраст пимца:{Sam.getAge()}')
print (Baron.pet_info())
print (Sam.pet_info())