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
- Apply stash entries across different working states and branches.
- Resolve conflicts when applying stashed changes.
- Understand branch-based stash recovery.
- Manage stash entries using `drop` and `clear`.
- Investigate and recover dropped stash entries using Git's object database.
- Understand how Git preserves and restores mixed staged and unstaged working-tree states.
- Combine multiple stash entries while maintaining index-state separation.
- Manage interrupted development workflows by stashing complete working states, committing urgent fixes, and restoring previous work.

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

This was an overwrite-protection failure rather than a content conflict.

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

## 8. Cross-Branch Stash Workflows

The second phase introduced branch-based stash operations using separate experiment branches.

The experiment used the following branches:

```text
feature/work-management
        |
        ├── experiment/stash-source
        |
        ├── experiment/stash-destination
        |
        └── recovery/stash-owner
```

The experiment branches were created from the existing feature branch so that the stash operations could be tested independently of the main development workflow.

### Creating a stash on the source branch

On `experiment/stash-source`, a deployment owner helper was introduced in `deployment_config.py`:

```python
def get_deployment_owner():
    return "platform-team"
```

The change was saved using:

```powershell
git stash push -m "WIP: deployment owner on source branch"
```

This created a stash containing the new function without requiring a commit on the source branch.

### Applying the stash on another branch

The destination branch was checked out:

```powershell
git switch experiment/stash-destination
```

The stash was applied:

```powershell
git stash apply 'stash@{0}'
```

Git successfully restored the source branch's changes on the destination branch.

The original stash remained available because `apply` does not remove the stash entry.

This demonstrated that a stash can be applied on a different branch when the destination working tree and the changes are compatible.

### Handling a cross-branch content conflict

The destination branch was then given its own implementation of `get_deployment_owner()`:

```python
def get_deployment_owner():
    return "infrastructure-team"
```

The destination implementation was committed in:

`58948f9 test: add destination deployment owner`

The original stash was applied again:

```powershell
git stash apply 'stash@{0}'
```

This time Git reported a content conflict because both branches contained different implementations of the same function.

The conflict was represented using Git's conflict markers:

```python
def get_deployment_owner():
 <<<<<<< Updated upstream
     return "infrastructure-team"
 =======
     return "platform-team"
 >>>>>>> Stashed changes
```

The resolution retained the source implementation:

```python
def get_deployment_owner():
    return "platform-team"
```

The resolved file was staged and committed:

`dfd74fc test: resolve cross-branch stash conflict`

This exercise demonstrated that stash application across branches follows the same conflict-resolution principles as other Git merge operations.

### Important observations

- A stash is not restricted to the branch on which it was created.
- Applying a stash on another branch does not change the original stash entry.
- A clean destination working tree does not guarantee conflict-free application.
- Changes to the same function or lines can produce a content conflict.
- A successfully resolved stash application can be committed like any other working-tree change.

## 9. Branch-Based Stash Recovery with `git stash branch`

The next experiment explored `git stash branch`, which creates a new branch using the original base commit of a stash and applies the stash there.

The operation was performed using:

```powershell
git stash branch recovery/stash-owner 'stash@{0}'
```

Git created and switched to the new branch:

`recovery/stash-owner`

The stashed implementation was restored:

```python
def get_deployment_owner():
    return "platform-team"
```

The stash entry was automatically dropped after successful application.

### Understanding the behaviour

`git stash branch` differs from applying a stash directly to another branch.

| Operation | Behaviour |
|---|---|
| `git stash apply` | Applies changes to the current branch and retains the stash |
| `git stash pop` | Applies changes and removes the stash after successful application |
| `git stash branch` | Creates a branch at the stash's original base, applies the stash, and drops the stash after successful application |

The important distinction is that `git stash branch` recreates the original working context rather than applying the changes on top of the current branch's latest commit.

### Validation

The recovered implementation was checked using Ruff:

