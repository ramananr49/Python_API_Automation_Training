import os
import shutil
import subprocess
import webbrowser
from datetime import datetime

def run_behave_with_allure():
    # Generate date and time for folder structure
    current_time = datetime.now()
    date_str = current_time.strftime("%Y-%m-%d")
    time_str = current_time.strftime("%I-%M-%S %p")
    result_dir = f"reports/{date_str}/{time_str}"
    allure_results = "reports/allure-results"

    # Clean previous allure results
    # ✅ SAFELY DELETE OLD ALLURE RESULTS (cross-platform)
    if os.path.exists(allure_results):
        shutil.rmtree(allure_results)

    # Step 1: Run Behave tests and generate Allure results
    print("[INFO] Running Behave tests...")
    behave_cmd  = [
        "behave", "--no-capture",
        "-f", "allure_behave.formatter:AllureFormatter",
        "-o", allure_results
    ]
    subprocess.run(behave_cmd, check=True)

    # Add Allure to PATH manually for PyCharm
    os.environ["PATH"] += os.pathsep + r"C:\allure-2.33.0\bin"

    # Detect allure
    allure_exe = shutil.which("allure")
    if not allure_exe:
        raise FileNotFoundError("❌ 'allure' command not found. Add Allure to PATH.")

    # Step 2: Generate the Allure HTML report
    print(f"[INFO] Generating Allure report at: {result_dir}")
    os.makedirs(result_dir, exist_ok=True)
    allure_cmd = [
        allure_exe, "generate", allure_results,
        "-o", result_dir,
        "--clean"
    ]
    subprocess.run(allure_cmd, check=True)

    print(f"✅ [SUCCESS] Report available at {result_dir}/index.html")

if __name__ == "__main__":
    try:
        report_path = run_behave_with_allure()
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Test execution failed: {e}")
