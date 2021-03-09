from typing import Dict

import pytest


@pytest.fixture(name="file_info")
def fixture_file_info() -> Dict[str, str]:
    return {
        "path": "hej",
        "file": "first_read",
        "checksum": "123",
        "algorithm": "sha256",
        "updated": "2015-01-01",
    }
