import logging
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import math
from fuzzywuzzy import fuzz

####


import os
from emlpfsms import EMLPfsms

logging.basicConfig(level=logging.INFO)

LOG = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO)

LOG = logging.getLogger(__name__)

print("loading emlpfsms")

def fuzzy_matching(mapper, fav_movie, verbose=True):
    """
    return the closest match via fuzzy ratio. If no match found, return None
    
    Parameters
    ----------    
    mapper: dict, map movie title name to index of the movie in data

    fav_movie: str, name of user input movie
    
    verbose: bool, print log if True

    Return
    ------
    index of the closest match
    """
    match_tuple = []
    # get match
    for title, idx in mapper.items():
        ratio = fuzz.ratio(title.lower(), fav_movie.lower())
        if ratio >= 60:
            match_tuple.append((title, idx, ratio))
    # sort
    match_tuple = sorted(match_tuple, key=lambda x: x[2])[::-1]
    if not match_tuple:
        print('Oops! No match is found')
        return
    if verbose:
        print('Found possible matches in our database: {0}\n'.format([x[0] for x in match_tuple]))
    return match_tuple[0][1]



def make_recommendation(model_knn, data, mapper, fav_movie, n_recommendations):
    """
    return top n similar movie recommendations based on user's input movie


    Parameters
    ----------
    model_knn: sklearn model, knn model

    data: movie-user matrix

    mapper: dict, map movie title name to index of the movie in data

    fav_movie: str, name of user input movie

    n_recommendations: int, top n recommendations

    Return
    ------
    list of top n similar movie recommendations
    """
    # fit
    model_knn.fit(data)
    # get input movie index
    print('You have input movie:', fav_movie)
    idx = fuzzy_matching(mapper, fav_movie, verbose=True)
    # inference
    print('Recommendation system start to make inference')
    print('......\n')
    distances, indices = model_knn.kneighbors(data[idx], n_neighbors=n_recommendations+1)
    # get list of raw idx of recommendations
    raw_recommends = \
        sorted(list(zip(indices.squeeze().tolist(), distances.squeeze().tolist())), key=lambda x: x[1])[:0:-1]
    # get reverse mapper
    reverse_mapper = {v: k for k, v in mapper.items()}
    # print recommendations
    print('Recommendations for {}:'.format(fav_movie))
    for i, (idx, dist) in enumerate(raw_recommends):
        print('{0}: {1}, with distance of {2}'.format(i+1, reverse_mapper[idx], dist))


def save_model(some_string: str) -> str:
    print('CURRENT DIR2 ' + os.getcwd())
    fsms = EMLPfsms()

    upload_ms_path = './knn_model.sav'
    ms_bucket_path = 'test_project/knn_model.sav'
    project_name = 'test_project'
    model_name = 'Knn_model'

    test_model_description = 'description'
    test_training_dataset_name = 'your training dataset name'
    test_training_dataset_uuid = 'your uuid'
    test_training_algo = 'the training algo'
    test_input_type = 'the input type'
    test_output_type = 'ur output type'
    test_exp_notes = 'ur exp notes'
    test_tag_broken = True
    test_accuracy_auc = 0.9
    test_hyp_batch_size = 100
    test_data_source = 'Test data source'
    test_fe_methods = 'Test feature eng methods'
    test_contact = 'sreedhar.kumar@macys.com'


    ms_uuid = fsms.upload_ms_model(
       upload_ms_path,
       ms_bucket_path,
       project_name,
       model_name,
       test_model_description,
       test_training_dataset_name,
       test_training_dataset_uuid,
       test_training_algo,
       test_input_type,
       test_output_type,
       test_contact,
       exp_notes=test_exp_notes,
       tag_broken=test_tag_broken,
       accuracy_auc=test_accuracy_auc,
       hyp_batch_size=test_hyp_batch_size)

    print('ms_uuid ' + ms_uuid)
    print('ms_bucket_path ' + ms_bucket_path)
    return some_string

if __name__ == '__main__':
    
    print("data_loading_starting")
    
    movies_filename = '/srv/app/data/ml-10M100K/movies.dat'
    ratings_filename = '/srv/app/data/ml-10M100K/ratings.dat'
    
    movies = pd.read_csv(movies_filename,header=None,  sep = '::')
    movies.columns = ["movieId", "title", "genre"]
    
    ratings = pd.read_csv(ratings_filename,header=None,  sep = '::')
    ratings.columns = ["userId", "movieId", "rating","dummy"]
    

    df_movies = movies[["movieId","title"]]
    df_ratings = ratings[["userId", "movieId", "rating"]]
   
    #################################################### pandas dataframe with objects #################################
    
    print("data_loading_completed\n\n")
    print("building model\n\n")
    # pivot and create movie-user matrix
    movie_user_mat = df_ratings.pivot(index='movieId', columns='userId', values='rating').fillna(0)
    # create mapper from movie title to index
    movie_to_idx = {
        movie: i for i, movie in 
        enumerate(list(df_movies.set_index('movieId').loc[movie_user_mat.index].title))
    }
    # transform matrix to scipy sparse matrix
    movie_user_mat_sparse = csr_matrix(movie_user_mat.values)
    
    # define model
    model_knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=20, n_jobs=-1)
    # fit
    model_knn.fit(movie_user_mat_sparse)
    
    #################################################### model to model store ##########################################
    
    print("model building completed\n\n")
    my_favorite = 'Iron Man'
    print("serving recommendations\n\n")
    make_recommendation(
        model_knn=model_knn,
        data=movie_user_mat_sparse,
        fav_movie=my_favorite,
        mapper=movie_to_idx,
        n_recommendations=10)
    
    
    ## # ## Save Model Using Pickle
    import pandas
    from sklearn import model_selection
    import pickle
       
    filename = 'knn_model.sav'
    pickle.dump(model_knn, open(filename, 'wb'))
        
    save_model('Done saving the KNN model')
    
    

