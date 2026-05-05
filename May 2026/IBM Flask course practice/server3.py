''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''

# Import Flask, render_template, request from the flask pramework package 

# Import the sentiment_analyzer function from the package created

from flask import Flask, render_template, request

from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

#Initiate the flask app 

app = Flask(__name__)

@app.route("/sentimentAnalyzer")
def sent_analyzer():

    text_to_analyze = request.args.get('textToAnalyze')
    
    response = sentiment_analyzer(text_to_analyze)

    label = response['label']
    score = response['score']

    if label is None:

        return "Invalid input try again!"
    
    return f'The given text has been identified as {label} with a score of {score}'
    
@app.route("/")
def render_index_page():
    return render_template("index.html")
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
