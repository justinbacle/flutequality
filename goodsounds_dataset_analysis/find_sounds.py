import json
import pathlib

soundsDbPath = pathlib.Path("./goodsounds_dataset/sounds.json")
print(soundsDbPath.resolve().as_posix())

with open(soundsDbPath.resolve().as_posix(), mode='r') as f:
    soundsDB = json.load(f)

available_klass_list = []
# get available descriptors for flute
for v in soundsDB.values():
    if v["instrument"] == "flute":
        if v["klass"] not in available_klass_list:
            available_klass_list.append(v["klass"])

# only keep timbre descriptors
available_klass_list = [_ for _ in available_klass_list if "timbre" in _.lower()]
# ['bad-stability-timbre', 'good-timbre-classic', 'good-timbre-wood', 'good-timbre-vague',
#     'bad-timbre', 'scale-bad-timbre-staccato', 'scale-bad-timbre-staccato-minor']

# grab list of sounds for bad-timbre and good-timbre-classic for flute
good_timbre_list = []
bad_timbre_list = []
for v in soundsDB.values():
    if v["instrument"] == "flute":
        if v["klass"] == "good-timbre-classic":
            good_timbre_list.append(v)
        elif v["klass"] == "bad-timbre":
            bad_timbre_list.append(v)

print("--- GOOD TIMBRE ---")
print(json.dumps(good_timbre_list, indent=4))
print("--- BAD TIMBRE ---")
print(json.dumps(bad_timbre_list, indent=4))

# Good timbre has notes: G4 (#563), G5 (#566), G6 (#569)
# Bad timbre had notes: F#5 (#2777)
# Thus only two sounds are of interest : G5 "good" #566 and F#5 "bad" #2777

# BAD
# sound_files/flute_josep_evaluation_recordings/iphone/0006.wav

# GOOD
# sound_files/flute_almudena_timbre/iphone/0003.wav
