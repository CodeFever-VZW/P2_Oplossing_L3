import pikepdf
from tqdm import tqdm

passwords = []
for lijn in open("woorden.txt"):
    passwords.append(lijn.strip())

# Probeer elk mogelijk wachtwoord
for password in tqdm(passwords):
    try:
        # Probeer pdf te decrypteren
        pikepdf.open("hacking.pdf", password=password)
        # Als we hier komen is het wachtwoord succesvol gevonden
        print("Wachtwoord gevonden:", password)
        break
    except pikepdf._core.PasswordError:
        # Fout wachtwoord, doe niets
        pass