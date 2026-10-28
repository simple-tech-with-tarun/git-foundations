import json
import re
from pathlib import Path

CONFIG_PATH = Path(__file__).parent / "config" / "release.json"


def load_release_metadata():
    with CONFIG_PATH.open(encoding="utf-8") as config_file:
        return json.load(config_file)


def load_release_policy():
    policy_path = Path(__file__).parent / "config" / "release-policy.json"

    with policy_path.open(encoding="utf-8") as policy_file:
        return json.load(policy_file)


def validate_version(version):
    return bool(re.fullmatch(r"\d+\.\d+\.\d+", version))


def display_release_summary():
    release = load_release_metadata()
    policy = load_release_policy()

    if policy["require_version_validation"] and not validate_version(
        release["version"]
    ):
        raise ValueError(f"Invalid release version: {release['version']}")

    if release["channel"] not in policy["allowed_channels"]:
        raise ValueError(f"Invalid release channel: {release['channel']}")

    print("Release Summary")
    print("---------------")
    print(f"Name: {release['name']}")
    print(f"Version: {release['version']}")
    print(f"Channel: {release['channel']}")
    print(f"Target branch: {release['target_branch']}")


if __name__ == "__main__":
    display_release_summary()
