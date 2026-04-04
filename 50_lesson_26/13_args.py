import sys

if len(sys.argv) > 1:
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"Аргумент {i}: {arg}")
else:
    print("Аргументы не переданы.")
