import tkinter 
from tkinter import messagebox
from PIL import ImageTk, Image
import cryptocode as cry




def encrypt_message():

    label_info.config(text="")


    if (title_entry.get() != "") & (password_entry.get() != ""):

        encrypt_path = cry.encrypt(message=encrypted_text.get(1.0,"end"), password=password_entry.get())
        f = open("Crypted_Path.txt","a")
        f.seek(0,2)
        f.write(f"{title_entry.get()}\n{encrypt_path}\n")
        f.close

    elif title_entry.get() == "":

        label_info.config(text="Please write title for encrypt")


    elif password_entry.get() == "":

        label_info.config(text="Please write Key for encrypt")
    
    else:

        messagebox.showerror(title="ERROR",message="Encypt Failed")



def decrypt_message():

    decrypt_path = encrypted_text.get(1.0,"end")
    output_password = password_entry.get()
    decrypted_message = cry.decrypt(decrypt_path, output_password)


    if decrypted_message:

        encrypted_text.delete(1.0, "end")
        encrypted_text.insert(1.0,decrypted_message)


    else:

        messagebox.showwarning(title="Error", message= "Key or Decrypt path are not exist")



def start_window():

    # Window

    win = tkinter.Tk()
    win.title("secret note")
    win.minsize(width=300, height=500)
    win.config(padx=20, pady=20)


    # İmage

    img = Image.open("Secret.png")
    img = img.resize((200,60))
    photo = ImageTk.PhotoImage(img)
    panel = tkinter.Label(win, image = photo)
    panel.pack(side = "top", fill = "none", expand = "0", padx=20, pady= 20)


    # Widget


    global title_entry
    global encrypted_text
    global password_entry
    global encrypt_button
    global decrypt_button
    global label_info

    

    label_1 = tkinter.Label(text="Enter Your Title", font= ("Helvetica","12",""))
    title_entry = tkinter.Entry(width=25, font= ("Helvetica","12",""))
    label_2 = tkinter.Label(text= "Enter Your Secret", font= ("Helvetica","12",""))
    encrypted_text = tkinter.Text(width=25, height=5, font= ("","12",""))
    label_3 = tkinter.Label(text= "Enter Master Key", font= ("Helvetica","12",""))
    password_entry = tkinter.Entry(width=25, font= ("Helvetica","12",""))
    encrypt_button = tkinter.Button(text="Save & Encrypt", width=25, command=encrypt_message)
    decrypt_button = tkinter.Button(text="Decrypt", width=15, command=decrypt_message)
    label_info = tkinter.Label(font= ("Helvetica","12",""))


    # Pack

    label_1.pack()
    title_entry.pack()
    label_2.pack(padx=5, pady=5)
    encrypted_text.pack()
    label_3.pack(padx=5, pady=5)
    password_entry.pack()
    encrypt_button.pack(padx=5, pady=5)
    decrypt_button.pack(padx=5, pady=5)
    label_info.pack(padx=5, pady=5)


    tkinter.mainloop()



start_window()