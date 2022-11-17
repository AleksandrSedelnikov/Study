# Функция обработки сообщений
import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_bot import VkBot
import data
import threading

# Создание мультипроцесса [Не работает]
def thread(fn):
    def execute(*args, **kwargs):
        threading.Thread(target=fn, args=args,
                         kwargs=kwargs, daemon=True).start()
    return execute

# Получение уровня прав пользователя
def permission(id):
    dostup = data.get_permission(id)
    return dostup

# Создание стандартной клавиатуры
def default_keyboard(id):
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button('команды', color=VkKeyboardColor.SECONDARY)
    return keyboard.get_keyboard()

# Создание командной клавиатуры
def command_keyboard(id):
    dostup = int(permission(id))
    if(dostup == 1 or dostup == 2):
        keyboard = VkKeyboard(one_time=False)
        keyboard.add_button('!инфо', color=VkKeyboardColor.SECONDARY)
        keyboard.add_button('в меню', color=VkKeyboardColor.SECONDARY)
        keyboard.add_line()
        keyboard.add_button('!дата', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('!рестарт', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('!доступ', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('заметки', color=VkKeyboardColor.PRIMARY)
        return keyboard.get_keyboard()
    elif(dostup == 3 or dostup == 4):
        keyboard = VkKeyboard(one_time=False)
        keyboard.add_button('!инфо', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('в меню', color=VkKeyboardColor.SECONDARY)
        keyboard.add_line()
        keyboard.add_button('заметки', color=VkKeyboardColor.PRIMARY)
        return keyboard.get_keyboard()

def note_keyboard(id):
    dostup = int(permission(id))
    if(dostup != 0):
        keyboard = VkKeyboard(one_time=False)
        keyboard.add_button('обновить поле #0', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('назад', color=VkKeyboardColor.SECONDARY)
        keyboard.add_line()
        keyboard.add_button('заметки инфо', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('заметки удалить', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_line()
        keyboard.add_button('заметки количество', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('заметки добавить', color=VkKeyboardColor.PRIMARY)
        return keyboard.get_keyboard()

def note_info_keyboard(id):
    dostup = int(permission(id))
    if(dostup != 0):
        row = data.find_people(id)
        count = data.note_value(row)
        if(count == 1):
            keyboard = VkKeyboard(one_time=False)
            keyboard.add_button('обновить поле #1', color=VkKeyboardColor.POSITIVE)
            keyboard.add_button('назад в заметки', color=VkKeyboardColor.SECONDARY)
            return keyboard.get_keyboard()
        else:
            keyboard = VkKeyboard(one_time=False)
            keyboard.add_button('назад в заметки', color=VkKeyboardColor.SECONDARY)
            keyboard.add_button('обновить поле #1', color=VkKeyboardColor.POSITIVE)
            keyboard.add_line()
            for i in range(count - 1):
                num = str(i + 1)
                next_line = i + 1
                if(next_line % 3 == 1 and next_line != 1):
                    keyboard.add_line()
                keyboard.add_button("заметка " + num, color=VkKeyboardColor.PRIMARY)
            return keyboard.get_keyboard()

def note_delete_keyboard(id):
    dostup = int(permission(id))
    if(dostup != 0):
        row = data.find_people(id)
        count = data.note_value(row)
        if(count == 1):
            keyboard = VkKeyboard(one_time=False)
            keyboard.add_button('обновить поле #2', color=VkKeyboardColor.POSITIVE)
            keyboard.add_button('назад в заметки', color=VkKeyboardColor.SECONDARY)
            return keyboard.get_keyboard()
        else:
            keyboard = VkKeyboard(one_time=False)
            keyboard.add_button('назад в заметки', color=VkKeyboardColor.SECONDARY)
            keyboard.add_button('обновить поле #2', color=VkKeyboardColor.POSITIVE)
            keyboard.add_line()
            for i in range(count - 1):
                num = str(i + 1)
                next_line = i + 1
                if(next_line % 3 == 1 and next_line != 1):
                    keyboard.add_line()
                keyboard.add_button("зудалить " + num, color=VkKeyboardColor.NEGATIVE)
            return keyboard.get_keyboard()



def write_msg(user_id, message):
    vk.method('messages.send', {
              'user_id': user_id, 'message': message, 'random_id': random.randint(0, 2048)})

# Отправление стандартных сообщений клавиатурой
def create_keyboard_d(user_id, message):
    vk.method('messages.send', {
              'user_id': user_id, 'message': message, 'random_id': random.randint(0, 2048), 'keyboard': default_keyboard(user_id)})

# Отправление командных сообщений клавиатурой
def create_keyboard_c(user_id, message):
    vk.method('messages.send', {
              'user_id': user_id, 'message': message, 'random_id': random.randint(0, 2048), 'keyboard': command_keyboard(user_id)})

def create_keyboard_n(user_id, message):
    vk.method('messages.send', {
              'user_id': user_id, 'message': message, 'random_id': random.randint(0, 2048), 'keyboard': note_keyboard(user_id)})

def create_keyboard_ni(user_id, message):
    vk.method('messages.send', {
              'user_id': user_id, 'message': message, 'random_id': random.randint(0, 2048), 'keyboard': note_info_keyboard(user_id)})

def create_keyboard_nd(user_id, message):
    vk.method('messages.send', {
              'user_id': user_id, 'message': message, 'random_id': random.randint(0, 2048), 'keyboard': note_delete_keyboard(user_id)})

# API-ключ
token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
vk = vk_api.VkApi(token=token)
# Работа с сообщениями
longpoll = VkLongPoll(vk)

print("Бот поднят или перезапущен")
for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:

            print("-------------------")
            print(
                f'Получено новое сообщение от пользователя с id: {event.peer_id}', end='\n')
            print('Text: ', event.text)
            bot = VkBot(event.peer_id)
            if(data.find_people(event.peer_id) == 0):
                name = VkBot._get_user_name_from_vk_id(VkBot,event.peer_id) + " " + VkBot._get_user_lastname_from_vk_id(VkBot,event.peer_id)
                data.g_write(event.peer_id, 4, name, 0)
                data.n_write(event.peer_id)
            if (event.text.upper() == 'НАЧАТЬ' or event.text.upper() == "В МЕНЮ"):
                create_keyboard_d(event.peer_id, 'Вы в меню.')
            elif (event.text.upper() == "КОМАНДЫ" or event.text.upper() == "НАЗАД"):
                create_keyboard_c(event.peer_id, 'Вы в меню команд.')
            elif (event.text.upper() == "ЗАМЕТКИ" or event.text.upper() == "ОБНОВИТЬ ПОЛЕ #0" or event.text.upper() == "НАЗАД В ЗАМЕТКИ"):
                create_keyboard_n(event.peer_id, 'Вы в меню заметок.')
            elif (event.text.upper() == "ЗАМЕТКИ ИНФО" or event.text.upper() == "ОБНОВИТЬ ПОЛЕ #1"):
                create_keyboard_ni(event.peer_id, 'Вы в меню получения заметок.')
            elif (event.text.upper() == "ЗАМЕТКИ УДАЛИТЬ" or event.text.upper() == "ОБНОВИТЬ ПОЛЕ #2"):
                create_keyboard_nd(event.peer_id, 'Вы в меню удаления заметок.')
            else:
                write_msg(event.peer_id, bot.new_message(event.text))