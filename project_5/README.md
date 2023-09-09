# Проект 5. Прогнозирование продолжительности поездки на такси в Нью-Йорке

## Оглавление
[1. Описание проекта](https://github.com/yamovan/datascience/blob/main/project_5/README.md#Описание-проекта)  
[2. Какой кейс решаем](https://github.com/yamovan/datascience/blob/main/project_5/README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](https://github.com/yamovan/datascience/blob/main/project_5/README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](https://github.com/yamovan/datascience/blob/main/project_5/README.md#Этапы-работы-над-проектом)  
[5. Результат](https://github.com/yamovan/datascience/blob/main/project_5/README.md#Результат)  
[6. Выводы](https://github.com/yamovan/datascience/blob/main/project_5/README.md#Выводы)

### 1. Описание проекта
Сервисы такси хранят огромные объёмы информации о поездках, включая такие данные, как конечная и начальная точки маршрута, дата поездки и её продолжительность. Эти данные можно использовать для того, чтобы прогнозировать длительность поездки в автоматическом режиме с привлечением искусственного интеллекта. Известно, что стоимость такси в США рассчитывается на основе фиксированной ставки и тарифной стоимости, величина которой зависит от времени и расстояния. Тарифы варьируются в зависимости от города.

В свою очередь, время поездки зависит от множества факторов, таких как направление поездки, время суток, погодные условия и так далее.

Таким образом, если мы разработаем алгоритм, способный определять длительность поездки, мы сможем прогнозировать её стоимость самым тривиальным образом, например, просто умножая стоимость на заданный тариф.

### 2. Какой кейс решаем?
Построить модель машинного обучения, которая на основе предложенных характеристик клиента будет предсказывать числовой признак — время поездки такси, то есть решить задачу регрессии.

**Метрика качества**  
Результат метрики RMSLE

**Что практикуем**
- Разведывательный анализ данных (EDA), проектирование признаков.
- Создание моделей машинного обучения.

### 3. Краткая информация о данных
Предоставлен набор данных, содержащий информацию о поездках на жёлтом такси в Нью-Йорке за 2016 год. Первоначально данные были выпущены Комиссией по Такси и Лимузинам Нью-Йорка и включают в себя информацию о времени поездки, географических координатах, количестве пассажиров и несколько других переменных.  
Исходные данные находятся [здесь](https://drive.google.com/file/d/1X_EJEfERiXki0SKtbnCL9JDv49Go14lF/view)  

Исходный файл с праздничными датами находится [здесь](https://lms-cdn.skillfactory.ru/assets/courseware/v1/33bd8d5f6f2ba8d00e2ce66ed0a9f510/asset-v1:SkillFactory+DST-3.0+28FEB2021+type@asset+block/holiday_data.csv)  

Файлы с данными из OSRM для поездок из тренировочной таблицы [здесь](https://drive.google.com/file/d/1ecWjor7Tn3HP7LEAm5a0B_wrIfdcVGwR/view?usp=sharing)  

[Набор данных](https://lms-cdn.skillfactory.ru/assets/courseware/v1/0f6abf84673975634c33b0689851e8cc/asset-v1:SkillFactory+DST-3.0+28FEB2021+type@asset+block/weather_data.zip), содержащий информацию о погодных условиях в Нью-Йорке в 2016 году.

### 4. Этапы работы над проектом
1. Первичная обработка данных
2. Разведывательный анализ данных (EDA)
3. Отбор и преобразование признаков
4. Решение задачи регрессии: линейная регрессия и деревья решений
5. Решение задачи регрессии: ансамбли моделей и построение прогноза

### 5. Результат
* Завершен пятый data science проект.  
  
[Ноутбук с выполненными заданиями и выводами](https://github.com/yamovan/datascience/blob/main/project_5/Project_5%20trip_duration.ipynb)  

### 6. Выводы
Создан кейс по машинному обучению


[к оглавлению](https://github.com/yamovan/datascience/blob/main/project_5/README.md#Оглавление)