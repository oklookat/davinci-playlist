# davinci-playlist

Davinci resolve music playlist to YouTube timecodes.

Tested on DaVinci Resolve 18 Studio

1. Open DaVinci project that contains many audiofiles (music) in first audio timeline.
2. Create venv: `python -m venv .venv`.
3. `pip install pip install pydavinci --ignore-requires-python`
4. Activate script: `python ./main.py`.

## Supported filenames

Currently only names like "01 - Cool Artist - Cool track".
Or "MUSTBE TWOWORDS аnyname anytext etc". I hope you know what I mean.

## Output

Timecodes will be saved in timecodes.txt


Example:

`
00:00:00 Cool Artist - Cool track
00:04:22 Cool Artist 2 - Cool track 2
00:07:12 Cool Artist 2 - Cool track 2
`
