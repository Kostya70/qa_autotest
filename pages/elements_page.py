import random
import time

from selenium.webdriver.common.by import By

from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators
from pages.base_page import BasePage

class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()
    # Заполняю форму
    def fill_all_fields(self):
        person_info = next(generated_person()) # итератор позволяет взять одну итерацию. Один раз экземпляра Person
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    # Проверяю форму
    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address

class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)] # всего 17 элементов будем обращаться от 1 до 15
            if count > 0:
                self.go_to_element(item)
                item.click()
                print(item.text)
                count -= 1
            else:
                break

    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_elements(By.XPATH, ".//ancestor::span[@class='rct-title']")
            data.append(title_item)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()


#     def get_checked_checkboxes(self):
#         checked_list = self.element_are_present(self.locators.CHECKED_ITEMS)
#         data = [] # список куда буду писать данные
#         for box in checked_list:
#             title_item = box.find_elements(By.XPATH, ".//ancestor::span[@class='rct-title']")
#             data.append(title_item) # добавляем в список
#         return data
#
# #         for item in item_list:
# # #            print(item.text) #проверяю
# #             self.go_to_element(item) #элемент был перекрыт этот метод поможет
# #             item.click()
#
#     def get_output_result(self):
#         result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
#         data = []
#         for item in result_list:
#             data.append(item.text)
#         return data
class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()
    def click_on_the_radio_button(self, choice): # добавил аргумент choise для выбора 3 радиобаттонов
        choices = {'yes': self.locators.YES_RADIOBUTTON,
                  'impressive': self.locators.IMPRESSIVE_RADIOBUTTON,
                  'no': self.locators.NO_RADIOBUTTON}
        self.element_is_visible(choices[choice]).click()

    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text