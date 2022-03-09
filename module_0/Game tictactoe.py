print("Привет! Сыграем в крестики-нолики?")
print("Чтобы сделать ход, выбери пронумерованную ячейку и введи ее номер, как только тебя попросит программа")
print("Теперь передай ход своему сопернику")
print("Программа определит, кто выйграл, удачи!")
field = list(range(1,10))

def show_field(field):
      '''Игровое поле'''
      for i in range(3):
          print("|", field[0+i*3], "|", field[1+i*3], "|", field[2+i*3], "|")
          print("-" * 14)


def player_entry(player_token):
   """Проверка введенного пользователем значения"""

   while True:
      answer = (input("Очередь хода " + player_token))
      if not (answer.isdigit()):
          print(" Введите числа! ")
          continue
      if int(answer) < 1 or int(answer) > 9:
          print("Что-то не так! Введи число от 1 до 9.")
          continue
      if (field[int(answer) - 1]) in [1,2,3,4,5,6,7,8,9]:
          field[int(answer) - 1] = player_token
          return False
      else:
            print("Клетка занята")


def check_winning(field):
   """Проверка на выйгрышную комбинацию"""
   variants_of_win = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for place in variants_of_win:
       if field[place[0]] == field[place[1]] == field[place[2]]:
           if field[place[0]] == "X":
               print("Выйграл Х")
               return True
           else:
               print("Выйграл 0")
               return True
   return False


def game_process(field):
    """Игровой процесс"""
    count = 0
    while True:
        show_field(field)
        if count % 2 == 0:
            player_entry("X")
            count += 1
        else:
            player_entry("0")
            count += 1
        if check_winning(field):
            break
        if count == 9:
            print("Ничья")
            break
    show_field(field)

game_process(field)