```powershell
python -m ruff format .\work-management\exercises\
python -m ruff check .\work-management\exercises\
```

Both checks passed.

## 10. Recovering Dropped Stashes

The final recovery exercise investigated whether a stash removed using `git stash drop` could be recovered from Git's object database.

### Dropping a stash

Before removing the stash, its commit hash was captured:

```powershell
git rev-parse 'stash@{0}'
```

The resulting hash was:

```text
782d5f921962cf29a905042db25d8b046ae3cb5e
```

The stash was then removed:

```powershell
git stash drop 'stash@{0}'
```

The stash list no longer contained the entry.

### Investigating unreachable Git objects

The following command was used:

```powershell
git fsck --no-reflogs --unreachable
```

This command checks Git's object database and reports objects that are unreachable from the references and reflogs considered by the operation.

The output contained numerous unreachable objects, including the previously captured stash commit:

```text
unreachable commit 782d5f921962cf29a905042db25d8b046ae3cb5e
```

This confirmed that removing the stash reference did not immediately remove the underlying commit object.

### Inspecting the recovered candidate

The commit was inspected using:

```powershell
git show --stat 782d5f921962cf29a905042db25d8b046ae3cb5e
```

Commit metadata was inspected using:

```powershell
git show --format=fuller --no-patch 782d5f921962cf29a905042db25d8b046ae3cb5e
```

The output confirmed:

- The object was a merge commit.
- Its message identified the original stash operation.
- It contained the expected change to `deployment_config.py`.
- The file change added `get_deployment_owner()`.

### Re-registering the dropped stash

The existing stash commit was restored to the stash list using:

```powershell
git stash store -m "Recovered dropped deployment owner" 782d5f921962cf29a905042db25d8b046ae3cb5e
```

The stash was verified:

```powershell
git stash list
git stash show -p 'stash@{0}'
```

The original implementation was present:

```python
def get_deployment_owner():
    return "platform-team"
```

### Applying the recovered stash

The recovered stash was applied:

```powershell
git stash apply 'stash@{0}'
```

The change was restored to the working tree as an unstaged modification.

The working-tree state was verified using:

```powershell
git status -sb
git diff
```

The recovered implementation was then staged and committed:

`e63edae test: restore deployment owner from dropped stash`

### Important observations

- `git stash drop` removes the stash reference, not necessarily the underlying Git objects immediately.
- `git fsck --no-reflogs --unreachable` can help locate unreachable stash commit objects.
- The output can contain many unrelated unreachable objects, so identifying the correct commit requires inspection.
- `git stash store` can register an existing stash commit in the stash list again.
- `git stash apply` restores the recovered changes without removing the newly registered stash entry.
- A dropped stash is not guaranteed to remain recoverable indefinitely.

Git garbage collection can eventually prune unreachable objects. Therefore, stash recovery should be treated as a recovery possibility, not a substitute for regular commits or backups.

## 11. Experiment Branches and Preserved Work

The practical exercises were maintained in separate branches to isolate the different stash scenarios.

| Branch | Purpose | Key commit |
|---|---|---|
| `experiment/stash-source` | Original source-side stash changes | `d79c178` |
| `experiment/stash-destination` | Cross-branch application and conflict resolution | `dfd74fc` |
| `recovery/stash-owner` | Original-base recovery and dropped-stash recovery | `e63edae` |

The branches were pushed to the remote repository to preserve the practical work.

They were retained as experiment references rather than merged into `main`.

## 12. Integrated Workflows and Index-State Management

The third phase explored integrated Git stash workflows involving staged and unstaged changes, multiple stash entries, and interrupted development work.

The exercises used `deployment_config.py` to introduce independent modifications across multiple functions while preserving different staging states.

### Mixed staged and unstaged changes

The initial experiment introduced a staged modification to `get_deployment_summary()` followed by an unstaged modification to the same function.

The working-tree status showed:

```text
MM work-management/exercises/deployment_config.py
```

