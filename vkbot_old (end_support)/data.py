# Функция работы с гугл таблицами
import gspread

gc = gspread.service_account(filename='BD.json')

sh = gc.open_by_url(
    "url")
worksheet = sh.get_worksheet(0)
notesheet = sh.get_worksheet(1)
count_note = 0

# функции для считывания/записи в базу данных
def len_base():
    value_list = worksheet.col_values(1)
    return len(value_list)

def row_len(row):
    value_list = worksheet.row_values(row)
    return len(value_list)

def get_id():
    value_list = worksheet.get_values("A2:A")
    return value_list

def get_name():
    value_list = worksheet.get_values("C2:C")
    return value_list

def find_people(id):
    value_list = worksheet.col_values(1)
    for i in range(1,len(value_list)):
        if (int(value_list[i]) == id):
            return i+1
    return 0

def get_permission(id):
    count = find_people(id)
    return worksheet.cell(count, 2).value

def g_write(id, dostup, name, row):
    if (row == 0):
        count = len_base() + 1
        worksheet.update_cell(count, 1, id)
        worksheet.update_cell(count, 2, dostup)
        worksheet.update_cell(count, 3, name)
    else:
        count = find_people(id)
        worksheet.update_cell(count, 2, dostup)

def get_info(id):
    number = find_people(id)
    if (number == 0):
        return 0
    else:
        value_list = worksheet.row_values(number)
        return value_list

def get_data():
    list_of_lists = worksheet.get_all_values()
    return list_of_lists

# функции для работы заметок
def row_len_note(row):
    value_list = notesheet.row_values(row)
    return len(value_list)

def n_write(id):
    count = row_len_note(1) + 1
    print(count)
    notesheet.update_cell(1,count, id)

def note_value(row):
    value_list = notesheet.col_values(row)
    return len(value_list)

def add_note(id,text):
    col = find_people(id)
    count_note = note_value(col) + 1
    notesheet.update_cell(count_note,col, text)
    return count_note - 1

def get_note(id,number):
    col = find_people(id)
    count = note_value(col)
    if(number < 1):
        return f"Вы указали неверный номер заметки."
    if(count == 1):
        return f"У Вас нет заметок."
    elif(count > 1 and number < count):
        value = notesheet.cell(number + 1,col).value
        return f"Содержание {number} заметки:\n{value}"
    else:
        return f"Заметки {number} не существует.\nВсего заметок {count - 1}."

def delete_note(id,number):
    col = find_people(id)
    count = note_value(col)
    if(number < 1 and number > count - 1):
        return f"Вы указали неверный номер заметки."
    if(count == 1):
        return f"У Вас нет заметок."
    elif(count > 1 and number < count):
        value_list = notesheet.col_values(col)
        for i in range(count):
            if(i == number):
                value_list[i] = ""
            elif(i > number):
                value_list[i - 1] = value_list[i]
        value_list[-1] = ""
        for i in range(count):
            notesheet.update_cell(i + 1, col, value_list[i])
        return f"Заметка {number} удалена."

def count_note(id):
    col = find_people(id) # номер столбца пользователя
    count = note_value(col) # количество значений в столбце пользователя
    note = []
    if(count == 0):
        return 1
    for i in range(2, count + 1):
        value = notesheet.cell(i,col).value
        num = i - 1
        string = "Заметка " + str(num) + ": " + str(value)
        note.append(string)
    return note, count - 1