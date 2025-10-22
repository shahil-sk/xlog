<center><img width="487" height="337" alt="Screenshot From 2025-10-22 19-22-23 (Copy)" src="https://github.com/user-attachments/assets/9f5a05b2-327f-42fb-bc7b-ce8b43d71dfc" /></center>


# XLog (Custom Colored Logging for Python)

**XLog** is a lightweight, dependency-free Python logging utility that brings color, clarity, and structure to your console output.
It supports multiple log levels, timestamps, and bold formatting — all with simple function calls.


## Features

*  **Color-coded log levels** (Error, Warning, Info, Success, Debug)
*  **Optional timestamps** for better traceability
*  **Bold and underlined headers** for section breaks
*  **Lightweight** — no external dependencies
*  **Custom separators** for clean console organization


## 🧠 Log Levels

| Flag | Level   | Color   | Symbol | Example Usage                          |
| ---- | ------- | ------- | ------ | -------------------------------------- |
| `d`  | Debug   | Magenta | `[?]`  | `xlog("Debug info", "d")`              |
| `e`  | Error   | Red     | `[#]`  | `xlog_error("Something failed")`       |
| `w`  | Warning | Yellow  | `[!]`  | `xlog_warning("Be careful!")`          |
| `s`  | Success | Green   | `[^]`  | `xlog_success("Operation completed!")` |
| `n`  | Info    | Blue    | `[*]`  | `xlog_info("Just so you know...")`     |
| —    | Default | White   | `[ ]`  | `xlog("Default message")`              |

<br>

## 📦 Installation

No setup needed — just drop the file into your project.

```bash
xlog.py Or git clone https://github.com/shahil-sk/xlog.git
```

Then import it in your code:

```python
from xlog import *
```
---

## 🚀 Quick Start

```python
from xlog import *

xlog_header("XLog Demo")

xlog_error("This is an error message")
xlog_warning("This is a warning message")
xlog_success("This is a success message")
xlog_info("This is an info message")
xlog_debug("This is a debug message")
xlog("This is a default message")

xlog_separator()

# With timestamps
xlog_error("Error with timestamp", timestamp=True)
xlog_success("Success with timestamp", timestamp=True)

xlog_separator()

# Bold text
xlog("Bold important message", "s", bold=True)
```


## ⚙️ Function Reference

| Function                                            | Description                                                          |
| --------------------------------------------------- | -------------------------------------------------------------------- |
| `xlog(msg, flag=None, timestamp=False, bold=False)` | Main logging function with custom flag, timestamp, and bold options. |
| `xlog_error(msg, timestamp=False)`                  | Log red error messages.                                              |
| `xlog_warning(msg, timestamp=False)`                | Log yellow warning messages.                                         |
| `xlog_success(msg, timestamp=False)`                | Log green success messages.                                          |
| `xlog_info(msg, timestamp=False)`                   | Log blue info messages.                                              |
| `xlog_debug(msg, timestamp=False)`                  | Log magenta debug messages.                                          |
| `xlog_header(msg)`                                  | Print a bold, underlined section header.                             |
| `xlog_separator(char="=", length=50)`               | Print a colored separator line.                                      |

<br>
## Example Output

<img width="428" height="226" alt="Screenshot From 2025-10-22 19-32-08" src="https://github.com/user-attachments/assets/700e6021-adfa-4281-9883-b4012c96dc1c" />


## 🧑‍💻 Author

**shahil-sk**
 *Created: October 2025*
 *Version: 1.0.0*


## 🪪 License

This project is licensed under the **MIT License** — free for personal and commercial use.
