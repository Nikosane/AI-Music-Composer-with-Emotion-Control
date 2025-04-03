import json

def load_emotion_mapping(file_path="data/emotions.json"):
    """
    Loads the emotion mapping from a JSON file.
    :param file_path: Path to the JSON file containing emotion mappings.
    """
    with open(file_path, "r") as file:
        return json.load(file)

def map_emotion_to_label(emotion, emotion_mapping):
    """
    Maps an emotion string to a corresponding numerical label.
    :param emotion: Emotion as a string.
    :param emotion_mapping: Dictionary containing emotion-to-label mappings.
    """
    return emotion_mapping.get(emotion.lower(), -1)
