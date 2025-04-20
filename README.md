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

Phase 1: Data Ingestion
Modular ingestion system that:
* **Data Retrieval**: Reads raw phishing data directly from MongoDB Atlas
* **Local Backup**: Saves a copy of the raw data locally for version control and reproducibility
* **Data Splitting**: Automatically splits the data into training and testing sets for downstream ML tasks

Phase 2: Data Validation
Modular validation system that:
* **Schema Check**: Verifies that the number of columns in the raw data matches the expected structure defined in schema.yaml

* **Data Drift Detection**: Automatically detects distribution shifts between training and testing datasets using a drift threshold of 0.05