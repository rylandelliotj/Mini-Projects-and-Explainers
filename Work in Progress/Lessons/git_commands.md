# Here are some commands for git that can be used in a terminal

> git --help: show git commands
> git init: designates a folder as a git repo.
> git add: can be used to stage/add a change in a repo. This does not commit the file.
> git add .: stages all changes in the repo.
> git status: shows us what is currently staged; tells us if there are changed that need to be commited to the repo
> git commit -m"": adds in a 'checkpoint' in your branch that can be used to return to if you make changes in a repo. You write in between the quotations what has been changed.
> git checkout master: switch to the "master" branch. replace "master" with the name of the branch if switching to a different branch.
>  git checkout <commit-hash>: enter the hash for a previous commit to return to that version. Use "git checkout master" to return to the most recent commit
> git reset --hard <commit-hash>: resets your master branch to a previous commit.
> git checkout -b new_branch: create a new branch called "new_branch". This will also switch you to the new branch.
> git merge master: will merge the current branch wit the master branch.
> git remote add origin https://github.com/username/repo.git: adds a url to another repo. The url is a remote that we have called "origin". You may need to put the link in quotations.
> git push -u origin master: push our commits on our local repo to the master branch on the origin repo.
> git config --global user.name "username": authenticates yourself so you can push changes locally to a remote repo with the name "username".
> git config --global user.email "elliot.ryland@cer-rec.gc.ca": authenticates yourself so you can push changes locally to a remote repo with the email "elliot.ryland@cer-rec.gc.ca".
> git pull origin master: get changes from the "origin" repo's master branch to your local repo. If you pull and there is a conflict, you need to manually enter the file that is conflicting and organize it how you want it to look.
> git push origin master: put changes into the remote's master branch. You should always pull before you push a change from local to remote to ensure there is no conflict.
> git log: show all changes to the git repo
> git init --bare: creates a "bare" repository that can be used as a remote by other git repos. 