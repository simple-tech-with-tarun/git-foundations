# Git Work Management – Stashing and Temporary Workflows

## Overview

This chapter explores Git stash as a mechanism for temporarily saving changes in the working directory and index without creating a commit.

The exercises focus on advanced stash operations, selective change management, recovery workflows, and understanding how Git represents stash entries internally.

The objective is to understand not only how to execute stash commands, but also how Git handles different categories of changes and how to recover work safely.

## Learning Objectives

- Understand the Git stash stack and its behaviour.
- Manage staged and unstaged changes independently.
- Include untracked and ignored files in stash entries.
- Selectively stash individual changes and hunks.
- Inspect the internal structure of stash commits.
- Apply stash entries across different working states.
- Resolve conflicts when applying stashed changes.
- Manage stash entries using `drop` and `clear`.
- Understand recovery considerations for removed stash entries.

## Repository Structure

```text
work-management/
├── README.md
└── exercises/
    ├── deployment_config.py
    ├── deployment_local.py
    ├── deployment_override.py
    └── deployment_temporary.py
```

The exercises use Python deployment configuration files to create realistic working-tree changes.

A root-level `.gitignore` file excludes generated deployment artifacts.

## 1. Stash Fundamentals and Inspection

The initial exercises covered creating, listing, inspecting, applying, and removing stash entries.

### Commands explored

| Command | Purpose |
|---|---|
| `git stash push -m "message"` | Save working changes with a description |
| `git stash list` | List available stash entries |
| `git stash show` | Summarize a stash entry |
| `git stash show -p` | Display the stash patch |
| `git stash apply` | Apply a stash without removing it |
| `git stash pop` | Apply a stash and remove it after successful application |

Stash entries are maintained as a stack.

New entries are placed at the top, and references such as `stash@{0}` identify entries by their current position.

## 2. Staged and Unstaged Change Management

This section explored how Git handles changes already staged in the index separately from unstaged working-tree changes.

### `--keep-index`

```powershell
git stash push --keep-index -m "WIP: replica configuration"
```

The experiment demonstrated that:

- Staged changes remain in the index and working tree.
- Unstaged changes are removed from the working tree.
- The stash snapshot includes both staged and unstaged tracked changes.

### `--staged`

```powershell
git stash push --staged -m "WIP: staged deployment settings"
```

This option saves only staged changes while leaving unstaged modifications in the working tree.

The exercise was performed more than once:

- An initial attempt created the stash but failed during working-tree cleanup.
- A subsequent attempt using ordinary staging with `git add` completed successfully.

The first failure remains an observation requiring further investigation.

### `--index`

```powershell
git stash apply --index 'stash@{0}'
```

The `--index` option attempts to restore the original staged and unstaged state when applying a stash.

The experiment confirmed that Git can restore the original index state rather than simply applying every change as an unstaged modification.

## 3. Untracked and Ignored Files

The exercises compared the behaviour of the default stash operation, `-u`, and `--all`.

| Option | Tracked changes | Untracked files | Ignored files |
|---|---|---|---|
| Default | Yes | No | No |
| `-u` / `--include-untracked` | Yes | Yes | No |
| `-a` / `--all` | Yes | Yes | Yes |

### Commands explored

```powershell
git stash push -m "WIP: default stash behaviour"

git stash push -u -m "WIP: include untracked files"

git stash push --all -m "WIP: include untracked and ignored files"
```

A generated deployment file was excluded using a `.gitignore` rule:

```gitignore
# Generated deployment artifacts
*.generated.py
```

The rule was verified using:

```powershell
git check-ignore -v .\work-management\exercises\deployment.generated.py
```

### Important observations

- Default stash operations do not include untracked files.
- `-u` includes untracked files but excludes ignored files.
- `--all` includes both untracked and ignored files.
- If `.gitignore` itself is untracked, using `-u` can stash that file too.
- The `--all` experiment also captured Ruff cache files because they were not excluded by the repository's ignore rules at the time.

The exercise demonstrated why repository ignore rules should be established and maintained carefully.

## 4. Selective Stashing

Selective stashing was explored using:

```powershell
git stash push -p -m "WIP: selectively stash deployment changes"
```

The interactive patch interface provides several options, including:

| Option | Purpose |
|---|---|
| `y` | Stash the current hunk |
| `n` | Leave the current hunk unstashed |
| `s` | Split the current hunk into smaller hunks |
| `e` | Manually edit the patch |
| `q` | Quit |
| `?` | Display help |

### Manual patch editing

The `e` option was used to select an individual function from a combined patch.

