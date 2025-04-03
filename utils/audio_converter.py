import subprocess
import os

def convert_midi_to_wav(midi_file, output_file):
    """
    Converts a MIDI file to WAV using FluidSynth.
    :param midi_file: Path to the input MIDI file.
    :param output_file: Path to save the output WAV file.
    """
    soundfont = "soundfonts/default.sf2"  # Ensure you have a proper SoundFont file
    command = ["fluidsynth", "-ni", soundfont, midi_file, "-F", output_file, "-r", "44100"]
    subprocess.run(command, check=True)
    print(f"Converted {midi_file} to {output_file}")
