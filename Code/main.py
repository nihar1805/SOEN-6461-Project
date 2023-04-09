from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
from PIL import ImageTk, Image

class TicketVendingMachine:

    def __init__(self, master):
        self.master = master
        self.master.title("iGo Ticket Vending System")
        self.master.geometry("700x700")
        self.master.resizable(False, False)
        self.tit = ctk.CTkFrame(master=self.master, fg_color="orange")
        self.tit.pack(side = "top", fill = "both")
        self.title_label = ctk.CTkLabel(self.tit, text="Welcome to the iGo Ticket Vending Machine")
        self.title_label.pack(pady=20)

        self.language_label = ctk.CTkLabel(self.master, text="Select a language:")
        self.language_label.pack(pady=20)

        self.language_var = StringVar()
        self.language_var.set(None)

        self.language_radio_frame = ctk.CTkFrame(master=self.master, fg_color="white")
        self.language_radio_frame.pack(pady=20)

        self.english_radio_button = ctk.CTkRadioButton(self.language_radio_frame, text="English", variable=self.language_var,
                                                value="English")
        self.english_radio_button.pack(side=LEFT)

        self.french_radio_button = ctk.CTkRadioButton(self.language_radio_frame, text="French", variable=self.language_var,
                                               value="French")
        self.french_radio_button.pack(side=LEFT)

        self.next_button = ctk.CTkButton(self.master, text="Next", command=self.select_option)
        self.next_button.pack(pady=20)





    def select_option(self):
        self.language = self.language_var.get()

        if self.language == 'English':
            if self.language:
                self.tit.pack_forget()
                self.language_label.pack_forget()
                self.title_label.forget()
                self.language_radio_frame.pack_forget()
                self.next_button.pack_forget()

                self.option_label = ctk.CTkLabel(self.master, text="Select an option:")
                self.option_label.pack(pady=20)

                self.option_var = StringVar()
                self.option_var.set(None)

                self.option_radio_frame = ctk.CTkFrame(master=self.master, fg_color="white")
                self.option_radio_frame.pack(pady=20)

                self.recharge_radio_button = ctk.CTkRadioButton(self.option_radio_frame, text="Recharge card",
                                                         variable=self.option_var, value="Recharge")
                self.recharge_radio_button.pack(side=LEFT)

                self.buy_radio_button = ctk.CTkRadioButton(self.option_radio_frame, text="Buy new ticket",
                                                    variable=self.option_var, value="Buy")
                self.buy_radio_button.pack(side=LEFT)

                self.next_button.configure(text="Next", command=self.select_age_group)
                self.next_button.pack(pady=20)
            else:
                messagebox.showerror("Error", "Please select a language.")

        if self.language == 'French':
            if self.language:
                self.tit.pack_forget()
                self.language_label.pack_forget()
                self.language_radio_frame.pack_forget()
                self.next_button.pack_forget()

                self.option_label = ctk.CTkLabel(self.master, text="Choisir une option:")
                self.option_label.pack(pady=20)

                self.option_var = StringVar()
                self.option_var.set(None)

                self.option_radio_frame = ctk.CTkFrame(master=self.master, fg_color="white")
                self.option_radio_frame.pack(pady=20)

                self.recharge_radio_button = ctk.CTkRadioButton(self.option_radio_frame, text="Carte de recharge",
                                                         variable=self.option_var, value="Recharger")
                self.recharge_radio_button.pack(side=LEFT)

                self.buy_radio_button = ctk.CTkRadioButton(self.option_radio_frame, text="Acheter un ticket",
                                                    variable=self.option_var, value="Acheter")
                self.buy_radio_button.pack(side=LEFT)

                self.next_button.configure(text="Prochain", command=self.select_age_group)
                self.next_button.pack(pady=20)
            else:
                messagebox.showerror("Erreur", "Veuillez sélectionner une langue.")





    def select_age_group(self):
        self.option = self.option_var.get()

        if self.option == 'Recharge':
            if self.language == 'English':
                if self.option:
                    self.next_button.pack_forget()
                    self.option_label.pack_forget()
                    self.option_radio_frame.pack_forget()
                    self.next_button.pack_forget()

                    self.age_label = ctk.CTkLabel(self.master, text="Select age group:")
                    self.age_label.pack()

                    self.age_var = StringVar()
                    self.age_var.set(None)

                    self.age_radio_frame = ctk.CTkFrame(master=self.master, fg_color="white")
                    self.age_radio_frame.pack(pady=20)

                    self.adult_radio_button = ctk.CTkRadioButton(self.age_radio_frame, text="Adult", variable=self.age_var,
                                                          value="Adult")
                    self.adult_radio_button.pack(side=LEFT)

                    self.child_radio_button = ctk.CTkRadioButton(self.age_radio_frame, text="Child", variable=self.age_var,
                                                          value="Child")
                    self.child_radio_button.pack(side=LEFT)

                    self.senior_radio_button = ctk.CTkRadioButton(self.age_radio_frame, text="Senior", variable=self.age_var,
                                                           value="Senior")
                    self.senior_radio_button.pack(side=LEFT)

                    self.next_button.configure(text="Next", command=self.select_fare)
                    self.next_button.pack(pady=20)
                else:
                    messagebox.showerror("Error", "Please select an option.")

        elif self.option == 'Buy':
            if self.language == 'English':
                if self.option:
                    self.option_label.pack_forget()
                    self.option_radio_frame.pack_forget()
                    self.next_button.pack_forget()

                    self.fare_label = ctk.CTkLabel(self.master, text="Select fare type:")
                    self.fare_label.pack(pady=20)

                    self.fare_var = StringVar()
                    self.fare_var.set(None)

                    self.fare_prc = IntVar()
                    self.fare_prc.set(0)

                    self.fare_radio_frame = ctk.CTkFrame(master=self.master, fg_color="white")
                    self.fare_radio_frame.pack(pady=20)

                    self.trip1_button = ctk.CTkRadioButton(self.fare_radio_frame, text="1 Trip (3)", variable=self.fare_var,
                                                          value="1 Trip")
                    self.trip1_button.pack(side=LEFT)

                    self.trip2_button = ctk.CTkRadioButton(self.fare_radio_frame, text="2 Trip (6)", variable=self.fare_var,
                                                          value="2 Trip")
                    self.trip2_button.pack(side=LEFT)

                    self.day_trip_button = ctk.CTkRadioButton(self.fare_radio_frame, text="1 Day Trip (10)",
                                                           variable=self.fare_var,
                                                           value="1 Day Trip")
                    self.day_trip_button.pack(side=LEFT)

                    self.next_button.configure(text="Next", command=self.select_payment_option)
                    self.next_button.pack(pady=20)
                else:
                    messagebox.showerror("Error", "Please select an option.")

        if self.option == 'Recharger':
            if self.language == 'French':
                if self.option:
                    self.option_label.pack_forget()
                    self.option_radio_frame.pack_forget()
                    self.next_button.pack_forget()

                    self.age_label = ctk.CTkLabel(self.master, text="Sélectionnez le groupe d'âge :")
                    self.age_label.pack(pady=20)

                    self.age_var = StringVar()
                    self.age_var.set(None)

                    self.age_radio_frame = ctk.CTkFrame(master=self.master, fg_color="white")
                    self.age_radio_frame.pack(pady=20)

                    self.adult_radio_button = ctk.CTkRadioButton(self.age_radio_frame, text="Adulte", variable=self.age_var,
                                                          value="Adulte")
                    self.adult_radio_button.pack(side=LEFT)

                    self.child_radio_button = ctk.CTkRadioButton(self.age_radio_frame, text="Enfant", variable=self.age_var,
                                                          value="Enfant")
                    self.child_radio_button.pack(side=LEFT)

                    self.senior_radio_button = ctk.CTkRadioButton(self.age_radio_frame, text="Senior", variable=self.age_var,
                                                           value="Senior")
                    self.senior_radio_button.pack(side=LEFT)

                    self.next_button.configure(text="Prochain", command=self.select_fare)
                    self.next_button.pack(pady=20)
                else:
                    messagebox.showerror("Erreur", "Veuillez sélectionner une option.")

        elif self.option == 'Acheter':
            if self.language == 'French':
                if self.option:
                    self.option_label.pack_forget()
                    self.option_radio_frame.pack_forget()
                    self.next_button.pack_forget()

                    self.fare_label = ctk.CTkLabel(self.master, text="Sélectionnez le type de tarif :")
                    self.fare_label.pack(pady=20)

                    self.fare_var = StringVar()
                    self.fare_var.set(None)

                    self.fare_prc = IntVar()
                    self.fare_prc.set(0)

                    self.fare_radio_frame = ctk.CTkFrame(master=self.master, fg_color="white")
                    self.fare_radio_frame.pack(pady=20)

                    self.trip1_button = ctk.CTkRadioButton(self.fare_radio_frame, text="1 voyage (3)", variable=self.fare_var,
                                                          value="1 voyage")
                    self.trip1_button.pack(side=LEFT)

                    self.trip2_button = ctk.CTkRadioButton(self.fare_radio_frame, text="2 voyage (6)", variable=self.fare_var,
                                                          value="2 voyage")
                    self.trip2_button.pack(side=LEFT)

                    self.day_trip_button = ctk.CTkRadioButton(self.fare_radio_frame, text="Excursion d'une journée (10)",
                                                           variable=self.fare_var,
                                                           value="Excursion d'une journée")
                    self.day_trip_button.pack(side=LEFT)

                    self.next_button.configure(text="Prochain", command=self.select_payment_option)
                    self.next_button.pack(pady=20)
                else:
                    messagebox.showerror("Erreur", "Veuillez sélectionner une option.")

    def select_fare(self):
        self.age = self.age_var.get()

        if self.language == 'English':
            if self.age:
                self.age_label.pack_forget()
                self.age_radio_frame.pack_forget()
                self.next_button.pack_forget()
                self.fare_label = ctk.CTkLabel(self.master, text="Select fare type:")
                self.fare_label.pack(pady=20)

                self.fare_var = StringVar()
                self.fare_var.set(None)

                self.fare_prc = IntVar()
                self.fare_prc.set(0)

                self.fare_radio_frame = ctk.CTkFrame(master=self.master, fg_color="white")
                self.fare_radio_frame.pack(pady=20)

                if self.age == "Adult":
                    self.monthly_radio_button = ctk.CTkRadioButton(self.fare_radio_frame, text="1 Month Pass (100)",
                                                            variable=self.fare_var, value="Monthly")
                    self.monthly_radio_button.pack(side=LEFT)

                    self.weekly_radio_button = ctk.CTkRadioButton(self.fare_radio_frame, text="1 Week Pass (50)",
                                                           variable=self.fare_var, value="Weekly")
                    self.weekly_radio_button.pack(side=LEFT)

                    self.daily_radio_button = ctk.CTkRadioButton(self.fare_radio_frame, text="1 Day Pass (10)",
                                                          variable=self.fare_var, value="Daily")
                    self.daily_radio_button.pack(side=LEFT)

                elif self.age == "Child":
                    self.monthly_radio_button = ctk.CTkRadioButton(self.fare_radio_frame, text="Child 1 Month Pass (50)",
                                                            variable=self.fare_var, value="Child Monthly")
                    self.monthly_radio_button.pack(side=LEFT)

                    self.weekly_radio_button = ctk.CTkRadioButton(self.fare_radio_frame, text="Child 1 Week Pass (30)",
                                                           variable=self.fare_var, value="Child Weekly")
                    self.weekly_radio_button.pack(side=LEFT)

                    self.daily_radio_button = ctk.CTkRadioButton(self.fare_radio_frame, text="Child 1 Day Pass (5)",
                                                          variable=self.fare_var, value="Child Daily")
                    self.daily_radio_button.pack(side=LEFT)

                elif self.age == "Senior":
                    self.monthly_radio_button = ctk.CTkRadioButton(self.fare_radio_frame, text="Senior 1 Month Pass (75)",
                                                            variable=self.fare_var, value="Senior Monthly")
                    self.monthly_radio_button.pack(side=LEFT)

                    self.weekly_radio_button = ctk.CTkRadioButton(self.fare_radio_frame, text="Senior 1 Week Pass (40)",
                                                           variable=self.fare_var, value="Senior Weekly")
                    self.weekly_radio_button.pack(side=LEFT)

                    self.daily_radio_button = ctk.CTkRadioButton(self.fare_radio_frame, text="Senior 1 Day Pass (7)",
                                                          variable=self.fare_var, value="Senior Daily")
                    self.daily_radio_button.pack(side=LEFT)

                self.next_button.configure(text="Next", command=self.select_payment_option)
                self.next_button.pack(pady=20)

            else:
                messagebox.showerror("Error", "Please select an age group.")



        elif self.language == 'French':
            if self.age:
                self.age_label.pack_forget()
                self.age_radio_frame.pack_forget()
                self.next_button.pack_forget()
                self.fare_label = ctk.CTkLabel(self.master, text="Sélectionnez le type de tarif :")
                self.fare_label.pack(pady=20)

                self.fare_var = StringVar()
                self.fare_var.set(None)

                self.fare_prc = IntVar()
                self.fare_prc.set(0)

                self.fare_radio_frame = ctk.CTkFrame(master=self.master, fg_color="white")
                self.fare_radio_frame.pack(pady=20)

                if self.age == "Adulte":
                    self.monthly_radio_button = ctk.CTkRadioButton(self.fare_radio_frame, text="Pass 1 mois (100)",
                                                            variable=self.fare_var, value="Mensuel")
                    self.monthly_radio_button.pack(side=LEFT)

                    self.weekly_radio_button = ctk.CTkRadioButton(self.fare_radio_frame, text="Pass 1 semaine (50)",
                                                           variable=self.fare_var, value="Hebdomadaire")
                    self.weekly_radio_button.pack(side=LEFT)

                    self.daily_radio_button = ctk.CTkRadioButton(self.fare_radio_frame, text="Pass 1 jour (10)",
                                                          variable=self.fare_var, value="Quotidien")
                    self.daily_radio_button.pack(side=LEFT)

                elif self.age == "Enfant":
                    self.monthly_radio_button = ctk.CTkRadioButton(self.fare_radio_frame, text="Pass Enfant 1 Mois (50)",
                                                            variable=self.fare_var, value="Enfant Mensuel")
                    self.monthly_radio_button.pack(side=LEFT)

                    self.weekly_radio_button = ctk.CTkRadioButton(self.fare_radio_frame, text="Pass 1 Semaine Enfant (30)",
                                                           variable=self.fare_var, value="Enfant Hebdomadaire")
                    self.weekly_radio_button.pack(side=LEFT)

                    self.daily_radio_button = ctk.CTkRadioButton(self.fare_radio_frame, text="Pass Enfant 1 Jour (5)",
                                                          variable=self.fare_var, value="Enfant Quotidien")
                    self.daily_radio_button.pack(side=LEFT)

                elif self.age == "Senior":
                    self.monthly_radio_button = ctk.CTkRadioButton(self.fare_radio_frame, text="Forfait Sénior 1 Mois (75)",
                                                            variable=self.fare_var, value="Sénior Mensuel")
                    self.monthly_radio_button.pack(side=LEFT)

                    self.weekly_radio_button = ctk.CTkRadioButton(self.fare_radio_frame, text="Forfait Sénior 1 Semaine (40)",
                                                           variable=self.fare_var, value="Senior Hebdomadaire")
                    self.weekly_radio_button.pack(side=LEFT)

                    self.daily_radio_button = ctk.CTkRadioButton(self.fare_radio_frame, text="Pass 1 jour sénior (7)",
                                                          variable=self.fare_var, value="Sénior Quotidien")
                    self.daily_radio_button.pack(side=LEFT)

                self.next_button.configure(text="Prochain", command=self.select_payment_option)
                self.next_button.pack(pady=20)

            else:
                messagebox.showerror("Erreur", "Veuillez sélectionner une tranche d'âge.")


    def select_payment_option(self):
        self.fare = self.fare_var.get()
        self.prc = self.fare_prc.get()
        self.option = self.option_var.get()

        # print(self.age)
        print(self.fare)
        print(self.prc)
        print(self.option)

        if (self.option == "Recharge" or self.option == "Recharger"):
            self.age = self.age_var.get()
            if (self.age == "Adult" or self.age == "Adulte"):
                if (self.fare == "Monthly" or self.fare == "Mensuel"):
                    self.prc = 100
                elif (self.fare == "Weekly" or self.fare == "Hebdomadaire"):
                    self.prc = 50
                elif (self.fare == "Daily" or self.fare == "Quotidien"):
                    self.prc = 10
            elif (self.age == "Child" or self.age == "Enfant"):
                if (self.fare == "Child Monthly" or self.fare == "Enfant Mensuel"):
                    self.prc = 50
                elif (self.fare == "Child Weekly" or self.fare == "Enfant Hebdomadaire"):
                    self.prc = 30
                elif (self.fare == "Child Daily" or self.fare == "Enfant Quotidien"):
                    self.prc = 5
            elif (self.age == "Senior"):
                if (self.fare == "Senior Monthly" or self.fare == "Sénior Mensuel"):
                    self.prc = 75
                elif (self.fare == "Senior Weekly" or self.fare == "Senior Hebdomadaire"):
                    self.prc = 40
                elif (self.fare == "Senior Daily" or self.fare == "Sénior Quotidien"):
                    self.prc = 7
            else:
                self.prc.set = 0

        elif (self.option == "Buy" or self.option == "Acheter"):
            if (self.fare == "1 Trip" or self.fare == "1 voyage"):
                self.prc = 3
            elif (self.fare == "2 Trip" or self.fare == "2 voyage"):
                self.prc = 6
            elif (self.fare == "1 Day Trip" or self.fare == "Excursion d'une journée"):
                self.prc = 10
            else:
                self.prc.set = 0



        if self.language == "English":
            if self.fare:
                self.fare_label.pack_forget()
                self.fare_radio_frame.pack_forget()
                self.next_button.pack_forget()

                self.payment_label = ctk.CTkLabel(self.master, text="Select payment option:")
                self.payment_label.pack(pady=20)

                self.payment_var = StringVar()
                self.payment_var.set(None)

                self.payment_radio_frame = ctk.CTkFrame(master=self.master, fg_color="white")
                self.payment_radio_frame.pack(pady=20)

                self.cash_radio_button = ctk.CTkRadioButton(self.payment_radio_frame, text="Cash", variable=self.payment_var,
                                                     value="Cash")
                self.cash_radio_button.pack(side=LEFT)

                self.card_radio_button = ctk.CTkRadioButton(self.payment_radio_frame, text="Card", variable=self.payment_var,
                                                     value="Card")
                self.card_radio_button.pack(side=LEFT)

                self.next_button.configure(text="Pay", command=self.print_receipt)
                self.next_button.pack(pady=20)
            else:
                messagebox.showerror("Error", "Please select a fare type.")

        elif self.language == "French":
            if self.fare:
                self.fare_label.pack_forget()
                self.fare_radio_frame.pack_forget()
                self.next_button.pack_forget()

                self.payment_label = ctk.CTkLabel(self.master, text="Sélectionnez l'option de paiement :")
                self.payment_label.pack(pady=20)

                self.payment_var = StringVar()
                self.payment_var.set(None)

                self.payment_radio_frame = ctk.CTkFrame(self.master)
                self.payment_radio_frame.pack(pady=20)

                self.cash_radio_button = ctk.CTkRadioButton(self.payment_radio_frame, text="Espèces", variable=self.payment_var,
                                                     value="Espèces")
                self.cash_radio_button.pack(side=LEFT)

                self.card_radio_button = ctk.CTkRadioButton(self.payment_radio_frame, text="Carte", variable=self.payment_var,
                                                     value="Carte")
                self.card_radio_button.pack(side=LEFT)

                self.next_button.configure(text="Payer", command=self.print_receipt)
                self.next_button.pack(pady=20)
            else:
                messagebox.showerror("Erreur", "Veuillez sélectionner un type de tarif.")
    def print_receipt(self):
        self.payment_option = self.payment_var.get()

        if self.language == "English":
            if self.payment_option:
                self.payment_label.pack_forget()
                self.payment_radio_frame.pack_forget()
                self.next_button.pack_forget()

                self.receipt = f"Language: {self.language}\n"
                if self.option == "Recharge":
                    self.receipt += f"Age: {self.age}\n"
                self.receipt += f"Fare Type: {self.fare}\n"
                self.receipt += f"Payment Option: {self.payment_option}\n"

                if self.payment_option == "Cash":
                    self.amount_label = ctk.CTkLabel(self.master, text="Enter amount:")
                    self.amount_label.pack(pady=20)

                    self.amount_entry = ctk.CTkEntry(self.master)
                    self.amount_entry.pack(pady=20)

                    self.pay_button = ctk.CTkButton(self.master, text="Pay", command=self.calculate_change)
                    self.pay_button.pack(pady=20)
                else:
                    self.receipt += "Payment Successful"
                    self.print_label = ctk.CTkLabel(self.master, text=self.receipt)
                    self.print_label.pack(pady=20)
            else:
                messagebox.showerror("Error", "Please select a payment option.")

        elif(self.language == "French"):
            if self.payment_option:
                self.payment_label.pack_forget()
                self.payment_radio_frame.pack_forget()
                self.next_button.pack_forget()

                self.receipt = f"Langue: {self.language}\n"
                if self.option == "Recharger":
                    self.receipt += f"Age: {self.age}\n"
                self.receipt += f"Type de tarif: {self.fare}\n"
                self.receipt += f"Modalité de paiement: {self.payment_option}\n"

                if self.payment_option == "Espèces":
                    self.amount_label = ctk.CTkLabel(self.master, text="Entrer le montant:")
                    self.amount_label.pack(pady=20)

                    self.amount_entry = ctk.CTkEntry(self.master)
                    self.amount_entry.pack(pady=20)

                    self.pay_button = ctk.CTkButton(self.master, text="Payer", command=self.calculate_change)
                    self.pay_button.pack(pady=20)
                else:
                    self.receipt += "Paiement réussi"
                    self.print_label = ctk.CTkLabel(self.master, text=self.receipt)
                    self.print_label.pack(pady=20)
            else:
                messagebox.showerror("Erreur", "Veuillez sélectionner une option de paiement.")

    def calculate_change(self):
        self.amount = self.amount_entry.get()

        if self.language == "English":
            if self.amount:
                try:
                    self.amount = float(self.amount)
                    self.change = self.amount - self.prc
                    print(self.amount)
                    print(self.prc)

                    if self.change >= 0:
                        self.receipt += f"Amount Paid: {self.amount}\n"
                        self.receipt += f"Change: {self.change}\n"
                        self.receipt += "Payment Successful"

                        self.print_label = ctk.CTkLabel(self.master, text=self.receipt)
                        self.print_label.pack(pady=20)

                        self.email_receipt = ctk.CTkButton(self.master, text="Send Email Receipt", command=self.select_email_receipt)
                        self.email_receipt.pack(pady=20)
                    else:
                        messagebox.showerror("Error", "Insufficient amount.")
                except ValueError:
                    messagebox.showerror("Error", "Invalid amount.")
            else:
                messagebox.showerror("Error", "Please enter an amount.")

            # Create a Button to call close()
            # ctk.CTkButton(root, text="Close the Window", font=("Calibri", 12, "bold"), command=self.close).pack(pady=20)


        elif self.language == "French":
            if self.amount:
                try:
                    self.amount = float(self.amount)
                    self.change = self.amount - self.prc

                    if self.change >= 0:
                        self.receipt += f"Le montant payé: {self.amount}\n"
                        self.receipt += f"Changement: {self.change}\n"
                        self.receipt += "Paiement réussi"

                        self.print_label = ctk.CTkLabel(self.master, text=self.receipt)
                        self.print_label.pack(pady=20)

                        self.email_receipt = ctk.CTkButton(self.master, text="Envoyer un reçu par e-mail", command=self.select_email_receipt)
                        self.email_receipt.pack(pady=20)
                    else:
                        messagebox.showerror("Erreur", "Montant insuffisant.")
                except ValueError:
                    messagebox.showerror("Erreur", "Montant invalide.")
            else:
                messagebox.showerror("Erreur", "Veuillez saisir un montant.")

            # Create a Button to call close()
            # ctk.CTkButton(root, text="Ferme la fenêtre", font=("Calibri", 12, "bold"), command=self.close).pack(pady=10)

    def select_email_receipt(self):
        self.print_label.pack_forget()
        self.amount_label.pack_forget()
        self.pay_button.pack_forget()
        self.amount_entry.pack_forget()
        self.email_receipt.pack_forget()
        if self.language == "English":
            # self.email_receipt.pack_forget()
            self.email_label = ctk.CTkLabel(self.master, text="Enter E-mail id:")
            self.email_label.pack(pady=20)

            self.email_entry = ctk.CTkEntry(self.master)
            self.email_entry.pack(pady=20)

            self.email_receipt = ctk.CTkButton(self.master, text="Send",
                                               command=self.select_send)
            self.email_receipt.pack(pady=20)

        elif self.language == "French":
            self.email_label = ctk.CTkLabel(self.master, text="Entrez l'identifiant e-mail :")
            self.email_label.pack(pady=20)

            self.email_entry = ctk.CTkEntry(self.master)
            self.email_entry.pack(pady=20)

            self.email_receipt = ctk.CTkButton(self.master, text="Envoyer",
                                               command=self.select_send)
            self.email_receipt.pack(pady=20)


    def select_send(self):
        if self.language == "English":
            self.print_email = ctk.CTkLabel(self.master, text="Email Receipt Sent Successfully")
            self.print_email.pack(pady=20)
        elif self.language == "French":
            self.print_email = ctk.CTkLabel(self.master, text="Reçu par e-mail envoyé avec succès")
            self.print_email.pack(pady=20)

    def exit(self):
        self.master.destroy()

    # Define a function to close the window
    def close(self):
        self.master.quit()

if __name__ == "__main__":
    # Sets the appearance mode of the application
    # "System" sets the appearance same as that of the system
    ctk.set_appearance_mode("System")

    # Sets the color of the widgets
    # Supported themes: green, dark-blue, blue
    ctk.set_default_color_theme("green")
    root = ctk.CTk()
    # image = Image.open("C:/Users/Admin/Desktop/SDM Deliverable#2/Code/images/My First Board.jpg")
    # bg_image = ImageTk.PhotoImage(image)
    # canvas = Canvas(root, width=800, height=600)
    # canvas.create_image(0, 0, image=bg_image, anchor="nw")
    ticket_vending_system = TicketVendingMachine(root)
    root.mainloop()

