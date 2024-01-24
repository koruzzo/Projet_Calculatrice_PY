"""
    tkinter est utilisé pour la construction et l'affichage de l'application
    pandas est utilisé pour le travail sur csv et le calcul
    messagebox de tkinter est utilisé pour générer des boites de dialogue
"""
import tkinter as tk
from tkinter import messagebox
import pandas as pd

def calc_and_err():
    """
    _summary_
        Cette fonction fait le calcul de l'expression choisi tout en 
        gérant à l'aide d'un "try except" les différentes erreurs possibles.
        Elle lance aussi la fonction de sauvegarde.
    """
    try:
        expression = entry.get()
        expression = replace_commas(expression)
        result = pd.eval(expression)
        result_label.config(text = "Résultat : " + str(result))
        save_operation(expression, result)  # On sauvegarde l'opération
    except ZeroDivisionError:
        messagebox.showerror("Erreur", "Division par zéro impossible.")
        result_label.config(text = "Erreur")
    except NameError:
        messagebox.showerror("Erreur", "Vous esseyez d'entrer n'importe quoi hein ?")
        result_label.config(text = "Erreur")
    except ValueError:
        messagebox.showerror("Erreur", "Erreur de type. Entrer une expression valide.")
        result_label.config(text = "Erreur")
    except SyntaxError:
        messagebox.showerror("Erreur", "Vous esseyez d'entrer n'importe quoi hein ?")
        result_label.config(text = "Erreur")
    except ImportError as e:
        messagebox.showerror("Erreur", f"Erreur de calcul : {str(e)}")
        result_label.config(text = "Erreur")

def replace_commas(expression):
    """
    _summary_
        Cette fonction remplace les ',' entrées, par des points
    Args:
        expression (_str_): _L'expression mathématique entrée par l'utilisateur_

    Returns:
        parts (_str_): _L'expression mathématique entrée par l'utilisateur, modifiée_
    """
    parts = expression.split()
    for i, part in enumerate(parts):
        if '.' not in part and ',' in part:
            parts[i] = part.replace(',', '.')
    return ' '.join(parts)

def save_operation(expression, result):
    """
    _summary_
        Cette fonction ajoute une nouvelle ligne au fichier CSV 'operations.csv'
        contenant les dernières opérations.
        Si le fichier n'existe pas, il sera créé.

    Args:
        expression (_str_): _L'expression mathématique entrée par l'utilisateur_
        result (_float_): _Le résultat de l'expression_
    """
    try:
        data = pd.read_csv('operations.csv')
    except FileNotFoundError:
        data = pd.DataFrame(columns = ['Expression', 'Résultat'])

    new_data = pd.DataFrame({'Expression': [expression], 'Résultat': [result]})
    data = pd.concat([data, new_data], ignore_index = True)
    data.tail(5).to_csv('operations.csv', index = False)

def show_last_5():
    """
    _summary_
    Cette fonction affiche les 5 dernières opérations sauvegardées dans le fichier CSV.
    """
    try:
        data = pd.read_csv('operations.csv')
        last_operations = data.tail(5)
        messagebox.showinfo("Les 5 dernières opérations", last_operations.to_string(index = False))
    except FileNotFoundError:
        messagebox.showinfo("Empty", "Aucune opération n'a été enregistrée.")

def reset_entry():
    """
    _summary_
        Cette fonction réinitialise l'input de l'utilisateur.
    """
    entry.delete(0, 'end')
    result_label.config(text = "Résultat : ")

# Création fenêtre principale
root = tk.Tk()
root.title("Calculatrice")

# Input
entry = tk.Entry(root, font = ('Arial', 30), width = 50)
entry.pack(pady = 10)

# Afficher le résultat
result_label = tk.Label(root, text="Résultat : ", font = ('Arial', 30))
result_label.pack(pady = 10)

# Lancer le calcul
calculate_button = tk.Button(root, text = "Calculer", command = calc_and_err, font = ('Arial', 30))
calculate_button.pack(side = tk.LEFT, padx = 5)

# Réinitialiser Input
reset_button = tk.Button(root, text = "Reset", command = reset_entry, font = ('Arial', 30))
reset_button.pack(side = tk.LEFT, padx = 5)

# Afficher les 5 dernières opérations
history_button = tk.Button(root, text = "Historique", command = show_last_5, font = ('Arial', 30))
history_button.pack(side = tk.RIGHT, padx = 5)

root.mainloop()
