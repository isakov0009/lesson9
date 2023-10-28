#1

from datetime import datetime

def times():
    time1_str = input("1-ввод (чч:мм:сс): ")
    time2_str = input("2-ввод (чч:мм:сс): ")

    time_format = "%H:%M:%S"
    time1 = datetime.strptime(time1_str, time_format)
    time2 = datetime.strptime(time2_str, time_format)

    time_difference = (time2 - time1).total_seconds()
    print(f"Ответ: {int(time_difference)} секунд разница")
times()
# #2
def porsin():
    name = input(" Введите ваше имя: ")
    scour = [10,10,10,10,10]
    summ = sum(scour)
    summ_len = summ / len(scour)
    print(f" Среднее значение оценок:  {summ_len}")
porsin()

#3
