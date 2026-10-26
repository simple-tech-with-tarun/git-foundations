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

Git commonly reports the following states for changes:

- **Untracked:** A file exists in the working tree but is not tracked by Git.
- **Modified, unstaged:** A tracked file has changes that are not staged.
- **Staged:** Changes are selected for inclusion in the next commit.

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

When the working tree matches the staging area, `git diff HEAD` and `git diff --staged` show the same content differences relative to `HEAD`.

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

## 9. Undoing and Removing Changes

Git provides commands to discard unstaged changes, unstage changes, remove tracked files, and stop tracking files without deleting their local copies. These operations affect the working tree and staging area differently, so it is important to understand their effects before running them.

### `git restore <file>` — discard unstaged changes

Restores a file in the working tree from the staging area (index) by default.

```powershell
git restore fundamentals/restore-practice.txt
```

If a tracked file has been modified but the changes have not been staged, this command discards those modifications and restores the file to the version in the index.

**Important:** This can permanently discard uncommitted changes to the specified file. Inspect the changes with `git diff` before restoring.

### `git restore --staged <file>` — unstage changes

Removes the specified file's staged changes from the index while preserving its working-tree content.

```powershell
git restore --staged fundamentals/restore-practice.txt
```

After running this command, the index is restored to the version in `HEAD`, while the file's working-tree content remains unchanged.

If the file contains modifications, `git status` will show those changes as unstaged, and `git diff` will display them. `git diff --staged` will no longer display those changes.

### `git rm <file>` — remove a tracked file

Removes a tracked file from the working tree and stages its deletion.

```powershell
git rm fundamentals/restore-practice.txt
```

The file is removed from the working directory, and the deletion is recorded in the staging area. The deletion becomes part of repository history only when committed.

If the deletion has been staged but not committed, it can be undone by first restoring the index and then restoring the working-tree file:

```powershell
git restore --staged fundamentals/restore-practice.txt
git restore fundamentals/restore-practice.txt
```

The first command unstages the deletion. The second restores the file from the index.

### `git rm --cached <file>` — stop tracking a file

Removes a file from Git's index without deleting the local copy.

```powershell
git rm --cached fundamentals/restore-practice.txt
```

Git stages the file's removal from the repository, but the file remains in the working directory. `git status` shows a staged deletion and an untracked file with the same path.

The change becomes part of repository history only if committed. Until then, the previous commit still contains the file.

### Verify the effects of these commands

Use the following commands to inspect repository state and compare changes:

```powershell
git status
git status --short
git diff
git diff --staged
git ls-files
git ls-files --others --exclude-standard
```

- `git status` summarizes staged and unstaged changes.
- `git status --short` provides a compact status view.
- `git diff` displays unstaged changes to tracked files.
- `git diff --staged` displays staged changes relative to `HEAD`.
- `git ls-files` lists paths in Git's index.
- `git ls-files --others --exclude-standard` lists untracked files that are not excluded by standard ignore rules.

**Key distinction:** `git restore` changes file content or staging state, depending on its options. `git rm` stages a file's removal from tracking, with `--cached` preserving the local copy. None of these commands creates a commit.

---

## 10. Branching and Switching

Branches allow you to develop features, fix bugs, and experiment without making changes directly on another branch. A branch is a reference to a commit, not a separate copy of the repository.

### Understanding branches and `HEAD`

A branch name points to a commit. When a new commit is created on that branch, the branch reference advances to the new commit.

`HEAD` identifies the currently checked-out commit. In a typical branch-based workflow, `HEAD` points symbolically to the current branch.

For example, when `feature/logging` is checked out:

```text
HEAD -> feature/logging -> commit
```

Inspect the current branch:

```powershell
git branch --show-current
```

List local branches:

```powershell
git branch
```

The asterisk (`*`) identifies the current branch.

Display branch names, their latest commit hashes, and commit subjects:

```powershell
git branch -v
```

Include upstream tracking information, when configured:

```powershell
git branch -vv
```

Inspect the symbolic reference followed by `HEAD`:

```powershell
git symbolic-ref HEAD
```

On a branch named `feature/logging`, this typically prints:

```text
refs/heads/feature/logging
```

Inspect the latest commit reachable from `HEAD`:

```powershell
git log -1 --oneline HEAD
```

These commands help identify the current branch, its latest commit, and the relationship between `HEAD` and branch references.

### Switching branches

Use `git switch <branch>` to switch to an existing branch:

```powershell
git switch main
```

To create a new branch and switch to it immediately, use `git switch -c <new-branch>`:

```powershell
git switch -c feature/logging
```

The new branch starts at the currently checked-out commit. Creating a branch does not itself create a new commit or copy the repository.

### Switching with uncommitted changes

Git checks whether switching branches can be performed without overwriting local work.

- **Clean working tree:** Switching normally proceeds without conflicts.
- **Modified tracked files:** Git may block a switch if the target branch would overwrite or remove local changes.
- **Untracked files:** These generally remain in the working directory when switching, provided they do not conflict with files tracked by the target branch.

For example, Git may refuse to switch if a modified tracked file would be replaced by a different version from the target branch.

Before switching, inspect the repository state:

```powershell
git status
```

If necessary, commit the changes or temporarily save them with `git stash`. Do not discard changes unless you are certain they are no longer needed.

### Deleting branches

Use `git branch -d <branch>` to delete a branch safely:

```powershell
git branch -d feature/logging
```

Git checks whether the branch's work has been merged into the relevant reference. If the branch contains unmerged commits, Git normally refuses the deletion.

Use `git branch -D <branch>` to force-delete a branch:

```powershell
git branch -D feature/logging
```

The uppercase `-D` bypasses the unmerged-work safeguard. It removes the branch reference, not necessarily the commit objects immediately. Commits that are no longer reachable from other references may eventually be garbage-collected.

Prefer `-d` for normal cleanup. Use `-D` only when you have confirmed that the branch's unmerged work is no longer needed.

**Key takeaway:** Branches are lightweight references to commits. `git switch` changes the checked-out branch, while `git branch -d` protects against accidentally deleting unmerged work.

---

## 11. Merging and Merge Conflicts

Merging integrates changes from one branch into another. It allows work developed on separate branches to become part of a shared branch while preserving the project's commit history.

### 11.1 Understanding Git Merges

When you merge a branch, Git attempts to integrate its changes into the currently checked-out branch.

The current branch is the **target branch**, and the branch being integrated is the **source branch**.

```powershell
git switch main
git merge feature-branch
```

This switches to `main` and merges `feature-branch` into it.

**Important:** The merge affects the branch you currently have checked out. Git does not automatically switch to the source branch.

### 11.2 Fast-Forward Merges

A fast-forward merge is possible when the target branch has not diverged from the source branch's history.

Instead of creating a new commit, Git advances the target branch pointer to the source branch's latest commit.

```powershell
git switch main
git merge feature-branch
```

A successful fast-forward merge produces output similar to:

```text
Updating abc1234..def5678
Fast-forward
```

Characteristics of a fast-forward merge:

- No new merge commit is created.
- The target branch pointer advances to an existing commit.
- The existing commit history remains unchanged.

Fast-forward merges are possible when the target branch can advance directly to the source branch's tip without combining divergent histories.

### 11.3 Three-Way Merges and Merge Commits

When both branches have new commits since they diverged, Git cannot simply advance the target branch pointer.

Git uses a three-way merge, considering:

- The common ancestor of the two branches.
- The current state of the target branch.
- The current state of the source branch.

When the changes can be integrated, Git typically creates a **merge commit** that connects the two histories.

```powershell
git switch main
git merge feature-branch
```

A merge commit has two parents in a standard two-branch merge. It records the integration of the two lines of development.

A merge commit may also be created when a fast-forward would otherwise be possible by using:

