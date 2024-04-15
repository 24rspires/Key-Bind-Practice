
# Keybind Practice

## Overview
This project is designed to help people practice their keybinds on Xbox controllers (other controllers may work but are untested and not guaranteed to work at this time).

## Requirements Installation

Before running the project, ensure you have Python 3.12 installed on your system. You will also need to install the necessary dependencies.

Or download the prebuilt binaries for Windows [here](https://github.com/24rspires/Key-Bind-Practice/releases/tag/release)

### Installing Python 3.12

The method of installing Python 3.12 can vary depending on your operating system. Below are general guidelines:

#### Windows and macOS:
- Visit the official Python website at [python.org](https://www.python.org/downloads/).
- Download the installer for Python 3.12 for your operating system.
- Run the installer and follow the on-screen instructions to complete the installation.

#### Linux:
- Most Linux distributions include Python in their repositories. You can install Python 3.12 using your package manager. For Ubuntu, you can use the following commands:
    ```bash
    sudo apt update
    sudo apt install software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install python3.12
    ```
- Verify the installation by typing `python3.12 --version` in your terminal.

### Installing Project Requirements

After installing Python, navigate to the project's root directory in your terminal and run the following command to install the required Python packages:

```bash
pip install -r requirements.txt
```

## Running the Project

To run the project, use the following command in the terminal from the project's root directory:

```bash
python main.py
```

On the first launch, it will create a `config.json` file.

This config file has to stay in the same root directory as the python script or executable!

In this file, you can specify your keybinds. 

The keys to each `buttonBindings` and `motionBindings` specify the name of the command to be displayed. 

If you do not have a command for a specific key, please delete that line!

For example, if I do not have anything bound to dpadUp, I would delete the following line from `config.json`:

`"commandDPAD_UP": "DPAD_UP",`

Using this file, you can also specify the resolution you would like the tool to run in and whether or not to run in fullscreen

## Contributing

Contributions to this project are welcome. Please create a pull request or open an issue with your proposed changes. I am always looking to improve this project!
