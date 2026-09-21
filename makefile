build:
	python -m source\nsis_py\app.py

package:
	pyinstaller --onefile --windowed --name nsis-py source\nsis_py\app.py