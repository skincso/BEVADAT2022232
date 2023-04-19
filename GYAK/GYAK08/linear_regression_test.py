from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from LinearRegressionSkeleton import LinearRegression
import pandas as pd

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

#X = df['petal length (cm)'].values
#y = df['petal width (cm)'].values

X = df['petal length (cm)'].values
y = df['petal width (cm)'].values

# train_test_split()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
pred = lin_reg.predict(X_test)
#print(pred)