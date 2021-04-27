from joblib import load
import numpy as np
import os

# Load the RandomForestRegression model
# import pickle
#filename = 'randomForest-model.pkl'
#regressor = pickle.load(open(filename, 'rb'))

# Load the RandomForestRegression Model
forest = load(os.path.join(os.getcwd(), 'utilities', 'randomForest-model.pkl'))

def predict_score(batting_team, bowling_team, venue, runs, wickets, overs, runs_last_5, wickets_last_5):
    prediction_array = []

    # Batting Team
    if batting_team == 'Chennai Super Kings':
        prediction_array = prediction_array + [1, 0, 0, 0, 0, 0, 0, 0]
    elif batting_team == 'Delhi Daredevils':
        prediction_array = prediction_array + [0, 1, 0, 0, 0, 0, 0, 0]
    elif batting_team == 'Kings XI Punjab':
        prediction_array = prediction_array + [0, 0, 1, 0, 0, 0, 0, 0]
    elif batting_team == 'Kolkata Knight Riders':
        prediction_array = prediction_array + [0, 0, 0, 1, 0, 0, 0, 0]
    elif batting_team == 'Mumbai Indians':
        prediction_array = prediction_array + [0, 0, 0, 0, 1, 0, 0, 0]
    elif batting_team == 'Rajasthan Royals':
        prediction_array = prediction_array + [0, 0, 0, 0, 0, 1, 0, 0]
    elif batting_team == 'Royal Challengers Bangalore':
        prediction_array = prediction_array + [0, 0, 0, 0, 0, 0, 1, 0]
    elif batting_team == 'Sunrisers Hyderabad':
        prediction_array = prediction_array + [0, 0, 0, 0, 0, 0, 0, 1]

    # Bowling Team
    if bowling_team == 'Chennai Super Kings':
        prediction_array = prediction_array + [1, 0, 0, 0, 0, 0, 0, 0]
    elif bowling_team == 'Delhi Daredevils':
        prediction_array = prediction_array + [0, 1, 0, 0, 0, 0, 0, 0]
    elif bowling_team == 'Kings XI Punjab':
        prediction_array = prediction_array + [0, 0, 1, 0, 0, 0, 0, 0]
    elif bowling_team == 'Kolkata Knight Riders':
        prediction_array = prediction_array + [0, 0, 0, 1, 0, 0, 0, 0]
    elif bowling_team == 'Mumbai Indians':
        prediction_array = prediction_array + [0, 0, 0, 0, 1, 0, 0, 0]
    elif bowling_team == 'Rajasthan Royals':
        prediction_array = prediction_array + [0, 0, 0, 0, 0, 1, 0, 0]
    elif bowling_team == 'Royal Challengers Bangalore':
        prediction_array = prediction_array + [0, 0, 0, 0, 0, 0, 1, 0]
    elif bowling_team == 'Sunrisers Hyderabad':
        prediction_array = prediction_array + [0, 0, 0, 0, 0, 0, 0, 1]

    # Venue
    if venue == 'Dr DY Patil Sports Academy':
        prediction_array = prediction_array + [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif venue == 'Eden Gardens':
        prediction_array = prediction_array + [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    elif venue == 'Feroz Shah Kotla':
        prediction_array = prediction_array + [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    elif venue == 'M Chinnaswamy Stadium':
        prediction_array = prediction_array + [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    elif venue == 'MA Chidambaram Stadium, Chepauk':
        prediction_array = prediction_array + [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
    elif venue == 'Punjab Cricket Association Stadium, Mohali':
        prediction_array = prediction_array + [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    elif venue == 'Rajiv Gandhi International Stadium, Uppal':
        prediction_array = prediction_array + [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
    elif venue == 'Sawai Mansingh Stadium':
        prediction_array = prediction_array + [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
    elif venue == 'Subrata Roy Sahara Stadium':
        prediction_array = prediction_array + [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    elif venue == 'Wankhede Stadium':
        prediction_array = prediction_array + [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

    prediction_array = prediction_array + [overs, runs, wickets, runs_last_5, wickets_last_5]
    prediction_array = np.array([prediction_array])
    pred = forest.predict(prediction_array)
    #pred = int(forest.predict(prediction_array)[0])
    #return pred
    return int(round(pred[0]))


