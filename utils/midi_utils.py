import mido
import numpy as np

class MIDIUtils:
    @staticmethod
    def load_midi(file_path):
        midi = mido.MidiFile(file_path)
        notes = []
        for msg in midi:
            if not msg.is_meta and msg.type == 'note_on':
                notes.append((msg.note, msg.velocity, msg.time))
        return notes

    @staticmethod
    def save_midi(notes, output_path):
        midi = mido.MidiFile()
        track = mido.MidiTrack()
        midi.tracks.append(track)
        
        for note, velocity, time in notes:
            track.append(mido.Message('note_on', note=note, velocity=velocity, time=time))
            track.append(mido.Message('note_off', note=note, velocity=0, time=time+10))
        
        midi.save(output_path)
        print(f"MIDI file saved at {output_path}")

if __name__ == '__main__':
    sample_notes = [(60, 100, 200), (62, 90, 300), (64, 110, 250)]
    MIDIUtils.save_midi(sample_notes, 'outputs/generated_music/sample.mid')
