# polaris-interview
Sample project for gauging interviewee knowledge and process.

## Synopsis
Using the Django REST framework, we want you to display a list of trips. We don't think this should take you more than 4 hours or so. You're welcome to spend more time in it if you like, but that shouldn't be needed. The deadline is Monday Jan. 26th by 9am.

## What's the end goal
The point of this is to see how you work. We're looking for well-documented code that not only explains _what_ you're doing, but also _why_ you are doing it. We want to understand the how and why of you putting this together. We're looking for your understanding in the structure of the project, as well as why you opted to do things the way that you did.

## Getting started
First, you'll need to get your environment set up. We don't want you wasting your time setting your environment up, so here's what you'll need to do to get started:

- [install pip](http://stackoverflow.com/questions/17271319/installing-pip-on-mac-os-x)
- [install git](https://help.github.com/articles/set-up-git/)
- [clone repo](https://github.com/gadventures/polaris-interview)
- Install requirements `pip install -r requirements.txt`
- Run Server `python manage.py runserver`

### pulling the repo
Now you'll need to pull down a copy of our repo. Set up a folder for where you want to work and then:
`git clone https://github.com/gadventures/polaris-interview.git` or `git clone git@github.com:gadventures/polaris-interview.git`

Next you'll have to install the requirements:
`pip install -r requirements.txt`

### create a new branch
Before you dive into the code, we want you do create a new branch to do your work. The reason for this is so that you can issue a pull request, which will allow us to review your code. So to create a new branch:
`git checkout -b your_branch_name`

*Note:* Make sure you put your name in the branch so we can identify it.

You'll want to make sure you're doing commits along the way:
`git commit -ma "your message here"

That's good for us and you. It helps us by letting us see your thought processes, and it helps you by making save points.

## What we want you to do
We want you to create an application that lists Trips via a template and API. The Trip can be as detailed as you wish to make it with the end goal of being able to view all of the existing trips via `https://127.0.0.1:8000/` and via the API at `https://127.0.0.1:8000/api/`

## When you're finished
Once you're ready to submit, you can create a pull request:
`git request-pull your_branch_name https://github.com/gadventures/polaris-interview master`

We'll be notified, and then we can look it over.
