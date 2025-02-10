from utils import unzip_with_7z
import string


zip_file_path = 'congrats.7z'  # Garder tel quel
dest_path = '.'  # Garder tel quel
find_me = ""


letters = string.ascii_lowercase  # Contain 'abcdefghijklmnopqrstuvwxyz'

# This loop generate all combinations of two letters in the alphabet : 
for letter1 in letters:
    for letter2 in letters:
        find_me = letter1 + letter2  
        secret_password = find_me + 'bcmpda'  

        if unzip_with_7z(zip_file_path, dest_path, secret_password):
            print(f"Congratulation! Password found: {secret_password}")
            exit()  # Arrêter le programme une fois le bon mot de passe trouvé

print(" No valid password found.")




