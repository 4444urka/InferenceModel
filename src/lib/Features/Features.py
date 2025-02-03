from pydantic import BaseModel

class Features(BaseModel):
    totsp: int
    livesp: int
    kitsp: int
    dist: float
    metrdist: int
    walk: int
    brick: int
    floor: int