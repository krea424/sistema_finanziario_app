import streamlit as st
st.set_page_config(page_title="Sistema Finanziario Italiano", layout="wide")


# Dati completi della Sezione 1: SOGGETTI REGOLAMENTATI DAL TUB
sezione_1 = {
    "Banche": {
        "Descrizione": "Istituzioni autorizzate a raccogliere risparmio e concedere credito.",
        "Ruolo": "Fornire credito e gestire strumenti finanziari essenziali per il sistema economico.",
        "Principali Attività Consentite": [
            "Raccolta del risparmio",
            "Erogazione di mutui, prestiti",
            "Gestione di conti correnti",
            "Emissione di carte di credito"
        ],
        "Vigilanza/Controllo": "Banca d’Italia",
        "Normativa Principale": "Art. 10 TUB, PSD2 (Direttiva UE 2015/2366)",
        "Tipologie": [
            "Commerciali",
            "Credito cooperativo",
            "Investimento"
        ],
        "Principali Requisiti": [
            "Capitale minimo adeguato",
            "Governance strutturata",
            "Requisiti di trasparenza verso i clienti"
        ],
        "Prodotti, Strumenti, Servizi": [
            "Conti correnti",
            "Carte di credito/debito",
            "Mutui ipotecari",
            "Prestiti personali",
            "Finanziamenti aziendali",
            "Prodotti di risparmio (es. depositi a termine)"
        ]
    },
    "Intermediari Finanziari": {
        "Descrizione": "Soggetti autorizzati alla concessione di finanziamenti, ma non alla raccolta di risparmio.",
        "Ruolo": "Specialisti nel fornire credito non tradizionale, come leasing e factoring.",
        "Principali Attività Consentite": [
            "Leasing",
            "Factoring",
            "Credito al consumo",
            "Microcredito",
            "Emissione di garanzie finanziarie"
        ],
        "Vigilanza/Controllo": "Banca d’Italia",
        "Normativa Principale": "Art. 106 TUB, Regolamento Banca d’Italia 2014",
        "Tipologie": [
            "Specializzati in leasing",
            "Factoring",
            "Credito al consumo"
        ],
        "Principali Requisiti": [
            "Adeguata capitalizzazione",
            "Iscrizione all’albo",
            "Gestione dei rischi patrimoniali"
        ],
        "Prodotti, Strumenti, Servizi": [
            "Leasing finanziario",
            "Factoring (es. gestione crediti commerciali)",
            "Prestiti al consumo",
            "Emissione di garanzie per operazioni finanziarie"
        ]
    },
    "Confidi": {
        "Descrizione": "Consorzi di garanzia collettiva che agevolano l’accesso al credito per le PMI.",
        "Ruolo": "Garantire il credito bancario per le PMI mediante fideiussioni collettive.",
        "Principali Attività Consentite": [
            "Emissione di garanzie collettive per finanziamenti richiesti da imprese"
        ],
        "Vigilanza/Controllo": "Banca d’Italia",
        "Normativa Principale": "Art. 112 TUB, Regolamento Banca d’Italia 2014",
        "Tipologie": [
            "Vigilati",
            "Non vigilati"
        ],
        "Principali Requisiti": [
            "Struttura mutualistica",
            "Capitale minimo per i confidi vigilati"
        ],
        "Prodotti, Strumenti, Servizi": [
            "Fideiussioni collettive",
            "Strumenti di garanzia per linee di credito aziendali",
            "Supporto per agevolazioni di credito pubblico"
        ]
    },
    "Istituti di Pagamento (IP)": {
        "Descrizione": "Forniscono servizi di pagamento senza essere banche.",
        "Ruolo": "Abilitare transazioni di pagamento per individui e imprese tramite strumenti innovativi.",
        "Principali Attività Consentite": [
            "Bonifici",
            "Carte prepagate",
            "Trasferimenti di denaro",
            "Pagamenti digitali"
        ],
        "Vigilanza/Controllo": "Banca d’Italia",
        "Normativa Principale": "Art. 114-septies TUB, PSD2 (Direttiva UE 2015/2366)",
        "Tipologie": [
            "Digitali (es. app)",
            "Tradizionali (es. POS e bonifici)"
        ],
        "Principali Requisiti": [
            "Capitale minimo di 125.000 €",
            "Solide procedure antiriciclaggio"
        ],
        "Prodotti, Strumenti, Servizi": [
            "Carte prepagate",
            "Bonifici SEPA",
            "Soluzioni di pagamento digitale (es. QR code, wallet digitali)",
            "Terminali POS per negozi"
        ]
    },
    "IMEL (Istituti di Moneta Elettronica)": {
        "Descrizione": "Emettono moneta elettronica e strumenti di pagamento collegati.",
        "Ruolo": "Emissione e gestione di moneta elettronica come alternativa al denaro contante.",
        "Principali Attività Consentite": [
            "Creazione e gestione di portafogli digitali",
            "Emissione di carte prepagate"
        ],
        "Vigilanza/Controllo": "Banca d’Italia",
        "Normativa Principale": "Art. 114-quinquies TUB, PSD2 (Direttiva UE 2015/2366)",
        "Tipologie": [
            "Basati su piattaforme digitali"
        ],
        "Principali Requisiti": [
            "Capitale minimo di 350.000 €",
            "Requisiti tecnologici avanzati"
        ],
        "Prodotti, Strumenti, Servizi": [
            "Carte di pagamento prepagate",
            "Wallet digitali (es. Hype, PayPal)",
            "Emissione e gestione di moneta elettronica (credito digitale)"
        ]
    },
    "Microcredito": {
        "Descrizione": "Intermediari che offrono piccoli prestiti senza richiedere garanzie reali.",
        "Ruolo": "Supportare individui o microimprese che non possono accedere al credito tradizionale.",
        "Principali Attività Consentite": [
            "Concessione di piccoli finanziamenti a privati o microimprese"
        ],
        "Vigilanza/Controllo": "Banca d’Italia",
        "Normativa Principale": "Art. 111 TUB, Regolamento Banca d’Italia sul Microcredito",
        "Tipologie": ["N/A"],
        "Principali Requisiti": [
            "Dimensioni ridotte",
            "Massimale di credito per operazione (es. 40.000 €)"
        ],
        "Prodotti, Strumenti, Servizi": [
            "Piccoli finanziamenti per startup o privati",
            "Supporto finanziario per microimprese",
            "Formazione imprenditoriale inclusa nel servizio"
        ]
    },
    "Cambiavalute": {
        "Descrizione": "Offrono servizi di cambio di valuta estera per privati e imprese.",
        "Ruolo": "Permettere la conversione tra valute diverse per operazioni commerciali o personali.",
        "Principali Attività Consentite": [
            "Conversione di valute estere"
        ],
        "Vigilanza/Controllo": "Banca d’Italia",
        "Normativa Principale": "Art. 106 TUB, Regolamento antiriciclaggio (D.lgs. 231/2007)",
        "Tipologie": ["N/A"],
        "Principali Requisiti": [
            "Adeguata verifica della clientela",
            "Tracciabilità delle operazioni"
        ],
        "Prodotti, Strumenti, Servizi": [
            "Cambio valuta fisica",
            "Invio di denaro in valute estere tramite servizi (es. Western Union)",
            "Consulenza sui tassi di cambio per aziende"
        ]
    }
}
# Dati per la Sezione 2: SOGGETTI REGOLAMENTATI DAL TUF
sezione_2 = {
    "OICR (Organismi di Investimento Collettivo del Risparmio)": {
        "Descrizione": "Strumenti per la gestione collettiva del risparmio degli investitori.",
        "Ruolo": "Investire il risparmio di più investitori in strumenti finanziari diversificati.",
        "Principali Attività Consentite": [
            "Gestione di portafogli di strumenti finanziari, immobili o altre attività"
        ],
        "Vigilanza/Controllo": "CONSOB, Banca d’Italia",
        "Normativa Principale": "Art. 35 TUF, Direttiva AIFMD (2011/61/UE)",
        "Tipologie": [
            "SICAF",
            "SICAV",
            "Fondi di investimento (aperti, chiusi, alternativi, armonizzati)"
        ],
        "Principali Requisiti": [
            "Requisiti patrimoniali proporzionati al tipo di fondo",
            "Governance strutturata"
        ],
        "Prodotti, Strumenti, Servizi": [
            "Fondi comuni",
            "SICAV",
            "SICAF",
            "Fondi immobiliari",
            "Fondi alternativi (es. private equity, venture capital)"
        ]
    },
    "SICAF (Società di Investimento a Capitale Fisso)": {
        "Descrizione": "OICR costituito in forma societaria con capitale fisso e raccolta diretta da investitori.",
        "Ruolo": "Gestire il proprio patrimonio investendo in strumenti finanziari o immobili.",
        "Principali Attività Consentite": [
            "Gestione diretta del patrimonio raccolto dagli investitori"
        ],
        "Vigilanza/Controllo": "CONSOB, Banca d’Italia",
        "Normativa Principale": "Art. 35-bis TUF, Direttiva AIFMD (2011/61/UE)",
        "Tipologie": [
            "Ordinaria",
            "Riservata",
            "Eterogestita"
        ],
        "Principali Requisiti": [
            "Capitale minimo di 1 milione di euro",
            "Compliance con normativa AIFMD"
        ],
        "Prodotti, Strumenti, Servizi": [
            "Investimenti diversificati in strumenti finanziari",
            "Fondi immobiliari",
            "Private equity",
            "Venture capital"
        ]
    },
    "SIM (Società di Intermediazione Mobiliare)": {
        "Descrizione": "Offrono servizi di investimento.",
        "Ruolo": "Facilitare l’accesso a strumenti di investimento e gestire portafogli per conto terzi.",
        "Principali Attività Consentite": [
            "Gestione patrimoniale",
            "Consulenza finanziaria",
            "Negoziazione per conto terzi"
        ],
        "Vigilanza/Controllo": "CONSOB, Banca d’Italia",
        "Normativa Principale": "Art. 18 TUF, Direttiva MiFID II (2014/65/UE)",
        "Tipologie": [
            "Pura",
            "Negoziazione per conto proprio",
            "Gestione patrimoniale"
        ],
        "Principali Requisiti": [
            "Capitale minimo adeguato",
            "Compliance con normativa MiFID II"
        ],
        "Prodotti, Strumenti, Servizi": [
            "Gestione di portafogli",
            "Intermediazione su azioni, obbligazioni, ETF, derivati (es. futures, opzioni)"
        ]
    }
}
# Dati per la Sezione 3: SOGGETTI REGOLAMENTATI E CENSITI DA ORGANISMI SPECIALI
sezione_3 = {
    "Mediatori Creditizi": {
        "Descrizione": "Professionisti o società che mettono in relazione banche o intermediari con clienti per la concessione di finanziamenti.",
        "Ruolo": "Facilitare l’accesso al credito tra clienti e istituzioni finanziarie.",
        "Principali Attività Consentite": [
            "Mediazione per mutui, leasing e prestiti, senza erogare direttamente credito o assumere rischi"
        ],
        "Vigilanza/Controllo": "OAM",
        "Normativa Principale": "Art. 128-sexies TUB",
        "Tipologie": [
            "Immobiliari (mutui)",
            "Non immobiliari"
        ],
        "Principali Requisiti": [
            "Iscrizione all’albo OAM",
            "Requisiti di onorabilità e professionalità",
            "Formazione continua"
        ],
        "Prodotti, Strumenti, Servizi": [
            "Mediazione di mutui",
            "Leasing",
            "Prestiti personali",
            "Strumenti di supporto per aziende e privati nella ricerca del miglior credito disponibile"
        ]
    },
    "Agenti in Attività Finanziaria": {
        "Descrizione": "Promuovono e concludono contratti per conto di banche o intermediari finanziari, operando come mandatari diretti.",
        "Ruolo": "Agire per conto di istituti di credito nella distribuzione di prodotti finanziari.",
        "Principali Attività Consentite": [
            "Promozione di mutui, prestiti personali, carte di credito e altri prodotti finanziari per conto del mandante"
        ],
        "Vigilanza/Controllo": "OAM",
        "Normativa Principale": "Art. 128-quater TUB",
        "Tipologie": [
            "Per privati",
            "Per aziende"
        ],
        "Principali Requisiti": [
            "Iscrizione all’albo OAM",
            "Contratto di mandato con l’intermediario",
            "Rispetto del codice deontologico"
        ],
        "Prodotti, Strumenti, Servizi": [
            "Promozione e vendita di prodotti finanziari come carte di credito, mutui ipotecari e prestiti personali"
        ]
    },
    "Consulenti Finanziari Autonomi": {
        "Descrizione": "Offrono consulenza finanziaria indipendente senza promuovere o collocare prodotti di intermediari finanziari o bancari.",
        "Ruolo": "Fornire consulenza imparziale su investimenti e strategie finanziarie.",
        "Principali Attività Consentite": [
            "Consulenza su investimenti",
            "Pianificazione finanziaria",
            "Costruzione di portafogli personalizzati"
        ],
        "Vigilanza/Controllo": "OCF",
        "Normativa Principale": "Art. 31-bis TUF",
        "Tipologie": ["N/A"],
        "Principali Requisiti": [
            "Iscrizione all’albo OCF",
            "Indipendenza da intermediari",
            "Trasparenza nella remunerazione"
        ],
        "Prodotti, Strumenti, Servizi": [
            "Analisi patrimoniale",
            "Costruzione di portafogli su misura",
            "Monitoraggio di strategie d’investimento indipendenti"
        ]
    },
    "Consulenti Finanziari Abilitati all’Offerta Fuori Sede": {
        "Descrizione": "Operano per banche, SIM o SGR nella promozione di prodotti finanziari direttamente presso il cliente.",
        "Ruolo": "Collocare prodotti finanziari e strumenti d’investimento presso il cliente per conto di istituzioni.",
        "Principali Attività Consentite": [
            "Collocamento di strumenti finanziari e prodotti bancari come fondi comuni, polizze assicurative o servizi di gestione patrimoniale"
        ],
        "Vigilanza/Controllo": "OCF",
        "Normativa Principale": "Art. 31 TUF",
        "Tipologie": [
            "Collegati a reti bancarie",
            "Collegati a SIM"
        ],
        "Principali Requisiti": [
            "Iscrizione all’albo OCF",
            "Contratto con il soggetto mandante",
            "Rispetto delle normative MiFID II"
        ],
        "Prodotti, Strumenti, Servizi": [
            "Fondi comuni",
            "Polizze vita",
            "Gestioni patrimoniali",
            "Promozione e assistenza su strumenti d’investimento e bancari"
        ]
    },
    "Società di Consulenza Finanziaria (SCF)": {
        "Descrizione": "Forniscono consulenza finanziaria indipendente senza essere direttamente collegate a intermediari bancari o finanziari.",
        "Ruolo": "Offrire consulenza patrimoniale indipendente e strategica a clienti privati o istituzionali.",
        "Principali Attività Consentite": [
            "Pianificazione finanziaria per privati o aziende",
            "Ottimizzazione di portafogli",
            "Supporto strategico agli investitori istituzionali"
        ],
        "Vigilanza/Controllo": "OCF",
        "Normativa Principale": "Art. 18-bis TUF",
        "Tipologie": [
            "Specializzate in consulenza patrimoniale"
        ],
        "Principali Requisiti": [
            "Iscrizione nell’albo OCF",
            "Compliance normativa MiFID II",
            "Trasparenza nelle commissioni"
        ],
        "Prodotti, Strumenti, Servizi": [
            "Pianificazione patrimoniale",
            "Consulenza per investitori istituzionali e retail",
            "Analisi del rischio d’investimento"
        ]
    }
}
# Dati per la Sezione 4: ALTRI OPERATORI
sezione_4 = {
    "Crowdfunding Platforms": {
        "Descrizione": "Piattaforme digitali per la raccolta di capitali da parte di imprese o individui.",
        "Ruolo": "Facilitare la raccolta di fondi tramite piattaforme digitali.",
        "Principali Attività Consentite": [
            "Equity crowdfunding (raccolta di capitale in cambio di partecipazioni)",
            "Lending crowdfunding (prestiti da privati a imprese)"
        ],
        "Vigilanza/Controllo": "CONSOB",
        "Normativa Principale": "Regolamento CONSOB 18592/2013, Regolamento UE 2020/1503",
        "Tipologie": [
            "Equity",
            "Lending",
            "Reward-based"
        ],
        "Principali Requisiti": [
            "Iscrizione al registro CONSOB",
            "Requisiti tecnologici e trasparenza informativa"
        ],
        "Prodotti, Strumenti, Servizi": [
            "Equity crowdfunding per startup e PMI",
            "Lending crowdfunding per progetti personali o aziendali",
            "Modelli reward-based"
        ]
    },
    "Società Fiduciarie": {
        "Descrizione": "Gestiscono patrimoni per conto di terzi, garantendo anonimato e tutela del cliente.",
        "Ruolo": "Gestire e amministrare beni o patrimoni per conto di clienti privati o aziende.",
        "Principali Attività Consentite": [
            "Amministrazione fiduciaria di titoli, patrimoni o partecipazioni societarie"
        ],
        "Vigilanza/Controllo": "CONSOB, Ministero Economia",
        "Normativa Principale": "Legge 1966/1939",
        "Tipologie": [
            "Tradizionali",
            "Specializzate in investimenti"
        ],
        "Principali Requisiti": [
            "Adeguata capitalizzazione",
            "Gestione fiduciaria trasparente",
            "Compliance antiriciclaggio"
        ],
        "Prodotti, Strumenti, Servizi": [
            "Gestione patrimoniale fiduciaria",
            "Amministrazione di partecipazioni societarie",
            "Protezione dell’anonimato patrimoniale"
        ]
    },
    "Società di Cartolarizzazione": {
        "Descrizione": "Acquistano crediti per trasformarli in titoli negoziabili sul mercato.",
        "Ruolo": "Facilitare la raccolta di risorse tramite strumenti di cartolarizzazione.",
        "Principali Attività Consentite": [
            "Cartolarizzazione di crediti commerciali, immobiliari o finanziari"
        ],
        "Vigilanza/Controllo": "Banca d’Italia",
        "Normativa Principale": "Legge 130/1999",
        "Tipologie": ["N/A"],
        "Principali Requisiti": [
            "Struttura giuridica ad hoc (SPV)",
            "Compliance alle regole di trasparenza e segregazione patrimoniale"
        ],
        "Prodotti, Strumenti, Servizi": [
            "Emissione di ABS (Asset-Backed Securities)",
            "Strumenti per finanziare grandi progetti immobiliari o industriali"
        ]
    },
    "Borsa e Mercati Regolamentati": {
        "Descrizione": "Gestiscono mercati regolamentati per la negoziazione di strumenti finanziari.",
        "Ruolo": "Garantire la liquidità e trasparenza nei mercati azionari e obbligazionari.",
        "Principali Attività Consentite": [
            "Quotazione e negoziazione di azioni, obbligazioni e derivati"
        ],
        "Vigilanza/Controllo": "CONSOB",
        "Normativa Principale": "TUF, Regolamento CONSOB dei mercati",
        "Tipologie": [
            "Mercati regolamentati",
            "Mercati alternativi"
        ],
        "Principali Requisiti": [
            "Compliance con normative di trasparenza e vigilanza per emittenti e intermediari"
        ],
        "Prodotti, Strumenti, Servizi": [
            "Azioni",
            "Obbligazioni",
            "ETF",
            "Derivati (futures, opzioni)",
            "Strumenti negoziati su mercati regolamentati e alternativi (AIM Italia)"
        ]
    }
}
# Funzione per filtrare i nodi in base al termine di ricerca
def filtra_nodi(sezione, termine):
    if not termine:  # Se la barra di ricerca è vuota, restituisci tutti i nodi
        return sezione
    termine = termine.lower()  # Rendiamo il termine di ricerca case-insensitive
    return {
        nodo: dettagli
        for nodo, dettagli in sezione.items()
        if termine in nodo.lower() or any(termine in str(val).lower() for val in dettagli.values())
    }

