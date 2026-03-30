 Human Activity Recognition using machine learning
 

this is my first machine learning project 

## 📌 Project Overview

This project focuses on **Human Activity Recognition (HAR)** using smartphone sensor data. The goal is to classify human activities such as walking, sitting, standing, and laying based on signals collected from mobile sensors like accelerometers and gyroscopes.

Human Activity Recognition is widely used in:

* Fitness tracking 📱
* Health monitoring 🏥
* Smart devices 🤖
* Surveillance systems 🎥

---

## 📊 Dataset Information

The dataset contains sensor readings collected from smartphones. It includes:

* Total Features: **561**
* Data Types: Mostly numerical (float values)
* Activities:

  * WALKING
  * WALKING_UPSTAIRS
  * WALKING_DOWNSTAIRS
  * SITTING
  * STANDING
  * LAYING

The dataset is divided into:

* `train.csv` → Training data
* `test.csv` → Testing data

---

## ⚙️ Technologies Used

* Python 🐍
* Pandas (Data handling)
* NumPy (Numerical operations)
* Matplotlib & Seaborn (Visualization)
* Scikit-learn (Machine Learning)

---

## 🔄 Project Workflow

### 1️⃣ Data Loading

The dataset is loaded using pandas:

* Train and test data are read from CSV files
* Both datasets are merged for preprocessing

---

### 2️⃣ Data Preprocessing

* Removed unnecessary columns like `subject` and `Data`
* Converted labels into proper format
* Checked missing values and unique values

---

### 3️⃣ Feature Scaling

Standardization is applied using **StandardScaler**:

* Ensures all features have equal importance
* Improves model performance

---

### 4️⃣ Dimensionality Reduction (PCA)

* PCA is used to reduce feature size from 561 to fewer components
* Retains **90% variance**
* Helps in reducing noise and computation time

---

### 5️⃣ Model Training

We used **K-Nearest Neighbors (KNN)** algorithm:

* Number of neighbors = 8
* Distance metric = Manhattan (p=1)
* Weighted by distance

---

### 6️⃣ Model Evaluation

* Accuracy Score
* Confusion Matrix
* Classification Report

---

## 📈 Results

* ✅ Accuracy: **95%**
* High precision and recall across all activity classes

### Sample Output:

* WALKING → Highly accurate
* SITTING → Slight confusion with standing
* LAYING → Perfect classification

---

## 📉 Visualization

* Bar graph for activity distribution
* Heatmap for confusion matrix

---

## 🚀 How to Run the Project

1. Install dependencies:

```
pip install pandas numpy matplotlib seaborn scikit-learn
```

2. Run the script:

```
python main.py
```

---

## 📂 Project Structure

```
Human-Activity-Recognition/
│── main.py
│── train.csv
│── test.csv
│── README.md
│── requirements.txt
```

---

## 💡 Future Improvements

* Implement Deep Learning models (LSTM, CNN)
* Try Random Forest and SVM
* Deploy as a web app 🌐
* Real-time activity recognition using mobile sensors

---

## 👨‍💻 Author

name sachin kumar

---

## ⭐ Conclusion

This project demonstrates how machine learning can be used to analyze sensor data and accurately predict human activities. It highlights the importance of preprocessing, feature engineering, and model selection in achieving high performance.
