try:
    with open("missing_file.csv", "r") as file:
        data = file.read()
except FileNotFoundError:
    with open("MISSING_FILE.csv", "r") as file:
            data = file.read()
finally:
     print("cleanup completed!")
