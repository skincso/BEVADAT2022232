import pandas as pd
from typing import Tuple
from scipy.stats import mode
import seaborn as sns
from sklearn.metrics import confusion_matrix

class KNNClassifier:

    @property
    def k_neighbors(self):
        return self.k
    
    def  __init__(self, k: int, test_split_ratio: float) -> None:
        self.k = k
        self.test_split_ratio = test_split_ratio

    @staticmethod
    def load_csv(csv_path: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
        df = pd.read_csv(csv_path, delimiter=',')
        df_shuffled = df.sample(frac=1, random_state=42)
        x, y = df_shuffled.iloc[:,:-1], df_shuffled.iloc[:,-1]
        return x, y
    
    def train_test_split(self, features: pd.DataFrame,
                     labels: pd.DataFrame) -> None:
        test_size = int(len(features) * self.test_split_ratio)
        train_size = len(features) - test_size
        assert len(features) == test_size + train_size, "Size mismatch!"

        x_train, y_train = features.iloc[:train_size, :], labels.iloc[:train_size]
        x_test, y_test = features.iloc[train_size:, :], labels.iloc[train_size:]
        
        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test
        self.y_test = y_test
        return (x_train, y_train, x_test, y_test)

    def euclidean(self, points: pd.DataFrame, element_of_x: pd.DataFrame) -> pd.DataFrame:
        x = points.subtract(element_of_x, axis=0)
        y = x.pow(2)
        z = y.sum(axis=1)
        zs = z.pow(1./2)
        return zs
    
    def predict(self, x_train: pd.DataFrame, y_train: pd.DataFrame, x_test: pd.DataFrame, k: int) -> pd.DataFrame:
        labels_pred =[]
        for x_test_element in x_test.iterrows():

            print(x_test_element)

            distances = self.euclidean(self, self.x_train, x_test_element[1])
            distances = pd.DataFrame(sorted(zip(distances, y_train)))

            label_pred = mode(distances.iloc[:k, 1], keepdims = False).mode

            labels_pred.append(label_pred)
        return pd.DataFrame(labels_pred, dtype=pd.Int64Dtype)
    
    def accuracy(self) -> float:
        true_positive = (self.y_test == self.y_preds).sum()
        return true_positive / len(self.y_test) * 100
    
    def confusion_matrix(self) -> None:
        return confusion_matrix(self.y_test, self.y_preds)