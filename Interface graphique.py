import webbrowser
from tkinter import *
import yfinance as yf
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def open_link(url):
    webbrowser.open_new(url)


def ouvrir():
    # Nouvelle fenêtre
    fenetre2 = Toplevel(fenetre)
    fenetre2.title("Finance")
    fenetre2.geometry("1920x1080")
    fenetre2.configure(background="floral white")

    liste = Listbox(fenetre2, width=32)
    x = list(stocks.keys())
    for i in range(len(x)):
        liste.insert(END, x[i])

    liste.config(font=('Arial', 16))
    liste.pack(side="left")

    def update_info(event):
        selected_stock = liste.get(liste.curselection())
        ticker = stocks[selected_stock]

        #Afficher les informations
        info_frame = LabelFrame(fenetre2, text=f"Informations de {selected_stock}", padx=20, pady=20)
        info_frame.config(font=('Arial', 24))
        info_frame.pack(fill="both", expand="yes")

        info = ticker.info
        directeur = "Inconnu"
        for people in info.get('companyOfficers', []):
            if 'CEO' in people.get('title', ''):
                directeur = people['name']

        info_label = Label(info_frame, text=f" Directeur : {directeur}")
        info_label.config(font=('Arial', 16))
        info_label.pack()

        info_label = Label(info_frame, text=f" Pays : {info['country']}")
        info_label.config(font=('Arial', 16))
        info_label.pack()

        info_label = Label(info_frame, text=f" Secteur : {info['sector']}")
        info_label.config(font=('Arial', 16))
        info_label.pack()

        employes = info["fullTimeEmployees"] if (info["fullTimeEmployees"])  else 'inconnu'

        info_label = Label(info_frame, text=f"Nombre d'employés : {employes}")
        info_label.config(font=('Arial', 16))
        info_label.pack()

        # Afficher les actualités
        actu_frame = LabelFrame(fenetre2, text=f"Actualités avec mention de {selected_stock}", padx=20, pady=20)
        actu_frame.config(font=('Arial', 24))
        actu_frame.pack(fill="both", expand="yes")

        news = ticker.news
        for item in news:
            link_label = Label(actu_frame, text=item['title'], fg="blue", cursor="hand2")
            link_label.config(font=('Arial', 16))
            link_label.pack()
            link_label.bind("<Button-1>", lambda e, url=item['link']: open_link(url))


        # Afficher le graphique

        # Extraire les revenus (Total Revenue)
        income_statement = ticker.financials
        revenues = income_statement.loc['Total Revenue']

        graph_frame = LabelFrame(fenetre2, text=f"Revenus de {selected_stock}", padx=20, pady=20)
        graph_frame.config(font=('Arial', 24))
        graph_frame.pack(fill="both", expand="yes")
        
        fig = Figure(figsize=(10, 6), dpi=100)
        plot1 = fig.add_subplot(111)
        plot1.plot(revenues.index, revenues.values, marker='o')
        plot1.set_xlabel('Année')
        plot1.set_ylabel('Revenus (en milliards)')
        plot1.grid(True)


        canvas = FigureCanvasTkAgg(fig, master=graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=20)

    liste.bind("<<ListboxSelect>>", update_info)


# Fenêtre principale et configuration
fenetre = Tk()
fenetre.title("Finance")
fenetre.geometry("1024x720")
fenetre.configure(background="floral white")

# Stocks info
# Stocks info
stocks = {
    "Microsoft": yf.Ticker("MSFT"),
    "Tesla": yf.Ticker("TSLA"),
    "BMW": yf.Ticker("BMW.DE"),
    "Google": yf.Ticker("GOOG"),
    "Apple": yf.Ticker("AAPL"),
    "Facebook": yf.Ticker("META"),
    "Bouygues": yf.Ticker("EN.PA"),
    "Carrefour": yf.Ticker("CA.PA"),
    "Amazon": yf.Ticker("AMZN"),
    "Netflix": yf.Ticker("NFLX"),
    "NVIDIA": yf.Ticker("NVDA"),
    "Adobe": yf.Ticker("ADBE"),
    "Intel": yf.Ticker("INTC"),
    "Oracle": yf.Ticker("ORCL"),
    "Salesforce": yf.Ticker("CRM"),
    "IBM": yf.Ticker("IBM"),
    "Qualcomm": yf.Ticker("QCOM"),
    "SAP": yf.Ticker("SAP"),
    "Sony": yf.Ticker("6758.T"),
    "Samsung": yf.Ticker("005930.KS"),
}

#création de l'image

width = 500
height = 500
image = PhotoImage(file="Logo.png")
canvas = Canvas(fenetre,width=width,height=height,bd=0,highlightthickness=0,bg="floral white")
canvas.create_image(width/2, height/2,image=image)
canvas.pack(expand=YES)



# Ajouter le bouton démarrer
frame = Frame(fenetre)
dm_button = Button(frame, text="Démarrer", font=(40), command=ouvrir)
dm_button.pack()
frame.pack(expand=YES)

# Afficher la fenêtre principale
fenetre.mainloop()