# Funzione per mostrare dettagli di un nodo
def mostra_dettagli(value):
    if isinstance(value, dict):
        for sub_key, sub_value in value.items():
            st.markdown(
                f"<p style='color: rgb(0, 0, 245); font-weight: bold;'>{sub_key}:</p>", 
                unsafe_allow_html=True
            )
            if isinstance(sub_value, list):
                st.write("- " + "\n- ".join(sub_value))
            else:
                st.write(sub_value)



# Menu a tendina
sezione_selezionata = st.sidebar.selectbox(
    "Seleziona una sezione:",
    [
        "Introduzione",
        "1: SOGGETTI REGOLAMENTATI DAL TUB",
        "2: SOGGETTI REGOLAMENTATI DAL TUF",
        "3: SOGGETTI REGOLAMENTATI E CENSITI DA ORGANISMI SPECIALI",
        "4: ALTRI OPERATORI"
    ]
)
# Barra di ricerca nella sidebar
st.sidebar.write("### Ricerca")
termine_ricerca = st.sidebar.text_input("Inserisci un termine di ricerca:")

# Visualizzazione della sezione Introduzione
if sezione_selezionata == "Introduzione":
    st.markdown(
        """
        <div style='margin-top: -50px;'>
            <h1 style='color: rgb(0, 0, 245); text-align: center;'>KREA Mappa del Sistema Finanziario Italiano</h1>
            <img src='mindmap_sistema_finanziario2.jpg' style='width: 100%; margin-top: -60px;'>
        </div>
        """,
        unsafe_allow_html=True
    )

    
    st.image(
        "mindmap_sistema_finanziario2.jpg",
        caption="Mappa concettuale del Sistema Finanziario Italiano",
        use_container_width=True
    )

    st.markdown(
        """
        <div style='margin-top: -15px;'>
        <img src='mindmap_sistema_finanziario2.jpg' style='width: 100%;'>
        </div>
        """,
        unsafe_allow_html=True
    )


    

