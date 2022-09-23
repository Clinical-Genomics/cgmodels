from enum import Enum


class StrEnum(str, Enum):
    def __str__(self) -> str:
        return str.__str__(self)


class AnalysisTypes(StrEnum):
    WGS: str = "wgs"
    WES: str = "wes"
    TGS: str = "tgs"
    RNA: str = "rna"
    OTHER: str = "other"
