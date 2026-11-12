# Git Internals

This section explores how Git stores, organizes, and manages repository data internally. It focuses on Git's object model, references, repository structure, commit graphs, and object lifecycle.

Understanding Git internals helps explain how commits, branches, tags, and file snapshots are represented and connected. It also provides the foundation for investigating repository state, recovering objects, and diagnosing unusual Git behaviour.

## Topics Covered

- Git's content-addressable storage and four fundamental object types
- Blob, tree, commit, and annotated tag objects
- Git references, symbolic references, and HEAD
- Detached HEAD and reference movement
- Repository structure, index, loose objects, and packfiles
- Commit ancestry, snapshots, and commit graph traversal
- Object reachability, reflog, garbage collection, and pruning
- Repository maintenance and object recovery

## Practical Exercises

The exercises use controlled Git repositories to investigate Git's internal architecture through practical commands, object inspection, and evidence-based analysis.

### 1. Git Object Model

<badge color="success">Completed</badge>

[Exercise 1: Git Object Model](./exercises/01-git-object-model/README.md)

Explore Git's content-addressable storage and inspect blob, tree, commit, and annotated tag objects.

**Key commands:**
- `git hash-object`
- `git cat-file`
- `git write-tree`
- `git ls-tree`
- `git mktag`

### 2. References and HEAD

<badge color="success">Completed</badge>

[Exercise 2: References and HEAD](./exercises/02-reference-and-head/README.md)

Investigate how Git references identify commits, how HEAD tracks the current position, and what happens during detached HEAD operations.

**Key commands:**
- `git show-ref`
- `git rev-parse`
- `git symbolic-ref`
- `git reflog`
- `git update-ref`

### 3. Repository Internals

<badge color="success">Completed</badge>

[Exercise 3: Repository Internals](./exercises/03-repository-internals/README.md)

Examine the physical repository structure, staging index, object storage, packfiles, and repository configuration.

**Key commands:**
- `git ls-files --stage`
- `git count-objects -v`
- `git cat-file`
- `git verify-pack -v`
- `git symbolic-ref`

### 4. Commit Graphs and Object Relationships

<badge color="success">Completed</badge>

[Exercise 4: Commit Graphs and Object Relationships](./exercises/04-commit-graphs/README.md)

Explore commit ancestry, parent relationships, snapshots, branching, merging, and graph traversal.

**Key commands:**
- `git log --graph`
- `git rev-list --parents`
- `git merge-base`
- `git rev-list --left-right --count`
- `git diff`

### 5. Object Lifecycle and Maintenance

<badge color="success">Completed</badge>

[Exercise 5: Object Lifecycle and Maintenance](./exercises/05-object-lifecycle/README.md)

Investigate object reachability, reflog retention, dangling objects, garbage collection, pruning, and repository maintenance.

**Key commands:**
- `git fsck`
- `git reflog`
- `git gc`
- `git prune`
- `git maintenance`

## Key Takeaways

- Git stores repository content using content-addressable objects.
- Blobs, trees, commits, and annotated tags serve different purposes.
- Branches and tags are references to Git objects.
- HEAD identifies the current repository position.
- The index and working tree are distinct from committed snapshots.
- Commits form a directed acyclic graph through parent relationships.
- Object reachability determines whether objects are retained or eligible for cleanup.
- Reflogs can help recover references and commits after certain operations.
- Git maintenance manages repository storage and object efficiency.
- Inspecting Git internals provides a deeper understanding of everyday Git operations.

## Useful Commands

| Command | Purpose |
|---|---|
| `git cat-file -t <object>` | Identify an object type |
| `git cat-file -p <object>` | Inspect an object's contents |
| `git hash-object <file>` | Calculate an object hash |
| `git ls-tree <tree>` | List tree contents |
| `git show-ref` | Display references |
| `git rev-parse HEAD` | Resolve HEAD to an object ID |
| `git ls-files --stage` | Inspect index entries |
| `git count-objects -v` | Inspect object storage statistics |
| `git log --oneline --graph --all` | Visualize commit history |
| `git fsck --full` | Check repository object integrity |

## Important Notes

- Perform destructive object lifecycle experiments in isolated or disposable repositories.
- Do not run pruning experiments against the primary learning repository.
- Inspect repository state and object reachability before attempting recovery or cleanup.
- Record command output and findings as evidence for each exercise.
