.PHONY: help install lab1-basic lab1-advanced lab2-basic lab2-advanced \
        lab3-basic lab3-advanced lab4-basic lab4-advanced test lint clean

help:
	@echo "Доступные команды:"
	@echo "  make install         — установить зависимости"
	@echo "  make lab1-basic      — запустить ЛР №1 (basic)"
	@echo "  make lab1-advanced   — запустить ЛР №1 (advanced)"
	@echo "  make test            — запустить pytest"
	@echo "  make lint            — ruff + mypy"
	@echo "  make clean           — очистить кэш и артефакты"

install:
	pip install -r requirements.txt

lab1-basic:
	python lab_01_linear_function/src/basic.py

lab1-advanced:
	python lab_01_linear_function/src/advanced.py

lab2-basic:
	python lab_02_branching/src/basic.py

lab2-advanced:
	python lab_02_branching/src/advanced.py

lab3-basic:
	python lab_03_loops/src/basic.py

lab3-advanced:
	python lab_03_loops/src/advanced.py

lab4-basic:
	python lab_04_arrays/src/basic.py

lab4-advanced:
	python lab_04_arrays/src/advanced.py

test:
	pytest

lint:
	ruff check .
	mypy .

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	rm -f results/*.txt
