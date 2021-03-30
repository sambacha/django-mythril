#!/bin/bash
python3 --version
python3 manage.py test test/ --verbosity=1

# Command line tests
chmod +x test/test_command_line.sh
./test/test_command_line.sh
