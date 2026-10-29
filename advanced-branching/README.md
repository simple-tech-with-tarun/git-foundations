# Advanced Branching

## Overview

This chapter explores advanced Git branching workflows through practical exercises. It covers cherry-picking selected commits, handling commit dependencies, rebasing feature branches onto an updated main branch, and comparing merge and rebase workflows.

The exercises use a release preparation tool as a working example.

## Learning Objectives

By completing this chapter, you will learn how to:

- Cherry-pick an independent commit onto another branch.
- Understand why dependent commits must be applied in the correct order.
- Rebase a feature branch onto an updated main branch.
- Understand how rebasing changes commit IDs.
- Compare merge and rebase history structures.
- Inspect commit ancestry and verify branch state.
- Document exercise results and validation evidence.

## Prerequisites

You should be familiar with:

- Creating and switching branches.
- Creating commits and inspecting commit history.
- Basic merge conflict handling.
- Commands such as `git status`, `git log`, and `git show`.

## Exercise 1: Cherry-pick an Independent Commit

### Objective

Apply a specific commit from one branch to another without merging the entire source branch.

### Workflow

1. Create a source branch containing an independent change.
2. Identify the commit to transfer.
3. Switch to the target branch.
4. Cherry-pick the selected commit.
5. Inspect the resulting history and file changes.

### Commands

```powershell
git log --oneline
git switch feature/advanced-branching
git cherry-pick <commit-id>
git show --stat HEAD
```

Replace `<commit-id>` with the actual commit hash you want to apply.

### Result

The release channel label formatter was added to the target branch.

- Original commit: `16727e2`
- Cherry-picked commit: `33eb31f`

The new commit has a different ID because Git created it with the target branch's current commit as its parent.

### Key Lesson

Cherry-pick applies the change from a selected commit without merging all commits from the source branch. It is useful when you need one specific change on another branch.

## Exercise 2: Cherry-pick Dependent Commits

### Objective

Understand why the order of cherry-picking matters when commits depend on files or changes introduced by earlier commits.

### Workflow

The release preparation tool was split across dependent commits. Attempting to cherry-pick the validation change before the tool itself caused a modify/delete conflict because the required file did not exist on the target branch.

The unsuccessful operation was aborted, and the commits were then applied in dependency order.

### Commands

```powershell
git cherry-pick --abort
git cherry-pick 052e313
git cherry-pick 3526778
```

### Result

The correct order was:

1. `052e313` - Add the release preparation tool.
2. `3526778` - Validate the release version format.

The release tool ran successfully after the commits were applied in the correct order.

### Key Lesson

Identify a commit's prerequisites before cherry-picking it. Apply prerequisite commits first. If a cherry-pick fails and you want to return to the state before that operation, use `git cherry-pick --abort`.

## Exercise 3: Rebase onto Updated Main

### Objective

Rebase a feature branch onto a newer base so that the feature can use changes added to main after the branch was created.

### Initial Problem

The release preparation tool was updated to load a validation policy file. That file existed on main but was absent from the feature branch's original history. Running the tool before rebasing resulted in a `FileNotFoundError`.

### Workflow

1. Inspect the current commit history.
2. Confirm that main contains the required policy file.
3. Rebase the feature branch onto main.
4. Inspect the resulting history.
5. Run the tool and validate the result.

### Commands

```powershell
git log --oneline --graph --all
git switch feature/advanced-branching
git rebase main
git merge-base main feature/advanced-branching
git log --oneline -5
```

### Result

The rebase completed successfully without conflicts. The feature commits were replayed on top of the updated main history.

The updated main commit was `aabdc0f`. The rebased feature commits included:

- `97731c7` - Add release preparation tool.
- `a024da2` - Validate release version format.
- `e9d9b65` - Add release channel label formatter.
- `c0b90a5` - Load release validation policy.
- `d35afe3` - Enforce release validation policy.

The release tool ran successfully after the rebase, and Ruff validation passed.

### Key Lesson

Rebase replays feature commits onto a new base. Replayed commits receive new IDs because their parent history changes. This can create a linear history.

The merge base identifies a common ancestor. It does not prove that the application or its tests are working correctly.

## Exercise 4: Compare Merge and Rebase

### Objective

Compare how merging and rebasing integrate changes from an updated main branch.

### Merge Workflow

The `lab/merge-comparison` branch contained a feature change while main received a separate release notes policy change.

The updated main branch was merged into the comparison branch.

Relevant commits:

- Feature commit: `33737ec`
- Updated main commit: `f39dc84`
- Merge commit: `3b48b27`

The merge preserved both lines of history and created a merge commit with two parents. The original feature commit ID remained unchanged.

### Rebase Workflow

The `lab/rebase-comparison` branch contained a manual release approval change while main received a notification policy change.

The feature branch was rebased onto the updated main branch.

Relevant commits:

- Original feature commit: `48a9eb8`
- Updated main commit: `b40d7b4`
- Rebased feature commit: `2f2d20b`

The rebase replayed the feature change on top of main. The feature commit received a new ID, and the resulting history was linear without a merge commit.

### Comparison

| Aspect | Merge | Rebase |
| --- | --- | --- |
| History | Preserves both branch histories | Replays commits on a new base |
| Merge commit | Creates a merge commit when required | Does not create a merge commit by itself |
| Existing feature commit IDs | Preserved | Replayed commits receive new IDs |
| History shape | May show parallel development | Usually linear |
| Main consideration | Records the integration point | Rewrites the feature branch history |

### Key Lesson

Both merge and rebase can integrate changes successfully. The choice depends on the team's preferred history, collaboration workflow, and whether rewriting the feature branch history is appropriate.

## Verification Practices

Use the commands relevant to the exercise being performed.

### Inspect Git State and History

```powershell
git status -sb
git log --oneline --graph --all
git show --stat HEAD
git merge-base main feature/advanced-branching
```

### Validate the Release Policy JSON

```powershell
python -m json.tool .\advanced-branching\release-prep\config\release-policy.json
```

### Run Ruff

```powershell
python -m ruff check .\advanced-branching\release-prep\release_tool.py
```

A successful Git operation does not replace application-level validation. Check both the repository state and the behavior of the code affected by the exercise.

## Exercise Evidence

The detailed exercise history, original and resulting commit IDs, verification results, and observations are recorded in:

- `exercises/commit-log.md`

This file provides a record of what was performed and observed during the practical exercises.

## Summary

Advanced branching workflows provide control over how changes move between branches.

- Cherry-pick transfers selected commits.
- Dependent commits must be applied in the correct order.
- Rebase replays feature commits onto an updated base.
- Merge preserves branch history and records the integration point.
- Verification helps distinguish a successful Git operation from a working application.

These techniques are useful when maintaining feature branches, integrating independent changes, and choosing an appropriate project history strategy.
