# actions-mojap-package-depends

Composite action that can run a check on whether any changes made during development to the requirements of a `mojap` package cause dependency conflicts with any of the other `mojap` packages.

## Packages included

- `mojap-metadata`
- `pydbtools`
- `data-linter`
- `s3-data-packer`
- `arrow-pd-parser`
- `gluejobutils`
- `dataengineeringutils3`

The action should be used in the the repositories of the above packages.

If you want to add to the packages included in the check you should add to [this](https://github.com/moj-analytical-services/actions-mojap-package-depends/blob/main/mojap_package_names.py#L18-L27) list in the format `({PyPI_package_name}, {repo_name})`

Example usage:

```
env:
  REPO_NAME: ${{ github.event.repository.name }} # name of repo calling the compoisite action
  ORG_REPO: ${{ github.repository }} # org/name of repo calling the composite action
  
jobs:
  build:
    name: test mojap dependencies
    runs-on: ubuntu-latest
    strategy:
        fail-fast: true
        matrix:
          python-version: [3.7, 3.8]
    steps:
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: ${{ matrix.python-version }}
      - name: check changes for conflicts with other mojap package dependencies
        uses: moj-analytical-services/actions-mojap-package-depends@main
        with:
          org-repo: ${{ env.ORG_REPO }}
          repo: ${{ env.REPO_NAME }}
```
