# #1
# dictionary_1 = {'a': 300, 'b':400} 
# dictionary_2 = {'c':500,'d':600}
# dictionary_1.update(dictionary_2)
# print(dictionary_1)

# #2
# numbers = {'num_1' : 1, 'num_2':2, 'num_3':3, 'num_100':100}
# num = numbers['num_1']*5, numbers['num_2']*5, numbers['num_3']*5, numbers['num_100']*5
# print(num)

# #3 
# student = {'name': 'Askhat', 'age': 17}
# res = student['age'] * 2
# print(res)

# #4
# student = {'name':'Askhat','age':17,'color':'White'}
# res = student['age'] = 16
# print(res)

# #5
# student = {'name':'Askhat','age':17}
# student.pop("age")
# print(student)

# #6
# student = {'nams':'Askhat'}
# student['address'] = "Amatofa 1B"
# print(student)

7
# while True:
#     password = input("Введите пароль: ")
#     confirm_password = input("Введите пароль повторно: ")
#     if len(password) < 8:
#         print("Короткий пароль")
#     elif "123" in password:
#         print("Простой пароль")
#     elif password != confirm_password:
#         print("Различаются")
#     else:
#         print("OK")
#         print("Пароль создан")
#         break