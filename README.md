# Endpoint_Automation_Framework
Page Object Model Automation Framework requires `Python 3.6` version and various packages that could be found in 
Endpoint_Automation_Framework/configuration/environment.yml file. To start you can create Conda Virtual Environment 
using Anaconda/Miniconda.

`Pytest` is used as a test runner and required to be default test runner to execute auto_tests
 
 # Conda Virtual Environment
Install Anaconda/Miniconda (package, environment management system) and use
Platform_Test_Automation/configuration/Conda_Environment.yml file to create Conda Virtual Environment.

- Download Anaconda or MiniConda
- Anaconda - https://www.anaconda.com/distribution/#download-section
- MiniConda - https://docs.conda.io/en/latest/miniconda.html
- Install Anaconda or MiniConda

Conda Virtual Environment commands:
* To **Create** Conda Environment: \
`conda env create -f C:\...\Conda_Environment.yml` (path to Conda_Environment.yml)
* **Activate/Deactivate** Conda Environment: \
Windows: \
`activate {env_name}` \
`deactivate` \
Mac and Linux: \
`source activate {env_name}` \
`source deactivate` 
* To **Remove** Conda Environment: \
`conda env remove --name {env_name} --all`
* List of conda Virtual Environments:
```
conda info --envs
conda env list
```
* To install packages: \
`conda install -n {env_name} {package_name}`
* To search for a package: \
`conda search {package_name}`
* To see list of packages in the specific environment: \
`conda list -n (C:\..\env name)`
* To use Pip to install packages: \
Windows:
```
activate {env_name}
pip install {package_name}
```
Mac:
```
source activate {env_name}
source pip install {package_name}
```

# PyCharm
PyCharm integrated development environment can be used to execute tests. 
* Download from community edition: https://www.jetbrains.com/pycharm/download 
* Checkout Endpoint_Automation_Framework from Version Control Git 
* Use `Python 3.6` Interpreter from Conda Virtual Environment (that was previously created)
* Choose `Pytest` as a default test runner

# Test run results
Interactive Test run results are located in Endpoint_Automation_Framework/auto_tests/ - `login_tests_report.html` file.
Open in any browser

# Test Execution screen recording and Bug Report Example
Bug Report example pdf file is available under `001_Bug_Report_example_for_Endpoint_Closing.pdf`
Login Page test suite execution screen recording is available under `002_Test_Execution_Example_video_recording.mov`
Both files are located in main directory /Endpoint_Automation_Framework