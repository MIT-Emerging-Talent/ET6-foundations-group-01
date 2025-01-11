# Notes

## Note 1: Using Ruff for Consistent Formatting

To avoid formatting collisions caused by using different tools (e.g., Black and Ruff)
and to align with the `.github/workflows/py_formatting.yml` configuration, everyone
in the team should use the Ruff extension. Follow the steps below to install and
use Ruff:

### Step 1: Install or Update Ruff

For Windows:

```bash
pip install ruff
```

For Mac:

```bash
pip3 install ruff
```

Even if you already have Ruff installed, this command will update it to the
latest version.

### Step 2: Format Code with Ruff

Run the following command to format your code:

```bash
ruff format
```

### Step 3: Commit and Push Changes

After formatting the code, stage, commit, and push your changes:

```bash
git add .
git commit -m "fix formatting issue"
git push origin <branch-name>
```

---

## Note 2: Verifying Files as a Reviewer

If you are assigned as a reviewer, follow these steps to verify files in your
local repository:

### Step 1: Switch to the Remote Branch in VS Code

1. Open VS Code.
2. Click on the current branch name (e.g., `main`) in the bottom left corner.
3. A list of branches will appear.
4. Find the desired remote branch (remote branches have a cloud icon).
5. Click on the branch to switch to it.

[![VSCode][def]][def]

### Step 2: Run Doctest and Unittest

#### Running Doctest

For Windows:

```bash
python -m doctest -v .\solutions\file_name.py
```

For Mac:

```bash
python3 -m doctest -v .\solutions\file_name.py
```

#### Running Unittest

For Windows:

```bash
python -m unittest -v .\solutions\tests\test_file_name.py
```

For Mac:

```bash
python3 -m unittest -v .\solutions\tests\test_file_name.py
```

### Step 3: Observe Results and Comment

- Observe the results of the tests.
- If any tests fail, write comments about the issues in your code review.

---

Feel free to add more notes as you learn and share insights about Python, Git, GitHub,
code review, collaboration, or anything else!

[def]: ../collaboration/guide/assets/vscode_1.png
