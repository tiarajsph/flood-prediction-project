import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import pickle
df = pd.read_csv('kerala-flood.csv') 
X = df.drop(columns=['YEAR','FLOODS'])
y = df['FLOODS']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)


print("Classification Report:")
print(classification_report(y_test, y_pred))

print("Accuracy Score:")
print(accuracy_score(y_test,y_pred))
label_mapping = {0: 'NO', 1:'YES'}
new_data = pd.DataFrame({
    'JAN': [10.3],
    'FEB': [0],
    'MAR': [30.1],
    'APR': [141.5],
    'MAY': [169.4],
    'JUN': [657.5],
    'JUL': [450.7],
    'AUG': [285.5],
    'SEP': [271.1],
    'OCT': [308.0],
    'NOV': [92.9],
    'DEC': [5.6],
    ' ANNUAL RAINFALL':[2422.7]
})
prediction = clf.predict(new_data)
prediction_label = label_mapping[prediction[0]]
print(f"Predicted Flood Status: {prediction_label}")

# Save the trained model to a file
with open('flood-model.pkl', 'wb') as file:
    pickle.dump(clf, file)
