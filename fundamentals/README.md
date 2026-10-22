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

Git is a distributed version control system.

This allows developers to work and record commits locally without requiring a network connection for every operation.

---

## 2. Introduction to Git

Git is a free, open-source, distributed version control system designed to track changes in files and support software development workflows.

It was originally created by Linus Torvalds in 2005 to support Linux kernel development.

Git records project history through commits. Each commit represents a recorded state of the project and contains information that connects it to the surrounding history.

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

Git can compare the working tree with the content recorded in the repository and identify changes.

### Staging area

The staging area allows you to choose which changes will be included in the next commit.

For example, if you modify three files, you can stage only one of them and commit that change separately.

The staging area is also called the **index** in Git documentation.

### Local repository

When you create a commit, Git records the staged state as a new snapshot in the repository's history.

Commits can be inspected later to understand how the project evolved.

### Remote repository

A remote repository provides a location for sharing commits with another repository.

The `git push` command sends eligible local commits to a remote, while `git fetch` retrieves information and commits from a remote without automatically integrating them into the current branch.

The `git pull` command fetches changes and then integrates them into the current branch according to the configured pull behavior.

These remote operations will be covered in more detail in a later section.
