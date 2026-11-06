# Exercise 3: Repository Internals

## Overview

Explore Git's internal repository structure and understand how Git manages its index, object database, references, configuration, and physical object storage.

This exercise focuses on how Git represents and stores repository data internally, including the distinction between loose objects and packed objects, the role of the staging index, and the differences between bare and non-bare repositories.

## Learning Objectives

By completing this exercise, you will:

- Understand the internal directory structure of a Git repository.
- Identify the purpose of important files and directories inside `.git`.
- Investigate how Git's staging index stores file information.
- Understand the relationship between the working tree, index, and committed snapshots.
- Explore loose object storage and Git's object directory fan-out structure.
- Inspect packfiles, pack indexes, reverse indexes, and multi-pack indexes.
- Understand packed references.
- Compare bare and non-bare repositories.
- Observe how a bare repository receives objects through a push.

## Topics Covered

### 1. Git Repository Structure

- Internal structure of `.git`.
- Repository configuration through `.git/config`.
- HEAD and reference storage.
- Object database under `.git/objects`.
- Reflog storage under `.git/logs`.
- Hooks and repository-specific information.
- Difference between Git metadata and working-tree files.

### 2. The Git Index and Staging Area

- Purpose of the Git index.
- Index entries and file modes.
- Inspecting the index using `git ls-files --stage`.
- Relationship between the working tree, index, and HEAD.
- Understanding staged and unstaged modifications.
- How staging an updated file changes its index entry.

### 3. Loose Object Storage

- Physical storage of Git objects.
- Two-character fan-out directory structure.
- Relationship between object IDs and filesystem paths.
- Inspecting object storage using `git count-objects`.
- Understanding loose-object storage and object types.

### 4. Packfiles and Packed References

- Purpose of Git packfiles.
- Packfile (`.pack`) and index (`.idx`) files.
- Reverse index (`.rev`) files.
- Multi-pack index.
- Delta compression and delta chain depth.
- Inspecting packfiles using `git verify-pack`.
- Understanding packed references in `packed-refs`.

### 5. Bare and Non-Bare Repositories

- Structure of a normal Git repository.
- Structure of a bare Git repository.
- Understanding the `bare` configuration.
- How a bare repository receives commits through `git push`.
- Object storage inside a bare repository.
- Default branch configuration through symbolic HEAD.

## Practical Exercises

### Exercise 1: Explore the Git Directory

Investigate the internal structure of a Git repository.

Explore:

- `.git` directory structure.
- Repository configuration.
- HEAD and reference files.
- Object storage directories.
- Reflogs, hooks, and repository information.

### Exercise 2: Investigate the Git Index

Explore how Git maintains the staging index.

Investigate:

- Index entries using `git ls-files --stage`.
- Blob objects referenced by index entries.
- Differences between staged and unstaged changes.
- How staging an updated file changes its index entry.

### Exercise 3: Explore Loose Object Storage

Investigate how Git stores loose objects on disk.

Use:

- `git count-objects -v`
- `Get-ChildItem .git/objects`
- `git cat-file`

Observe the fan-out directory structure and understand how object IDs map to physical storage paths.

### Exercise 4: Investigate Packfiles and Packed References

Explore how Git stores objects in packfiles and references in packed-refs.

Use:

- `git verify-pack -v`
- `Get-ChildItem .git/objects/pack`
- `Get-Content .git/packed-refs`

Investigate delta compression, pack indexes, reverse indexes, and multi-pack indexes.

### Exercise 5: Bare Repository Investigation

Create a separate bare repository and a client repository to investigate how Git repositories communicate.

Explore:

- Initializing a bare repository using `git init --bare`.
- Inspecting its directory structure and configuration.
- Creating a normal client repository.
- Adding the bare repository as a remote.
- Pushing a branch to the bare repository.
- Inspecting the resulting references and stored objects.
- Understanding why pushing a branch does not automatically update the bare repository's symbolic HEAD.

## Lab Results and Observations

### 1. Index Investigation

A scratch file named `index-lab.py` was used to investigate the staging index.

Initial staged blob:

`7bd71a5402530925dbfbacdcdbd567d313414cbc`

