"""
Custom Logging Module


Provides colored console logging with different severity levels.
Uses ANSI escape codes for terminal color output.


Author: shahil-sk
Created: October 2025
Version: 1.0.0
"""


from enum import Enum
from datetime import datetime
from typing import Optional



class LogLevel(Enum):
    """Log level enumeration with associated colors and symbols."""
    DEBUG = ("d", "\033[95m", "[?]")      # Magenta
    ERROR = ("e", "\033[91m", "[#]")      # Red
    WARNING = ("w", "\033[93m", "[!]")    # Yellow
    SUCCESS = ("s", "\033[92m", "[^]")    # Green
    INFO = ("n", "\033[94m", "[*]")       # Blue
    DEFAULT = ("", "\033[97m", "[ ]")     # White



# ANSI color codes
class Colors:
    """ANSI escape codes for terminal colors."""
    RESET = "\033[00m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"



def xlog(msg: str, flag: Optional[str] = None, timestamp: bool = False, 
         bold: bool = False) -> None:
    """
    Print colored log messages to console.
    
    Args:
        msg (str): The message to log.
        flag (str, optional): Log level flag:
            - 'd': Debug (magenta)
            - 'e': Error (red)
            - 'w': Warning (yellow)
            - 's': Success (green)
            - 'n': Info (blue)
            - None: Default (white)
        timestamp (bool): Whether to include timestamp. Defaults to False.
        bold (bool): Whether to make text bold. Defaults to False.
    
    Returns:
        None
    """
    # Map flags to log levels
    flag_map = {
        "d": LogLevel.DEBUG,
        "e": LogLevel.ERROR,
        "w": LogLevel.WARNING,
        "s": LogLevel.SUCCESS,
        "n": LogLevel.INFO,
    }
    
    level = flag_map.get(flag, LogLevel.DEFAULT)
    color = level.value[1]
    symbol = level.value[2]
    
    # Build the log message
    prefix = f"{Colors.BOLD if bold else ''}{color}{symbol}{Colors.RESET}"
    
    if timestamp:
        time_str = datetime.now().strftime("%H:%M:%S")
        prefix = f"{color}[{time_str}]{Colors.RESET} {prefix}"
    
    formatted_msg = f"{color}{msg}{Colors.RESET}" if bold else msg
    
    print(f"{prefix} {formatted_msg}")



def xlog_error(msg: str, timestamp: bool = False) -> None:
    """Log error message in red."""
    xlog(msg, "e", timestamp)



def xlog_warning(msg: str, timestamp: bool = False) -> None:
    """Log warning message in yellow."""
    xlog(msg, "w", timestamp)



def xlog_success(msg: str, timestamp: bool = False) -> None:
    """Log success message in green."""
    xlog(msg, "s", timestamp)



def xlog_info(msg: str, timestamp: bool = False) -> None:
    """Log info message in blue."""
    xlog(msg, "n", timestamp)



def xlog_debug(msg: str, timestamp: bool = False) -> None:
    """Log debug message in magenta."""
    xlog(msg, "d", timestamp)



def xlog_header(msg: str) -> None:
    """Print a bold, underlined header."""
    print(f"\n{Colors.BOLD}{Colors.UNDERLINE}{msg}{Colors.RESET}\n")



def xlog_separator(char: str = "=", length: int = 50) -> None:
    """Print a separator line."""
    print(Colors.CYAN + char * length + Colors.RESET)



# Example usage
if __name__ == "__main__":
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