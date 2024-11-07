# Assignment-AI-ML  

pip install IMDbPy   

Run the **WebScrapigScript**


**#Problem-2**

START

# Step 1: Data Preprocessing
LOAD Kepler dataset
REMOVE non-informative columns (e.g., IDs)
SELECT relevant numerical features as X
ENCODE target labels (koi_disposition) to numerical as y
IMPUTE missing values in X with median
SPLIT X and y into training and testing sets

# Step 2: Define Models
INITIALIZE Logistic Regression, Decision Tree, and Random Forest

# Step 3: Train and Evaluate Models
FOR each model in [Logistic Regression, Decision Tree, Random Forest]:
    TRAIN model on X_train and y_train
    PREDICT on X_test to get y_pred
    CALCULATE metrics (Accuracy, Precision, Recall, F1 Score)
    PERFORM 5-fold cross-validation on X_train
    PRINT or STORE metrics

# Step 4: Select the Best Model
COMPARE models based on evaluation metrics
CHOOSE model with highest performance

# Step 5: Final Model Deployment
USE selected model for future predictions if needed
SAVE model if necessary

END


**1. Why did you choose the particular algorithm?**
I chose Logistic Regression for simplicity, Decision Tree for handling complex patterns, and Random Forest because it combines trees for higher accuracy and handles complex data well.

**2. What are the different tuning methods used for the algorithm?**
Grid Search and Randomized Search for finding the best settings, k-fold Cross-Validation to test stability, and Regularization to prevent overfitting in Logistic Regression.

**3. Did you consider any other choice of algorithm? Why or why not?**
Yes, I considered SVM (computationally heavy) and k-NN (slow with large data). I skipped them to keep it efficient and manageable.

**4. What is the accuracy?**
Likely around 85-90%, depending on data split and tuning.

**5. What are the different types of metrics that can be used to evaluate the model?**
Accuracy shows overall correctness, Precision and Recall for focus on positives, F1 Score as a balance, and AUC-ROC for binary classification performance. Each adds a different perspective on how well the model performs.



