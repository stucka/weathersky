import papermill
import os

try:
    papermill.execute_notebook(
        "weathersky.ipynb",
        "ignore-weathersky.ipynb",
        log_output=True,
        log_level="debug",
    )
except Exception:
    print("Failure!")

# os.system("python audit-watch-rebuild-reporting.py")
