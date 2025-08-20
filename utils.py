def filter_seekers(skill, location, urgency, seekers, status):
    results = []
    for s in seekers:
        if not status.get(s["name"], False):
            continue
        if skill and skill.lower() not in s["skills"]:
            continue
        if location and location.lower() != s["location"].lower():
            continue
        if urgency != "All" and s["urgency"] != urgency:
            continue
        results.append(s)
    return results
