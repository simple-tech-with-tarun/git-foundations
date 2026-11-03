
# Debugging and Investigation

This chapter focuses on advanced Git techniques for investigating repository history, tracing code changes, identifying regressions, and reconstructing historical repository states.

The emphasis is on understanding how changes evolved, identifying where and when problems were introduced, and gathering reliable evidence to support an investigation.

## Learning Objectives

By completing this chapter, you will be able to:

- Investigate complex commit histories and understand commit ancestry.
- Trace code changes across commits, files, and contributors.
- Identify regression-introducing commits using manual and automated Git bisect workflows.
- Investigate historical files, Git objects, references, and unreachable commits.
- Understand Git object storage, packfiles, delta compression, and garbage collection.
- Investigate dangling objects and recover historical repository data.
- Combine Git investigation techniques into structured debugging workflows.
- Document investigation findings with reproducible commands and supporting evidence.

## Learning Roadmap

The chapter is divided into five practical learning phases.

### 1. Advanced Git History Investigation

**Status:** Completed — Practical work documented

Investigate complex repository histories and understand how commits, branches, and merges relate to each other.

Topics:

- Advanced `git log` filtering and formatting.
- Commit ancestry and revision ranges.
- Branch divergence and merge history.
- Feature and hotfix branch investigation.
- Historical comparisons using `git diff`.
- Comparing changes across different development paths.

Practical exercises documented:

- Repository history investigation.
- Advanced history investigation.
- Feature and hotfix branch analysis.
- Merge history investigation.
- Historical change comparison.

