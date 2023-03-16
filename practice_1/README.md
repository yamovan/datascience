# Практика 1. Подбор гиперпараметров моделей  
Практика основана на соревновании [Kaggle: Predicting a Biological Response](https://www.kaggle.com/c/bioresponse)

## Оглавление
[1. Описание задачи](https://github.com/yamovan/datascience/blob/main/practice_1/README.md#Описание-задачи)  
[2. Какой кейс решаем](https://github.com/yamovan/datascience/blob/main/practice_1/README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](https://github.com/yamovan/datascience/blob/main/practice_1/README.md#Краткая-информация-о-данных)  
[4. Этапы работы](https://github.com/yamovan/datascience/blob/main/practice_1/README.md#Этапы-работы)  
[5. Результат](https://github.com/yamovan/datascience/blob/main/practice_1/README.md#Результат)  
[6. Выводы](https://github.com/yamovan/datascience/blob/main/practice_1/README.md#Выводы)

### 1. Описание задачи
Необходимо предсказать биологический ответ молекул (столбец 'Activity') по их химическому составу (столбцы D1-D1776).   

### 2. Какой кейс решаем?
1. Обучить две модели: **логистическую регрессию** и **случайный лес**.
2. Сделать подбор гиперпараметров с помощью базовых и продвинутых методов оптимизации. Важно использовать **все четыре метода** (*GridSeachCV*, *RandomizedSearchCV*, *Hyperopt*, *Optuna*) хотя бы по разу, максимальное количество итераций не должно превышать 50.

**Метрика качества**  
В качестве метрики будем использовать **F1-score**

**Что практикуем**
- Подбор гиперпараметров моделей с помощью инструментов библиотеки *sklearn*: *GridSearchCV* и *RandomizedSearchCV*, а также библиотек *Hyperopt* и *Optuna*.

### 3. Краткая информация о данных
Исходные данные находятся [здесь:](https://drive.google.com/file/d/19NmwU2NX8pYaqprOKS-kBA0LPWaK1fl4/view?usp=share_link)
Данные представлены в формате *CSV*.  Каждая строка представляет молекулу. 

* Первый столбец *Activity* содержит экспериментальные данные, описывающие фактический биологический ответ [0, 1]; 
* Остальные столбцы *D1*-*D1776* представляют собой молекулярные дескрипторы — это вычисляемые свойства, которые могут фиксировать некоторые характеристики молекулы, например размер, форму или состав элементов.

### 4. Этапы работы
1. Знакомство с данными
2. Обучение модели *LogisticRegression*
3. Подбор гиперпараметров модели *LogisticRegression* с помощью четырех методов
4. Обучение модели *RandomForestClassifier* 
5. Подбор гиперпараметров модели *RandomForestClassifier* с помощью четырех методов
6. Выводы по результатам оценки качества моделей

### 5. Результат
* Выполнено практическое задание  
  
[Ноутбук с выполненными заданиями и выводами](https://github.com/yamovan/datascience/blob/main/practice_1/Practice_1_param_select.ipynb)  

### 6. Выводы
Создан кейс по машинному обучению


[к оглавлению](https://github.com/yamovan/datascience/blob/main/practice_1/README.md#Оглавление)