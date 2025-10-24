import re

COURSE_ID_PATTERN = re.compile(r"^[A-Za-z0-9_-]{3,64}$")

def normalize_course_id(raw: str) -> str:
    cleaned = " ".join(raw.strip().split())
    return cleaned.replace(" ", "-")

def is_valid_course_id(course_id: str) -> bool:
    return bool(COURSE_ID_PATTERN.match(course_id))

def validate_and_normalize_course_id(raw: str) -> str:
    cid = normalize_course_id(raw)
    if not is_valid_course_id(cid):
        raise ValueError("Invalid course_id format. Use 3-64 chars: letters, numbers, _ or -")
    return cid
