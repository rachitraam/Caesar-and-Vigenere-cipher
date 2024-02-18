import customtkinter
import string

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()
root.geometry('1000*1000')

root.title('Mini Project')


def caesar_window():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')

    root = customtkinter.CTk()
    root.geometry('1000*1000')
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(expand=True)
    label1 = customtkinter.CTkLabel(master=frame, text='Enter the Text: ')
    label1.pack()
    user_text = customtkinter.CTkEntry(master=frame)
    user_text.pack()
    label2 = customtkinter.CTkLabel(master=frame, text='Enter the Shift: ')
    label2.pack()
    user_shift = customtkinter.CTkEntry(master=frame)
    user_shift.pack()

    def error_window():
        customtkinter.set_appearance_mode('Dark')
        customtkinter.set_default_color_theme('dark-blue')
        root = customtkinter.CTk()
        root.geometry('1000x1000')
        root.title('Error Window')
        label_error = customtkinter.CTkLabel(root, text='Invalid Input', width=150, height=90)
        label_error.pack(pady=60)
        label_try = customtkinter.CTkLabel(root, text='Please Enter an Integer for the Shift', width=150, height=90)
        label_try.pack(pady=60)
        root.mainloop()

    def caesar_encrypt():
        textinput = user_text.get()
        shift = user_shift.get()
        if shift.isalpha():
            error_window()

        textoutput = ""
        shift = int(shift)
        for i in textinput:
            if i in string.ascii_letters:
                if 65 <= ord(i) <= 90:
                    temp = ord(i) + shift
                    if temp > ord('Z'):
                        temp = temp - 26
                elif 97 <= ord(i) <= 122:
                    temp = ord(i) + shift
                    if temp > ord('z'):
                        temp = temp - 26
                textoutput = textoutput + chr(temp)
            else:
                textoutput = textoutput + i
        output = customtkinter.CTkLabel(root, text=textoutput)
        output.pack()

    def caesar_decrypt():
        textinput = user_text.get()
        shift = user_shift.get()
        if shift.isalpha():
            error_window()
        textoutput = ''
        shift = int(shift)
        for i in textinput:
            if i in string.ascii_letters:
                if 65 <= ord(i) <= 90:
                    temp = ord(i) - shift
                    if temp < ord('A'):
                        temp = temp + 26
                elif 97 <= ord(i) <= 122:
                    temp = ord(i) - shift
                    if temp < ord('a'):
                        temp = temp + 26
                textoutput = textoutput + chr(temp)
            else:
                textoutput = textoutput + i

        output = customtkinter.CTkLabel(root, text=textoutput)
        output.pack()

    button_encrypt = customtkinter.CTkButton(master=frame, text='Encrypt', command=caesar_encrypt, width=900, height=150)
    button_encrypt.pack(pady=20)
    button_decrypt = customtkinter.CTkButton(master=frame, text='Decrypt', command=caesar_decrypt, width=900, height=150)
    button_decrypt.pack(pady=20)
    root.title('Caesar Window')
    button_close = customtkinter.CTkButton(master=frame, text='Close', command=root.destroy, width=900, height=150)
    button_close.pack(pady=20)

    root.mainloop()


