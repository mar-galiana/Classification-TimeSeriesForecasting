# PART 2: MULTIVARIANT TIME SERIE

## Project explanation
This project involves the analysis of a dataset obtained from Kaggle, specifically from the "Wind Speed Prediction Dataset" available at https://www.kaggle.com/datasets/fedesoriano/wind-speed-prediction-dataset.

The main objective of this exercise is to implement a model which will predict the wind speed for the next 100 instances using historical data. For this task, I have chosen the LSTM (Long Short-Term Memory) model, which has demonstrated remarkable performance in handling multivariate time series data, making it suitable for the needsof this exercice.


The primary goal of this exercise is to develop a model capable of predicting wind speeds for the next 100 instances using historical data. For this task, we have chosen the LSTM (Long Short-Term Memory) model, which has demonstrated remarkable performance in handling multivariate time series data, making it suitable for our needs.

# Project Set Up

To set up the project, follow these steps:

1. Download the dataset Excel file from the following link: https://www.kaggle.com/datasets/fedesoriano/wind-speed-prediction-dataset/download?datasetVersionNumber=1.

2. Rename the dataset file as stated in the DATA_FILE variable in the constants.py file.

3. Install the required dependencies by executing the following command in the terminal:

````
pip install -r requirements.txt
````

4. Execute the Jupyter notebook and review the outputs to understand the results.

After running the Jupyter notebook, an Excel file will be generated with the predictions for the next 100 instances on the left, and the corresponding correct values on the right. This allows for accurate evaluation and understanding of the model's performance.
