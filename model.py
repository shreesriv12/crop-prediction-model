# import pandas as pd
# from sklearn.preprocessing import StandardScaler
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split
import pickle
# #
# # Load the csv file
# df = pd.read_csv("Crop_recommendation.csv")
# #
# print(df.head())
#
# X = df[["N", "P", "K", "temperature","humidity","ph","rainfall"]]
# y = df["label"]
#
# # Split the dataset into train and test
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=50)
#
# # Feature scaling
# sc = StandardScaler()
# X_train = sc.fit_transform(X_train)
# X_test= sc.transform(X_test)
#
# # Instantiate the model
# classifier = RandomForestClassifier()
#
# # Fit the model
# classifier.fit(X_train, y_train)
#
# # Make pickle file of our model
# pickle.dump(classifier, open("model.pkl", "wb"))

# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv('Crop_recommendation.csv')  # Replace 'crop_data.csv' with your dataset file
X = data.iloc[:, :-1]  # Features
y = data.iloc[:, -1]   # Labels
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)
pickle.dump(model, open("model.pkl", "wb"))
