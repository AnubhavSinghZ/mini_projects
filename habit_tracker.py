import re
from datetime import date, timedelta
from typing import Optional, Dict, Any

# ___ Keyword lists (easy to extend later)___

COMPLETION_WORDS=["did", "done", "finished0", "completed"]
SKIPPED_WORDS=["skipped","missed", "didn't do", "did not do"]

# Regex to catch a duration like "30 min", "1 hour", "45 minutes"
DURATION_PATTERN=re.compile(r"(\d+)\s*(min|mins|minute|minutes|hr|hrs|hour|hours)")

# Words we strip out at the end to leave just the habit name
STRIP_WORDS=[
    "did", "done", "finished", "completed",
    "skipped", "missed", "didn't do", "did not do",
    "today", "yesterday", "for", "of", "min", "mins",
    "minute", "minutes", "hr", "hrs", "hour", "hours",
]