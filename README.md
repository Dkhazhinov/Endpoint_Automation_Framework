# Endpoint_Automation_Framework
Page Object Model Automation Framework requires Python 3.6 version and various packages that could be found in 
Endpoint_Automation_Framework/configuration/environment.yml file. To start you can create Conda Virtual Environment 
using Anaconda/Miniconda.
 
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
`deactivate`
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
* To use Pip to install packages:
```
activate {env_name}
pip install {package_name}
```