import json
import re
from pathlib import Path

CONFIG_PATH = Path(__file__).parent / "config" / "release.json"


def load_release_metadata():
    with CONFIG_PATH.open(encoding="utf-8") as config_file:
        return json.load(config_file)


def validate_version(version):
    return bool(re.fullmatch(r"\d+\.\d+\.\d+", version))


def display_release_summary():
    release = load_release_metadata()

    if not validate_version(release["version"]):
        raise ValueError(f"Invalid release version: {release['version']}")

    print("Release Summary")
    print("---------------")
    print(f"Name: {release['name']}")
    print(f"Version: {release['version']}")
    print(f"Channel: {release['channel']}")
    print(f"Target branch: {release['target_branch']}")


if __name__ == "__main__":
    display_release_summary()
