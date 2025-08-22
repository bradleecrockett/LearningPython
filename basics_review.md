# **Python Basics and Conditionals Study Guide** 

This guide covers the fundamental concepts of Python 3 programming needed to understand and predict the outcomes of simple scripts.

Take the time to compare your predictions with a partner, then execute them in IDLE or a python program to confirm your prediction.

More detailed explanations are outlined in chapter 2 and 3 of the textbook: [Python for Everyone](https://books.trinket.io/pfe)

-----

### **1. Variables and Data Types**

A **variable** is a name used to store a value. Python automatically determines the data type based on the value assigned.

  * **`int`**: Integer, a whole number (e.g., `10`, `-5`).
  * **`float`**: A number with a decimal point (e.g., `3.14`, `-0.5`).
  * **`str`**: String, a sequence of characters in quotes (e.g., `"Hello"`, `'Python'`).
  * **`bool`**: Boolean, either `True` or `False`.

**Practice Question:**
What is the data type of the variable `result` after the following code is executed?

```python
w = 30
x = 5
y = "4"
z = 6.2
print( type(w) )    # prediction
print( type(x) )    # prediction
print( type(y) )    # prediction
print( type(z) )    # prediction
print(x * y)    # prediction
print(x * z)    # prediction
print(w / x)    # prediction
print(w > z)    # prediction
```

-----

### **2. Arithmetic and Relational Operators**

**Arithmetic operators** perform mathematical calculations. Python follows the standard order of operations (PEMDAS/BODMAS).

  * **`+`**, **`-`**, **`*`**, **`/`**: Addition, subtraction, multiplication, division.
  * **`%`** (Modulus): Returns the remainder of a division (e.g., `10 % 3` is `1`).
  * **`//`** (Floor Division): Divides and rounds down to the nearest whole number (e.g., `10 // 3` is `3`).

**Relational operators** compare values and return a boolean (`True` or `False`).

  * **`==`**: Equal to
  * **`!=`**: Not equal to
  * **`>`**, **`<`**, **`>=`**, **`<=`**: Greater than, less than, etc.

**Practice Question:**
What will be the output of the following expression?

```python
print(15 % 4 + 2 * 3)   # prediction
print(20 + 40 / 2 * 5)  # prediction
print(25 // 4 + 3 ** 3) # prediction
print(25 // 4 > 30 % 6) # prediction
print(20 / 4 != 20 // 4) # prediction
```

-----

### **3. Conditional Execution**

Conditional statements control the flow of a program based on whether a condition is true.

  * **`if`**: Executes the code block only if its condition is `True`.
  * **`elif`** (else if): Checks its condition only if the preceding `if` and `elif` statements were `False`.
  * **`else`**: Executes its code block if all preceding `if` and `elif` conditions were `False`.

**Key Point 1:** In an `if`/`elif`/`else` structure, only *one* block of code will ever be executed.

**Key Point 2:** In a series of `if` structures, only one, some, all or none of the blocks of code may be executed.

**Practice Question:**
What will the following code print to the console?

```python
width = 40

if width > 50:
    print("small")
elif width > 20:
    print("large")
elif width % 10 == 0:
    print("multiple of ten")
else:
    print("Error")
```

```python
rate = 16.25
hours = 10

if hours > 30:
    print("full time")
if rate < 10:
    print("low pay")
print("climb the ladder")
if hours == 10:
    print("student")
if rate > 20:
    print("good money")
if rate * hours > 100:
    print("going shopping")
else:
    print("work more")

```

```python
num = 42  # Next try 40, then try 25
if num > 30:
    if num % 5 == 0:
        print("Nice")
    print("Try")
else:
    print("Fly")
    num = num // 6
    if num <  5:
        print("Guy")
    else:
        print("Sigh")

```


---
### 4. User `input()`

The `input()` function in Python allows a user of a program to enter data using the keyboard. All data returned by the `input()` function is string data `<class str>`.

If the user is entering numerical data it likely needs to be converted from a string to a numerical data type `int` or `float`. This can be accomplished usiong the `float()` or `int()` functions.

Similarily there is a `str()` function that will convert any data types to `str` data.

