import json
import threading
import webbrowser
import dearpygui.dearpygui as dpg
from datetime import datetime, timezone

# from secret.doNotPush import *
# from autokattis import Kattis
import pyperclip

import time
import random
from datetime import datetime, timedelta
import kattisProblemExplorerFolder.themes.themesFile as themes
import kattisProblemExplorerFolder.pages.menuBar as menuBar
import kattisProblemExplorerFolder.pages.problemList as problemList
import kattisProblemExplorerFolder.pages.problemView as problemView


def main():
    dpg.create_context()

    dpg.bind_theme(themes.create_theme_gpt_theme())

    # pages.download_csv.createPage((0, 0), 420, 700, db, clientList)
    problemList.createPage((0, 0), 880, 700, [])
    problemView.createPage((880, 0), 580, 700, [])

    # Set up the viewport
    dpg.create_viewport(title="Kattis Problems Explorer V0.0.1", width=1300, height=800)

    menuBar.menuBar()
    # Show the viewport
    dpg.setup_dearpygui()
    dpg.show_viewport()

    # Run the application
    dpg.start_dearpygui()

    # Clean up
    dpg.destroy_context()


if __name__ == "__main__":
    main()
