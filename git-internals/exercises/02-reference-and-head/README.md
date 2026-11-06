# Exercise 2: References and HEAD

## Overview

Explore how Git manages references, how `HEAD` identifies the current position in the repository, and how branch pointers move as commits and other operations are performed.

This exercise covers symbolic references, detached HEAD states, reference manipulation, reflog investigation, and recovery of commits that are no longer referenced by a branch.

## Learning Objectives

By completing this exercise, you will be able to:

- Identify local branches, remote-tracking branches, and other references.
- Understand the relationship between `HEAD` and branch references.
- Distinguish attached HEAD from detached HEAD.
- Inspect branch reference movement.
- Understand how reflogs record reference updates.
- Recover commits using reflog entries.
- Manipulate references directly with `git update-ref`.

## Topics Covered

### 1. Git References

- Local branch references under `refs/heads/`.
- Remote-tracking references under `refs/remotes/`.
- Stash reference under `refs/stash`.
- Symbolic references and reference resolution.

### 2. HEAD and Symbolic References

- How `HEAD` identifies the current branch.
- Contents of `.git/HEAD`.
- `git symbolic-ref`.
- `git rev-parse`.
- Attached and detached HEAD states.

### 3. Branch Reference Movement

- How commits advance branch references.
- How `git reset` moves the current branch reference.
- How reference updates affect `HEAD` and other branches.
- Direct reference manipulation using `git update-ref`.

### 4. Reflog Investigation and Recovery

- Inspecting HEAD and individual branch reflogs.
- Understanding reference movement history.
- Resolving historical positions using reflog selectors.
- Recovering commits by creating branches at previous positions.

## Practical Exercises

### Exercise 1: Explore Repository References

Inspect the references available in the repository.

```powershell
git show-ref
git show-ref --heads
git symbolic-ref HEAD
git symbolic-ref --short HEAD
git rev-parse HEAD
git rev-parse --symbolic-full-name HEAD
```

Inspect the contents of the HEAD file and a local branch reference.

```powershell
Get-Content .\.git\HEAD
Get-Content .\.git\refs\heads\feature\git-internals
```

**What to remember:**
- Local branches are stored under `refs/heads/`.
- Remote-tracking branches are stored under `refs/remotes/`.
- `HEAD` normally contains a symbolic reference to the current branch.
- `git rev-parse` resolves references to their underlying commit IDs.

### Exercise 2: Observe Branch Reference Movement

Create an isolated lab branch and inspect its initial position.

```powershell
git switch -c lab/reference-movement
git rev-parse HEAD
git rev-parse refs/heads/lab/reference-movement
```

Create a commit and inspect the updated reference.

```powershell
git commit --allow-empty -m "lab: observe branch reference movement"
git rev-parse HEAD
git reflog show lab/reference-movement
```

Move the branch backward using `git reset --hard` and inspect the resulting reference movement.

```powershell
git reset --hard HEAD~1
git reflog show -n 5 lab/reference-movement
```

The branch was accidentally moved back one additional commit during the experiment. The reflog was used to identify the intended commit and restore the branch position.

```powershell
git reset --hard 356772c
git rev-parse HEAD
git reflog show -n 5 lab/reference-movement
```

The original experimental commit (`c54badd`) remained recoverable through the reflog and was preserved on `recovery/reference-movement`.

**What to remember:**
- A branch is a movable reference to a commit.
- Creating a commit on an attached branch advances that branch reference.
- Resetting can move the current branch reference to an earlier commit.
- The reflog records previous reference positions.

### Exercise 3: Inspect HEAD and Detached HEAD

Inspect the current symbolic reference.

```powershell
git symbolic-ref HEAD
git branch --show-current
```

Enter detached HEAD state.

```powershell
git switch --detach 356772c
```

Inspect the resulting state.

```powershell
git symbolic-ref HEAD
git rev-parse HEAD
git branch --show-current
Get-Content .\.git\HEAD
```

In detached HEAD state, `git symbolic-ref HEAD` fails because HEAD points directly to a commit rather than symbolically referencing a branch.

Create a commit while detached.

```powershell
git commit --allow-empty -m "lab: create commit in detached HEAD state"
```

Return to a branch and inspect the reflog.

