Цели проекта

    cпарсить данные с сайта auto.ru
    обработать данные для построения модели
    сгенерировать новые признаки
    выбрать модель для корректной работы модели, применить бэггинг/стэкинг

Этапы работы:

    парсинг данных
    ознакомление с данными и выявление пустых значений, их заполнение,
    обработка категоральных и бинарных признаков;
    построение наивной модели и её оценка ее результатов;
    анализ каждого признака, оценка корреляции между признаками и между целевой переменной и признаками;
    создание новых признаков
    выбор и построение модели

Выводы:

Парсинг занял очень много времени, удалось спарсить данные по порядка 48 тысячам ссылок, как по мнне, недостаточно, но работала с тем, что есть. Было рассмотрено несколько моделей : ExtraTreesRegressor, RandomForestRegressor, GradientBoostingRegressor, BaggingRegressor, XGBRegressor и Catboost, который был предложен в Baseline, из них выбрано 3 модели для стекинга Rачество модели улучшилось, MAPE = 15,5, на ЛБ 20,16
в репозиторий добавила черновик, где прогоняла разные варианты моделей и подбор гиперпараметров

