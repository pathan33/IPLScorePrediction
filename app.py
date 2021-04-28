# Importing necessary Libraries
from flask import Flask, request, url_for, render_template
from utilities import predict
from utilities.predict import predict_score
from utilities.predict import forest

# Setting up the application
app = Flask(__name__)

TEAM_CODE = [
                'Chennai Super Kings',
				'Delhi Capitals',
				'Kings XI Punjab',
				'Kolkata Knight Riders',
				'Mumbai Indians',
				'Rajasthan Royals',
				'Royal Challengers Bangalore',
				'Sunrisers Hyderabad'
             ]

Venue = [
			'Dr DY Patil Sports Academy',
			'Eden Gardens',
			'Feroz Shah Kotla',
			'M Chinnaswamy Stadium',
			'MA Chidambaram Stadium, Chepauk',
			'Punjab Cricket Association Stadium, Mohali',
			'Rajiv Gandhi International Stadium, Uppal',
			'Sawai Mansingh Stadium',
			'Subrata Roy Sahara Stadium',
			'Wankhede Stadium'
        ]

predict_score = None

# making route
@app.route('/')
def home():
    return render_template('index.html',teams=TEAM_CODE, venue = Venue, score=predicted_score)

@app.route('/predict', methods=['GET', 'POST'])
def prediction():
	global predicted_score

	if request.method == 'POST':
		req = request.form()

		batting_team = req['batting_team']
		bowling_team = req['bowling_team']
		venue = req['venue']
		runs = int(req['runs'])
		overs = float(req['overs'])
		wickets = int(req['wickets'])
		runs_last_5 = int(req['runs_last_5'])
		wickets_last_5 = int(req['wickets_last_5'])

		predicted_score = predict_score(batting_team, bowling_team, venue, runs, wickets, overs, runs_last_5, wickets_last_5)
		return render_template('predict.html', lower_limit=predicted_score - 10, upper_limit=predicted_score + 5, info=dict(req))
	else:
		return render_template('404.html', msg="500 No Prediction: Looks like you're here without a prediction.")

@app.errorhandler(404)
def error(e):
	return render_template('404.html', msg=e)

# running application
if  __name__ == '__main__':
    app.run(debug=True)
