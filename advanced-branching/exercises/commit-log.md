# Advanced Branching - Exercise Log

## Exercise 1: Cherry-pick an Independent Commit

- Original branch: `feature/release-channel-label`
- Original commit: `16727e2` - `feat: add release channel label formatter`
- Target branch: `feature/advanced-branching`
- Cherry-picked commit: `33eb31f` - `feat: add release channel label formatter`
- Result: The independent formatter was added without bringing unrelated commits from the source branch.

## Exercise 2: Cherry-pick Dependent Commits

- Lab branch: `lab/cherry-pick-dependencies`
- Initial base: `709760e`
- Attempted to cherry-pick `8eebdce` before its prerequisite.
- Result: Git reported a modify/delete conflict because the release tool did not yet exist on the target branch.
- Recovery: Ran `git cherry-pick --abort`.
- Correct order:
  - `052e313` - `feat: add release preparation tool`
  - `3526778` - `feat: validate release version format`
- Validation: Ruff passed, the release summary ran successfully, and the working tree was clean.

## Exercise 3: Rebase onto Updated Main

### Before rebase

- Base: `709760e`
- Updated main commit: `aabdc0f` - `feat: add release validation policy`
- Feature commits:
  - `5bc1eb2` - `feat: add release preparation tool`
  - `8eebdce` - `feat: validate release version format`
  - `33eb31f` - `feat: add release channel label formatter`
  - `4cfc815` - `feat: load release validation policy`
  - `558cff9` - `feat: enforce release validation policy`

### Observations before rebase

- The release tool failed with `FileNotFoundError` because `release-policy.json` existed on main but was absent from the feature branch.
- The feature branch had five commits based on the older main history.

### After rebase

- Command: `git rebase main`
- Result: Successfully rebased `feature/advanced-branching` onto `aabdc0f`.
- Replayed feature commits:
  - `97731c7` - `feat: add release preparation tool`
  - `a024da2` - `feat: validate release version format`
  - `e9d9b65` - `feat: add release channel label formatter`
  - `c0b90a5` - `feat: load release validation policy`
  - `d35afe3` - `feat: enforce release validation policy`

### Verification

- `git merge-base main feature/advanced-branching` returned `aabdc0f2106b8b4dde2bbda4ff59333f832648b8`.
- The release tool ran successfully after rebase.
- Ruff check passed and Ruff formatting left the file unchanged.
- An in-memory channel-membership check confirmed that `invalid` is not an allowed release channel.
- `git status -sb` showed a clean working tree.

### Lessons learned

- Cherry-pick applies selected commits and creates new commits on the target branch.
- Dependent commits must be applied in an order that satisfies their prerequisites.
- Rebase replays feature commits on top of a new base and normally creates new commit IDs.
- A rebased branch can use files introduced by its new base commit.
- The merge base identifies shared ancestry; it does not itself prove that tests pass.

## Exercise 4: Comparing Merge and Rebase

### Merge workflow

- Comparison branch: `lab/merge-comparison`
- Feature commit: `33737ec` - `feat: add release approval policy`
- Updated `main` commit: `f39dc84` - `feat: add release notes policy`
- Merge commit: `3b48b27` - `Merge branch 'main' into lab/merge-comparison`

**Observation:** Merging `main` into the comparison branch preserved both lines of history and created a merge commit with two parents. The original feature commit ID remained unchanged.

### Rebase workflow

- Comparison branch: `lab/rebase-comparison`
- Original feature commit: `48a9eb8` - `feat: configure manual release approval`
- Updated `main` commit: `b40d7b4` - `feat: add release approval notifications`
- Rebased feature commit: `2f2d20b` - `feat: configure manual release approval`

**Observation:** Rebasing replayed the feature change on top of the updated `main`. The feature commit received a new ID, and the resulting history was linear without a merge commit.

### Verification

- `git rebase main` completed successfully without conflicts.
- `python -m json.tool` validated `release-policy.json`.
- `Test-Path` confirmed `notification-policy.json` exists.
- The release approval setting remained present after rebase.
- `git status -sb` showed no tracked changes.

### Key takeaway

Merge preserves the existing branch histories and joins them with a merge commit. Rebase replays feature commits on a new base, creating new commit IDs. Both approaches can integrate changes successfully; the choice depends on the desired history and team workflow.
