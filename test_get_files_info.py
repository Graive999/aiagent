from functions.get_files_info import get_files_info



print("Test 1------")
print(get_files_info("calculator", "."))

print("Test 2------")
print(get_files_info("calculator", "pkg"))

print("Test 3------")
print(get_files_info("calculator", "/bin"))

print("Test 4------")
print(get_files_info("calculator", "../"))


