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

def _contain_word(sentence:str, words:list)->bool:
    """Check if any word/phrase in `words` appear in `sentence` as a whole word. """
    return any(re.search(rf"\b{re.escape(w)}\b", sentence) for w in words)

def _extract_duration(sentence:str)-> Optional[int]:
    """
    Find a duration like '30 min' or '1 hour' and convert it to minutes.
    Returns None if no duration is mentioned.
    """
    match = DURATION_PATTERN.search(sentence)
    if not match:
        return None
    amount = int(match.group(1))
    unit = match.group(2)

    # Converts hours to minutes so everything is in one consistent unit
    if unit.startswith("hr") or unit.startswith("hour"):
        return amount*60
    return amount


def _extract_date(sentence: str) -> str:
    """Figure out which day this log entry refers to."""
    if "yesterday" in sentence:
        return(date.today()- timedelta(days=1)).isoformat()
    #default to today if no date word is found(habits are usually logged same-day)
    return date.today().isoformat()

def _extract_habit_name(sentence: str, duration_match:Optional[re.Match]) -> str:
    """
    Strip out status words, date words, and duration mentions,
    leaving just the habit itself (e.g. 'yoga').
    """
    title = sentence

    # Remove the duration phrase first (e.g. "30 min") so its number don't linger
    if duration_match:
        title=title.replace(duration_match.grooup(0), "")

        #Remove All kknown filler words
    for word in STRIP_WORDS:
        title= re.sub(rf"\b{re.escape(word)}\b", "", title )

        # clean up leftover extraspaces and pumctuation
    title=re.sub(r"\s+", " ", title).strip(" ,.")
    return title

def extract_habit_log(sentence: str) -> Dict[str, Any]:
    """
    Parse a natural-language habit log sentence into structured data.

    Example:
        extract_habit_log("did 30 min yoga today")
        -> {'habit': 'yoga', 'status': 'done', 'duration_minutes': 30, 'date': '2026-09-19'}
    """