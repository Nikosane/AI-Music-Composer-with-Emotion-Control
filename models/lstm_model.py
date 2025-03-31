import tensorflow as tf
from tensorflow.keras import layers, models

class LSTMModel:
    def __init__(self, input_shape=(None, 128), output_dim=128, lstm_units=256, dropout_rate=0.3):
        self.input_shape = input_shape
        self.output_dim = output_dim
        self.lstm_units = lstm_units
        self.dropout_rate = dropout_rate
        self.model = self.build_model()

    def build_model(self):
        model = models.Sequential([
            layers.LSTM(self.lstm_units, return_sequences=True, input_shape=self.input_shape),
            layers.Dropout(self.dropout_rate),
            layers.LSTM(self.lstm_units),
            layers.Dropout(self.dropout_rate),
            layers.Dense(self.output_dim, activation='softmax')
        ])

        model.compile(
            loss='categorical_crossentropy',
            optimizer='adam',
            metrics=['accuracy']
        )
        return model

    def summary(self):
        self.model.summary()

    def save_model(self, path):
        self.model.save(path)
        print(f"Model saved to {path}")

    def load_model(self, path):
        self.model = models.load_model(path)
        print(f"Model loaded from {path}")

if __name__ == '__main__':
    lstm_model = LSTMModel()
    lstm_model.summary()
