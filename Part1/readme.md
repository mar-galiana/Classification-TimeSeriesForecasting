# PART 1: DIABETES CLASSIFICATION

## Project explanation

Choose an open classification dataset other than Iris. In a Jupyter notebook you have to do all the exploratory analysis, preprocessing, visualisations and test the models you think appropriate. Once this is done, you choose the model that works best for you according to the metrics you have chosen.

With the conclusions of this notebook you have to create the files for production. That is to say, the Python files that you would pass to a DevOps to put in production.

***
In this project, I have chosen a dataset that classifies whether a patient has diabetes or not. The dataset can be downloaded from the following webpage: https://www.kaggle.com/datasets/mathchi/diabetes-data-set.

The dataset contains the following information:

* Pregnancies: Number of times pregnant
* Glucose: Plasma glucose concentration 2 hours after an oral glucose tolerance test
* BloodPressure: Diastolic blood pressure (mm Hg)
* SkinThickness: Triceps skinfold thickness (mm)
* Insulin: 2-Hour serum insulin (mu U/ml)
* BMI: Body mass index (weight in kg/(height in m)^2)
* DiabetesPedigreeFunction: Diabetes pedigree function
* Age: Age (years)
* Outcome: Class variable (0 or 1)


After studying the state-of-the-art, a paper was discovered that used the same dataset and had a similar goal to this project. The paper titled "Prediction of Diabetes Using Machine Learning Algorithms in Healthcare" by Azeem et al. can be found at the following link: https://ieeexplore.ieee.org/abstract/document/8748992.

In the paper, the accuracy metric was used to assess the model's performance. However, this metric may not be the most appropriate choice for an imbalanced dataset like ours, especially when dealing with a medical condition. To address this concern, we calculated the fbeta score metric based on the paper's confusion matrix, which allows us to penalize false negative results over false positive ones. The attached Excel file contains the calculation of an fbeta score metric based on their confusion matrix and the beta value can be modified to observe variations in the final results.

This project identifies the four best models reported by the Azeem et al. paper (highlighted in yellow in the Excel file) and implements them using various data processing techniques to improve the results.

The Jupyter notebook consists of five main sections:

1. Process dataset: In this section, I load, scale, oversample, and split the dataset into three different sets: train (80%), test (20%), and validation (20%). I test several scaling methods, including StandardScaler, MinMaxScaler, MaxAbsScaler, and RobustScaler. To address the imbalanced dataset issue, I apply the oversampling technique using SMOTE.

2. Train model: In this section, I define and train different models using the training set. The models compared are: Logistic Regression (LR), Naive Bayes (NB), K-Nearest Neighbors (KNN), and Support Vector Machine (SVM).

3. Evaluate model: This section evaluates the model using the testing set and the fbeta score. The fbeta score is chosen as the metric due to the dataset's imbalance and its medical prediction application. In medical predictions, false negatives need to be penalized to avoid missing patients with the disease. The beta constant, initially set to 3, can be modified.

4. Optimization: This section aims to identify the best configuration parameters for each model and preprocessing technique by performing parameter tuning using GridSearch.

5. Show results: In this section, I present all the tests performed and the fbeta score results obtained using the test set. The best results are achieved using Logistic Regression with MaxAbsScaler data processing and oversampling of the test and validation datasets (since the validation set is used for optimization). The selected parameters are {'C': 0.1, 'penalty': 'l2', 'solver': 'liblinear'}, resulting in an fbeta score of 84.6% (with only 5 false negative predictions out of 154 total samples). This model increased its performance by a 17.46% compared to the previous paper by Azeem et al. using SVM with the same dataset.

Currently, all models are implemented using sklearn, but there are several ways to enhance their accuracy. One effective method is to re-implement the models using PyTorch, allowing us to fine-tune each parameter for better performance.

The project demonstrates the successful application of various models and data processing techniques to achieve improved predictive performance in diabetes classification.
***


# Project Set Up

To set up the project, follow these steps:

1. Download the dataset Excel file from the following link: https://www.kaggle.com/datasets/mathchi/diabetes-data-set/download?datasetVersionNumber=1

2. Rename the dataset file as stated in the DATASET_CSV_FILE variable in the constants.py file.

3. Install the required dependencies by executing the following command in the terminal:

````
pip install -r requirements.txt
````

4. Execute the Jupyter notebook and review the outputs to understand the results.
