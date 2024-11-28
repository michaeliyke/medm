from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip


def cut_media(file_path: str, start: str, stop: str = None):
    start_time = parse_time(start)
    stop_time = parse_time(stop) if stop else None
    output_file = file_path.rsplit(
        ".", 1)[0] + "_cut." + file_path.rsplit(".", 1)[1]

    if file_path.endswith((".mp4", ".mkv", ".avi")):
        clip = VideoFileClip(file_path)
        sub_clip = clip.subclipped(start_time, stop_time)
        sub_clip.write_videofile(output_file)
    elif file_path.endswith((".mp3", ".wav")):
        clip = AudioFileClip(file_path)
        sub_clip = clip.subclipped(start_time, stop_time)
        sub_clip.write_audiofile(output_file)
    print(f"Cut file saved to {output_file}")


def parse_time(time_str: str):
    if ":" in time_str:
        parts = list(map(int, time_str.split(":")))
        return sum(p * 60**i for i, p in enumerate(reversed(parts)))
    return int(time_str)


def parse_time(time_str: str):
    # Replace periods with colons to standardize the input
    time_str = time_str.replace(".", ":")
    # Split the input into parts using colons as the delimiter
    parts = list(map(int, time_str.split(":")))
    # Ensure we have exactly 3 parts (hours, minutes, seconds) by prepending zeros
    while len(parts) < 3:
        parts.insert(0, 0)
    # Extract hours, minutes, and seconds
    hours, minutes, seconds = parts[-3], parts[-2], parts[-1]
    # Calculate total seconds
    return hours * 3600 + minutes * 60 + seconds


def parse_time(time_str: str):
    """Convert a time string in the format HH:MM:SS, MM:SS, or SS to seconds."""
    try:
        # Replace periods with colons to standardize the input
        time_str = time_str.replace(".", ":")

        # Split the input into parts using colons as the delimiter
        parts = list(map(int, time_str.split(":")))

        # Validate that all parts are non-negative integers
        if any(p < 0 for p in parts):
            raise ValueError("Time values cannot be negative.")

        # Ensure we have exactly 3 parts (hours, minutes, seconds) by prepending zeros
        while len(parts) < 3:
            parts.insert(0, 0)

        # Extract hours, minutes, and seconds
        hours, minutes, seconds = parts[-3], parts[-2], parts[-1]

        # Validate logical ranges for minutes and seconds
        if not (0 <= minutes < 60) or not (0 <= seconds < 60):
            raise ValueError("Minutes and seconds must be between 0 and 59.")

        # Calculate total seconds
        return hours * 3600 + minutes * 60 + seconds
    except ValueError as ve:
        raise ValueError(f"Invalid time format '{time_str}': {ve}")
    except Exception:
        raise ValueError(f"Invalid time format '{
                         time_str}'. Expected HH:MM:SS, MM:SS, or SS (colons or periods as separators).")
