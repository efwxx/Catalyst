from dataclasses import dataclass

@dataclass
class OsuMap():
    beatmap_id : int
    beatmapset_id : int
    allowed_responses : list