This represents a file with both staged and unstaged modifications.

The following commands were used to inspect the differences:

```powershell
git diff
git diff --staged
git diff HEAD
```

The experiment confirmed:

| Command | Displays |
|---|---|
| `git diff` | Unstaged changes compared with the index |
| `git diff --staged` | Staged changes compared with HEAD |
| `git diff HEAD` | Combined staged and unstaged changes compared with HEAD |

### Investigating `git stash push --staged`

The `--staged` option was tested with different combinations of staged and unstaged modifications.

The experiments covered:

- Staged and unstaged modifications to the same line.
- Changes to separate lines with dependencies between the modifications.
- Independent modifications in separate functions within the same file.

The results demonstrated that:

- Git could create a staged-only stash while retaining the staged snapshot.
- When dependent unstaged modifications prevented the staged changes from being cleanly removed, Git reported a patch application failure during working-tree cleanup.
- The stash entry could still be present even when cleanup failed.
- An independent staged modification in another function could be successfully stashed while leaving the unstaged modification in the working tree.

Example:

```powershell
git stash push --staged -m "WIP: independent staged-only experiment"
```

The experiment also showed that a stash being successfully created does not necessarily mean the working tree was successfully cleaned.

### Restoring staged changes with `--index`

The following command was used to restore a staged-only stash:

```powershell
git stash apply --index 'stash@{2}'
```

The restored change appeared in the index rather than as an unstaged modification.

The results confirmed that `--index` attempts to restore the original staging state when applying a stash.

Without `--index`, the same staged-only stash was applied with its modification restored as an unstaged change.

An additional experiment attempted to apply a stash while the same file already contained an unstaged local modification.

Git rejected the operation because the local modification could be overwritten.

This demonstrated that stash application is subject to the same working-tree overwrite protections as other Git operations.

### Combining changes from multiple stash entries

Two independent changes were preserved in separate stash entries:

- A staged modification to `get_deployment_summary()`.
- An unstaged modification to `get_deployment_region()`.

After restoring the staged modification using `--index`, the second stash was applied without `--index`.

Git successfully combined both modifications in the same file.

The resulting status was:

```text
MM work-management/exercises/deployment_config.py
```

The staged summary modification remained staged, while the deployment-region modification remained unstaged.

This demonstrated that applying an independent stash does not automatically unstage existing staged changes.

### Preserving an interrupted mixed working-tree state

A final integrated experiment introduced three independent modifications:

```python
def get_application_name():
    return f"Application: {deployment_config['application']}"


def get_deployment_summary():
    return "Deployment summary for payment-service"


def get_deployment_region():
    return f"Deployment region: {deployment_config['region']}"
```

Their initial staging states were:

| Function | Initial state |
|---|---|
| `get_deployment_summary()` | Staged |
| `get_application_name()` | Unstaged |
| `get_deployment_region()` | Unstaged |

All three modifications were preserved using a normal stash operation:

```powershell
git stash push -m "WIP: preserve mixed deployment configuration"
```

The working tree became clean.

The stash was then restored using:

```powershell
git stash apply --index 'stash@{0}'
```

The original staging separation was successfully reconstructed.

The restored state was verified using:

```powershell
git status -sb
git diff --staged
git diff
git diff HEAD
```

### Key observations

- A normal stash captures both staged and unstaged tracked changes.
- The stash retains information about the original index state.
- `--index` attempts to reconstruct the original staged and unstaged separation.
- Without `--index`, restored changes are not explicitly separated according to their original staging state.
- Existing staged changes can remain staged when independent changes from another stash are applied.
- Stash application can be rejected when local modifications would be overwritten.
- Independent changes within the same file can be combined successfully when their patches do not interfere.
- A successful stash creation and successful working-tree cleanup are separate outcomes.


## 13. Stashing Untracked and Ignored Files Together

This exercise explored how Git handles tracked, untracked, and ignored files when stashing interrupted work.

