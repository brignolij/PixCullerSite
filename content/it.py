# -*- coding: utf-8 -*-
# Italian translation of the FAQ and blog of the PixCuller site (source: en.py). Tokens in answers/articles: {pc} {mac} {win} (see link_tokens).

BLOG_UI = dict(
    nav="Blog", privacy="Privacy", more="Continua a leggere",
    cta_mac="💻 Scarica PixCuller per Mac", cta_win="🪟 Scarica PixCuller per Windows",
    twin_android="Usi un telefono Android? Leggi la guida per Android:",
    twin_iphone="Usi un iPhone? Leggi la guida per iPhone:",
    index={
        "pixculler": dict(
            title="Blog PixCuller: ordinare le foto su Mac o PC",
            desc="Guide per ordinare migliaia di foto più in fretta su un grande schermo, confrontare scatti simili e liberare spazio su iPhone o Android da un Mac o un PC.",
            h1="Guide per ordinare le tue foto dal computer",
            intro="Perché un grande schermo cambia la velocità con cui ordini le foto e come sfruttarlo per liberare spazio su iPhone o su un telefono Android."),
    },
)

FAQ_PIXCULLER = dict(
    title="FAQ PixCuller: ordinare ed eliminare foto da Mac o PC",
    desc="Come ordinare migliaia di foto dal computer, confrontare scatti simili, liberare spazio su iPhone o Android da Mac o PC: risposte su PixCuller.",
    nav_home="PixCuller",
    h1="Domande e risposte",
    intro="Come ordinare le tue foto più in fretta dal computer, liberare spazio su iPhone o su un telefono Android da un Mac o PC, e cosa fa (e non fa mai) PixCuller con le tue foto.",
    qa=[
        ("Come fa PixCuller a sapere che una foto è già salvata sul mio computer?",
         "Aggiungi le cartelle dove tieni le foto (un disco, una chiavetta USB) in «Cartelle di backup». PixCuller cerca poi una copia identica di ogni foto in queste cartelle: stesso contenuto, non solo stesso nome. Le foto trovate hanno una cornice verde nella griglia e il menu offre due filtri, «Salvate» e «Non salvate». Le cartelle vengono ricordate e il controllo è veloce dalla seconda volta. Scegli le cartelle dove ordini davvero le foto invece di un intero disco: è molto più rapido. Una Live Photo conta come salvata se c'è anche il suo video (un'opzione permette di non controllarlo). Niente lascia il tuo computer."),
        ("Posso cercare le mie foto per luogo o per data?",
         "Sì. Scrivi un luogo, un paese, una data o un nome di file nella barra di ricerca: «Milano», «Italia», «agosto 2026», «11.02.2025». Il luogo viene dal GPS delle foto ed è trovato offline, quindi non viene inviato nulla. Un pulsante calendario filtra per periodo e la griglia può mostrare una sezione per giorno o restare compatta."),
        ("Come ordino le foto dell'iPhone dal computer, Mac o PC?",
         "Collega l'iPhone al computer con un cavo USB, sbloccalo e tocca Autorizza, poi apri <a href=\"{pc}\">PixCuller</a>: raggruppa il rullino per viaggio, confronta gli scatti simili fianco a fianco e seleziona centinaia di foto in pochi clic. Guide passo passo: <a href=\"{post:sort-iphone-photos-on-mac}\">sul Mac</a> e <a href=\"{post:sort-iphone-photos-on-pc}\">su un PC Windows</a>."),
        ("Perché ordinare le foto sul computer invece che sull'iPhone?",
         "Un grande schermo mostra più foto contemporaneamente, mouse e tastiera ne selezionano centinaia in pochi secondi e confrontare gli scatti fianco a fianco è più facile che passare avanti e indietro. Ordinare un rullino di migliaia di foto richiede diverse sessioni sul telefono e una sessione molto più breve su un Mac o PC."),
        ("Che cos'è PixCuller?",
         "PixCuller è un'app desktop gratuita per Mac e Windows che raggruppa le tue foto per viaggio, confronta gli scatti simili fianco a fianco ed elimina in blocco ciò che non vale la pena tenere. Legge il rullino di un iPhone o di un telefono Android tramite un cavo USB, o qualsiasi cartella di foto sul tuo computer, e funziona 100% sul dispositivo."),
        ("Come ordino rapidamente migliaia di foto?",
         "Apri la vista Viaggi: la tua libreria è raggruppata per viaggio con lo spazio occupato da ciascuno, così parti dal più pesante. All'interno di un viaggio, seleziona le foto in blocco, confronta quelle simili fianco a fianco e tieni lo scatto migliore di ogni gruppo. I filtri (viaggi di un solo giorno, luoghi esclusi come casa o lavoro, dimensione) restringono la ricerca."),
        ("Come libero spazio su iPhone da un Mac o PC?",
         "Collega il tuo iPhone via USB, apri PixCuller, seleziona i viaggi e le foto che non ti servono più e conferma. PixCuller le elimina direttamente tramite il cavo USB, su Windows 10/11 o su un Mac con macOS 27 o successivo, a patto che Foto di iCloud sia disattivato. L'eliminazione è immediata e definitiva sull'iPhone, con una copia conservata per impostazione predefinita 30 giorni sul tuo computer. Con macOS 26 o precedente, PixCuller mostra e ordina comunque le foto dell'iPhone, ma le elimini nell'app Foto dell'iPhone."),
        ("Posso eliminare le foto dal mio iPhone direttamente dal computer?",
         "Sì. Con un iPhone, PixCuller elimina le foto direttamente tramite il cavo USB, da un Mac o da un PC Windows, senza nulla da acquistare. Tre condizioni: Foto di iCloud è disattivato sull'iPhone (quando è attivo, Apple non consente questa eliminazione), un Mac ha macOS 27 o successivo (va bene qualsiasi PC Windows 10/11) e accetti che l'eliminazione sia immediata e definitiva sull'iPhone: le foto non passano da «Eliminati di recente». Per impostazione predefinita, PixCuller conserva per 30 giorni una copia di ogni elemento eliminato sul tuo computer, in una cartella «PixCuller Trash» dentro Immagini (una casella da spuntare al momento della conferma), così un errore si annulla importando di nuovo il file. Le Live Photo e le foto modificate sono gestite correttamente (tutte le loro versioni vengono eliminate insieme) e PixCuller mostra la versione modificata di una foto modificata. Se Foto di iCloud è attivo, disattivalo (Impostazioni > [il tuo nome] > iCloud > Foto) oppure elimina nell'app Foto dell'iPhone. Con macOS 26 o precedente, PixCuller può mostrare e ordinare le foto dell'iPhone ma non eliminarle: un banner nell'app lo segnala, e le elimini nell'app Foto dell'iPhone."),
        ("Eliminare da PixCuller è definitivo?",
         "Su un telefono, sì. Con un iPhone o un telefono Android, l'eliminazione tramite il cavo USB è immediata e definitiva sul telefono: le foto non passano da «Eliminati di recente» né dal cestino del telefono. Per impostazione predefinita, PixCuller conserva per 30 giorni una copia di ogni elemento eliminato sul tuo computer, in una cartella «PixCuller Trash» dentro Immagini (una casella da spuntare al momento della conferma), per poterlo importare di nuovo. In una cartella del tuo computer, i file vanno nel Cestino."),
        ("Come collego il mio iPhone a PixCuller?",
         "Usa un cavo USB, sblocca l'iPhone e tocca «Autorizza» quando richiesto. Su Mac non serve altro. Su Windows, installa la app gratuita Apple Devices dal Microsoft Store, che fornisce il driver con cui PixCuller può leggere l'iPhone."),
        ("Posso ordinare le foto di un telefono Android dal Mac o dal PC?",
         "Sì, tramite un cavo USB: su qualsiasi PC Windows 10/11 e su un Mac con macOS 27 o successivo. Trovi la stessa vista Viaggi, lo stesso confronto fianco a fianco e la stessa eliminazione in blocco dell'iPhone. Sul telefono non serve installare nulla."),
        ("Come collego il mio telefono Android?",
         "Collega il telefono al computer con un cavo USB, sbloccalo e scegli «Trasferimento file» nella notifica USB. In PixCuller, clicca «Telefono Android», poi «Collega via USB». Guide: <a href=\"{post:sort-android-photos-on-mac}\">sul Mac</a>, <a href=\"{post:sort-android-photos-on-pc}\">su un PC Windows</a>."),
        ("Perché il mio Mac non vede il telefono Android?",
         "PixCuller legge i telefoni Android via USB con macOS 27 o successivo; su un Mac più vecchio, l'app mostra un messaggio che lo segnala. Con macOS 27 o successivo, verifica che il telefono sia sbloccato e che nella notifica USB sia scelto «Trasferimento file». Su Windows 10/11, la connessione USB funziona con qualsiasi versione."),
        ("Devo installare qualcosa sul telefono?",
         "No. PixCuller funziona da solo, senza nulla da installare sul telefono e senza bisogno di altre app. A un iPhone o a un telefono Android basta un cavo USB. Su Windows, per leggere un iPhone serve anche la app gratuita Apple Devices sul PC, dal Microsoft Store."),
        ("Cosa succede alle foto che elimino su un telefono Android?",
         "PixCuller le elimina direttamente tramite il cavo USB, dopo la tua conferma. L'eliminazione è immediata e definitiva: le foto non passano dal cestino del telefono. Per impostazione predefinita, PixCuller conserva per 30 giorni una copia di ogni elemento eliminato sul tuo computer, in una cartella «PixCuller Trash» dentro Immagini (una casella da spuntare al momento della conferma), così un errore si annulla."),
        ("Come trovo le foto duplicate in una cartella del Mac o del PC?",
         "Apri la cartella in PixCuller («Apri cartella», oppure trascinala sulla finestra). L'app esplora le sottocartelle, confronta il contenuto delle foto e applica lo stesso badge «≈ N» a copie esatte, raffiche e scatti quasi identici. Tieni il migliore di ogni gruppo e sposta il resto nel Cestino. Guide: <a href=\"{post:find-duplicate-photos-on-mac}\">sul Mac</a>, <a href=\"{post:find-duplicate-photos-on-windows}\">su Windows</a>."),
        ("Posso usare PixCuller su foto salvate sul mio computer, non su un iPhone?",
         "Sì. Apri una cartella qualsiasi: PixCuller trova le foto simili al suo interno, mostra i badge su quelle simili e ti permette di confrontare ed eliminare."),
        ("Come trova PixCuller le foto simili?",
         "Confronta il contenuto delle tue foto, non i nomi dei file, quindi raffiche, scatti quasi identici e la stessa scena fotografata più volte finiscono nello stesso gruppo. Puoi confrontare fino a 6 foto fianco a fianco e tenere la più nitida e meglio inquadrata."),
        ("Come confronto le foto simili fianco a fianco?",
         "Seleziona un gruppo di foto simili e apri il confronto: fino a 6 foto vengono mostrate alla stessa dimensione, così puoi valutare messa a fuoco, espressioni e inquadratura. Tieni la migliore e seleziona le altre."),
        ("PixCuller funziona su Windows?",
         "Sì: Windows 10 e 11 (64 bit). Per leggere un iPhone serve la app gratuita Apple Devices dal Microsoft Store. L'app non è ancora firmata digitalmente, quindi Windows SmartScreen può mostrare un avviso al primo avvio: scegli «Ulteriori informazioni» e poi «Esegui comunque»."),
        ("Quali Mac supporta PixCuller?",
         "Mac con Apple Silicon e macOS 11 o successivo. L'app è firmata e notarizzata da Apple, quindi si apre senza avvisi di sicurezza."),
        ("PixCuller è gratuito? C'è un abbonamento?",
         "Sì, PixCuller è gratuito, senza abbonamento e senza acquisti in-app. Sfogliare, confrontare, ordinare ed eliminare è gratuito, su un telefono come in una cartella del tuo computer."),
        ("PixCuller invia le mie foto a un server o al cloud?",
         "No. PixCuller funziona 100% sul dispositivo: nessun account, nessun cloud, nessuna foto, video o posizione viene mai inviata altrove. Il riconoscimento dei luoghi e il rilevamento delle foto simili avvengono sul tuo computer. Possono essere inviate solo statistiche d'uso anonime, disattivabili."),
        ("PixCuller modifica le mie foto originali?",
         "No. PixCuller legge le tue foto solo per mostrarle e confrontarle. L'unica modifica che fa è l'eliminazione che confermi tu."),
        ("Come nascondo casa e ufficio dalla vista dei viaggi?",
         "Aggiungili come luoghi esclusi: la vita quotidiana smette di comparire come viaggio e i tuoi veri viaggi risaltano."),
        ("Posso fare ordine dopo una vacanza dal computer?",
         "Sì, è l'uso tipico. Dopo un viaggio, collega il telefono, apri quel viaggio in PixCuller, confronta gli scatti simili, tieni il migliore di ciascuno ed elimina il resto."),
        ("Posso usare PixCuller per preparare un album fotografico o un backup?",
         "PixCuller ti aiuta a decidere cosa vale la pena tenere: ordina il viaggio, elimina i duplicati e gli scatti quasi identici, poi fai il backup o condividi ciò che resta."),
    ],
    footer_copy="© 2026 PixCuller. Sviluppato da Jeffrey Brignoli.",
    footer_privacy="Privacy", footer_kofi="Ko-fi",
)

