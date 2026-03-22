import tkinter as tk
from tkinter import scrolledtext
from filesystem import Folder, File
from storage import save_vfs

class TerminalGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Linux Terminal Simulator")
        self.root.geometry("750x500")
        self.root.configure(bg="black")

        # --- INISIALISASI VFS (Virtual File System) ---
        self.vfs_root = Folder("/")
        self.current_dir = self.vfs_root
        
        # Buat manual otomatis
        manual_content = """
    === RUMUS LINUX TERMINAL ===
    ls    : Lihat isi folder
    cd    : Pindah folder (cd .. untuk keluar)
    mkdir : Buat folder baru
    touch : Buat file baru
    cat   : Baca isi file
    save  : Simpan sistem ke JSON
    clear : Bersihkan layar terminal
    exit  : Keluar aplikasi
        """
        self.vfs_root.add_file("manual.txt", manual_content)

        # --- SETUP GUI ---
        # Area Output (Layar Terminal)
        self.output_area = scrolledtext.ScrolledText(root, bg="black", fg="#00FF00", font=("Consolas", 12), bd=0)
        self.output_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.output_area.config(state=tk.DISABLED) # Kunci agar user tidak bisa ketik bebas di sini

        # Frame Input (Bawah)
        self.input_frame = tk.Frame(root, bg="black")
        self.input_frame.pack(fill=tk.X, padx=10, pady=(0, 10))

        # Teks Prompt (rayan@simulator:/$)
        self.prompt_label = tk.Label(self.input_frame, text="rayan@simulator:/$ ", bg="black", fg="#00FF00", font=("Consolas", 12))
        self.prompt_label.pack(side=tk.LEFT)

        # Kotak Input Perintah
        self.cmd_input = tk.Entry(self.input_frame, bg="black", fg="#00FF00", font=("Consolas", 12), insertbackground="white", relief=tk.FLAT)
        self.cmd_input.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.cmd_input.bind("<Return>", self.process_command) # Eksekusi saat tekan ENTER
        self.cmd_input.focus()

        # Pesan Pembuka
        self.print_text("--- LINUX TERMINAL SIMULATOR ---\nKetik 'cat manual.txt' untuk melihat daftar rumus.\n")

    def print_text(self, text):
        """Fungsi pembantu untuk mencetak teks ke layar terminal"""
        self.output_area.config(state=tk.NORMAL)
        self.output_area.insert(tk.END, text + "\n")
        self.output_area.see(tk.END) # Auto-scroll ke bawah
        self.output_area.config(state=tk.DISABLED)

    def update_prompt(self):
        """Fungsi untuk mengupdate tulisan path di kiri input box"""
        path_str = self.current_dir.name if self.current_dir == self.vfs_root else f"/{self.current_dir.name}"
        self.prompt_label.config(text=f"rayan@simulator:{path_str}$ ")

    def process_command(self, event):
        """Logika saat user menekan ENTER"""
        raw_cmd = self.cmd_input.get().strip()
        self.cmd_input.delete(0, tk.END)

        # Cetak perintah yang baru diketik ke layar atas
        prompt = self.prompt_label.cget("text")
        self.print_text(f"{prompt}{raw_cmd}")

        if not raw_cmd: return

        cmd_parts = raw_cmd.split()
        cmd = cmd_parts[0]
        args = cmd_parts[1:] if len(cmd_parts) > 1 else []

        # --- LOGIKA PERINTAH LINUX ---
        if cmd == "ls":
            names = "  ".join(self.current_dir.children.keys())
            self.print_text(names)

        elif cmd == "mkdir":
            if args:
                self.current_dir.add_folder(args[0])
            else: self.print_text("mkdir: butuh nama folder")

        elif cmd == "touch":
            if args:
                self.current_dir.add_file(args[0])
            else: self.print_text("touch: butuh nama file")

        elif cmd == "cd":
            if not args or args[0] == "/":
                self.current_dir = self.vfs_root
            elif args[0] == "..":
                if self.current_dir.parent:
                    self.current_dir = self.current_dir.parent
            elif args[0] in self.current_dir.children:
                target = self.current_dir.children[args[0]]
                if isinstance(target, Folder):
                    self.current_dir = target
                else: self.print_text(f"cd: {args[0]} bukan folder")
            else: self.print_text(f"cd: {args[0]} tidak ditemukan")

        elif cmd == "cat":
            if args and args[0] in self.current_dir.children:
                target = self.current_dir.children[args[0]]
                if isinstance(target, File):
                    self.print_text(target.content)
                else: self.print_text(f"cat: {args[0]} adalah folder")
            else: self.print_text("cat: file tidak ditemukan")

        elif cmd == "save":
            save_vfs(self.vfs_root)
            self.print_text("Sistem berhasil disimpan ke vfs_data.json")

        elif cmd == "clear":
            self.output_area.config(state=tk.NORMAL)
            self.output_area.delete('1.0', tk.END) # Hapus semua teks
            self.output_area.config(state=tk.DISABLED)

        elif cmd == "exit":
            self.root.quit()

        else:
            self.print_text(f"Perintah '{cmd}' tidak dikenal. Ketik 'cat manual.txt'")

        # Update tulisan path setelah perintah dieksekusi
        self.update_prompt()

if __name__ == "__main__":
    root = tk.Tk()
    app = TerminalGUI(root)
    root.mainloop()