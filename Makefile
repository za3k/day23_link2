run-debug:
	flask --debug run
run-demo:
	gunicorn3 -e SCRIPT_NAME=/hackaday/link2 --bind 0.0.0.0:8023 app:app
