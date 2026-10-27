# History Rewriting

This section explores how Git history can be modified to make commits clearer, better organized, and easier to review.

History rewriting is useful when preparing a feature branch for review. It allows you to correct commit messages, combine related changes, reorganize commits, and refine individual changes before sharing them.

> **Important:** Rewriting history changes commit IDs. Use these operations carefully on branches that have already been shared with others.

## Topics Covered

- Amending the latest commit with `git commit --amend`
- Changing commit messages with interactive rebase
- Reordering commits
- Resolving conflicts during an interactive rebase
- Combining commits with `squash`
- Combining commits with `fixup`
- Editing a commit during an interactive rebase

## Practical Exercises

The exercises use a small task tracker script to practise history rewriting with meaningful code changes.

### 1. Amend the Latest Commit

**Command:**

```bash
git commit --amend
```

Amending replaces the latest commit with a new commit containing the updated content, commit message, or both.

**What to remember:**
- The amended commit receives a new commit ID.
- `git commit --amend --no-edit` updates the commit without changing its message.
- Amendments are most straightforward before the commit is shared.

### 2. Reword a Commit Message

Start an interactive rebase:

```bash
git rebase -i HEAD~2
```

Change `pick` to `reword` beside the commit whose message needs updating.

**What to remember:**
- `reword` changes a commit message without intentionally changing its content.
- The rebase creates a new commit ID for the rewritten commit.
- Choose the correct commit in the interactive rebase list.

### 3. Reorder Commits

In the interactive rebase editor, rearrange the relevant `pick` lines into the desired order.

**What to remember:**
- Later commits may depend on changes introduced by earlier commits.
- Reordering dependent commits can produce conflicts or leave intermediate commits in an invalid state.
- Resolve conflicts carefully and validate the resulting code after the rebase.

### 4. Squash Commits

In the interactive rebase editor, change `pick` to `squash` for a commit that should be combined with the preceding commit.

**What to remember:**
- `squash` combines changes with the preceding commit.
- Git lets you edit the resulting combined commit message.
- Squashing is useful for consolidating related incremental work.

### 5. Fix Up Commits

Change `pick` to `fixup` for a commit that should be absorbed into the preceding commit.

**What to remember:**
- `fixup` combines the changes into the preceding commit.
- The preceding commit's message is retained by default.
- It is useful for folding small corrections into the commit they belong to.

### 6. Edit a Commit During Rebase

Change `pick` to `edit` for the commit you want to modify.

When Git pauses, amend the commit and continue:

```bash
git commit --amend --no-edit
git rebase --continue
```

**What to remember:**
- `edit` tells Git to pause at the selected commit.
- `git commit --amend` makes the actual change to that paused commit.
- `git rebase --continue` resumes the rebase after the edit is complete.

## Key Takeaways

- Git history can be refined before a branch is merged.
- Interactive rebase provides control over commit messages, order, and grouping.
- `squash` and `fixup` both combine commits, but handle commit messages differently.
- `edit` pauses a rebase so a commit can be changed.
- Reordering commits can expose dependencies and cause conflicts.
- Always inspect the rewritten history and test the resulting code.
- Be especially careful when rewriting commits that have already been pushed or shared.

## Useful Commands

| Command | Purpose |
|---|---|
| `git commit --amend` | Amend the latest commit |
| `git rebase -i HEAD~N` | Interactively rewrite the last N commits |
| `git rebase --continue` | Continue after resolving a conflict or editing a commit |
| `git rebase --abort` | Cancel the current rebase and return to its original state |
| `git log --oneline --graph` | Inspect commit history |
| `git status` | Check the working tree and rebase state |

## Next Steps

Continue to [Advanced Branching](../advanced-branching/README.md) to explore cherry-picking, rebasing feature branches, and comparing merge and rebase workflows.