After modifying and staging the file again, the index referenced:

`2bfe6513e92707cb49e1dcfdf4787ac9f46ed593`

The investigation demonstrated:

- The index stores an object ID for each staged file.
- Modifying a file in the working tree does not automatically modify its index entry.
- Staging the modification updates the index entry to reference the new blob.
- The previous blob remains in the object database even after the index entry changes.

### 2. Object Storage Investigation

The primary `git-foundations` repository reported the following through `git count-objects -v`:

| Field | Value |
|---|---:|
| Loose objects | 417 |
| Loose object size | 180 KiB |
| Packed objects | 327 |
| Packfiles | 2 |
| Pack size | 86 KiB |
| Prune-packable | 0 |
| Garbage | 0 |

The object directory contained the expected two-character fan-out directories.

### 3. Packfile Investigation

The packfile investigation used:

`git verify-pack -v`

The inspected packfile contained:

| Object category | Count |
|---|---:|
| Non-delta objects | 219 |
| Delta chain length 1 | 79 |
| Delta chain length 2 | 19 |
| Delta chain length 3 | 5 |
| Delta chain length 4 | 1 |
| Delta chain length 5 | 1 |
| **Total** | **324** |

The pack verification completed successfully with `pack: ok`.

The primary repository contained 327 packed objects across two packfiles. The inspected pack accounted for 324 objects, with the remaining three in the second packfile.

### 4. Packed References

The `.git/packed-refs` file contained packed local and remote-tracking references.

The header identified the following properties:

- `peeled`
- `fully-peeled`
- `sorted`

This demonstrated that Git can store references in a consolidated file instead of maintaining a separate loose reference file for every branch or tag.

### 5. Bare Repository Investigation

A separate bare repository was created at:

`git-bare-repository-lab`

A separate client repository was created at:

`git-bare-repository-client`

The experiment was deliberately isolated from the primary `git-foundations` repository.

#### Bare Repository Initialization

The bare repository was initialized using:

`git init --bare`

Its root contained:

- `HEAD`
- `config`
- `description`
- `hooks`
- `info`
- `objects`
- `refs`

Unlike a normal repository, it did not contain a `.git` subdirectory or a checked-out working tree.

The following commands confirmed its bare-repository status:

- `git rev-parse --is-bare-repository` returned `true`.
- `git rev-parse --is-inside-work-tree` returned `false`.
- `git rev-parse --git-dir` returned `.`.

Its configuration included:

```ini
[core]
    repositoryformatversion = 0
    filemode = false
    bare = true
    symlinks = false
    ignorecase = true
```

Initially, its HEAD pointed to:

`refs/heads/master`

No branch references or Git objects existed immediately after initialization.

#### Pushing from the Client Repository

A normal client repository was initialized, and a `README.md` file was committed.

The initial commit was:

`14a5d2afc9a36afdd20b586a0878f3122b2d13cc`

The client repository was configured with the bare repository as its `origin` remote.

The branch was renamed to `main` and pushed:

`git push -u origin main`

The push successfully created `refs/heads/main` in the bare repository.

The branch reference contained:

`14a5d2afc9a36afdd20b586a0878f3122b2d13cc`

#### Inspecting the Bare Repository's Objects

The pushed commit referenced the following object hierarchy:

| Object type | Object ID |
|---|---|
| Commit | `14a5d2afc9a36afdd20b586a0878f3122b2d13cc` |
| Tree | `f5808582b4adbbfc17769a5515f23eee0254081a` |
| Blob | `cfb570bacb33a2f6f1e653159120e6ab914c7e89` |

The three objects were stored as loose objects using Git's two-character fan-out structure.

| Object | Directory | Remaining filename | Physical size |
|---|---|---|---:|
| Commit | `objects/14/` | `a5d2afc9a36afdd20b586a0878f3122b2d13cc` | 137 bytes |
| Tree | `objects/f5/` | `808582b4adbbfc17769a5515f23eee0254081a` | 54 bytes |
| Blob | `objects/cf/` | `b570bacb33a2f6f1e653159120e6ab914c7e89` | 45 bytes |

The physical sizes represent compressed on-disk object files.

#### Object Storage Accounting

