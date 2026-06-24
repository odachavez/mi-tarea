import tkinter as tk
from tkinter import messagebox
from controller.soccer_team_controller import SoccerTeamController

class CreateTeamView:

    def __init__(self, root):
        self.controller = SoccerTeamController()

        root.title("Register New Soccer Team")
        root.geometry("400x300")

        tk.Label(root, text="Team ID").pack()
        self.txt_id = tk.Entry(root)
        self.txt_id.pack()

        tk.Label(root, text="Team Name").pack()
        self.txt_name = tk.Entry(root)
        self.txt_name.pack()

        tk.Label(root, text="Matches Won").pack()
        self.txt_won = tk.Entry(root)
        self.txt_won.pack()

        tk.Label(root, text="Matches Drawn").pack()
        self.txt_drawn = tk.Entry(root)
        self.txt_drawn.pack()

        btn_save = tk.Button(root, text="SAVE TEAM",
                             command=self.handle_save_button_click)
        btn_save.pack(pady=10)

    def handle_save_button_click(self):
        try:
            team_id = int(self.txt_id.get())
            name = self.txt_name.get()
            won = int(self.txt_won.get())
            drawn = int(self.txt_drawn.get())

            self.controller.save_team(team_id, name, won, drawn)

            points = (won * 3) + drawn

            messagebox.showinfo(
                "Success",
                f"Team saved successfully!\nPoints: {points}"
            )

        except ValueError:
            messagebox.showerror(
                "Error",
                "ID, Matches Won and Matches Drawn must be numbers."
            )

root = tk.Tk()
app = CreateTeamView(root)
root.mainloop()