# The Quote Indexer V: Skyrim
A fun project, created to index a dataset of known quotes!
Its idea is very simple:
Speak any quote, simple or advanced, correct or almost correct, and get the original quote out.  

There is even a mapping from famous TESV-quotes to sounds.

There are some pages to visit:
 * [Progress Reports](https://sebastiaan-alvarez-rodriguez.github.io/The-Quote-Indexer-V-Skyrim/progress.html)
 * [Credits](https://sebastiaan-alvarez-rodriguez.github.io/The-Quote-Indexer-V-Skyrim/credits.html)

## Requirements
```bash
pip3 install deepspeech==0.5.1 --user
pip3 install pyqt5 --user
pip3 install qdarkstyle --user
pip3 install playsound --user
```

You need a pre-trained Deepspeech model to convert speech to text.
You can either use [pre-trained Deepspeech 0.51](https://github.com/mozilla/DeepSpeech/releases/download/v0.5.1/deepspeech-0.5.1-models.tar.gz),
or you have to train your own neural network...  

You need to have a microphone available to record speech.

## Running
Simply run
```bash
python3 run.py
```

## dynamic-loading-protocol
Do you want to add your own dataset to this quote indexer?
This will be explained soon.