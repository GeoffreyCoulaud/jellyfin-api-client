from enum import Enum


class PlayerStateInfoPlayMethod(str, Enum):
    DIRECTPLAY = "DirectPlay"
    DIRECTSTREAM = "DirectStream"
    TRANSCODE = "Transcode"

    def __str__(self) -> str:
        return str(self.value)