```powershell
git merge --no-ff feature-branch
```

This forces Git to create a merge commit rather than fast-forwarding.

### 11.4 Understanding Merge Conflicts

A merge conflict occurs when Git cannot automatically reconcile changes from different branches.

One common example is when two branches modify the same line of a file differently.

Suppose the target branch contains:

```text
Topic: merging strategies
```

The source branch contains:

```text
Topic: resolving merge conflicts
```

Git cannot determine which version should be kept, so it marks the file as conflicted and pauses the merge.

Conflicts do not necessarily mean the changes are incorrect. They mean that a human decision is needed to determine the intended result.

### 11.5 Reading Conflict Markers

During a content conflict, Git places markers in the affected file:

```text
[Current branch version]
Topic: merging strategies
[Separator]
Topic: resolving merge conflicts
[Incoming branch version]
```

The markers identify the competing versions:

- `<<<<<<< HEAD` begins the version from the current branch.
- `=======` separates the two versions.
- `>>>>>>> feature-branch` ends the incoming branch's version.

The incoming branch name appears after the final marker. The exact labels depend on the branches involved.

These markers are temporary conflict-resolution instructions, not content that should normally remain in the final file.

### 11.6 Resolving a Merge Conflict

Resolve a conflict by editing the affected file and choosing the intended final content. You may keep either version, combine them, or rewrite the content appropriately.

For example, the resolved file could contain:

```text
Topic: merging strategies and resolving merge conflicts
```

After editing the file, inspect the repository state:

```powershell
git status
```

Stage the resolved file:

```powershell
git add <resolved-file>
```

Staging a resolved file tells Git that the conflict has been addressed.

Check the status again:

```powershell
git status
```

Once all conflicts are resolved and staged, Git reports that all conflicts are fixed but the merge is still in progress. Complete the merge by creating the merge commit:

```powershell
git commit -m "Resolve merge conflict"
```

After the commit, verify the repository state:

```powershell
git status
```

A successful merge should leave the working tree clean if there are no other changes.

**Important:** Resolving and staging conflicts does not finish the merge. The merge must be committed unless it is aborted.

### 11.7 Inspecting Merge History

Git provides commands to inspect commits and understand how branches were integrated.

Display a compact commit history:

```powershell
git log --oneline
```

Display the history as a graph, including branch and tag references:

```powershell
git log --graph --oneline --decorate
```

Limit the graph to recent commits:

```powershell
git log --graph --oneline --decorate -10
```

The graph helps distinguish between:

- A fast-forward merge, which advances a branch pointer without creating a merge commit.
- A merge commit, which connects two previously divergent lines of development.
- Commits unique to each branch before the merge.

To inspect the changes recorded by a commit, including a merge commit:

```powershell
git show --stat HEAD
```

To compare the file contents represented by two branches:

```powershell
git diff main feature-branch
```

`git diff` compares the snapshots represented by the specified references. It does not, by itself, establish whether one branch has been merged into another.

---

## 12. Working with Remote Repositories

Remote repositories allow you to share commits between repositories and collaborate with other developers. Git supports this through remote configuration, fetching, pulling, and pushing.

Understanding these operations requires distinguishing between a local branch, a remote-tracking branch, and the branch stored in the remote repository.

### 12.1 Configuring Remotes

A **remote** is a named reference to another Git repository. Git commonly uses `origin` as the default name for the remote from which a repository was cloned.

List configured remotes and their URLs:

```powershell
git remote -v
```

Add a remote to an existing repository:

```powershell
git remote add origin <repository-url>
```

The remote name `origin` is conventional, not mandatory. A repository can have multiple remotes, each with its own name and URL.

Inspect the URLs configured for a specific remote:

```powershell
git remote get-url origin
```

### 12.2 Fetching Remote Changes

Fetching downloads commits and other relevant information from a remote repository and updates the corresponding remote-tracking references.

```powershell
git fetch origin
```

