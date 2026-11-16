# Advanced Practice - Trunk-Based Development

## Objective

Practise realistic Trunk-Based Development scenarios using short-lived feature branches, GitHub Pull Requests, automated CI validation, and frequent integration into a shared main branch.

The Deployment Readiness Checker project was used to simulate collaborative development and common integration challenges.

## 1. Multiple Contributors

### Objective

Understand how multiple contributors can work independently while integrating their changes into a shared trunk.

### Practice

- Created separate feature branches for two contributors.
- Implemented independent changes in parallel.
- Integrated one contributor's changes through a Pull Request.
- Integrated the second contributor's changes afterward.
- Verified that both changes were present in `main`.

### Key Learning

Multiple contributors can work independently without maintaining long-lived branches.

Frequent integration reduces divergence and makes collaboration easier.

## 2. Merge Conflicts

### Objective

Understand why merge conflicts occur and how to resolve them safely.

### Practice

- Created two branches that modified the same section of a file.
- Integrated the first branch into `main`.
- Attempted to integrate the second branch.
- Reproduced the merge conflict.
- Resolved the conflict while preserving the required changes.
- Ran tests and quality checks before completing integration.

### Key Learning

Merge conflicts are a normal part of collaborative development.

The important part is resolving conflicts carefully and validating the result before integration.

## 3. Broken Trunk Recovery

### Objective

Understand how to recover when a faulty change reaches the shared trunk.

### Practice

- Introduced an intentionally incorrect production policy.
- Verified that automated tests failed.
- Integrated the faulty change to simulate a broken trunk.
- Created a corrective branch.
- Restored the expected policy using a fix-forward commit.
- Integrated the correction through a Pull Request.

### Key Learning

A broken trunk should be restored quickly.

Fix-forward adds a corrective commit without rewriting shared history.

## 4. Reverting Faulty Changes

### Objective

Learn how to safely undo an already integrated change.

### Practice

- Introduced an invalid production replica limit.
- Integrated the faulty change.
- Created a revert branch.
- Used `git revert -m 1` to reverse the merge commit.
- Validated the restored behavior.
- Integrated the revert through a Pull Request.

### Key Learning

`git revert` preserves shared history by creating a new commit that reverses an earlier change.

Avoid rewriting published shared history with commands such as `git reset`.

## 5. Feature Flags

### Objective

Understand how incomplete functionality can be integrated without activating it for users.

### Practice

- Introduced readiness scoring behind a disabled-by-default flag.
- Integrated the feature scaffolding.
- Implemented the scoring functionality in a separate short-lived branch.
- Added tests for enabled and disabled behavior.
- Integrated both changes through Pull Requests.

### Key Learning

Git integration and feature activation are separate concerns.

Feature flags allow code to reach the trunk before the functionality is enabled.

## 6. Backward-Compatible Changes

### Objective

Understand how to evolve application interfaces without breaking existing consumers.

### Practice

- Introduced an optional deployment owner field.
- Preserved compatibility for existing configuration consumers.
- Added validation for the new field.
- Tested both existing and new usage patterns.
- Integrated the change through a Pull Request.

### Key Learning

Backward-compatible changes allow teams to evolve applications incrementally.

Optional fields and safe defaults reduce the need for coordinated changes across consumers.

## 7. Keeping Trunk Releasable

### Objective

Understand how continuous validation and controlled feature integration help keep the trunk healthy.

### Practice

**Milestone 1: Release Readiness Gate**

- Introduced a release-readiness check.
- Added tests for ready and unready deployments.
- Integrated the change through a Pull Request.
- Verified CI and the complete test suite.

**Milestone 2: Incomplete Functionality Behind a Feature Flag**

- Introduced an experimental CLI flag.
- Kept the flag disabled by default.
- Verified existing CLI behavior remained unchanged.
- Added tests for both enabled and disabled states.
- Integrated through a Pull Request.
- Verified trunk health after integration.

### Key Learning

Keeping the trunk releasable requires more than successful merges.

It requires small changes, automated validation, backward compatibility, controlled feature activation, and quick recovery from failures.

## 8. GitHub Pull Request Workflow

The advanced exercises followed this integration workflow:

```text
main
 |
 +--- Create short-lived feature branch
 |             |
 |             +--- Make focused changes
 |             +--- Run local quality checks
 |             +--- Commit changes
 |             +--- Push feature branch
 |             |
 +-------------+--- Create Pull Request
                       |
                       +--- GitHub Actions CI
                       +--- Code review
                       +--- Approval
                       |
                       +--- Merge commit
                                |
                                +--- Update local main
                                +--- Verify trunk health
```

### Quality Checks

The project used the following checks:

```powershell
python -m ruff format --check .
python -m ruff check .
python -m pytest -v
```

Git checks included:

```powershell
git status -sb
git diff --check
git diff --cached --check
git log --oneline -10
```

## 9. Lessons Learned

1. Keep feature branches short-lived.
2. Integrate small changes frequently.
3. Use Pull Requests to review changes before integration.
4. Let automated CI checks validate every Pull Request.
5. Resolve merge conflicts carefully.
6. Restore broken trunk quickly using fix-forward or revert.
7. Use feature flags to control incomplete functionality.
8. Preserve backward compatibility when evolving interfaces.
9. Keep `main` healthy and ready for release.
10. Verify trunk health after every integration.

## Conclusion

Advanced Trunk-Based Development is not simply about creating and merging branches.

It is about maintaining a healthy shared trunk while multiple contributors continuously integrate changes.

**Small changes, short-lived branches, frequent integration, automated validation, and fast recovery are the foundations of a reliable trunk.**
