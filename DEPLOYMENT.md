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
1. Make sure you are on `main` (`git checkout main`)
1. Bump the package version with poetry like: `poetry version pathch|minor|mayor` and commit the changes
1. Bump version according to step 1 with git, example: `git tag -a 0.2.0 -m "Fix another thing"`
1. Push the commit and the tags: 
    - `git push`
    - `git push --tag`
1. Great job :whale2:


[pypi]: https://pypi.org/project/cgmodels/
[poetry]: https://python-poetry.org/docs/#installation
[pr-version]: docs/img/version.png
[confirm-deploy]: docs/img/confirm_deploy.png
[development-guide]: http://www.clinicalgenomics.se/development/publish/prod/
[gh-flow]: http://www.clinicalgenomics.se/development/dev/models/#rolling-release-github-flow
