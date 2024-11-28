# medm

Media manager cli: audio extraction, clip cutting, media compression, QR code reading and generation, and much more coming on the pipeline

## Usage

```bash
python -m medm convert video.mkv
python -m medm compress audio.mp3
python -m medm cut video.mp4 00:01:00 00:02:00
python -m medm qr generate "Hello, World!" -f hello.png
python -m medm qr decode hello.png
```

**If you prefer a bash alias:**

```bash
alias medm='python -m medm'
```

## How to install

### Ubuntu

```bash
sudo apt update
sudo apt install ffmpeg

pip install -r requirements.txt
```

### Windows

1. Download and install [ffmpeg](https://ffmpeg.org/download.html)
2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

### macOS (Homebrew)

```bash
brew install ffmpeg

pip install -r requirements.txt
```

### Verifying Installations

```bash
ffmpeg -version

python -m medm --help
```

### And in Python

```python
import moviepy.editor
import pydub
import qrcode
from PIL import Image
from pyzbar.pyzbar import decode

print("All libraries are installed and working!")
```

**If you get no errors, your environment is ready to use medm*

### License

MIT License
