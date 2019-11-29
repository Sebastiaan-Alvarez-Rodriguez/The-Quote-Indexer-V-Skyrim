import threading, collections, queue, os, os.path
import deepspeech
import numpy as np
import pyaudio
import wave
import webrtcvad
from scipy import signal

class Audio(object):
    """Streams raw audio from microphone. Data is received in a separate thread, and stored in a buffer, to be read from."""

    FORMAT = pyaudio.paInt16
    # Network/VAD rate-space
    RATE_PROCESS = 16000
    CHANNELS = 1
    BLOCKS_PER_SECOND = 50

    def __init__(self, callback=None, device=None, input_rate=RATE_PROCESS):
        def proxy_callback(in_data, frame_count, time_info, status):
            callback(in_data)
            return (None, pyaudio.paContinue)
        if callback is None: callback = lambda in_data: self.buffer_queue.put(in_data)
        self.buffer_queue = queue.Queue()
        self.device = device
        self.input_rate = input_rate
        self.sample_rate = self.RATE_PROCESS
        self.block_size = int(self.RATE_PROCESS / float(self.BLOCKS_PER_SECOND))
        self.block_size_input = int(self.input_rate / float(self.BLOCKS_PER_SECOND))
        self.pa = pyaudio.PyAudio()

        kwargs = {
            'format': self.FORMAT,
            'channels': self.CHANNELS,
            'rate': self.input_rate,
            'input': True,
            'frames_per_buffer': self.block_size_input,
            'stream_callback': proxy_callback,
        }

        # if not default device
        if self.device:
            kwargs['input_device_index'] = self.device

        self.stream = self.pa.open(**kwargs)
        self.stream.start_stream()

    def resample(self, data, input_rate):
        """
        Microphone may not support our native processing sampling rate, so
        resample from input_rate to RATE_PROCESS here for webrtcvad and
        deepspeech

        Args:
            data (binary): Input audio stream
            input_rate (int): Input audio rate to resample from
        """
        data16 = np.fromstring(string=data, dtype=np.int16)
        resample_size = int(len(data16) / self.input_rate * self.RATE_PROCESS)
        resample = signal.resample(data16, resample_size)
        resample16 = np.array(resample, dtype=np.int16)
        return resample16.tostring()

    def read_resampled(self):
        """Return a block of audio data resampled to 16000hz, blocking if necessary."""
        return self.resample(data=self.buffer_queue.get(),
                             input_rate=self.input_rate)

    def read(self):
        """Return a block of audio data, blocking if necessary."""
        return self.buffer_queue.get()

    def destroy(self):
        self.stream.stop_stream()
        self.stream.close()
        self.pa.terminate()

    frame_duration_ms = property(lambda self: 1000 * self.block_size // self.sample_rate)

    def write_wav(self, filename, data):
        logging.info("write wav %s", filename)
        wf = wave.open(filename, 'wb')
        wf.setnchannels(self.CHANNELS)
        # wf.setsampwidth(self.pa.get_sample_size(FORMAT))
        assert self.FORMAT == pyaudio.paInt16
        wf.setsampwidth(2)
        wf.setframerate(self.sample_rate)
        wf.writeframes(data)
        wf.close()

class VADAudio(Audio):
    """Filter & segment audio with voice activity detection."""

    def __init__(self, aggressiveness=3, device=None, input_rate=None):
        super().__init__(device=device, input_rate=input_rate)
        self.vad = webrtcvad.Vad(aggressiveness)

    def frame_generator(self):
        if self.input_rate == self.RATE_PROCESS:
            while True:
                yield self.read()
        else:
            while True:
                yield self.read_resampled()

    def vad_collector(self, padding_ms=300, ratio=0.75, frames=None):
        if frames is None: frames = self.frame_generator()
        num_padding_frames = padding_ms // self.frame_duration_ms
        ring_buffer = collections.deque(maxlen=num_padding_frames)
        triggered = False

        for frame in frames:
            is_speech = self.vad.is_speech(frame, self.sample_rate)

            if not triggered:
                ring_buffer.append((frame, is_speech))
                num_voiced = len([f for f, speech in ring_buffer if speech])
                if num_voiced > ratio * ring_buffer.maxlen:
                    triggered = True
                    for f, s in ring_buffer:
                        yield f
                    ring_buffer.clear()

            else:
                yield frame
                ring_buffer.append((frame, is_speech))
                num_unvoiced = len([f for f, speech in ring_buffer if not speech])
                if num_unvoiced > ratio * ring_buffer.maxlen:
                    triggered = False
                    yield None
                    ring_buffer.clear()

class QuoteSpeech(object):
    '''Simple class to handle quotes and speech'''

    N_FEATURES = 26
    N_CONTEXT = 9
    BEAM_WIDTH = 500

    DEFAULT_SAMPLE_RATE = 44100
    LM_ALPHA = 0.75
    LM_BETA = 1.85
    VAD_AGGRESSIVENESS = 3

    def __init__(self, model_dir):
        super(QuoteSpeech, self).__init__()
        model_graph = os.path.join(model_dir, 'output_graph.pbmm')
        alphabet    = os.path.join(model_dir, 'alphabet.txt')
        lm          = os.path.join(model_dir, "lm.binary")
        trie        = os.path.join(model_dir, "trie")
        self.model = deepspeech.Model(model_graph, self.N_FEATURES, self.N_CONTEXT, alphabet, self.BEAM_WIDTH)
        self.model.enableDecoderWithLM(alphabet, lm, trie, self.LM_ALPHA, self.LM_BETA)

    def get_speech(self):
        print('\t\tSTART')
        vad_audio = VADAudio(aggressiveness=self.VAD_AGGRESSIVENESS,device=None,input_rate=self.DEFAULT_SAMPLE_RATE)
        frames = vad_audio.vad_collector()
        stream_context = self.model.setupStream()
        for frame in frames:
            if frame is not None:
                self.model.feedAudioContent(stream_context, np.frombuffer(frame, np.int16))
            else:
                return self.model.finishStream(stream_context)
        raise RuntimeError('Could not get speech')

if __name__ == '__main__':
    a = QuoteSpeech('/home/radon/Uni/api/The-Quote-Indexer-V-Skyrim/models/')
    print(a.get_speech())