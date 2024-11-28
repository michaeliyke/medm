from moviepy import VideoFileClip


def convert_to_audio(file_path: str):
    """Handles video-to-audio conversion"""
    output_file = file_path.rsplit(".", 1)[0] + ".mp3"
    clip = VideoFileClip(file_path)
    clip.audio.write_audiofile(output_file)
    print(f"Converted to {output_file}")