Fetching does not automatically merge remote changes into the current local branch or modify the working-tree files.

This makes fetching useful when you want to learn about incoming changes before deciding whether to integrate them.

### 12.3 Understanding Remote-Tracking Branches

A **remote-tracking branch** records the state of a remote branch as observed by your local repository during operations such as fetching.

For example:

- `main` is a local branch.
- `origin/main` is a remote-tracking branch representing the observed state of the remote's `main` branch.
- The actual remote branch is stored in the remote repository.

These references can point to different commits. For example, another contributor may push a commit to GitHub while your local `main` remains unchanged. After fetching, `origin/main` can advance to reflect that commit, while your local `main` stays where it was.

Inspect local branches and their upstream tracking information:

```powershell
git branch -vv
```

Check the current branch and working-tree state:

```powershell
git status -sb
```

Remember that remote-tracking branches reflect the latest remote state your local repository has observed; they are not necessarily a live view of the remote.

### 12.4 Inspecting Incoming Changes

After fetching, you can compare your current branch with its upstream before integrating changes.

Display commits reachable from the upstream but not from `HEAD`:

```powershell
git log HEAD..@{upstream} --oneline
```

Compare the file contents represented by the current commit and its upstream:

```powershell
git diff HEAD..@{upstream}
```

Count commits unique to each side of the comparison:

```powershell
git rev-list --left-right --count 'HEAD...@{upstream}'
```

The two numbers represent:

1. Commits reachable only from `HEAD`.
2. Commits reachable only from the upstream.

For example, `2 3` means the current branch has two commits not in the upstream, while the upstream has three commits not in the current branch.

These commands answer different questions: `git log` inspects commits, `git diff` compares file content, and `git rev-list` counts commits unique to each side.

The `@{upstream}` reference requires an upstream to be configured for the current branch. In PowerShell, quote the expression to prevent the shell from interpreting its special characters:

```powershell
git log 'HEAD..@{upstream}' --oneline
git diff 'HEAD..@{upstream}'
git rev-list --left-right --count 'HEAD...@{upstream}'
```

### 12.5 Pulling Remote Changes

`git pull` fetches remote changes and integrates them into the current branch according to the configured pull behavior.

```powershell
git pull
```

When an upstream is configured, Git uses it to determine which remote branch to pull from.

Unlike `git fetch`, pulling proceeds to integration rather than stopping after updating remote-tracking references. Depending on the branch history and configuration, integration may use a fast-forward, a merge, or a rebase.

Before pulling, inspect the working-tree state and review incoming changes when appropriate. This helps you understand what will be integrated and reduces the risk of unexpected conflicts.

### 12.6 Pushing Local Commits

Pushing publishes eligible local commits to a remote repository.

```powershell
git push
```

When the current branch has an upstream configured, Git can use that relationship to determine the default destination.

To push a new local branch and set its upstream at the same time:

```powershell
git push -u origin <branch-name>
```

The `-u` option, also called `--set-upstream`, configures the upstream relationship after a successful push. This allows subsequent `git push` and `git pull` commands to use the configured relationship by default.

Pushing does not automatically update other developers' local branches. They must fetch or pull the remote changes into their own repositories.

### 12.7 Understanding Upstream Tracking

An **upstream branch** is the remote-tracking branch associated with a local branch. This relationship helps Git determine the default remote branch for synchronization operations.

For example, a local `main` branch commonly tracks `origin/main`. A feature branch may track `origin/feature/example`.

Inspect the upstream of the current branch:

```powershell
git rev-parse --abbrev-ref --symbolic-full-name '@{upstream}'
```

If no upstream is configured, Git reports an error. You can establish the relationship when publishing a new branch:

```powershell
git push -u origin <branch-name>
```

Use `git branch -vv` to inspect upstream information across local branches.

A local branch can exist without an upstream. Creating a branch locally does not automatically create its remote counterpart or configure tracking.

### 12.8 A Practical Remote Synchronization Workflow

