import keyboard
import mouse
import time
import tkinter as tk
import webbrowser
import threading
from pynput import keyboard as pynput_keyboard
from pynput.keyboard import Key, KeyCode

# Zmienne globalne
macro_running = True
animation_running = True
macro_executing = False

def execute_macro():
    """Wykonuje sekwencję akcji po naciśnięciu 'r'"""
    global macro_executing
    
    if not macro_running or macro_executing:
        return
    
    macro_executing = True
    
    try:
        # Balans między szybkością a działaniem
        water_delay = 0.05
        slot_delay = 0.07
        web_delay = 0.1
        
        # 1. Wiadro + woda
        keyboard.press_and_release('c')
        time.sleep(slot_delay)
        
        mouse.click(button='right')
        time.sleep(water_delay)
        mouse.click(button='right')
        time.sleep(water_delay)
        
        # Poczekaj aż woda zniknie
        time.sleep(0.06)
        
        # 2. Web - DŁUŻEJ
        keyboard.press_and_release('6')
        time.sleep(web_delay)
        
        # Klik na web
        mouse.click(button='right')
        
        time.sleep(0.05)
        
        # 3. Slot 1
        keyboard.press_and_release('1')
        
        flash_effect()
        update_status("R executed", "#a855f7")
    finally:
        time.sleep(0.3)
        macro_executing = False

def execute_macro_v():
    """Wykonuje sekwencję akcji po naciśnięciu 'v'"""
    global macro_executing
    
    if not macro_running or macro_executing:
        return
    
    macro_executing = True
    
    try:
        water_delay = 0.08
        slot_delay = 0.08
        
        keyboard.press_and_release('c')
        time.sleep(slot_delay)
        
        mouse.click(button='right')
        time.sleep(water_delay)
        mouse.click(button='right')
        time.sleep(water_delay)
        
        keyboard.press_and_release('x')
        time.sleep(slot_delay)
        
        mouse.click(button='right')
        
        time.sleep(0.03)
        
        keyboard.press_and_release('1')
        
        flash_effect()
        update_status("V executed", "#a855f7")
    finally:
        time.sleep(0.1)  # Cooldown
        macro_executing = False

def flash_effect():
    """Flash effect przy wykonaniu makra"""
    try:
        status_label.config(fg="#ffffff")
        root.after(100, lambda: status_label.config(fg="#a855f7"))
    except:
        pass

def rainbow_logo():
    """Rainbow animation dla logo"""
    if not animation_running:
        return
    
    try:
        colors = ["#a855f7", "#ec4899", "#f43f5e", "#f97316", "#eab308", "#22c55e", "#06b6d4", "#3b82f6", "#8b5cf6"]
        current = getattr(rainbow_logo, 'index', 0)
        
        logo_j.config(fg=colors[current % len(colors)])
        logo_u.config(fg=colors[(current + 1) % len(colors)])
        logo_d.config(fg=colors[(current + 2) % len(colors)])
        logo_a.config(fg=colors[(current + 3) % len(colors)])
        logo_s.config(fg=colors[(current + 4) % len(colors)])
        
        rainbow_logo.index = (current + 1) % len(colors)
        root.after(200, rainbow_logo)
    except:
        pass

def update_status(text, color="#e2e8f0"):
    """Aktualizuje status w GUI"""
    try:
        status_label.config(text=text, foreground=color)
    except:
        pass

def toggle_macro():
    """Włącza/wyłącza makro"""
    global macro_running
    macro_running = not macro_running
    
    if macro_running:
        toggle_btn.config(text="● ACTIVE", bg="#22c55e", activebackground="#16a34a")
        status_label.config(text="Active", foreground="#22c55e")
    else:
        toggle_btn.config(text="○ INACTIVE", bg="#ef4444", activebackground="#dc2626")
        status_label.config(text="Inactive", foreground="#ef4444")

def open_discord():
    """Otwiera link do Discorda - Judas"""
    webbrowser.open("https://discord.gg/EcVJytEh")
    discord_btn.config(text="OPENING...", bg="#4752c4")
    root.after(1000, lambda: discord_btn.config(text="JUDAS DISCORD", bg="#5865f2"))

def on_press(key):
    """Handler dla klawiszy - używa virtual key codes (działa z Shift/Ctrl)"""
    try:
        if isinstance(key, KeyCode) and key.vk:
            # R = 82, V = 86 (virtual key codes - działają niezależnie od Shift/Ctrl)
            if key.vk == 82 and macro_running and not macro_executing:
                threading.Thread(target=execute_macro, daemon=True).start()
            elif key.vk == 86 and macro_running and not macro_executing:
                threading.Thread(target=execute_macro_v, daemon=True).start()
    except:
        pass

def start_pynput_listener():
    """Uruchamia listener pynput - działa zawsze"""
    listener = pynput_keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()

# GUI
root = tk.Tk()
root.title("Judas Nemos Killer")
root.geometry("420x600")
root.configure(bg="#0a0a0f")
root.resizable(False, False)