BLOG = {
"pixculler": [
dict(slug="sort-iphone-photos-on-mac",
     title="Come ordinare le foto dell'iPhone sul Mac",
     desc="Ordina migliaia di foto dell'iPhone sul Mac: cosa fanno Foto e Acquisizione Immagine, e un metodo più rapido per raggruppare, confrontare ed eliminare.",
     h1="Come ordinare le foto dell'iPhone sul Mac",
     body="""      <p>Ordinare un rullino pieno sull'iPhone vuol dire ore di tocchi. Sul Mac vedi molte più foto insieme, selezioni con il mouse e confronti gli scatti su un grande schermo. Ecco come fare, con gli strumenti di macOS e con un'app dedicata.</p>

      <h2>Con gli strumenti integrati in macOS</h2>
      <ul>
        <li><strong>Foto:</strong> importa una copia delle foto dell'iPhone sul Mac. Utile come backup, ma non ti dice cosa eliminare sull'iPhone.</li>
        <li><strong>Acquisizione Immagine:</strong> elenca le foto dell'iPhone come semplici file, senza raggrupparle per viaggio né confrontare gli scatti simili.</li>
      </ul>
      <p>Funzionano entrambi, ma con migliaia di foto scorri comunque un unico lungo elenco.</p>

      <h2>Con PixCuller, passo dopo passo</h2>
      <p><strong>1. Installa PixCuller.</strong> <a href="{mac}">Scaricalo gratis</a>: macOS 11 o successivo su Apple Silicon, firmato e autenticato da Apple.</p>
      <p><strong>2. Collega l'iPhone.</strong> Collegalo con un cavo USB, sbloccalo e tocca Autorizza.</p>
      <p><strong>3. Ordina un viaggio alla volta.</strong> La vista Viaggi raggruppa il rullino per data e luogo e mostra lo spazio occupato da ogni viaggio. Inizia dal più pesante.</p>
      <p><strong>4. Confronta e seleziona.</strong> Le foto simili hanno un badge: aprine fino a sei fianco a fianco, tieni la migliore e seleziona le altre, insieme a screenshot e video pesanti che non ti servono.</p>
      <p><strong>5. Elimina in sicurezza.</strong> Con Foto di iCloud disattivato e macOS 27 o successivo, PixCuller elimina le foto direttamente tramite il cavo USB. L'eliminazione è immediata e definitiva sull'iPhone: le foto non passano da «Eliminati di recente». Per impostazione predefinita, PixCuller conserva per 30 giorni una copia di ogni elemento eliminato sul tuo Mac, in una cartella «PixCuller Trash» dentro Immagini, così un errore si annulla importando di nuovo il file. Se Foto di iCloud è attivo, disattivalo (Impostazioni > [il tuo nome] > iCloud > Foto) oppure elimina nell'app Foto dell'iPhone.</p>

      <h2>Da sapere</h2>
      <ul>
        <li>Tutto resta sul tuo Mac e sul tuo iPhone: nessun account, nessun cloud, nessun invio.</li>
        <li>PixCuller non modifica mai gli originali ed elimina solo ciò che confermi.</li>
        <li>Con macOS 26 o precedente, PixCuller mostra e ordina le foto dell'iPhone ma non può eliminarle: un banner nell'app lo segnala, e le elimini nell'app Foto dell'iPhone.</li>
        <li>PixCuller è gratuito, e ordinare una cartella di foto sul Mac funziona allo stesso modo.</li>
      </ul>"""),
dict(slug="sort-iphone-photos-on-pc",
     title="Come ordinare le foto dell'iPhone su un PC Windows",
     desc="Ordina migliaia di foto dell'iPhone su Windows 10 o 11: cosa mostrano l'app Foto ed Esplora file, e un metodo più rapido per ordinare ed eliminare.",
     h1="Come ordinare le foto dell'iPhone su un PC Windows",
     body="""      <p>Hai un iPhone ma un computer Windows? Puoi comunque ordinare le foto su un grande schermo invece che sul telefono. Ecco cosa sa fare Windows da solo, e un metodo più rapido.</p>

      <h2>Con gli strumenti integrati in Windows</h2>
      <ul>
        <li><strong>App Foto:</strong> importa una copia delle foto dell'iPhone sul PC. Va bene per un backup, ma non ti aiuta a scegliere cosa eliminare.</li>
        <li><strong>Esplora file:</strong> mostra le foto dell'iPhone in cartelle come 100APPLE, con nomi come IMG_0001, senza viaggi né confronto degli scatti simili.</li>
      </ul>

      <h2>Con PixCuller, passo dopo passo</h2>
      <p><strong>1. Installa Apple Devices.</strong> Installa l'app gratuita Apple Devices dal Microsoft Store: Windows ne ha bisogno per leggere un iPhone.</p>
      <p><strong>2. Installa PixCuller.</strong> Dal Microsoft Store oppure <a href="{win}">scaricandolo gratis</a> (Windows 10/11, 64 bit). Il download non è ancora firmato, quindi SmartScreen può mostrare un avviso al primo avvio.</p>
      <p><strong>3. Collega l'iPhone.</strong> Collegalo con un cavo USB, sbloccalo e tocca Autorizza.</p>
      <p><strong>4. Ordina un viaggio alla volta.</strong> La vista Viaggi raggruppa il rullino per data e luogo e mostra lo spazio occupato da ogni viaggio. Inizia dal più pesante.</p>
      <p><strong>5. Confronta, seleziona, elimina.</strong> Le foto simili hanno un badge: confrontane fino a sei fianco a fianco, tieni la migliore e seleziona le altre. Con Foto di iCloud disattivato, PixCuller le elimina direttamente tramite il cavo USB. L'eliminazione è definitiva sull'iPhone (niente «Eliminati di recente»), ma per impostazione predefinita PixCuller conserva per 30 giorni una copia di ogni elemento eliminato sul tuo PC, in una cartella «PixCuller Trash» dentro Immagini. Se Foto di iCloud è attivo, disattivalo (Impostazioni > [il tuo nome] > iCloud > Foto) oppure elimina nell'app Foto dell'iPhone.</p>

      <h2>Da sapere</h2>
      <ul>
        <li>Tutto resta sul tuo PC e sul tuo iPhone: nessun account, nessun cloud, nessun invio.</li>
        <li>PixCuller non modifica mai gli originali ed elimina solo ciò che confermi.</li>
        <li>Sfogliare e ordinare è gratis, e ordinare una cartella di foto già sul PC non ha mai limiti.</li>
      </ul>"""),
dict(slug="sort-photos-on-computer",
     title="Ordinare migliaia di foto più in fretta su Mac o PC Windows",
     desc="Perché ordinare le foto su un grande schermo è molto più veloce che sul telefono, e un metodo semplice per esaminare migliaia di foto in una sola sessione.",
     h1="Come ordinare migliaia di foto più in fretta su Mac o PC",
     body="""      <p>Se il tuo rullino contiene diecimila foto, ordinarlo sullo schermo di un telefono è un progetto che non finirai mai. Su un computer può bastare una serata. Ecco perché, e un metodo che funziona.</p>

      <h2>Perché un computer è più veloce</h2>
      <ul>
        <li><strong>Più cose sullo schermo:</strong> decine di foto alla volta invece di una manciata.</li>
        <li><strong>Selezione precisa:</strong> mouse e tastiera selezionano centinaia di foto in pochi secondi.</li>
        <li><strong>Vero confronto:</strong> foto simili una accanto all'altra a una dimensione in cui messa a fuoco ed espressioni sono ben visibili.</li>
      </ul>

      <h2>Un metodo che funziona</h2>
      <p><strong>1. Raggruppa per viaggio.</strong> Ordinare per data e luogo divide la libreria in parti gestibili. Parti dal viaggio che occupa più spazio.</p>
      <p><strong>2. Elimina le quasi copie.</strong> Confronta ogni gruppo di scatti simili, tieni il migliore e seleziona gli altri.</p>
      <p><strong>3. Filtra il rumore.</strong> Nascondi i luoghi che non ti interessano (casa, lavoro) così i veri viaggi risaltano, e filtra per dimensione per trovare i file pesanti.</p>
      <p><strong>4. Elimina in un colpo solo.</strong> Seleziona centinaia di foto e conferma una volta sola.</p>

      <h2>PixCuller fa esattamente questo</h2>
      <p><a href="{pc}">PixCuller</a> è un'app desktop gratuita per Mac e Windows. La sua vista Viaggi raggruppa la libreria per viaggio e mostra lo spazio occupato da ciascuno, le foto simili hanno un badge e puoi confrontarne fino a sei fianco a fianco. Legge un iPhone o un telefono Android tramite un cavo USB, o qualsiasi cartella sul tuo computer, funziona 100% sul dispositivo e non modifica mai i tuoi originali.</p>
      <p>Su un telefono, PixCuller elimina direttamente tramite il cavo USB, su Windows 10/11 o su un Mac con macOS 27 o successivo (con Foto di iCloud disattivato su un iPhone). L'eliminazione è definitiva sul telefono, con una copia conservata per impostazione predefinita 30 giorni sul tuo computer. In una cartella, i file vanno nel Cestino. Ordinare non ha mai limiti.</p>

      <h2>Consigli per una sessione lunga</h2>
      <ul>
        <li>Lavora viaggio per viaggio, non scorrendo l'intera libreria.</li>
        <li>Decidi in fretta: se due scatti si assomigliano, tienine uno.</li>
        <li>Elimina alla fine di ogni viaggio, così i progressi si vedono.</li>
      </ul>"""),
dict(slug="free-up-iphone-from-mac-or-pc",
     title="Come liberare spazio su iPhone da un Mac o PC Windows",
     desc="Collega il tuo iPhone, ordina le foto su un grande schermo ed elimina ciò che non ti serve, senza iCloud e senza inviare nulla online.",
     h1="Come liberare spazio su iPhone da un Mac o PC Windows",
     body="""      <p>Fare pulizia su un iPhone pieno direttamente dall'iPhone è noioso. Da un computer vedi molte più foto alla volta e decidi più in fretta. Ecco l'intero procedimento.</p>

      <h2>Cosa ti serve</h2>
      <ul>
        <li>Un Mac (Apple Silicon, macOS 11+) o un PC Windows 10/11.</li>
        <li>Un cavo USB. Su Windows, anche la app gratuita Apple Devices dal Microsoft Store.</li>
        <li><a href="{pc}">PixCuller</a>, gratuito per entrambi i sistemi.</li>
        <li>Per eliminare dall'iPhone: Foto di iCloud disattivato e, su un Mac, macOS 27 o successivo. Con macOS 26 o precedente, PixCuller mostra e ordina comunque le foto, e le elimini nell'app Foto dell'iPhone.</li>
      </ul>

      <h2>Passo dopo passo</h2>
      <p><strong>1. Collega e autorizza.</strong> Collega l'iPhone, sbloccalo e tocca Autorizza.</p>
      <p><strong>2. Apri la vista Viaggi.</strong> PixCuller raggruppa il tuo rullino per viaggio e mostra lo spazio occupato da ciascuno.</p>
      <p><strong>3. Ordina i viaggi più pesanti.</strong> Confronta gli scatti simili, tieni il migliore e seleziona il resto, più gli screenshot e i video pesanti che non ti servono.</p>
      <p><strong>4. Conferma l'eliminazione.</strong> Con Foto di iCloud disattivato (e macOS 27 o successivo su un Mac), PixCuller elimina le foto direttamente tramite il cavo USB, anche su Windows. L'eliminazione è immediata e definitiva sull'iPhone, ma per impostazione predefinita PixCuller conserva per 30 giorni una copia di ogni elemento eliminato sul tuo computer, in una cartella «PixCuller Trash» dentro Immagini.</p>
      <p><strong>5. Se Foto di iCloud è attivo.</strong> PixCuller rifiuta l'eliminazione: disattiva Foto di iCloud (Impostazioni > [il tuo nome] > iCloud > Foto) oppure elimina nell'app Foto dell'iPhone.</p>

      <h2>È sicuro?</h2>
      <p>Sì: le tue foto restano sui tuoi dispositivi, senza account, senza cloud e senza upload. PixCuller si limita a leggere le tue foto finché non confermi. Un'eliminazione è definitiva sull'iPhone, ma una copia resta per impostazione predefinita 30 giorni sul tuo computer.</p>


      <h2>Su Windows</h2>
      <p>I passaggi sono gli stessi su Windows 10 e 11. Installa prima la app gratuita Apple Devices dal Microsoft Store, così PixCuller può leggere l'iPhone. L'app non è ancora firmata digitalmente, quindi SmartScreen può mostrare un avviso al primo avvio.</p>"""),
dict(slug="compare-similar-photos-keep-the-best",
     title="Confrontare foto simili fianco a fianco e tenere la migliore",
     desc="Una routine semplice per scegliere lo scatto migliore tra foto quasi identiche: cosa guardare e come farlo in fretta su un grande schermo.",
     h1="Come confrontare foto simili e tenere la migliore",
     body="""      <p>Hai scattato sei foto dello stesso momento e sembrano tutte buone. Scegliere la migliore richiede pochi secondi con il metodo giusto e qualche minuto con quello sbagliato.</p>

      <h2>Cosa controllare, in quest'ordine</h2>
      <ol>
        <li><strong>Messa a fuoco.</strong> Ingrandisci sugli occhi o sul soggetto principale. Un soggetto sfocato è motivo di esclusione.</li>
        <li><strong>Espressioni.</strong> Occhi aperti, sorrisi naturali, nessuno a metà di un battito di ciglia.</li>
        <li><strong>Inquadratura.</strong> Niente tagliato fuori, sfondo pulito, orizzonte dritto.</li>
        <li><strong>Momento.</strong> Se due scatti si equivalgono, tieni quello che sembra più vivo.</li>
      </ol>

      <h2>Perché il confronto fianco a fianco conta</h2>
      <p>Passare da una foto all'altra rende difficile vedere le piccole differenze. Vederle una accanto all'altra alla stessa dimensione rende evidente quella più nitida o meglio inquadrata. Lo schermo di un computer ne mostra fino a sei insieme, dove un telefono ne mostra una.</p>

      <h2>Una routine più veloce</h2>
      <p>Raggruppa prima le foto simili, così non devi mai cercarle nella libreria. Per ogni gruppo, apri il confronto, scegline una e seleziona le altre. Decidi in secondi, non in minuti.</p>

      <h2>Fallo con PixCuller</h2>
      <p><a href="{pc}">PixCuller</a> mostra un badge sulle foto simili, ne apre fino a sei fianco a fianco e ti permette di selezionare le altre con un clic. Funziona su un iPhone collegato via USB o su qualsiasi cartella del tuo Mac o PC, offline, e non modifica mai i tuoi originali.</p>

      <h2>Tieni, senza rimpianti</h2>
      <p>Quando hai dubbi, tienine due. Quando PixCuller elimina da un telefono, conserva per impostazione predefinita una copia sul tuo computer per 30 giorni; in una cartella, i file vanno nel Cestino. In entrambi i casi puoi ancora cambiare idea.</p>"""),
dict(slug="find-duplicate-photos-on-mac",
     title="Come trovare foto duplicate e simili sul Mac",
     desc="Trova copie esatte, raffiche e scatti quasi identici nelle cartelle di foto del Mac o su un disco esterno, tieni il migliore e sposta il resto nel Cestino.",
     h1="Come trovare foto duplicate e simili sul Mac",
     body="""      <p>Anni di importazioni, schede della fotocamera e backup lasciano le stesse foto sparse in tante cartelle del Mac. Alcune sono copie esatte; la maggior parte sono scatti quasi identici dello stesso momento. Ecco come trovare entrambe, tenere la migliore e liberare spazio, senza toccare la libreria di Foto.</p>

      <h2>Cosa offre macOS</h2>
      <ul>
        <li><strong>Finder:</strong> ordinare una cartella per nome o dimensione aiuta a individuare le copie evidenti come «IMG_1234 copia.jpg», ma non due scatti diversi della stessa scena.</li>
        <li><strong>Foto:</strong> l'album Duplicati copre solo le foto già presenti nella libreria di Foto, non le altre cartelle né i dischi.</li>
      </ul>

      <h2>Con PixCuller, passo dopo passo</h2>
      <p><strong>1. Installa PixCuller.</strong> <a href="{mac}">Scaricalo gratis</a>: macOS 11 o successivo su Apple Silicon, firmato e autenticato da Apple.</p>
      <p><strong>2. Apri la cartella.</strong> Clicca su «Apri cartella» oppure trascina una cartella sulla finestra. Le sottocartelle sono incluse, così come i dischi esterni.</p>
      <p><strong>3. Guarda i badge.</strong> PixCuller confronta il contenuto delle foto, non i nomi: copie esatte, raffiche e scatti quasi identici ricevono lo stesso badge «≈ N».</p>
      <p><strong>4. Tieni la migliore.</strong> Apri un gruppo per confrontare fino a sei foto fianco a fianco, tieni la più nitida e seleziona le altre.</p>
      <p><strong>5. Elimina in sicurezza.</strong> I file selezionati vanno nel Cestino del Mac, dove «Ripristina» li rimette al loro posto se cambi idea.</p>

      <h2>Da sapere</h2>
      <ul>
        <li>Sono supportati JPEG, HEIC, PNG, TIFF, WebP e file RAW (CR2, CR3, NEF, ARW, RAF, ORF, RW2, DNG), oltre ai video MOV e MP4.</li>
        <li>Le foto sono datate in base ai dati EXIF, quindi anche le cartelle copiate restano ordinate per il giorno dello scatto.</li>
        <li>Ordinare una cartella è gratis e senza limiti. Tutto funziona sul tuo Mac: nessun account, nessun invio.</li>
        <li>Le librerie di Foto e i pacchetti di app dentro la cartella vengono ignorati, così PixCuller non entra mai nei file di un'altra app.</li>
      </ul>"""),
dict(slug="find-duplicate-photos-on-windows",
     title="Come trovare foto duplicate e simili su Windows",
     desc="Trova copie esatte, raffiche e scatti quasi identici nelle cartelle di foto del PC o su un disco esterno, tieni il migliore e sposta il resto nel Cestino.",
     h1="Come trovare foto duplicate e simili su Windows 10 o 11",
     body="""      <p>Backup del telefono, schede della fotocamera e vecchie copie lasciano le stesse foto in più cartelle del PC. Alcune sono duplicati esatti, la maggior parte sono scatti quasi identici. Ecco come trovare entrambi e fare pulizia in sicurezza.</p>

      <h2>Cosa offre Windows</h2>
      <ul>
        <li><strong>Esplora file:</strong> ordinare per nome, dimensione o data aiuta con le copie evidenti, ma non capisce che due file diversi mostrano la stessa scena.</li>
        <li><strong>App Foto:</strong> ottima per visualizzare e importare, ma senza uno strumento per trovare scatti simili e scegliere il migliore.</li>
      </ul>

      <h2>Con PixCuller, passo dopo passo</h2>
      <p><strong>1. Installa PixCuller.</strong> Scaricalo gratis <a href="{win}">per Windows 10 o 11</a> (64 bit), oppure dal Microsoft Store.</p>
      <p><strong>2. Apri la cartella.</strong> Clicca su «Apri cartella» oppure trascina una cartella sulla finestra. Sottocartelle e dischi esterni sono inclusi.</p>
      <p><strong>3. Guarda i badge.</strong> PixCuller confronta ciò che mostrano le foto, non i nomi dei file: copie esatte, raffiche e scatti quasi identici ricevono lo stesso badge «≈ N».</p>
      <p><strong>4. Tieni la migliore.</strong> Confronta fino a sei foto fianco a fianco, tieni la più nitida e seleziona le altre.</p>
      <p><strong>5. Elimina in sicurezza.</strong> I file selezionati vanno nel Cestino, quindi puoi ripristinarli.</p>

      <h2>Da sapere</h2>
      <ul>
        <li>Sono supportati JPEG, HEIC, PNG, TIFF, WebP e file RAW (CR2, CR3, NEF, ARW, RAF, ORF, RW2, DNG), oltre ai video MOV e MP4. Per le anteprime HEIC servono le Estensioni immagine HEIF gratuite di Microsoft.</li>
        <li>Le foto sono datate in base ai dati EXIF, quindi anche le cartelle copiate restano ordinate per il giorno dello scatto.</li>
        <li>Ordinare una cartella è gratis e senza limiti. Tutto funziona sul tuo PC: nessun account, nessun invio.</li>
      </ul>"""),
dict(slug="sort-photo-folder-external-drive",
     title="Come ordinare una grande cartella di foto su Mac o PC",
     desc="Vecchi backup, schede SD, un disco esterno pieno di foto: un metodo semplice per ordinare migliaia di file per viaggio ed eliminare le quasi copie.",
     h1="Come ordinare una grande cartella di foto, o un intero disco esterno",
     body="""      <p>Ce l'abbiamo tutti: una cartella chiamata «Foto da ordinare», un vecchio backup del telefono, un disco esterno riempito in dieci anni. Migliaia di file, nessun ordine, tante quasi copie. Ecco un metodo per sistemare tutto in una sola sessione.</p>

      <h2>1. Apri tutta la cartella in una volta</h2>
      <p>Non andare cartella per cartella. Apri la cartella principale in <a href="{pc}">PixCuller</a> («Apri cartella», oppure trascinala sulla finestra): le sottocartelle sono incluse e ogni foto è datata in base ai dati EXIF, non al giorno in cui è stata copiata.</p>

      <h2>2. Lascia emergere i viaggi</h2>
      <p>La vista Viaggi raggruppa le foto per data e luogo e mostra lo spazio occupato da ciascun gruppo. Dieci anni di file diventano un elenco di viaggi ed eventi, e parti dal più pesante.</p>

      <h2>3. Riduci le quasi copie</h2>
      <p>Raffiche, scatti ripetuti e copie della stessa foto hanno un badge «≈ N». Confrontane fino a sei fianco a fianco, tieni la migliore e seleziona le altre. Questo passaggio da solo spesso elimina buona parte dei file.</p>

      <h2>4. Seleziona gli scarti più ovvi</h2>
      <p>Screenshot, foto mosse, video accidentali: selezionali man mano. Nulla viene eliminato finché non confermi.</p>

      <h2>5. Elimina in sicurezza</h2>
      <p>I file confermati vanno nel Cestino su Mac o nel Cestino di Windows, quindi un errore si può annullare. Svuotalo quando sei sicuro.</p>

      <h2>Da sapere</h2>
      <ul>
        <li>I file RAW delle fotocamere (CR2, CR3, NEF, ARW, RAF, ORF, RW2, DNG) sono supportati insieme a JPEG, HEIC, PNG e video.</li>
        <li>Ordinare le cartelle è gratis e senza limiti, su Mac (<a href="{mac}">download</a>) e Windows (<a href="{win}">download</a>).</li>
        <li>I tuoi originali non vengono mai modificati: l'unica modifica di PixCuller è l'eliminazione che confermi.</li>
      </ul>"""),
dict(slug="sort-android-photos-on-mac",
     title="Come ordinare le foto del tuo Android sul Mac",
     desc="Da sempre un Mac fatica a leggere i telefoni Android via USB. Come ordinare migliaia di foto Android su un Mac con macOS 27 ed eliminare ciò che non serve.",
     h1="Come ordinare le foto del tuo Android sul Mac",
     body="""      <p>Collega un telefono Android a un Mac e, il più delle volte, non succede nulla di utile: macOS non ha mai letto i telefoni Android via USB come fa Windows. Eppure un Mac è il posto migliore per ordinare un grande rullino, con uno schermo ampio, un mouse e il confronto fianco a fianco. Ecco cosa funziona.</p>

      <h2>Cosa sa fare macOS da solo</h2>
      <ul>
        <li><strong>Acquisizione Immagine:</strong> può vedere il telefono se scegli «Trasferisci foto» (PTP) nella notifica USB, ma solo come elenco piatto di file, senza raggruppamenti e senza confronto tra scatti simili.</li>
        <li><strong>Android File Transfer di Google:</strong> non è più mantenuto e comunque si limita a copiare file.</li>
        <li><strong>Caricamento nel cloud:</strong> inviare tutto a un servizio online solo per ordinare è lento, consuma il tuo piano dati e mette le tue foto sul server di qualcun altro.</li>
      </ul>

      <h2>Con PixCuller, via USB, passo dopo passo</h2>
      <p><strong>1. Installa PixCuller.</strong> <a href="{mac}">Scarica PixCuller per Mac</a> gratis. Per leggere un telefono Android serve macOS 27 o successivo; su un Mac più vecchio, l'app mostra un messaggio che lo segnala. Sul telefono non serve installare nulla.</p>
      <p><strong>2. Collega il telefono.</strong> Collegalo con un cavo USB, sbloccalo e scegli «Trasferimento file» nella notifica USB.</p>
      <p><strong>3. Connettiti.</strong> In PixCuller, clicca «Telefono Android», poi «Collega via USB».</p>
      <p><strong>4. Ordina un viaggio alla volta.</strong> La vista Viaggi raggruppa il rullino per data e luogo, con lo spazio occupato da ogni viaggio. Le foto simili hanno un badge: confrontane fino a sei fianco a fianco, tieni la migliore, seleziona le altre.</p>
      <p><strong>5. Elimina in sicurezza.</strong> Clicca Elimina e conferma. PixCuller elimina le foto direttamente tramite il cavo: l'eliminazione è immediata e definitiva sul telefono (le foto non passano dal suo cestino), ma per impostazione predefinita PixCuller conserva per 30 giorni una copia di ogni elemento eliminato sul tuo Mac, in una cartella «PixCuller Trash» dentro Immagini, così puoi rimediare a un errore.</p>

      <h2>Da sapere</h2>
      <ul>
        <li>Tutto resta sul tuo Mac e sul tuo telefono: nessun account, nessun cloud, nessun invio.</li>
        <li>PixCuller non modifica mai gli originali ed elimina solo ciò che confermi.</li>
        <li>PixCuller è gratuito, senza abbonamento.</li>
        <li>Hai anche un iPhone? Anche lui si collega al Mac con un cavo USB.</li>
      </ul>"""),
dict(slug="sort-android-photos-on-pc",
     title="Come ordinare le foto del tuo Android su un PC Windows",
     desc="Ordina migliaia di foto Android su Windows 10 o 11: cosa mostrano Esplora file e l'app Foto, e un metodo più rapido per raggruppare, confrontare ed eliminare.",
     h1="Come ordinare le foto del tuo Android su un PC Windows",
     body="""      <p>Windows legge bene i telefoni Android, ma leggere non vuol dire ordinare. Con migliaia di foto, gli strumenti integrati ti lasciano a scorrere un unico lungo elenco di nomi di file. Ecco cosa fanno e un metodo più rapido per liberare il telefono dal PC.</p>

      <h2>Con gli strumenti integrati in Windows</h2>
      <ul>
        <li><strong>Esplora file:</strong> dopo aver scelto «Trasferimento file» sul telefono, la sua cartella DCIM compare come semplici file. Da lì puoi eliminare, ma senza raggruppamenti e senza confronto tra scatti simili.</li>
        <li><strong>App Foto:</strong> importa una copia sul PC. Un buon backup, ma non ti dice cosa togliere dal telefono.</li>
        <li><strong>Collegamento al telefono:</strong> mostra solo le foto recenti, una alla volta.</li>
      </ul>

      <h2>Con PixCuller, passo dopo passo</h2>
      <p><strong>1. Installa PixCuller.</strong> Scaricalo gratis <a href="{win}">per Windows 10 o 11</a>, oppure dal Microsoft Store. Sul telefono non serve installare nulla.</p>
      <p><strong>2. Collegati via USB.</strong> Collega il telefono, sbloccalo e scegli «Trasferimento file» nella notifica USB. Poi clicca «Telefono Android» in PixCuller, e «Collega via USB».</p>
      <p><strong>3. Ordina un viaggio alla volta.</strong> La vista Viaggi raggruppa il rullino per data e luogo e mostra lo spazio occupato da ogni viaggio. Inizia dal più pesante.</p>
      <p><strong>4. Confronta e seleziona.</strong> Le foto simili hanno un badge: aprine fino a sei fianco a fianco, tieni la migliore e seleziona le altre, insieme a screenshot e video pesanti.</p>
      <p><strong>5. Elimina in sicurezza.</strong> Conferma, e PixCuller elimina le foto direttamente tramite il cavo. L'eliminazione è immediata e definitiva sul telefono (niente cestino), ma per impostazione predefinita PixCuller conserva per 30 giorni una copia di ogni elemento eliminato sul tuo PC, in una cartella «PixCuller Trash» dentro Immagini.</p>

      <h2>Da sapere</h2>
      <ul>
        <li>Tutto resta sul tuo PC e sul tuo telefono: nessun account, nessun cloud, nessun invio.</li>
        <li>Eliminare da Esplora file è definitivo e non conserva alcuna copia; PixCuller conserva per impostazione predefinita la copia di 30 giorni sul PC.</li>
        <li>PixCuller è gratuito, e ordinare una cartella sul PC funziona allo stesso modo.</li>
      </ul>"""),
dict(slug="free-up-android-from-mac-or-pc",
     title="Come liberare spazio su Android da un Mac o PC Windows",
     desc="Collega il tuo telefono Android via USB, ordina le foto su un grande schermo ed elimina ciò che non serve, senza Google One e senza caricare nulla online.",
     h1="Come liberare spazio sul tuo telefono Android da un Mac o PC",
     body="""      <p>Quando un telefono Android resta senza spazio, il motivo sono quasi sempre foto e video. Sistemarli su un piccolo schermo è lento. Da un computer vedi di più in una volta e decidi più in fretta, senza comprare altro spazio nel cloud.</p>

      <h2>Perché un computer aiuta</h2>
      <p>Un grande schermo mostra decine di foto insieme, un mouse ne seleziona centinaia in pochi secondi e confrontare scatti quasi identici fianco a fianco è molto più facile che passare avanti e indietro. Un rullino che sul telefono richiederebbe una serata si sistema in pochi minuti.</p>

      <h2>Il metodo</h2>
      <p><strong>1. Collega il telefono.</strong> Installa <a href="{pc}">PixCuller</a> su un PC Windows 10/11 o su un Mac con macOS 27 o successivo; sul telefono non serve installare nulla. Collega il telefono con un cavo USB, sbloccalo, scegli «Trasferimento file» nella notifica USB, poi clicca «Telefono Android» e «Collega via USB».</p>
      <p><strong>2. Parti da ciò che pesa di più.</strong> La vista Viaggi mostra lo spazio occupato da ogni viaggio; i video lunghi e le vecchie vacanze di solito liberano di più.</p>
      <p><strong>3. Elimina gli scatti quasi identici.</strong> Raffiche e scatti ripetuti della stessa scena hanno un badge. Confrontali fianco a fianco, tieni il migliore, seleziona gli altri.</p>
      <p><strong>4. Elimina screenshot e foto sfocate.</strong> Raramente meritano di restare e si selezionano in blocco in un attimo.</p>
      <p><strong>5. Conferma l'eliminazione.</strong> PixCuller elimina le foto direttamente tramite il cavo. L'eliminazione è immediata e definitiva sul telefono (nessun cestino da svuotare, lo spazio torna subito disponibile) e per impostazione predefinita PixCuller conserva per 30 giorni una copia di ogni elemento eliminato sul tuo computer, in una cartella «PixCuller Trash» dentro Immagini.</p>

      <h2>Mi serve Google One?</h2>
      <p>Lo spazio nel cloud è un buon backup, ma conserva tutto, compresi i duplicati. Fare ordine prima significa aver bisogno di meno spazio, sul telefono e nel cloud.</p>

      <h2>Da sapere</h2>
      <ul>
        <li>Nessun account e nessun invio: telefono e computer comunicano tramite il cavo USB.</li>
        <li>PixCuller è gratuito, senza abbonamento.</li>
      </ul>"""),
],
}
