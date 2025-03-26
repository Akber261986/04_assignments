# Countdown for launch a 🚀

This is a simple Python script that implements a countdown timer using both a `for` loop and a `while` loop.

## Features

- Counts down from 10 to 1
- Prints each number with a 1-second delay
- Displays "Lift Off" when the countdown reaches zero
- Uses both `for` and `while` loops (only one is executed at a time)

## How to Use

1. Clone or download the script.
2. Ensure you have Python installed on your system.
3. Open a terminal and navigate to the script's directory.
4. Run the script using the command:
   ```bash
   python main.py
   ```
5. just comment out the first function and uncomment the second one.
6. run the script using command:
   ```bash
   python main.py
   ```


## Code Explanation

- The script defines a `main()` function that performs the countdown.
- The `for` loop version decrements a counter and prints each step with a 1-second delay.
- The `while` loop version does the same but is commented out by default.
- You can uncomment the `while` loop section and comment out the `for` loop section to use the alternative approach.

## Example Output

```
10
9
8
7
6
5
4
3
2
1
Lift Off
```

## Notes

- The script uses `time.sleep(1)` to create a delay of 1 second between each countdown step.
- Only one loop (either `for` or `while`) should be active at a time.
- The script includes a `main()` function call to ensure proper execution.

## Author

- **Ghulam Akber**

Happy coding! 🚀

