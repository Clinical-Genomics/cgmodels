from io import StringIO
from pathlib import Path

import pytest
from cgmodels.demultiplex.sample_sheet import (
    SampleSheet,
    get_sample_sheet,
    get_sample_sheet_from_file,
)
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


def test_validate_s2_sample_sheet_str():
    # GIVEN a NovaSeq S2 sample sheet
    sheet_type = "S2"
    sample_sheet_string = (
        "[Data]\n"
        "FCID,Lane,SampleID,SampleRef,index,index2,SampleName,Control,Recipe,Operator,Project\n"
        "HWHMWDMXX,1,ACC7628A68,hg19,ATTCCACACT,TGGTCTTGTT,814206,N,R1,script,814206\n"
        "HWHMWDMXX,1,ACC7628A1,hg19,AGTTAGCTGG,GATGAGAATG,814206,N,R1,script,814206"
    )

    # WHEN validating the sample sheet
    sheet: SampleSheet = get_sample_sheet(sample_sheet=sample_sheet_string, sheet_type=sheet_type)
    # THEN assert that the sample sheet has the correct type
    assert sheet.type == sheet_type


def test_validate_s2_sample_sheet_duplicate_same_lane():
    # GIVEN a NovaSeq S2 sample sheet with same sample duplicated in same lane
    sheet_type = "S2"
    sample_sheet_string = (
        "[Data]\n"
        "FCID,Lane,SampleID,SampleRef,index,index2,SampleName,Control,Recipe,Operator,Project\n"
        "HWHMWDMXX,1,ACC7628A68,hg19,ATTCCACACT,TGGTCTTGTT,814206,N,R1,script,814206\n"
        "HWHMWDMXX,1,ACC7628A1,hg19,AGTTAGCTGG,GATGAGAATG,814206,N,R1,script,814206\n"
        "HWHMWDMXX,1,ACC7628A1,hg19,GAGAGCTAAC,CAATACTTGC,814206,N,R1,script,814206\n"
    )

    # WHEN validating the sample sheet
    with pytest.raises(SampleSheetError):
        # THEN assert that a sample sheet error is raised
        get_sample_sheet(sample_sheet=sample_sheet_string, sheet_type=sheet_type)


def test_validate_s2_sample_sheet_duplicate_different_lanes():
    # GIVEN a NovaSeq S2 sample sheet with same sample duplicated in different lanes
    sheet_type = "S2"
    sample_sheet_string = (
        "[Data]\n"
        "FCID,Lane,SampleID,SampleRef,index,index2,SampleName,Control,Recipe,Operator,Project\n"
        "HWHMWDMXX,1,ACC7628A68,hg19,ATTCCACACT,TGGTCTTGTT,814206,N,R1,script,814206\n"
        "HWHMWDMXX,1,ACC7628A1,hg19,AGTTAGCTGG,GATGAGAATG,814206,N,R1,script,814206\n"
        "HWHMWDMXX,2,ACC7628A1,hg19,GAGAGCTAAC,CAATACTTGC,814206,N,R1,script,814206\n"
    )

    # WHEN validating the sample sheet
    sample_sheet: SampleSheet = get_sample_sheet(
        sample_sheet=sample_sheet_string, sheet_type=sheet_type
    )

    # THEN assert that a sample sheet is returned with samples in it
    assert sample_sheet.samples


def test_validate_s2_sample_sheet_file(s2_sheet: Path):
    # GIVEN a NovaSeq S2 sample sheet
    sheet_type = "S2"

    # WHEN validating the sample sheet
    sheet: SampleSheet = get_sample_sheet_from_file(infile=s2_sheet, sheet_type=sheet_type)

    # THEN assert that the sample sheet has the correct type
    assert sheet.type == sheet_type


def test_duplicated_sample(hiseq_dup_sheet: Path):
    # GIVEN a hiseq 2500 sample sheet with a sample that is duplicated in different lines
    sheet_type = "2500"

    # WHEN validating the sample sheet
    sample_sheet: SampleSheet = get_sample_sheet_from_file(
        infile=hiseq_dup_sheet, sheet_type=sheet_type
    )

    # THEN assert that a sample sheet with samples is returned
    assert sample_sheet.samples
