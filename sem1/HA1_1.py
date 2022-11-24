#1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример:*
# - 6 -> да
# - 7 -> да
# - 1 -> не

dayOfWeek = int(input('d = '))
if dayOfWeek in range (1,6):
  print("no, it isn't")
elif dayOfWeek ==6 or dayOfWeek ==7:
    print('yes, it is')
else:
    print('please, try again!')