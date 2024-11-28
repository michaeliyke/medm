from moviepy import VideoFileClip
from pydub import AudioSegment


def compress_media(file_path: str):
    output_file = file_path.rsplit(
        ".", 1)[0] + "_compressed." + file_path.rsplit(".", 1)[1]
    if file_path.endswith((".mp4", ".mkv", ".avi")):
        clip = VideoFileClip(file_path)
        clip.write_videofile(output_file, bitrate="500k")
    elif file_path.endswith((".mp3", ".wav")):
        audio = AudioSegment.from_file(file_path)
        audio.export(output_file, format=file_path.rsplit(
            ".", 1)[1], bitrate="64k")
    print(f"Compressed to {output_file}")
