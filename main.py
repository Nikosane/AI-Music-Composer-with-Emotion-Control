import json
import os
from models.emotion_classifier import EmotionClassifier
from models.emotion_composer import EmotionComposer
from utils.midi_utils import save_midi

def load_emotions():
    with open('data/emotions.json', 'r') as file:
        return json.load(file)

def get_emotion_choice(emotions):
    print("Available emotions:")
    for i, emotion in enumerate(emotions, 1):
        print(f"{i}. {emotion}")

    choice = int(input("Choose an emotion (1 - {}): ".format(len(emotions))))
    return emotions[choice - 1]

def main():
    # Load emotions and models
    emotions_data = load_emotions()
    classifier = EmotionClassifier()
    composer = EmotionComposer()

    # Select emotion
    emotion_choice = get_emotion_choice(list(emotions_data.keys()))
    print(f"Selected Emotion: {emotion_choice}")

    # Generate Music
    print("Generating music...")
    midi_data = composer.generate_music(emotion_choice)

    # Save MIDI File
    output_path = os.path.join('outputs', 'generated_music', f'{emotion_choice}.mid')
    save_midi(midi_data, output_path)
    print(f"Music generated and saved to {output_path}")

if __name__ == "__main__":
    main()
