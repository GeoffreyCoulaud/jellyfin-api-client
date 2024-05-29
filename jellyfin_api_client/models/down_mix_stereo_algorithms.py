from enum import Enum


class DownMixStereoAlgorithms(str, Enum):
    DAVE750 = "Dave750"
    NIGHTMODEDIALOGUE = "NightmodeDialogue"
    NONE = "None"

    def __str__(self) -> str:
        return str(self.value)
