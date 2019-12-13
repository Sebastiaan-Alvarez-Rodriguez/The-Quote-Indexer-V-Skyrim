import threading, collections, queue, os, os.path
import deepspeech
import numpy as np

from src.stt.vad import VADAudio
import src.general.general as g
from ui.messager import msg, Severity


class QuoteSpeech(object):
    '''Simple class to handle speech to text'''

    BEAM_WIDTH = 500
    DEFAULT_SAMPLE_RATE = 44100
    LM_ALPHA = 0.75
    LM_BETA = 1.85
    VAD_AGGRESSIVENESS = 3

    def __init__(self):
        super(QuoteSpeech, self).__init__()
        model_graph = os.path.join(g.mdl_loc, 'output_graph.pbmm')
        lm          = os.path.join(g.mdl_loc, 'lm.binary')
        trie        = os.path.join(g.mdl_loc, 'trie')
        if not os.path.isfile(model_graph) or not os.path.isfile(lm) or not os.path.isfile(trie):
            msg(f'Could not find all model files (output_graph.pbmm, alphabet.txt, lm.binary, trie) in {g.mdl_loc}', severity=Severity.CRITICAL)
            exit(1)
        else:
            self.model = deepspeech.Model(model_graph, self.BEAM_WIDTH)
            self.model.enableDecoderWithLM(lm, trie, self.LM_ALPHA, self.LM_BETA)

    # Listen for audio from the microphone, perform text-to-speech, return the recognized speech as string
    def get_speech(self):
        try:
            vad_audio = VADAudio(aggressiveness=self.VAD_AGGRESSIVENESS,device=None,input_rate=self.DEFAULT_SAMPLE_RATE)
            frames = vad_audio.vad_collector()
            stream_context = self.model.createStream()
            for frame in frames:
                if frame is not None:
                    self.model.feedAudioContent(stream_context, np.frombuffer(frame, np.int16))
                else:
                    detected_str = self.model.finishStream(stream_context)
                    vad_audio.destroy()
                    return detected_str
        except OSError as e:
            msg('Could not open audio device (Linux at it again)', severity=Severity.CRITICAL)