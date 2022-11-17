# Основная функция бота
import bs4 as bs4
import requests,sys,os,data
status = 1

command_1 = f"Ваш уровень доступа: Администратор\nДоступные команды:\n!версия - информация о версии бота\n!команды - список всех доступных команд бота\n!доступ - откроет/закроет доступ к возможностям бота для пользователей правами ниже Тестера\n!тест2 - вывод количества пользователей в БД\n!стоп - остановка бота(только локальная машина!)\n!рестарт - перезагрузка скрипта бота\n!инфо - информация о себе\n!узнать [id] - выдаст информацию о пользователе с введённым id\n!сменаправ [id] [permission] - сменить уровень прав пользователя с id на право permisson\n* * *\nТестовые команды:\n!заметка [num] - вывести содержание заметки с индексом num\n!добавить [text] - новую заметку с содержанием введённого текста\n!удалить [num] - удалить заметку с номером num"
command_2 = f"Ваш уровень доступа: Технический модератор\nДоступные команды:\n!версия - информация о версии бота\n!команды - список всех доступных команд бота\n!доступ - откроет/закроет доступ к возможностям бота для пользователей правами ниже Тестера\n!тест2 - вывод количества пользователей в БД\n!стоп - остановка бота(только локальная машина!)\n!рестарт - перезагрузка скрипта бота\n!инфо - информация о себе\n!узнать [id] - выдаст информацию о пользователе с введённым id\n!сменаправ [id] [permission] - сменить уровень прав пользователя с введённым id на право permisson\n* * *\nТестовые команды:\n!заметка [num] - вывести содержание заметки с индексом num\n!добавить [text] - новую заметку с содержанием введённого текста\n!удалить [num] - удалить заметку с номером num"
command_3 = f"Ваш уровень доступа: Редактор\nДоступные команды:\n!версия - информация о версии бота\n!команды - список доступных команд бота\n!инфо - информация о себе\n!узнать [id] - выдаст информацию о пользователе с введённым id\n*список команд дополняется"
command_4 = f"Ваш уровень доступа: Стандартный\nДоступные команды:\n!версия - информация о версии бота\n!команды - список доступных команд бота\n!инфо - информация о себе\n!узнать [id] - выдаст информацию о пользователе с введённым id\n*список команд дополняется"
my_array = []

