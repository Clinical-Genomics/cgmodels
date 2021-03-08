import datetime
from typing import Dict

import pytest
from cgmodels.crunchy.metadata import CrunchyFile, CrunchyMetadata
from pydantic import ValidationError


def test_crunchy_file_schema(file_info: Dict[str, str]):
    # GIVEN some file metadata

    # WHEN creating a file object
    file_obj = CrunchyFile(**file_info)

    # THEN assert that it has been converted as expected
    assert isinstance(file_obj.updated, datetime.date)


def test_crunchy_file_schema_malformed_date(file_info: Dict[str, str]):
    # GIVEN some file metadata where the date format is wrong
    file_info["updated"] = "2015-111-01"

    # WHEN creating a file object
    with pytest.raises(ValidationError):
        # THEN assert that a validation error is raised
        CrunchyFile(**file_info)
