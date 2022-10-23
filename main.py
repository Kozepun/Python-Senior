Correct = 0
InCorrect = 0

def Question(Q = "",A1 = "", A2 = "", A3 = "", CA = 0):
    print(f"{Q}\n")
    print(f"А) {A1}")
    print(f"Б) {A2}")
    print(f"В) {A3}\n")
    CAStr = ""
    AL = ""
    Answer = input("Ответ: ")
    if(CA == 1):
        CAStr = A1
        AL = "а"
    elif(CA == 2):
        CAStr = A2
        AL = "б"
    elif (CA == 3):
        CAStr = A3
        AL = "в"
    if Answer.lower() == (CAStr.lower()) or Answer.lower() == (AL):
        print("\nПравильно\n")
        global Correct
        Correct += 1
    else:
        print("\nНе Правильно\n")
        global InCorrect
        InCorrect += 1

Question("QQQ","Q","QQ","QQQ",2)
'''
print("Кто Ты")
print("А) Собака")
print("Б) Человек ")
print("В) Еда")
Answer = input("Ответ: ")
if Answer.lower() == ("человек") or Answer.lower() == ("б"):
    print("Правильно")
    Correct += 1
else:
    print("Не Правильно")
    InCorrect += 1
print("Какая Столица Сингапура")
print("А) Сингапур")
print("Б) Киев")
print("В) Вена")
Answer = input("Ответ: ")
if Answer.lower() == ("сингапур") or Answer.lower() == ("а"):
    print("Правильно")
    Correct += 1
else:
    print("Не Правильно")
    InCorrect += 1
print("Где Находится Река Днепр")
print("А) Австрия")
print("Б) Турция")
print("В) Украина")
Answer = input("Ответ: ")
if Answer.lower() == ("украина") or Answer.lower() == ("в"):
    print("Правильно")
    Correct += 1
else:
    print("Не Правильно")
    InCorrect += 1
print("Где Купить Слона")
print("А) OLX")
print("Б) AlieExpress")
print("В) Amazon")
Answer = input("Ответ: ")
if Answer.lower() == ("olx") or Answer.lower() == ("а"):
    print("Правильно")
    Correct += 1
else:
    print("Не Правильно")
    InCorrect += 1

print(f"\nПравильно: {Correct}\n")
print(f"Не Правильно: {InCorrect}")
'''