class VkBot:

    def __init__(self, user_id):
        print("Команда обработана")
        print("-------------------")

        self._USER_ID = user_id
        self._USERNAME = self._get_user_name_from_vk_id(user_id)
        self._USERLASTNAME = self._get_user_lastname_from_vk_id(user_id)

        self._COMMANDS = ["!ВЕРСИЯ", "!КОМАНДЫ", "НАЧАТЬ", "!ДОСТУП", "!ТЕСТ2", "!СТОП", "!ИНФО", "!РЕСТАРТ", "ПРИВЕТ", "ПРИВ", "КУ", "!узнать", "!сменаправ", "!ДАТА", "!МОДЕР", "ЗАМЕТКА", "ЗДОБАВИТЬ", "ЗУДАЛИТЬ", "ЗАМЕТКИ КОЛИЧЕСТВО"]
    def _get_user_name_from_vk_id(self, user_id):
        request = requests.get("https://vk.com/id"+str(user_id))
        bs = bs4.BeautifulSoup(request.text, "html.parser")
        user_name = self._clean_all_tag_from_str(bs.findAll("title")[0])
        return user_name.split()[0]

    def _get_user_lastname_from_vk_id(self, user_id):
        request = requests.get("https://vk.com/id"+str(user_id))
        bs = bs4.BeautifulSoup(request.text, "html.parser")
        user_name = self._clean_all_tag_from_str(bs.findAll("title")[0])
        return user_name.split()[1]

    def new_message(self, message):
        for i in message:
            if i in ('''@=™''' or i not in '''abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя1234567890 ''') and i not in '''abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя1234567890!.- ''':
                return f"Вы ввели запрещенный символ!"
        global status
        dostup = 0
        id = self._USER_ID
        name = self._USERNAME + " " + self._USERLASTNAME
        if (data.find_people(id) == 0):
            data.g_write(id, 4, name, 0)
            dostup = 4
        else:
            dostup = int(data.get_permission(id))

        # название прав
        if (dostup == 1):
            pravo = "Администратор"
        elif (dostup == 2):
            pravo = "Технический модератор"
        elif (dostup == 3):
            pravo = "Редактор"
        elif (dostup == 4):
            pravo = "Стандартный"
        
        # проверка доступа
        if (status == 0 and (dostup != 1 and dostup != 2)):
            return f"Технические работы.\nДоступ к боту закрыт.\nВ данный момент команды недоступны. [Error code: #0000]"

        # доступ к командам начинающимся на !
        if((message[0] == "!" and (message.upper() != self._COMMANDS[0] and message.upper() != self._COMMANDS[1] and message.upper() != self._COMMANDS[6])) and (dostup != 1 and dostup != 2)):
            return f"В данный момент данная команда не работает или её не существует."

        # !версия
        if message.upper() == self._COMMANDS[0]:
            if(dostup == 1 or dostup == 2):
                return f"Версия бота: 0.1.5 beta"
            else:
                return f"Версия бота: 0.1 stable"

        # !команды
        if message.upper() == self._COMMANDS[1]:
            if (dostup == 1):
                return command_1
            elif (dostup == 2):
                return command_2
            elif (dostup == 3):
                return command_3
            elif (dostup == 4):
                return command_4

        # начать
        elif message.upper() == self._COMMANDS[2]:
            if (dostup == 1):
                return f"Приветствую, администратор!\n{command_1}"
            elif (dostup == 2):
                return f"Приветствую, технический модератор!\n{command_2}"
            elif (dostup == 3):
                return f"Приветствую, редактор!\n{command_3}"
            elif (dostup == 4):
                return f"Приветствую, {self._USERNAME}!\n{command_4}"


        # !доступ
        elif (message.upper() == self._COMMANDS[3] and (dostup == 1 or dostup == 2)):
            if (status == 1):
                status = 0
                return f"Доступ закрыт."
            else:
                status = 1
                return f"Доступ открыт."

        # !узнать
        elif (message[:7] == self._COMMANDS[11]):
            if(len(message) != 17):
                return f"Команда введена неверно. [Error code: #0A1A]"
            for i in message[8:17]:
                if i not in '''1234567890''':
                    return f"Команда введена неверно. [Error code: #0A1B]"
            new_id = int(message[8:17])
            personal_data = data.get_info(new_id)
            if(not (personal_data != 0)):
                return f"Пользователь не найден."
            dostup = int(personal_data[1])
            if (dostup == 1):
                pravo = "Администратор"
            elif (dostup == 2):
                pravo = "Технический модератор"
            elif (dostup == 3):
                pravo = "Редактор"
            elif (dostup == 4):
                pravo = "Стандартный"
            return f"Информация о [id{new_id}|пользователе]:\nИмя пользователя: {personal_data[2]}\nID пользователя: {personal_data[0]}\nУровень доступа: {pravo}"

        # !тест2
        elif(message.upper() == self._COMMANDS[4] and (dostup == 1 or dostup == 2)):
            return data.len_base() - 1
        
        # !стоп
        elif (message.upper() == self._COMMANDS[5] and (dostup == 1 or dostup == 2)):
            return sys.exit("Бот остановлен")

        # !рестарт
        elif (message.upper() == self._COMMANDS[7] and (dostup == 1 or dostup == 2)):
                os.execl(sys.executable, sys.executable, *sys.argv)

         # !инфо
        elif message.upper() == self._COMMANDS[6]:
                return f"Информация о [id{self._USER_ID}|себе]:\nВаше Имя - {self._USERNAME}\nВаша Фамилия - {self._USERLASTNAME}\nВаш ID - {self._USER_ID}\nУровень доступа - {pravo}"
        
        # привет, прив, ку
        elif (message.upper() == self._COMMANDS[8] or message.upper() == self._COMMANDS[9] or message.upper() == self._COMMANDS[10]):
            return f"Привет-привет!"
        
        # !сменаправ
        elif(message[:10] == self._COMMANDS[12] and (dostup == 1 or dostup == 2)):
            if(len(message) != 22):
                return f"Команда введена неверно. [Error code: #0A1A]"
            for i in message[11:20]:
                if i not in '''1234567890''':
                    return f"Команда введена неверно. [Error code: #0A1B]"
                if message[21] not in '''1234''':
                    return f"Команда введена неверно. [Error code: #0A1B]"
            id_info = int(message[11:20])
            permisson = int(message[21])
            if(permisson == 1 and dostup != 1):
                return f"Вы не можете присвоить данный уровень прав пользователю."
            elif(len(message) != 22):
                return f"Вы ввели неверный ID или уровень доступа пользователя."
            elif(id_info == 224856116 and self._USER_ID != 224856116):
                return f"Вы не можете изменить права данному пользователю."
            elif(id_info == self._USER_ID and self._USER_ID != 224856116):
                return f"Вы не можете изменить самому себе права.\nДля смены себе прав обратитесь к технической модерации.\nДля этого введите команду !модер"
            data.g_write(id_info,permisson," ",1)
            return f"Команда выполнена."
        
        # !дата
        elif (message.upper() == self._COMMANDS[13] and (dostup == 1 or dostup == 2)):
            text = "База данных:\n* * *\n"
            count_1 = data.len_base()
            if (count_1 < 150):
                list = data.get_data()
                for i in range(1,count_1):
                    for j in range(3):
                        text += list[i][j] + " "
                    text += "\n"
                text += "* * *"
                return text
            else:
                return f"База данных находится по адресу: https://docs.google.com/spreadsheets/d/1TfR990VJgs3pzePYsIQZ6ZPg1BGn0CgIY3J3lK1Ntlg"
        
        # заметка
        elif(message[:7].upper() == self._COMMANDS[15] and (dostup != 0)):
            for i in message[8:]:
                if i not in '''1234567890''':
                    return f"Команда введена неверно. [Error code: #0A1B]"
            number = int(message[8:])
            return data.get_note(self._USER_ID,number)

        # здобавить
        elif(message[:9].upper() == self._COMMANDS[16] and (dostup != 0)):
            text = message[10:]
            if(text == ""):
                return f"Вы не указали текст заметки."
            number = data.add_note(self._USER_ID, text)
            return f"Заметка добавлена. Её номер {number}"

        # зудалить
        elif(message[:8].upper() == self._COMMANDS[17] and (dostup != 0)):
            for i in message[9:]:
                if i not in '''1234567890''':
                    return f"Команда введена неверно. [Error code: #0A1B]"
            number = int(message[9:])
            return data.delete_note(self._USER_ID, number)

        # заметки количество
        elif(message.upper() == self._COMMANDS[18] and (dostup != 0)):
            true = data.count_note(self._USER_ID)
            if(true == 1):
                return f"Заметок нет."
            note = true[0]
            value = ""
            for i in range(len(note)):
                value += note[i] + "\n"
            return f"Список заметок:\n{value}\nВсего заметок {true[1]}"
        elif (message.upper() == "ЗАМЕТКИ ДОБАВИТЬ"):
                return f"Техническая справка по добавлению заметок:\nЧтобы добавить заметку, Вам нужно использовать команду\nздобавить [text]\nПример верной команды: !добавить привет\nВнимание! В данный момент запрещено использовать везде символ =, будьте внимательны!"
        else:
            return f"Данной команды не существует!"
    
    @staticmethod
    def _clean_all_tag_from_str(string_line):
        result = ""
        not_skip = True
        for i in list(string_line):
            if not_skip:
                if i == "<":
                    not_skip = False
                else:
                    result += i
            else:
                if i == ">":
                    not_skip = True

        return result