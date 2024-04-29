# NoSQL Project README

## Project Overview

This project focuses on understanding NoSQL databases, particularly MongoDB, and utilizing it with Python. The tasks include writing MongoDB command files and Python scripts to interact with MongoDB using PyMongo.

## Learning Objectives

At the end of this project, you should be able to:

- Explain what NoSQL means and its differences from SQL databases.
- Understand the ACID properties.
- Define document storage in the context of databases.
- Identify different types of NoSQL databases and their benefits.
- Query, insert, update, and delete information in a NoSQL database, specifically MongoDB.
- Utilize MongoDB with Python.

## Requirements

### MongoDB Command File:

- Files should be interpreted/compiled on Ubuntu 18.04 LTS using MongoDB 4.2.
- First line in all files should be a comment.
- Include a README.md file at the root of the project folder.
- Length of files will be tested using `wc`.

### Python Scripts:

- Files should be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7 and PyMongo 3.10.
- First line in all files should be `#!/usr/bin/env python3`.
- Include a README.md file at the root of the project folder.
- Code should follow PEP 8 style guidelines.
- Length of files will be tested using `wc`.
- All modules and functions should have documentation.
- Code should not be executed when imported.

## Installation

Ensure MongoDB 4.2 is installed on your Ubuntu 18.04 system and PyMongo is installed via pip:

```bash
$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
...
$ pip3 install pymongo

