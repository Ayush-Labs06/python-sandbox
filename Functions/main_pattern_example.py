def greet(name="User"):
    return f"Hello, {name}"


def show_examples():
    # This function groups the demo code so it can be called only when needed.
    print(greet("Ayush"))
    print(greet())


# __name__ becomes "__main__" only when this file is run directly.
# That is why show_examples() runs with:
# python3 Functions/main_pattern_example.py
#
# If another file imports this file, this block does not run automatically.
# This is useful when you want to reuse greet() without extra print output.
if __name__ == "__main__":
    show_examples()
