# Python Version Checker Exercise

This is a simple Python program that checks and displays the version of Python you are currently using. It’s a beginner-friendly exercise to help you get familiar with Python's `sys` module and basic scripting.

---

## Table of Contents
- [About](#about)
- [How It Works](#how-it-works)
- [How to Run](#how-to-run)
- [Example Output](#example-output)
- [Contributing](#contributing)
- [License](#license)

---

## About

This exercise demonstrates how to use Python's built-in `sys` module to retrieve and display the version of Python installed on your system. It’s a great starting point for beginners to understand how to interact with system-specific information in Python.

---

## How It Works

The program uses the `sys` module, which provides access to system-specific parameters and functions. Specifically:
- `sys.version_info` returns a tuple containing the major, minor, and micro version numbers of Python.
- The program formats and prints this information in a user-friendly way.

---

## How to Run

1. Save the code in a file, e.g., `python_version_checker.py`.
2. Run the script using your Python interpreter:
   ```bash
   python python_version_checker.py
   ```

---

## Example Output

If you’re using Python 3.10.12, the output will look like this:
```
You are using Python 3.10.12
```

Alternatively, if you print the full version string using `sys.version`, the output might look like this:
```
You are using Python 3.10.12 (main, Oct  3 2023, 12:00:00) [GCC 9.4.0]
```

---

## Contributing

Contributions are welcome! If you’d like to improve this exercise or add more features, feel free to:
1. Fork the repository.
2. Create a new branch for your changes.
3. Submit a pull request with your improvements.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Happy coding! 🐍