import tkinter as tk
import tkinter.messagebox
from login_form import LoginForm

font = ('Hellas Dust Cyrillic', 20)

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.btn = tk.Button(text="База хулиганов", font=font,
                             command=self.open_login)
        self.btn.pack(pady=20, padx=50)
        self.open_login()

    def open_login(self):
        login_form = LoginForm(self)
        post = login_form.open()
        if post:
            print("Login ok")
        else:
            tk.messagebox.showerror(title="Wrong login",
                                          message="Не верный логин или пароль"
                                          )
            self.open_login()


if __name__ == '__main__':
    root = MainWindow()
    root.title("Наша база")
    root.geometry('1600x800')
    root.mainloop()