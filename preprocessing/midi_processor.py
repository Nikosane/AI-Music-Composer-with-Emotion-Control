import os
import numpy as np
from mido import MidiFile

class MidiProcessor:
    def __init__(self, midi_dir='data/midi_files'):
        self.midi_dir = midi_dir

    def load_midi_files(self):
        midi_data = []
        for file_name in os.listdir(self.midi_dir):
            if file_name.endswith('.mid'):
                path = os.path.join(self.midi_dir, file_name)
                midi_data.append(self.parse_midi(path))
        return midi_data

    def parse_midi(self, file_path):
        midi = MidiFile(file_path)
        notes = []
        for msg in midi.play():
            if msg.type == 'note_on' or msg.type == 'note_off':
                notes.append((msg.note, msg.velocity, msg.time))
        return notes

    def encode_notes(self, notes, num_notes=128):
        encoded = []
        for note, velocity, time in notes:
            note_vector = np.zeros(num_notes)
            note_vector[note] = velocity / 127.0
            encoded.append(note_vector)
        return np.array(encoded)

if __name__ == '__main__':
    processor = MidiProcessor()
    midi_data = processor.load_midi_files()
    print(f"Loaded {len(midi_data)} MIDI files.")
