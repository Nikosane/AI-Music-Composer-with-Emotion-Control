# AI Music Composer with Emotion Control

## 📌 Project Overview
AI Music Composer with Emotion Control is a Python-based project that uses Generative AI to create music compositions based on emotional cues. Using TensorFlow and MIDI processing, this system generates emotionally expressive music, making it suitable for applications in games, films, or virtual experiences.

---

## 🧑‍💻 Features
- Emotion-driven music composition
- LSTM-based generative AI model
- Emotion classification for dynamic music generation
- MIDI file processing and generation
- Real-time emotion-based soundtrack creation

---

## 🛠️ Tech Stack
- **Programming Language:** Python
- **Frameworks:** TensorFlow, Keras
- **Music Processing:** Mido, Music21
- **Data Management:** JSON
- **Modeling:** LSTM Neural Networks



---

## 🧑‍🏫 Installation
1. Clone the repository:
```bash
git clone https://github.com/Nikosane/ AI-Music-Composer-with-Emotion-Control.git
cd  AI-Music-Composer-with-Emotion-Control
```
2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
3. Install the required packages:
```bash
pip install -r requirements.txt
```

---

## 🧪 Usage
1. Run the main application:
```bash
python main.py
```
2. Choose an emotion input from available options (e.g., Happy, Sad, Angry, Calm).
3. The AI will generate a MIDI file based on the emotional cue.
4. Find the output in the `outputs/generated_music/` directory.

---

## 📊 Training
1. Prepare MIDI data and label emotions in `data/emotions.json`.
2. Train the emotion classifier:
```bash
python training/train_classifier.py
```
3. Train the generative model:
```bash
python training/train_composer.py
```
4. Evaluate models:
```bash
python training/evaluation.py
```

---

## 🛎️ Contributing
Contributions are welcome! If you'd like to contribute, follow these steps:
1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Submit a pull request.

---

## 📧 Contact
For questions or issues, reach out via GitHub Issues or contact the author at [niteshkotian3@gmail.com](mailto:niteshkotian3@gmail.com).

Happy composing! 🎵

temp1
temp2 ( for timeline issues) 
temp3 