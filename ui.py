import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import main

class EmailGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Send Email GUI")

        # Variables para almacenar la entrada del usuario
        self.sender_var = tk.StringVar()
        self.recipient_var = tk.StringVar()
        self.subject_var = tk.StringVar()
        self.body_var = tk.StringVar()
        self.body_file_path = tk.StringVar()
        self.config_file_path = tk.StringVar()

        # Configurar y mostrar los elementos de la interfaz gráfica
        self.setup_ui()

    def setup_ui(self):
        # Etiquetas y campos de entrada
        tk.Label(self.master, text="Sender's Email:").grid(row=0, column=0, sticky=tk.E)
        tk.Entry(self.master, textvariable=self.sender_var).grid(row=0, column=1)

        tk.Label(self.master, text="Recipient's Email:").grid(row=1, column=0, sticky=tk.E)
        tk.Entry(self.master, textvariable=self.recipient_var).grid(row=1, column=1)

        tk.Label(self.master, text="Email Subject:").grid(row=2, column=0, sticky=tk.E)
        tk.Entry(self.master, textvariable=self.subject_var).grid(row=2, column=1)

        tk.Label(self.master, text="Body File:").grid(row=3, column=0, sticky=tk.E)
        tk.Entry(self.master, textvariable=self.body_file_path, state="readonly").grid(row=3, column=1)
        tk.Button(self.master, text="Browse", command=self.browse_body_file).grid(row=3, column=2)

        tk.Label(self.master, text="Config File (optional):").grid(row=4, column=0, sticky=tk.E)
        tk.Entry(self.master, textvariable=self.config_file_path, state="readonly").grid(row=4, column=1)
        tk.Button(self.master, text="Browse", command=self.browse_config_file).grid(row=4, column=2)

        # Botón para enviar el correo electrónico
        tk.Button(self.master, text="Send Email", command=self.send_email).grid(row=5, column=1, pady=10)

    def browse_body_file(self):
        file_path = filedialog.askopenfilename(title="Select Body File", filetypes=[("HTML Files", "*.html")])
        if file_path:
            self.body_file_path.set(file_path)

    def browse_config_file(self):
        file_path = filedialog.askopenfilename(title="Select Config File", filetypes=[("Text Files", "*.txt")])
        if file_path:
            self.config_file_path.set(file_path)

    def send_email(self):
        sender = self.sender_var.get()
        recipient = self.recipient_var.get()
        subject = self.subject_var.get()
        body_file_path = self.body_file_path.get()
        config_file_path = self.config_file_path.get()

        try:
            ses_client = EnviaEmail(region_name='your_aws_region')
            body = EnviaEmail.read_body(body_file_path)

            if config_file_path:
                config = EnviaEmail.read_config(config_file_path)
                sender = config.get('sender', sender)
                recipient = config.get('recipient', recipient)
                subject = config.get('subject', subject)
                body = EnviaEmail.read_body(config.get('body_file', ''))

            ses_client.send_email(sender, recipient, subject, body)
            messagebox.showinfo("Success", "Email sent successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send email. Error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = EmailGUI(root)
    root.mainloop()
