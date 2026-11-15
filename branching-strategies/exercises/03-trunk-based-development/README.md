# Exercise 03 - Trunk-Based Development

## Objective

Understand and practice Trunk-Based Development (TBD) by integrating small, focused changes frequently into a shared main branch.

This exercise uses the completed **Deployment Readiness Checker** project as a practical case study.

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

This repository practices TBD using short-lived feature branches and fast-forward-only integration.

### Workflow Diagram

```text
main
 |
 +--- feature/feature-one
 |          |
 |          +--- commit
 |          +--- commit
 |          |
 +----------+  fast-forward merge
 |
 +--- feature/feature-two
 |          |
 |          +--- commit
 |          |
 +----------+  fast-forward merge
 |
main remains the integration trunk
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

**6. Integrate into main**

```powershell
git switch main
git merge --ff-only feature/my-feature
```

**7. Push the integration trunk**

```powershell
git push origin main
```

**8. Delete the completed feature branch**

```powershell
git branch -d feature/my-feature
```

**9. Verify repository health**

```powershell
git status -sb
git branch
git log --oneline -10
```

## 3. Practical Case Study - Deployment Readiness Checker

The Deployment Readiness Checker project was developed using this workflow.

### What Was Practiced?

- Building functionality through small, focused features.
- Using short-lived feature branches.
- Keeping `main` as the integration trunk.
- Integrating changes using fast-forward-only merges.
- Running automated tests before integration.
- Using Ruff for linting and formatting checks.
- Pushing integrated changes to GitHub.
- Deleting completed feature branches.
- Verifying that `main` was clean and synchronized with `origin/main`.

### Project Milestones

Ten features were implemented and integrated:

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

The final integration passed all 70 tests, Ruff linting, and formatting checks.

### Important Lessons

- Frequent integration reduces the amount of change accumulated between integrations.
- Small commits make changes easier to review and troubleshoot.
- Automated checks help detect problems before they reach the trunk.
- Fast-forward-only merges preserve a linear integration history.
- A clean working tree and synchronized remote branch provide useful evidence of repository health.

## 4. Advanced Scenarios to Practice

The next stage is to simulate realistic team development situations.

| Scenario | Learning objective |
|---|---|
| Multiple contributors | Integrate parallel work into one trunk |
| Merge conflicts | Resolve competing changes safely |
| Broken trunk | Diagnose and restore a failing integration branch |
| Faulty changes | Revert an integrated commit |
| Feature flags | Integrate incomplete functionality safely |
| Backward compatibility | Evolve interfaces without breaking existing consumers |
| Continuous integration | Automatically validate every integration |

## 5. When Is Trunk-Based Development Useful?

TBD works particularly well when teams can integrate small changes frequently and have reliable automated testing.

It supports:

- Continuous integration.
- Frequent releases.
- Short feedback cycles.
- Reduced long-lived branch divergence.
- Shared ownership of integration quality.

TBD does not mean skipping testing or integrating unfinished functionality carelessly. Feature flags and backward-compatible changes help keep incomplete work safe.

## Key Takeaway

**Keep the trunk healthy, make small changes, integrate frequently, and use automation to protect every integration.**

The goal is not simply to merge branches quickly. It is to maintain a consistently healthy and releasable main branch.
