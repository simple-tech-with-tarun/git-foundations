# Exercise 5: Object Lifecycle and Maintenance

## Overview

This exercise explores how Git manages the lifecycle of repository objects, from creation and reachability to reflog retention, recovery, garbage collection, and pruning.

All destructive experiments were performed in an isolated local repository to protect the primary learning repository.

## Objectives

- Understand reachable and unreachable Git objects.
- Investigate how references and reflogs affect object retention.
- Explore reflog expiration and commit recovery.
- Examine garbage collection, pruning, and cruft packs.
- Understand loose-object consolidation and packfile maintenance.
- Use Git maintenance and integrity-checking commands.
- Trace the complete lifecycle of commits, trees, and blobs.
- Validate object recovery and repository integrity.

## Lab Environment

All practical experiments were conducted in a separate local repository:

- **Repository:** `git-object-lifecycle-lab`
- **Location:** `C:\Users\ertar\Documents\GitHub\git-object-lifecycle-lab`
- **Remote:** None (local repository)
- **Primary branch:** `master`

The isolated repository ensured that reflog expiration, garbage collection, and pruning experiments could be performed without affecting the primary learning repository.

### Initial Repository History

The initial repository contained two commits on `master`:

| Commit | Description |
|---|---|
| `13920e0` | Add initial application |
| `0c01f97` | Update application |

A separate recovered branch, `lab/recovered`, contained the experimental commit `d5424fd`.

These existing commits were preserved throughout the subsequent experiments.

## Exercise 1: Investigating Object Reachability

### Objective

Understand how Git determines object reachability and how deleting a branch affects the accessibility and retention of commits, trees, and blobs.

### Procedure

1. Created an initial application commit (`13920e0`).
2. Updated the application and created a second commit (`0c01f97`).
3. Created a temporary branch named `lab/unreachable`.
4. Modified `app.txt` and committed the experimental version.
5. Switched back to `master` and deleted `lab/unreachable`.
6. Compared reachable objects using `git rev-list --objects --all`.
7. Investigated unreachable objects using `git fsck --no-reflogs --unreachable`.
8. Inspected reflog entries and recovered the experimental commit.

### Experimental Commit

| Object | SHA-1 |
|---|---|
| Commit | `d5424fd59b39d95232db987d175164bb765eaf3d` |
| Tree | `09bfee76e638327e7f009d10dc4befe7d1867e71` |
| Blob | `1e256e4b39e2a407f023833d33f867508e4205ef` |

### Observations

- A branch reference makes its commit and reachable history accessible.
- Deleting a branch removes that reference but does not immediately delete its objects.
- The deleted branch's commit, tree, and blob became unreachable from normal references.
- The HEAD reflog retained the deleted commit, allowing it to be inspected and recovered.
- `git fsck --no-reflogs --unreachable` exposed objects that were otherwise retained through reflogs.
- Creating `lab/recovered` restored reachability without creating a new commit.

### Key Takeaway

Object reachability is determined by references and their reachable object graphs. Deleting a branch does not immediately destroy its objects because reflogs can retain references to previous commit positions.

## Exercise 2: Exploring Reflog and Object Retention

### Objective

Investigate how reflogs retain references to previous commits, how reflog expiration affects object reachability, and how garbage collection handles unreachable objects.

### Procedure

1. Created a temporary branch named `lab/reflog-retention`.
2. Modified `app.txt` to `Version 4: Reflog retention experiment`.
3. Created commit `1c7ffe5`.
4. Switched to `master` and deleted the temporary branch.
5. Inspected HEAD and branch reflog entries.
6. Compared normal `git fsck --unreachable` with `git fsck --no-reflog --unreachable`.
7. Configured repository-local reflog expiration:
   - `gc.reflogExpire = 7.days`
   - `gc.reflogExpireUnreachable = 1.days`
8. Expired unreachable reflog entries using `git reflog expire`.
9. Verified that the commit, tree, and blob remained readable even after reflog expiration.
10. Ran ordinary `git gc` and inspected the resulting regular and cruft packfiles.
11. Ran `git gc --prune=now` to remove the expired unreachable objects.

### Experimental Objects

| Object | SHA-1 |
|---|---|
| Commit | `1c7ffe550e29a0a55040f26137568448af466285` |
| Tree | `2ee22c064e3a56b630bf6b1fffedf11114ff67d4` |
| Blob | `cffc0cb5e57b267ce7c6b6d327fabb82da0a2edb` |

### Observations

- Deleting a branch removed its branch reference and branch reflog.
- The HEAD reflog continued to retain the deleted branch's commit.
- Normal `git fsck --unreachable` did not report objects retained by reflogs.
- Using `--no-reflog` exposed the unreachable commit, tree, and blob.
- Reflog expiration removed the relevant reflog entries but did not immediately delete the Git objects.
- Ordinary `git gc` packed reachable objects into a regular packfile and unreachable objects into a cruft pack.
- The cruft pack contained an `.mtimes` file for tracking object modification times.
- `git gc --prune=now` removed the expired unreachable objects.
- The original recovered history remained intact.

### Storage Comparison

| State | Loose objects | Packed objects | Packfiles |
|---|---:|---:|---:|
| Before GC | 12 | 0 | 0 |
| After ordinary GC | 0 | 12 | 2 |
| After `git gc --prune=now` | 0 | 9 | 1 |

### Key Takeaway

