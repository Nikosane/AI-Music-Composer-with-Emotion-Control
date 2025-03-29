# Configuration settings for AI Music Composer

# General Settings
LOG_DIR = 'outputs/logs'
GENERATED_MUSIC_DIR = 'outputs/generated_music'

# Model Settings
LSTM_UNITS = 256
DROPOUT_RATE = 0.3
LEARNING_RATE = 0.001
EPOCHS = 100
BATCH_SIZE = 64

# Emotion Mapping
EMOTION_CATEGORIES = [
    'Happy',
    'Sad',
    'Angry',
    'Calm',
    'Excited',
    'Melancholic'
]

# MIDI Processing
MIDI_TICKS_PER_BEAT = 480
MIDI_TEMPO = 120  # BPM

# File Paths
EMOTION_DATA_PATH = 'data/emotions.json'
MIDI_DATA_PATH = 'data/midi_files'

# Model Paths
CLASSIFIER_MODEL_PATH = 'models/saved/classifier_model.h5'
COMPOSER_MODEL_PATH = 'models/saved/composer_model.h5'

# Training Configuration
TRAIN_SPLIT = 0.8
VALIDATION_SPLIT = 0.1
TEST_SPLIT = 0.1

print("Configuration loaded successfully.")

