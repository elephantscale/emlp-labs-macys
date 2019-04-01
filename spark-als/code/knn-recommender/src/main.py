import logging
logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)

import time
t1 = time.time()
import os

import math
import numpy as np
import pandas as pd

from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

from fuzzywuzzy import fuzz

from utils import make_recommendation,\
                  fuzzy_matching
                  
from emlpfsms import EMLPfsms

LARGE_DATASET = True

if __name__ == '__main__':
    
    if LARGE_DATASET is False:
        
        movies_filename = '/srv/app/src/movies.csv'
        ratings_filename = '/srv/app/src/ratings.csv'
        
        df_movies = pd.read_csv(movies_filename,
                            usecols=['movieId', 'title'],
                            dtype={'movieId': 'int32', 'title': 'str'})
    
        df_ratings = pd.read_csv(ratings_filename,
                             usecols=['userId', 'movieId', 'rating'],
                             dtype={'userId': 'int32', 'movieId': 'int32', 'rating': 'float32'})
        
    else:   
        movies_filename = '/srv/app/src/movies1.csv'
        ratings_filename = '/srv/app/src/ratings1.csv'
    
        df_movies = pd.read_csv(movies_filename,
                            usecols=['movieId', 'title'],
                            dtype={'movieId': 'int32', 'title': 'str'})
                            
        df_movies = df_movies[["movieId","title"]]
    
        df1_ratings = pd.read_csv(ratings_filename,
                             usecols=['userId', 'movieId', 'rating'],
                             dtype={'userId': 'int32', 'movieId': 'int32', 'rating': 'float32'})
                             
        df1_ratings = df1_ratings[["userId", "movieId", "rating"]]

        df_ratings = df1_ratings


    # BLOCK 2 : Read In Data, Sample A Few Movies 

    num_users = len(df_ratings.userId.unique())
    num_items = len(df_ratings.movieId.unique())
    num_ratings = len(df_ratings.rating)
    print('There are {} ratings from {} unique users and {} unique movies in this data set \n'.format(num_ratings,num_users, num_items))
    
    print(df_movies.head().to_string())
    print("\n")
    print(df_ratings.head().to_string())
    
    print("data_loading_completed\n\n")
    print("building model\n\n")
    
    movie_user_mat = df_ratings.pivot(index='movieId', columns='userId', values='rating').fillna(0)
    
    # Create Mapper From Movie Title To Index
    movie_to_idx = {
        movie: i for i, movie in 
        enumerate(list(df_movies.set_index('movieId').loc[movie_user_mat.index].title))
    }
    
    # Transform Matrix To Scipy Sparse Matrix
    movie_user_mat_sparse = csr_matrix(movie_user_mat.values)
    
    # BLOCK 8: Train Model
    
    # Define Model - The function called is imported from scikit-learn
    model_knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=20, n_jobs=-1)
    # Fit Model To Data
    model_knn.fit(movie_user_mat_sparse)
    
    # BLOCK 10 : Let's Make Some Recommendations!

    my_favorite = 'Iron Man'
    # 'Finding Nemo' 'Dark Knight' 'Avatar' 'Up' 'Inception' 'Beautiful Mind' 'Iron Man'
    
    make_recommendation(
        model_knn=model_knn,
        data=movie_user_mat_sparse,
        fav_movie=my_favorite,
        mapper=movie_to_idx,
        n_recommendations=10)
    print(f'\n Total time taken for the Recommender System to run is {time.time()-t1}')
