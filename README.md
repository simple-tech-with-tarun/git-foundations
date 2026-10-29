# Git Foundations

<sub>🛡️ © 2026 Tarun Bansal · Simple Tech With Tarun. All rights reserved, except where otherwise stated. See the <a href="https://github.com/simple-tech-with-tarun/simple-tech-with-tarun/blob/main/COPYRIGHT.md">Copyright & Intellectual Property Notice</a>.</sub>

A practical learning repository for understanding Git, mastering version control workflows, and developing the skills needed to work confidently with Git in software development and DevOps environments.

This repository combines hands-on exercises, technical explanations, and practical references to help learners understand not only which Git commands to use, but also how Git works and why different workflows matter.

## 📚 Learning Areas

### 1. Git Fundamentals

The fundamentals section covers the essential concepts and workflows required to work with Git effectively.

Topics include:

- Introduction to version control and Git
- Understanding the Git workflow
- Working with the staging area and commits
- Inspecting repository state and differences
- Reviewing changes before committing
- Undoing and removing changes
- Branching and switching between branches
- Merging branches and handling merge conflicts
- Working with remote repositories
- Understanding and managing Git tags

**Learning materials:** [`fundamentals/`](fundamentals/)

The [Fundamentals Learning Guide](fundamentals/README.md) provides the detailed roadmap, organized into 13 sections, along with key takeaways and references.

### 2. Advanced Git

The advanced section builds on the fundamentals through focused topics, practical exercises, and dedicated documentation. Each topic explores specific Git workflows through hands-on practice, repository inspection, and documented results.

| Topic | Focus | Status |
|---|---|---|
| [History Rewriting](history-rewriting/README.md) | Rebasing, interactive rebase, amending commits, and squashing changes | Completed |
| [Advanced Branching](advanced-branching/README.md) | Cherry-picking, branch integration, and advanced conflict resolution | Completed |
| [Recovery and Undo](recovery-and-undo/README.md) | Restoring changes, resetting and reverting commits, reflog, and recovering work | In Progress |
| [Work Management](work-management/README.md) | Stashing changes and managing interrupted work | Planned |
| [Debugging and Investigation](debugging-and-investigation/README.md) | Bisecting history, inspecting contributions, and tracing bugs | Planned |
| [Git Internals](git-internals/README.md) | Objects, references, HEAD, and the internal structure of a repository | Planned |

Each advanced topic has, or will have, its own directory containing learning materials, practical exercises, and supporting documentation. Topics are developed incrementally, validated through hands-on practice, and integrated into `main` through pull requests.

## 🧠 Core Git Workflow

The fundamental Git workflow moves changes from the working directory through the staging area and into commits. Those commits are stored in the local repository and can be shared with a remote repository.

```text
Working Directory
       │
       ▼
   Staging Area
       │
       ▼
     Commit
       │
       ▼
 Local Repository
       │
       ▼
 Remote Repository
```

This workflow provides the foundation for understanding how Git tracks changes, records project history, and supports collaboration.

## 🛠️ How to Use This Repository

1. Start with the [Git Fundamentals Learning Guide](fundamentals/README.md).
2. Work through the topics in sequence, practicing the commands and examining their effects.
3. Use the accompanying reference documentation when revisiting a concept or command.
4. Progress to the advanced learning areas as their materials become available.

The repository is intended to serve as both a structured learning path and a long-term technical reference.

---

> **🛡️ Copyright & Intellectual Property**
>
> © 2026 Tarun Bansal · Simple Tech With Tarun. All rights reserved, except where otherwise stated.
>
> This repository may contain original technical documentation, tutorials, source code, Terraform configurations, scripts, diagrams, and other materials created and published by Tarun Bansal under the GitHub identity **Simple Tech With Tarun**.
>
> Public availability does not automatically grant permission to reproduce, republish, redistribute, or commercially exploit original materials. Please review the [Copyright & Intellectual Property Notice](https://github.com/simple-tech-with-tarun/simple-tech-with-tarun/blob/main/COPYRIGHT.md) before reusing such materials.
>
> Any explicit repository-level or file-level license governs the materials it covers. Third-party content and contributions remain subject to their respective ownership rights, licenses, and applicable terms.