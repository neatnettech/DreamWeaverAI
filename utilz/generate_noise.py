import numpy as np
import soundfile as sf

def generate_white_noise(duration, file, sample_rate=44100):
    samples = np.random.normal(0, 0.1, size=int(duration * sample_rate))
    sf.write(file, samples, sample_rate)

def generate_natural_noise(duration, file, sample_rate=44100):
    samples = np.random.normal(0, 0.1, size=int(duration * sample_rate))
    sf.write(file, samples, sample_rate)