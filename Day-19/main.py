import os
import qrcode_terminal

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

title_color = '\033[94m'
author_color = '\033[92m'
input_prompt_color = '\033[93m'
logo_color = '\033[96m'
reset_color = '\033[0m'

logo = f'''
{logo_color}
         █████╗ ██╗     ███████╗██╗  ██╗         ██████╗ ██████╗
        ██╔══██╗██║     ╚══███╔╝██║  ██║        ██╔═══██╗██╔══██╗
        ███████║██║       ███╔╝ ███████║        ██║   ██║██████╔╝
        ██╔══██║██║      ███╔╝  ██╔══██║        ██║▄▄ ██║██╔══██╗
        ██║  ██║███████╗███████╗██║  ██║███████╗╚██████╔╝██║  ██║
        ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝ ╚══▀▀═╝ ╚═╝  ╚═╝
                                                         {reset_color}
'''

clear_screen()

print(logo)
print(f"{title_color}                     ===== QR Code Generator ====={reset_color}")

while True:
    input_data = input(f"\n{input_prompt_color}Masukkan Teks Atau Link:{reset_color} ")

    if not input_data:
        print(f"{input_prompt_color}Teks atau link tidak boleh kosong. Silakan coba lagi.{reset_color}")
        clear_screen()
        print(logo)
        print(f"{title_color}                     ===== QR Code Generator ====={reset_color}")
        continue

    qrcode_terminal.draw(input_data)

    choice = input(f"\n{input_prompt_color}Buat QR Code lagi? (Y/n): {reset_color}")
    if choice.lower() != 'y':
        clear_screen()
        print(f"{author_color}Terima kasih telah menggunakan script ini!\nJangan lupa follow Instagram  @_4lghifari_ ^_^{reset_color}")
        break
    clear_screen()
    print(logo)
    print(f"{title_color}                     ===== QR Code Generator ====={reset_color}")
