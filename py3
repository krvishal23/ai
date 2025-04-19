from sklearn.ensemble import IsolationForest

# Assuming X_train and X_test are your feature datasets for training and testing
# 'contamination' is the proportion of outliers in the data (adjust based on your dataset)
iso_forest = IsolationForest(contamination=0.01, random_state=42)

# Fit the IsolationForest model on the training data
iso_forest.fit(X_train)

# Predict anomalies in the test data
anomalies = iso_forest.predict(X_test)

# Convert anomalies output to a more readable format (1 for normal, -1 for anomaly)
anomalies = ['Anomaly' if x == -1 else 'Normal' for x in anomalies]

# Print the predicted anomalies
print(anomalies)
