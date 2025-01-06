# The Pacific 🌊: Group Code Review Exercise

Welcome to **The Pacific** - a collaborative coding initiative by **Group 1** of
the MIT Emerging Talent Program. Together, we aim to code, learn, and grow as
developers while fostering a supportive and inspiring team environment.

<img src="./collaboration\guide\assets\the_pacific.gif" alt="The Pacific"
style="width: 100%; height: auto;">

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [How to Contribute](#how-to-contribute)
3. [Project Goals](#project-goals)
4. [Team Composition](#team-composition)
5. [Repository Structure](#repository-structure)
6. [Setup and Usage](#setup-and-usage)
7. [Roles and Responsibilities](#roles-and-responsibilities)
8. [Task Breakdown](#task-breakdown)
9. [Definition of Done](#definition-of-done)
10. [Tools and Technologies](#tools-and-technologies)
11. [Milestones](#milestones)

---

## Project Overview

This repository serves as the hub for our group collaboration, where we:  

1. **Collaborate on coding projects**: Work together on group projects to hone our
   technical skills.  
2. **Learn from each other**: Share knowledge, resources, and tips to help everyone
   grow.  
3. **Code reviews**: Provide constructive feedback to improve the quality of our
   code and learn best practices.
4. **Build community**: Strengthen our team spirit as we progress through the  
   MIT Emerging Talent Program.

---

## How to Contribute

We encourage all team members to actively participate. Here's how you can  
contribute:  

1. Check the **Tasks** section for assigned roles and deadlines.  
2. Follow the **Setup and Usage** guide to get started with the repository.  
3. Submit pull requests for code contributions, ensuring your work meets the  
   **Definition of Done.**  
4. Participate in code reviews by providing constructive feedback on your peers'
   submissions.

---

## Project Goals

1. Strengthen Python programming and unit testing skills.
2. Practice professional GitHub workflows, including pull requests and code reviews.
3. Develop teamwork and collaboration skills.
4. Prepare for group-oriented Data Science projects.

---

## Team Composition

| **Name**               | **Role**               | **Email**                   |
|-------------------------|------------------------|-----------------------------|
| Yurii Spizhovyi         | Developer, Reviewer   | <spizhov22y@gmail.com>       |
| Alemayehu Kiros         | Developer, Reviewer   | <alemayehu8363@gmail.com>    |
| Khadija al Ramlawi      | Developer, Reviewer   | <kalramlawi@gmail.com>       |
| Henry Ogoe              | Developer, Reviewer   | <djokwa@gmail.com>           |
| Suhrob Muborakshoev     | Developer, Reviewer   | <suhrob.m89@gmail.com>       |
| Mithchell Cenatus       | Developer, Reviewer   | <mlawenskycenatus@gmail.com> |
| Olumide Kolawole        | Developer, Reviewer   | <olumidekolawole26@gmail.com>|
| Mykyta Kondratiev       | Developer, Reviewer   | <kondratiev.mikita@gmail.com>|
| Dmytro Klymenko         | Developer, Reviewer   | <dmtrklymenko05@gmail.com>   |
| Manezhah Mohmand        | Developer, Reviewer   | <mohmandmanezha@gmail.com>   |

---

## Repository Structure

<details>
<summary>Click to expand/collapse the repository structure</summary>

```plaintext
.
│   .gitignore
│   .ls-lint.yml
│   .markdownlint.yml
│   CONTRIBUTING.md
│   LICENSE
│   README.md
│
├───.github
│   │   PULL_REQUEST_TEMPLATE.md
│   │
│   ├───ISSUE_TEMPLATE
│   │       help_wanted.md
│   │       meeting_agenda.md
│   │       new_challenge.md
│   │       question.md
│   │
│   └───workflows
│           ci-checks.yml
│
├───.vscode
│       extensions.json
│       launch.json
│       settings.json
│
├───collaboration
│   │   communication.md
│   │   constraints.md
│   │   learning_goals.md
│   │   README.md
│   │   retrospective.md
│   │
│   └───guide
│       │   0_repository_setup.md
│       │   1_group_norms.md
│       │   2_learning_goals.md
│       │   3_constraints.md
│       │   4_communication.md
│       │   5_project_board.md
│       │   6_development.md
│       │   7_retrospective.md
│       │   README.md
│       │
│       └───assets
│               branching_strategy.svg
│               claim_branch_review_merge.svg
│
├───notes
│   │   README.md
│   │
│   └───meeting_minutes
│           12_24_2024_meeting_minute.md
│
└───solutions
    │   README.m
    │       solution_1.py
    │       solution_2.py
    │       solution_3.py
    │       solution_4.py
    │       solution_5.py
    │       solution_6.py
    │       solution_7.py
    │       solution_8.py
    │       solution_9.py
    │       solution_10.py
    │       solution_11.py
    │       solution_12.py
    │       solution_13.py
    │       solution_14.py
    │       solution_15.py
    │       solution_16.py
    │       solution_17.py
    │       solution_18.py
    │       solution_19.py
    │       solution_20.py
    └───tests
        │       test_solution_1.py
        │       test_solution_2.py
        │       test_solution_3.py
        │       test_solution_4.py
        │       test_solution_5.py
        │       test_solution_6.py
        │       test_solution_7.py
        │       test_solution_8.py
        │       test_solution_9.py
        │       test_solution_10.py
        │       test_solution_11.py
        │       test_solution_12.py
        │       test_solution_13.py
        │       test_solution_14.py
        │       test_solution_15.py
        │       test_solution_16.py
        │       test_solution_17.py
        │       test_solution_18.py
        │       test_solution_19.py
        │       test_solution_20.py
```

</details>

---

## Setup and Usage

### Prerequisites

- Python 3.8+
- Git
- Text Editor (e.g., VSCode, PyCharm)

### Clone Repository

```bash
git clone https://github.com/MIT-Emerging-Talent/ET6-foundations-group-01.git
cd Group-Code-Review
```

### Run Tests

```bash
unittest /tests
```

---

## Roles and Responsibilities

- **Developer and Reviewer:** Yuriy Spizhovy
  - Develop and review code submissions.
  - Ensure adherence to project guidelines.
- **Developer and Reviewer:** Suhrob Muborakshoev, Mithchell Cenatus
  - Develop and review code submissions.
  - Assist with CI/CD tasks as needed.
- **Developer and Reviewer:** Alemayehu Kiros, Khadija Al Ramlawi
  - Develop and review code submissions.
  - Assist with documentation tasks as needed.
- **Developer and Reviewer:** Henry Ogoe, Olumide Kolawole
  - Develop and review code submissions.
  - Ensure adherence to coding standards.
- **Developers:** All team members
  - Submit solutions and unit tests.

---

## Task Breakdown

- **Individual Tasks:**
  Each team member submits:
  
  | **Team Member**       | **Task**                      | **Deadline**       |
  |-----------------------|-------------------------------|--------------------|
  | Yurii Spizhovyi       | solution_1.py, solution_2.py  | January 3, 2025    |
  | Alemayehu Kiros       | solution_1.py, solution_2.py  | January 3, 2025    |
  | Khadija al Ramlawi    | solution_1.py, solution_2.py  | January 3, 2025    |
  | Henry Ogoe            | solution_1.py, solution_2.py  | January 3, 2025    |
  | Suhrob Muborakshoev   | solution_1.py, solution_2.py  | January 3, 2025    |
  | Mithchell Cenatus     | solution_1.py, solution_2.py  | January 3, 2025    |
  | Olumide Kolawole      | solution_1.py, solution_2.py  | January 3, 2025    |
  | Mykyta Kondratiev     | solution_1.py, solution_2.py  | January 3, 2025    |
  | Dmytro Klymenko       | solution_1.py, solution_2.py  | January 3, 2025    |
  | Manezhah Mohmand      | solution_1.py, solution_2.py  | January 3, 2025    |

- **Shared Tasks:**

| Task               | Assigned Members                | Deadline         |
|--------------------|---------------------------------|------------------|
| communication.md   | Khadija al Ramlawi, Suhrob Muborakshoev | December 30, 2025|
| constraints.md     | Alemayehu Kiros, Manezhah Mohmand  | December 30, 2025|
| learning_goals.md  | Yurii Spizhovyi, Mithchell Cenatus  | December 30, 2025|
| README.md          | Olumide Kolawole, Mykyta Kondratiev | December 30, 2025 |
| retrospective.md   | Dmytro Klymenko, Henry Ogoe, | January 9, 2025 |

---

## Definition of Done

A task is complete when:

1. Solutions pass all unit tests and code reviews.
2. Collaboration documents are reviewed and approved.
3. CI/CD pipelines run successfully.

---

## Tools and Technologies

- **Version Control:** Git
- **Documentation:** Markdown
- **Testing:** pytest
- **CI/CD:** GitHub Actions

---

## Milestones

| **Milestone**                | **Deadline**       |
|-------------------------------|--------------------|
| Repository Setup              | December 20, 2024 |
| Individual Solutions          | January 3, 2025   |
| Collaboration Documents       | December 20, 2024 |
| Code Reviews                  | January 7, 2025  |
| Finalization                  | January 9, 2025  |

---

For further details, visit the project [repository](https://github.com/MIT-Emerging-Talent/ET6-foundations-group-01).
