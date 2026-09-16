test:
	pytest -v --html=reports/report.html --self-contained-html

smoke:
	pytest -m smoke -v --html=reports/smoke-report.html --self-contained-html

regression:
	pytest -m regression -v --html=reports/regression-report.html --self-contained-html

report:
	pytest -v --html=reports/report.html --self-contained-html