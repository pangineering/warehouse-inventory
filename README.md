
# Warehouse Inventory

![side-project.svg](/side-project.svg) ![type-web-app.svg](/type-web-app.svg)
[![Status - In Progress](https://img.shields.io/badge/Status-In_Progress-2ea44e?style=for-the-badge)](https://)

## Tech Stack
### For developing Web App
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green) ![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

### Database
![Sqlite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

<!-- ### Hosting
![Heroku](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white) -->

### For developing models
![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white) ![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white) ![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)

### Tools
![VS Code](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)



## Features
A Webapp platform for a warehouse to manage its inventories and its operation in real-time. 
1. Use AI to help manage the inventories
2. Customer and supplier lists
3. Responsive
4. Create reports
5. Control or monitor robots in the warehouse
6. A dashboard for IoT

## Screenshots

![App Screenshot](screens/inventory.png)


## Clone the project
```bash
  git clone https://github.com/pangineering/warehouse-inventory.git
```

## Installation
1. Create a virual environment
```bash
  virtualenv env
  source env/bin/activate
```
2. Install Libraries
```bash
    pip3 install -r requirements.txt
```
## Run Locally
```bash
    python3 manage.py runserver
```