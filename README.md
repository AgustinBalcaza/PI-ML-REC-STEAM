PI-ML-REC-STEAM
==============

Introducción
--------------

Este proyecto es una simulación de una experiencia laboral como Data Scientist en Steam. El objetivo principal es crear una API que cuente con 6 endpoints (debe tener un endpoint de recomendación de juegos) y que esa API pueda ser consumible desde la web (se debe realizar el deploy de la app).

Contenido del repositorio
-----------------------------

- `ETL y EDA/`: En esta carpeta se encuentran los procesos de ETL y el EDA (Exploratory Data Analysis). Podrás encontrar tanto los procesos de ETL que se utilizaron para obtener los datasets de la carpeta **data** como también el EDA.

- `data/`: En esta carpeta encontrararás los conjuntos de datos resultantes de todo el proceso de ETL para asegurar que funcionen de manera efectiva tanto en FastAPI como en Render. Esto garantiza que los datos estén listos para su uso sin que haya problemas.

- `functions_test.ipynb`: En este archivo se encuentran la creación y las pruebas de las funciones antes de crear la API, incluyendo la función de Machine Learning (recomendación de juegos).

- `Machine_Learning.ipynb`: En este archivo está el procedimiento que se llevó a cabo para la preparación del modelo de Machine Learning.

- `functions.py`: En este archivo se encuentran las funciones para poder levantar los endpoints de la API.

- `main.py`: Este es el archivo principal de la API FastAPI que expone los endpoints y proporciona acceso a la funcionalidad del sistema de recomendación.

- `requirements.txt`: El archivo que lista las bibliotecas de Python necesarias para ejecutar el proyecto.


Endpoints de la API
--------------------

- `GET /PlayTimeGenre`: Devuelve cuál es el año con más horas jugadas para el género especificado.

- `GET /UserForGenre`: Proporciona información sobre el usuario que ha acumulado más horas jugadas para un género específico, junto con una lista de la acumulación de horas jugadas por año.

- `GET /UsersRecommend`: Devuelve el Top 3 de los juegos más recomendados por los usuarios para el año especificado (con mayor cantidad de reseñas positivas).

- `GET /UsersWorstDeveloper`: Devuelve el Top 3 de las desarrolladoras con mayor cantidad de reseñas negativas para el año especificado.

- `GET /sentiment_analysis`: Devuelve la cantidad en total de reseñas positivas, neutrales y negativas que ha tenido una desarrolladora en específico.

- `GET /recomendacion_juego`: Proporciona una lista de 5 juegos recomendados similares al juego con el ID especificado.


Utilización de la API
---------------------

Para utilizar la API, puedes realizar consultas directamente en el sitio donde se hizo el deploy. La API está diseñada para recomendar juegos y también brindar datos sobre desarrolladoras y juegos de Steam. Puedes acceder a la documentación y realizar consultas haciendo [click aquí](https://pi-ds-mlops-steam-agustinbalcaza.onrender.com/docs).


Autor
-------

- **Agustín Balcaza** - [LinkedIn](https://ar.linkedin.com/in/agustin-balcaza-35aaa5266?trk=people_directory)
