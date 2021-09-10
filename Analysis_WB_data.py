'''
Im going to work on the WB data to make it clean as much as possible
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle


# import the data
def load_data_pickle(name):
    with open(name, 'rb') as f:
        return pickle.load(f)

raw_df = load_data_pickle('disney_movie_data_final.pickle')
raw_df = pd.DataFrame(raw_df)
raw_df.to_csv('disney_movie_data_final.csv')

raw_df = pd.read_csv('disney_movie_data_final.csv')
raw_df = raw_df.drop('Unnamed: 0', axis=1)
raw_df.sort_values(by='Directed by', inplace=True)
crosstab_by_director = pd.crosstab(raw_df['Directed by'], raw_df['title'])
film_made_by_director = crosstab_by_director.sum(axis=1)

# Director who made most film
raw_df['Directed by'] = raw_df['Directed by'].astype('str')
director_with_must_movies = pd.DataFrame()
director_with_must_movies['Director'], director_with_must_movies['Films'] = np.unique(raw_df['Directed by'], return_counts=True)

# Split the movies with two directors



print('Done!')