A safe synchronization workflow separates inspection, integration, and publication.

```powershell
git status -sb
git fetch origin
git branch -vv
git log 'HEAD..@{upstream}' --oneline
git diff 'HEAD..@{upstream}'
git pull
git status -sb
git push
```

This sequence assumes that the current branch has an upstream configured and that the intended operation is to integrate its upstream changes before pushing local work.

The workflow demonstrates the following:

1. Inspect the current branch and working-tree state.
2. Fetch remote updates without immediately integrating them.
3. Check branch tracking information.
4. Review incoming commits and file differences.
5. Pull changes when ready to integrate them.
6. Verify the repository state after integration.
7. Push local commits when they are ready to publish.

If the branch has no upstream, establish the appropriate tracking relationship first. If the local and remote histories have diverged, inspect both sides before choosing how to integrate them.

**Key distinction:** `git fetch` updates your knowledge of the remote, `git pull` fetches and integrates changes, and `git push` publishes local commits. Upstream tracking connects these operations to the intended remote branch.

---

## 13. Working with Git Tags

Git tags are references used to mark specific commits in a repository's history. They are commonly used to identify releases, milestones, and other important points in a project's development.

Unlike branches, tags do not automatically move forward when new commits are created. A tag can point to a commit that is reachable from `main`, a feature branch, or another branch's history.

### 13.1 Listing Tags

List all tags in the local repository:

```powershell
git tag
```

Use `--list` to explicitly list tags:

```powershell
git tag --list
```

If no tags exist, these commands return no output.

### 13.2 Lightweight and Annotated Tags

Git supports two common types of tags.

**Lightweight tags** are simple references to a commit. They do not create a separate tag object containing tagger information or a message.

Create a lightweight tag:

```powershell
git tag v1.0
```

**Annotated tags** create a separate Git tag object containing the tagger, creation date, message, and reference to the target object. They are generally preferred for releases and other significant milestones.

Create an annotated tag:

```powershell
git tag -a v1.0 -m "Version 1.0"
```

Both types can point to the current commit or a specific earlier commit.

### 13.3 Tagging a Specific Commit

To tag a specific commit, provide its commit hash or another valid commit reference.

Create a lightweight tag for a specific commit:

```powershell
git tag v1.0 <commit-hash>
```

Create an annotated tag for a specific commit:

```powershell
git tag -a v1.0 <commit-hash> -m "Version 1.0"
```

Creating a tag for an earlier commit does not require checking out that commit.

### 13.4 Inspecting Tags

Use `git show` to inspect a tag and its target commit:

```powershell
git show v1.0
```

For annotated tags, the output includes the tag metadata and the target commit's information. Depending on the target commit, it may also show a diff.

To display the tag and commit information without the patch:

```powershell
git show v1.0 --no-patch
```

Inspect the underlying Git object type:

```powershell
git cat-file -t v1.0
```

A lightweight tag normally resolves directly to a `commit` object, while an annotated tag resolves to a `tag` object.

To resolve either tag to its target commit hash:

```powershell
git rev-parse 'v1.0^{commit}'
```

The `^{commit}` suffix peels the tag and resolves it to the commit it ultimately references. In PowerShell, quote the complete expression so the shell does not misinterpret the special characters.

### 13.5 Inspecting Merge Commits

A merge commit has multiple parents. By default, `git show` generally does not display a patch for a merge commit.

Use `-m` to display separate diffs against its parents:

```powershell
git show -m v1.0
```

This helps inspect the changes introduced by a merge relative to each parent. The option changes how Git displays the commit; it does not modify the commit or tag.

### 13.6 Pushing Tags to a Remote

Pushing a branch does not automatically push every local tag.

Push one specific tag:

```powershell
git push origin v1.0
```

List tags advertised by the remote:

```powershell
git ls-remote --tags origin
```

To push all local tags that are not already present on the remote:

```powershell
git push origin --tags
```

Use `--tags` carefully because it publishes all local tags, including tags that may have been created for testing.

