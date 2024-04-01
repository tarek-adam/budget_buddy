#!/bin/bash

# Activate the virtual environment
source /home/x/myenv/bin/activate

# Run emailCheck.py
python3 emailCheck.py &

# Run LogIn.py
python3 LogIn.py

# Run password.py
python3 password.py

# Run passwordSecurity.py
python3 passwordSecurity.py