Reflog expiration and object deletion are separate operations. Expiring reflog entries removes retention references, while garbage collection and pruning determine when unreachable objects are physically removed.

## Exercise 3: Investigating Garbage Collection and Pruning

### Objective

Understand the difference between garbage collection and pruning, and investigate how Git removes unreachable loose objects.

### Procedure

1. Created a temporary branch named `lab/prune-experiment`.
2. Modified `app.txt` to `Version 5: Pruning experiment`.
3. Created commit `d867e85`.
4. Switched to `master` and deleted the temporary branch.
5. Expired reflog entries using `git reflog expire --expire=now --expire-unreachable=now --all`.
6. Inspected repository storage using `git count-objects -v`.
7. Identified unreachable objects using `git fsck --no-reflog --unreachable`.
8. Executed `git prune --expire=now`.
9. Verified that the unreachable objects were no longer reported by `git fsck`.
10. Used `git cat-file` to confirm that the experimental commit was no longer accessible.

### Experimental Objects

| Object | SHA-1 |
|---|---|
| Commit | `d867e85c6f9101c283aaf5ec15aaa641e1acdfd4` |
| Tree | `329ae372f050f3281877f971c9cdfb5cf3720af9` |
| Blob | `5ba656e91999d77dafc48aabc37d73868bb0273d` |

### Observations

- The experimental commit initially existed as a loose object.
- Deleting its branch and expiring its reflog entries made the commit, tree, and blob unreachable.
- `git fsck --no-reflog --unreachable` identified all three objects before pruning.
- `git prune --expire=now` removed the unreachable loose objects.
- The repository returned to zero loose objects and nine packed objects.
- `git cat-file -t` could no longer locate the pruned commit.
- The existing reachable history remained intact.

### Storage Comparison

| State | Loose objects | Packed objects | Packfiles |
|---|---:|---:|---:|
| Before experiment | 0 | 9 | 1 |
| After experimental commit | 3 | 9 | 1 |
| After pruning | 0 | 9 | 1 |

### Key Takeaway

`git prune` removes eligible unreachable loose objects, whereas `git gc` performs broader repository maintenance, including object packing and pruning. Packed unreachable objects require separate consideration during maintenance.

## Exercise 4: Exploring Repository Maintenance and Integrity

### Objective

Investigate Git's repository maintenance commands and verify repository integrity, object connectivity, packfile consistency, and commit graph integrity.

### Procedure

1. Executed `git maintenance run` to trigger repository maintenance.
2. Inspected the maintenance configuration using `git config --show-origin --get-regexp "maintenance\."`.
3. Executed `git fsck --full` to perform a comprehensive integrity check.
4. Executed `git fsck --unreachable` to check for unreachable objects.
5. Executed `git fsck --no-reflog --unreachable` to check reachability without reflog references.

### Observations

- `git maintenance run` completed with the message `Nothing new to pack`.
- No explicit maintenance configuration was present in the repository.
- `git fsck --full` completed without reporting integrity errors.
- Git verified object ordering, packfile offsets, multi-pack-index information, and commit graph integrity.
- Both unreachable-object checks completed without reporting unreachable objects.
- The repository contained nine packed objects and no loose objects.

### Key Takeaway

Git maintenance helps optimize repository storage, while `git fsck` validates object integrity and connectivity. These checks provide confidence that repository objects and their relationships remain consistent after maintenance and pruning operations.

## Exercise 5: End-to-End Object Lifecycle Investigation

### Objective

Trace the lifecycle of a Git commit, including object creation, reachability changes, object recovery, and integrity verification.

### Procedure

1. Created a temporary branch named `lab/lifecycle-experiment`.
2. Modified `app.txt` to `Version 6: End-to-end lifecycle experiment`.
3. Created commit `9348242`.
4. Inspected the commit using `git cat-file -p HEAD`.
5. Inspected its tree using `git ls-tree HEAD`.
6. Verified the stored file content using `git show HEAD:app.txt`.
7. Switched to `master` and deleted the experimental branch.
8. Used `git fsck --no-reflog --unreachable` to identify the unreachable commit, tree, and blob.
9. Recovered the original commit by creating `lab/lifecycle-recovered` using its full object ID.
10. Inspected the recovered commit history and file content.
11. Executed `git fsck --no-reflog --unreachable` again to verify restored reachability.

### Experimental Objects

| Object | SHA-1 |
|---|---|
| Commit | `93482424de3ce3c7968307b6667850d646bb9214` |
| Tree | `c59e314639b6b2999dce8c1988d86c59db545571` |
| Blob | `6402f9f94294cb30f846db0dcb65d7d763de2d63` |

### Observations

- Git stored the experimental commit as a commit object referencing a tree and parent commit.
- The tree referenced the blob containing the experimental `app.txt` content.
- Deleting the experimental branch removed its reference to the commit.
- The commit, tree, and blob became unreachable from normal references.
- `git fsck --no-reflog --unreachable` identified all three objects.
- Creating `lab/lifecycle-recovered` restored reachability using the original commit ID.
- Recovery did not create a new commit or modify the original commit history.
- The recovered branch retained the original file snapshot.
- A subsequent integrity check reported no unreachable objects.

### Key Takeaway

Git objects can remain recoverable after their branch references are deleted. As long as the objects have not been pruned, their original commit IDs can be used to restore reachability without rewriting history.