### 13.7 Deleting Tags

Delete a local tag:

```powershell
git tag -d v1.0
```

Delete a tag from a remote repository:

```powershell
git push origin --delete v1.0
```

These operations delete tag references, not the commits themselves. Removing a remote tag does not automatically delete the corresponding local tag, and deleting a local tag does not automatically remove the remote tag.

### 13.8 Renaming Tags

Git does not provide a dedicated tag-renaming command. To rename a tag, create a new tag with the desired name pointing to the same target, then delete the old tag.

For example:

```powershell
git tag new-name old-name
git tag -d old-name
```

If the old tag has already been pushed, update the remote separately by pushing the new tag and deleting the old remote tag.

### 13.9 Tags Versus Branches

Tags and branches can both reference commits, but they serve different purposes.

- **Branches** are movable references that normally advance when new commits are created on them.
- **Tags** mark specific points in history and do not automatically advance when new commits are created.
- A tag can reference a commit reachable from any branch; it is not restricted to `main`.
- Tags are useful for releases and milestones, while branches are used to continue and organize development work.

Annotated tags are a good choice for meaningful releases and milestones because they include metadata and a descriptive message.

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
- `git restore <file>` discards unstaged changes by restoring content from the index.
- `git restore --staged <file>` unstages changes while preserving working-tree content.
- `git rm <file>` removes a tracked file and stages its deletion.
- `git rm --cached <file>` stages removal from Git's index while keeping the local file.
- `git status`, `git diff`, and `git diff --staged` help verify the effects of changes before committing.
- Branches are references to commits, and `HEAD` identifies the currently checked-out commit.
- `git branch`, `git branch -v`, and `git branch -vv` provide different levels of branch information.
- `git switch <branch>` switches branches, while `git switch -c <new-branch>` creates and switches to a new branch.
- Git may block branch switching when local changes would be overwritten; untracked files generally remain in the working directory unless a conflict prevents switching.
- `git branch -d` safely deletes a branch when its work is merged, while `git branch -D` force-deletes the branch reference.
- **Merging branches:** A fast-forward merge advances the target branch pointer without creating a merge commit. When branches have diverged, Git may create a merge commit to connect their histories.
- **Resolving conflicts:** Git marks conflicting content with conflict markers when it cannot automatically reconcile changes. Resolve the file, stage the result, and commit to complete the merge.
- **Inspecting history:** Use `git log --graph --oneline --decorate` to visualize branch divergence and merge relationships. Use `git diff` to compare file snapshots between references.
- A remote is a named reference to another Git repository, commonly identified by a name such as `origin`.
- `git fetch` updates remote-tracking references without automatically integrating changes into the current branch.
- `git pull` fetches and integrates remote changes, while `git push` publishes eligible local commits.
- Remote-tracking branches such as `origin/main` represent the remote state observed during the latest fetch.
- `git log`, `git diff`, and `git rev-list` help inspect incoming changes, compare snapshots, and count commits unique to each side.
- Upstream tracking identifies the remote-tracking branch used by default for operations such as `git pull` and `git push`.
- `git push -u origin <branch-name>` publishes a branch and configures its upstream after a successful push.
- Git tags mark specific commits and are commonly used for releases and development milestones.
- Lightweight tags are simple commit references, while annotated tags include metadata and a message and are generally preferred for releases.
- Tags can point to commits reachable from any branch; they are not restricted to `main`.
- `git show`, `git cat-file -t`, and `git rev-parse 'tag-name^{commit}'` help inspect tags and resolve their target commits.
- `git push origin <tag-name>` publishes a specific tag; pushing a branch does not automatically publish every local tag.
- Local and remote tags are managed separately. Deleting a tag removes the reference, not the commit itself.
- `git show -m <commit>` displays separate diffs for a merge commit against its parents, while `--no-patch` suppresses patch output.

These fundamentals provide the basis for understanding branching, merging, remote synchronization, and safe history management.
