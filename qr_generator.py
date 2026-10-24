"""
QR Code Generator - Mini Project (Pure Python)
------------------------------------------------
Generates QR codes for links, webpages, YouTube videos, social media
profiles, WiFi logins, contact cards, email, SMS, and plain text.
 
IMPORTANT (please read): a QR code can only store TEXT data (a link or a
short string), not an actual image, video, or audio file. There is no way
to "put a video inside" a QR code - the file itself is far too large to
fit (a QR code tops out around 2-3 KB of data). So for images/videos this
tool builds a QR that points to the file's LINK instead - e.g. a YouTube
URL, a Google Drive / Dropbox share link, or any URL where the file is
hosted online. Scanning the code then opens that link.
 
Install requirements first:
    pip install qrcode[pil] pillow
 
Run:
    python qr_generator.py
"""

import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import qrcode
from qrcode.constants import ERROR_CORRECT_H
from PIL import Image, ImageTk