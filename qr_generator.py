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



# ----------------------------------------------------------------------
# Data builders: each QR "type" formats the user's input into the right
# string format so scanning apps understand what to do with it.
# ----------------------------------------------------------------------
 
def build_plain_text(fields):
    return fields["text"].get("1.0", "end").strip()
 
 
def build_link(fields):
    url = fields["url"].get().strip()
    if url and not url.lower().startswith(("http://", "https://")):
        url = "https://" + url


def build_social(fields):
    platform = fields["platform"].get()
    handle = fields["handle"].get().strip().lstrip("@")
    templates = {
        "Instagram": "https://instagram.com/{}",
        "Facebook": "https://facebook.com/{}",
        "Twitter / X": "https://x.com/{}",
        "LinkedIn": "https://linkedin.com/in/{}",
        "GitHub": "https://github.com/{}",
        "WhatsApp (number)": "https://wa.me/{}",
        "Telegram": "https://t.me/{}",
    }
    template = templates.get(platform, "https://{}")
    return template.format(handle)


def build_wifi(fields):
    ssid = fields["ssid"].get().strip()
    password = fields["password"].get().strip()
    security = fields["security"].get()
    hidden = "true" if fields["hidden"].get() else "false"
    # Standard WIFI: QR format understood by phone camera apps
    sec = "nopass" if security == "None" else security
    return "WIFI:T:{};S:{};P:{};H:{};;".format(sec, ssid, password, hidden)


def build_contact(fields):
    name = fields["name"].get().strip()
    phone = fields["phone"].get().strip()
    email = fields["email"].get().strip()
    org = fields["org"].get().strip()
    # vCard format - scanning offers "Add to Contacts"
    vcard = [
        "BEGIN:VCARD",
        "VERSION:3.0",
        "N:{}".format(name),
        "FN:{}".format(name),
    ]
    if org:
        vcard.append("ORG:{}".format(org))
    if phone:
        vcard.append("TEL:{}".format(phone))
    if email:
        vcard.append("EMAIL:{}".format(email))
    vcard.append("END:VCARD")
    return "\n".join(vcard)



def build_email(fields):
    to = fields["to"].get().strip()
    subject = fields["subject"].get().strip()
    body = fields["body"].get("1.0", "end").strip()
    return "mailto:{}?subject={}&body={}".format(to, subject, body)


def build_sms(fields):
    number = fields["number"].get().strip()
    message = fields["message"].get("1.0", "end").strip()
    return "SMSTO:{}:{}".format(number, message)


def build_file_link(fields):
    url = fields["url"].get().strip()
    if url and not url.lower().startswith(("http://", "https://")):
        url = "https://" + url
    return url

# Maps each QR type name to (list of field specs, builder function)
# field spec: (key, label, kind) -- kind is "entry", "text", "combo", "check"
QR_TYPES = {
    "Plain Text": {
        "fields": [("text", "Text", "text")],
        "builder": build_plain_text,
    },
    "Website / Webpage Link": {
        "fields": [("url", "URL (e.g. https://example.com)", "entry")],
        "builder": build_link,
    },
    "YouTube Video": {
        "fields": [("url", "YouTube video URL", "entry")],
        "builder": build_youtube,
    },
    "Image / Video / File (hosted link)": {
        "fields": [("url", "Link to the file (Drive, Dropbox, etc.)", "entry")],
        "builder": build_file_link,
    },
    "Social Media Profile": {
        "fields": [
            ("platform", "Platform", "combo", [
                "Instagram", "Facebook", "Twitter / X", "LinkedIn",
                "GitHub", "WhatsApp (number)", "Telegram",
            ]),
            ("handle", "Username / number (no @)", "entry"),
        ],
        "builder": build_social,
    },
    "WiFi Network": {
        "fields": [
            ("ssid", "Network name (SSID)", "entry"),
            ("password", "Password", "entry"),
            ("security", "Security", "combo", ["WPA", "WEP", "None"]),
            ("hidden", "Hidden network", "check"),
        ],
        "builder": build_wifi,
    },
    "Contact Card": {
        "fields": [
            ("name", "Full name", "entry"),
            ("phone", "Phone number", "entry"),
            ("email", "Email", "entry"),
            ("org", "Organization (optional)", "entry"),
        ],
        "builder": build_contact,
    },
    "Email": {
        "fields": [
            ("to", "Send to", "entry"),
            ("subject", "Subject", "entry"),
            ("body", "Body", "text"),
        ],
        "builder": build_email,
    },
    "SMS": {
        "fields": [
            ("number", "Phone number", "entry"),
            ("message", "Message", "text"),
        ],
        "builder": build_sms,
    },
}
