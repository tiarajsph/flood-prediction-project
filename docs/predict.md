with open('flood-model.pkl', 'rb') as file:
    clf = pickle.load(file)

def predict_flood(data):
    # Convert input data to a Pandas DataFrame
    df = pd.DataFrame(data)

    # Make predictions using the trained model
    prediction = clf.predict(df)

    # Map the prediction to a label (e.g., 'NO' or 'YES')
    label_mapping = {0: 'NO', 1: 'YES'}
    prediction_label = label_mapping[prediction[0]]

    return prediction_label