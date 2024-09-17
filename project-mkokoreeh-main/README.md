[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/txO78GXh)
# CSCI360-2023Fall-Project

## Installation
If you want to create a brand new environment for project, use commands:
```
conda create -n csci360_project python=3.8
conda activate csci360_project
pip install -r requirements.txt
```
Or, you can install new libraries to previous environment with commands:
```
conda activate [PREVIOUS_ENV_NAME]
pip install xlrd
```

## Instructions
- If the problem asks you to download a dataset, read the first part of Jupyter Notebook for each problem and put it to designated location.
- A separate Jupyter Notebook is created for P1, P2 and P3+extra credit. Finish marked code blocks accordingly.

## FAQ
### Rules of helper function/class
Write inside `# ===== XXX ===== #` blocks where you will use. When grading, we will call each block once from top. If we encounter an error because you place functions in a later block, we are not going to give points back during regrading (even major point deduction due to syntax error). Note that some compiled functions are saved in memory temporarily so you never get error if you once called the block later.

### How we will grade
Please check instruction PDF for point assignment. We will not disclose further detailed rubrics.