# Visualizzazione dei nodi per la Sezione 1
elif sezione_selezionata == "1: SOGGETTI REGOLAMENTATI DAL TUB":
    st.markdown(
    "<h1 style='color: rgb(0, 0, 245); font-size: 24px;'>1:SOGGETTI REGOLAMENTATI DAL TUB</h1>",
    unsafe_allow_html=True
)

    nodi_filtrati = filtra_nodi(sezione_1, termine_ricerca)
    for nodo, dettagli in nodi_filtrati.items():

        with st.expander(nodo):
            mostra_dettagli(dettagli)

# Visualizzazione dei nodi per la Sezione 2
elif sezione_selezionata == "2: SOGGETTI REGOLAMENTATI DAL TUF":
    st.markdown(
    "<h1 style='color: rgb(0, 0, 245); font-size: 24px;'>2:SOGGETTI REGOLAMENTATI DAL TUF</h1>",
    unsafe_allow_html=True
)

    nodi_filtrati = filtra_nodi(sezione_2, termine_ricerca)
    for nodo, dettagli in nodi_filtrati.items():

        with st.expander(nodo):
            mostra_dettagli(dettagli)

# Visualizzazione dei nodi per la Sezione 3
elif sezione_selezionata == "3: SOGGETTI REGOLAMENTATI E CENSITI DA ORGANISMI SPECIALI":
    st.markdown(
    "<h1 style='color: rgb(0, 0, 245); font-size: 24px;'>3:SOGGETTI REGOLAMENTATI E CENSITI DA ORGANISMI SPECIALI</h1>",
    unsafe_allow_html=True
)

    nodi_filtrati = filtra_nodi(sezione_3, termine_ricerca)
    for nodo, dettagli in nodi_filtrati.items():

        with st.expander(nodo):
            mostra_dettagli(dettagli)

# Visualizzazione dei nodi per la Sezione 4
elif sezione_selezionata == "4: ALTRI OPERATORI":
    st.markdown(
    "<h1 style='color: rgb(0, 0, 245); font-size: 24px;'>4:ALTRI OPERATORI</h1>",
    unsafe_allow_html=True
)

    nodi_filtrati = filtra_nodi(sezione_4, termine_ricerca)
    for nodo, dettagli in nodi_filtrati.items():

        with st.expander(nodo):
            mostra_dettagli(dettagli)
