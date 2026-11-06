# Exercise 4: Commit Graphs and Object Relationships

## Overview

Explore how Git represents commit history as a directed acyclic graph (DAG). Investigate parent-child relationships, commit snapshots, branching, merge commits, and history traversal.

This exercise focuses on understanding how commits connect to one another and how Git traverses those relationships.

## Learning Objectives

- Understand commit ancestry and parent relationships.
- Examine how commits reference tree snapshots.
- Investigate branching and divergent histories.
- Understand merge commits and multiple parents.
- Traverse commit graphs using Git history commands.
- Compare commit ranges and identify unique commits.

## Topics Covered

1. **Commit Ancestry**
   - Parent and child commit relationships.
   - Root commits and linear history.
   - Traversing commit ancestry.

2. **Commit Snapshots**
   - How commits reference tree objects.
   - Comparing snapshots across commits.
   - Understanding how file changes relate to commit history.

3. **Branching and Divergent Histories**
   - Common ancestors.
   - Divergent commit histories.
   - Comparing branches and commit ranges.

4. **Merge Commits**
   - Multiple parent relationships.
   - First-parent and second-parent history.
   - Understanding merge results and snapshots.

5. **Commit Graph Traversal**
   - Visualizing history with `git log --graph`.
   - Inspecting parent relationships.
   - Using revision ranges to identify unique commits.

## Exercise Structure

### Exercise 1: Exploring Commit Ancestry
- Inspect commit objects and their parent references.
- Identify root commits and trace commit ancestry.
- Understand how Git represents linear history.

### Exercise 2: Understanding Commit Snapshots
- Inspect the tree referenced by a commit.
- Compare tree snapshots across different commits.
- Investigate how commit history relates to repository content.

### Exercise 3: Investigating Branching and Divergence
- Identify common ancestors between branches.
- Examine divergent commit histories.
- Compare commits unique to each branch.

### Exercise 4: Analyzing Merge Commits
- Inspect merge commits with multiple parents.
- Identify first-parent and second-parent relationships.
- Compare merge results with their parent snapshots.

### Exercise 5: Commit Graph Traversal
- Visualize commit history using Git graph commands.
- Traverse commit ranges.
- Identify reachable and unique commits across histories.
- Combine ancestry, snapshots, branching, and merge analysis.

## Practical Investigation

### 1. Commit Ancestry Investigation

Inspected commit objects to understand how Git records parent relationships.

Commands used:
```powershell
git cat-file -p HEAD
git cat-file -p 8aa72a8
git rev-list --parents -8 HEAD
```

Findings:
- Each commit references a tree representing its repository snapshot.
- Each non-root commit references one or more parent commits.
- Root commits have no parent reference.
- Git represents commit history through backward-pointing parent relationships.
- Following parent references allows Git to traverse commit ancestry.

### 2. Commit Snapshot Investigation

Examined how commits reference tree objects and how repository snapshots change between commits.

Commands used:
- `git ls-tree HEAD`
- `git ls-tree 8c4b4cb9`
- `git diff 8aa72a8 fb541c2 -- git-internals/`
- `git log --oneline --format="%h %T %s" -3 feature/git-internals`

Findings:
- Every commit references a root tree object representing its repository snapshot.
- Tree objects can reference blobs and other trees, forming a hierarchical snapshot.
- Different commits can reference different tree objects when repository content changes.
- Comparing commit trees helps identify snapshot differences.
- Commit ancestry and snapshot content are separate relationships: parent references establish history, while tree references represent repository content at a particular commit.

### 3. Branching and Divergent History Investigation

Investigated how Git represents branches that share a common ancestor but contain different commits.

Commands used:
- `git merge-base cd0e2d7 b43a82d`
- `git rev-list --left-right --count cd0e2d7...b43a82d`
- `git log cd0e2d7..b43a82d`
- `git log b43a82d..cd0e2d7`

Findings:
- Branches can share a common ancestor and subsequently develop independently.
- `git merge-base` identifies the best common ancestor between two histories.
- The symmetric difference (`...`) identifies commits reachable from either side but not both.
- `git rev-list --left-right --count` reports commits unique to each side.
- Double-dot (`..`) notation identifies commits reachable from the second revision but not the first.
- In the investigated histories, four commits were unique to the first side and two to the second side.

