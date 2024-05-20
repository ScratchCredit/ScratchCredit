"""
ScratchCredit Debugging Module: Debug Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

from scratchattach.session import Session

# XXX This class is only used during development, so... :/
class DebugMode:
    def __init__(self, debug_mode: bool, session: Session):
        self.debug_mode = debug_mode
        self.session = session
        self.ban_message = f"Unfortunately, {self.session._username} is banned. \033[1mThis means that ScratchCredit won't work properly.\033[0m"
        self.not_banned_message = f"Fortunately, {self.session._username} isn't banned."
        self.new_scratcher_message = f"{self.session._username} is a \033[1mNew Scratcher\033[0m. \033[1mThis means that ScratchCredit won't work properly.\033[0m"
        self.scratcher_message = f"{self.session._username} is a \033[1mScratcher\033[0m."
    def print_if_debug_mode_is_enabled(self):
        if self.debug_mode:
            print(f"\033[1mDEBUG MODE ENABLED.\n\033[0mUsername: {self.session._username}\nBanned?: {self.ban_message if self.session.banned else self.not_banned_message}\nIs {self.session._username} a \033[1mNew Scratcher\033[0m or a \033[1mScratcher\033[0m?: {self.new_scratcher_message if self.session.new_scratcher else self.scratcher_message}\nScratch user URL: https://scratch.mit.edu/users/{self.session._username}/")
