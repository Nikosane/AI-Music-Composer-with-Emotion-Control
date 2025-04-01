import numpy as np
import tensorflow as tf
from models.lstm_model import LSTMComposer
from preprocessing.data_loader import DataLoader

class TrainComposer:
    def __init__(self, epochs=50, batch_size=32):
        self.epochs = epochs
        self.batch_size = batch_size
        self.data_loader = DataLoader()
        self.model = LSTMComposer(input_shape=(None, 128))

    def train(self):
        X_train, y_train = self.data_loader.data, self.data_loader.labels
        X_train = np.array(X_train)
        y_train = tf.keras.utils.to_categorical(y_train, num_classes=6)
        
        self.model.model.fit(
            X_train, y_train,
            epochs=self.epochs,
            batch_size=self.batch_size,
            validation_split=0.2
        )
        self.model.model.save('models/saved/composer_model.h5')
        print("Model training complete and saved.")

if __name__ == '__main__':
    trainer = TrainComposer()
    trainer.train()
