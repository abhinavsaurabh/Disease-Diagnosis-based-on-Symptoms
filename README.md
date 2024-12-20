
# Disease Diagnosis Based on Symptoms

This project leverages Machine Learning (ML) and Information Retrieval (IR) techniques to detect diseases based on user-inputted symptoms. It provides detailed information about the top predicted diseases, including treatment recommendations.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
  - [TF-IDF Interaction](#tf-idf-interaction)
  - [Machine Learning Interaction](#machine-learning-interaction)
- [Results](#results)
- [Contributors](#contributors)
- [License](#license)

## Introduction

Early and accurate disease diagnosis is crucial for effective treatment. This project utilizes both ML and IR methods to predict potential diseases from a given set of symptoms, aiming to assist in early detection and provide relevant treatment information.

## Features

- **Symptom Input**: Users can input a combination of symptoms.
- **Disease Prediction**: The system predicts possible diseases based on the input symptoms.
- **Treatment Recommendations**: Provides information on treatment options for the predicted diseases.
- **Two Approaches**:
  - **TF-IDF Cosine Similarity**: Uses term frequency-inverse document frequency and cosine similarity for disease prediction.
  - **Machine Learning Models**: Implements various ML algorithms for prediction.

## Dataset

The dataset includes records of diseases and their associated symptoms.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/abhinavsaurabh/Disease-Diagnosis-based-on-Symptoms.git
   cd Disease-Diagnosis-based-on-Symptoms
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### TF-IDF Interaction

1. **Files Required**:
   - `combination (3).csv`
   - `cosine_results.py`
   - `generatesymptoms.py`
   - `Interaction_TF_IDF_Cosine.ipynb`
   - `normal (3).csv`
   - `synonyms.py`
   - `tf_idf_result.py`
   - `tokenizer.py`

2. **Instructions**:
   - Ensure all the above files are in the same directory.
   - Open and run `Interaction_TF_IDF_Cosine.ipynb` sequentially in a Jupyter Notebook environment.
   - For Google Colab users, upload all the files in the same runtime session and execute the notebook.

### Machine Learning Interaction

1. **Files Required**:
   - `combinational (3).csv`
   - `decisionT.py`
   - `IRadaboost.py`
   - `IRgdb.py`
   - `IRsvm.py`
   - `IRxgb.py`
   - `knneigbh.py`
   - `LR.py`
   - `mnb.py`
   - `multiLP.py`
   - `normal (3).csv`
   - `randomrf.py`
   - `synonyms.py`
   - `IR_final_ML_interaction_.ipynb`

2. **Instructions**:
   - Place all the listed files in the same directory.
   - Open and execute `IR_final_ML_interaction_.ipynb` sequentially in Jupyter Notebook.
   - For Colab users, upload all files in the same runtime session before running the notebook.

## Results

The performance of various models is as follows:

| Model                     | Accuracy (%) |
|---------------------------|--------------|
| Multi-Layer Perceptron    | 89.42        |
| Decision Tree             | 72.62        |
| Random Forest             | 89.97        |
| Logistic Regression       | 89.88        |
| K-Nearest Neighbour       | 89.97        |
| Support Vector Machine    | 87.99        |
| Multinomial Naive Bayes   | 81.30        |
| Gradient Boosting Machine | 80.94        |
| Extreme Gradient Boosting | 78.83        |

## Contributors

- [Abhinav Saurabh](https://github.com/abhinavsaurabh)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
