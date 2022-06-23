## mechine_learning_project
this is first machine learning project

### software_and_account_requirements
 1. [GIT Account](https://github.com/Anubnr/mechine_learning_project)
 2. [Heraku Account](https://dashboard.heroku.com/apps)
 3. [VSCode IDE](https://code.visualstudio.com/download)
 4. [Git Cli](https://git-scm.com/download/win)
 5. [Git command documnentation](https://git-scm.com/docs/git)

Creating conda Environment
```
conda create -p venv python==3.7 -y
```
```
conda activate venv
```
OR
```
conda activate venv/
```
```
pip install -r requirements.txt
```
to add files to git
```
git add .
```
OR
```
git add <file_name>
```
to check status
```
git status
```
>note: to ignore file/folder, write the name of the file/folder in .gitignore
to check all the versions maintained by git
```
git log
```
to create version/commit all the changes
```
git commit -m "message"
```
to send version/changes to git
```
git push origin main
```
to check remote url
```
git remote -v
```


To set-up CI/CD pipeline in heroku we need 3 informations
1. Heroku Email: billaanushabnr@gmail.com
2. Heroku_API_KEY:ca62a501-9e00-4992-91b6-69e345b08911
3. Heroku_API_NAME:https://dashboard.heroku.com/apps/ml-regression-anusha/deploy/heroku-git


BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
>Note: image name for docker must be in lowercase

to list docker images
```
docker images
```
Run docker images
```
docker run -p 5000:5000 -e PORT:5000 image_code
```
>note: image_code is the location where the image is loaded from

To check running containers in docker
```
docker ds
```
to stop docker container 
```
docker stop <container_id>
```
