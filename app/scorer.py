from typing import Iterable


POSITIVE_TERMS = ["romantic", "bpm", "safe", "no violence", "no explicit"]
NEGATIVE_TERMS = ["aggressive", "intense", "fast", "dramatic"]


def _score_prompt(prompt: str) -> int:
    lowered = prompt.lower()
    score = 50

    if "romantic" in lowered:
        score += 20

    bpm_bonus = 0
    if "bpm" in lowered:
        score += 10
        for bpm in range(68, 101):
            if f"bpm {bpm}" in lowered:
                bpm_bonus = 10
                break
    score += bpm_bonus

    if all(term in lowered for term in ["safe", "no violence", "no explicit"]):
        score += 15

    for word in NEGATIVE_TERMS:
        if word in lowered:
            score -= 10

    return max(0, min(100, score))


def score_pack(prompts: Iterable[str]) -> int:
    items = list(prompts)
    if not items:
        return 0
    total = sum(_score_prompt(prompt) for prompt in items)
    return round(total / len(items))


def pick_top_prompts(prompts: Iterable[str], top_n: int = 3) -> list[str]:
    scored = [(prompt, _score_prompt(prompt)) for prompt in prompts]
    scored.sort(key=lambda item: item[1], reverse=True)
    return [item[0] for item in scored[:top_n]]
