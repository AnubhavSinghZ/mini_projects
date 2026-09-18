import re
from datetime import date, timedelta

def extract_intent(sentence):
    sentence=sentence.lower()

    #--- Intent Detection (String Parsing)----
    