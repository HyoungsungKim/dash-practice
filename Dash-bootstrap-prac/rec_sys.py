import pandas as pd
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity

NUMBER_OF_SAMPLES = 100

class RecSys:
    def __init__(self):
        self.movies = pd.read_csv("../sample_data/movies.csv")
        self.ratings = pd.read_csv("../sample_data/ratings.csv")
        
        self.movies["genres"] = self.movies["genres"].apply(lambda x: "etc" if x == "(no genres listed)" else x)
        self.genres_columns = self.movies["genres"].str.get_dummies('|')
        self.genres_names = self.genres_columns.columns
        
        self.movies = pd.concat([self.movies.loc[:, ["movieId", "title"]], self.genres_columns], axis=1)        
                
                
    def get_genre_names(self):
        return self.genres_names
        
    # Filter out users who do not rate enough or rate too much
    def filter_out_users(self, lower_bound_rate=0.2, upper_bound_rate=0.8):
        temp_group = self.ratings.groupby("userId").count()
        
        np_ratings = temp_group["rating"].to_numpy()
        np_ratings = np.sort(np_ratings)

        lower_bound = np_ratings[int((len(np_ratings)*lower_bound_rate))]
        upper_bound = np_ratings[int((len(np_ratings)*upper_bound_rate))]
        
        filtered_userIds = temp_group.loc[(temp_group["rating"] > lower_bound) & (temp_group["rating"] < upper_bound)].reset_index()
        filtered_userIds = filtered_userIds[["userId"]]        
        
        filtered_ratings = pd.merge(left=filtered_userIds, right=self.ratings, on="userId")        
        
        return filtered_userIds.to_numpy(), filtered_ratings
    
    # Define user pivot table for future use. operate_rec_sys function only uses id column of pivot table
    def generate_user_pivot_table(self, src_userId):
        empty_genres = np.zeros((len(src_userId), len(self.genres_names)))

        user_pivot_table = pd.DataFrame({"userId":src_userId}).reset_index(drop=True)
        user_pivot_table = pd.concat([user_pivot_table, pd.DataFrame(empty_genres, columns=self.genres_names).reset_index(drop=True)], axis=1)
        user_pivot_table.sort_values(by="userId", inplace=True)
        
        return user_pivot_table
    
    def sample_bounded_userId(self, filtered_userIds):        
        # Random sample target userId for testing recommendation system        
        
        target_userId = np.random.choice(filtered_userIds.reshape(-1), 1)[0]
        src_userId_array = np.random.choice(filtered_userIds.reshape(-1), NUMBER_OF_SAMPLES)
        src_userId_array = np.sort(src_userId_array)
        
        return target_userId, src_userId_array
    
    def get_target_row(self, filtered_ratings, target_userId ):
        user_movies_ratings = pd.merge(left=filtered_ratings, right=self.movies, on="movieId")
        target_user_ratings = user_movies_ratings.loc[user_movies_ratings["userId"] == target_userId][["rating"]].to_numpy()
        target_user_genres = user_movies_ratings.loc[user_movies_ratings["userId"] == target_userId][self.genres_names].to_numpy()

        # Normalize to [0, 1]
        x = np.sum(target_user_ratings * target_user_genres, axis=0)
        target_user_row = (x - np.min(x))/(np.max(x) - np.min(x)).reshape(1, -1)
        
        return target_user_row
        
    def operate_rec_sys(self, filtered_ratings, target_userId=None, src_userId_array=None):              
        user_pivot_table = self.generate_user_pivot_table(src_userId_array)["userId"]        
        
        user_movies_ratings = pd.merge(left=filtered_ratings, right=self.movies, on="movieId")
        target_user_ratings = user_movies_ratings.loc[user_movies_ratings["userId"] == target_userId][["rating"]].to_numpy()
        target_user_genres = user_movies_ratings.loc[user_movies_ratings["userId"] == target_userId][self.genres_names].to_numpy()

        # Normalize to [0, 1]
        x = np.sum(target_user_ratings * target_user_genres, axis=0)
        target_user_row = (x - np.min(x))/(np.max(x) - np.min(x)).reshape(1, -1)
        #print(x)
        #print(target_user_row)
        
        for id in src_userId_array:        
            rate = user_movies_ratings.loc[user_movies_ratings["userId"] == id][["rating"]].to_numpy()
            genres = user_movies_ratings.loc[user_movies_ratings["userId"] == id][self.genres_names].to_numpy()    
            
            x = np.sum(rate * genres, axis=0)            
            src_user_row = (x - np.min(x))/(np.max(x) - np.min(x)).reshape(1, -1)            
            target_user_row = np.concatenate((target_user_row, src_user_row))
        
        src_user_rows = target_user_row[1:]        
        
        target_user_row = target_user_row[0].reshape(1, -1)
        
        similarity = cosine_similarity(target_user_row, src_user_rows)
        
        high_similarity_arg_list = np.argsort(similarity[0])[::-1][:10]        
        #src_userID = user_pivot_table.iloc[high_similarity_arg_list[0]]["userId"]
        src_userId = user_pivot_table.iloc[high_similarity_arg_list[0]]
        
        target_users_movies = pd.merge(left=filtered_ratings.loc[filtered_ratings["userId"] == target_userId], right=self.movies, on="movieId").loc[:, ["userId", "movieId", "title", "rating"]]
        src_users_movies = pd.merge(left=filtered_ratings.loc[filtered_ratings["userId"] == src_userId], right=self.movies, on="movieId").loc[:, ["userId", "movieId", "title", "rating"]]
        
        #duplicated_movie_ids = pd.merge(left=target_users_movies, right=src_users_movies, on="movieId")["movieId"]        
        recommended_movie_ids = list(set(src_users_movies["movieId"]) - set(target_users_movies["movieId"]))        
        recommended_movies = src_users_movies.loc[src_users_movies["movieId"].isin(recommended_movie_ids)]
        
        # * target_user_row denotes genre preferences
        #return recommended_movies.sort_values(by="rating", ascending=False)[["movieId", "title", "rating"]]
        return recommended_movies.sort_values(by="rating", ascending=False)[["movieId", "title"]]
        
        
if __name__ == "__main__":
    rec_sys = RecSys()
    filtered_userIds, filtered_ratings = rec_sys.filter_out_users()
    target_userId, src_userId_array = rec_sys.sample_bounded_userId(filtered_userIds)
    
    recommended_movies = rec_sys.operate_rec_sys(filtered_ratings, target_userId, src_userId_array)
    
    print(recommended_movies)
    