**Supporting repository:** [Git Debugging Lab](https://github.com/simple-tech-with-tarun/git-debugging-lab)

The repository contains dedicated history investigation exercises and deliberately constructed Git histories for examining branch relationships, merges, and historical changes.

### 2. Tracing Code Changes and Contributions

**Status:** Completed — Practical work documented

Investigate when code was introduced, how it evolved, and how changes moved between files and contributors.

Topics:

- Line-level attribution using `git blame`.
- Code movement and copy detection using `-M` and `-C`.
- Whitespace-insensitive attribution using `-w`.
- Pickaxe searches using `git log -S` and `git log -G`.
- Rename tracking using `git log --follow`.
- Historical file retrieval using `git show`.
- Contribution investigation using `git shortlog` and `git log --author`.
- Author and committer investigation.

Practical exercises documented:

- Line-level code attribution.
- Moved and copied code analysis.
- Whitespace change investigation.
- Exact-string and regular-expression searches.
- File rename and historical attribution.
- Contribution history analysis.

**Supporting repository:** [Git Debugging Lab](https://github.com/simple-tech-with-tarun/git-debugging-lab)

Exercise documentation: [Code Attribution and Historical Investigation](https://github.com/simple-tech-with-tarun/git-debugging-lab/tree/main/code-attribution-investigation)

The exercise demonstrates how to trace code origins, investigate historical modifications, follow renamed files, and understand contribution history.

### 3. Advanced Git Bisect and Regression Detection

**Status:** Planned

Identify regression-introducing commits using Git's binary-search capabilities and automated testing.

Topics:

- Manual Git bisect workflows.
- Skipping untestable commits.
- Automated regression detection using `git bisect run`.
- Exit codes and test-script behaviour.
- Merge-related regression investigation.
- Bisect recovery and reproducibility.

Planned exercises:

- Manual regression investigation.
- Skipped and untestable commits.
- Automated bisect.
- Merge-related regression.
- Bisect recovery and reproducibility.

**Supporting repository:** Practical exercises to be developed.

### 4. Repository Forensics and Historical Reconstruction

**Status:** Partially supported by completed sibling repositories — Issue verification pending

Investigate historical repository states, Git objects, references, and commits that are no longer reachable through ordinary branch history.

Topics:

- Historical file and commit inspection.
- Git blobs, trees, commits, and tags.
- Loose and packed Git objects.
- Packfile creation and inspection.
- Delta compression and delta chains.
- References, `HEAD`, and reflogs.
- Dangling and unreachable objects.
- Cruft pack creation and expiration.
- Commit and patch investigation using `git patch-id`.

Practical exercises documented across sibling repositories:

- Dangling tree recovery.
- Git object inspection and reconstruction.
- Loose object and packed object comparison.
- Packfile inspection and verification.
- Delta compression analysis.
- Garbage collection and repacking.
- Reflog expiration.
- Unreachable object investigation.
- Cruft pack creation and inspection.
- Unreachable object expiration and removal.

**Supporting repositories:**

1. [Git Debugging Lab](https://github.com/simple-tech-with-tarun/git-debugging-lab)
2. [Git Packfile Lab](https://github.com/simple-tech-with-tarun/git-packfile-lab)
3. [Git Cruft Pack Lab](https://github.com/simple-tech-with-tarun/git-cruft-pack-lab)

These repositories provide practical examples of Git object storage, repository maintenance, unreachable object recovery, and historical reconstruction.

The proposed commands and exercises for this phase must still be checked against the original sub-issue before marking it complete.

### 5. Integrated Git Debugging and Investigation Workflows

**Status:** Planned

Combine the techniques from the previous phases to investigate realistic repository problems.

Topics:

- End-to-end regression investigation.
- Multi-branch and merge-related defects.
- Code evolution and contribution tracing.
- Historical reconstruction and repository recovery.
- Evidence-based investigation reporting.
- Combining Git history and object-level investigation techniques.

Planned exercises:

- Production regression investigation.
- Merge-introduced defect investigation.
- Historical code reconstruction.
- Advanced repository investigation.
- End-to-end investigation report.

**Supporting repository:** To be determined based on the integrated exercise requirements.

## Related Practical Repositories

This chapter is supported by three dedicated Git learning repositories. Each repository focuses on a different aspect of Git history investigation, object storage, repository maintenance, and recovery.

### 1. Git Debugging Lab

Repository: [simple-tech-with-tarun/git-debugging-lab](https://github.com/simple-tech-with-tarun/git-debugging-lab)

Purpose:

A hands-on repository for learning advanced Git history investigation, recovery, debugging, code attribution, and repository forensics.

Key learning areas:

- Commit history and branch investigation.
- Feature and hotfix branch workflows.
- Merge history and branch divergence.
- Code attribution and historical change tracking.
- Moved, copied, and renamed file investigation.
- Exact-string and regular-expression history searches.
- Git trees, blobs, commits, and unreachable objects.
- Dangling tree recovery and evidence preservation.

Important commands documented in the repository:

```bash
git log --graph --oneline --all
git show <commit>
git diff <branch1> <branch2>

git blame
git log -S
git log -G
git log --follow

git fsck --full --unreachable
git cat-file -p <object>
git ls-tree -r <tree>
git hash-object <file>
```

### 2. Git Packfile Lab

Repository: [simple-tech-with-tarun/git-packfile-lab](https://github.com/simple-tech-with-tarun/git-packfile-lab)

Purpose:

A practical laboratory exploring Git object storage, packfiles, delta compression, garbage collection, and repository maintenance.

Key learning areas:

- Git object types: blobs, trees, commits, and tags.
- Loose objects versus packed objects.
- Packfile creation and management.
- Delta compression and delta chains.
- Packfile integrity verification.
- Garbage collection and repacking.
- Reflog expiration and unreachable object pruning.

Important commands documented in the repository:

```bash
git count-objects -v

git cat-file -t <object-id>
git cat-file -s <object-id>
git cat-file -p <object-id>

git gc
git repack -ad
git repack -adf

git verify-pack -v <pack-index-file>
git fsck --full
```

The experiments demonstrate how Git stores objects efficiently and how repository maintenance operations reorganize the object database.

### 3. Git Cruft Pack Lab

Repository: [simple-tech-with-tarun/git-cruft-pack-lab](https://github.com/simple-tech-with-tarun/git-cruft-pack-lab)

Purpose:

A practical laboratory demonstrating how Git handles unreachable objects through cruft packs, retention periods, expiration, and eventual removal.

Key learning areas:

- Reachable and unreachable Git objects.
- Branch deletion and reflog expiration.
- Unreachable object identification.
- Cruft pack creation.
- Packfile component inspection.
- Object retention and expiration.
- Repacking and object pruning.

Important commands documented in the repository:

```powershell
git switch -c feature/application-metadata

git branch -D feature/application-metadata

git reflog expire --all --expire=now
git reflog --all --oneline

git fsck --full --unreachable

git gc --cruft --no-prune

Get-ChildItem .git\objects\pack

git verify-pack -v .git/objects/pack/pack-<hash>.idx

git cat-file -t <object-id>

git repack -d --cruft --cruft-expiration="2.weeks.ago"
git repack -d --cruft --cruft-expiration=now
```

The experiments demonstrate that deleting a branch does not immediately delete its commits and that unreachable objects can remain recoverable while retained in cruft packs.

## Relationship to the Learning Roadmap

| Learning Phase | Supporting Repository | Status |
|---|---|---|
| Advanced Git History Investigation | Git Debugging Lab | Completed — verification pending |
| Tracing Code Changes and Contributions | Git Debugging Lab | Completed — verification pending |
| Advanced Git Bisect and Regression Detection | To be developed | Planned |
| Repository Forensics and Historical Reconstruction | Git Debugging Lab, Git Packfile Lab, Git Cruft Pack Lab | Partially supported |
| Integrated Git Debugging and Investigation Workflows | To be determined | Planned |

## Working Approach

Each phase follows a practical, investigation-oriented workflow.

1. Establish the scenario and expected outcome.
2. Prepare the required repository history or test conditions.
3. Execute investigation commands and inspect the results.
4. Validate findings against commit history and repository state.
5. Document useful commands, observations, and conclusions.
6. Commit meaningful changes throughout the work.

Exercises will use controlled scenarios wherever possible so that the results are reproducible and safe to investigate.

## Documentation Structure

The chapter README serves as the central learning reference.

As each phase progresses, its documentation will be expanded with:

- Exercise objectives and scenarios.
- Commands and their purpose.
- Relevant command output and observations.
- Investigation findings.
- Supporting repository and PR references.
- Validation and conclusions.

Only completed exercises and verified findings will be marked as completed.

## Progress Tracking

| Phase | Topic | Status |
|---|---|---|
| 1 | Advanced Git History Investigation | Completed — verification pending |
| 2 | Tracing Code Changes and Contributions | Completed — verification pending |
| 3 | Advanced Git Bisect and Regression Detection | Planned |
| 4 | Repository Forensics and Historical Reconstruction | Partially supported — verification pending |
| 5 | Integrated Git Debugging and Investigation Workflows | Planned |

## Completion Criteria

The chapter will be considered complete when:

- All five learning phases have been completed.
- Each planned exercise has been performed and validated.
- Proposed commands have been practised and verified.
- Relevant commands and findings are documented.
- Supporting repositories and merged PRs are referenced.
- Integrated investigation workflows have been demonstrated.
- The documentation accurately reflects the completed work.
