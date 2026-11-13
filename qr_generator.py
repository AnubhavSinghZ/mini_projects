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


class QRApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("QR Code Generator")
        self.geometry("760x560")
        self.minsize(680, 520)
        self.configure(bg="#101418")
 
        self.logo_path = None
        self.current_qr_image = None   # PIL image, full resolution
        self.current_preview = None    # PhotoImage shown on screen
 
        self._build_style()
        self._build_layout()
        self._on_type_change()
     # -- STYLING ---------------------------------------------------
    def _build_style(self):
        style = ttk.Style(self)
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass
        bg = "#101418"
        panel = "#171C22"
        text = "#E8EDF2"
        accent = "#4FD1C5"
        style.configure("TFrame", background=bg)
        style.configure("Panel.TFrame", background=panel)
        style.configure("TLabel", background=bg, foreground=text, font=("Segoe UI", 10))
        style.configure("Panel.TLabel", background=panel, foreground=text, font=("Segoe UI", 10))
        style.configure("Heading.TLabel", background=bg, foreground=text, font=("Segoe UI", 15, "bold"))
        style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=8)
        style.configure("Accent.TButton", background=accent, foreground="#06201C")
        style.map("Accent.TButton", background=[("active", "#3FBFB2")])
        style.configure("TCombobox", padding=4)
      # -- LAYOUT ------------------------------------------------------
    def _build_layout(self):
        container = ttk.Frame(self, padding=18)
        container.pack(fill="both", expand=True)
 
        ttk.Label(container, text="QR Code Generator", style="Heading.TLabel").pack(anchor="w")
        ttk.Label(
            container,
            text="Choose what the QR code should open or contain, fill in the details, then generate.",
        ).pack(anchor="w", pady=(2, 14))
 
        body = ttk.Frame(container)
        body.pack(fill="both", expand=True)
        body.columnconfigure(0, weight=1)
        body.columnconfigure(1, weight=1)
        body.rowconfigure(0, weight=1)
     # -- left: form panel
        left = ttk.Frame(body, style="Panel.TFrame", padding=16)
        left.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
 
        ttk.Label(left, text="QR Type", style="Panel.TLabel").pack(anchor="w")
        self.type_var = tk.StringVar(value="Website / Webpage Link")
        type_combo = ttk.Combobox(
            left, textvariable=self.type_var, values=list(QR_TYPES.keys()),
            state="readonly",
        )
        type_combo.pack(fill="x", pady=(4, 14))
        type_combo.bind("<<ComboboxSelected>>", lambda e: self._on_type_change())
 
        self.fields_frame = ttk.Frame(left, style="Panel.TFrame")
        self.fields_frame.pack(fill="both", expand=True)
 
        logo_row = ttk.Frame(left, style="Panel.TFrame")
        logo_row.pack(fill="x", pady=(12, 0))
        ttk.Button(logo_row, text="Add logo (optional)", command=self._choose_logo).pack(side="left")
        self.logo_label = ttk.Label(logo_row, text="No logo selected", style="Panel.TLabel")
        self.logo_label.pack(side="left", padx=10)
 
        ttk.Button(left, text="Generate QR Code", style="Accent.TButton", command=self._generate,
           ).pack(fill="x", pady=(18, 0))
            


    # -- right: preview panel
        right = ttk.Frame(body, style="Panel.TFrame", padding=16)
        right.grid(row=0, column=1, sticky="nsew")

        ttk.Label(right, text="Preview", style="Panel.TLabel").pack(anchor="w")
        self.preview_canvas = tk.Label(right, bg="#FFFFFF", width=260, height=260)
        self.preview_canvas.pack(pady=14)

        self.save_btn = ttk.Button(right, text="Save as PNG", command=self._save, state="disabled")
        self.save_btn.pack(fill="x")
     # -- dynamic form --------------------------------------------------
    def _on_type_change(self):
        for child in self.fields_frame.winfo_children():
            child.destroy()

        spec = QR_TYPES[self.type_var.get()]
        self.active_fields = {}

        for field in spec["fields"]:
            key, label = field[0], field[1]
            kind = field[2]
            row = ttk.Frame(self.fields_frame, style="Panel.TFrame")
            row.pack(fill="x", pady=6)
            ttk.Label(row, text=label, style="Panel.TLabel").pack(anchor="w")

            if kind == "entry":
                widget = ttk.Entry(row)
                widget.pack(fill="x")
            elif kind == "text":
                widget = tk.Text(row, height=4, bg="#20262E", fg="#E8EDF2", insertbackground="#E8EDF2")
                widget.pack(fill="x")
            elif kind == "combo":
                options = field[3]
                var = tk.StringVar(value=options[0])
                widget = ttk.Combobox(row, textvariable=var, values=options, state="readonly")
                widget.pack(fill="x")
                widget._var = var  # keep reference
            elif kind == "check":
                var = tk.BooleanVar(value=False)
                widget = ttk.Checkbutton(row, variable=var, style="Panel.TLabel")
                widget.pack(anchor="w")
                widget._var = var

            self.active_fields[key] = self._wrap(widget, kind)

    @staticmethod
    def _wrap(widget, kind):
        """Give every widget type a uniform .get() so builders stay simple."""
        if kind == "combo":
            class ComboWrap:
                def get(self_inner):
                    return widget._var.get()
            return ComboWrap()
        if kind == "check":
            class CheckWrap:
                def get(self_inner):
                    return widget._var.get()
            return CheckWrap()
        return widget  # Entry and Text already support .get()
     # -- actions ---------------------------------------------------
    def _choose_logo(self):
        path = filedialog.askopenfilename(
            title="Choose a logo image",
            filetypes=[("Image files", "*.png *.jpg *.jpeg")],
        )
        if path:
            self.logo_path = path
            self.logo_label.config(text=os.path.basename(path))

    def _generate(self):
        spec = QR_TYPES[self.type_var.get()]
        try:
            data = spec["builder"](self.active_fields)
        except Exception as exc:
            messagebox.showerror("Error", "Could not read the form: {}".format(exc))
            return

        if not data or not data.strip():
            messagebox.showwarning("Missing info", "Please fill in the details first.")
            return

        qr = qrcode.QRCode(
            version=None,
            error_correction=ERROR_CORRECT_H,  # highest correction, needed if a logo is added
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

        if self.logo_path:
            img = self._paste_logo(img, self.logo_path)

        self.current_qr_image = img
        preview = img.resize((260, 260))
        self.current_preview = ImageTk.PhotoImage(preview)
        self.preview_canvas.config(image=self.current_preview)
        self.save_btn.config(state="normal")

    @staticmethod
    def _paste_logo(qr_img, logo_path):
        qr_img = qr_img.copy()
        logo = Image.open(logo_path).convert("RGBA")
        qr_w, qr_h = qr_img.size
        logo_size = qr_w // 4
        logo.thumbnail((logo_size, logo_size))

        # white backing so the logo stays readable against the QR pattern
        pad = 10
        backing = Image.new(
            "RGBA", (logo.width + pad, logo.height + pad), "white"
        )
        backing.paste(logo, (pad // 2, pad // 2), logo)

        pos = ((qr_w - backing.width) // 2, (qr_h - backing.height) // 2)
        qr_img.paste(backing, pos, backing)
        return qr_img

    def _save(self):
        if not self.current_qr_image:
            return
        path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG image", "*.png")],
            initialfile="qr_code.png",
        )
        if path:
            self.current_qr_image.save(path)
            messagebox.showinfo("Saved", "QR code saved to:\n{}".format(path))


if __name__ == "__main__":
    app = QRApp()
    app.mainloop()


               


