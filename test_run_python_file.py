from functions.run_python_file import run_python_file


print("--- Test 1: Help Menu ---")
print(run_python_file("calculator", "main.py"))


print("\n--- Test 2: 3 + 5 ---")
print(run_python_file("calculator", "main.py", ["3 + 5"]))

print("---calculator test---")
print(run_python_file("calculator", "tests.py"))

print("\n--- Test 3: Outside Sandbox ---")
print(run_python_file("calculator", "../main.py"))

print(run_python_file("calculator", "nonexistent.py"))

print(run_python_file("calculator", "lorem.txt"))