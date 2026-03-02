from typing import Dict, List


ROMANTIC_TEMPLATE = (
    "Romantic Kitchen cinematic scene, {scene}, {mood}, {camera}, "
    "BPM {bpm}, warm tungsten lighting, cozy textures, gentle motion, "
    "safe for all audiences, no violence, no explicit content"
)


KEYWORD_EXPANSION: Dict[str, List[str]] = {
    "pasta": ["fresh pasta dough tossed in olive oil", "steam rising from handmade fettuccine"],
    "wine": ["ruby wine swirl in crystal glass", "intimate toast by candlelight"],
    "rain": ["rain drops on window beside kitchen island", "soft thunder ambience outside"],
    "dessert": ["strawberry tart plating close-up", "chocolate drizzle over plated dessert"],
    "morning": ["sunrise glow through linen curtains", "coffee pour-over with heart-shaped foam"],
    "jazz": ["vinyl jazz record spinning gently", "subtle saxophone rhythm in background"],
}


def expand_scenes_from_keywords(base_text: str) -> List[str]:
    lowered = base_text.lower()
    scenes: List[str] = []
    for keyword, mapped_scenes in KEYWORD_EXPANSION.items():
        if keyword in lowered:
            scenes.extend(mapped_scenes)

    if not scenes:
        scenes = [
            "couple preparing dinner together at marble island",
            "hands brushing while passing a wooden spoon",
            "candlelit table set with handwritten love note",
        ]
    return scenes


def generate_prompt_candidates(source_text: str, total: int = 12) -> List[str]:
    scenes = expand_scenes_from_keywords(source_text)
    moods = [
        "tender romantic atmosphere",
        "dreamy intimate mood",
        "playful affectionate tone",
        "nostalgic love story feeling",
    ]
    cameras = [
        "35mm close-up rack focus",
        "slow dolly-in with shallow depth of field",
        "overhead food styling shot",
        "handheld natural movement",
    ]
    bpm_values = [72, 78, 82, 88, 90, 96]

    prompts: List[str] = []
    idx = 0
    while len(prompts) < total:
        scene = scenes[idx % len(scenes)]
        mood = moods[idx % len(moods)]
        camera = cameras[idx % len(cameras)]
        bpm = bpm_values[idx % len(bpm_values)]
        prompt = ROMANTIC_TEMPLATE.format(scene=scene, mood=mood, camera=camera, bpm=bpm)
        prompts.append(prompt)
        idx += 1

    return prompts
