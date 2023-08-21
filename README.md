# Итоговый проект по автоматизации тестирования
Skillfactory курса QAP-1035

В рамках проекта было произвелдено автоматизированное UI-тестирование нового интерфейса авторизации в личном кабинете от заказчика Ростелеком (https://b2c.passport.rt.ru/) с использованием PyTest и Selenium WebDriver

Для тестирования были использованы следующие техники тест-дизайна:
 - Таблица решений;
 - Выделение классов эквивалентности;
 - Анализ граничных значений;
 - Предугадывание ошибок.

В корне проекта содержится:
- chromedriver.exe - webdriver для взаимодействия с браузером Google Chrome 115.0.5790.170;
- conftest.py - файл, который содержит стуктуру для инициализации браузера и закрытия сессии после завершения теста
- requirements.py - файл, содержащий список внешних зависимостей

В директории pages:
- base_page.py - файл, в котором находится конструктор webdriver и общие для всех тестируемых страниц методы.
- locators.py - файл, который содержит все локаторы.
- random_page.py - файл, который содержит GET-запросы к временному почтовому ящику на сайте 1secmail.com для получения валидного E-mail и кода
- auth_page.py - файл, содержащий необходимые методы для работы с web-элементами на страницах авторизации, регистрации и восстановления пароля
- settings.py - исходные статические данные и учётные данные, используемые в проведении тестирования

В директории tests:
- test_positive_reg.py - автоматизированные тесты с позитивными сценариями страницы регистрации (python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_positive_reg.py)
- test_positive_auth.py - автоматизированные тесты с позитивными сценариями страницы авторизации (python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_positive_auth.py)
- test_negative_reg.py - автоматизированные тесты с негативными сценариями страницы регистрации (python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_negative_reg.py)
- test_negative_auth.py - автоматизированные тесты с негативными сценариями страницы авторизации (python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_negative_auth.py)
- test_negative_new_pass.py - автоматизированные тесты с негативными сценариями страницы восстановления пароля (python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_negative_new_pass.py)
