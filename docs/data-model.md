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
| start_date        | string            | no     | no       |
| due_date          | string            | no     | no       |
| is_completed      | string            | no     | yes      |
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
| members           | string            | no     | no       |
| company           | string            | no     | yes      |
| date_added        | ref to project    | no     | no       |


### Company

| name              | type              | unique | optional |
| ----------------  | ----------------- | ------ | -------- |
| id                | int               | yes    | no       |
| name              | string            | no     | no       |
| project           | ref to project    | no     | no       |
