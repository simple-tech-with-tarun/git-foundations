# Git Tag Workflow

Git tags mark specific commits in a repository's history. They are useful for identifying releases, milestones, and other important points in a project's development.

This reference covers creating, inspecting, publishing, and deleting Git tags.

## 1. List Tags

List all local tags:

```powershell
git tag --list
```

## 2. Create Tags

### Lightweight tag

A lightweight tag is a simple reference to a commit.

```powershell
git tag v1.0
```

This creates a tag for the current commit.

### Annotated tag

An annotated tag creates a separate tag object containing the tagger, date, message, and target object.

```powershell
git tag -a v1.0 -m "Version 1.0"
```

Annotated tags are generally preferred for releases and meaningful milestones.

### Tag a specific commit

Provide a commit hash or another valid commit reference to tag a specific commit.

```powershell
git tag v1.0 <commit-hash>
git tag -a v1.0 <commit-hash> -m "Version 1.0"
```

Creating a tag for an earlier commit does not require checking out that commit.

## 3. Inspect Tags

Display a tag and its target commit:

```powershell
git show v1.0
```

Display the tag and commit information without the patch:

```powershell
git show v1.0 --no-patch
```

Inspect the underlying object type:

```powershell
git cat-file -t v1.0
```

A lightweight tag normally resolves directly to a `commit` object. An annotated tag resolves to a `tag` object.

Resolve a tag to its target commit:

```powershell
git rev-parse 'v1.0^{commit}'
```

The `^{commit}` suffix resolves the reference to the commit it ultimately identifies. In PowerShell, quote the complete expression to prevent the shell from misinterpreting its special characters.

## 4. Inspect Merge Commits

A merge commit has multiple parents. By default, `git show` generally omits its patch.

Display separate diffs against the merge commit's parents:

```powershell
git show -m <commit-hash>
```

This changes how Git displays the merge commit; it does not modify the commit or any tag pointing to it.

## 5. Push Tags

Publish one specific tag:

```powershell
git push origin v1.0
```

List tags advertised by the remote:

```powershell
git ls-remote --tags origin
```

Publish all local tags that are not already present on the remote:

```powershell
git push origin --tags
```

Use the last command carefully because it publishes all local tags, including any temporary tags.

## 6. Delete Tags

Delete a local tag:

```powershell
git tag -d v1.0
```

Delete a remote tag:

```powershell
git push origin --delete v1.0
```

Local and remote tag references are managed separately. Deleting one does not automatically delete the other. Neither operation deletes the commit itself.

## 7. Rename a Tag

Git does not provide a dedicated tag-renaming command. Create a replacement tag pointing to the same target, then delete the old local tag:

```powershell
git tag new-name old-name
git tag -d old-name
```

If the old tag exists on the remote, push the replacement tag and delete the old remote tag separately.

## 8. Tags and Branches

- A branch is a movable reference that normally advances when new commits are created on it.
- A tag marks a specific point in history and does not automatically advance with new commits.
- A tag can point to a commit reachable from any branch; it is not restricted to `main`.
- Annotated tags are generally preferable for releases and meaningful milestones because they include metadata and a message.
