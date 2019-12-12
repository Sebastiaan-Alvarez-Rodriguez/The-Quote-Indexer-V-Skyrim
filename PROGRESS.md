# 2019-12-11
Working on bug fixing and documentation.
Updated the project README, and created this site, including all progress reports.
Learned how to work with Github Pages on the fly.

Further documentation will follow, as well as updates to this website.

## TODO
The following things need to be worked on:
 * Documentation
 * Bug fixing

## Done
The following items are complete:
 * Construct dataset for The Elder Scrolls V: Skyrim
 * Voice Activity Detection (VAD)
 * Text-to-speech implementation
 * Dataset with famous quotes
 * Main infrastructure
 * Main UI
 * Dynamic loading of datasets
 * Hyperlinking to relevant online pages
 * Play spoken quotes
 * Dark theme


# 2019-12-08
I had big plans for 'the additional info' screen for quite a while.
It was to have a generated story, telling about the quest or situation in which the found quote can occur.
I even have support for this in the skyrim-quote-dataset.

In this update, I implemented this, sort of.
The problem is: Many quest identifiers are not actual quests visible in the game, but are named 
`WIRemoveItem01 "Drop weapon, Guard extorts" [QUST:0002C6AB]`.
This is not good to show to the user. many of these items exist in the dataset, and are not easily or cleanly separated from actual quests.
To sort-of resolve this, we created many tests to check quest type before returning this extra info. 

Also, to better support dynamic loading, we removed config reading to find datasets.
If you would want to add a dataset, you would have to add a line in a config.
This is too much work.
So now, datasets are automatically loaded, if you make sure that your dynamic code is in a subdirectory of `dynamic`, with name `<SOME_NAME>`,
and your dataset in `datasets`, with name `<SOME_NAME>.dat`.

Finally, implemented a dark theme.

Now, all the implementations are complete. Now it is time for documentation, and bug fixing.

## TODO
The following things need to be worked on:
 * Documentation
 * Bug fixing

## Done
The following items are complete:
 * Construct dataset for The Elder Scrolls V: Skyrim
 * Voice Activity Detection (VAD)
 * Text-to-speech implementation
 * Dataset with famous quotes
 * Main infrastructure
 * Main UI
 * Dynamic loading of datasets
 * Hyperlinking to relevant online pages
 * Play spoken quotes
 * Dark theme


