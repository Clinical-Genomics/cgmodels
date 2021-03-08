from datetime import date, datetime
from typing import List

from pydantic import BaseModel
from typing_extensions import Literal


class CrunchyFile(BaseModel):
    path: str
    file: Literal["first_read", "second_read", "spring"]
    checksum: str
    algorithm: str
    updated: date


class CrunchyMetadata(BaseModel):
    files: List[CrunchyFile]


if __name__ == "__main__":
    file_info = {
        "path": "hej",
        "file": "first_read",
        "checksum": "123",
        "algorithm": "sha256",
        "updated": "2015-01-01",
    }
    file_obj = CrunchyFile(**file_info)
    print(file_obj.json())
