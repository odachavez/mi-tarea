import tkinter as tk
from view.create_team_view import CreateTeamView

def main():
    root = tk.Tk()
    CreateTeamView(root)
    root.mainloop()

if __name__ == "__main__":
    main()