# 2019-12-05
Until now, there were no audio files to play back when a quote was matched.
From this point on, this is possible.
With much difficulty, and a tool named [B.A.E](https://www.nexusmods.com/skyrimspecialedition/mods/974/) (Bethesda Archive Extracter),
I extracted the games spoken audio files.
Then, I converted them from their strange formatting to WAV using the tool [Unfuzer cpp edition](https://www.nexusmods.com/skyrim/mods/19242),
which is highly unstable.

As a result for all of this effort, I got a dataset of WAV files.
In the skyrim-quotes-dataset, there is a path from each dialogue to a file containing the right audio.
With some trivial manipulations, those paths can be used to index the all new extracted-audio-dataset.

During generation of the audio-dataset, we missed some dialogue audio files somehow (probably the tools).
So, not every quote has an audio file.

Also, this dataset is more than 20GB large, which is about as much as the entire game. This extraction was pricey.
I might want to look into compressing the WAV files somehow.


## TODO
The following things need to be worked on:
 * Dark theme

## Done
The following items are complete:
 * Construct dataset for The Elder Scrolls V: Skyrim
 * Voice Activity Detection (VAD)
 * Text-to-speech implementation
 * Dataset with famous quotes
 * Main infrastructure
 * Main UI
 * Dynamic loading of datasets
 * Hyperlinking to relevant online pages
 * Play spoken quotes


# 2019-12-04
Main infrastructure is stable. First fun thing implemented: Hyperlinking.
I used [The Unofficial Elder Scrolls Pages](https://en.uesp.net/) to serve informational pages on characters speaking quotes.
So, hyperlinking to online pages is implemented!

De-horrified UI. First, it was a complete mess. Now, everything is constructed in an orderly, overviewable fashion.
Created a UI-handler, which sets all callbacks, and handles interaction between UI and code in a streamlined manner.
The main UI is finished now.

Finally, transformed weird names (such as `DLC2BanditPillarWorker`) to normal names (such as `Bandit`).

Soon, I will start developping more fun things (play spoken quotes, dark theme).

## TODO
The following things need to be worked on:
 * Play spoken quotes
 * Dark theme

## Done
The following items are complete:
 * Construct dataset for The Elder Scrolls V: Skyrim
 * Voice Activity Detection (VAD)
 * Text-to-speech implementation
 * Dataset with famous quotes
 * Main infrastructure
 * Main UI
 * Dynamic loading of datasets
 * Hyperlinking to relevant online pages


# 2019-12-02
Main infrastructure is getting pretty stable. Basic UI is setup.
Further refinement in the 500K dataset (only 77759 quotes left).

Dynamic loading now works by checking out the dynamic modules.
When it is being loaded, it checks where the database is to be loaded by checking the configs in `configs` directory.
For more detailed information, check out the [dynamic loading protocol](https://sebastiaan-alvarez-rodriguez.github.io/The-Quote-Indexer-V-Skyrim/#dynamic-loading-protocol) on the main page.

Soon, I can start developping the fun things (Hyperlinking to relevant online pages, playing spoken quotes).

## TODO
The following things need to be worked on:
 * Main infrastructure
 * Main UI
 * Hyperlinking to relevant online pages
 * Play spoken quotes

## Done
The following items are complete:
 * Construct dataset for The Elder Scrolls V: Skyrim
 * Voice Activity Detection (VAD)
 * Text-to-speech implementation
 * Dataset with famous quotes
 * Dynamic loading of datasets


# 2019-12-01
Status update:
Found a dataset containing quotes named [Quotes-500K](https://github.com/ShivaliGoel/Quotes-500K).
It is rather raw, ill-structured and contains non-English quotes, and quotes which are way too long.
With enough refinement, however, it is an adequate dataset to show the ability of dynamic loading, once I implement that.

Implemented a basic dynamic loader, but should be improved before calling it finished.
The protocol is to look for datasets, and then find dynamic Python modules in `dynamic` folder.
This should probably be the other way around.

In the near future, I will start on main infrastructure, UI, and continue on dynamic loading.

## TODO
The following things need to be worked on:
 * Main infrastructure
 * Main UI
 * Dynamic loading of datasets

## Done
The following items are complete:
 * Construct dataset for The Elder Scrolls V: Skyrim
 * Voice Activity Detection (VAD)
 * Text-to-speech implementation
 * Dataset with famous quotes


# 2019-11-29
Today, I implemented Voice Activity Detection for DeepSpeech, and made an implementation to get speech-to-text in Python, using Deepspeech.
Also, I started thinking on a user interface. 
This program will most likely support desktops and laptops, and is (ideally) operating system independent.
To support this, the UI must be operating system independent, too.

Since I have no experience in developping user interfaces for pc, the UI must be simple.
Maybe I will use [pyQt5](https://www.riverbankcomputing.com/software/pyqt).

## TODO
The following things need to be worked on:
 * Main infrastructure
 * Main UI
 * Dynamic loading of datasets
 * Dataset with famous quotes

## Done
The following items are complete:
 * Construct dataset for The Elder Scrolls V: Skyrim
 * Voice Activity Detection (VAD)
 * Text-to-speech implementation


# 2019-11-28
I Installed [DeepSpeech](https://github.com/mozilla/DeepSpeech/) and learned to develop with its Python bindings.
Also, I used a program named [TES5Edit](https://www.nexusmods.com/skyrim/mods/25859) to extract all English dialogue subtitles from The Elder Scrolls V: Skyrim.
Finally, I wrote a little program to transform the raw data into an orderly tab-separated file without redundancy, to compress this dataset.
Once I have more time, I will continue work


## TODO
The following things need to be worked on:
 * Main infrastructure
 * Main UI
 * Voice Activity Detection (VAD)
 * Text-to-speech implementation
 * Dynamic loading of datasets
 * Dataset with famous quotes

## Done
The following items are complete:
 * Construct dataset for The Elder Scrolls V: Skyrim