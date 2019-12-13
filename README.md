# The Quote Indexer V: Skyrim
A fun project, created to index a dataset of known quotes!
Its idea is very simple:
Speak any quote, simple or advanced, correct or almost correct, and get the original quote out.  

There is even a mapping from famous TESV-quotes to sounds.

## Requirements
```bash
pip3 install deepspeech==0.6.0 pyqt5 qdarkstyle playsound --user
```

You need a pre-trained Deepspeech model to convert speech to text.
You can either use [pre-trained Deepspeech 0.6.0](https://github.com/mozilla/DeepSpeech/releases/download/v0.6.0/deepspeech-0.6.0-models.tar.gz),
or you have to train your own neural network...  

You need to have a microphone, in order to record speech.

## Running
Simply run
```bash
python3 run.py
```

## Dynamic Loading Protocol
Adding another quote dataset to index is fairly simple, and contains several steps.
Most of the fime, there is a dataset with quotes to add.
Here is all required information to add a dataset of quotes for indexing.

### Quotelist
The primary job of the quotelist, is to store all quotes, and handle `find()` calls.
Create a file named `quotelist.py`, containing a class named `QList`, which has [QuoteList](https://github.com/Sebastiaan-Alvarez-Rodriguez/The-Quote-Indexer-V-Skyrim/blob/master/src/quotes/quotelist.py) as parent.
`quotelist.py` should look like this:
```python
from src.quotes.quotelist import QuoteList

class QList(QuoteList):
    def __init__(self, file):
        super(QList, self).__init__()
        pass

    def find(self, sentence, acceptscore):
        pass
```
The constructor of `QList` receives a `file` argument, which is one of the following 2:
 * a string path to the dataset file, if it is found
 * `None` if no dataset file is found

The  `find` function receives a `sentence` (a speech-recognized string) and an `acceptscore` (float between [0,1]) stating when to accept a candidate string.
An `acceptscore` of `0.8` would mean that a potential quote candidate should match `sentence` for at least `80%`.
It should return an object which is a child of `Quote`. This will be explained in the next section.

You should store this file as `dynamic/<NAME>/quotelist.py`. Then, a dataset in `datasets/<NAME>.dat` is associated with this `QuoteList`,
and the path to this file is passed as `file` argument in the contstructor of the `QList`.


### Quote
Each line of the dataset contains one or more fields, separated by a tab, comma, or something else.
A line may look like `A,B,C,D,Quote`, or `A|Quote|B`, or something entirely different.
You should tell this program how to interpret these lines of text in your dataset.
You should specify an object, which is a child of `Quote`, and should look like this:
```python
from src.quotes.quote import Quote

class SOME_NAME(Quote):
    def __init__(self, line):
        super(SOME_NAME, self).__init__()
        pass

    def get_quote(self):
        pass

    def get_url(self):
        pass

    def get_extra_info(self):
        pass

    def get_audio_path(self, basepath):
        pass
```
In the constructor, `line` is the raw line in the dataset.
In `get_quote`, you should return a human-readable string of the quote for a line in the dataset.
In `get_url`, return a url giving information about the quote, or `None`, if there is no url to return.
In `get_extra_info`, return extra info, or `None`, if there is no extra information.
In `get_audio_path`, return a path to an audio file related to the quote, or `None` if there is no audio file.
The `basepath` parameter points to the `sounds/<NAME>/`. You are expected to store all audio files for the dataset there.
Audio files are played with [playsound](https://pypi.org/project/playsound/), and we therefore support all audio formats that playsound supports.

### A complete example
Here, we give a complete example, which you can use to create support for your own dataset.
`datasets/sebastiaan.dat` contains the following:
```
TODO or not TODO, that is the question,Sebastiaan,todo_or_not_todo\path\todo.wav
Prefer one working feature over ten features half-working,Sebastiaan,"none.wav"
...

```
`dynamic/sebastiaan/quotelist.py` contains the following:
```python
from difflib import get_close_matches

from src.quotes.quotelist import QuoteList
from src.quotes.quote import Quote

class SebastiaanQuote(Quote):
    def __init__(self, line):
        self.QUOTE,self.PERSON,self.FILE = line.split(',')


    def get_quote(self):
        return f'{self.QUOTE}\n- {self.PERSON}'

    def get_url(self):
        return None

    def get_extra_info(self):
        return None

    def get_audio_path(self, basepath):
        return self.FILE if not '"none.wav"' in self.FILE else None

class QList(QuoteList):
    def __init__(self, file):
        super(QList, self).__init__()
        with open(file, 'r') as quotefile:
                next(quotefile) #skip first line
                for line in quotefile:
                    obj = SebastiaanQuote(line[:-1])
                    self.map[obj.QUOTE] = obj

    def find(self, sentence, acceptscore):
        response = get_close_matches(sentence, self.map, n=1, cutoff=0.6)
        return None if len(response)==0 else self.map[response[0]]

```
This minimal example works well for the example dataset.