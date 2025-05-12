import tkinter as tk
import random


def loe_kaart():
    return random.randint(2, 11)


def arvuta_tulemus(mängija_summa, vastane_summa):
    if mängija_summa > 21:
        return "Kaotasid! Ületasid 21!"
    elif vastane_summa > 21:
        return "Võitsid! Vastane ületas 21!"
    elif mängija_summa > vastane_summa:
        return "Võitsid!"
    elif mängija_summa < vastane_summa:
        return "Kaotasid!"
    else:
        return "Viik!"


def alusta_mängu():
    global mängija_nimi, mängija_summa, vastane_summa, mängija_kaardid, vastase_kaardid
    mängija_nimi = mängija_nimi_entry.get()
    if not mängija_nimi:
        lõppseis_label.config(text="Sisesta mängija nimi!")
        return

    mängija_nimi_entry.config(state=tk.DISABLED)

    mängija_summa, vastane_summa = 0, 0
    mängija_kaardid, vastase_kaardid = [], []
    
    mängija_kaardid_label.config(text=f"Mängija kaardid: {mängija_kaardid}")
    mängija_summa_label.config(text=f"Summa: {mängija_summa}")
    vastane_kaardid_label.config(text="Vastase kaardid: ?")
    vastane_summa_label.config(text="Summa: ?")
    
    alustamisnupp.pack_forget()  # Eemaldab nupu pärast vajutamist
    võta_kaart_nupp.config(state=tk.NORMAL)
    peatu_nupp.config(state=tk.NORMAL)


def võta_kaart():
    global mängija_summa, mängija_kaardid
    kaart = loe_kaart()
    mängija_kaardid.append(kaart)
    mängija_summa += kaart
    mängija_kaardid_label.config(text=f"Mängija kaardid: {mängija_kaardid}")
    mängija_summa_label.config(text=f"Summa: {mängija_summa}")
    if mängija_summa > 21:
        lõppseis("Kaotasid! Ületasid 21!")


def peatu():
    global mängija_summa, vastane_summa, mängija_kaardid, vastase_kaardid
    while vastane_summa < 17:
        kaart = loe_kaart()
        vastase_kaardid.append(kaart)
        vastane_summa += kaart
    vastane_kaardid_label.config(text=f"Vastase kaardid: {vastase_kaardid}")
    vastane_summa_label.config(text=f"Summa: {vastane_summa}")
    lõppseis(arvuta_tulemus(mängija_summa, vastane_summa))


def lõppseis(tulemus):
    lõppseis_label.config(text=f"Tulemus: {tulemus}")
    alustamisnupp.config(text="Mängi uuesti")  # Muudab nupu teksti "Mängi uuesti"
    alustamisnupp.pack()  # Kuvab "Mängi uuesti" nupu tagasi
    võta_kaart_nupp.config(state=tk.DISABLED)
    peatu_nupp.config(state=tk.DISABLED)

    salvesta_tulemus(mängija_nimi, tulemus, mängija_summa)
    

    mängija_nimi_entry.config(state=tk.NORMAL)


def salvesta_tulemus(nimi, tulemus, summa):
    with open("tulemused.txt", "a") as f:
        f.write(f"{nimi}, {tulemus}, {summa}\n")


aken = tk.Tk()
aken.title("Mäng 21")
aken.geometry("400x400")


mängija_nimi_label = tk.Label(aken, text="Sisesta Mängija nimi:")
mängija_nimi_label.pack()
mängija_nimi_entry = tk.Entry(aken)
mängija_nimi_entry.pack()


alustamisnupp = tk.Button(aken, text="Alusta mängu", command=alusta_mängu)
alustamisnupp.pack()


mängija_kaardid_label = tk.Label(aken, text="Mängija kaardid: []")
mängija_kaardid_label.pack()
mängija_summa_label = tk.Label(aken, text="Summa: 0")
mängija_summa_label.pack()
vastane_kaardid_label = tk.Label(aken, text="Vastase kaardid: ?")
vastane_kaardid_label.pack()
vastane_summa_label = tk.Label(aken, text="Summa: ?")
vastane_summa_label.pack()


võta_kaart_nupp = tk.Button(aken, text="Võta kaart", command=võta_kaart, state=tk.DISABLED)
võta_kaart_nupp.pack()
peatu_nupp = tk.Button(aken, text="Peatu", command=peatu, state=tk.DISABLED)
peatu_nupp.pack()


lõppseis_label = tk.Label(aken, text="Tulemus:")
lõppseis_label.pack()


aken.mainloop()

