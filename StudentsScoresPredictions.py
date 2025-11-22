


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import seaborn as sns


df = pd.read_csv("student_scores.csv")

print("First 5 rows of data:")
print(df.head())

print("\nShape of dataset:", df.shape)
print("\nColumn names:", df.columns.tolist())


print("\nMissing values per column:")
print(df.isna().sum())


plt.figure(figsize=(7,5))
plt.scatter(df["Hours"], df["Score"], color='blue')
plt.title("Hours vs Score")
plt.xlabel("Hours Studied")
plt.ylabel("Score")
plt.show()


target = 'Score'
y = df[target]           
X = df.drop(columns=['Score'])  


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("\nModel Evaluation:")
print(f"R² Score: {r2:.3f}")
print(f"RMSE: {rmse:.3f}")


plt.figure(figsize=(8,6))
sns.scatterplot(x=y_test, y=y_pred, color='orange', s=60)
plt.xlabel("Actual Scores")
plt.ylabel("Predicted Scores")
plt.title("Actual vs Predicted Student Scores")
plt.show()


plt.figure(figsize=(7,5))
plt.scatter(df["Hours"], df["Score"], label='Actual', color='blue')
plt.plot(df["Hours"], model.predict(df[["Hours"]]), color='red', label='Regression Line')
plt.xlabel("Hours Studied")
plt.ylabel("Score")
plt.title("Regression Line: Hours vs Score")
plt.legend()
plt.show()
