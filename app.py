import customtkinter as ctk
from modules.logic import compute_derivative, compute_integral
from modules.plotter import plot_function_and_derivative
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pygame

# Inisialisasi pygame untuk efek suara
pygame.init()
click_sound = pygame.mixer.Sound("click_pop.mp3")  # Letakkan file ini di folder yang sama

# Mode terang dan tema warna ceria
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Setup aplikasi
app = ctk.CTk()
app.title("CalcULife – By Muhamad Aziz Nur Wahid (312410040)")
app.geometry("800x600")
app.configure(bg="#ffffff")  # latar putih

def play_click():
    click_sound.play()

def calculate():
    play_click()
    expr = entry.get()
    method = method_var.get()
    a = lower_bound.get()
    b = upper_bound.get()

    if method == "Turunan":
        result = compute_derivative(expr)
        result_label.configure(text=f"Turunan: {result}")
        plot_function_and_derivative(expr, ax)
    elif method == "Integral":
        if a and b:
            result = compute_integral(expr, a=float(a), b=float(b))
        else:
            result = compute_integral(expr)
        result_label.configure(text=f"Integral: {result}")
        plot_function_and_derivative(expr, ax)

    canvas.draw()

def reset():
    play_click()
    entry.delete(0, 'end')
    lower_bound.delete(0, 'end')
    upper_bound.delete(0, 'end')
    result_label.configure(text="")
    ax.clear()
    canvas.draw()

def toggle_mode(choice):
    ctk.set_appearance_mode(choice)
    if choice == "Light":
        app.configure(bg="#ffffff")
        frame.configure(fg_color="#ffffff")
        result_label.configure(text_color="#000000")
        footer.configure(text_color="#000000")
    else:
        app.configure(bg="#121212")
        frame.configure(fg_color="#1e1e1e")
        result_label.configure(text_color="#ffffff")
        footer.configure(text_color="#cccccc")

# UI Frame
frame = ctk.CTkFrame(app, fg_color="#ffffff", corner_radius=12)
frame.pack(pady=20)

entry = ctk.CTkEntry(frame, width=400, placeholder_text="Masukkan fungsi aljabar (misal: x**2 + 3*x + 2)", font=("Comic sans", 14))
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

method_var = ctk.StringVar(value="Turunan")
method_dropdown = ctk.CTkOptionMenu(frame, values=["Turunan", "Integral"], variable=method_var, width=120, font=("Comic sans", 12), fg_color="#38b6ff", button_color="#FFC400", button_hover_color="#38b6ff", text_color="#000000")
method_dropdown.grid(row=1, column=0, padx=10)

lower_bound = ctk.CTkEntry(frame, width=100, placeholder_text="Batas bawah", font=("Comic sans", 12))
lower_bound.grid(row=1, column=1, padx=5)

upper_bound = ctk.CTkEntry(frame, width=100, placeholder_text="Batas atas", font=("Comic sans", 12))
upper_bound.grid(row=1, column=2, padx=5)

calc_button = ctk.CTkButton(frame, text="Hitung", command=calculate, fg_color="#38b6ff", hover_color="#FFC400", text_color="#000000", font=("Comic sans", 13))
calc_button.grid(row=2, column=0, pady=10)

reset_button = ctk.CTkButton(frame, text="Reset", command=reset, fg_color="#FFC400", hover_color="#38b6ff", text_color="#FFFFFF", font=("Comic sans", 13))
reset_button.grid(row=2, column=1, columnspan=2, pady=10)

# Dropdown Mode Light/Dark
mode_label = ctk.CTkLabel(app, text="Mode Tampilan:", font=("Comic sans", 12), text_color="#000000")
mode_label.pack(pady=(5, 0))

mode_var = ctk.StringVar(value="Light")
mode_dropdown = ctk.CTkOptionMenu(app, values=["Light", "Dark"], variable=mode_var, command=toggle_mode, width=100, fg_color="#38b6ff", button_color="#FFC400", text_color="#000000")
mode_dropdown.pack()

# Label hasil
result_label = ctk.CTkLabel(app, text="", font=("Comic sans", 16), text_color="#000000")
result_label.pack(pady=10)

# Plot canvas (diperbesar)
fig, ax = plt.subplots(figsize=(7, 4.5), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=app)
canvas.get_tk_widget().pack(pady=(0, 10), fill='x', expand=False)

# Jalankan aplikasi
app.mainloop()
