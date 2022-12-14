# Data models

## Accounts application

### Account

Inherited from Django Users.


## Tasks application

### Task

| name              | type              | unique | optional |
| ----------------  | ----------------- | ------ | -------- |
| id                | int               | yes    | no       |
| name              | string            | no     | no       |
| start_date        | date              | no     | no       |
| due_date          | date              | no     | no       |
| is_completed      | boolean           | no     | yes      |
| project           | ref to project    | no     | no       |
| assignee          | ref to account    | no     | no       |
| notes             | string            | no     | yes      |


## Projects application

### Project

| name              | type              | unique | optional |
| ----------------  | ----------------- | ------ | -------- |
| id                | int               | yes    | no       |
| name              | string            | no     | no       |
| description       | string            | no     | yes      |
| members           | ref to user       | no     | no       |
| company           | ref to company    | no     | yes      |
| date_added        | date              | no     | no       |


### Company

| name              | type              | unique | optional |
| ----------------  | ----------------- | ------ | -------- |
| id                | int               | yes    | no       |
| name              | string            | no     | no       |
| project           | ref to project    | no     | no       |
