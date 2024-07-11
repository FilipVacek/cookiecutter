# Report for Assignment 1 resit

## Project chosen

Name: cookiecutter

URL: https://github.com/cookiecutter/cookiecutter

Number of lines of code and the tool used to count it: 7545 NLOC, counted with lizard

Programming language: Python

## Coverage measurement with existing tool

The tool used to measure coverage: Coverage.py

The following command was used to generate a coverage report: coverage run --source tests -m unittest discover && coverage report

<img width="678" alt="Screenshot 2024-07-11 162819" src="https://github.com/FilipVacek/cookiecutter/assets/121828721/469e1446-172b-4660-9724-d4207e7013cb">
<img width="425" alt="Screenshot 2024-07-11 162438" src="https://github.com/FilipVacek/cookiecutter/assets/121828721/38bb29d6-6188-41e8-ad7c-3b58f8b38538">

## Coverage improvement

### Individual tests

Function 1

https://github.com/FilipVacek/cookiecutter/commit/000273602258b800ba91fc1b3134b80d45266eca

<img width="709" alt="image" src="https://github.com/FilipVacek/cookiecutter/assets/121828721/3fd0ceee-904f-47a6-8431-bcd6c019edaf">

<img width="722" alt="image" src="https://github.com/FilipVacek/cookiecutter/assets/121828721/b54d9465-b3dc-4869-8341-b50a073f1682">

The is_copy_only_path function, which was previously flagged as missed, has been given its own test. The coverage of the 'generate' module has improved by 4%, the coverage of the entire project has improved by 1%.

Function 2



### Overall

<Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed at the beginning of the report)>

<Provide a screenshot of the new coverage results by running the existing tool using all test modifications>
