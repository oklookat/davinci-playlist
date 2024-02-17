import io
from pydavinci import davinci
import eyed3

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

timeline = resolve.active_timeline
timeline.custom_settings(True)

with io.open("timecodes.txt", mode="w", encoding="utf-8") as f:
    for item in timeline.items("audio", 1):
        itemProps = item.mediapoolitem.properties
        itemName = itemProps['Clip Name']
        if not isinstance(itemProps, dict):
            print("Media pool item properties not a dict. Its strange.")
            break
        if itemProps['Audio Codec'] != "MP3":
            print(f"'{itemName}' have wrong codec. Only MP3 supported.")
            break
        pathd = itemProps["File Path"]
        af = eyed3.load(pathd).tag
        if not hasattr(af, 'artist') or not hasattr(af, 'title'):
            print(f"'{itemName}' dont have artist and title tags.")
            break
        artist = af.artist
        title = af.title
        converter = AudioTimeConverter(timeline.settings.frame_rate)
        ti = converter.frames_to_time(item.start, item.end)
        formatted = f"{ti.start_minutes:02}:{ti.start_seconds:02} {artist} - {title}"
        if ti.start_hours > 0:
            formatted = f"{ti.start_hours:02}:" + formatted
        f.write(f"{formatted}\n")


#print(f"{ti.start_hours:02}:{ti.start_minutes:02}:{ti.start_seconds:02} - {ti.end_hours:02}:{ti.end_minutes:02}:{ti.end_seconds:02}")
