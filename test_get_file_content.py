from functions.get_file_content import get_file_content

def main():


        
    print("Test 1------")
    res = get_file_content("calculator", "lorem.txt")
    print(f"Lorem length: {len(res)}")
    if "truncated" in res:
        print("Success: File was truncated properly!")

    print("Test 2------")
    print(get_file_content("calculator", "main.py"))

    print("Test 3------")
    print(get_file_content("calculator", "pkg/calculator.py"))
    
    print("Test 4------")
    print(get_file_content("calculator", "/bin/cat"))

    print("Test 5------")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))


if __name__ == "__main__":
    main()       