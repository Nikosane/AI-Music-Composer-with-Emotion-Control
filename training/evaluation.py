import numpy as np
import tensorflow as tf
from preprocessing.data_loader import DataLoader

class Evaluator:
    def __init__(self, model_path):
        self.model = tf.keras.models.load_model(model_path)
        self.data_loader = DataLoader()
        self.X_test, self.y_test = self.data_loader.data, self.data_loader.labels
        self.X_test = np.array(self.X_test)
        self.y_test = tf.keras.utils.to_categorical(self.y_test, num_classes=6)
    
    def evaluate(self):
        loss, accuracy = self.model.evaluate(self.X_test, self.y_test)
        print(f"Model Accuracy: {accuracy * 100:.2f}%")
        print(f"Model Loss: {loss:.4f}")

if __name__ == '__main__':
    evaluator = Evaluator('models/saved/classifier_model.h5')
    evaluator.evaluate()
