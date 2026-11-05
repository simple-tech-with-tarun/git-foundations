# Exercise 1: Git Object Model and Content-Addressable Storage

## Objective

Understand how Git stores repository data using a content-addressable object database. Explore the four fundamental Git object types - blobs, trees, commits, and annotated tags - and investigate how these objects are created, identified, stored, and connected.

The exercises focus on inspecting Git's internal objects rather than relying only on high-level Git commands.

## Prerequisites

- Basic familiarity with Git repositories, commits, branches, and tags.
- Understanding of staging and committing changes.
- Familiarity with commands such as `git status`, `git add`, `git commit`, and `git log`.
- A working Git installation.

## Lab Environment

Use an isolated repository for the practical exercises.

Do not perform experimental object creation or manipulation in the primary `git-foundations` repository.

Create a dedicated practice repository:

```powershell
mkdir git-object-model-lab
cd git-object-model-lab
git init
```

Configure a local identity if required:

```powershell
git config user.name "Git Internals Lab"
git config user.email "git-internals@example.com"
```

All exercises should be performed inside this lab repository unless explicitly stated otherwise.

---

## 1. Git Object Fundamentals

### Concepts

Understand Git's content-addressable storage model.

Explore:

- How Git represents repository content as objects.
- The four fundamental object types:
  - Blob
  - Tree
  - Commit
  - Annotated tag
- How Git calculates object identifiers using object content.
- How object identifiers allow Git to locate and verify stored objects.
- Why identical object content produces identical object identifiers.
- The distinction between file content, filenames, and Git objects.

### Practical Tasks

1. Initialize the isolated Git repository.
2. Create two files containing identical content.
3. Calculate their object identifiers using `git hash-object`.
4. Compare the resulting identifiers.
5. Inspect the object type and content using `git cat-file`.
6. Investigate how Git identifies an object independently of its filename.

### Expected Outcome

Explain Git's content-addressable storage model and distinguish object identity from filesystem filenames.

---

## 2. Exploring Blob Objects

### Concepts

A blob object stores file content without storing its filename or directory location.

Explore:

- Blob object creation.
- Object hashing.
- Writing objects into Git's object database.
- Reading stored object content.
- Identical content producing identical blob identifiers.
- The difference between a working-tree file and its corresponding blob object.

### Useful Commands

```bash
git hash-object <file>
git hash-object -w <file>
git cat-file -t <object-id>
git cat-file -s <object-id>
git cat-file -p <object-id>
```

### Practical Tasks

1. Create a sample text file.
2. Calculate its object identifier without writing it to the object database.
3. Store the blob using `git hash-object -w`.
4. Verify that the object exists.
5. Inspect its type, size, and content.
6. Create another file with identical content.
7. Compare both object identifiers.
8. Modify the content and investigate how the identifier changes.

### Expected Outcome

Demonstrate how Git creates and stores blob objects and explain why filenames are not part of blob identity.

---

## 3. Inspecting Tree Objects

### Concepts

Tree objects represent directory structures and connect filenames to blobs or other trees.

Explore:

- How Git represents directories.
- Relationships between tree objects and blob objects.
- Nested directory structures.
- File modes and object types stored in tree entries.
- How Git constructs tree objects from the index.
- The difference between a working directory and a Git tree snapshot.

### Useful Commands

```bash
git add <file>
git write-tree
git ls-tree <tree-id>
git ls-tree -r <tree-id>
git cat-file -p <tree-id>
git cat-file -t <tree-id>
```

### Practical Tasks

1. Create a directory containing multiple files.
2. Add files to the Git index.
3. Inspect staged entries using `git ls-files --stage`.
4. Generate a tree object using `git write-tree`.
5. Inspect the resulting tree using `git ls-tree`.
6. Investigate the relationship between tree entries and their referenced blobs.
7. Create a nested directory structure and inspect its corresponding tree hierarchy.
8. Modify a file and compare the resulting tree identifiers after staging the change.

### Expected Outcome

