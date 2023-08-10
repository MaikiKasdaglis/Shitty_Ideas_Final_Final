# Shitty Ideas CLI Project

## Introduction

This is my phase 3 final project. It allows users to create and log in as developers. Users can create phase 3 projects by selecting an existing or creating a new "shitty idea." Developers and shitty ideas exist independently but are joined in projects. Projects require both a developer and a shitty idea to be created.

## Schema

```
+-------------------+             +---------------------+             +-----------------+
|    Shitty_Idea    |             |   Phase_3_Project   |             |    Developer    |
+===================+             +=====================+             +=================+
|       id          |             |         id          |             |       id        |
+-------------------+             +---------------------+             +-----------------+
|    idea_name      |             |    project_name     |             |      name       |
+-------------------+             +---------------------+             +-----------------+
| idea_description  |             |     fun_scale       |             |                 |
+-------------------+  1---------*| shitty_idea_id(1,2) +*----------1 |                 |
| shittiness_scale  |             | developer_id(1,2)   |             |                 |
+-------------------+             +---------------------+             +-----------------+

```

## Features

- Login with existing Developer name. If none exists, one will be created.
- Create/Delete a shitty idea.
- Create/Delete a Phase 3 Project.
- Find the project/s associated with the shittiest idea.
- Find the Developer associated with the most project instances.
- Show all the existing projects, ordered by how fun they are.
- See a 'tuple' in action. Learn about 'tuples'
- Exit the CLI

---

> **Note: You must run pipenv install && pipenv shell and cd in to lib/db before running python3 cli.py. **

---

## Usage

once you've enteredt the CLI enter the developer name you'd like to use. enter the number for whatever feature you'd like to utilize and hit enter.

## Contact

https://www.linkedin.com/in/michael-kasdaglis/
