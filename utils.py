import json


def load_candidates_from_json():
    """Возвращает список всех кандидатов"""
    path = "candidates.json"
    with open(path, 'r', encoding='utf-8') as data:
        candidates = json.loads(data.read())
        return candidates


def get_candidate(candidate_id):
    """Возвращает одного кандидата по его id"""

    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate["num"] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    """Возвращает кандидатов по имени"""

    candidates = load_candidates_from_json()
    candidate_list = []
    for candidate in candidates:
        if candidate_name.lower() in candidate["name"].lower():
            candidate_list.append(candidate)
    return candidate_list


def get_candidates_by_skill(skill_name):
    """Возвращает кандидатов по навыку"""

    candidates = load_candidates_from_json()
    candidate_by_skill = []
    for candidate in candidates:
        if skill_name.lower() in [skill.lower() for skill in candidate['skills'].split(', ')]:
            candidate_by_skill.append(candidate)
    return candidate_by_skill
