'''Задача №4, код принимает на вход число temp, а затем возвращает номер категории'''
a = int(input('temp: '))
if (a <= -20):
    print('Холодно')
elif a >= -19 and a <= 0:
    print('Прохладно')
elif a >= +1 and a <= +15:
    print('Зябко')
elif a >= +16 and a <= +25:
    print('Тепло')
elif a >= +26:
    print('Жарко')
else:
    print(' ')