PYTHON=python3
PYLINT=pylint3
Source=ctsesam.py

all:
	${PYTHON} -m py_compile $(Source)
	${PYLINT} --reports=n $(Source)

