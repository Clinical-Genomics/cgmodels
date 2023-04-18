# Change Log

<!---
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

About changelog [here](https://keepachangelog.com/en/1.0.0/)

Please add a new candidate release at the top after changing the latest one. Feel free to copy paste from the "squash and commit" box that gets generated when creating PRs

Try to use the following format:

## [x.x.x]
### Added
### Changed
### Fixed
-->

## [0.12.0]

### Added [cg]
- Adds taxprofiler to pipeline options
## [0.11.0]
### Added [cg]
- Adds RNAFUSION to pipeline options

## [0.10.2]
### Changed [cg]
- Adds BALSAMIC-PON to pipeline options

## [0.10.1]
### Changed [cg]
- Adds BALSAMIC-QC to pipeline options

## [0.9.0]
### Changed [cg]
- Adds Balsamic-UMI to pipeline options

## [0.8.1]
### Fixed
fix unbumped pyproject.toml

## [0.8.0]
### Added
Sample sheet validation models for both bcl2fastq and dragen

## [0.7.0]
### Changed [cg]
- Adds spring to pipeline options
- Adds rsync to pipeline options

## [0.6.0]
### Changed [cg]
- Adds demultiplex to pipeline options

## [0.5.0]
### Changed [demultiplexing]
- Allow sample ids to be duplicated if not in same lane

### Added
- Functionality to parse sample sheet from string or file with different functions
- Functionality to parse sample sheets with more complicated headers


## [0.4.1]
### Fixed
- Small bug in `demultiplex/get_sample_sheet`

## [0.4.0]
### Added
- Pipeline class definition for communication between cg and hermes

## [0.3.0]
### Added

- Base class for sample and headers to facilitate creation of sample sheets

## [0.2.2]
### Fixed

- So that not all files in crunchy metadata need `checksum` and `algorithm`

## [0.2.1]

- This got lost :)

## [0.2.0]
### Added

- Workflow for publish to pypi
- Workflow for CI
- Workflow for changelog reminder
- Model for the crunchy metadata file


## [0.1.0]
### Added
- Models for SampleSheets