Explain how tree objects represent directory snapshots and connect filenames, file modes, and object identifiers.

---

## 4. Deconstructing Commit Objects

### Concepts

A commit object records a repository snapshot and the metadata associated with that snapshot.

Explore:

- Commit object structure.
- Root tree reference.
- Parent commit references.
- Author and committer metadata.
- Commit messages.
- Root commits and parent relationships.
- How commit objects reference tree objects rather than storing file contents directly.
- Why identical snapshots can have different commit identifiers.

### Useful Commands

```bash
git commit
git cat-file -p <commit-id>
git cat-file -t <commit-id>
git show --no-patch --format=raw <commit-id>
git rev-parse HEAD^{tree}
git rev-parse HEAD^
```

### Practical Tasks

1. Create and commit a sample repository snapshot.
2. Identify the resulting commit object.
3. Inspect the raw commit contents using `git cat-file -p`.
4. Identify its tree reference.
5. Investigate author, committer, timestamps, and commit message.
6. Identify the parent relationship.
7. Create another commit and compare the two commit objects.
8. Investigate how a root commit differs from a commit with a parent.
9. Trace the commit's tree reference to its underlying tree and blob objects.

### Expected Outcome

Reconstruct the internal structure of a commit object and explain how commits connect repository snapshots through tree and parent references.

---

## 5. Investigating Annotated Tag Objects

### Concepts

Git supports lightweight and annotated tags, but they are represented differently.

Explore:

- Lightweight tags as references.
- Annotated tags as Git objects.
- Tag object structure.
- Target object identifiers and target object types.
- Tagger metadata and tag messages.
- The distinction between a tag reference and an annotated tag object.
- Tags pointing to commits and the object relationships involved.

### Useful Commands

```bash
git tag <tag-name>
git tag -a <tag-name> -m "<message>"
git show-ref --tags
git cat-file -t <tag-name>
git cat-file -p <tag-name>
git rev-parse <tag-name>
git rev-parse <tag-name>^{}
```

### Practical Tasks

1. Create a lightweight tag pointing to a commit.
2. Inspect the tag reference.
3. Create an annotated tag pointing to a commit.
4. Inspect its object type and raw contents.
5. Identify the target object, target type, tagger, and message.
6. Compare lightweight and annotated tags.
7. Resolve the annotated tag to its underlying commit.
8. Investigate the difference between the tag object identifier and the commit identifier.

### Expected Outcome

Explain the structural difference between lightweight and annotated tags and identify how annotated tag objects reference their target objects.

---

## 6. End-to-End Object Relationship Investigation

### Objective

Combine the concepts from the previous exercises to reconstruct how Git represents a committed repository snapshot.

### Practical Tasks

1. Create a repository containing multiple files and nested directories.
2. Stage and commit the repository contents.
3. Create an annotated tag for the commit.
4. Identify the commit object.
5. Inspect the commit's tree reference.
6. Traverse the tree hierarchy.
7. Identify the blob objects referenced by the trees.
8. Inspect the annotated tag object and identify its target.
9. Build a complete relationship map connecting the tag, commit, trees, and blobs.
10. Record the relevant object identifiers and supporting command output.

### Expected Outcome

Demonstrate the complete relationship:

```text
Annotated Tag
     |
     v
   Commit
     |
     v
   Tree
     |
     +------> Blob
     |
     +------> Blob
     |
     +------> Subtree
                  |
                  +------> Blob
                  |
                  +------> Blob
```

Explain how Git uses these objects to represent a repository snapshot.

---

## Key Learning Outcomes

After completing this exercise, you should be able to:

- Explain Git's content-addressable object storage.
- Identify and distinguish blob, tree, commit, and annotated tag objects.
- Calculate and inspect object identifiers.
- Create and inspect blob objects.
- Reconstruct directory snapshots from tree objects.
- Deconstruct commit objects and identify their metadata and relationships.
- Distinguish lightweight tags from annotated tags.
- Trace object relationships across a complete repository snapshot.
- Support findings with reproducible commands and recorded evidence.

