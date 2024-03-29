from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
from PIL import ImageTk, Image
from datetime import datetime
import re


class TicketVendingMachine:

    def __init__(self, master):
        self.master = master
        self.master.title("iGo Ticket Vending System")
        self.master.geometry("1000x700")
        self.master.resizable(False, False)

        self.tit = ctk.CTkFrame(master=self.master, fg_color="orange")
        self.tit.pack(side="top", fill="both")
        self.title_label = ctk.CTkLabel(self.tit, text="iGo TVM", font=('Grotesco',30))
        self.title_label.pack(pady=20)

        image = Image.open("images/img1.jpg")
        img = image.resize((1500, 800))
        img1 = ImageTk.PhotoImage(img)
        self.img = ctk.CTkLabel(self.master, image=img1, text="", width=0, height=0)
        self.img.place(x=0, y=100)

        self.language_label = ctk.CTkLabel(self.master, text="Select a language:", font=('Davish',20))
        self.language_label.pack(pady=100)

        self.language_var = StringVar()
        self.language_var.set(None)

        self.language_radio_frame = ctk.CTkFrame(master=self.master, fg_color="white")
        self.language_radio_frame.pack(pady=20)

        self.english_radio_button = ctk.CTkRadioButton(self.language_radio_frame, text="English",
                                                       variable=self.language_var,
                                                       value="English", font=('Davish',20))
        self.english_radio_button.pack(side=LEFT, padx=10)

        self.french_radio_button = ctk.CTkRadioButton(self.language_radio_frame, text="French",
                                                      variable=self.language_var,
                                                      value="French", font=('Davish',20))
        self.french_radio_button.pack(side=LEFT, padx=10)

        self.next_button = ctk.CTkButton(self.master, text="Next", command=self.select_option, corner_radius=0, font=('Davish',20))
        self.next_button.pack(pady=20)

    def select_option(self):
        self.img.place_forget()
        image = Image.open("images/img3.jpg")
        img = image.resize((1500, 800))
        img1 = ImageTk.PhotoImage(img)
        self.img = ctk.CTkLabel(self.master, image=img1, text="", width=0, height=0)
        self.img.place(x=0, y=100)

        self.language = self.language_var.get()

        if self.language == 'English':
            if self.language:
                self.tit.pack_forget()
                self.language_label.pack_forget()
                self.title_label.forget()
                self.language_radio_frame.pack_forget()
                self.next_button.pack_forget()

                self.tit = ctk.CTkFrame(master=self.master, fg_color="orange")
                self.tit.pack(side="top", fill="both")

                self.title_label = ctk.CTkLabel(self.tit, text="Welcome to the iGo Ticket Vending Machine", font=('Grotesco',30))
                self.title_label.pack(pady=20)

                self.option_label = ctk.CTkLabel(self.master, text="Select an option:", font=('Davish',20))
                self.option_label.pack(pady=100)

                self.option_var = StringVar()
                self.option_var.set(None)

                self.option_radio_frame = ctk.CTkFrame(master=self.master, fg_color="white")
                self.option_radio_frame.pack(pady=20)

                self.recharge_radio_button = ctk.CTkRadioButton(self.option_radio_frame, text="Recharge card",
                                                                variable=self.option_var, value="Recharge", font=('Davish',20))
                self.recharge_radio_button.pack(side=LEFT, padx=30)

                self.buy_radio_button = ctk.CTkRadioButton(self.option_radio_frame, text="Buy new ticket",
                                                           variable=self.option_var, value="Buy", font=('Davish',20))
                self.buy_radio_button.pack(side=LEFT, padx=30)

                self.next_button = ctk.CTkButton(self.master, text="Next", command=self.select_age_group, corner_radius=0,
                                                 font=('Davish', 20))
                self.next_button.pack(pady=20)
            else:
                messagebox.showerror("Error", "Please select a language.")

        if self.language == 'French':
            if self.language:
                self.tit.pack_forget()
                self.language_label.pack_forget()
                self.language_radio_frame.pack_forget()
                self.next_button.pack_forget()

                self.tit = ctk.CTkFrame(master=self.master, fg_color="orange")
                self.tit.pack(side="top", fill="both")

                self.title_label = ctk.CTkLabel(self.tit,
                                                text="Bienvenue sur le distributeur automatique de billets iGo", font=('Grotesco',30))
                self.title_label.pack(pady=20)

                self.option_label = ctk.CTkLabel(self.master, text="Choisir une option:", font=('Davish',20))
                self.option_label.pack(pady=100)

                self.option_var = StringVar()
                self.option_var.set(None)

                self.option_radio_frame = ctk.CTkFrame(master=self.master, fg_color="white")
                self.option_radio_frame.pack(pady=20)

                self.recharge_radio_button = ctk.CTkRadioButton(self.option_radio_frame, text="Carte de recharge",
                                                                variable=self.option_var, value="Recharger", font=('Davish',20))
                self.recharge_radio_button.pack(side=LEFT, padx=30)

                self.buy_radio_button = ctk.CTkRadioButton(self.option_radio_frame, text="Acheter un ticket",
                                                           variable=self.option_var, value="Acheter", font=('Davish',20))
                self.buy_radio_button.pack(side=LEFT, padx=30)

                self.next_button = ctk.CTkButton(self.master, text="Prochain", command=self.select_age_group, corner_radius=0,
                                                 font=('Davish', 20))
                self.next_button.pack(pady=20)
            else:
                messagebox.showerror("Erreur", "Veuillez sélectionner une langue.")

    def select_age_group(self):
        self.img.place_forget()
        image = Image.open("images/img2.jpg")
        img = image.resize((1500, 800))
        img1 = ImageTk.PhotoImage(img)
        self.img = ctk.CTkLabel(self.master, image=img1, text="", width=0, height=0)
        self.img.place(x=0, y=100)
        self.option = self.option_var.get()

        if self.option == 'Recharge':
            if self.language == 'English':
                if self.option:
                    self.next_button.pack_forget()
                    self.option_label.pack_forget()
                    self.option_radio_frame.pack_forget()
                    self.next_button.pack_forget()
                    self.tit.pack_forget()
                    self.title_label.pack_forget()

                    self.tit = ctk.CTkFrame(master=self.master, fg_color="orange")
                    self.tit.pack(side="top", fill="both")
                    self.title_label = ctk.CTkLabel(self.tit, text="iGo TVM", font=('Grotesco', 30))
                    self.title_label.pack(pady=20)

                    self.age_label = ctk.CTkLabel(self.master, text="Select age group:", font=('Davish',20))
                    self.age_label.pack(pady=100)

                    self.age_var = StringVar()
                    self.age_var.set(None)

                    self.age_radio_frame = ctk.CTkFrame(master=self.master, fg_color="white")
                    self.age_radio_frame.pack(pady=20)

                    self.adult_radio_button = ctk.CTkRadioButton(self.age_radio_frame, text="Adult",
                                                                 variable=self.age_var,
                                                                 value="Adult", font=('Davish',20))
                    self.adult_radio_button.pack(side=LEFT, padx=10)

                    self.child_radio_button = ctk.CTkRadioButton(self.age_radio_frame, text="Child",
                                                                 variable=self.age_var,
                                                                 value="Child", font=('Davish',20))
                    self.child_radio_button.pack(side=LEFT, padx=10)

                    self.senior_radio_button = ctk.CTkRadioButton(self.age_radio_frame, text="Senior",
                                                                  variable=self.age_var,
                                                                  value="Senior", font=('Davish',20))
                    self.senior_radio_button.pack(side=LEFT, padx=10)

                    self.next_button = ctk.CTkButton(self.master, text="Next", command=self.select_fare, font=('Davish',20), corner_radius=0)
                    self.next_button.pack(pady=20)
                else:
                    messagebox.showerror("Error", "Please select an option.")

        elif self.option == 'Buy':
            if self.language == 'English':
                if self.option:
                    self.next_button.pack_forget()
                    self.option_label.pack_forget()
                    self.option_radio_frame.pack_forget()
                    self.next_button.pack_forget()
                    self.tit.pack_forget()
                    self.title_label.forget()

                    self.tit = ctk.CTkFrame(master=self.master, fg_color="orange")
                    self.tit.pack(side="top", fill="both")
                    self.title_label = ctk.CTkLabel(self.tit, text="iGo TVM", font=('Grotesco', 30))
                    self.title_label.pack(pady=20)

                    self.fare_label = ctk.CTkLabel(self.master, text="Select fare type:", font=('Davish',20))
                    self.fare_label.pack(pady=100)

                    self.fare_var = StringVar()
                    self.fare_var.set(None)

                    self.fare_prc = IntVar()
                    self.fare_prc.set(0)

                    self.fare_radio_frame = ctk.CTkFrame(master=self.master, fg_color="white")
                    self.fare_radio_frame.pack(pady=20)

                    self.trip1_button = ctk.CTkRadioButton(self.fare_radio_frame, text="1 Trip (3)",
                                                           variable=self.fare_var,
                                                           value="1 Trip", font=('Davish',20))
                    self.trip1_button.pack(side=LEFT, padx=10)

                    self.trip2_button = ctk.CTkRadioButton(self.fare_radio_frame, text="2 Trip (6)",
                                                           variable=self.fare_var,
                                                           value="2 Trip", font=('Davish',20))
                    self.trip2_button.pack(side=LEFT, padx=10)

                    self.day_trip_button = ctk.CTkRadioButton(self.fare_radio_frame, text="1 Day Trip (10)",
                                                              variable=self.fare_var,
                                                              value="1 Day Trip", font=('Davish',20))
                    self.day_trip_button.pack(side=LEFT, padx=10)

                    self.next_button = ctk.CTkButton(self.master, text="Next", command=self.select_payment_option, font=('Davish',20), corner_radius=0)
                    self.next_button.pack(pady=20)
                else:
                    messagebox.showerror("Error", "Please select an option.")

        if self.option == 'Recharger':
            if self.language == 'French':
                if self.option:
                    self.next_button.pack_forget()
                    self.option_label.pack_forget()
                    self.option_radio_frame.pack_forget()
                    self.next_button.pack_forget()
                    self.tit.pack_forget()
                    self.title_label.forget()

                    self.tit = ctk.CTkFrame(master=self.master, fg_color="orange")
                    self.tit.pack(side="top", fill="both")
                    self.title_label = ctk.CTkLabel(self.tit, text="iGo TVM", font=('Grotesco', 30))
                    self.title_label.pack(pady=20)

                    self.age_label = ctk.CTkLabel(self.master, text="Sélectionnez le groupe d'âge :", font=('Davish',20))
                    self.age_label.pack(pady=100)

                    self.age_var = StringVar()
                    self.age_var.set(None)

                    self.age_radio_frame = ctk.CTkFrame(master=self.master, fg_color="white")
                    self.age_radio_frame.pack(pady=20)

                    self.adult_radio_button = ctk.CTkRadioButton(self.age_radio_frame, text="Adulte",
                                                                 variable=self.age_var,
                                                                 value="Adulte", font=('Davish',20))
                    self.adult_radio_button.pack(side=LEFT, padx=10)

                    self.child_radio_button = ctk.CTkRadioButton(self.age_radio_frame, text="Enfant",
                                                                 variable=self.age_var,
                                                                 value="Enfant", font=('Davish',20))
                    self.child_radio_button.pack(side=LEFT, padx=10)

                    self.senior_radio_button = ctk.CTkRadioButton(self.age_radio_frame, text="Senior",
                                                                  variable=self.age_var,
                                                                  value="Senior", font=('Davish',20))
                    self.senior_radio_button.pack(side=LEFT, padx=10)

                    self.next_button = ctk.CTkButton(self.master, text="Prochain", command=self.select_fare, corner_radius=0)
                    self.next_button.pack(pady=20)
                else:
                    messagebox.showerror("Erreur", "Veuillez sélectionner une option.")

        elif self.option == 'Acheter':
            if self.language == 'French':
                if self.option:
                    self.next_button.pack_forget()
                    self.option_label.pack_forget()
                    self.option_radio_frame.pack_forget()
                    self.next_button.pack_forget()
                    self.tit.pack_forget()
                    self.title_label.forget()

                    self.tit = ctk.CTkFrame(master=self.master, fg_color="orange")
                    self.tit.pack(side="top", fill="both")
                    self.title_label = ctk.CTkLabel(self.tit, text="iGo TVM", font=('Grotesco', 30))
                    self.title_label.pack(pady=20)

                    self.fare_label = ctk.CTkLabel(self.master, text="Sélectionnez le type de tarif :", font=('Davish',20))
                    self.fare_label.pack(pady=100)

                    self.fare_var = StringVar()
                    self.fare_var.set(None)

                    self.fare_prc = IntVar()
                    self.fare_prc.set(0)

                    self.fare_radio_frame = ctk.CTkFrame(master=self.master, fg_color="white")
                    self.fare_radio_frame.pack(pady=20)

                    self.trip1_button = ctk.CTkRadioButton(self.fare_radio_frame, text="1 voyage (3)",
                                                           variable=self.fare_var,
                                                           value="1 voyage", font=('Davish',20))
                    self.trip1_button.pack(side=LEFT, padx=10)

                    self.trip2_button = ctk.CTkRadioButton(self.fare_radio_frame, text="2 voyage (6)",
                                                           variable=self.fare_var,
                                                           value="2 voyage", font=('Davish',20))
                    self.trip2_button.pack(side=LEFT, padx=10)

                    self.day_trip_button = ctk.CTkRadioButton(self.fare_radio_frame,
                                                              text="Excursion d'une journée (10)",
                                                              variable=self.fare_var,
                                                              value="Excursion d'une journée", font=('Davish',20))
                    self.day_trip_button.pack(side=LEFT, padx=10)

                    self.next_button = ctk.CTkButton(self.master, text="Prochain", command=self.select_payment_option, font=('Davish',20), corner_radius=0)
                    self.next_button.pack(pady=20)
                else:
                    messagebox.showerror("Erreur", "Veuillez sélectionner une option.")

    def select_fare(self):
        self.img.place_forget()
        image = Image.open("images/img4.jpg")
        img = image.resize((1500, 800))
        img1 = ImageTk.PhotoImage(img)
        self.img = ctk.CTkLabel(self.master, image=img1, text="", width=0, height=0)
        self.img.place(x=0, y=100)
        self.age = self.age_var.get()

        if self.language == 'English':
            if self.age:
                self.age_label.pack_forget()
                self.age_radio_frame.pack_forget()
                self.next_button.pack_forget()
                self.fare_label = ctk.CTkLabel(self.master, text="Select fare type:", font=('Davish',20))
                self.fare_label.pack(pady=100)

                self.fare_var = StringVar()
                self.fare_var.set(None)

                self.fare_prc = IntVar()
                self.fare_prc.set(0)

                self.fare_radio_frame = ctk.CTkFrame(master=self.master, fg_color="white")
                self.fare_radio_frame.pack(pady=20)

                if self.age == "Adult":
                    self.monthly_radio_button = ctk.CTkRadioButton(self.fare_radio_frame, text="1 Month Pass (100)",
                                                                   variable=self.fare_var, value="Monthly", font=('Davish',20))
                    self.monthly_radio_button.pack(side=LEFT, padx=20)

                    self.weekly_radio_button = ctk.CTkRadioButton(self.fare_radio_frame, text="1 Week Pass (50)",
                                                                  variable=self.fare_var, value="Weekly", font=('Davish',20))
                    self.weekly_radio_button.pack(side=LEFT, padx=20)

                    self.daily_radio_button = ctk.CTkRadioButton(self.fare_radio_frame, text="1 Day Pass (10)",
                                                                 variable=self.fare_var, value="Daily", font=('Davish',20))
                    self.daily_radio_button.pack(side=LEFT, padx=20)

                elif self.age == "Child":
                    self.monthly_radio_button = ctk.CTkRadioButton(self.fare_radio_frame,
                                                                   text="Child 1 Month Pass (50)",
                                                                   variable=self.fare_var, value="Child Monthly", font=('Davish',20))
                    self.monthly_radio_button.pack(side=LEFT, padx=20)

                    self.weekly_radio_button = ctk.CTkRadioButton(self.fare_radio_frame, text="Child 1 Week Pass (30)",
                                                                  variable=self.fare_var, value="Child Weekly", font=('Davish',20))
                    self.weekly_radio_button.pack(side=LEFT, padx=20)

                    self.daily_radio_button = ctk.CTkRadioButton(self.fare_radio_frame, text="Child 1 Day Pass (5)",
                                                                 variable=self.fare_var, value="Child Daily", font=('Davish',20))
                    self.daily_radio_button.pack(side=LEFT, padx=20)

                elif self.age == "Senior":
                    self.monthly_radio_button = ctk.CTkRadioButton(self.fare_radio_frame,
                                                                   text="Senior 1 Month Pass (75)",
                                                                   variable=self.fare_var, value="Senior Monthly", font=('Davish',20))
                    self.monthly_radio_button.pack(side=LEFT, padx=20)

                    self.weekly_radio_button = ctk.CTkRadioButton(self.fare_radio_frame, text="Senior 1 Week Pass (40)",
                                                                  variable=self.fare_var, value="Senior Weekly", font=('Davish',20))
                    self.weekly_radio_button.pack(side=LEFT, padx=20)

                    self.daily_radio_button = ctk.CTkRadioButton(self.fare_radio_frame, text="Senior 1 Day Pass (7)",
                                                                 variable=self.fare_var, value="Senior Daily", font=('Davish',20))
                    self.daily_radio_button.pack(side=LEFT, padx=20)

                self.next_button = ctk.CTkButton(self.master, text="Next", command=self.select_payment_option, corner_radius=0, font=('Davish',20))
                self.next_button.pack(pady=20)

            else:
                messagebox.showerror("Error", "Please select an age group.")



        elif self.language == 'French':
            if self.age:
                self.age_label.pack_forget()
                self.age_radio_frame.pack_forget()
                self.next_button.pack_forget()
                self.fare_label = ctk.CTkLabel(self.master, text="Sélectionnez le type de tarif :", font=('Davish',20))
                self.fare_label.pack(pady=100)

                self.fare_var = StringVar()
                self.fare_var.set(None)

                self.fare_prc = IntVar()
                self.fare_prc.set(0)

                self.fare_radio_frame = ctk.CTkFrame(master=self.master, fg_color="white")
                self.fare_radio_frame.pack(pady=20)

                if self.age == "Adulte":
                    self.monthly_radio_button = ctk.CTkRadioButton(self.fare_radio_frame, text="Pass 1 mois (100)",
                                                                   variable=self.fare_var, value="Mensuel", font=('Davish',20))
                    self.monthly_radio_button.pack(side=LEFT)

                    self.weekly_radio_button = ctk.CTkRadioButton(self.fare_radio_frame, text="Pass 1 semaine (50)",
                                                                  variable=self.fare_var, value="Hebdomadaire", font=('Davish',20))
                    self.weekly_radio_button.pack(side=LEFT, padx=20)

                    self.daily_radio_button = ctk.CTkRadioButton(self.fare_radio_frame, text="Pass 1 jour (10)",
                                                                 variable=self.fare_var, value="Quotidien", font=('Davish',20))
                    self.daily_radio_button.pack(side=LEFT, padx=20)

                elif self.age == "Enfant":
                    self.monthly_radio_button = ctk.CTkRadioButton(self.fare_radio_frame,
                                                                   text="Pass Enfant 1 Mois (50)",
                                                                   variable=self.fare_var, value="Enfant Mensuel", font=('Davish',20))
                    self.monthly_radio_button.pack(side=LEFT)

                    self.weekly_radio_button = ctk.CTkRadioButton(self.fare_radio_frame,
                                                                  text="Pass 1 Semaine Enfant (30)",
                                                                  variable=self.fare_var, value="Enfant Hebdomadaire", font=('Davish',20))
                    self.weekly_radio_button.pack(side=LEFT, padx=20)

                    self.daily_radio_button = ctk.CTkRadioButton(self.fare_radio_frame, text="Pass Enfant 1 Jour (5)",
                                                                 variable=self.fare_var, value="Enfant Quotidien", font=('Davish',20))
                    self.daily_radio_button.pack(side=LEFT, padx=20)

                elif self.age == "Senior":
                    self.monthly_radio_button = ctk.CTkRadioButton(self.fare_radio_frame,
                                                                   text="Forfait Sénior 1 Mois (75)",
                                                                   variable=self.fare_var, value="Sénior Mensuel", font=('Davish',20))
                    self.monthly_radio_button.pack(side=LEFT)

                    self.weekly_radio_button = ctk.CTkRadioButton(self.fare_radio_frame,
                                                                  text="Forfait Sénior 1 Semaine (40)",
                                                                  variable=self.fare_var, value="Senior Hebdomadaire", font=('Davish',20))
                    self.weekly_radio_button.pack(side=LEFT, padx=20)

                    self.daily_radio_button = ctk.CTkRadioButton(self.fare_radio_frame, text="Pass 1 jour sénior (7)",
                                                                 variable=self.fare_var, value="Sénior Quotidien", font=('Davish',20))
                    self.daily_radio_button.pack(side=LEFT, padx=20)

                self.next_button = ctk.CTkButton(self.master, text="Prochain", command=self.select_payment_option, corner_radius=0, font=('Davish',20))
                self.next_button.pack(pady=20)

            else:
                messagebox.showerror("Erreur", "Veuillez sélectionner une tranche d'âge.")

    def select_payment_option(self):
        self.img.place_forget()
        image = Image.open("images/img5.jpg")
        img = image.resize((1500, 800))
        img1 = ImageTk.PhotoImage(img)
        self.img = ctk.CTkLabel(self.master, image=img1, text="", width=0, height=0)
        self.img.place(x=0, y=100)
        self.fare = self.fare_var.get()
        self.prc = self.fare_prc.get()
        self.option = self.option_var.get()

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

                self.payment_label = ctk.CTkLabel(self.master, text="Select payment option:", font=('Davish',20))
                self.payment_label.pack(pady=100)

                self.payment_var = StringVar()
                self.payment_var.set(None)

                self.payment_radio_frame = ctk.CTkFrame(master=self.master, fg_color="white")
                self.payment_radio_frame.pack(pady=20)

                self.cash_radio_button = ctk.CTkRadioButton(self.payment_radio_frame, text="Cash",
                                                            variable=self.payment_var,
                                                            value="Cash", font=('Davish',20))
                self.cash_radio_button.pack(side=LEFT)

                self.card_radio_button = ctk.CTkRadioButton(self.payment_radio_frame, text="Card",
                                                            variable=self.payment_var,
                                                            value="Card", font=('Davish',20))
                self.card_radio_button.pack(side=LEFT)

                self.next_button = ctk.CTkButton(self.master, text="Pay", command=self.print_receipt, font=('Davish',20), corner_radius=0)
                self.next_button.pack(pady=20)
            else:
                messagebox.showerror("Error", "Please select a fare type.")

        elif self.language == "French":
            if self.fare:
                self.fare_label.pack_forget()
                self.fare_radio_frame.pack_forget()
                self.next_button.pack_forget()

                self.payment_label = ctk.CTkLabel(self.master, text="Sélectionnez l'option de paiement :", font=('Davish',20))
                self.payment_label.pack(pady=100)

                self.payment_var = StringVar()
                self.payment_var.set(None)

                self.payment_radio_frame = ctk.CTkFrame(self.master)
                self.payment_radio_frame.pack(pady=20)

                self.cash_radio_button = ctk.CTkRadioButton(self.payment_radio_frame, text="Espèces",
                                                            variable=self.payment_var,
                                                            value="Espèces", font=('Davish',20))
                self.cash_radio_button.pack(side=LEFT)

                self.card_radio_button = ctk.CTkRadioButton(self.payment_radio_frame, text="Carte",
                                                            variable=self.payment_var,
                                                            value="Carte", font=('Davish',20))
                self.card_radio_button.pack(side=LEFT)

                self.next_button = ctk.CTkButton(self.master, text="Payer", command=self.print_receipt, font=('Davish',20), corner_radius=0)
                self.next_button.pack(pady=20)
            else:
                messagebox.showerror("Erreur", "Veuillez sélectionner un type de tarif.")

    def print_receipt(self):
        self.img.place_forget()
        image = Image.open("images/img6.jpg")
        img = image.resize((1500, 800))
        img1 = ImageTk.PhotoImage(img)
        self.img = ctk.CTkLabel(self.master, image=img1, text="", width=0, height=0)
        self.img.place(x=0, y=100)
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
                self.receipt += f"Amount Paid: {self.prc}\n"

                if self.payment_option == "Cash":
                    self.amount_label = ctk.CTkLabel(self.master, text="Enter amount:", font=('Davish',20))
                    self.amount_label.pack(pady=100)

                    self.amount_entry = ctk.CTkEntry(self.master)
                    self.amount_entry.pack(pady=20)

                    self.pay_button = ctk.CTkButton(self.master, text="Pay", command=self.calculate_change, font=('Davish',20), corner_radius=0)
                    self.pay_button.pack(pady=20)
                else:
                    self.success = "Payment Successful\n"
                    self.success += f"Timestamp: {str(datetime.now())}\n"
                    self.print_success = ctk.CTkLabel(self.master, text=self.success, font=('Davish',20))
                    self.print_success.pack(pady=100)

                    self.paper_receipt = ctk.CTkButton(self.master, text="Print Paper Receipt",
                                                       command=self.print_paper_receipt, font=('Davish',20), corner_radius=0)
                    self.paper_receipt.pack(pady=20)

                    self.email_receipt = ctk.CTkButton(self.master, text="Send Email Receipt",
                                                       command=self.select_email_receipt, font=('Davish',20), corner_radius=0)
                    self.email_receipt.pack(pady=20)
            else:
                messagebox.showerror("Error", "Please select a payment option.")

        elif (self.language == "French"):
            if self.payment_option:
                self.payment_label.pack_forget()
                self.payment_radio_frame.pack_forget()
                self.next_button.pack_forget()

                self.receipt = f"Langue: {self.language}\n"
                if self.option == "Recharger":
                    self.receipt += f"Age: {self.age}\n"
                self.receipt += f"Type de tarif: {self.fare}\n"
                self.receipt += f"Modalité de paiement: {self.payment_option}\n"
                self.receipt += f"Le montant payé: {self.prc}\n"

                if self.payment_option == "Espèces":
                    self.amount_label = ctk.CTkLabel(self.master, text="Entrer le montant:", font=('Davish',20))
                    self.amount_label.pack(pady=100)

                    self.amount_entry = ctk.CTkEntry(self.master)
                    self.amount_entry.pack(pady=20)

                    self.pay_button = ctk.CTkButton(self.master, text="Payer", command=self.calculate_change, font=('Davish',20), corner_radius=0)
                    self.pay_button.pack(pady=20)
                else:
                    self.success = "Paiement réussi\n"
                    self.success += f"Horodatage: {str(datetime.now())}\n"
                    self.print_success = ctk.CTkLabel(self.master, text=self.success)
                    self.print_success.pack(pady=50)

                    self.paper_receipt = ctk.CTkButton(self.master, text="Imprimer le reçu papier",
                                                       command=self.print_paper_receipt, font=('Davish',20), corner_radius=0)
                    self.paper_receipt.pack(pady=20)

                    self.email_receipt = ctk.CTkButton(self.master, text="Envoyer un reçu par e-mail",
                                                       command=self.select_email_receipt, font=('Davish',20), corner_radius=0)
                    self.email_receipt.pack(pady=20)
            else:
                messagebox.showerror("Erreur", "Veuillez sélectionner une option de paiement.")

    def calculate_change(self):
        self.amount_label.pack_forget()
        self.amount_entry.pack_forget()
        self.pay_button.pack_forget()
        self.img.place_forget()
        image = Image.open("images/img3.jpg")
        img = image.resize((1500, 800))
        img1 = ImageTk.PhotoImage(img)
        self.img = ctk.CTkLabel(self.master, image=img1, text="", width=0, height=0)
        self.img.place(x=0, y=100)
        self.amount = self.amount_entry.get()

        if self.language == "English":
            if self.amount:
                try:
                    self.amount = float(self.amount)
                    self.change = self.amount - self.prc

                    if self.change >= 0:
                        self.receipt += f"Amount Paid: {self.amount}\n"
                        self.receipt += f"Change: {self.change}\n"
                        self.success = "Payment Successful\n"
                        self.success += f"Timestamp: {str(datetime.now())}\n"

                        self.print_success = ctk.CTkLabel(self.master, text=self.success, font=('Davish',20))
                        self.print_success.pack(pady=100)

                        self.paper_receipt = ctk.CTkButton(self.master, text="Print Paper Receipt",
                                                           command=self.print_paper_receipt, font=('Davish',20), corner_radius=0)
                        self.paper_receipt.pack(pady=20)

                        self.email_receipt = ctk.CTkButton(self.master, text="Send Email Receipt",
                                                           command=self.select_email_receipt, font=('Davish',20), corner_radius=0)
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
                        self.success = "Paiement réussi\n"
                        self.success += f"Horodatage: {str(datetime.now())}\n"

                        self.print_success = ctk.CTkLabel(self.master, text=self.success, font=('Davish',20))
                        self.print_success.pack(pady=100)

                        self.paper_receipt = ctk.CTkButton(self.master, text="Imprimer le reçu papier",
                                                           command=self.print_paper_receipt, font=('Davish',20), corner_radius=0)
                        self.paper_receipt.pack(pady=20)

                        self.email_receipt = ctk.CTkButton(self.master, text="Envoyer un reçu par e-mail",
                                                           command=self.select_email_receipt, font=('Davish',20), corner_radius=0)
                        self.email_receipt.pack(pady=20)
                    else:
                        messagebox.showerror("Erreur", "Montant insuffisant.")
                except ValueError:
                    messagebox.showerror("Erreur", "Montant invalide.")
            else:
                messagebox.showerror("Erreur", "Veuillez saisir un montant.")

            # Create a Button to call close()
            # ctk.CTkButton(root, text="Ferme la fenêtre", font=("Calibri", 12, "bold"), command=self.close).pack(pady=10)

    def print_paper_receipt(self):
        self.img.place_forget()
        image = Image.open("images/img1.jpg")
        img = image.resize((1500, 800))
        img1 = ImageTk.PhotoImage(img)
        self.img = ctk.CTkLabel(self.master, image=img1, text="", width=0, height=0)
        self.img.place(x=0, y=100)
        if self.payment_option == "Cash":
            self.amount_label.pack_forget()
            self.pay_button.pack_forget()
            self.amount_entry.pack_forget()
            self.email_receipt.pack_forget()
            self.paper_receipt.pack_forget()
            self.print_success.pack_forget()
        if self.payment_option == "Card":
            self.email_receipt.pack_forget()
            self.paper_receipt.pack_forget()
            self.print_success.pack_forget()
        if self.language == "English":
            self.email_label = ctk.CTkLabel(self.master, text="Paper Receipt:\n", font=('Davish',20))
            self.email_label.pack(pady=100)
        else:
            self.email_label = ctk.CTkLabel(self.master, text="Reçu papier:\n", font=('Davish',20))
            self.email_label.pack(pady=100)

        self.print_label = ctk.CTkLabel(self.master, text=self.receipt, font=('Davish',20))
        self.print_label.pack(pady=20)

    def select_email_receipt(self):
        self.img.place_forget()
        image = Image.open("images/img2.jpg")
        img = image.resize((1500, 800))
        img1 = ImageTk.PhotoImage(img)
        self.img = ctk.CTkLabel(self.master, image=img1, text="", width=0, height=0)
        self.img.place(x=0, y=100)
        if self.payment_option == "Cash":
            self.amount_label.pack_forget()
            self.pay_button.pack_forget()
            self.amount_entry.pack_forget()
            self.email_receipt.pack_forget()
            self.paper_receipt.pack_forget()
            self.print_success.pack_forget()
        if self.payment_option == "Card":
            self.email_receipt.pack_forget()
            self.paper_receipt.pack_forget()
            self.print_success.pack_forget()
        if self.language == "English":
            # self.email_receipt.pack_forget()
            self.email_label = ctk.CTkLabel(self.master, text="Enter E-mail id:", font=('Davish',20))
            self.email_label.pack(pady=100)

            self.email_entry = ctk.CTkEntry(self.master)
            self.email_entry.pack(pady=20)

            self.email_receipt = ctk.CTkButton(self.master, text="Send",
                                               command=self.select_send, font=('Davish',20), corner_radius=0)
            self.email_receipt.pack(pady=20)

        elif self.language == "French":
            self.email_label = ctk.CTkLabel(self.master, text="Entrez l'identifiant e-mail :", font=('Davish',20))
            self.email_label.pack(pady=100)

            self.email_entry = ctk.CTkEntry(self.master)
            self.email_entry.pack(pady=20)

            self.email_receipt = ctk.CTkButton(self.master, text="Envoyer",
                                               command=self.select_send, font=('Davish',20), corner_radius=0)
            self.email_receipt.pack(pady=20)

    def select_send(self):
        self.img.place_forget()
        image = Image.open("images/img5.jpg")
        img = image.resize((1500, 800))
        img1 = ImageTk.PhotoImage(img)
        self.img = ctk.CTkLabel(self.master, image=img1, text="", width=0, height=0)
        self.img.place(x=0, y=100)
        self.regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        self.email = self.email_entry.get()
        if self.language == "English":
            if re.fullmatch(self.regex, self.email):
                self.print_email = ctk.CTkLabel(self.master, text="Email Receipt Sent Successfully", font=('Davish',20))
                self.print_email.pack(pady=20)
            else:
                messagebox.showerror("Error", "Please enter a valid e-mail.")

        elif self.language == "French":
            if re.fullmatch(self.regex, self.email):
                self.print_email = ctk.CTkLabel(self.master, text="Reçu par e-mail envoyé avec succès", font=('Davish',20))
                self.print_email.pack(pady=20)
            else:
                messagebox.showerror("Erreur", "Veuillez entrer un e-mail valide.")

    def exit(self):
        self.master.destroy()

    # Define a function to close the window
    def close(self):
        self.master.quit()


if __name__ == "__main__":
    ctk.set_appearance_mode("System")

    # Sets the color of the widgets
    # Supported themes: green, dark-blue, blue
    ctk.set_default_color_theme("green")
    root = ctk.CTk()

    ticket_vending_system = TicketVendingMachine(root)
    root.mainloop()
