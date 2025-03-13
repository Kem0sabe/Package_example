try:
    with open("ctab_xtra_dp/README.md") as f:
        long_description = f.read()
        print(long_description)
except FileNotFoundError:
    print("README.md not found!")
    long_description = "Description not available"