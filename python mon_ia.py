import time
import google.generativeai as genai

# ==========================================
# 1. TA CLÉ SECRÈTE (À REMPLACER)
# ==========================================
# Remplace le texte ci-dessous par ta vraie clé API (garde bien les guillemets)
CLE_API_GEMINI = "COLLE_TA_CLE_ICI"

# ==========================================
# 2. CONFIGURATION DE L'IA
# ==========================================
genai.configure(api_key=CLE_API_GEMINI)

# Utilisation du modèle rapide et performant
model = genai.GenerativeModel('gemini-1.5-flash')

# On lance un "chat" pour que l'IA ait de la mémoire et se souvienne de la discussion
chat = model.start_chat(history=[])

print("================================================")
print(" TERMINAL IA PRIVÉ - CONNEXION À GEMINI ÉTABLIE ")
print(" (Tape 'quitter' pour fermer le programme)      ")
print("================================================")

# ==========================================
# 3. BOUCLE DE DISCUSSION
# ==========================================
while True:
    # On attend ta question
    texte_utilisateur = input("\n> Toi : ")

    # Si tu tapes 'quitter', le programme s'arrête
    if texte_utilisateur.lower() in ['quitter', 'exit', 'quit']:
        print("\n[Système] : Déconnexion du serveur...")
        time.sleep(1)
        break

    # Petit effet visuel de chargement stylé
    print("> Gemini : ⏳ Analyse en cours...", end="\r")

    try:
        # On envoie ta question à l'IA
        reponse = chat.send_message(texte_utilisateur)
        
        # On efface la ligne de chargement et on affiche la vraie réponse
        print(" " * 50, end="\r") 
        print(f"> Gemini : {reponse.text}")
        
    except Exception as e:
        print(f"\n[Erreur] : La connexion a échoué. As-tu bien mis ta clé API ? ({e})")