### 4. Merge Commit Investigation

Inspected a real merge commit to understand how Git records multiple parent relationships and represents the resulting repository snapshot.

Commands used:
- `git cat-file -p 4b11cc9`
- `git log --oneline --graph --parents -8 4b11cc9`
- `git log --oneline --first-parent -8 4b11cc9`
- `git diff --stat cd0e2d7 4b11cc9`
- `git rev-parse 'b43a82d^{tree}'`

Findings:
- Merge commits contain multiple parent references.
- The investigated merge commit `4b11cc9` had two parents: `cd0e2d7` and `b43a82d`.
- The first parent represented the destination branch history; the second parent represented the merged feature branch.
- First-parent traversal follows the mainline integration history.
- The merge commit referenced tree `9193607a`, which was identical to the tree referenced by its second parent.
- A merge commit has its own commit identity even when its snapshot matches one of its parents.
- Merge commits connect previously divergent histories into a shared commit graph.

### 5. Commit Graph Traversal Investigation

Explored how Git traverses commit history and how revision ranges help analyze relationships between commits.

Commands used:
- `git log --oneline --graph --all -16`
- `git rev-list --parents -5 feature/git-internals`
- `git rev-list --count 356772c..fb541c2`
- `git rev-list --count 356772c...fb541c2`
- `git diff --stat 356772c fb541c2`

Findings:
- `git log --graph` visualizes commit ancestry and branching relationships.
- `git rev-list --parents` exposes parent relationships for each commit.
- Double-dot notation identifies commits reachable from one revision but not the other.
- Triple-dot notation identifies commits reachable from either revision, excluding commits reachable from both.
- Since `356772c` was an ancestor of `fb541c2`, both range expressions returned two commits in this investigation.
- Reversing the double-dot range returned zero commits because the earlier commit had no descendants unique to it.
- Comparing commit ranges and diff statistics provides complementary views of history and repository changes.

### 6. Commit Graph and Snapshot Observations

Compared commit ancestry, tree references, and repository changes to understand how Git connects history with repository snapshots.

Key observations:
- Commit objects form a directed acyclic graph (DAG).
- Parent references establish commit ancestry.
- Tree references represent the repository snapshot associated with each commit.
- Branches are represented by references to commits within the graph.
- Merge commits connect divergent histories through multiple parent references.
- First-parent traversal provides a mainline view of merge history.
- Commit range comparisons identify differences in reachability.
- Two commits can have different identities while referencing identical tree snapshots.

## Key Takeaways

- Git stores commit history as a directed acyclic graph rather than a simple linear sequence.
- Every commit references a tree object representing its repository snapshot.
- Parent references establish ancestry between commits.
- Branching creates divergent paths from a shared commit ancestor.
- Merge commits contain multiple parent references and connect divergent histories.
- First-parent traversal helps isolate the mainline integration history.
- Double-dot and triple-dot notation provide different ways to compare commit reachability.
- Commit identity and snapshot identity are distinct: different commits can reference the same tree.
- Git history commands provide different perspectives on ancestry, reachability, and repository changes.

## Useful Commands

| Command | Purpose |
|---|---|
| `git cat-file -p <commit>` | Inspect commit contents and parent references |
| `git ls-tree <commit>` | Inspect a commit's root tree |
| `git rev-list --parents <commit>` | Display commits and their parent relationships |
| `git log --oneline --graph --all` | Visualize commit history |
| `git log --first-parent <commit>` | Follow first-parent history |
| `git merge-base <branch1> <branch2>` | Find the common ancestor |
| `git rev-list --left-right --count A...B` | Count commits unique to each side |
| `git log A..B` | List commits reachable from B but not A |
| `git diff A B` | Compare repository snapshots |
| `git rev-parse <commit>^{tree}` | Resolve a commit to its tree object |

## Completion Status

- [x] Explored commit ancestry and parent relationships.
- [x] Investigated commit-to-tree snapshot relationships.
- [x] Examined branching and divergent histories.
- [x] Inspected merge commits and multiple parents.
- [x] Practiced commit graph traversal and revision range comparisons.
- [x] Documented practical findings and observations.

**Status:** Practical investigation completed. Documentation prepared for review.
