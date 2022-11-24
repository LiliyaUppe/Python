# 2'. Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ⋁ - "Или"
# ⋀ - "И"
# ¬ - "Не"

#запрос данных
x = int(input('Введите x: '))
y = int(input('Введите y: '))
z = int(input('Введите z: '))

#проверка истинности
def true_or_false(x, y, z):
    left = not (x or y or z)
    right = not x and not y and not z
    result = left == right
    return result

#печать результата
if true_or_false(x, y, z) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")

