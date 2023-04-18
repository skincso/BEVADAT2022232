from matplotlib import pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split


class LinearRegression:
    def __init__(self, epochs: int = 1000, lr: float = 1e-3):
        self.epochs = epochs
        self.lr = lr


    def fit(self, X: np.array, y: np.array):
        # Building the model
        self.m = 0
        self.c = 0

        #L = 0.0001  # The learning Rate
        #epochs = 1000  # The number of iterations to perform gradient descent

        n = float(len(X)) # Number of elements in X

        # Performing Gradient Descent 
        losses = []
        for i in range(self.epochs): 
            y_pred = self.m*X + self.c  # The current predicted value of Y

            residuals = y_pred - y
            loss = np.sum(residuals ** 2)
            losses.append(loss)
            D_m = (-2/n) * sum(X * residuals)  # Derivative wrt m
            D_c = (-2/n) * sum(residuals)  # Derivative wrt c
            self.m = self.m + self.lr * D_m  # Update m
            self.c = self.c + self.lr * D_c  # Update c
            if i % 100 == 0:
                print(np.mean(y - y_pred))

        #plt.plot(losses)

        # Run the model on the test set
        pred = []
        for x in X:
            y_pred = self.m*x + self.c
            pred.append(y_pred)
        print(pred)
        print(y)


    def predict(self, X, y):
        y_pred = self.m*X + self.c

        plt.scatter(X, y)
        plt.plot([min(X), max(X)], [min(y_pred), max(y_pred)], color='red') # predicted
        plt.show()
