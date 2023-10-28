tuple, str, float, int, bool, list
nums1 = [10, 20, 30, 40, 50]
nums2 = [40, 50, 60, 70, 80]
print(set(nums1 + nums2))

names = {"Nur", "Beka", "Bayas", "Janar", "Nur", "Beka"}
print(names)

it = {"Google", "Meta", "Geeks", "Amazon", "Meta", "Tesla"}
print(it)
it.add("Tesla")
print(it)
it.add("Mad Devs")
print(it)
it.remove("Meta")
print(it)

cars = {10, True, "Hello", 1.1, (10, 20, 30)}
print(cars)

# Frozenset
names = frozenset({10, 10, 20, 30, 30})
print(names)
names.add("Geeks")
names.remove(10)

# Dictionary - словари
student = {'name':'Bayastan', 'age':17}
print(student)
print(student['name'])
print(student['age'])
student.setdefault('language', 'Python') #Метод для добавления ключа и значения
print(student)
student.pop("age") #Метод для удаления ключа и значения из словаря
print(student)
student['language'] = "Java" #Синтаксис для обновления значения по ключу в словарях
print(student)
student['address'] = "Amatova 1B"
print(student)

print(student.keys()) #Метод для получения ключей из словаря
print(student.values()) #Метод для получения значений из словаря
print(student.items()) #Метод для получения ключа и значений в виде кортежей

for key, value in student.items():
    print(key, value)

contact = {'Geeks': '0771121212'}
while True:
    command = input("1 - посмотреть, 2 - добавить, 3 - удалить, 4 - обновить: ")
    if command == "1":
        print(contact)
    elif command == "2":
        add_name = input("Кого добавить: ")
        add_number = input("Номер: ")
        contact.setdefault(add_name, add_number)
        print("Контакт", add_name, "успешно добавлен")