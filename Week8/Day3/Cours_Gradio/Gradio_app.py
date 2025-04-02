import numpy as np
from utils import determine_pause

def process_audio(audio: tuple, state: AppState):
    if state.stream is None:
        state.stream = audio[1]
        state.sampling_rate = audio[0]
    else:
        state.stream = np.concatenate((state.stream, audio[1]))

    pause_detected = determine_pause(state.stream, state.sampling_rate, state)
    state.pause_detected = pause_detected

    if state.pause_detected and state.started_talking:
        return gr.Audio(recording=False), state
    return None, state