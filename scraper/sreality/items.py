from dataclasses import dataclass


@dataclass(frozen=True)
class Flat:
    title: str
    image_url: str
