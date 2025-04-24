### 🛡️ Network Security Project: Phishing Data Analysis

This project lays the groundwork for analyzing phishing-related network data with a focus on security and reliability.

#### ✅ Key Features Implemented:

---

#### 🧠 Intelligent Logging & Exception Handling
To enhance debugging and maintainability, the project begins with a robust logging and exception handling setup. This system ensures:

- Clear identification of error types  
- Precise traceback with file name and line number  
- Informative and structured runtime diagnostics  

---

#### 🛠️ ETL Pipeline 

A basic ETL (Extract, Transform, Load) pipeline has been developed to manage the initial dataset:

- **Extract**: Read phishing data from a local CSV file  
- **Transform**: Convert tabular data into JSON format suitable for database ingestion  
- **Load**: Push the cleaned data into **MongoDB Atlas** for scalable cloud-based storage  

📥 Phase 1: Data Ingestion
Modular ingestion system that:
* **Data Retrieval**: Reads raw phishing data directly from **MongoDB Atlas**
* **Local Backup**: Saves a copy of the raw data locally for version control and reproducibility
* **Data Splitting**: Automatically splits the data into **training** and **testing** sets for downstream ML tasks

📊 Phase 2: Data Validation
Modular validation system that:
* **Schema Check**: Verifies that the number of columns in the raw data matches the expected structure defined in `schema.yaml`
* **Data Drift Detection**: Automatically detects distribution shifts between training and testing datasets using a drift threshold of `0.05`

🧪 Phase 3: Data Transformation
A structured transformation pipeline to prepare the data for machine learning:
* **Target Normalization**: Converts the target values from `-1` to `0` to ensure consistency (`0` and `1` as binary labels)
* **Missing Value Handling**: Uses **KNNImputer** to fill missing data based on feature similarity
* **Pipeline Integration**: All transformation steps are wrapped in a pipeline for reusability and consistency
* **Output Generation**: Saves the transformed training and testing data as NumPy `.npy` files for efficient storage and fast loading

🚀 **Phase 4: Model Training**  
A robust training pipeline built for experimentation, optimization, and tracking:  
* **Model Variety**: Evaluated multiple ML algorithms including  
  `Random Forest`, `Decision Tree`, `Gradient Boosting`, `Logistic Regression`, and `AdaBoost`  
* **Hyperparameter Tuning**: Employed **GridSearchCV** with 3-fold cross-validation to identify the best model configurations  
* **Performance Metrics**: Assessed models using `F1 Score`, `Precision`, and `Recall` for balanced evaluation on imbalanced data  
* **Experiment Tracking**: Integrated **MLflow** and **DagsHub** to track experiments, metrics, and parameters seamlessly  
* **Results**: Best model achieved outstanding performance on the test set:  
  - **Recall**: 0.988  
  - **Precision**: 0.979  
  - **F1 Score**: 0.984  

