# Flyguesser 
ML model that predicts the flight price using regression based algorithms and help users to look for optimal time and prices to book flight tickets.

Link: [https://flyguesser.herokuapp.com/](https://flyguesser.herokuapp.com/)

[![](https://i.imgur.com/4VSHxE9.png?1)](https://flyguesser.herokuapp.com/)

## Inspiration
Nowadays, airline ticket prices can vary dynamically for the same flight. Customers are seeking to get the lowest price while airlines are trying to keep their overall revenue as high as possible and maximize their profit. Airlines use various kinds of computational techniques to increase their revenue such as demand prediction and price discrimination. 

This is a Flask web app that predicts the ticket price so that customer can find optimal time and prices to book flight tickets.

## Installation
The Code is written in Python 3.6.10. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```

## Dataset

 - [Dataset Link](https://www.kaggle.com/nikhilmittal/flight-fare-prediction-mh)


## Deployement on Heroku
Login or signup in order to create virtual app. You can either connect your github profile or download CLI to manually deploy this project.

[![](https://i.imgur.com/dKmlpqX.png)](https://heroku.com)

create new app and provide an unique app name. This name will be depicted in the url of your app.

1. To deploy using Heroku Git:
Download and install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), and run these commands
```bash
    heroku login
```
```bash
    cd <go-to-your-project-directory>/
```
```bash
    git init
```
```bash
    heroku git:remote -a <add-your-app-name>
```
```bash
    git add .
```
```bash
    git commit -am "make it better"
```
```bash
    git push heroku master
```
2. To deploy using github:
Connect this app to GitHub and search for a repository to connect to. Then choose between automatic or manual deployment. Heroku will start building the app and satisfying the requirements from requirements.txt

## Directory Tree 
```
├── static/css 
│   ├── styles.css
├── templates
│   ├── home.html
├── Data_train.xlsx
├── Procfile
├── README.md
├── app.py
├── flight_price.ipynb
├── flight_rf.pkl
├── requirements.txt
```

## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)[<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=170>](https://flask.palletsprojects.com/en/1.1.x/) [<img target="_blank" src="https://number1.co.za/wp-content/uploads/2017/10/gunicorn_logo-300x85.png" width=280>](https://gunicorn.org) [<img target="_blank" src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" width=200>](https://scikit-learn.org/stable/) [<img target="_blank" src="https://miro.medium.com/max/792/1*lJ32Bl-lHWmNMUSiSq17gQ.png" width=170>](https://developer.mozilla.org/en-US/docs/Web/HTML)[<img target="_blank" src="https://images.g2crowd.com/uploads/product/image/social_landscape/social_landscape_bf0fb4cb7fe948c42f37ded73895638f/salesforce-heroku.png" width=170>](https://en.wikipedia.org/wiki/Heroku)
