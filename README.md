Создаем таблицы в PostgreSQL базе:<br/>
> python table_create_alchemy.py \<company\><br/>
Например: python table_create_alchemy.py playstation<br/>
(table_delete_alchemy.py \<company\> соответственно удаляет таблицы)<br/>
В базе создается таблица playstation_games<br/>

# Тут будут замеры асинхронных парсеров:
Функция ps_parser выполнилась за 1052.337182044983 секунд.<br/>
Функция async_ps_parser выполнилась за 1264.0373182296753 секунд.<br/>
Функция async_ps_parser_optimized выполнилась за 1215.7589137554169 секунд.<br/>
<br/>
¯\\_(ツ)_/¯<br/>
