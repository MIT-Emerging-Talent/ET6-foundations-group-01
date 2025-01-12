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

| **Name**                | **Role**               | **Username / Profile**    |
|-------------------------|------------------------|---------------------------|
| Yurii Spizhovyi         | Developer, Reviewer   | [yuri-spizhovyi-mit][link-1]|
| Alemayehu Kiros         | Developer, Reviewer   | [Alemayehu-Desta][link-2]|
| Khadija al Ramlawi      | Developer, Reviewer   | [Khadijaramlawi][link-3]|
| Henry Ogoe              | Developer, Reviewer   | [Djokwa][link-4]|
| Suhrob Muborakshoev     | Developer, Reviewer   | [suhrobmuboraksho][link-5]|
| Mithchell Cenatus       | Developer, Reviewer   | [Mithchell509][link-6] |
| Olumide Kolawole        | Developer, Reviewer   | [olumide-AI][link-7] |
| Mykyta Kondratiev       | Developer, Reviewer   | [Mykytako][link-8]|
| Dmytro Klymenko         | Developer, Reviewer   | [Papsik09][link-9]|
| Manezhah Mohmand        | Developer, Reviewer   | [Manezhahm][link-10] |

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
    │   add_two_numbers.py
    │   binary_to_decimal.py
    │   calculate_and_classify_bmi.py
    │   calculate_median.py
    │   capitalize_character.py
    │   convert_fahrenheit_to_celsius.py
    │   count_character_occurrences.py
    │   count_vowels.py
    │   days_passed_2025.py
    │   emoji_sentiment.py
    │   even_numbers.py
    │   find_max_in_list.py
    │   is_palindrome.py
    │   README.md
    │   repeat_characters.py
    │   sum_odd_numbers.py
    │   sum_of_digits.py
    │   weight_conversion.py
    │   __init__.py
    │
    └───tests
            README.md
            test_add_two_numbers.py
            test_binary_to_decimal.py
            test_calculate_and_classify_bmi.py
            test_calculate_median.py
            test_capitalize_character.py
            test_convert_fahrenheit_to_celsius.py
            test_count_character_occurrences.py
            test_count_vowels.py
            test_days_passed_2025.py
            test_emoji_sentiment.py
            test_even_numbers.py
            test_find_max_in_list.py
            test_is_palindrome.py
            test_kilograms_to_pounds.py
            test_pounds_to_kilogram.py
            test_repeat_characters.py
            test_sum_odd_numbers.py
            test_sum_of_digits.py  
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
cd ET6-foundations-group-01
```

### Run Tests

```bash
unittest /tests
```

---

## Roles and Responsibilities

- **Developer and Reviewer:** Yurii Spizhovyi
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

[link-1]: https://github.com/yuri-spizhovyi-mit
[link-2]: https://github.com/Alemayehu-Desta
[link-3]: https://github.com/Khadijaramlawi
[link-4]: https://github.com/Djokwa
[link-5]: https://github.com/suhrobmuboraksho
[link-6]: https://github.com/Mithchell509
[link-7]: https://github.com/olumide-AI
[link-8]: https://github.com/Mykytako
[link-9]: https://github.com/Papsik09
[link-10]: https://github.com/Manezhahm