After the push, `git count-objects -v` reported:

| Field | Value |
|---|---:|
| count | 3 |
| size | 0 |
| in-pack | 0 |
| packs | 0 |
| size-pack | 0 |
| prune-packable | 0 |
| garbage | 0 |
| size-garbage | 0 |

This confirmed that the bare repository contained three loose objects and no packfiles.

#### Bare Repository HEAD Configuration

An important observation was made after pushing `main`.

The push created the `main` branch but did not automatically change the bare repository's symbolic HEAD. HEAD continued to point to `refs/heads/master`, even though that branch did not exist.

The default branch was corrected using:

`git symbolic-ref HEAD refs/heads/main`

Verification with `git symbolic-ref HEAD` returned:

`refs/heads/main`

This demonstrated that the branch reference and the repository's default symbolic HEAD are separate pieces of repository metadata.

### 6. Reflog Storage Investigation

The physical reflog structure was investigated inside the primary `git-foundations` repository.

The `.git/logs` directory contained the following reflog locations:

| Path | Purpose |
|---|---|
| `.git/logs/HEAD` | Records HEAD movements, including checkouts and commits. |
| `.git/logs/refs/heads/` | Contains individual reflogs for local branches. |
| `.git/logs/refs/remotes/` | Contains reflogs for remote-tracking references. |
| `.git/logs/refs/stash` | Records changes to the stash reference. |

#### Inspecting Reflog Entries

The reflog files were inspected using PowerShell's `Get-Content` command.

For example:

`Get-Content .git/logs/HEAD -Tail 5`

Each reflog entry contains the following fields:

1. Previous object ID.
2. New object ID.
3. Committer identity.
4. Unix timestamp.
5. Timezone offset.
6. Operation description.

A typical entry records information such as a checkout, commit, pull, or fetch operation.

#### Observations

- HEAD and individual branch references have separate reflog files.
- Switching branches can update the HEAD reflog without moving the underlying branch reference.
- The local branch reflog records movements of that specific branch.
- The remote-tracking reflog records updates received through fetch operations.
- The stash reflog is maintained separately in `.git/logs/refs/stash`.
- Reflogs are organized on disk according to the references they track.

This investigation demonstrated how Git physically stores reflog history inside the repository's metadata directory.

## Key Takeaways

1. The `.git` directory contains the internal metadata and object database of a normal Git repository.
2. The index is Git's staging representation and stores object references independently of the working tree.
3. Git stores loose objects using a two-character fan-out directory structure.
4. Packfiles provide compressed storage for Git objects, including delta-compressed representations.
5. References can be stored individually or consolidated into `packed-refs`.
6. A bare repository stores Git data directly at its root and has no working tree.
7. Pushing to a bare repository transfers objects and updates branch references.
8. A bare repository's symbolic HEAD must identify its intended default branch independently of the branches received through pushes.
9. Reflogs are not stored in a single centralized file. Git maintains separate reflog files for HEAD and individual references under `.git/logs`.

## Useful Commands

| Command | Purpose |
|---|---|
| `git rev-parse --git-dir` | Locate the Git metadata directory |
| `git rev-parse --is-bare-repository` | Check whether a repository is bare |
| `git ls-files --stage` | Inspect index entries |
| `git count-objects -v` | Inspect loose and packed object statistics |
| `git cat-file -t <object>` | Identify an object type |
| `git cat-file -p <object>` | Inspect object contents |
| `git verify-pack -v <index-file>` | Inspect packfile contents |
| `git symbolic-ref HEAD` | Inspect the symbolic HEAD |
| `git symbolic-ref HEAD refs/heads/main` | Set the bare repository's default branch |
| `git push -u origin main` | Push a branch and configure upstream tracking |
| `Get-Content .git/logs/HEAD -Tail 5` | Inspect recent HEAD reflog entries |

## Completion Status

- [x] Investigated Git repository structure.
- [x] Explored the staging index.
- [x] Examined loose object storage.
- [x] Inspected packfiles and packed references.
- [x] Created and investigated a separate bare repository.
- [x] Documented actual experimental results and observations.

**Status:** Practical investigation completed. Documentation prepared for review.
