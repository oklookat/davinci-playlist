import io
from pathlib import Path
from pydavinci import davinci

resolve = davinci.Resolve()

class AudioTimeConverter:
    def __init__(self, frame_rate):
        self.frame_rate = frame_rate
        self.start_hours = 0
        self.start_minutes = 0
        self.start_seconds = 0
        self.start_milliseconds = 0
        self.end_hours = 0
        self.end_minutes = 0
        self.end_seconds = 0
        self.end_milliseconds = 0

    def frames_to_time(self, start_frame, end_frame):
        start_time_seconds = start_frame / self.frame_rate
        end_time_seconds = end_frame / self.frame_rate

        self.start_hours = int(start_time_seconds // 3600)
        self.start_minutes = int((start_time_seconds % 3600) // 60)
        self.start_seconds = int(start_time_seconds % 60)
        self.start_milliseconds = int((start_time_seconds - int(start_time_seconds)) * 1000)

        self.end_hours = int(end_time_seconds // 3600)
        self.end_minutes = int((end_time_seconds % 3600) // 60)
        self.end_seconds = int(end_time_seconds % 60)
        self.end_milliseconds = int((end_time_seconds - int(end_time_seconds)) * 1000)

        return self

# Example: 01 - Cool Artist - Cool track.mp3
def formatDeemixStyle(file: str) -> str:
    splitted = file.split(" ")[2:]
    return " ".join(splitted)

timeline = resolve.active_timeline
timeline.custom_settings(True)

f = io.open("timecodes.txt", mode="w", encoding="utf-8") 
 
for item in timeline.items("audio", 1):
    converter = AudioTimeConverter(timeline.settings.frame_rate)
    ti = converter.frames_to_time(item.start, item.end)
    formattedFilename = Path(item.name).stem
    formattedFilenameDeemix = formatDeemixStyle(formattedFilename)
    formatted = f"{ti.start_hours:02}:{ti.start_minutes:02}:{ti.start_seconds:02} {formattedFilenameDeemix}"
    f.write(f"{formatted}\n")

f.close()


#print(f"{ti.start_hours:02}:{ti.start_minutes:02}:{ti.start_seconds:02} - {ti.end_hours:02}:{ti.end_minutes:02}:{ti.end_seconds:02}")
