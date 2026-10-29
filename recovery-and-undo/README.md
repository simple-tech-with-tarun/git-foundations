# Git Fundamentals - Recovery and Undo

## Overview

This chapter explores Git recovery and undo operations through hands-on exercises. The objective is to understand how Git manages the working tree, staging area, commit history, and references when changes need to be restored or undone.

The exercises cover both safe recovery operations and history-changing operations, including practical scenarios involving accidental resets and commit recovery.

## Learning Objectives

- Restore working tree changes using `git restore`.
- Unstage changes without discarding working tree modifications.
- Understand selective restoration using interactive patch mode.
- Reverse existing commits using `git revert`.
- Understand revert conflicts and how to resolve or abort them.
- Compare `git reset --soft`, `git reset --mixed`, and `git reset --hard`.
- Inspect reference history using `git reflog`.
- Recover commits after resetting a branch.
- Preserve recovered commits using separate branches.

---

## 1. Restoring Changes with git restore

The `git restore` command is used to restore files in the working tree or staging area.

### 1.1 Restore Unstaged Changes

```bash
git restore <file>
```

Restores the working tree version of a file from the staging area.

Any unstaged modifications to that file are discarded.

### 1.2 Unstage Changes

```bash
git restore --staged <file>
```

Removes a file's changes from the staging area while preserving its working tree modifications.

### 1.3 Restore from a Specific Commit

```bash
git restore --source=<commit> <file>
```

Restores the working tree version of a file from a specified commit.

To restore the staging area as well:

```bash
git restore --source=<commit> --staged <file>
```

To restore both the staging area and working tree:

```bash
git restore --source=<commit> --staged --worktree <file>
```

### 1.4 Interactive Restoration

```bash
git restore -p <file>
```

Allows individual changes or hunks to be selected for restoration instead of discarding all modifications.

This is useful when only specific portions of a file need to be discarded.

### Practical Exercises

The following operations were practised:

- Restoring unstaged modifications.
- Unstaging changes while preserving working tree content.
- Restoring files from earlier commits.
- Restoring both the index and working tree from a selected commit.
- Selectively discarding individual changes using interactive patch mode.

The selective restoration exercise preserved the intended line while discarding an unwanted addition.

---

## 2. Reversing Commits with git revert

`git revert` reverses the changes introduced by an existing commit by creating a new commit.

Unlike `git reset`, it does not move the branch pointer backwards or remove the original commit from history.

### Syntax

```bash
git revert <commit-hash>
```

To accept the default revert commit message:

```bash
git revert --no-edit <commit-hash>
```

To apply the inverse changes without immediately creating a commit:

```bash
git revert --no-commit <commit-hash>
```

### 2.1 Reverting File Creation

A commit that introduces a file can be reversed using `git revert`.

Git creates a new commit that removes the file.

### 2.2 Reverting a Revert

A revert is itself a commit. Reverting that commit applies the original changes again.

This allows previously reversed changes to be reapplied without rewriting history.

### 2.3 Reverting File Modifications

Reverting a commit that modifies an existing file restores the content to the state before that commit.

The original creation and modification commits remain in history.

### 2.4 Handling Revert Conflicts

A modify/delete conflict can occur when Git attempts to reverse an earlier file creation while a later commit has modified that file.

Git cannot automatically determine whether the file should be deleted or retained.

Useful commands:

```bash
git status
git revert --continue
git revert --skip
git revert --abort
```

- `--continue`: Continues the revert after resolving the conflict.
- `--skip`: Skips the current commit being reverted.
- `--abort`: Cancels the revert and returns to the state before the revert operation.

For merge commits, the `-m` option specifies the mainline parent to retain.

### Practical Exercises

The following operations were performed:

- Reverted a file creation commit.
- Reverted the revert commit to restore the file.
- Reverted the reapplication to remove the file again.
- Created separate commits for file creation and modification.
- Reverted only the modification commit.
- Encountered a modify/delete conflict while attempting to revert an earlier creation commit.
- Aborted the conflicting revert and successfully reverted the intended modification.

Important commit references:

| Commit | Description |
|---|---|
| `26ee70e` | Initial revert exercise fixture |
| `b038ff5` | Reverted the fixture creation |
| `0ab47f5` | Reapplied the fixture |
| `9dcae67` | Reverted the reapplication |
| `409fbf9` | Created the modification exercise fixture |
| `a661e6a` | Modified the fixture |
| `61aff9e` | Reverted the modification |
| `48f5a01` | Reapplied the modification |
| `9ba9ba4` | Reverted the modification again |

---

## 3. Resetting Commits with git reset

Unlike `git revert`, `git reset` moves the current branch pointer to another commit.

Depending on the reset mode, it can also modify the staging area and working tree.

### Syntax

```bash
git reset <mode> <commit>
```

The three primary modes are:

- `--soft`
- `--mixed`
- `--hard`

### 3.1 Soft Reset

```bash
git reset --soft HEAD~1
```

Moves the current branch pointer to the previous commit while preserving the staging area and working tree.

Result:

- The latest commit is removed from the current branch history.
- Changes remain staged.
- Working tree content remains unchanged.

This is useful when a commit needs to be undone but its changes should remain ready for recommitting.

### 3.2 Mixed Reset

```bash
git reset --mixed HEAD~1
```

Moves the branch pointer and resets the staging area to match the target commit.

The working tree remains unchanged.

Result:

