# Exercise 1: GitHub Flow

## Overview

GitHub Flow is a lightweight branching strategy designed around short-lived feature branches and pull requests.

Developers create a branch for each change, commit their work, and open a pull request to review and discuss the proposed changes. Once approved, the branch is merged into the main branch.

This exercise simulates a typical GitHub Flow workflow, from creating a feature branch to merging it back into main.

## Objective

Practise the GitHub Flow workflow by:

- Creating a short-lived feature branch from `main`.
- Making and committing a focused change.
- Pushing the feature branch to a remote repository.
- Opening a pull request for review.
- Merging the pull request into `main`.
- Removing the feature branch after successful integration.

## Key Concept

In GitHub Flow, `main` should remain in a deployable state. All changes are developed in short-lived branches and integrated through pull requests.

## Workflow

1. Create and clone a GitHub repository with a `main` branch.
2. Create a feature branch from the latest `main`.
3. Make a small, focused change.
4. Commit the change with a descriptive message.
5. Push the feature branch to the remote repository.
6. Open a pull request targeting `main`.
7. Review and merge the pull request.
8. Update the local `main` branch and remove the merged feature branch.

## Expected Outcome

The feature change is integrated into `main` through a pull request.

The feature branch is no longer needed after successful integration.

## Lab Scenario

You are working on a small Python application that maintains deployment environment configurations.

A team member needs to introduce support for development, staging, and production environments.

You will implement this change using GitHub Flow.

### Sample Change

Add a `deployment_environments.py` script containing:

- Development environment configuration.
- Staging environment configuration.
- Production environment configuration.
- A function to display the configured environments.

The script should be executable and follow basic Python code quality practices.

### Tasks

1. Create a separate GitHub repository for the lab.
2. Clone the repository locally.
3. Create a feature branch named `feature/deployment-environments`.
4. Implement the deployment environment configuration script.
5. Execute the script and validate its output.
6. Run Ruff linting and formatting checks.
7. Commit and push the change.
8. Open a pull request against `main`.
9. Review and merge the pull request.
10. Verify the change in `main`.

## Verification

After completing the workflow, verify the following:

### Inspect Branches

```powershell
git branch -a
```

### Inspect Commit History

```powershell
git log --oneline --graph --all
```

### Verify the Integrated Change

```powershell
git switch main
git pull origin main
git show HEAD:deployment_environments.py
python .\deployment_environments.py
```

Confirm that:

- The feature branch was merged into `main`.
- The deployment environment script exists in `main`.
- The script executes successfully.
- The remote repository reflects the merged change.
- The feature branch has been removed after merging.

## Key Lessons

- Short-lived feature branches isolate individual changes.
- Pull requests provide a place for collaboration and code review.
- Changes are integrated into `main` through pull requests.
- Keeping `main` deployable is a central GitHub Flow principle.
