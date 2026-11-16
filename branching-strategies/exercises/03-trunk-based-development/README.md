# Exercise 03 - Trunk-Based Development

## Objective

Understand and practice Trunk-Based Development (TBD) by integrating small, focused changes frequently into a shared main branch.

This exercise uses the **Deployment Readiness Checker** project as a practical case study.

## 1. What Is Trunk-Based Development?

Trunk-Based Development is a branching strategy in which developers integrate their changes into a shared central branch (usually `main`) frequently.

Developers may work directly on `main` or use short-lived feature branches. The important principle is to avoid long-lived development branches and keep the integration trunk healthy.

### Core Principles

- `main` is the shared integration trunk.
- Feature branches are short-lived.
- Changes are small and focused.
- Integration happens frequently.
- Automated tests and quality checks protect the trunk.
- Completed feature branches are deleted after integration.
- The trunk should remain in a releasable state.

## 2. Typical Workflow

This repository practises TBD using short-lived feature branches and GitHub Pull Requests.

### Workflow Diagram

```text
main
 |
 +--- Create short-lived feature branch
 |             |
 |             +--- Make small changes
 |             +--- Run tests and quality checks
 |             +--- Commit and push
 |             |
 +-------------+--- Create Pull Request
                       |
                       +--- CI validation
                       +--- Code review
                       +--- Approval
                       |
                       +--- Merge into main
                                |
                                +--- Pull updated main
                                +--- Verify trunk health
```

### Step-by-Step Workflow

**1. Start from an updated main branch**

```powershell
git switch main
git pull --ff-only origin main
```

**2. Create a short-lived feature branch**

```powershell
git switch -c feature/my-feature
```

**3. Make a small, focused change**

Implement one logical piece of functionality.

Avoid combining unrelated changes into one branch.

**4. Run quality checks**

```powershell
python -m pytest
python -m ruff check .
python -m ruff format --check .
```

**5. Commit the change**

```powershell
git add .
git commit -m "feat: describe the change"
```

**6. Push the feature branch**

```powershell
git push -u origin feature/my-feature
```

**7. Create a Pull Request**

- Open a PR targeting `main`.
- Review the changes.
- Wait for automated CI checks.
- Address any review feedback.
- Obtain approval before merging.

**8. Merge into main**

Use the GitHub **Create a merge commit** option for this exercise.

The merge commit preserves the integration history of the feature branch.

**9. Update the local main branch**

```powershell
git switch main
git pull --ff-only origin main
```

**10. Clean up the completed feature branch**

```powershell
git branch -d feature/my-feature
```

**11. Verify repository health**

```powershell
git status -sb
git branch
git log --oneline -10
```

## 3. Practical Case Study - Deployment Readiness Checker

The Deployment Readiness Checker project was developed using short-lived feature branches and GitHub Pull Requests.

### What Was Practised?

- Building functionality through small, focused changes.
- Using short-lived feature branches.
- Keeping `main` as the integration trunk.
- Integrating changes through GitHub Pull Requests.
- Reviewing changes before integration.
- Using GitHub Actions for continuous integration.
- Running automated tests before integration.
- Using Ruff for linting and formatting checks.
- Recovering from broken integrations.
- Reverting faulty changes without rewriting shared history.
- Keeping incomplete functionality behind disabled feature flags.
- Verifying that `main` remained clean and synchronized with `origin/main`.

### Project Milestones

The project evolved through these major areas:

1. Deployment Configuration Model
2. Deployment Configuration Validation
3. CLI Interface
4. JSON Configuration Support
5. Deployment Readiness Evaluation
6. CLI Readiness Integration
7. Deployment Resource Validation
8. Environment-Specific Deployment Policies
9. Deployment Readiness JSON Reports
10. Documentation and End-to-End Testing
11. Maximum Replica Policies
12. Text Readiness Reports
13. Readiness Scoring
14. Optional Deployment Owner Metadata
15. Release Readiness Gate
16. Experimental Insights Feature Flag

The project reached 94 passing tests, with Ruff linting and formatting checks passing.

## 4. Advanced Trunk-Based Development Scenarios

The following scenarios were practised using the Deployment Readiness Checker project.

| Scenario | What Was Practised |
|---|---|
| Multiple contributors | Integrating parallel feature branches into a shared trunk |
| Merge conflicts | Resolving conflicting changes before integration |
| Broken trunk recovery | Restoring a failing trunk using fix-forward |
| Reverting faulty changes | Using `git revert` to undo an integrated change |
| Feature flags | Integrating functionality safely while keeping it disabled |
| Backward compatibility | Evolving interfaces without breaking existing consumers |
| Keeping trunk releasable | Maintaining a healthy trunk through continuous validation |

See [advanced-practice.md](advanced-practice.md) for the detailed scenarios, Git workflows, and lessons learned.

## 5. Important Lessons from Advanced Practice

### Multiple Contributors

Multiple developers can work independently on short-lived branches while integrating their work frequently into the same trunk.

### Merge Conflicts

Merge conflicts are a normal part of collaborative development. Resolve them carefully, validate the result, and integrate without losing another contributor's changes.

### Broken Trunk Recovery

When an integration breaks the trunk, prioritize restoring its health.

A fix-forward approach adds a corrective commit without rewriting shared history.

### Reverting Faulty Changes

`git revert` creates a new commit that reverses an earlier change.

It is safer for shared branches than rewriting published history with commands such as `git reset`.

### Feature Flags

Feature flags separate code integration from feature activation.

Incomplete functionality can be integrated into `main` while remaining disabled until it is ready.

### Backward Compatibility

Changes to shared interfaces should preserve existing consumers whenever possible.

Optional fields and compatible defaults help teams evolve applications without forcing simultaneous changes across all consumers.

### Keeping Trunk Releasable

A healthy trunk requires:

- Small and frequent integrations.
- Automated CI checks.
- Passing tests.
- Code review.
- Backward-compatible changes.
- Controlled feature activation.
- Fast recovery from faulty integrations.

## 6. When Is Trunk-Based Development Useful?

TBD works particularly well when teams can integrate small changes frequently and have reliable automated testing.

It supports:

- Continuous integration.
- Frequent releases.
- Short feedback cycles.
- Reduced long-lived branch divergence.
- Shared ownership of integration quality.
- Faster detection and recovery from integration problems.

TBD does not mean skipping testing or integrating unfinished functionality carelessly.

Feature flags, backward-compatible changes, automated validation, and short-lived branches help keep integration safe.

## Key Takeaway

**Keep the trunk healthy, make small changes, integrate frequently, and use automation to protect every integration.**

The goal is not simply to merge branches quickly. It is to maintain a consistently healthy and releasable `main` branch.
