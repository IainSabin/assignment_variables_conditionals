# Codespace Configuration Overview

This document explains the devcontainer setup for instructors and advanced users.

## Installed VS Code Extensions

The following extensions are automatically installed in the Codespace to help students learn Python:

### Core Python Extensions
1. **ms-python.python** - Microsoft's official Python extension
   - Provides IntelliSense, linting, debugging, and code navigation
   - Essential for Python development

2. **ms-python.vscode-pylance** - Advanced language server
   - Provides fast, feature-rich language support
   - Includes type checking and code analysis

3. **ms-python.debugpy** - Python debugger
   - Allows students to set breakpoints and step through code
   - Essential for learning debugging skills

### Code Formatting Extensions
4. **ms-python.black-formatter** - Black Python formatter
   - Automatically formats Python code to follow best practices
   - Enforces consistent style (88 character line length)
   - Works with format-on-save feature

5. **esbenp.prettier-vscode** - Prettier formatter
   - Formats non-Python files (JSON, Markdown, etc.)
   - Ensures consistent formatting across all file types

### Testing Extensions
6. **littlefoxteam.vscode-python-test-adapter** - Python Test Explorer
   - Visual interface for running tests (beaker icon in sidebar)
   - Makes it easy to see which tests pass/fail
   - Automatically discovers pytest tests

### Helper Extensions
7. **njpwerner.autodocstring** - Auto Docstring
   - Helps generate docstrings for functions
   - Teaches students proper documentation practices

8. **streetsidesoftware.code-spell-checker** - Spell Checker
   - Catches typos in code, comments, and strings
   - Helps students write clean, professional code

**Note:** The Environment Manager extension was removed as VS Code's built-in Python extension already provides environment selection in the status bar.

## Disabled Features (For Learning)

To ensure students learn without AI assistance, the following are disabled:
- GitHub Copilot
- IntelliSense auto-complete suggestions
- Inline suggestions
- Word-based suggestions
- Parameter hints during typing

Students must type code themselves and think through problems independently.

## Enabled Features (For Learning Support)

### Visual Aids
- **Bracket Pair Colorization** - Makes matching brackets easier to see
- **Bracket Pair Guides** - Shows vertical lines connecting bracket pairs
- **88-character Ruler** - Helps students learn Black's line length standard
- **Whitespace Rendering** - Shows spaces/tabs at boundaries

### Auto-Save and Formatting
- Files auto-save after 1 second of inactivity
- **Format on Save enabled** - Code is automatically formatted when you save
- Black formatter for Python (88 character line length)
- Prettier formatter for other file types
- Reduces risk of lost work and teaches proper formatting

### Testing Features
- **Auto Test Discovery** - Tests are automatically found when files are saved
- **pytest Integration** - Built-in pytest support with visual test runner

### Type Checking
- **Basic Type Checking** - Alerts students to potential type errors
- Helps catch bugs before running code

### Editor Settings
- **4-space indentation** - Python standard
- **No minimap** - Reduces clutter for beginners
- **Light theme** - Default comfortable theme

## Automatic Setup

When a student opens the Codespace:
1. Python 3.12 environment is created
2. All extensions are installed automatically
3. Dependencies from `requirements.txt` are installed
4. Student can start coding immediately

## For Instructors

You can customize the devcontainer by editing `.devcontainer/devcontainer.json`:
- Add/remove extensions
- Change settings
- Modify the postCreateCommand
- Add additional dependencies to requirements.txt

### Adding More Extensions
To add an extension, find its ID from the VS Code marketplace and add it to the `extensions` array.

### Changing Settings
All VS Code settings can be customized in the `settings` section of devcontainer.json.

## Python Version

This template uses Python 3.12, which is the latest stable version as of 2024. You can change this by modifying the image in devcontainer.json:
```json
"image": "mcr.microsoft.com/devcontainers/python:3.11"
```

## Dependencies

Students can add more Python packages by:
1. Adding them to `requirements.txt`
2. Running `pip install -r requirements.txt` in the terminal
3. Or running `pip install package-name` directly

The devcontainer will automatically install requirements.txt on startup.