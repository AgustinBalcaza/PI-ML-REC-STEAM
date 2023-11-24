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
    grouped_df = filtered_df.groupby('release_year')['playtime_forever'].sum()
    max_year = grouped_df.idxmax()
    result = {"Año de lanzamiento con más horas jugadas para {}: {}".format(genero, max_year)}
    return result

def UserForGenre(genero: str):
    genre_df = userforgenre[userforgenre['genres'] == genero]
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
    filtered_df = usersrecommend[(usersrecommend['year'] == año) & (usersrecommend['recommendations'] > 0)]
    sorted_df = filtered_df.sort_values(by='recommendations', ascending=False)
    top_3 = sorted_df.head(3)
    result = [{"Puesto 1": top_3.iloc[0]['app_name']},
              {"Puesto 2": top_3.iloc[1]['app_name']},
              {"Puesto 3": top_3.iloc[2]['app_name']}]
    return result

def UsersWorstDeveloper(año: int):
    filtered_df = usersworstdeveloper[(usersworstdeveloper['year'] == año) & (usersworstdeveloper['bad_reviews'] > 0)]
    developer_bad_reviews = filtered_df.groupby('developer')['bad_reviews'].sum()
    top_developers = developer_bad_reviews.sort_values(ascending=False).head(3)
    result = [{"Puesto {}: {}".format(i + 1, developer)}
              for i, (developer) in enumerate(top_developers.items())]
    return result

def sentiment_analysis(desarrolladora: str):
    empresa_df = sentimentanalysis[sentimentanalysis['developer'] == desarrolladora]
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
    path = 'data/cosine_sim.npy'
    cosine_sim = np.load(path)
    idx = recomendacionjuego[recomendacionjuego['id'] == game_id].index[0]
    rec_games = recomendacionjuego['app_name'].iloc[cosine_sim[idx]]
    info = {'recomendaciones': None}
    info['recomendaciones'] = list(rec_games)
    return info