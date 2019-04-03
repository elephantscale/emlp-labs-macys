import logging
logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)

import time
t1 = time.time()

import numpy as np
import pandas as pd

from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import StratifiedKFold
from fuzzywuzzy import fuzz

from utils import get_movieId,\
                  add_new_user_to_data,\
                  recommend,\
                  fuzzy_matching,\
                  ALSRecommender,\
                  get_rating_matrix
                  
from emlpfsms import EMLPfsms
    

LARGE_DATASET = True

if __name__ == '__main__':
    
    if LARGE_DATASET is False:
        
        movies_filename = '/srv/app/src/movies.csv'
        ratings_filename = '/srv/app/src/ratings.csv'
        
        movies_df = pd.read_csv(movies_filename,
                            usecols=['movieId', 'title'],
                            dtype={'movieId': 'int32', 'title': 'str'})
    
        ratings_df = pd.read_csv(ratings_filename,
                             usecols=['userId', 'movieId', 'rating'],
                             dtype={'userId': 'int32', 'movieId': 'int32', 'rating': 'float32'})
        
    else:   
        movies_filename = '/srv/app/src/movies1.csv'
        ratings_filename = '/srv/app/src/ratings1.csv'
    
        movies_df = pd.read_csv(movies_filename,
                            usecols=['movieId', 'title'],
                            dtype={'movieId': 'int32', 'title': 'str'})
                            
        movies_df = movies_df[["movieId","title"]]
    
        ratings_df1 = pd.read_csv(ratings_filename,
                             usecols=['userId', 'movieId', 'rating'],
                             dtype={'userId': 'int32', 'movieId': 'int32', 'rating': 'float32'})
                             
        ratings_df1 = ratings_df1[["userId", "movieId", "rating"]]

        ratings_df = ratings_df1

    num_users = len(ratings_df.userId.unique())
    num_items = len(ratings_df.movieId.unique())
    num_ratings = len(ratings_df.rating)
    print('There are {} ratings from {} unique users and {} unique movies in this data set \n'.format(num_ratings,num_users, num_items))
    
    print(movies_df.head().to_string())
    print("\n")
    print(ratings_df.head().to_string())
    
    print("data_loading_completed\n\n")
    print("building model\n\n")
    
    new_mat = ratings_df.pivot(index='movieId', columns='userId', values='rating').fillna(0)
    movie_to_idx = { movie: i for i,movie in 
        enumerate(list(movies_df.set_index('movieId').loc[new_mat.index].title))}

    n_splits = 2
    skf = StratifiedKFold(n_splits=n_splits, random_state=0)
    splits = [
        (train_inds, test_inds)
        for train_inds, test_inds in skf.split(ratings_df, ratings_df['userId'])
    ]
    
    train_inds, test_inds = splits[0]
    train_df, test_df = ratings_df.iloc[train_inds], ratings_df.iloc[test_inds]
    
    model = ALSRecommender(k=20, lmbda=0.1, max_epochs=15, baseline_algo=None, verbose=False)
    movie_list = ["Iron Man"] 
    movies, pred = recommend(model, train_df, movie_list, movies_df, ratings_df, movie_to_idx)
    
    print("Making Recommendations\n\n")
    
    for i,idx in enumerate(movies):
        print('{0}: {1}'.format(i+1, (movies_df[movies_df.movieId==idx].title).values))
    
    print(f'\n Total time taken for the Recommender System to run is {time.time()-t1}')
