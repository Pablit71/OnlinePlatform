# OnlinePlatform

## Стак:

1. Python 3.10, Django , DRF - backend
2. DATABASE - Postgresql

## Тестовый проект сделан по ТЗ:

1. Реализация сети в которую входит информация и структура о ней
2. В админ панели реализовано:
- Ссылка на главного поставщика;
- фильтр по названи города;
- «admin action», очищающий задолженность перед поставщиком у выбранных объектов.
3.  Информация обо всех объектах сети
4. Информация об объектах определённой страны (фильтр по названию)
5. Статистика об объектах, задолженность которых превышает среднюю задолженность всех объектов
6. Все объекты сети, где можно встретить определённый продукт (фильтр по id продукта)
7. Возможность создания и удаления объекта сети и продукта
8. Возможность обновления данных объекта сети и продукта (запрет обновления через API поля «Задолженность перед поставщиком»)
9. Настроены права доступа к API так, чтобы только активные сотрудники имели доступ к API

## Для подключения и проверки:

1. Данные дляподключения к БД хранятся в файле .env в незашифрованном виде 
2. Ссылки :
- http://127.0.0.1:8000/swagger/ - swagger для данного сайта
- http://127.0.0.1:8000/api-auth/ - rest_framework
- http://127.0.0.1:8000/create_chain/ -  создание сети
- http://127.0.0.1:8000/update_chain/pk - обновление сети
- http://127.0.0.1:8000/all_chain/ - все сети
- http://127.0.0.1:8000/country/ - фильтрация по стране 
- http://127.0.0.1:8000/product/ - фильтрация по id продукта
- http://127.0.0.1:8000/staticdebt/ - сети , превышающую среднюю задолженность 
- http://127.0.0.1:8000/delete_chain/ - удаление сети ( а так же продуктов и контактов)
