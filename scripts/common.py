def enquote(text, use_tex):
    if use_tex:
        return f"``{text}''"
    else:
        return f'"{text}"'


LABEL_DICT = {
    "WORK": "Workload",
    "LEVL": "Level",
    "ASS1": "Assignment 1",
    "ASS2": "Assignment 2",
    "ASS3": "Assignment 3",
    "ASS4": "Assignment 4",
    "ILAL": "Taught me a lot",
    "INTC": "Was intellectually challenging",
    "CSTR": "Was clearly structured",
    "FACT": "Factual knowledge",
    "FUND": "Fundamental principles",
    "CURR": "Current scientific theories",
    "APPL": "To apply subject matter",
    "PROF": "Professional skills",
    "TECH": "Technical skills",
}

AGREE_DISAGREE_SCALE = [
    "Firmly Disagree",
    "Disagree",
    "Neutral",
    "Agree",
    "Firmly Agree",
]

RIGHTNESS_SCALE = ["Too Low", "Low", "Just Right", "High", "Too High"]
