# qa_autotest_ui
# Для тестов взял сайт https://demoqa.com/

Для установки: python -m pip install -r requirements. txt 

Установить allure: For Windows, Allure is available from the Scoop commandline-installer. To install Allure, download and install Scoop and then execute in the Powershell -scoop install allure

Для запуска allure прописать алиас: Set-Alias allure C:\allure-2.19.0\bin\allure.bat 
- pytest --alluredir=tests\allure_results tests\elements_test.py
- allure serve .\tests\allure_results 

Запустить тест локально можно из папки tests
Чтобы запустить конкретный тест из модуля, выполните:

pytest test_mod.py::test_func
Еще один пример спецификации тестового метода в командной строке:

pytest test_mod.py::TestClass::test_method