def vigenere_window():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')

    root = customtkinter.CTk()
    root.geometry('500x500')
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(expand=True)
    label1 = customtkinter.CTkLabel(master=frame, text='Enter the Text: ')
    label1.pack()
    user_text = customtkinter.CTkEntry(master=frame)
    user_text.pack()
    label2 = customtkinter.CTkLabel(master=frame, text='Enter the Key: ')
    label2.pack()
    user_key = customtkinter.CTkEntry(master=frame)
    user_key.pack()

    def error_window():
        customtkinter.set_appearance_mode('Dark')
        customtkinter.set_default_color_theme('dark-blue')
        root = customtkinter.CTk()
        root.geometry('300x300')
        root.title('Error Window')
        label_error = customtkinter.CTkLabel(root, text='Invalid Input', width=150, height=90)
        label_error.pack(pady=60)
        label_try = customtkinter.CTkLabel(root, text='Please Enter a String for the Key', width=150, height=90)
        label_try.pack(pady=60)
        root.mainloop()

    def vigenere_encrypt():
        cipher = ''
        plaintext = str(user_text.get())
        key = str(user_key.get())
        if key.isdigit():
            error_window()
        v_list = [chr(x + 97) for x in range(26)]
        v_list += v_list
        pt_list = plaintext.split()
        encrypt_list = []
        p = 0
        while len(key) < len(plaintext):
            key = key + key
        key = key.lower()
        for i in pt_list:
            n = len(i) - 1
            x = 0
            while x <= n:
                if 65 <= ord(i[x]) < 91:
                    keynum = ord(key[p]) - 97
                    ptnum = ord(i[x]) - 65
                    cipher = cipher + v_list[keynum + ptnum].upper()
                elif ord(i[x]) >= 97:
                    keynum = ord(key[p]) - 97
                    ptnum = ord(i[x]) - 97
                    cipher = cipher + v_list[keynum + ptnum]
                elif i[x].isdigit():
                    cipher = cipher + i[x]
                x += 1
                p += 1
            encrypt_list.append(cipher)
            cipher = ''
        encrypt_string = ' '.join(encrypt_list)
        output = customtkinter.CTkLabel(root, text=encrypt_string)
        output.pack()

    def vigenere_decrypt():
        cipher = str(user_text.get())
        key = str(user_key.get())
        if key.isdigit():
            error_window()
        cipher_list = cipher.split()
        decrypt_list = []
        v_list = [chr(x + 97) for x in range(26)]
        v_list += v_list
        p = 0
        ptext = ''
        while len(key) < len(cipher):
            key = key + key
        key = key.lower()
        for i in cipher_list:
            n = len(i) - 1
            x = 0
            while x <= n:
                if 65 <= ord(i[x]) < 91:
                    keynum = ord(key[p]) - 97
                    cnum = ord(i[x]) - 65
                    ptext = ptext + v_list[cnum - keynum].upper()
                elif ord(i[x]) >= 97:
                    keynum = ord(key[p]) - 97
                    cnum = ord(i[x]) - 97
                    ptext = ptext + v_list[cnum - keynum]
                elif i[x].isdigit():
                    ptext = ptext + i[x]
                x += 1
                p += 1
            decrypt_list.append(ptext)
            ptext = ''
        decrypt_string = ' '.join(decrypt_list)
        output = customtkinter.CTkLabel(root, text=decrypt_string)
        output.pack()

    button_encrypt = customtkinter.CTkButton(master=frame, text='Encrypt', command=vigenere_encrypt, width=900,
                                             height=150)
    button_encrypt.pack(pady=60)
    button_decrypt = customtkinter.CTkButton(master=frame, text='Decrypt', command=vigenere_decrypt, width=900,
                                             height=150)
    button_decrypt.pack(pady=60)
    button_close = customtkinter.CTkButton(master=frame, text='Close', command=root.destroy, width=900, height=150)
    button_close.pack(pady=60)
    root.title('Vigenere Window')

    root.mainloop()


frame = customtkinter.CTkFrame(master=root)
frame.pack(expand=True)

label_main = customtkinter.CTkLabel(master=frame, text='Please Choose the Type of Encryption', width=300, height=60)
label_main.pack(padx=60, pady=60)

button_c = customtkinter.CTkButton(master=frame, text='CAESAR', command=caesar_window, width=900, height=150)
button_c.pack(padx=60, pady=60)

button_v = customtkinter.CTkButton(master=frame, text='VIGENERE', command=vigenere_window, width=900, height=150)
button_v.pack(padx=60, pady=60)

button_q = customtkinter.CTkButton(master=frame, text='QUIT', command=root.destroy, width=900, height=150)
button_q.pack(padx=60, pady=60)

root.mainloop()
