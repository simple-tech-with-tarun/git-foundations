# Exercise 2: Git Flow

## Overview

Git Flow is a structured branching strategy that uses dedicated branches for feature development, release preparation, and production maintenance.

Unlike GitHub Flow, Git Flow separates ongoing development from production-ready code through long-lived `main` and `develop` branches.

This exercise simulates the Git Flow lifecycle, including feature development, release management, and production hotfixes.

## Objective

Practise the Git Flow workflow by:

- Understanding the roles of `main` and `develop`.
- Creating feature branches from `develop`.
- Integrating completed features into `develop`.
- Preparing releases using release branches.
- Publishing production releases with version tags.
- Creating hotfix branches from `main`.
- Integrating hotfixes into both `main` and `develop`.
- Cleaning up merged branches.

## Key Concepts

### Main Branch

The `main` branch represents production-ready code.

Only tested and approved releases and production hotfixes should be integrated into `main`.

### Develop Branch

The `develop` branch contains the latest integrated development changes.

Feature branches are created from `develop` and merged back into it when completed.

### Feature Branches

Feature branches isolate individual development tasks.

They are created from `develop` and merged back into `develop` through pull requests.

Naming convention: `feature/<feature-name>`

### Release Branches

Release branches are created from `develop` when the planned features for a release are complete.

They are used for release preparation, version updates, final verification, and release-related fixes.

After approval, a release branch is merged into `main` and tagged with the release version. The release changes are also integrated back into `develop`.

Naming convention: `release/<version>`

### Hotfix Branches

Hotfix branches are created from `main` to address urgent production issues.

After implementation and testing, a hotfix is merged into `main` and tagged as a new production release. It must also be integrated into `develop` to keep ongoing development synchronized.

Naming convention: `hotfix/<issue-name>`

## Workflow

### 1. Feature Development

1. Create or clone a Git repository.
2. Establish `main` and `develop` branches.
3. Create a feature branch from `develop`.
4. Implement and test the feature.
5. Commit and push the changes.
6. Open a pull request targeting `develop`.
7. Review and merge the pull request.
8. Repeat for additional features.

### 2. Release Management

1. Create a release branch from `develop`.
2. Update the project version.
3. Run the test suite and code quality checks.
4. Commit the release preparation changes.
5. Push the release branch.
6. Open a pull request targeting `main`.
7. Review and merge the release pull request.
8. Create and push an annotated version tag.
9. Publish the GitHub Release.
10. Merge the release branch back into `develop`.
11. Delete the release branch after integration.

### 3. Maintenance and Hotfixes

1. Identify and reproduce a production issue.
2. Create a hotfix branch from `main`.
3. Implement the fix and add regression tests.
4. Run the test suite and code quality checks.
5. Update the project version.
6. Push the hotfix branch.
7. Open a pull request targeting `main`.
8. Review and merge the hotfix pull request.
9. Create and push an annotated version tag.
10. Publish the GitHub Release.
11. Merge the hotfix branch into `develop`.
12. Verify the integration and remove the hotfix branch.

## Lab Scenario

You are maintaining a Python-based Incident Tracker application.

The application supports incident creation, updates, filtering, and JSON persistence through a command-line interface.

You will use Git Flow to manage feature development, prepare a production release, and resolve a production issue through a hotfix.

### Feature Development

Implement the application through separate feature branches:

- Incident creation and retrieval.
- Incident updates and filtering.
- JSON persistence.
- Command-line interface.

Each feature must be developed independently and integrated into `develop` through a pull request.

### Release 1.0.0

Prepare the first production release.

Tasks include:

- Create `release/1.0.0` from `develop`.
- Update the project version to `1.0.0`.
- Run tests and quality checks.
- Open a pull request targeting `main`.
- Merge the release.
- Create and push the `v1.0.0` tag.
- Publish the GitHub Release.
- Synchronize the release changes back into `develop`.

### Production Hotfix 1.0.1

A production issue is discovered when imported incident records contain uppercase status values.

The application rejects these records because status validation does not normalize the imported value.

Resolve the issue through a Git Flow hotfix.

Tasks include:

- Reproduce the production issue using an imported incident record.
- Create `hotfix/normalize-imported-incident-status` from `main`.
- Normalize incident status values before validation.
- Add regression tests for uppercase and mixed-case status values.
- Run the full test suite and quality checks.
- Update the project version to `1.0.1`.
- Open a pull request targeting `main`.
- Merge the hotfix.
- Create and push the `v1.0.1` tag.
- Publish the GitHub Release.
- Merge the hotfix into `develop`.
- Remove the hotfix branch after successful integration.

## Verification

Use the following commands to inspect the repository.

### Inspect Branches

    git branch -a

### Inspect Commit History

    git log --oneline --graph --all

### Inspect Version Tags

    git tag --list

### Verify Project Version

    python -c "import tomllib; print(tomllib.load(open('pyproject.toml', 'rb'))['project']['version'])"

### Run Tests

    python -m pytest -v

### Run Code Quality Checks

    python -m ruff check .
    python -m ruff format --check .

Confirm that:

- Feature branches were integrated into `develop`.
- Release `1.0.0` was merged into `main`.
- Tag `v1.0.0` exists.
- Hotfix `1.0.1` was merged into `main`.
- Tag `v1.0.1` exists.
- The hotfix was also integrated into `develop`.
- Both `main` and `develop` contain the production fix.
- The test suite and quality checks pass.
- Merged feature, release, and hotfix branches have been cleaned up.

## Key Lessons

- `main` represents production-ready code.
- `develop` provides an integration branch for ongoing development.
- Feature branches isolate individual development tasks.
- Release branches provide a controlled environment for release preparation.
- Hotfix branches allow urgent production fixes without waiting for the next planned release.
- Releases and hotfixes must be integrated back into `develop`.
- Version tags provide identifiable points in the repository's release history.
