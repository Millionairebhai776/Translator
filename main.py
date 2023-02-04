import tkinter as tk
from googletrans import Translator

def translate_text():
    input_text = input_field.get("1.0", END)
    translator = Translator(service_urls=['translate.google.com'])
    translated_text = translator.translate(input_text, dest='ml').text
    output_field.delete("1.0", END)
    output_field.insert(INSERT, translated_text)

root = tk.Tk()
root.title("English to Malayalam Translator")

input_field = tk.Text(root, height=10, width=30)
input_field.pack(pady=10)

translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=10)

output_field = tk.Text(root, height=10, width=30, state=tk.DISABLED)
output_field.pack(pady=10)

root.mainloop()
