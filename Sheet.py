import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from abc import ABC, abstractmethod

class Connect_with_sheet():
    def __init__(self):
        self.scope = ['https://www.googleapis.com/auth/spreadsheets',\
         'https://www.googleapis.com/auth/drive.file',\
         "https://www.googleapis.com/auth/drive"]
        self.creds = ServiceAccountCredentials.from_json_keyfile_name(\
            'testing-747a17f8cab3.json', self.scope)
        self.client = gspread.authorize(self.creds)
        self.sheet = self.client.open('1984').sheet1
        self.data = self.sheet.get_all_records

        
    def calculate_responsobility(self):
        responsobility = list(self.sheet.row_values(1))[0:32]
        responsobility = [element for element in responsobility if element !='']
        return responsobility
    
    def return_sheet(self):
        return self.sheet
    
    def calculate_number_of_slaves(self):
        return list(self.sheet.row_values(2))[0:4]
    
class Business(ABC):
    
    def __init__(self):
        pass
    
    def find_cheater(self):
        pass
    
    def notify_cheater(self):
        pass
    
    def mark_cheater(self):
        pass
    
    def work_with_max_min(self):
        pass
    
class Notneccessary(Business):
    
    def __init__(self, values_of_notneccessary, value_to_calculate):
        self.sheet = Connect_with_sheet().return_sheet()
        self.notneccessary = values_of_notneccessary
        self.value_to_calculate = value_to_calculate
        self.responsobility = Connect_with_sheet().calculate_responsobility()
        self.slaves = Connect_with_sheet().calculate_number_of_slaves()
        self.number = len(self.slaves)
    
    def calculate_the_positions_of_markers(self):
        tmp_value_index = self.responsobility.index(self.value_to_calculate)
        value_of_position = 1 * self.number * (tmp_value_index) + 1
        return [value_of_position, value_of_position + self.number]
    
    def calculate_the_number_of_signs(self, list_where_setted_values):
        list_with_signs = [tmp_element for tmp_element in list_where_setted_values if tmp_element == '!']
        return len(list_with_signs)
    
    def find_cheater(self):
        check = False
        tmp_iterator = 0
        for tmp in self.notneccessary:
            if tmp == self.value_to_calculate:
                check = True
        if check:
            position = self.calculate_the_positions_of_markers()
            tmp_array = []
            for tmp in range(position[0], position[1], 1):
                col = list(sheet.col_values(tmp))[2:]
                tmp_array.append(col)
            tmp_value = tmp_array[0]
            for tmp_number in tmp_array:
                if tmp_value == tmp_number:
                    tmp_iterator += 1
            if tmp_iterator < len(tmp_array):
                tmp_index = tmp_array.index(min(tmp_array))
            else:
                tmp_index = 0
            return self.slaves[tmp_index]

    def mark_cheater(self):
        name_of_undone_worker = self.find_cheater()
        string_to_return = '{}, пожалуйста у тебя остались дела, {} не совершалась очень давно'.format(\
                            name_of_undone_worker, self.value_to_calculate.lower())
        return string_to_return
    
    def update_the_quantity(self):
        first_index = self.calculate_the_positions_of_markers()[0]
        tmp_mark = '!'
        position_to_take = len(list(sheet.col_values(first_index))[2:]) + 3
        for tmp_value in range(first_index, first_index + len(self.slaves), 1):
            self.sheet.update_cell(position_to_take, tmp_value, tmp_mark)
        return 0

    def deleting_values(self):
        first_index = self.calculate_the_positions_of_markers()[0]
        position_to_take = len(list(sheet.col_values(first_index))[2:]) + 2
        for tmp_value in range(first_index, first_index + len(self.slaves), 1):
            self.sheet.update_cell(position_to_take, tmp_value, '')
        return 0
    
    def notify_cheater(self):
        pass


