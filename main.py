#!/usr/bin/env python3
"""
Entry program for make.fun competition news-image-20261118.
Summarizes Wednesday 18 November 2026 world news in a one-page newspaper image:
54 stories, 7 regions, 16 drawn panels, UTC timeline, numbers strip, world map,
38-item index, and date-check footer.
"""

import os
from pathlib import Path
import shutil

def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    
    image_path = Path(__file__).with_name("entry.png")
    dest_path = output_dir / "entry.png"
    
    shutil.copyfile(image_path, dest_path)
    print(f"Copied {image_path.name} to {dest_path}")

if __name__ == "__main__":
    main()
