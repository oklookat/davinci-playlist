# davinci-playlist

Davinci resolve music playlist to YouTube timecodes.

Tested on DaVinci Resolve 18 Studio and Python 3.10.6.

## Install

1. Clone repo and cd to it.
2. Create and activate venv, install deps: 
```sh
python -m venv .venv
.venv/scripts/activate
pip install -r requirements.txt --ignore-requires-python # --ignore-requires-python for pydavinci
```

## Run

1. Activate venv.
2. Open DaVinci project. The first audio track should have mp3s going in a row. All mp3's must contain the artist and title in the tags.
3. Set timeline starting timecode to 00:00:00:00.
4. Activate script: `python ./main.py`.

## Output

Timecodes will be saved in timecodes.txt

Example:

```txt
00:00 Cool Artist - Cool track
04:22 Cool Artist 2 - Cool track 2
07:12 Cool Artist 3 - Long track 3
01:09:17 Cool Artist 4 - Cool track 4
```