### 13.1 Stashing Tracked and Untracked Files

The `-u` option includes untracked files in a stash while excluding ignored files.

```powershell
git stash push -u -m "WIP: tracked and untracked deployment files"
```

The experiment confirmed that:

- Tracked modifications were captured.
- Untracked files such as `deployment_notes.txt` were captured.
- Ignored files such as `deployment.generated.py` remained in the working directory.

### 13.2 Stashing Tracked, Untracked, and Ignored Files

The `--all` option includes ignored files in addition to tracked and untracked changes.

```powershell
git stash push --all -m "WIP: tracked untracked and ignored deployment files"
```

The experiment confirmed that the ignored deployment file and generated Ruff cache files were also captured and removed from the working directory.

### 13.3 Inspecting Stashed Untracked and Ignored Files

The default stash summary does not display every file captured by a stash.

The following command displays untracked files in the stash diff:

```powershell
git stash show -u -p 'stash@{0}'
```

To inspect the files stored in the third parent of a stash:

```powershell
git ls-tree -r --name-only 'stash@{0}^3'
```

The third parent contains the snapshot of untracked files. When `--all` is used, this snapshot also includes ignored files.

The experiment confirmed that both `deployment_notes.txt` and `deployment.generated.py` were present in this tree.

In this experiment, even `git stash show --all -p` did not display the ignored deployment file, although the third-parent tree confirmed that it was stored.

### 13.4 Restoring Ignored Files

Applying a stash created with `--all` can restore ignored files alongside tracked and untracked changes.

```powershell
git stash apply 'stash@{0}'
```

The ignored deployment file was deleted manually after the initial restoration and then recovered through another stash application.

During the second application, Git reported errors because some tracked and untracked files already had local changes or existing copies. Despite those errors, the missing ignored deployment file was restored.

This demonstrated that stash application can partially restore files even when the overall operation reports an error.

### 13.5 Key Observations

- `git stash push -u` includes tracked and untracked changes but excludes ignored files.
- `git stash push --all` includes tracked, untracked, and ignored files.
- The third parent of a stash stores the untracked-file snapshot and, with `--all`, ignored files as well.
- `git stash show` output should not be treated as a complete inventory of every file stored in a stash.
- `git stash apply` can partially restore files even when another part of the operation fails.
- Ignored files remain excluded from ordinary `git status` output, even after restoration.

## 14. Integrated Interrupted-Work Workflow

The final exercise combined the stash operations explored throughout the third phase into a realistic interrupted-development scenario.

The objective was to preserve an incomplete deployment configuration task, temporarily switch to an independent production fix, commit that fix, and subsequently resume the original work without losing its staging state or additional files.

### 14.1 Preparing Interrupted Work

The exercise introduced multiple changes in `deployment_config.py`:

| Change | Initial state |
|---|---|
| Update `get_deployment_summary()` | Staged |
| Update `get_deployment_region()` | Unstaged |
| Add `deployment_incident_notes.txt` | Untracked |
| `deployment.generated.py` | Ignored |

The ignored deployment artifact was verified using:

```powershell
git check-ignore -v .\work-management\exercises\deployment.generated.py
```

This established a working state containing four different categories of changes.

### 14.2 Stashing the Complete Working State

All interrupted work was preserved using:

```powershell
git stash push --all -m "WIP: preserve integrated deployment interruption"
```

The working tree became clean after the operation.

The stash was inspected using:

```powershell
git stash show -p 'stash@{0}'
git stash show -u -p 'stash@{0}'
```

The third-parent tree was inspected to verify the additional files:

```powershell
git ls-tree -r --name-only 'stash@{0}^3'
```

The output included:

- `.ruff_cache` files
- `work-management/exercises/deployment.generated.py`
- `work-management/exercises/deployment_incident_notes.txt`

This confirmed that the stash contained the untracked incident notes and ignored deployment artifact.