Git successfully created a stash containing the selected function, but failed while removing the corresponding working-tree change.

The stash itself remained available and was inspected using `git stash show -p`.

The working-tree cleanup was subsequently performed manually.

The underlying reason for the cleanup failure remains unconfirmed.

### Automatic hunk splitting

The `s` option was then tested with multiple function additions.

Initially, Git presented two function additions in a single hunk.

Using `s` successfully split the original hunk into two independently selectable hunks.

Changes were also introduced in a second Python file to demonstrate file-level separation.

The final experiment successfully stashed selected changes from both files in one stash entry.

This demonstrated that:

- A file can contain multiple selectable hunks.
- Different files are presented as separate changes.
- Multiple selected hunks can be stored in one stash entry.
- `s` can split a combined hunk into smaller hunks.

## 5. Understanding Stash Internals

Stash entries were inspected using:

```powershell
git cat-file -p 'stash@{0}'
```

A stash is represented by Git commit objects rather than being a simple patch file.

The main stash commit generally contains:

- The original `HEAD` commit as its first parent.
- An index commit as its second parent.
- An optional third parent containing untracked files when they are included.

The relationships can be understood as follows:

| Comparison | Represents |
|---|---|
| Original HEAD to index commit | Staged changes |
| Index commit to stash commit | Unstaged changes |
| Third parent | Additional untracked files |

This internal structure explains how Git can preserve staged and unstaged changes independently.

## 6. Applying Stashes and Conflict Resolution

The exercises explored applying multiple stash entries and handling overlapping changes.

### Applying a stash to a modified working tree

An attempt to apply one stash was rejected because the working tree already contained uncommitted changes to the same file.

Git prevented the operation because applying the second stash could overwrite local modifications.

The existing changes were temporarily stashed before proceeding.

### Resolving a content conflict

After applying another stash and committing the restored changes, the temporary stash was applied again.

This time Git attempted the merge but reported a content conflict.

The conflict involved two independently added functions in `deployment_config.py`:

- `is_production_deployment()`
- `get_deployment_region()`

Both functions were required, so the conflict was resolved by preserving both implementations and removing the conflict markers.

The resolution was staged and verified:

```powershell
git add .\work-management\exercises\deployment_config.py
git diff --cached
```

Ruff validation was performed before committing.

The recovery was recorded in commit `e1dfec9`.

This exercise demonstrated that a conflict during stash application does not necessarily mean the changes are incompatible. Git may require manual reconciliation even when both changes can coexist.

## 7. Stash Stack Management

The stash stack was managed using `drop` and `clear`.

### Removing the latest stash

```powershell
git stash drop
```

Removes the top entry, equivalent to:

```powershell
git stash drop 'stash@{0}'
```

### Removing a specific entry

```powershell
git stash drop 'stash@{2}'
```

Removes the entry at the specified position.

### Removing all entries

```powershell
git stash clear
```

Removes all entries from the stash list.

### Positional references

The exercises confirmed that stash references are positional.

When an entry is removed, subsequent entries shift up in the list.

For example, after dropping `stash@{2}`, the previous `stash@{3}` becomes the new `stash@{2}`.

This is important when working with multiple stash entries: always inspect the current stash list before applying or removing a particular entry.

The final `git stash clear` exercise removed all remaining stash entries.

## 8. Observations and Further Investigation

Several experiments produced results worth revisiting:

1. **`--staged` cleanup failure:** The first attempt created a stash but failed during working-tree cleanup. A later attempt succeeded. The reason for the difference has not been established.

2. **Manual patch editing:** The `e` option created a stash containing the selected function, but cleanup failed. The selected change was subsequently removed manually from the working tree.

3. **Automatic patch splitting:** The `s` option successfully split a combined hunk into smaller selectable hunks and completed the stash operation successfully.

4. **Ignored file capture:** Using `--all` captured Ruff cache files because the cache directory was not excluded by the repository's ignore rules.

These observations should be revisited where useful during future exercises.

## 9. Remaining Exercises

The following topics remain planned:

- Applying stash entries on a different branch.
- Understanding branch-related stash conflicts.
- Using `git stash branch` to recreate the original working context.
- Recovering dropped stash entries using Git's object database.
- Further stash inspection and recovery scenarios.
- Integrated scenarios combining staged, unstaged, untracked, and ignored changes.

## Validation

Python exercises are validated using Ruff:

```powershell
python -m ruff check .\work-management\exercises\
python -m ruff format --check .\work-management\exercises\
```

All checks should pass before committing changes.
