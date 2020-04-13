import subprocess
subprocess.call(["ls"])
subprocess.call(["touch", "sample.txt"])
subprocess.call(["ls"])
print("Sample file created")
subprocess.call(["rm", "sample.txt"])
subprocess.call(["ls"])
print("Sample file deleted")