```powershell
git switch lab/reference-movement
git reflog -n 8
```

**What to remember:**
- In attached state, `HEAD` points symbolically to a branch.
- In detached state, `HEAD` contains a commit ID directly.
- Commits created while detached are not automatically attached to a branch.
- The HEAD reflog can help locate commits created in detached state.

### Exercise 4: Recover Previous Reference Positions

Inspect the reflog to locate the earlier lab commit and detached HEAD commit.

```powershell
git reflog
```

Identify the relevant commit IDs from the reflog. Reflog selectors such as `HEAD@{3}` are relative to the current reflog and can change as new operations occur.

Resolve a selected reflog entry when needed.

```powershell
git rev-parse "HEAD@{3}"
```

Create a recovery branch at the recovered commit.

```powershell
git branch recovery/reference-movement c54badd
```

Recover the detached HEAD commit using its reflog entry.

```powershell
git branch recovery/detached-head "HEAD@{1}"
```

Verify the recovered history.

```powershell
git log --oneline -3 recovery/reference-movement
git log --oneline -3 recovery/detached-head
```

**What to remember:**
- Reflogs retain historical reference positions.
- Reflog selectors are relative to the current reflog and may change as new operations occur.
- A commit can be recovered by creating a branch at its commit ID.
- Recovery branches preserve commits independently of the original branch.

### Exercise 5: Manipulate References with git update-ref

Create an isolated branch at a known commit.

```powershell
git branch lab/update-ref 356772c
```

Move the reference directly.

```powershell
git update-ref refs/heads/lab/update-ref c54badd
```

Verify the reference.

```powershell
git rev-parse lab/update-ref
git show-ref --verify refs/heads/lab/update-ref
```

Move it back while recording a custom reflog message.

```powershell
git update-ref -m "lab: move reference back" refs/heads/lab/update-ref 356772c
git reflog show -n 10 lab/update-ref
```

**What to remember:**
- `git update-ref` directly updates a reference.
- Updating one branch reference does not move the currently checked-out branch or modify the working tree.
- Custom reflog messages make reference updates easier to investigate.

## Lab Results and Observations

The practical investigation produced the following observations:

| Investigation | Result |
|---|---|
| Initial feature branch | `356772c` |
| Lab branch commit | `c54badd` |
| Detached HEAD commit | `4c2f804` |
| Recovered reference movement commit | `c54badd` |
| Recovered detached HEAD commit | `4c2f804` |
| Direct reference update | `lab/update-ref` moved from `356772c` to `c54badd` and back |
| Custom reflog message | `lab: move reference back` |

### Reflog and Reachability

The investigation also compared:

```powershell
git fsck --unreachable
git fsck --no-reflog --unreachable
```

The detached and reset commits were preserved through reflog references. The `--no-reflog` option excluded reflog entries as reachability roots, revealing commits that were otherwise retained through reflog history.

No garbage collection or pruning was performed.

## Key Takeaways

- Git references are pointers to objects, usually commits.
- Branches are movable references rather than independent copies of repository history.
- `HEAD` identifies the current position, either symbolically through a branch or directly through a commit.
- Detached HEAD allows commits to be created without advancing a branch.
- Reflogs record reference movement and provide a practical recovery mechanism.
- `git update-ref` provides direct control over reference updates.
- Recovery branches can preserve commits that would otherwise become difficult to locate.

## Useful Commands

| Command | Purpose |
|---|---|
| `git show-ref` | List references |
| `git symbolic-ref HEAD` | Inspect symbolic HEAD |
| `git rev-parse HEAD` | Resolve HEAD to a commit ID |
| `git branch --show-current` | Display the current branch |
| `git switch --detach <commit>` | Enter detached HEAD |
| `git reflog` | Inspect HEAD reference history |
| `git reflog show <branch>` | Inspect a branch reflog |
| `git update-ref` | Update a reference directly |
| `git fsck --unreachable` | Inspect unreachable objects |

## Completion Status

- [x] Repository references explored.
- [x] Symbolic HEAD inspected.
- [x] Branch reference movement investigated.
- [x] Detached HEAD state explored.
- [x] Reflog-based recovery performed.
- [x] Direct reference manipulation tested.
- [x] Practical observations documented.
