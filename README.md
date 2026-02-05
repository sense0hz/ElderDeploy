# 🛡️ ElderDeploy: The Elder One

A professional Windows deployment and automation tool designed to streamline corporate environment setups. This script automates domain integration and handles silent software installations with persistence logic.

## ⚙️ How it works
The core of this project is a persistence engine that survives system reboots. By using Windows **RunOnce** registry keys and temporary status flags, the script knows exactly when it's returning from a restart and continues to the installation phase automatically.

## 🚀 Key Features
- **Automated Domain Join**: Integration via PowerShell credentials.
- **Post-Reboot Persistence**: Skips completed steps after a restart.
- **Silent Deployment**: Support for `.exe` and `.msi` installers with visual progress tracking.
- **Modular Design**: Easy-to-edit dictionary for custom software stacks.

## 🛠️ Usage
1. Clone the repository.
2. Create an `Instaladores` folder in the root directory or use the actual.
3. Add your installers and update the `programas_dict` with the correct filenames and silent parameters.
4. Fill in the Domain, User, and Password variables.

## 👨‍💻 Author
**Sense.** (The Elder One)  
*Software Development Student*


