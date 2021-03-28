from pathlib import Path

import pytest
from cgmodels.demultiplex.sample_sheet import SampleSheet, get_sample_sheet_from_file
from cgmodels.exceptions import SampleSheetError


def test_validate_hiseq_sample_sheet(hiseq_sample_sheet: Path):
    # GIVEN a hiseq 2500 sample sheet
    sheet_type = "2500"

    # WHEN validating the sample sheet
    sheet: SampleSheet = get_sample_sheet_from_file(
        infile=hiseq_sample_sheet, sheet_type=sheet_type
    )

    # THEN assert that the sample sheet has the correct type
    assert sheet.type == sheet_type


def test_validate_s2_sample_sheet(s2_sheet: Path):
    # GIVEN a NovaSeq S2 sample sheet
    sheet_type = "S2"

    # WHEN validating the sample sheet
    sheet: SampleSheet = get_sample_sheet_from_file(infile=s2_sheet, sheet_type=sheet_type)

    # THEN assert that the sample sheet has the correct type
    assert sheet.type == sheet_type


def test_duplicated_sample(hiseq_dup_sheet: Path):
    # GIVEN a hiseq 2500 sample sheet with a duplicated sample
    sheet_type = "2500"

    # WHEN validating the sample sheet
    with pytest.raises(SampleSheetError):
        # THEN assert that a sample sheet exception is raised
        get_sample_sheet_from_file(infile=hiseq_dup_sheet, sheet_type=sheet_type)
