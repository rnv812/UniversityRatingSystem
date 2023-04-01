# University Rating System

## Introduction

### Objective
The objective of the "University Rating System" is to stimulate the growth of qualifications, professionalism, productivity of pedagogical, scientific and other kinds of activities.

### Task
The main task of the project is creation the inforamtion system that has:
- ability to manage and to store information about different kinds of activities of educators (also about departments and faculties subsequently) within the university;
- tools for analysys of storing information;
- possibility of integration with external services (e.g. internal departments of rating calculation);

### Storing Data
The rating of **educators** consists of six **partitions**:
- **Potential** - qualification of the educator, achieved by him throughout his entire university career;
- **Scientific and creative activity** - involvement in the scientific, innovative and creative activities;
- **Educational activity** - quality of the provision of educational services;
- **Financial indicators** - attraction of additional financing;
- **Administrative activity** - contribution to university administration;
- **International activity** - participation in international activities.

## Terms
**Form** (ru. Бланк) - web form that the educator fills up on the site at the end of each year. He enters his **indicators values** for the current year.

**Indicator** (ru. Показатель) - parameter representing the effectiveness of the educator in a particular task.

**Criterion** (ru. Критерий) - indicator that belongs to specific **partition** and has some weight of rating impact.

**Criterion value** (ru. Значение критерия) - value achieved by the educator for a specific **сriterion**.

**Partition** (ru. Раздел) - named group of criterions related to a similar thematics.

## Roles and permissions

The start implementation supposes the following human roles: 
- **Educator**:
  - creates own forms;
  - edits own forms;
  - browses own forms.
- **Forms controller**:
  - has forms possibilities of all educators on department which he is assigned to;
  - examines and approves available forms.
- **Administartor**:
  - asigns roles and perform CRUD operations with any resource.
