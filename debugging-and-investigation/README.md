
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

**Status:** Completed - Practical work documented

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

**Status:** Completed - Practical work documented

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

**Status:** Completed - Practical work documented

Identify regression-introducing commits using Git's binary-search capabilities, automated testing, and structured investigation workflows.

Topics:

- Manual Git bisect workflows and good/bad boundaries.
- Skipping untestable commits using `git bisect skip`.
- Bisect investigation history using `git bisect log` and `git bisect visualize`.
- Automated regression detection using `git bisect run`.
- Test-script exit codes and untestable revisions.
- Merge-related regression investigation and commit ancestry.
- Recovery from incorrect bisect classifications.
- Bisect reproducibility and log replay limitations.

Practical exercises documented:

- Manual regression investigation.
- Skipped and untestable commits.
- Automated regression investigation.
- Merge-related regression investigation.
- Bisect recovery and reproducibility.

**Supporting repository:** [Git Bisect Lab](https://github.com/simple-tech-with-tarun/git-bisect-lab)

The repository contains five practical exercises covering manual and automated regression detection, skipped commits, merge-related regressions, and recovery from incorrect bisect decisions. Each exercise includes documented scenarios, commands, observations, and validation evidence.

### 4. Repository Forensics and Historical Reconstruction

**Status:** Completed - Practical work documented

Investigate historical repository states, Git objects, references, and commits that are no longer reachable through ordinary branch history.

Topics:

- Historical file and commit inspection.
- Git blobs, trees, commits, and tags.
- Loose and packed Git objects.
- Packfile creation, inspection, and verification.
- Delta compression and delta chains.
- Direct and symbolic references.
- Attached and detached HEAD states.
- Reflog investigation and historical reference movements.
- Dangling and unreachable objects.
- Cruft pack creation, retention, and expiration.
- Commit and patch investigation using `git patch-id`.
- Equivalent change identification using `git cherry`.
- Rebase and cherry-pick effects on commit identity and patch equivalence.
- Reflog-based commit recovery.

Practical exercises and investigations:

- Historical file reconstruction and retrieval.
- Git object inspection and reconstruction.
- Loose object creation and inspection using `git hash-object`.
- Commit, tree, and blob relationship investigation.
- Symbolic reference and detached HEAD investigation.
- Dangling tree recovery.
- Reflog-based lost commit investigation and recovery.
- Commit metadata and raw diff inspection.
- Patch equivalence investigation using `git patch-id`.
- Duplicate change identification using `git cherry`.
- Rebase and cherry-pick commit identity and patch equivalence investigation.
- Packfile inspection and verification.
- Delta compression and garbage collection.
- Cruft pack creation, inspection, and expiration.

**Supporting repositories:**

1. [Git Debugging Lab](https://github.com/simple-tech-with-tarun/git-debugging-lab)
2. [Git Packfile Lab](https://github.com/simple-tech-with-tarun/git-packfile-lab)
3. [Git Cruft Pack Lab](https://github.com/simple-tech-with-tarun/git-cruft-pack-lab)

The Git Debugging Lab contains practical investigation and recovery exercises with documented findings and validation evidence. The Git Packfile Lab and Git Cruft Pack Lab cover practical exercises involving object storage, packfile creation and verification, delta compression, repository maintenance, cruft pack lifecycle, and unreachable object recovery.

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

This chapter is supported by four dedicated Git learning repositories. Each repository focuses on a different aspect of Git history investigation, object storage, repository maintenance, and recovery.

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
- Reflog investigation and HEAD movement analysis.
- Symbolic references, direct references, and detached HEAD.
- Recovery of commits removed from branch history.
- Commit, tree, and blob relationship investigation.
- Patch equivalence analysis using `git patch-id`.
- Identifying equivalent changes using `git cherry`.
- Rebase and cherry-pick effects on commit identity.
- Raw commit metadata and diff investigation.

Important commands documented in the repository:

```bash
git log --graph --oneline --all
git show <commit>
git show --format=fuller <commit>
git show --raw --format=fuller <commit>
git diff <branch1> <branch2>

git blame
git log -S
git log -G
git log --follow

git reflog --date=local
git reset --hard <commit>

git fsck --full --unreachable
git cat-file -t <object>
git cat-file -s <object>
git cat-file -p <object>
git ls-tree -r <tree>
git hash-object <file>
git hash-object -w <file>

git patch-id --stable
git cherry <upstream> <head>
```

### 2. Git Bisect Lab

Repository: [simple-tech-with-tarun/git-bisect-lab](https://github.com/simple-tech-with-tarun/git-bisect-lab)

Purpose:

A hands-on repository for learning advanced Git bisect techniques, identifying regression-introducing commits, automating regression investigations, and handling complex Git histories.

Key learning areas:

- Manual regression investigation and bisect boundaries.
- Skipped and untestable commits.
- Automated regression testing using `git bisect run`.
- Merge-related regression investigation.
- Recovery from incorrect bisect classifications.
- Bisect investigation logs and reproducibility.

Exercise documentation:

- [Manual and skipped-commit bisect exercises](https://github.com/simple-tech-with-tarun/git-bisect-lab/tree/main/01-manual-bisect)
- [Automated bisect](https://github.com/simple-tech-with-tarun/git-bisect-lab/tree/main/02-automated-bisect)
- [Merge-related bisect](https://github.com/simple-tech-with-tarun/git-bisect-lab/tree/main/03-merge-bisect)
- [Bisect recovery](https://github.com/simple-tech-with-tarun/git-bisect-lab/tree/main/04-bisect-recovery)

### 3. Git Packfile Lab

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

The repository demonstrates how Git stores objects efficiently and how repository maintenance operations reorganize the object database. The practical exercises cover loose and packed objects, delta compression, packfile verification, garbage collection, and reflog expiration.

### 4. Git Cruft Pack Lab

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

The repository demonstrates how deleting a branch and expiring reflog entries can leave objects unreachable, how Git stores those objects in cruft packs, and how expiration and pruning affect their retention.

## Relationship to the Learning Roadmap

| Learning Phase | Supporting Repository | Status |
|---|---|---|
| Advanced Git History Investigation | Git Debugging Lab | Completed — verification pending |
| Tracing Code Changes and Contributions | Git Debugging Lab | Completed — verification pending |
| Advanced Git Bisect and Regression Detection | Git Bisect Lab | Completed - verification pending |
| Repository Forensics and Historical Reconstruction | Git Debugging Lab, Git Packfile Lab, Git Cruft Pack Lab | Completed - practical work documented |
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
| 3 | Advanced Git Bisect and Regression Detection | Completed — verification pending |
| 4 | Repository Forensics and Historical Reconstruction | Completed - practical work documented |
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
