#!/usr/bin/env python
# coding: utf-8

# In[124]:


import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

class Working_with_sheet():
    
    def __init__(self, value_to_calculate):
        self.scope = ['https://www.googleapis.com/auth/spreadsheets',         'https://www.googleapis.com/auth/drive.file',         "https://www.googleapis.com/auth/drive"]
        self.creds = ServiceAccountCredentials.from_json_keyfile_name(            'testing-747a17f8cab3.json', self.scope)
        self.client = gspread.authorize(self.creds)
        self.responsobility = ('МУСОР', 'УБОРКА', 'СТОЛ', 'ИНТЕРНЕТ',                                'ТАРАКАНЫ', 'МОЮЩИЕ', 'ПРИБОРЫ', 'ГРИБОК')
        self.list_of_slaves = ['Саша', 'Данил','Влад', 'Андрей']
        self.value_to_calculate = value_to_calculate
       
    def calculating_the_positions_of_markers(self):
        tmp_value_index = self.responsobility.index(self.value_to_calculate)
        value_of_position = 1*4*(tmp_value_index) + 1
        return [value_of_position, value_of_position + 4]
    
    def checking_of_all_cheaters(self, column, minimum_in_list, index_of_minimum):
        array_with_cheaters_index = []
        cheaters = []
        for tmp_value in range(0, len(column), 1):
            if tmp_value != (index_of_minimum  - 1) and column[tmp_value] == minimum_in_list:
                array_with_cheaters_index.append(tmp_value)
        if len(array_with_cheaters_index) > 0:
            for tmp_index in array_with_cheaters_index:
                cheaters.append(self.list_of_slaves[tmp_index])
            return cheaters
        else:
            return self.list_of_slaves[index_of_minimum - 1]
    
    def checking_how_much_must_he_work(self, array_with_work, index_of_minimum_value):
        reworked_array = array_with_work[:]
        reworked_array.remove(array_with_work[index_of_minimum_value])
        minimum_of_job = min(reworked_array) - array_with_work[index_of_minimum_value]
        maximum_of_job = max(reworked_array) - array_with_work[index_of_minimum_value]
        return [minimum_of_job, maximum_of_job]
    
    def developing_string(self, list_to_develop):
        string_for_return = ''
        for tmp in list_to_develop:
            string_for_return += str(tmp) + ', '
        string_for_return = string_for_return[0:len(string_for_return) - 2]
        return string_for_return
    
    def using_the_second_strings(self, list_with_minimum_maximum):
        second_part_string = ''
        ridiculous_punch = ' Исправь пока не пошутил про mommy, padlo.'
        if list_with_minimum_maximum[0] == list_with_minimum_maximum[1]:
            second_part_string += ' Расстояние от людей составляет ' + str(list_with_minimum_maximum[0]) + '.'
            second_part_string += ridiculous_punch
        elif list_with_minimum_maximum[0] == 0 and list_with_minimum_maximum[1] != 0:
            second_part_string += 'Вроде всё хорошо, но есть куда стремиться. Вот пока у максимально работающего'
            second_part_string += ' пока отрыв на ' + str(list_with_minimum_maximum[1]) + '.'
        elif list_with_minimum_maximum[1] == 0:
            second_part_string += ' Или вы все бездельники или пока не всё так плохо.'
        else:
            second_part_string += 'Минимальный отрыв от людей составляет ' + str(list_with_minimum_maximum[0]) + '.'
            second_part_string += ' Максимальный - ' + str(list_with_minimum_maximum[1]) + '.'
            second_part_string += ridiculous_punch
        return second_part_string

    def using_the_strings(self, value_of_cheaters):
        string_of_message = ''
        if len(value_of_cheaters) == 1:
            string_of_cheater = str(value_of_cheaters[0])
            string_of_message += 'Не выполняет обязанности по делу ' +  self.value_to_calculate.lower() + ' '
            string_of_message += string_of_cheater + '. '
        elif len(value_of_cheaters) > 1 and len(value_of_cheaters) < len(self.list_of_slaves):
            string_of_cheater = self.developing_string(value_of_cheaters)
            string_of_message += 'Не выполняют обязанности по делу ' +  self.value_to_calculate.lower() + ' '
            string_of_message += string_of_cheater + '. '
        else:
            string_of_message += 'Не выполняют обязанности по делу ' +  self.value_to_calculate.lower() + ' все.'
        return string_of_message
    
    def developing_an_ultimate_answer(self, cheaters_list, list_of_min_max):
        string_first_part = self.using_the_strings(cheaters_list)
        string_second_part = self.using_the_second_strings(list_of_min_max)
        return string_first_part + string_second_part
    
    def opening_and_finding_min(self):
        position = self.calculating_the_positions_of_markers()
        sheet = self.client.open('1984').sheet1
        if self.value_to_calculate:
            tmp_array = []
            for tmp in range(position[0], position[1], 1):
                col = list(sheet.col_values(tmp))[2:]
                tmp_array.append(len(col))
            a = tmp_array.index(min(tmp_array))
            minimum_and_maximum = self.checking_how_much_must_he_work(tmp_array, a)
            cheaters_list = self.checking_of_all_cheaters(tmp_array, min(tmp_array), a)
            result_speech = self.developing_an_ultimate_answer(cheaters_list, minimum_and_maximum)
            print(result_speech)
        return 0
    
    def updating_values(self):
        pass
    
    def delaying_value(self):
        pass
    
if __name__ == '__main__':
    responsobility = ('МУСОР', 'УБОРКА', 'СТОЛ', 'ИНТЕРНЕТ',                                'ТАРАКАНЫ', 'МОЮЩИЕ', 'ПРИБОРЫ', 'ГРИБОК')
    for tmp in responsobility:
        Working_with_sheet(tmp).opening_and_finding_min()




