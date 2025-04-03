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


if __name__ == "__main__":
    midi_path = "outputs/generated_music/sample.mid"
    wav_path = "outputs/generated_music/sample.wav"
    
    if not os.path.exists("soundfonts/default.sf2"):
        print("Error: SoundFont file missing. Please provide a valid SoundFont.")
    else:
        convert_midi_to_wav(midi_path, wav_path)
