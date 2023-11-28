import pandas as pd
import numpy as np


playtimegenre = pd.read_csv('data/PlayTimeGenre.csv')
userforgenre = pd.read_csv('data/UserForGenre.csv')
usersrecommend = pd.read_csv('data/UsersRecommend.csv')
usersworstdeveloper = pd.read_csv('data/UsersWorstDeveloper.csv')
sentimentanalysis = pd.read_csv('data/sentiment_analysis.csv')
recomendacionjuego = pd.read_csv('data/product.csv')


def PlayTimeGenre(genero: str):
    filtered_df = playtimegenre[playtimegenre['genres'] == genero]
    if filtered_df.empty:
        error_message = {"Error": "Género incorrecto"}
        return error_message
    grouped_df = filtered_df.groupby('release_year')['playtime_forever'].sum()
    max_year = int(grouped_df.idxmax())
    result = {"Año de lanzamiento con más horas jugadas para Género {}".format(genero): max_year}
    return result

def UserForGenre(genero: str):
    genre_df = userforgenre[userforgenre['genres'] == genero]
    if genre_df.empty:
        error_message = {"Error": "Género no encontrado"}
        return error_message
    user_hours = genre_df.groupby('user_id')['playtime_forever'].sum()
    max_user = user_hours.idxmax()
    max_user_df = genre_df[genre_df['user_id'] == max_user]
    hours_by_year = max_user_df.groupby('release_year')['playtime_forever'].sum().reset_index()
    hours_list = [{'Año': year, 'Horas': hours} for year, hours in zip(hours_by_year['release_year'], hours_by_year['playtime_forever'])]
    result = {
        "Usuario con más horas jugadas para Género {}".format(genero): max_user,
        "Horas jugadas": hours_list
    }
    return result

def UsersRecommend(año: int):
    if not isinstance(año, int):
        error_message = {"Error": "Debe ingresar un año en formato entero"}
        return error_message
    filtered_df = usersrecommend[(usersrecommend['year'] == año) & (usersrecommend['recommend_score'] > 0)]
    if filtered_df.empty:
        error_message = {"Error": "No hay recomendaciones para el año especificado"}
        return error_message
    sorted_df = filtered_df.sort_values(by='recommend_score', ascending=False)
    top_3 = sorted_df.head(3)
    result = [{"Puesto 1": top_3.iloc[0]['app_name']},
              {"Puesto 2": top_3.iloc[1]['app_name']},
              {"Puesto 3": top_3.iloc[2]['app_name']}]
    return result

def UsersWorstDeveloper(año: int):
    if not isinstance(año, int):
        error_message = {"Error": "Debe ingresar un año en formato entero"}
        return error_message
    filtered_df = usersworstdeveloper[(usersworstdeveloper['year'] == año) & (usersworstdeveloper['bad_reviews'] > 0)]
    if filtered_df.empty:
        error_message = {"Error": "No hay reseñas negativas para el año especificado"}
        return error_message
    developer_stats = filtered_df.groupby('developer').agg({'bad_reviews': 'sum', 'recommend_score': ['min', 'sum']})
    sorted_developers = developer_stats.sort_values(by=[('bad_reviews', 'sum'), ('recommend_score', 'min'), ('recommend_score', 'sum')],
                                                    ascending=[False, True, True])
    top_developers = sorted_developers.head(3)
    result = [{"Puesto {}".format(i + 1): developer}
              for i, developer in enumerate(top_developers.index)]
    return result

def sentiment_analysis(desarrolladora: str):
    empresa_df = sentimentanalysis[sentimentanalysis['developer'] == desarrolladora]
    if empresa_df.empty:
        error_message = {'Error': 'Desarrolladora incorrecta'}
        return error_message
    total_negativas = int(empresa_df['bad_reviews'].sum())
    total_neutrales = int(empresa_df['neutral_reviews'].sum())
    total_positivas = int(empresa_df['good_reviews'].sum())
    resultado = {
        desarrolladora: {
            'Negative': total_negativas,
            'Neutral': total_neutrales,
            'Positive': total_positivas
        }
    }
    return resultado

def recomendacion_juego(game_id: int):
    if not isinstance(game_id, int):
        error_message = {"Error": "El Id del juego debe ser un valor entero"}
        return error_message
    if game_id not in recomendacionjuego['id'].values:
        error_message = {"Error": "Id de juego incorrecto"}
        return error_message
    path = 'data/cosine_sim.npy'
    cosine_sim = np.load(path)
    idx = recomendacionjuego[recomendacionjuego['id'] == game_id].index[0]
    rec_games = recomendacionjuego['app_name'].iloc[cosine_sim[idx]]
    info = {'recomendaciones': None}
    info['recomendaciones'] = list(rec_games)
    return info