# Container
main = tk.Frame(root, bg="#0a0a0f")
main.pack(fill="both", expand=True, padx=25, pady=25)

# Logo - tylko litery JUDAS
logo_container = tk.Frame(main, bg="#0a0a0f")
logo_container.pack(pady=(0, 15))

logo_text_frame = tk.Frame(logo_container, bg="#0a0a0f")
logo_text_frame.pack()

logo_j = tk.Label(logo_text_frame, text="J", font=("Arial Black", 28, "bold"), bg="#0a0a0f", fg="#a855f7")
logo_j.pack(side="left", padx=2)

logo_u = tk.Label(logo_text_frame, text="U", font=("Arial Black", 28, "bold"), bg="#0a0a0f", fg="#a855f7")
logo_u.pack(side="left", padx=2)

logo_d = tk.Label(logo_text_frame, text="D", font=("Arial Black", 28, "bold"), bg="#0a0a0f", fg="#a855f7")
logo_d.pack(side="left", padx=2)

logo_a = tk.Label(logo_text_frame, text="A", font=("Arial Black", 28, "bold"), bg="#0a0a0f", fg="#a855f7")
logo_a.pack(side="left", padx=2)

logo_s = tk.Label(logo_text_frame, text="S", font=("Arial Black", 28, "bold"), bg="#0a0a0f", fg="#a855f7")
logo_s.pack(side="left", padx=2)

# Title
tk.Label(
    main,
    text="NEMOS KILLER",
    font=("Segoe UI", 26, "bold"),
    bg="#0a0a0f",
    fg="#ffffff"
).pack(pady=(0, 20))

# Status
status_box = tk.Frame(main, bg="#13131a", highlightthickness=1, highlightbackground="#1e1e28")
status_box.pack(fill="x", pady=(0, 20))

status_inner = tk.Frame(status_box, bg="#13131a")
status_inner.pack(pady=18)

tk.Label(status_inner, text="STATUS:", font=("Segoe UI", 10, "bold"), bg="#13131a", fg="#64748b").pack(side="left", padx=(0, 10))
status_label = tk.Label(status_inner, text="Active", font=("Segoe UI", 12, "bold"), bg="#13131a", fg="#22c55e")
status_label.pack(side="left")

# Keybinds
keys_box = tk.Frame(main, bg="#13131a", highlightthickness=1, highlightbackground="#1e1e28")
keys_box.pack(fill="x", pady=(0, 20))

tk.Label(keys_box, text="KEYBINDS", font=("Segoe UI", 9, "bold"), bg="#13131a", fg="#64748b").pack(anchor="w", padx=20, pady=(15, 10))

r_row = tk.Frame(keys_box, bg="#13131a")
r_row.pack(fill="x", padx=20, pady=8)
tk.Label(r_row, text="R", font=("Segoe UI", 11, "bold"), bg="#1e1e28", fg="#a855f7", width=3, padx=6, pady=3).pack(side="left", padx=(0, 12))
tk.Label(r_row, text="Full Sequence", font=("Segoe UI", 10), bg="#13131a", fg="#cbd5e1").pack(side="left")

v_row = tk.Frame(keys_box, bg="#13131a")
v_row.pack(fill="x", padx=20, pady=(8, 15))
tk.Label(v_row, text="V", font=("Segoe UI", 11, "bold"), bg="#1e1e28", fg="#a855f7", width=3, padx=6, pady=3).pack(side="left", padx=(0, 12))
tk.Label(v_row, text="Quick Sequence", font=("Segoe UI", 10), bg="#13131a", fg="#cbd5e1").pack(side="left")

# Buttons
toggle_btn = tk.Button(
    main,
    text="● ACTIVE",
    font=("Segoe UI", 11, "bold"),
    bg="#22c55e",
    fg="white",
    activebackground="#16a34a",
    activeforeground="white",
    command=toggle_macro,
    relief="flat",
    cursor="hand2",
    pady=12
)
toggle_btn.pack(fill="x", pady=(0, 10))

discord_btn = tk.Button(
    main,
    text="JUDAS DISCORD",
    font=("Segoe UI", 11, "bold"),
    bg="#5865f2",
    fg="white",
    activebackground="#4752c4",
    activeforeground="white",
    command=open_discord,
    relief="flat",
    cursor="hand2",
    pady=12
)
discord_btn.pack(fill="x")

# Footer
tk.Label(main, text="Made with 💜 by Judas", font=("Segoe UI", 9), bg="#0a0a0f", fg="#475569").pack(side="bottom", pady=(15, 0))

# Start listener z pynput (działa ZAWSZE)
listener_thread = threading.Thread(target=start_pynput_listener, daemon=True)
listener_thread.start()

# Start animations
rainbow_logo()

# Auto open Discord
webbrowser.open("https://discord.gg/EcVJytEh")

root.mainloop()
