# hello-world-github-actions-pytest

Hello world for pytest on GitHub Actions.

## How to try

### 1. Create your own repository from this template

In main page of this repository on GitHub, Click [Use this template] button above the file list.

cf. [Creating a repository from a template - GitHub Help](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template)

### 2. Clone your created repository into your local

### 3. Add test pattern

For example, tests/test_hello.py:

```python
    @pytest.mark.parametrize(
        'target, expect', [
            ('world', 'Hello world\n'),
            ('U.S.A', 'Hello U.S.A\n'),
        ])
```

↓

```python
    @pytest.mark.parametrize(
        'target, expect', [
            ('world', 'Hello world\n'),
            ('U.S.A', 'Hello U.S.A\n'),
            ('Japan', 'Hello Japan\n'),
        ])
```

### 4. Commit it and push

### 5. Check workflow run page

In main page of your created repository on GitHub, Click [Actions] tab under your repository name.

cf. [Managing a workflow run - GitHub Help](https://help.github.com/en/actions/automating-your-workflow-with-github-actions/managing-a-workflow-run)