## Validation Criteria

The exercise has been completed successfully.

- [x] All four fundamental Git object types investigated.
- [x] Blob objects created, stored, and inspected.
- [x] Identical content demonstrated to produce identical object identifiers.
- [x] Tree objects generated and inspected.
- [x] Tree entries traced to their referenced objects.
- [x] Commit objects deconstructed successfully.
- [x] Root and parent commit relationships investigated.
- [x] Lightweight and annotated tags compared.
- [x] End-to-end object relationships investigated.
- [x] Reachable and unreachable objects identified.
- [x] Findings and command output documented.

## Evidence and Documentation

Evidence collected during the practical work includes:

- Commands executed and their relevant output.
- Object identifiers for investigated objects.
- Raw blob, tree, commit, and annotated tag contents.
- Comparisons demonstrating content-addressable behaviour.
- Object relationship diagrams.
- Short explanations of findings and observations.

## Lab Results and Observations

The practical investigation was performed in the isolated `git-object-model-lab` repository.

### Blob Objects

Identical initial file contents produced the same object identifier:

`9b81633ce0bcb3504c1a0c9a1c3f044091641b5d`

After changing the content of `file-two.txt`, its object identifier changed:

`eb25117462ac76263e79e746cfb7fda0e404cc6d`

The final version of `file-two.txt` produced:

`104fe5337abe4b5aceaa2c45c63025ae7b368e28`

### Tree Objects

The initial tree object:

`a67f58c376567e4ed451a88eec80c2b39a3e8643`

The updated tree object:

`ccf2bb855fe14b7a7390bfec063cc56859219eb3`

Changing one file resulted in a new blob and tree, while the unchanged file retained its original blob identifier.

The original tree continued referencing the previous blob, demonstrating Git object immutability.

### Commit Objects

Initial root commit:

`8ec8a36f93f17c5416dee056a5b6ddb7dc00d7ea`

Second commit:

`cfa6cedb420b8359c3ff19ffb9bd5489c6ba22f0`

Both commits referenced the same tree:

`ccf2bb855fe14b7a7390bfec063cc56859219eb3`

The second commit referenced the initial commit as its parent. This demonstrated that different commits can represent the same snapshot while having different commit identifiers.

### Tag Objects

- `v1.0`: Lightweight tag pointing directly to the second commit.
- `v1.1`: Annotated tag represented by a separate Git object.

Annotated tag object:

`e61334576df47d0a81f6e085a2b268e4f144de14`

### Object Reachability

The complete object database contained eight objects.

Six objects were reachable through the current references. Two objects were no longer reachable:

| Object ID | Type | Description |
|---|---|---|
| `a67f58c376567e4ed451a88eec80c2b39a3e8643` | Tree | Original tree |
| `eb25117462ac76263e79e746cfb7fda0e404cc6d` | Blob | Previous content of file-two.txt |

These objects remained in the object database despite no longer being reachable through current references.

No pruning or garbage collection was performed.

### Overall Findings

The investigation demonstrated:

- Git identifies objects through content-addressable storage.
- Trees connect filenames and directory structures to blobs and subtrees.
- Commits reference snapshots and parent commits.
- Annotated tags are independent Git objects.
- Object databases can contain unreachable objects that remain available until maintenance removes them.

## Scope Boundaries

This exercise focuses specifically on the Git object model and content-addressable storage.

The following topics are reserved for subsequent exercises:

- References, branch pointers, and HEAD mechanics - Exercise 2.
- Physical repository structure, index internals, and packfiles - Exercise 3.
- Detailed commit graph traversal and history reconstruction - Exercise 4.
- Object reachability, reflog retention, garbage collection, and pruning - Exercise 5.

## Completion Criteria

**Status: Completed**

All six practical sections have been performed in the isolated lab repository. The validation criteria have been satisfied, and the findings have been documented with actual object identifiers and experimental observations.

The exercise demonstrated how Git represents repository content through interconnected blob, tree, commit, and annotated tag objects.
