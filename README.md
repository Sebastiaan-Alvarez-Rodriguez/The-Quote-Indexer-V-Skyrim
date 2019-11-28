# The Quote Indexer V: Skyrim
This project is created to convert speech to a certain quote
It uses [this](https://github.com/mozilla/DeepSpeech/tree/master/examples/mic_vad_streaming) for setup.

## Requirements
```bash
pip3 install deepspeech==0.5.1 --user
```

## Run
Need to have microphone in laptop while booting, errors otherwise.
### Run deepspeech itself
```bash
deepspeech \
--model models/output_graph.pbmm \
--alphabet models/alphabet.txt \
--lm models/lm.binary \
--trie models/trie \
--audio audio/2830-3980-0043.wav
```
### Run deepspeech program
```bash
python3 src/speech-to-text/stt.py \
--model models/output_graph.pbmm \
--alphabet models/alphabet.txt \
--lm models/lm.binary \
--trie models/trie \
--file oof.wav
```
### Run audio device info script in
```python
import pyaudio
p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
    print p.get_device_info_by_index(i)
```