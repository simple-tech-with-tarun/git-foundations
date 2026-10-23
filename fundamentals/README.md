# Git Fundamentals

## 1. Introduction to Version Control

Version control is a system for tracking changes to files over time. It allows developers to review previous versions, understand what changed, and collaborate without relying on manually maintained copies of files.

Consider a project where files are saved with names such as:

```text
app_v1.py
app_v2.py
app_final.py
app_final_updated.py
app_final_latest.py
```

This approach quickly becomes difficult to manage. It is not always clear which version is correct, what changed between versions, or how to recover an earlier state.

A version control system addresses these problems by recording changes in a structured and traceable way.

### Why use version control?

- **Change tracking:** Understand what changed and when.
- **History:** Review earlier versions of a project.
- **Recovery:** Restore previous versions when needed.
- **Collaboration:** Allow multiple people to work on the same project.
- **Accountability:** Identify the author of a change and understand its purpose.
- **Experimentation:** Develop new features without losing the existing working version.

### Types of version control systems

Version control systems are commonly categorized into two types.

**Centralized Version Control System (CVCS)**

A centralized system maintains a central repository that users access to retrieve and submit changes. The central server is the primary location for project history.

Examples include Subversion (SVN) and Perforce in its centralized workflow.

**Distributed Version Control System (DVCS)**

A distributed system gives each user a local repository containing the project's history. Users can commit changes locally and synchronize with other repositories when needed.

Git is a distributed version control system. This allows developers to work and record commits locally without requiring a network connection for every operation.

---

## 2. Introduction to Git

Git is a free, open-source, distributed version control system designed to track changes in files and support software development workflows.

It was originally created by Linus Torvalds in 2005 to support Linux kernel development.

Git records project history through commits. Each commit represents a recorded snapshot of the project and connects to the surrounding history.

### Git vs. GitHub

Git and GitHub are related, but they are not the same thing.

| Git | GitHub |
|---|---|
| A version control system | A platform for hosting Git repositories and collaborating |
| Runs locally on a developer's machine | Provides online services for repositories |
| Tracks changes through commits | Adds pull requests, issues, code reviews, and collaboration features |
| Can be used without an internet connection for local work | Requires network access for online collaboration |

Git can be used without GitHub. A developer can initialize a repository, make commits, and inspect its history entirely on a local machine.

GitHub provides a place to host repositories and collaborate with others.

### Local and remote repositories

A **local repository** is the repository available on your machine. It contains Git's metadata and recorded project history.

A **remote repository** is another repository that Git can communicate with, commonly hosted on a platform such as GitHub.

A remote is not required to use Git. It becomes useful when sharing changes or collaborating with other developers.

---

## 3. Understanding the Git Workflow

A typical Git workflow involves three important areas:

1. **Working tree:** The files you view and modify in your project.
2. **Staging area:** The changes selected for inclusion in the next commit.
3. **Local repository:** The recorded commits and project history.

The relationship between these areas is illustrated below:

```text
Working Tree
     |
     | git add
     v
Staging Area
     |
     | git commit
     v
Local Repository
     |
     | git push
     v
Remote Repository
```

The first three areas form the core local workflow. Pushing changes to a remote repository is a separate operation.

### Working tree

The working tree contains the project files you interact with. You can create, edit, and delete files here.

Git compares the working tree with the staging area or a committed snapshot to identify differences.

### Staging area

The staging area allows you to choose which changes will be included in the next commit.

For example, if you modify three files, you can stage only one of them and commit that change separately.

The staging area is also called the **index** in Git documentation.

Use `git add` to stage changes:

```powershell
git add .\fundamentals\notes.txt
```

This stages the current contents of the specified file. If you modify the file again after staging it, the new modifications are not staged automatically.

### Local repository and commits

When you create a commit, Git records the staged state as a new snapshot in the repository's history.

```powershell
git commit -m "Add Git fundamentals introduction"
```

A commit includes the recorded project state, metadata such as the author and timestamp, a commit message, and a reference to its parent commit or commits.

Each commit has a unique identifier represented by a hash. Git commonly displays an abbreviated version of this identifier in its output.

### Remote repository

A remote repository provides a location for sharing commits with another repository.

- `git push` sends eligible local commits to a remote.
- `git fetch` retrieves information and commits from a remote without automatically integrating them into the current branch.
- `git pull` fetches changes and then integrates them into the current branch according to the configured pull behavior.

These remote operations are covered in more detail in the collaboration section.

---

## 4. Staging Changes

The staging area allows you to select which changes will be included in the next commit.

### Stage a specific file

Use `git add <file>` to stage changes to a particular file.

```powershell
git add fundamentals/notes.txt
```

This stages changes to `notes.txt` without automatically staging changes to other files.

### Stage changes from the current directory

Use `git add .` to stage changes under the current directory, including changes in nested directories.

```powershell
git add .
```

When run from the repository root, this stages applicable changes throughout the working tree, including new files, modifications, and deletions.

### Verify what is staged

After staging changes, inspect the repository status:

```powershell
git status
git status --short
```

To inspect the actual content of staged changes, use:

```powershell
git diff --staged
```

**Key takeaway:** `git add` updates the staging area. It does not create a commit; the staged changes become part of repository history only when you commit them.

---

## 5. Inspecting Repository State

Before staging or committing changes, inspect the repository to understand its current state.

### `git status`

Displays the current branch and summarizes changes in the working tree and staging area.

```powershell
git status
```

Git commonly classifies changes as:

- **Untracked:** A file exists in the working tree but is not tracked by Git.
- **Modified, unstaged:** A tracked file has changes that are not staged.
- **Staged:** Changes are selected for inclusion in the next commit.
- **Committed:** Changes have been recorded in repository history.

A clean working tree means there are no pending changes for Git to report.

### `git log`

Displays commit history.

```powershell
git log
```

For a compact view, use:

```powershell
git log --oneline
```

A commit history helps you understand how the project has evolved and identify commits for further inspection.

For example:

```text
2d29a78 Extend Git workflow practice notes
c0ca49d Add practical files for Git exercises
8ffb0fd Add Git fundamentals introduction
```

Each entry represents a commit. The abbreviated hash identifies the commit, and the accompanying text is its commit message.

### Understanding `HEAD`

`HEAD` identifies the commit currently checked out. In a typical branch-based workflow, `HEAD` refers to the current branch, which in turn points to a commit.

As new commits are created on that branch, its reference advances and `HEAD` follows it.

This makes `HEAD` a useful reference when inspecting the current state of the repository or comparing changes.

---

## 6. Understanding Git Differences

Git provides several commands for comparing file contents and committed snapshots. Understanding what each command compares is essential for reviewing changes before committing them.

### `git diff` — working tree vs. staging area

Displays changes in tracked files that have not been staged.

```powershell
git diff
```

If you edit a file without staging it, this command displays the difference between the working tree and the staging area.

If the working tree matches the staging area, the command produces no output.

### `git diff --staged` — staging area vs. `HEAD`

Displays staged changes that differ from the current commit.

```powershell
git diff --staged
```

Use this command before committing to review the changes selected for the next commit.

It is also possible to use the equivalent option:

```powershell
git diff --cached
```

Both commands display the difference between the staging area and `HEAD`.

### `git diff HEAD` — working tree vs. current commit

Displays differences between the working tree and the current commit, including both staged and unstaged changes.

```powershell
git diff HEAD
```

When there are no unstaged changes, the output will match `git diff --staged`, because the working tree and staging area contain the same content.

### Comparing two commits

Git can compare any two commit snapshots without switching branches or changing the working tree.

```powershell
git diff c0ca49d HEAD
```

This compares the snapshot identified by `c0ca49d` with the snapshot identified by `HEAD`.

The output shows the net differences between those snapshots, including changed files and line-level changes.

The order of the commits matters. Reversing the arguments reverses the comparison:

```powershell
git diff HEAD c0ca49d
```

Lines shown as additions in one comparison will appear as removals in the reversed comparison, and vice versa.

Comparing two commits shows the differences between their snapshots. It does not directly indicate how many commits separate them.

### Reading diff output

Consider the following example:

```diff
-This is the original line.
+This is the updated line.
```

- Lines prefixed with `-` represent content present in the first version but absent from the second.
- Lines prefixed with `+` represent content present in the second version but absent from the first.
- Unchanged lines may appear around the differences to provide context.

Git compares file content, not the intention behind an edit. Replacing a blank line with a new numbered line, for example, can appear as one deletion and one insertion.

The output is a representation of the difference between the compared states, not necessarily a record of every intermediate editing action.

---

## 7. Inspecting Commits

Use `git show` to inspect a specific commit.

### `git show`

Displays the commit metadata and the changes introduced by that commit relative to its parent.

```powershell
git show HEAD
```

You can also specify an abbreviated commit hash:

```powershell
git show c0ca49d
```

The output typically includes:

- The commit identifier.
- Author and timestamp.
- Commit message.
- Changed files and their diffs.

This is useful when reviewing an individual commit without changing the currently checked-out branch.

### `git show --stat`

Displays commit metadata and a summary of the files changed.

```powershell
git show --stat HEAD
```

Example:

```text
fundamentals/README.md | 2 +-
fundamentals/hello.py  | 4 ++++
fundamentals/notes.txt | 6 ++++++
3 files changed, 11 insertions(+), 1 deletion(-)
```

The summary identifies the number of changed files, insertions, and deletions. The `+` and `-` characters provide a compact visual representation of the line changes.

For the full patch, use `git show` without `--stat`.

---

## 8. Reviewing Changes Before a Commit

A reliable workflow is to inspect the repository at each stage rather than commit changes without reviewing them.

```powershell
git status
git diff
git add .\fundamentals\notes.txt
git diff --staged
git commit -m "Update Git fundamentals notes"
git status
git log -1 --oneline
```

This sequence demonstrates the following:

1. Inspect the current repository state.
2. Review unstaged changes.
3. Stage the intended file.
4. Review the staged changes.
5. Create a commit.
6. Verify that the working tree is clean.
7. Inspect the latest commit.

Staging and committing are separate operations. `git add` selects the content for the next commit; `git commit` records that staged content in repository history.

Reviewing staged changes before committing helps prevent unintended edits from entering a commit.

---

## Key Takeaways

- Git records project history through commits.
- The working tree, staging area, and repository history represent distinct states.
- `git status` summarizes the current state of the repository.
- `git add` stages changes, while `git commit` records them.
- `git diff`, `git diff --staged`, and `git diff HEAD` compare different repository states.
- `git diff <commit-1> <commit-2>` compares two committed snapshots.
- `git show` inspects an individual commit, while `git show --stat` summarizes its changes.
- `HEAD` identifies the currently checked-out commit.
- Reviewing changes before committing is an important habit in collaborative development.

These fundamentals provide the basis for understanding branching, merging, remote synchronization, and safe history management.
