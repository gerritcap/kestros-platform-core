kestros-build-helper


git-helper.py - helper script for working with multiple git projects.

- Runs commands for each project listed in the git_projects array
- There are some prerequisites, see module list
- Examples:
    1. Check what branch each project is on: ./git-helper.py -c "git branch"
    2. Commit with multi-line comment: ./git-helper.py -c "git commit -a -m\"- Adding installPackage profile to slingare-settings.xml.\" -m \"- Added maven-sling-plugin to core pom files.\" -m \"- Removed embedded bundles and packages from frontend pom files.\""
