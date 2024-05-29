from enum import Enum


class SeriesTimerInfoDtoDayPattern(str, Enum):
    DAILY = "Daily"
    WEEKDAYS = "Weekdays"
    WEEKENDS = "Weekends"

    def __str__(self) -> str:
        return str(self.value)
