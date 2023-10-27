import json
import csv
import os

def save_game(inventory):
    with open('save.json', 'w') as f:
        json.dump(list(inventory), f)

def load_game():
    if os.path.exists('save.json'):
        with open('save.json', 'r') as f:
            return set(json.load(f))
    return set()

def delete_save():
    if os.path.exists('save.json'):
        os.remove('save.json')

def save_to_csv(username, inventory):
    with open('game_data.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([username] + list(inventory))

def kz(d):
    print(d)

def ng(b):
    print(b + " в игру 'Тайна заброшенного особняка'!" )

def th(c):
    print(c)
    return c

def nv(a):
    print("Неверный ввод. " + a)

ng("Добро пожаловать")
start_game = input(f"Хотите ли вы начать игру? {th('Если да, нажмите 1, если хотите выйти, нажмите 0:')} ")

while start_game not in ["1", "0"]:
    nv("Пожалуйста, попробуйте снова.")
    start_game = input(f"Хотите ли вы начать игру? {th('Если да, нажмите 1, если хотите выйти, нажмите 0:')} ")

if start_game == "1":
    username = input("Введите ваше имя: ")
    inventory = load_game()

if start_game == "1":
    door = input("Вы вошли в заброшенный особняк и видите две двери:\n1. Дверь в подвал\n2. Дверь на чердак\nВыберите дверь (1 или 2): ")

    while door not in ["1", "2"]:
        nv("Пожалуйста, попробуйте снова.")
        door = input("Выберите дверь (1 или 2): ")

    action_choice = input("Вы хотите взять фотографию с собой? Да или Нет: ").lower()

    while action_choice not in ["да", "нет"]:
        nv("Пожалуйста, попробуйте снова.")
        action_choice = input("Вы хотите взять фотографию с собой? Да или Нет: ").lower()

    if action_choice == "да":
        if door == "1":
            inventory.add("старая фотография")
            print("Вы взяли фотографию с собой")
            print("Вы обнаружили тайну дверь в подвале")
            secret_choice = input("Вы хотите взять книгу с собой? Да или Нет: ").lower()

            while secret_choice not in ["да", "нет"]:
                nv("Пожалуйста, попробуйте снова.")
                secret_choice = input("Вы хотите взять книгу с собой? Да или Нет: ").lower()

            if secret_choice == "да":
                inventory.add("древняя книга")
                print("Вы взяли книгу с собой")
                print("Вы обнаружили потайную комнату")
                secret_choice = input("Вы хотите взять золотую статуэтку? Да или Нет: ").lower()

                while secret_choice not in ["да", "нет"]:
                    nv("Пожалуйста, попробуйте снова.")
                    secret_choice = input("Вы хотите взять золотую статуэтку? Да или Нет: ").lower()

                if secret_choice == "да":
                    inventory.add("золотая статуэтка")
                    print("Вы взяли золотую статуэтку с собой")
                else:
                    inventory.add("древний меч")
                    print("Вы взяли древний меч с собой")
            else:
                print("Вы решили не брать книгу")
        else:
            inventory.add("старинная кукла")
            print("Вы взяли куклу с собой")
            print("Вы обнаружили секретный проход в подземелье")
            secret_choice = input("Хотите войти? Да или Нет: ").lower()

            while secret_choice not in ["да", "нет"]:
                nv("Пожалуйста, попробуйте снова.")
                secret_choice = input("Хотите войти? Да или Нет: ").lower()

            if secret_choice == "да":
                inventory.add("секретный артефакт")
                print("Вы нашли секретный артефакт и добавили его в инвентарь")
            else:
                underground_choice = input("Вы попали в подземный лабиринт.\n1. Пойти налево\n2. Пойти направо\nВыберите направление (1 или 2): ")

                while underground_choice not in ["1", "2"]:
                    nv("Пожалуйста, попробуйте снова.")
                    underground_choice = input("Выберите направление (1 или 2): ")

                if underground_choice == "1":
                    left_choice = input("Вы пошли налево и обнаружили сокровища.\nХотите взять сокровища с собой? Да или Нет: ").lower()

                    while left_choice not in ["да", "нет"]:
                        nv("Пожалуйста, попробуйте снова.")
                        left_choice = input("Хотите взять сокровища с собой? Да или Нет: ").lower()

                    if left_choice == "да":
                        inventory.add("сокровища")
                        print("Вы взяли сокровища с собой")
                else:
                    right_choice = input("Вы пошли направо и обнаружили древний меч.\nХотите взять меч с собой? Да или Нет: ").lower()

                    while right_choice not in ["да", "нет"]:
                        nv("Пожалуйста, попробуйте снова.")
                        right_choice = input("Хотите взять меч с собой? Да или Нет: ").lower()

                    if right_choice == "да":
                        inventory.add("древний меч")
                        print("Вы взяли древний меч с собой")
                    else:
                        print("Вы решили не брать меч")
                        additional_choice = input("Вы обнаружили дополнительный путь.\n1. Пойти по пути\n2. Остаться на месте\nВыберите действие (1 или 2): ")

                        while additional_choice not in ["1", "2"]:
                            nv("Пожалуйста, попробуйте снова.")
                            additional_choice = input("Выберите действие (1 или 2): ")

                        if additional_choice == "1":
                            river_choice = input("Вы нашли подземную реку.\n1. Попытаться переплыть\n2. Остаться на месте\nВыберите действие (1 или 2): ")

                            while river_choice not in ["1", "2"]:
                                nv("Пожалуйста, попробуйте снова.")
                                river_choice = input("Выберите действие (1 или 2): ")

                            if river_choice == "1":
                                swim_choice = input("Вы решили переплыть реку.\n1. Плыть вперед\n2. Повернуть назад\nВыберите действие (1 или 2): ")

                                while swim_choice not in ["1", "2"]:
                                    nv("Пожалуйста, попробуйте снова.")
                                    swim_choice = input("Выберите действие (1 или 2): ")

                                if swim_choice == "1":
                                    cave_choice = input("Вы обнаружили пещеру с тайным оружием.\nХотите взять оружие с собой? Да или Нет: ").lower()

                                    while cave_choice not in ["да", "нет"]:
                                        nv("Пожалуйста, попробуйте снова.")
                                        cave_choice = input("Хотите взять оружие с собой? Да или Нет: ").lower()

                                    if cave_choice == "да":
                                        inventory.add("тайное оружие")
                                        print("Вы взяли тайное оружие с собой")
                                else:
                                    print("Вы вернулись обратно")
                            else:
                                print("Вы решили остаться на месте")
    else:
        print("Вы решили оставить предмет на месте")

    if "сокровища" in inventory:
        treasure_choice = input("Вы нашли комнату с сокровищами.\n1. Взять сокровища\n2. Оставить их\nВыберите действие (1 или 2): ")

        while treasure_choice not in ["1", "2"]:
            nv("Пожалуйста, попробуйте снова.")
            treasure_choice = input("Выберите действие (1 или 2): ")

        if treasure_choice == "1":
            inventory.add("сокровища")
            print("Вы взяли сокровища с собой")
    elif "амулет" in inventory:
        tomb_choice = input("Вы нашли древнюю гробницу.\n1. Исследовать гробницу\n2. Оставить ее\nВыберите действие (1 или 2): ")

        while tomb_choice not in ["1", "2"]:
            nv("Пожалуйста, попробуйте снова.")
            tomb_choice = input("Выберите действие (1 или 2): ")

    print("Вы вышли из подземелья и обнаружили заброшенный сад")
    garden_choice = input("Вы нашли заброшенный сад.\n1. Исследовать цветы\n2. Исследовать кусты\nВыберите действие (1 или 2): ")

    while garden_choice not in ["1", "2"]:
        nv("Пожалуйста, попробуйте снова.")
        garden_choice = input("Выберите действие (1 или 2): ")

    alchemist_choice = input("Вы обнаружили лабораторию алхимика.\n1. Исследовать рецепты\n2. Искать ингредиенты\nВыберите действие (1 или 2): ")

    while alchemist_choice not in ["1", "2"]:
        nv("Пожалуйста, попробуйте снова.")
        alchemist_choice = input("Выберите действие (1 или 2): ")

    if alchemist_choice == "1":
        explore_choice = input("Вы хотите изучить рецепты зелий? Да или Нет: ").lower()

        while explore_choice not in ["да", "нет"]:
            nv("Пожалуйста, попробуйте снова.")
            explore_choice = input("Вы хотите изучить рецепты зелий? Да или Нет: ").lower()

        if explore_choice == "да":
            print("Вы нашли рецепт зелья силы")
            potion_choice = input("Вы создали зелье силы. Хотите взять зелье с собой? Да или Нет: ").lower()

            while potion_choice not in ["да", "нет"]:
                nv("Пожалуйста, попробуйте снова.")
                potion_choice = input("Вы создали зелье силы. Хотите взять зелье с собой? Да или Нет: ").lower()

            if potion_choice == "да":
                inventory.add("зелье силы")
                print("Зелье силы добавлено в инвентарь.")
    else:
        print("Вы решили искать ингредиенты для зелий.")
        print("Вы нашли необходимые ингредиенты.")

    mystical_choice = input("Вы попали в таинственный лес.\n1. Пойти налево\n2. Пойти направо\nВыберите направление (1 или 2): ")

    while mystical_choice not in ["1", "2"]:
        nv("Пожалуйста, попробуйте снова.")
        mystical_choice = input("Выберите направление (1 или 2): ")

    if mystical_choice == "1":
        temple_choice = input("Вы пошли налево и обнаружили заброшенный храм.\nХотите войти в храм? Да или Нет: ").lower()

        while temple_choice not in ["да", "нет"]:
            nv("Пожалуйста, попробуйте снова.")
            temple_choice = input("Хотите войти в храм? Да или Нет: ").lower()

        if temple_choice == "да":
            talisman_choice = input("Вы вошли в заброшенный храм и обнаружили древний талисман.\nХотите взять талисман с собой? Да или Нет: ").lower()

            while talisman_choice not in ["да", "нет"]:
                nv("Пожалуйста, попробуйте снова.")
                talisman_choice = input("Хотите взять талисман с собой? Да или Нет: ").lower()

            if talisman_choice == "да":
                inventory.add("древний талисман")
                print("Вы взяли древний талисман с собой")
    else:
        well_choice = input("Вы пошли направо и обнаружили колодец.\nХотите проверить колодец? Да или Нет: ").lower()

        while well_choice not in ["да", "нет"]:
            nv("Пожалуйста, попробуйте снова.")
            well_choice = input("Хотите проверить колодец? Да или Нет: ").lower()

        if well_choice == "да":
            pearl_choice = input("Вы подошли к колодцу и увидели светящуюся жемчужину.\nХотите взять жемчужину? Да или Нет: ").lower()

            while pearl_choice not in ["да", "нет"]:
                nv("Пожалуйста, попробуйте снова.")
                pearl_choice = input("Хотите взять жемчужину? Да или Нет: ").lower()

            if pearl_choice == "да":
                inventory.add("светящаяся жемчужина")
                print("Вы взяли светящуюся жемчужину с собой")
    
    kz("Конец игры")
    print("Ваши предметы:")
    for item in inventory:
        print(item)

    save_to_csv(username, inventory)
    delete_save()
else:
    save_game(inventory)
