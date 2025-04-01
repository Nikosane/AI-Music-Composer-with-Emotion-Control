import numpy as np
from preprocessing.midi_processor import MidiProcessor

class FeatureExtractor:
    def __init__(self):
        self.midi_processor = MidiProcessor()

    def extract_features(self, midi_data):
        features = []
        for notes in midi_data:
            encoded_notes = self.midi_processor.encode_notes(notes)
            features.append(encoded_notes)
        return np.array(features)

if __name__ == '__main__':
    extractor = FeatureExtractor()
    sample_midi = [[[60, 100, 0.5], [62, 90, 0.3], [64, 110, 0.4]]]
    extracted_features = extractor.extract_features(sample_midi)
    print(f"Extracted features shape: {extracted_features.shape}")
