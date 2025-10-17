


import os
import shutil
import subprocess
import tempfile
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

# ---------------- GUI FUNCTIONS ----------------

def select_project():
    directory = filedialog.askdirectory(title="Select Python Project Directory")
    if directory:
        project_path.set(directory)

def build_apk():
    directory = project_path.get()
    if not directory:
        messagebox.showerror("Error", "Please select a project directory first.")
        return

    app_name = app_name_var.get().strip() or "MyApp"
    version = app_version_var.get().strip() or "1.0"
    log_box.delete(1.0, tk.END)
    log_box.insert(tk.END, f"Preparing to build APK for: {app_name} (v{version})\n")

    # Create temporary workspace
    workspace = tempfile.mkdtemp(prefix="buildozer_")
    app_dir = os.path.join(workspace, "app")
    shutil.copytree(directory, app_dir, dirs_exist_ok=True)

    log_box.insert(tk.END, f"Copied project to workspace: {workspace}\n")

    # Create or modify buildozer.spec
    spec_path = os.path.join(app_dir, "buildozer.spec")
    if not os.path.exists(spec_path):
        spec_content = f"""[app]
title = {app_name}
package.name = {app_name.lower()}
package.domain = org.example
source.dir = .
version = {version}
requirements = python3,kivy
orientation = portrait
"""
        with open(spec_path, "w", encoding="utf-8") as f:
            f.write(spec_content)
        log_box.insert(tk.END, "Created new buildozer.spec file.\n")
    else:
        log_box.insert(tk.END, "Using existing buildozer.spec file.\n")

    # Start build process in background
    threading.Thread(target=run_buildozer, args=(app_dir,), daemon=True).start()


def run_buildozer(app_dir):
    log_box.insert(tk.END, "Starting Buildozer build process...\n")
    log_box.see(tk.END)
    try:
        process = subprocess.Popen(
            ["buildozer", "android", "debug"],
            cwd=app_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )

        for line in process.stdout:
            log_box.insert(tk.END, line)
            log_box.see(tk.END)

        process.wait()
        if process.returncode == 0:
            log_box.insert(tk.END, "\n✅ APK build completed successfully!\n")
            messagebox.showinfo("Success", "APK built successfully! Check 'bin/' inside your project.")
        else:
            log_box.insert(tk.END, "\n❌ Build failed. Check logs above.\n")
            messagebox.showerror("Error", "Build failed. Please review the log output.")

    except Exception as e:
        log_box.insert(tk.END, f"\nError: {e}\n")
        messagebox.showerror("Error", str(e))

# ---------------- GUI DESIGN ----------------

root = tk.Tk()
root.title("Python to APK Converter")
root.geometry("650x500")
root.configure(bg="#101820")

title_label = tk.Label(
    root, text="Python ➜ APK Converter", 
    fg="white", bg="#101820", font=("Arial", 18, "bold")
)
title_label.pack(pady=10)

# --- App Name ---
app_name_var = tk.StringVar(value="MyApp")
tk.Label(root, text="App Name:", bg="#101820", fg="white", font=("Arial", 12, "bold")).pack()
app_name_entry = tk.Entry(root, textvariable=app_name_var, font=("Arial", 12))
app_name_entry.pack(pady=5)

# --- App Version ---
app_version_var = tk.StringVar(value="1.0")
tk.Label(root, text="App Version:", bg="#101820", fg="orange", font=("Arial", 12, "bold")).pack()
app_version_entry = tk.Entry(root, textvariable=app_version_var, font=("Arial", 12))
app_version_entry.pack(pady=5)

# --- Project Directory Selection ---
project_path = tk.StringVar()
select_button = tk.Button(
    root, text="Select Project Directory",
    bg="blue", fg="white", font=("Arial", 12, "bold"),
    command=select_project
)
select_button.pack(pady=10)

tk.Entry(root, textvariable=project_path, width=60, font=("Arial", 10)).pack(pady=5)

# --- Build Button ---
build_button = tk.Button(
    root, text="Convert to APK",
    bg="green", fg="white", font=("Arial", 14, "bold"),
    command=build_apk
)
build_button.pack(pady=10)

# --- Log Box ---
log_box = scrolledtext.ScrolledText(root, width=80, height=15, bg="#0D1B2A", fg="white", font=("Consolas", 10))
log_box.pack(padx=10, pady=10)

# --- Footer ---
footer_label = tk.Label(
    root, text="Powered by Shahmeer",
    bg="#101820", fg="cyan", font=("Arial", 10, "italic")
)
footer_label.pack(side="bottom", pady=5)

root.mainloop()



