import re
from datetime import date, timedelta

def extract_intent(sentence):
    sentence=sentence.lower()

    #--- Intent Detection (String Parsing)----
    if any(w in sentence for w in["remind me to", "add", "i need to"]):
        intent="add"
    elif any(w in sentence for w in["done", "finished", "completed"]):
        intent="done"
    elif any(w in sentence for w in["delete", "remove", "cancel"]):
        intent="delete"
    else:
        intent="unknown"

    # --- Priority Detection---
    priority="high" if any(w in sentence for w in["urgent", "asap", "important",]) else "medium"

    # Date Manipulation

    if "tomorrow" in sentence:
        due = (date.today()+timedelta(days=1)).isoformat()
    elif "today" in sentence:
        due = date.today().isoformat()
    else:
        match = re.search(r"in(\d+) days?", sentence)
        if match:
            due= (date.today()+ timedelta(days=int(match.group(1)))).isoformat()
