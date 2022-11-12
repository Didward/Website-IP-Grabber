# Check if python3 is installed
if ! command -v python3 &> /dev/null
then
    echo "python3 could not be found"
    echo "Please install python3 from https://www.python.org/downloads/"
    exit
fi

# Check if pip3 is installed
if ! command -v pip3 &> /dev/null
then
    echo "pip3 could not be found"
    echo "Please install pip3 from https://pip.pypa.io/en/stable/installing/"
    exit
fi

# Run main.py
python3 main.py