- The latest commit is removed from the current branch history.
- Staged changes become unstaged.
- Working tree content remains unchanged.

`--mixed` is the default reset mode, so the following is equivalent:

```bash
git reset HEAD~1
```

An important distinction is that a file introduced by the commit being reset becomes untracked, while a modification to an already tracked file remains a tracked but unstaged modification.

### 3.3 Hard Reset

```bash
git reset --hard HEAD~1
```

Moves the branch pointer and resets both the staging area and working tree to match the target commit.

Result:

- The latest commit is removed from the current branch history.
- Staging area changes are discarded.
- Working tree changes are discarded.
- Files return to their state in the target commit.

**Warning:** Hard reset is destructive to uncommitted changes in affected paths. Always verify the target commit and working tree before executing it.

### Comparison of Reset Modes

| Behaviour | Soft | Mixed | Hard |
|---|---|---|---|
| Moves branch pointer | Yes | Yes | Yes |
| Resets staging area | No | Yes | Yes |
| Resets working tree | No | No | Yes |
| Preserves staged changes | Yes | No | No |
| Preserves working tree changes | Yes | Yes | No |

### Practical Exercises

A dedicated reset practice file was used to demonstrate each reset mode.

The exercises included:

- Creating a disposable commit and performing a soft reset.
- Observing that the changes remained staged.
- Performing a mixed reset and observing an untracked file.
- Reintroducing the file and creating a separate modification commit.
- Performing a mixed reset on a tracked modification.
- Verifying that the modification remained in the working tree but became unstaged.
- Creating another disposable commit and performing a hard reset.
- Verifying that the commit and its added content disappeared from the current branch state.

Important commit references:

| Commit | Description |
|---|---|
| `db145e5` | Initial reset practice fixture |
| `545f2de` | Mixed reset exercise result |
| `54e11a6` | Reset practice fixture |
| `fd6cbfc` | Tracked file modification for mixed reset |
| `ff59c6a` | Hard reset exercise change |

---

## 4. Recovering Commits with git reflog

A commit that disappears from the current branch history after a reset may still be recoverable.

Git maintains a reference log that records changes to `HEAD` and other references.

### Syntax

```bash
git reflog
```

To inspect a limited number of entries:

```bash
git reflog -8
```

Example output:

```text
54e11a6 HEAD@{0}: reset: moving to HEAD~1
ff59c6a HEAD@{1}: commit: test: add hard reset exercise change
```

The first entry shows the most recent reset.

The second entry identifies the commit that was previously at the branch tip.

### 4.1 Recovering a Commit

A commit can be recovered by resetting the branch to its previous commit reference:

```bash
git reset --hard <commit-hash>
```

In the practical exercise, commit `ff59c6a` was recovered after it had been removed from the current branch history by a hard reset.

The recovery restored:

- The original commit at the branch tip.
- The previously discarded file content.
- A clean working tree.

Reflog entries are local and subject to expiration and Git garbage collection. They should not be treated as permanent backups.

---

## 5. Preserving Recovered Commits with Branches

Another useful recovery technique is creating a separate branch pointing to a recovered commit.

### Syntax

```bash
git branch <branch-name> <commit-hash>
```

Example:

```bash
git branch recovery/backup ff59c6a
```

This creates a new branch pointing to the specified commit without moving the current branch.

To inspect branches:

```bash
git branch
```

To inspect commits across branches:

```bash
git log --oneline --all
```

To switch branches:

```bash
git switch <branch-name>
```

### Practical Exercise

A recovery branch named `recovery/backup` was created at commit `ff59c6a`.

The branch was inspected, and switching between `recovery/backup` and `feature/recovery-and-undo` was practised.

Both branches pointed to the same commit at the time of verification.

This demonstrates how a recovered commit can be preserved independently before performing further history operations.

---

## 6. Important Concepts and Lessons Learned

### Revert vs Reset

| Aspect | git revert | git reset |
|---|---|---|
| Creates a new commit | Yes | No |
| Moves branch pointer | No | Yes |
| Rewrites current branch history | No | Yes |
| Suitable for shared history | Generally yes | Requires caution |
| Can preserve changes for recommitting | With `--no-commit` | With `--soft` or `--mixed` |

### Log vs Reflog

| Command | Purpose |
|---|---|
| `git log` | Displays commit history reachable from the selected references |
| `git reflog` | Displays recent movements of references such as `HEAD` |

### Key Takeaways

- `git restore` handles file-level recovery.
- `git revert` reverses changes by creating new commits.
- `git reset` moves the current branch pointer.
- `--soft` preserves staged changes.
- `--mixed` resets the staging area but preserves working tree content.
- `--hard` resets both the staging area and working tree.
- A commit disappearing from `git log` does not necessarily mean it is permanently lost.
- `git reflog` helps locate previous reference positions.
- A separate recovery branch can preserve a commit before further operations.

---

## 7. Exercise Directory

```text
recovery-and-undo/
|
+-- README.md
|
+-- exercises/
    +-- restore-unstaged.txt
    +-- revert-practice.txt
    +-- reset-practice.txt
```

The reset practice file was also used during the reset exercises.

---

## Conclusion

This chapter covered Git recovery and undo operations through practical exercises rather than command-only demonstrations.

The exercises established how Git handles changes across the working tree, staging area, and commit history, and how previously displaced commits can be recovered using the reflog.

These concepts provide a foundation for safely managing mistakes, recovering work, and understanding the consequences of history-changing operations in Git.
