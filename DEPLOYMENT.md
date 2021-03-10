# Deployment guide
This includes instructions for deploying **cgmodels**. **cgmodels** is only a library which means it does not need to be
deployed on any server, it only needs a version bump. When pushing a new tag to github a distribution will be created 
and published on [pypi][pypi] 
General instructions for deployment is in the [development guide][development-guide]

## Branch model

**cgmodels** is following the [GitHub flow][gh-flow] branching model which means that every time a PR is merged to 
master a new release is created.

## Requirements

- [poetry]

## Steps

1. Check in the PR if the change is a minor, mayor or patch: ![Version][pr-version]
1. Make sure you are on `master` (`git checkout master`) and bump version according to step 1 with git, example: `git tag 0.2.0`
1. Push the commit: `git push --tags`
1. Great job :whale2:


[pypi]: https://pypi.org/project/cgmodels/
[poetry]: https://python-poetry.org/docs/#installation
[pr-version]: docs/img/version.png
[confirm-deploy]: docs/img/confirm_deploy.png
[development-guide]: http://www.clinicalgenomics.se/development/publish/prod/
[gh-flow]: http://www.clinicalgenomics.se/development/dev/models/#rolling-release-github-flow