![photo-1573710459621-bb101783ca0f](https://user-images.githubusercontent.com/92402366/151297669-4d457f28-5c53-4604-803f-f4c755faabd8.jpg)

# Capstone Project
## Used and New Car Price Predictor
Wordsmith/Coder: Roger Pineda
## Overview
The project here has sought out to go and predict the price of used and new cars from a dataset that had over four hundred thousand car listings from craigslist with the use of a variety of regression algorithms. Many features of the car were used to attempt to accurately predict the price.
## Business Problem
Figuring out what to sell your car is something people don't know off the top of their head. With the sky rocketing prices many are looking to sell their vehicle at the right price. Knowing that price is tough. Vice versa when it comes to buying a car. You don't want to over pay for something that may lose value quickly. Therefore this model was created to aid those car buyers and sellers.
## Data Understanding
The dataset is from Kaggle and it is currently over 1.5g of space and therefore too big to be pushed to GitHub. The link to the dataset will be at the bottom of this Read.ME
## Data Cleaning
The data started with four hundred thirty thousand car listings from craigslist and was saved in a in a csv file. This dataset ended up having over 1.6 million missing cells of data and therefore had to be either removed or filled in by data within the dataset already. In the end the cleaned dataset was left with only one hundred fifty thousand listings. 
## Modeling
For the modeling portion of this repo you have to go into the modeling note book to see all the work and coding that was needed to properly predict the price of any vehicle.
The modeling algorithms used were as follows
* Linear Regression
* Lasso Regression
* Ridge Regression
* XG Boost Regression
* Random Forest Regression
* Neural Network Regression

Final Model
* Random Forest Regessor

The Random Forest Regressor came to be the final model since it had the lowest RSME score out all the models used in this repo. When it comes to regression and predicting price the most important metric is RSME score be as low as possible.

![Screenshot 2022-01-27 010123](https://user-images.githubusercontent.com/92402366/151300955-8a29899e-7667-4c87-957d-4d828143a308.png)

## Deployment
An app that is currently only able to run locally has been created for users to go out and figuree out what their cars value is or what they could possibly buy a vehicle for.
All the required packages to run the app correctly are stored within the required folder in the main part of this repo. The app is stored in the app.py file.
## Conclusions and Next Steps
After many forms and attempts and clean this heavily mucky dataset from Kaggle it is come down that what was left over wasn't enough to allow the models to trainwell enough to acheive proper predictions. As seen in the predictions section of this notebook, the model isn't predicting well to new data. When given all the features in the datset it vastly underperforms. With the model having an RSME of 3724.54 it is way to high of a number in reference to the range of the values of the prices within the dataset. The model can either predict well over the price therefore having the buyer spend way too much for a car or way too low and having the seller lose out on profits. Currently the model needs more work and it is currently not in a position to be used by the public. 

Next steps are to use find stronger regressors to use on the data and also to see if the removing of features can fine tune the model to see if it can be more accurate. As well grab far more computing power.

## Links
[Kaggle Dataset](https://www.kaggle.com/austinreese/craigslist-carstrucks-data)

[Article on Regressors](https://www.jigsawacademy.com/popular-regression-algorithms-ml/#Neural-Network-Regression-)

Presentation

## Repository Structure
```
├── [gitignore]
├── Final_Notebook.ipynb
├── Modeling_Notebook.ipynb
├── ProcFile 
├── README.md
├── app.py
├── [data]
├── required.txt 
└── setup.sh
 
```
