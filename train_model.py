import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

df = pd.read_csv("dataset/student_scores.csv")

print(df)

print(df.head())

print(df.info())

print(df.describe())

X = df[["Hours"]]
y = df["Score"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train,y_train)

predictions = model.predict(X_test)

print(predictions)

mae = mean_absolute_error(y_test,predictions)

print(mae)

pickle.dump(model,open("model/exam_model.pkl","wb"))


