from enum import Enum


class VideoRangeType(str, Enum):
    DOVI = "DOVI"
    DOVIWITHHDR10 = "DOVIWithHDR10"
    DOVIWITHHLG = "DOVIWithHLG"
    DOVIWITHSDR = "DOVIWithSDR"
    HDR10 = "HDR10"
    HDR10PLUS = "HDR10Plus"
    HLG = "HLG"
    SDR = "SDR"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
