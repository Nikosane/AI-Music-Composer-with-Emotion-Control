import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from utils.midi_utils import generate_midi_from_notes

class EmotionComposer:
    def __init__(self, model_path='models/saved/composer_model.h5'):
        self.model_path = model_path
        self.model = self.build_model()
        self.load_model()

    def build_model(self):
        model = models.Sequential([
            layers.LSTM(256, return_sequences=True, input_shape=(None, 128)),
            layers.Dropout(0.3),
            layers.LSTM(256),
            layers.Dropout(0.3),
            layers.Dense(128, activation='softmax')
        ])
        model.compile(loss='categorical_crossentropy', optimizer='adam')
        return model

    def load_model(self):
        try:
            self.model.load_weights(self.model_path)
            print(f"Loaded model from {self.model_path}")
        except Exception as e:
            print(f"Failed to load model: {e}")

    def generate_music(self, emotion, num_notes=200):
        input_sequence = np.random.rand(1, 1, 128)  # Initial random input
        output_notes = []

        for _ in range(num_notes):
            prediction = self.model.predict(input_sequence, verbose=0)
            note_index = np.argmax(prediction)
            output_notes.append(note_index)

            next_input = np.zeros((1, 1, 128))
            next_input[0, 0, note_index] = 1.0
            input_sequence = np.concatenate((input_sequence, next_input), axis=1)

            if input_sequence.shape[1] > 100:
                input_sequence = input_sequence[:, -100:, :]

        return generate_midi_from_notes(output_notes)

if __name__ == '__main__':
    composer = EmotionComposer()
    midi_data = composer.generate_music('Happy')
    print("Generated MIDI data.")