### 14.3 Committing an Independent Production Fix

While the original work remained stashed, an independent accessor was added to `deployment_config.py`:

```python
def get_deployment_environment():
    return deployment_config["environment"]
```

The file was validated using Ruff before committing.

The production fix was committed separately:

`eed3b6a fix: add deployment environment accessor`

This simulated an urgent change that needed to be committed without including the incomplete development work.

### 14.4 Restoring the Interrupted Work

The original stash was restored using:

```powershell
git stash apply --index 'stash@{0}'
```

The `--index` option was used to reconstruct the original staged and unstaged separation.

Git successfully restored:

- The staged deployment summary modification.
- The unstaged deployment region modification.
- The untracked incident notes file.

The resulting status was:

```text
MM work-management/exercises/deployment_config.py
?? work-management/exercises/deployment_incident_notes.txt
```

The ignored deployment artifact was also verified to be present with its original contents.

### 14.5 Handling Partial Stash Restoration

Although the tracked changes were restored successfully, Git reported an error during restoration of the additional files:

```text
.ruff_cache/.gitignore already exists, no checkout
.ruff_cache/0.17.3/6570452681107847919 already exists, no checkout
.ruff_cache/CACHEDIR.TAG already exists, no checkout
error: could not restore untracked files from stash
```

The error did not prevent all restoration.

Subsequent inspection confirmed that:

- The staged and unstaged modifications were restored.
- The incident notes file was present.
- The ignored deployment artifact was present with its original contents.

This demonstrated that stash application can partially fail while still restoring some of the requested changes.

It also highlighted the importance of inspecting the resulting working-tree state rather than assuming that an error means the entire operation was unsuccessful.

### 14.6 Validation and Commit Strategy

After restoration, the exercise directory was validated:

```powershell
python -m ruff check .\work-management\exercises\
python -m ruff format --check .\work-management\exercises\
```

Both checks passed.

The resumed work was committed separately from the urgent production fix:

`1813495 test: resume interrupted deployment workflow`

The incident notes were included in the commit, while the ignored generated deployment artifact remained excluded.

The final working tree was clean, and the original stash was retained for verification.

### 14.7 Key Observations

- A complete interrupted working state can be preserved using `git stash push --all`.
- An independent production fix can be committed while previous work remains stashed.
- `git stash apply --index` can restore the original staging separation on top of a subsequent commit.
- Stash application can report an error while successfully restoring tracked changes and some additional files.
- Existing untracked or ignored files can interfere with restoration of the stash's additional-file snapshot.
- Inspecting the third parent provides a useful inventory of files included in the stash.
- Separate commits keep urgent fixes independent from resumed development work.
- Retaining the stash until restoration and validation are complete provides an additional recovery reference.

## 15. Observations and Further Investigation

Several experiments produced results worth revisiting:

1. **`--staged` cleanup failure:** The first attempt created a stash but failed during working-tree cleanup. A later attempt succeeded. The reason for the difference has not been established.

2. **Manual patch editing:** The `e` option created a stash containing the selected function, but cleanup failed. The selected change was subsequently removed manually from the working tree.

3. **Automatic patch splitting:** The `s` option successfully split a combined hunk into smaller selectable hunks and completed the stash operation successfully.

4. **Ignored file capture:** Using `--all` captured Ruff cache files because the cache directory was not excluded by the repository's ignore rules.

5. **Cross-branch application:** Stash entries can be applied on other branches, but overlapping changes may require manual conflict resolution.

6. **Branch-based recovery:** `git stash branch` provides a way to recreate the original base context of a stash.

7. **Dropped-stash recovery:** Unreachable stash commit objects can sometimes be located and re-registered, provided they have not been pruned.

## Validation

Python exercises are validated using Ruff:

```powershell
python -m ruff check .\work-management\exercises\
python -m ruff format --check .\work-management\exercises\
```

All checks should pass before committing changes.
