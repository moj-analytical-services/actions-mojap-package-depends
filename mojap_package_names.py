import argparse


parser = argparse.ArgumentParser(
    description="gets packages minus package of repo test is run on"
)

parser.add_argument(
    "--repo",
    help="the name of the github repository calling the action"
)

args = parser.parse_args()

repo_name = args.repo

# list of packages included in this test
# (pypi-name, repo-name)
mojap_packages = [
    ("mojap-metadata", "mojap-metadata"),
    ("pydbtools", "pydbtools"),
    ("data-linter", "data_linter"),
    ("s3-data-packer", "s3_data_packer"),
    ("arrow-pd-parser", "mojap-arrow-pd-parser"),
    ("gluejobutils", "gluejobutils"),
    ("dataengineeringutils3", "dataengineeringutils3"),
    ("iam-builder", "iam_builder")
]

packages_to_install = [p[0] for p in mojap_packages if p[1] != repo_name]

print("pip install " + " ".join(packages_to_install))
