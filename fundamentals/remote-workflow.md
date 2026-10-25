# Working with Remote Repositories

## Remote and Local Branches

A local branch and its remote-tracking branch can point to different commits. Git uses remote-tracking branches, such as `origin/main`, to represent the remote state observed during the latest fetch.

## Common Commands

```bash
git remote -v
git fetch origin
git branch -vv
git status -sb
git pull
git push
git push -u origin <branch-name>
```

## Key Distinctions

- `git fetch` updates remote-tracking references without integrating changes into the current branch.
- `git pull` fetches remote changes and integrates them into the current branch.
- `git push` publishes local commits to a remote branch.
- `git push -u` also configures the upstream for the local branch.

## Tracking Branches

An upstream connects a local branch to a remote-tracking branch. This relationship allows Git to determine the default remote branch for operations such as `git push` and `git pull`.

Check the configured upstream with:

```bash
git rev-parse --abbrev-ref --symbolic-full-name '@{upstream}'
```
