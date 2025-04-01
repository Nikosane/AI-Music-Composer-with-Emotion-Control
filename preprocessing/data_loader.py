import os
import json
import numpy as np
from preprocessing.midi_processor import MidiProcessor

class DataLoader:
    def __init__(self, midi_dir='data/midi_files', emotion_file='data/emotions.json'):
        self.midi_dir = midi_dir
        self.emotion_file = emotion_file
        self.midi_processor = MidiProcessor(midi_dir)
        self.data, self.labels = self.load_data()

    def load_emotions(self):
        with open(self.emotion_file, 'r') as file:
            return json.load(file)

    def load_data(self):
        emotions = self.load_emotions()
        midi_data = self.midi_processor.load_midi_files()
        labels = [emotions.get(os.path.basename(file), 'neutral') for file in os.listdir(self.midi_dir) if file.endswith('.mid')]
        return np.array(midi_data), np.array(labels)

if __name__ == '__main__':
    loader = DataLoader()
    print(f"Loaded {len(loader.data)} MIDI files with emotions.")
