# Fork Repository Commands

Manual commands to fork a GitHub repo locally (without using the script).

## Step-by-step commands

Replace `<github-url>` with the actual repository URL and `<target-directory>` with your desired folder name.

### Clone the repository

```bash
git clone <github-url> <target-directory>
```

### Navigate into the repository

```bash
cd <target-directory>
```

### Rename origin to upstream

```bash
git remote rename origin upstream
```

### Verify the remote setup

```bash
git remote -v
```

## Later: Add your own remote

When you're ready to add your own remote repository:

```bash
git remote add origin <your-repo-url>
```

### Push to your remote

```bash
git push -u origin main
```

## Pulling updates from upstream

When you want to sync with the original repository:

```bash
git pull upstream main
```

## Example workflow

```bash
# Fork the repo
git clone https://github.com/user/awesome-project my-fork
cd my-fork
git remote rename origin upstream

# Later, add your own remote
git remote add origin https://github.com/yourname/my-fork
git push -u origin main

# Pull updates from upstream
git pull upstream main
```
