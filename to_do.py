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


    # --- Title extraction (strip the trigger phrase, keep the rest) ---
    title=re.sub(r"(remind me to | add | i need to)","", sentence)
    title=re.sub(r"(tomorrow | today | urgent | asap | important | in \d+ days?)", "", title)
    title=title.strip(",.")

    return {"intent": intent, "title": title, "priority": priority, "due": due}

print(extract_intent("remind me to buy milk tomorrow, it's urgent"))