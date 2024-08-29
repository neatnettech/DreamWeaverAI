import os
import random
from difflib import get_close_matches

def find_sound(query):
    sound_folder = "sounds"
    sound_files = [f for f in os.listdir(sound_folder) if f.endswith('.wav')]

    simple_names = [os.path.splitext(f)[0].lower() for f in sound_files]
    matches = get_close_matches(query.lower(), simple_names, n=1, cutoff=0.6)

    if matches:
        return os.path.join(sound_folder, sound_files[simple_names.index(matches[0])])
    else:
        return os.path.join(sound_folder, random.choice(sound_files))