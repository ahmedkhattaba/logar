import datetime
from colorama import init, Fore, Style
init()
class Logar:
    """Simple colored logging module for python"""
    _RESET = Style.RESET_ALL

    _COLORS = {
        "default": Fore.RESET,
        "success": Fore.GREEN,
        "error": Fore.RED,
        "warning": Fore.YELLOW,
        "info": Fore.BLUE
    }

    def _log(self, level, message):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        color = self._COLORS.get(level, "")
        print(f"{color} [{level.upper()}] {message} [{now}] {self._RESET}")
    
    def default(self, message) -> None:
        self._log("default", message)

    def success(self, message) -> None:
        """Log a success message"""
        self._log("success", message)
    
    def error(self, message) -> None:
        """Log an error message"""
        self._log("error", message)

    def warning(self, message) -> None:
        """Log a warning message"""
        self._log("warning", message)
    
    def info(self, message) -> None:
        """Log an info message"""
        self._log("info", message)