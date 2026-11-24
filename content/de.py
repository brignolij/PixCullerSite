# -*- coding: utf-8 -*-
# Deutsche Fassung der FAQ und des Blogs der PixCuller-Website. Tokens in Antworten/Artikeln: {pc} {mac} {win} (siehe link_tokens).

BLOG_UI = dict(
    nav="Blog", privacy="Datenschutz", more="Weiterlesen",
    cta_mac="💻 PixCuller für Mac laden", cta_win="🪟 PixCuller für Windows laden",
    twin_android="Du nutzt ein Android-Telefon? Lies die Android-Anleitung:",
    twin_iphone="Du nutzt ein iPhone? Lies die iPhone-Anleitung:",
    index={
        "pixculler": dict(
            title="PixCuller Blog – Fotos am Mac oder PC sortieren",
            desc="Tausende Fotos am großen Bildschirm schneller sortieren, ähnliche Aufnahmen vergleichen und iPhone oder Android-Telefon vom Mac oder PC aus aufräumen.",
            h1="Anleitungen zum Sortieren deiner Fotos am Computer",
            intro="Warum ein großer Bildschirm das Sortieren von Fotos so viel schneller macht und wie du damit dein iPhone oder Android-Telefon aufräumst."),
    },
)

FAQ_PIXCULLER = dict(
    title="PixCuller FAQ – Fotos am Mac oder PC sortieren und löschen",
    desc="Tausende Fotos am Computer sortieren, ähnliche Aufnahmen vergleichen, iPhone oder Android-Telefon vom Mac oder PC aus aufräumen: Antworten zu PixCuller.",
    nav_home="PixCuller",
    h1="Fragen und Antworten",
    intro="Wie du deine Fotos am Computer schneller sortierst, dein iPhone oder Android-Telefon von einem Mac oder PC aus aufräumst und was PixCuller mit deinen Fotos macht (und nie macht).",
    qa=[
        ("Woher weiß PixCuller, dass ein Foto schon auf meinem Computer gesichert ist?",
         "Fügen Sie die Ordner, in denen Sie Ihre Fotos ablegen (eine Festplatte, einen USB-Stick), unter „Sicherungsordner“ hinzu. PixCuller sucht dann in ihnen eine identische Kopie jedes Fotos: gleicher Inhalt, nicht nur gleicher Name. Gefundene Fotos bekommen im Raster einen grünen Rahmen, und das Menü bietet zwei Filter, „Gesichert“ und „Nicht gesichert“. Die Ordner werden gemerkt, und die Prüfung ist ab dem zweiten Mal schnell. Wählen Sie die Ordner, in denen Sie Ihre Fotos wirklich sortieren, statt einer ganzen Festplatte: Das geht viel schneller. Ein Live Photo gilt als gesichert, wenn auch sein Video da ist (eine Option überspringt diese Prüfung). Nichts verlässt Ihren Computer."),
        ("Kann ich meine Fotos nach Ort oder Datum suchen?",
         "Ja. Geben Sie einen Ort, ein Land, ein Datum oder einen Dateinamen in das Suchfeld ein: „Mailand“, „Italien“, „August 2026“, „11.02.2025“. Der Ort stammt aus dem GPS der Fotos und wird offline bestimmt, es wird also nichts gesendet. Ein Kalender-Button filtert nach Zeitraum, und das Raster kann einen Abschnitt pro Tag zeigen oder dicht bleiben."),
        ('Wie sortiere ich meine iPhone-Fotos am Computer, Mac oder PC?',
         "Verbinde das iPhone per USB-Kabel mit dem Computer, entsperre es und tippe auf „Vertrauen“, dann öffne <a href=\"{pc}\">PixCuller</a>: Es gruppiert deine Fotorolle nach Reise, vergleicht ähnliche Aufnahmen nebeneinander und markiert Hunderte Fotos mit wenigen Klicks. Schritt-für-Schritt-Anleitungen: <a href=\"{post:sort-iphone-photos-on-mac}\">am Mac</a> und <a href=\"{post:sort-iphone-photos-on-pc}\">am Windows-PC</a>."),
        ("Warum Fotos am Computer statt auf dem iPhone sortieren?",
         "Ein großer Bildschirm zeigt mehr Fotos auf einmal, mit Maus und Tastatur wählst du Hunderte in Sekunden aus, und Aufnahmen nebeneinander zu vergleichen ist einfacher, als hin und her zu blättern. Eine Fotomediathek mit Tausenden Fotos zu sortieren, kostet am Telefon mehrere Sitzungen und am Mac oder PC deutlich weniger Zeit."),
        ("Was ist PixCuller?",
         "PixCuller ist eine kostenlose Desktop-App für Mac und Windows, die deine Fotos nach Reisen gruppiert, ähnliche Aufnahmen nebeneinander vergleicht und alles, was nicht behalten werden muss, gesammelt löscht. Sie liest die Fotomediathek eines iPhones oder Android-Telefons per USB-Kabel oder einen beliebigen Fotoordner auf deinem Computer und arbeitet 100 % auf dem Gerät."),
        ("Wie sortiere ich Tausende Fotos schnell?",
         "Öffne die Ansicht „Reisen“: Deine Mediathek ist nach Reisen gruppiert, mit dem Speicherplatz jeder Reise, sodass du mit der größten beginnst. Markiere innerhalb einer Reise Fotos gesammelt, vergleiche die ähnlichen nebeneinander und behalte die beste Aufnahme jeder Gruppe. Filter (eintägige Reisen, ausgeschlossene Orte wie Zuhause oder Arbeit, Größe) grenzen die Auswahl weiter ein."),
        ("Wie gebe ich iPhone Speicher von einem Mac oder PC aus frei?",
         "Verbinde dein iPhone per USB, öffne PixCuller, markiere die Reisen und Fotos, die du nicht mehr brauchst, und bestätige. PixCuller löscht sie direkt über das USB-Kabel, unter Windows 10/11 oder auf einem Mac mit macOS 27 oder neuer, sofern iCloud-Fotos ausgeschaltet ist. Das Löschen ist auf dem iPhone sofort und endgültig; eine Kopie bleibt standardmäßig 30 Tage auf deinem Computer. Unter macOS 26 oder älter zeigt und sortiert PixCuller die Fotos des iPhones weiterhin, aber du löschst sie in der Fotos-App des iPhones."),
        ("Kann ich Fotos direkt vom Computer aus von meinem iPhone löschen?",
         "Ja. Bei einem iPhone löscht PixCuller die Fotos direkt über das USB-Kabel, von einem Mac oder einem Windows-PC aus, ohne etwas zu kaufen. Drei Bedingungen: iCloud-Fotos ist auf dem iPhone ausgeschaltet (ist es eingeschaltet, erlaubt Apple dieses Löschen nicht), ein Mac läuft mit macOS 27 oder neuer (jeder Windows-10/11-PC funktioniert), und du nimmst in Kauf, dass das Löschen auf dem iPhone sofort und endgültig ist: Die Fotos landen nicht in „Zuletzt gelöscht“. Standardmäßig bewahrt PixCuller 30 Tage lang eine Kopie jedes gelöschten Elements auf deinem Computer auf, in einem Ordner „PixCuller Trash“ im Ordner Bilder (ein Kontrollkästchen beim Bestätigen), sodass sich ein Fehler durch erneutes Importieren der Datei rückgängig machen lässt. Live Photos und bearbeitete Fotos werden korrekt behandelt (alle Versionen werden zusammen gelöscht), und PixCuller zeigt bei einem bearbeiteten Foto die bearbeitete Version. Ist iCloud-Fotos eingeschaltet, schalte es aus (Einstellungen > [dein Name] > iCloud > Fotos) oder lösche in der Fotos-App des iPhones. Unter macOS 26 oder älter kann PixCuller die Fotos des iPhones anzeigen und sortieren, aber nicht löschen: Ein Banner in der App weist darauf hin, und du löschst in der Fotos-App des iPhones."),
        ("Ist das Löschen mit PixCuller endgültig?",
         "Auf einem Telefon ja. Bei einem iPhone oder einem Android-Telefon ist das Löschen über das USB-Kabel auf dem Telefon sofort und endgültig: Die Fotos landen weder in „Zuletzt gelöscht“ noch im Papierkorb des Telefons. Standardmäßig bewahrt PixCuller 30 Tage lang eine Kopie jedes gelöschten Elements auf deinem Computer auf, in einem Ordner „PixCuller Trash“ im Ordner Bilder (ein Kontrollkästchen beim Bestätigen), damit du es erneut importieren kannst. In einem Ordner auf deinem Computer landen die Dateien im Papierkorb."),
        ("Wie verbinde ich mein iPhone mit PixCuller?",
         "Verwende ein USB-Kabel, entsperre das iPhone und tippe auf „Vertrauen“, wenn du dazu aufgefordert wirst. Am Mac ist nichts weiter nötig. Installiere unter Windows die kostenlose App Apple Devices aus dem Microsoft Store, die den Treiber bereitstellt, mit dem PixCuller das iPhone lesen kann."),
        ("Kann ich die Fotos eines Android-Telefons an meinem Mac oder PC sortieren?",
         "Ja, per USB-Kabel: an jedem Windows-10/11-PC und an einem Mac mit macOS 27 oder neuer. Du bekommst dieselbe Reiseansicht, denselben Vergleich nebeneinander und dasselbe gesammelte Löschen wie beim iPhone. Auf dem Telefon muss nichts installiert werden."),
        ("Wie verbinde ich mein Android-Telefon?",
         "Schließe das Telefon per USB-Kabel an den Computer an, entsperre es und wähle in seiner USB-Benachrichtigung „Dateiübertragung“. Klicke in PixCuller auf „Android-Telefon“ und dann auf „Per USB verbinden“. Anleitungen: <a href=\"{post:sort-android-photos-on-mac}\">am Mac</a>, <a href=\"{post:sort-android-photos-on-pc}\">am Windows-PC</a>."),
        ("Warum sieht mein Mac mein Android-Telefon nicht?",
         "PixCuller liest Android-Telefone per USB unter macOS 27 oder neuer; auf einem älteren Mac zeigt die App eine entsprechende Meldung. Prüfe unter macOS 27 oder neuer, ob das Telefon entsperrt ist und in seiner USB-Benachrichtigung „Dateiübertragung“ gewählt ist. Unter Windows 10/11 funktioniert die USB-Verbindung mit jeder Version."),
        ("Muss ich etwas auf meinem Telefon installieren?",
         "Nein. PixCuller funktioniert allein, ohne dass etwas auf dem Telefon installiert werden muss und ohne andere App. Ein iPhone oder ein Android-Telefon braucht nur ein USB-Kabel. Unter Windows braucht das Lesen eines iPhones zusätzlich die kostenlose App Apple Devices auf dem PC, aus dem Microsoft Store."),
        ("Was passiert mit Fotos, die ich auf einem Android-Telefon lösche?",
         "PixCuller löscht sie direkt über das USB-Kabel, nachdem du bestätigt hast. Das Löschen ist sofort und endgültig: Die Fotos landen nicht im Papierkorb des Telefons. Standardmäßig bewahrt PixCuller 30 Tage lang eine Kopie jedes gelöschten Elements auf deinem Computer auf, in einem Ordner „PixCuller Trash“ im Ordner Bilder (ein Kontrollkästchen beim Bestätigen), sodass sich ein Fehler rückgängig machen lässt."),
        ("Wie finde ich doppelte Fotos in einem Ordner auf meinem Mac oder PC?",
         "Öffne den Ordner in PixCuller („Ordner öffnen“ oder per Drag-and-drop ins Fenster ziehen). Die App durchsucht auch die Unterordner, vergleicht, was auf den Fotos zu sehen ist, und versieht exakte Kopien, Serienaufnahmen und fast identische Aufnahmen mit demselben „≈ N“-Abzeichen. Behalte die beste Aufnahme jeder Gruppe und schicke den Rest in den Papierkorb. Anleitungen: <a href=\"{post:find-duplicate-photos-on-mac}\">am Mac</a>, <a href=\"{post:find-duplicate-photos-on-windows}\">unter Windows</a>."),
        ("Kann ich PixCuller für Fotos auf meinem Computer verwenden, nicht auf einem iPhone?",
         "Ja. Öffne einen beliebigen Ordner: PixCuller findet darin ähnliche Fotos, zeigt Markierungen an den ähnlichen und lässt dich vergleichen und löschen."),
        ("Wie findet PixCuller ähnliche Fotos?",
         "Es vergleicht den Inhalt deiner Fotos, nicht ihre Dateinamen, sodass Serienaufnahmen, fast identische Aufnahmen und dieselbe mehrfach aufgenommene Szene in derselben Gruppe landen. Du kannst bis zu 6 Fotos nebeneinander vergleichen und das schärfste, am besten komponierte behalten."),
        ("Wie vergleiche ich ähnliche Fotos nebeneinander?",
         "Wähle eine Gruppe ähnlicher Fotos aus und öffne den Vergleich: Bis zu 6 Fotos werden gleich groß angezeigt, sodass du Schärfe, Gesichtsausdrücke und Bildausschnitt beurteilen kannst. Behalte das beste und markiere den Rest."),
        ("Funktioniert PixCuller unter Windows?",
         "Ja: Windows 10 und 11 (64 Bit). Zum Lesen eines iPhones ist die kostenlose App Apple Devices aus dem Microsoft Store nötig. Die App ist noch nicht codesigniert, daher zeigt Windows SmartScreen beim ersten Start eventuell eine Warnung: Wähle „Weitere Informationen“ und dann „Trotzdem ausführen“."),
        ("Welche Macs unterstützt PixCuller?",
         "Macs mit Apple Silicon unter macOS 11 oder neuer. Die App ist von Apple signiert und notarisiert, sodass sie ohne Sicherheitswarnung geöffnet wird."),
        ("Ist PixCuller kostenlos? Gibt es ein Abo?",
         "Ja, PixCuller ist kostenlos, ohne Abo und ohne In-App-Kauf. Durchsehen, Vergleichen, Sortieren und Löschen sind kostenlos, auf einem Telefon wie in einem Ordner auf deinem Computer."),
        ("Sendet PixCuller meine Fotos an einen Server oder in die Cloud?",
         "Nein. PixCuller arbeitet 100 % auf dem Gerät: kein Konto, keine Cloud, und kein Foto, kein Video und kein Standort wird jemals irgendwohin gesendet. Die Ortserkennung und die Erkennung ähnlicher Fotos laufen auf deinem Computer. Es können nur anonyme, abschaltbare Nutzungsstatistiken gesendet werden."),
        ("Verändert PixCuller meine Originalfotos?",
         "Nein. PixCuller liest deine Fotos nur, um sie anzuzeigen und zu vergleichen. Die einzige Änderung, die es je vornimmt, ist das Löschen, das du bestätigst."),
        ("Wie blende ich mein Zuhause und meinen Arbeitsplatz in der Reiseansicht aus?",
         "Füge sie als ausgeschlossene Orte hinzu: Der Alltag erscheint dann nicht mehr als Reise und deine echten Reisen treten hervor."),
        ("Kann ich nach einem Urlaub am Computer aufräumen?",
         "Ja, das ist der typische Einsatz. Verbinde nach einer Reise das Telefon, öffne diese Reise in PixCuller, vergleiche die ähnlichen Aufnahmen, behalte die beste jeder Gruppe und lösche den Rest."),
        ("Kann ich PixCuller nutzen, um ein Fotoalbum oder ein Backup vorzubereiten?",
         "PixCuller hilft dir zu entscheiden, was behaltenswert ist: Sortiere die Reise, entferne die doppelten und fast identischen Aufnahmen und sichere oder teile dann, was übrig bleibt."),
    ],
    footer_copy="© 2026 PixCuller. Entwickelt von Jeffrey Brignoli.",
    footer_privacy="Datenschutz", footer_kofi="Ko-fi",
)

BLOG = {
"pixculler": [
dict(slug="sort-iphone-photos-on-mac",
     title="iPhone-Fotos am Mac sortieren: so geht's",
     desc="Tausende iPhone-Fotos am Mac sortieren: was Fotos und Digitale Bilder können und was nicht, und ein schnellerer Weg zum Gruppieren und Löschen.",
     h1="So sortierst du deine iPhone-Fotos am Mac",
     body="""      <p>Eine volle Fotorolle auf dem iPhone zu sortieren heißt stundenlang tippen. Am Mac siehst du viel mehr Fotos auf einmal, wählst mit der Maus aus und vergleichst Aufnahmen auf einem großen Bildschirm. So geht es, mit den Werkzeugen von macOS und mit einer eigenen App.</p>

      <h2>Mit den Werkzeugen von macOS</h2>
      <ul>
        <li><strong>Fotos:</strong> importiert eine Kopie deiner iPhone-Fotos auf den Mac. Nützlich als Backup, aber es sagt dir nicht, was du auf dem iPhone löschen kannst.</li>
        <li><strong>Digitale Bilder:</strong> listet die Fotos des iPhone als einfache Dateien auf, ohne Gruppierung nach Reise und ohne Vergleich ähnlicher Aufnahmen.</li>
      </ul>
      <p>Beides funktioniert, aber bei Tausenden Fotos scrollst du trotzdem durch eine einzige lange Liste.</p>

      <h2>Mit PixCuller, Schritt für Schritt</h2>
      <p><strong>1. PixCuller installieren.</strong> <a href="{mac}">Kostenlos herunterladen</a>: macOS 11 oder neuer auf Apple Silicon, von Apple signiert und notarisiert.</p>
      <p><strong>2. iPhone anschließen.</strong> Verbinde es per USB-Kabel, entsperre es und tippe auf „Vertrauen“.</p>
      <p><strong>3. Reise für Reise sortieren.</strong> Die Ansicht „Reisen“ gruppiert deine Fotorolle nach Datum und Ort und zeigt, wie viel Platz jede Reise belegt. Fang mit der größten an.</p>
      <p><strong>4. Vergleichen und markieren.</strong> Ähnliche Fotos tragen ein Abzeichen: Öffne bis zu sechs nebeneinander, behalte das beste und markiere den Rest, dazu Bildschirmfotos und große Videos, die du nicht brauchst.</p>
      <p><strong>5. Sicher löschen.</strong> Bei ausgeschaltetem iCloud-Fotos und macOS 27 oder neuer löscht PixCuller die Fotos direkt über das USB-Kabel. Das Löschen ist auf dem iPhone sofort und endgültig: Die Fotos landen nicht in „Zuletzt gelöscht“. Standardmäßig bewahrt PixCuller 30 Tage lang eine Kopie jedes gelöschten Elements auf deinem Mac auf, in einem Ordner „PixCuller Trash“ im Ordner Bilder, sodass sich ein Fehler durch erneutes Importieren der Datei rückgängig machen lässt. Ist iCloud-Fotos eingeschaltet, schalte es aus (Einstellungen > [dein Name] > iCloud > Fotos) oder lösche in der Fotos-App des iPhones.</p>

      <h2>Gut zu wissen</h2>
      <ul>
        <li>Alles bleibt auf deinem Mac und deinem iPhone: kein Konto, keine Cloud, kein Upload.</li>
        <li>PixCuller verändert nie deine Originale und löscht nur, was du bestätigst.</li>
        <li>Unter macOS 26 oder älter zeigt und sortiert PixCuller die Fotos des iPhones, kann sie aber nicht löschen: Ein Banner in der App weist darauf hin, und du löschst in der Fotos-App des iPhones.</li>
        <li>PixCuller ist kostenlos, und das Sortieren eines Fotoordners auf dem Mac funktioniert genauso.</li>
      </ul>"""),
dict(slug="sort-iphone-photos-on-pc",
     title="iPhone-Fotos am Windows-PC sortieren: so geht's",
     desc="Tausende iPhone-Fotos unter Windows 10 oder 11 sortieren: was die Fotos-App und der Explorer zeigen, und ein schnellerer Weg zum Sortieren und Löschen.",
     h1="So sortierst du deine iPhone-Fotos am Windows-PC",
     body="""      <p>iPhone, aber ein Windows-Computer? Du kannst deine Fotos trotzdem auf einem großen Bildschirm sortieren statt auf dem Telefon. Hier steht, was Windows allein kann, und ein schnellerer Weg.</p>

      <h2>Mit den Werkzeugen von Windows</h2>
      <ul>
        <li><strong>Fotos-App:</strong> importiert eine Kopie deiner iPhone-Fotos auf den PC. Gut als Backup, aber sie hilft dir nicht bei der Entscheidung, was weg kann.</li>
        <li><strong>Datei-Explorer:</strong> zeigt die Fotos des iPhone in Ordnern wie 100APPLE, benannt IMG_0001 und so weiter, ohne Reisen und ohne Vergleich ähnlicher Aufnahmen.</li>
      </ul>

      <h2>Mit PixCuller, Schritt für Schritt</h2>
      <p><strong>1. Apple Devices installieren.</strong> Installiere die kostenlose App Apple Devices aus dem Microsoft Store: Windows braucht sie, um ein iPhone zu lesen.</p>
      <p><strong>2. PixCuller installieren.</strong> Aus dem Microsoft Store oder <a href="{win}">kostenlos herunterladen</a> (Windows 10/11, 64 Bit). Der Download ist noch nicht signiert, daher kann SmartScreen beim ersten Start warnen.</p>
      <p><strong>3. iPhone anschließen.</strong> Verbinde es per USB-Kabel, entsperre es und tippe auf „Vertrauen“.</p>
      <p><strong>4. Reise für Reise sortieren.</strong> Die Ansicht „Reisen“ gruppiert deine Fotorolle nach Datum und Ort und zeigt, wie viel Platz jede Reise belegt. Fang mit der größten an.</p>
      <p><strong>5. Vergleichen, markieren, löschen.</strong> Ähnliche Fotos tragen ein Abzeichen: Vergleiche bis zu sechs nebeneinander, behalte das beste und markiere den Rest. Bei ausgeschaltetem iCloud-Fotos löscht PixCuller sie direkt über das USB-Kabel. Das Löschen ist auf dem iPhone endgültig (kein „Zuletzt gelöscht“), aber standardmäßig bewahrt PixCuller 30 Tage lang eine Kopie jedes gelöschten Elements auf deinem PC auf, in einem Ordner „PixCuller Trash“ im Ordner Bilder. Ist iCloud-Fotos eingeschaltet, schalte es aus (Einstellungen > [dein Name] > iCloud > Fotos) oder lösche in der Fotos-App des iPhones.</p>

      <h2>Gut zu wissen</h2>
      <ul>
        <li>Alles bleibt auf deinem PC und deinem iPhone: kein Konto, keine Cloud, kein Upload.</li>
        <li>PixCuller verändert nie deine Originale und löscht nur, was du bestätigst.</li>
        <li>Durchsehen und Sortieren sind kostenlos, und das Sortieren eines Fotoordners, der schon auf dem PC liegt, ist nie begrenzt.</li>
      </ul>"""),
dict(slug="sort-photos-on-computer",
     title="Tausende Fotos am Mac oder Windows-PC schneller sortieren",
     desc="Warum das Sortieren am großen Bildschirm so viel schneller geht als am Telefon – und eine einfache Methode für Tausende Fotos in einer Sitzung.",
     h1="So sortierst du Tausende Fotos schneller am Mac oder PC",
     body="""      <p>Wenn deine Fotomediathek zehntausend Fotos enthält, ist das Sortieren auf dem Telefonbildschirm ein Projekt, das du nie abschließen wirst. Am Computer kann es ein einziger Abend sein. Hier steht, warum, und eine Methode, die funktioniert.</p>

      <h2>Warum ein Computer schneller ist</h2>
      <ul>
        <li><strong>Mehr auf dem Bildschirm:</strong> Dutzende Fotos auf einmal statt einer Handvoll.</li>
        <li><strong>Präzise Auswahl:</strong> Mit Maus und Tastatur wählst du Hunderte Fotos in Sekunden aus.</li>
        <li><strong>Echter Vergleich:</strong> Ähnliche Fotos nebeneinander, in einer Größe, in der Schärfe und Gesichtsausdrücke sichtbar sind.</li>
      </ul>

      <h2>Eine Methode, die funktioniert</h2>
      <p><strong>1. Nach Reisen gruppieren.</strong> Das Sortieren nach Datum und Ort teilt die Mediathek in überschaubare Stücke. Beginne mit der Reise, die am meisten Platz belegt.</p>
      <p><strong>2. Die Beinahe-Kopien entfernen.</strong> Vergleiche jede Gruppe ähnlicher Aufnahmen, behalte die beste und markiere den Rest.</p>
      <p><strong>3. Störendes ausfiltern.</strong> Blende Orte aus, die dich nicht interessieren (Zuhause, Arbeit), damit echte Reisen hervortreten, und filtere nach Größe, um schwere Dateien zu finden.</p>
      <p><strong>4. Auf einmal löschen.</strong> Markiere Hunderte Fotos und bestätige einmal.</p>

      <h2>PixCuller macht genau das</h2>
      <p><a href="{pc}">PixCuller</a> ist eine kostenlose Desktop-App für Mac und Windows. Die Ansicht „Reisen“ gruppiert die Mediathek nach Reisen und zeigt den Speicherplatz jeder Reise, ähnliche Fotos tragen eine Markierung, und du kannst bis zu sechs nebeneinander vergleichen. Sie liest ein iPhone oder Android-Telefon per USB-Kabel oder einen beliebigen Ordner auf deinem Computer, arbeitet 100 % auf dem Gerät und verändert deine Originale nie.</p>
      <p>Auf einem Telefon löscht PixCuller direkt über das USB-Kabel, unter Windows 10/11 oder auf einem Mac mit macOS 27 oder neuer (bei einem iPhone mit ausgeschaltetem iCloud-Fotos). Das Löschen ist auf dem Telefon endgültig, standardmäßig bleibt 30 Tage lang eine Kopie auf deinem Computer. In einem Ordner landen die Dateien im Papierkorb. Das Sortieren ist nie begrenzt.</p>

      <h2>Tipps für eine lange Sitzung</h2>
      <ul>
        <li>Reise für Reise vorgehen, nicht durch die ganze Mediathek scrollen.</li>
        <li>Schnell entscheiden: Wenn zwei Aufnahmen gleich aussehen, behalte eine.</li>
        <li>Am Ende jeder Reise löschen, damit der Fortschritt sichtbar ist.</li>
      </ul>"""),
dict(slug="free-up-iphone-from-mac-or-pc",
     title="iPhone-Speicher vom Mac oder Windows-PC aus freigeben",
     desc="Schließe dein iPhone an, sortiere Fotos auf einem großen Bildschirm und lösche, was du nicht brauchst – ohne iCloud und ohne dass etwas online gesendet wird.",
     h1="So gibst du iPhone Speicher von einem Mac oder Windows-PC aus frei",
     body="""      <p>Ein volles iPhone am iPhone selbst aufzuräumen ist mühsam. Am Computer siehst du weit mehr Fotos auf einmal und entscheidest schneller. Hier der ganze Ablauf.</p>

      <h2>Was du brauchst</h2>
      <ul>
        <li>Einen Mac (Apple Silicon, macOS 11+) oder einen Windows-10/11-PC.</li>
        <li>Ein USB-Kabel. Unter Windows zusätzlich die kostenlose App Apple Devices aus dem Microsoft Store.</li>
        <li><a href="{pc}">PixCuller</a>, kostenlos für beide Systeme.</li>
        <li>Zum Löschen vom iPhone: iCloud-Fotos ausgeschaltet und auf einem Mac macOS 27 oder neuer. Unter macOS 26 oder älter zeigt und sortiert PixCuller die Fotos weiterhin, und du löschst sie in der Fotos-App des iPhones.</li>
      </ul>

      <h2>Schritt für Schritt</h2>
      <p><strong>1. Verbinden und vertrauen.</strong> Schließe das iPhone an, entsperre es und tippe auf „Vertrauen“.</p>
      <p><strong>2. Die Ansicht „Reisen“ öffnen.</strong> PixCuller gruppiert deine Fotomediathek nach Reisen und zeigt den Speicherplatz jeder Reise.</p>
      <p><strong>3. Die größten Reisen sortieren.</strong> Vergleiche ähnliche Aufnahmen, behalte die beste und markiere den Rest, dazu Screenshots und große Videos, die du nicht brauchst.</p>
      <p><strong>4. Das Löschen bestätigen.</strong> Bei ausgeschaltetem iCloud-Fotos (und macOS 27 oder neuer auf einem Mac) löscht PixCuller die Fotos direkt über das USB-Kabel, unter Windows ebenso. Das Löschen ist auf dem iPhone sofort und endgültig, aber standardmäßig bewahrt PixCuller 30 Tage lang eine Kopie jedes gelöschten Elements auf deinem Computer auf, in einem Ordner „PixCuller Trash“ im Ordner Bilder.</p>
      <p><strong>5. Wenn iCloud-Fotos eingeschaltet ist.</strong> PixCuller verweigert das Löschen: Schalte iCloud-Fotos aus (Einstellungen > [dein Name] > iCloud > Fotos) oder lösche in der Fotos-App des iPhones.</p>

      <h2>Ist das sicher?</h2>
      <p>Ja: Deine Fotos bleiben auf deinen Geräten, ohne Konto, ohne Cloud und ohne Upload. PixCuller liest deine Fotos nur, bis du bestätigst. Ein Löschen ist auf dem iPhone endgültig, aber standardmäßig bleibt 30 Tage lang eine Kopie auf deinem Computer.</p>


      <h2>Unter Windows</h2>
      <p>Die Schritte sind unter Windows 10 und 11 dieselben. Installiere zuerst die kostenlose App Apple Devices aus dem Microsoft Store, damit PixCuller das iPhone lesen kann. Die App ist noch nicht codesigniert, daher warnt SmartScreen beim ersten Start eventuell.</p>"""),
dict(slug="compare-similar-photos-keep-the-best",
     title="Ähnliche Fotos vergleichen und das beste behalten",
     desc="Eine einfache Routine, um unter fast identischen Fotos die beste Aufnahme zu wählen: worauf du achtest und wie es am großen Bildschirm schnell geht.",
     h1="So vergleichst du ähnliche Fotos und behältst das beste",
     body="""      <p>Du hast sechs Fotos desselben Moments gemacht und alle sehen gut aus. Mit der richtigen Methode dauert die Wahl der besten Sekunden, mit der falschen mehrere Minuten.</p>

      <h2>Worauf du achten solltest, in dieser Reihenfolge</h2>
      <ol>
        <li><strong>Schärfe.</strong> Zoome auf die Augen oder das Hauptmotiv. Ein unscharfes Motiv ist ein Ausschlusskriterium.</li>
        <li><strong>Gesichtsausdrücke.</strong> Augen offen, natürliches Lächeln, niemand mitten im Blinzeln.</li>
        <li><strong>Bildausschnitt.</strong> Nichts abgeschnitten, ein sauberer Hintergrund, ein gerader Horizont.</li>
        <li><strong>Moment.</strong> Wenn zwei Aufnahmen gleich gut sind, behalte die, die lebendiger wirkt.</li>
      </ol>

      <h2>Warum nebeneinander wichtig ist</h2>
      <p>Beim Hin- und Herblättern zwischen Fotos sind kleine Unterschiede schwer zu erkennen. Nebeneinander in gleicher Größe wird die schärfste oder am besten komponierte Aufnahme offensichtlich. Ein Computerbildschirm zeigt bis zu sechs auf einmal, wo ein Telefon nur eine zeigt.</p>

      <h2>Eine schnellere Routine</h2>
      <p>Gruppiere ähnliche Fotos zuerst, damit du sie nie in der Mediathek suchen musst. Öffne für jede Gruppe den Vergleich, wähle eines aus und markiere die anderen. Du entscheidest in Sekunden, nicht in Minuten.</p>

      <h2>Mit PixCuller</h2>
      <p><a href="{pc}">PixCuller</a> zeigt eine Markierung an ähnlichen Fotos, öffnet bis zu sechs nebeneinander und lässt dich den Rest mit einem Klick markieren. Es funktioniert mit einem per USB verbundenen iPhone oder mit jedem Ordner auf deinem Mac oder PC, offline, und verändert deine Originale nie.</p>

      <h2>Behalten statt bereuen</h2>
      <p>Wenn du unsicher bist, behalte zwei. Wenn PixCuller von einem Telefon löscht, bewahrt es standardmäßig 30 Tage lang eine Kopie auf deinem Computer auf; in einem Ordner landen die Dateien im Papierkorb. In beiden Fällen kannst du es dir noch anders überlegen.</p>"""),
dict(slug="find-duplicate-photos-on-mac",
     title="Doppelte und ähnliche Fotos am Mac finden und löschen",
     desc="Doppelte Fotos am Mac finden: exakte Kopien, Serien und fast identische Aufnahmen in Ordnern oder auf einer externen Festplatte, den Rest in den Papierkorb.",
     h1="So findest du doppelte und ähnliche Fotos am Mac",
     body="""      <p>Jahre voller Importe, Speicherkarten und Backups verteilen dieselben Fotos auf viele Ordner deines Macs. Manche sind exakte Kopien, die meisten sind fast identische Aufnahmen desselben Moments. So findest du beides, behältst die beste Aufnahme und gibst Speicherplatz frei, ohne deine Fotos-Mediathek anzufassen.</p>

      <h2>Was macOS bietet</h2>
      <ul>
        <li><strong>Finder:</strong> Ein Ordner nach Name oder Größe sortiert verrät offensichtliche Kopien wie „IMG_1234 Kopie.jpg“, aber keine zwei verschiedenen Aufnahmen derselben Szene.</li>
        <li><strong>Fotos:</strong> Das Album „Duplikate“ deckt nur Fotos ab, die schon in der Fotos-Mediathek liegen, nicht deine anderen Ordner oder Festplatten.</li>
      </ul>

      <h2>Mit PixCuller, Schritt für Schritt</h2>
      <p><strong>1. PixCuller installieren.</strong> <a href="{mac}">Kostenlos herunterladen</a>: macOS 11 oder neuer auf Apple Silicon, von Apple signiert und notarisiert.</p>
      <p><strong>2. Ordner öffnen.</strong> Klicke auf „Ordner öffnen“ oder ziehe einen Ordner ins Fenster. Unterordner sind eingeschlossen, ebenso externe Festplatten.</p>
      <p><strong>3. Auf die Abzeichen achten.</strong> PixCuller vergleicht den Inhalt der Fotos, nicht ihre Namen: Exakte Kopien, Serienaufnahmen und fast identische Aufnahmen tragen dasselbe „≈ N“-Abzeichen.</p>
      <p><strong>4. Die beste Aufnahme behalten.</strong> Öffne eine Gruppe, vergleiche bis zu sechs Fotos nebeneinander, behalte das schärfste und markiere den Rest.</p>
      <p><strong>5. Sicher löschen.</strong> Markierte Dateien landen im Papierkorb deines Macs, wo du sie mit „Zurücklegen“ wiederherstellen kannst, falls du es dir anders überlegst.</p>

      <h2>Gut zu wissen</h2>
      <ul>
        <li>Unterstützt werden JPEG, HEIC, PNG, TIFF, WebP und RAW-Dateien (CR2, CR3, NEF, ARW, RAF, ORF, RW2, DNG) sowie MOV- und MP4-Videos.</li>
        <li>Fotos werden nach ihren EXIF-Daten datiert, kopierte Ordner sortieren sich also weiterhin nach dem Tag der Aufnahme.</li>
        <li>Das Sortieren eines Ordners ist kostenlos und nie begrenzt. Alles läuft auf deinem Mac: kein Konto, kein Upload.</li>
        <li>Fotos-Mediatheken und App-Pakete im Ordner werden übersprungen, PixCuller wühlt also nie in den Dateien einer anderen App.</li>
      </ul>"""),
dict(slug="find-duplicate-photos-on-windows",
     title="Doppelte und ähnliche Fotos unter Windows finden",
     desc="Doppelte Fotos unter Windows finden: exakte Kopien, Serien und fast identische Aufnahmen in Ordnern oder auf externen Festplatten, den Rest in den Papierkorb.",
     h1="So findest du doppelte und ähnliche Fotos unter Windows 10 oder 11",
     body="""      <p>Handy-Backups, Speicherkarten und alte Kopien legen dieselben Fotos in mehreren Ordnern deines PCs ab. Manche sind exakte Duplikate, die meisten sind fast identische Aufnahmen. So findest du beides und räumst sicher auf.</p>

      <h2>Was Windows bietet</h2>
      <ul>
        <li><strong>Datei-Explorer:</strong> Sortieren nach Name, Größe oder Datum hilft bei offensichtlichen Kopien, erkennt aber nicht, dass zwei verschiedene Dateien dieselbe Szene zeigen.</li>
        <li><strong>Fotos-App:</strong> gut zum Ansehen und Importieren, aber ohne Werkzeug, um ähnliche Aufnahmen zu finden und die beste auszuwählen.</li>
      </ul>

      <h2>Mit PixCuller, Schritt für Schritt</h2>
      <p><strong>1. PixCuller installieren.</strong> Kostenlos <a href="{win}">für Windows 10 oder 11</a> (64 Bit) herunterladen oder aus dem Microsoft Store holen.</p>
      <p><strong>2. Ordner öffnen.</strong> Klicke auf „Ordner öffnen“ oder ziehe einen Ordner ins Fenster. Unterordner und externe Festplatten sind eingeschlossen.</p>
      <p><strong>3. Auf die Abzeichen achten.</strong> PixCuller vergleicht, was die Fotos zeigen, nicht ihre Dateinamen: Exakte Kopien, Serienaufnahmen und fast identische Aufnahmen tragen dasselbe „≈ N“-Abzeichen.</p>
      <p><strong>4. Die beste Aufnahme behalten.</strong> Vergleiche bis zu sechs Fotos nebeneinander, behalte das schärfste und markiere den Rest.</p>
      <p><strong>5. Sicher löschen.</strong> Markierte Dateien landen im Papierkorb, du kannst sie also wiederherstellen.</p>

      <h2>Gut zu wissen</h2>
      <ul>
        <li>Unterstützt werden JPEG, HEIC, PNG, TIFF, WebP und RAW-Dateien (CR2, CR3, NEF, ARW, RAF, ORF, RW2, DNG) sowie MOV- und MP4-Videos. Für HEIC-Vorschaubilder braucht Windows die kostenlosen HEIF-Bilderweiterungen von Microsoft.</li>
        <li>Fotos werden nach ihren EXIF-Daten datiert, kopierte Ordner sortieren sich also weiterhin nach dem Tag der Aufnahme.</li>
        <li>Das Sortieren eines Ordners ist kostenlos und nie begrenzt. Alles läuft auf deinem PC: kein Konto, kein Upload.</li>
      </ul>"""),
dict(slug="sort-photo-folder-external-drive",
     title="Großen Fotoordner oder externe Festplatte sortieren",
     desc="Alte Backups, Speicherkarten, eine externe Festplatte voller Fotos: eine einfache Methode, Tausende Dateien nach Reisen zu sortieren und Doppelte zu entfernen.",
     h1="So sortierst du einen großen Fotoordner oder eine ganze externe Festplatte",
     body="""      <p>Jeder hat so einen: einen Ordner „Fotos sortieren“, ein altes Handy-Backup, eine externe Festplatte, die über zehn Jahre voll geworden ist. Tausende Dateien, keine Ordnung, viele fast identische Aufnahmen. Hier eine Methode, die du in einer Sitzung schaffst.</p>

      <h2>1. Den ganzen Ordner auf einmal öffnen</h2>
      <p>Geh nicht Ordner für Ordner vor. Öffne den obersten Ordner in <a href="{pc}">PixCuller</a> („Ordner öffnen“ oder ins Fenster ziehen): Unterordner sind eingeschlossen, und jedes Foto wird nach seinen EXIF-Daten datiert, nicht nach dem Tag, an dem es kopiert wurde.</p>

      <h2>2. Die Reisen sichtbar machen</h2>
      <p>Die Ansicht „Reisen“ gruppiert Fotos nach Datum und Ort und zeigt den Speicherplatz jeder Gruppe. Zehn Jahre Dateien werden zu einer Liste von Reisen und Ereignissen, und du beginnst mit der größten.</p>

      <h2>3. Die Beinahe-Kopien zusammenfassen</h2>
      <p>Serienaufnahmen, wiederholte Versuche und Kopien derselben Aufnahme tragen ein „≈ N“-Abzeichen. Vergleiche bis zu sechs nebeneinander, behalte die beste und markiere den Rest. Allein dieser Schritt entfernt oft einen großen Teil der Dateien.</p>

      <h2>4. Das Offensichtliche markieren</h2>
      <p>Bildschirmfotos, verwackelte Aufnahmen, versehentliche Videos: Markiere sie nebenbei. Gelöscht wird erst, wenn du bestätigst.</p>

      <h2>5. Sicher löschen</h2>
      <p>Bestätigte Dateien landen im Papierkorb (am Mac wie unter Windows), ein Fehler lässt sich also rückgängig machen. Leere ihn erst, wenn du sicher bist.</p>

      <h2>Gut zu wissen</h2>
      <ul>
        <li>RAW-Dateien von Kameras (CR2, CR3, NEF, ARW, RAF, ORF, RW2, DNG) werden neben JPEG, HEIC, PNG und Videos unterstützt.</li>
        <li>Das Sortieren von Ordnern ist kostenlos und nie begrenzt, am Mac (<a href="{mac}">Download</a>) und unter Windows (<a href="{win}">Download</a>).</li>
        <li>Deine Originale werden nie verändert: Die einzige Änderung von PixCuller ist das Löschen, das du bestätigst.</li>
      </ul>"""),
dict(slug="sort-android-photos-on-mac",
     title="Android-Fotos am Mac sortieren: so geht's",
     desc="Ein Mac tat sich lange schwer, Android-Telefone per USB zu lesen. So sortierst du Tausende Android-Fotos am Mac mit macOS 27 und löschst, was du nicht brauchst.",
     h1="So sortierst du deine Android-Fotos am Mac",
     body="""      <p>Schließt du ein Android-Telefon an einen Mac an, passiert meist nichts Nützliches: macOS hat Android-Telefone nie per USB gelesen, wie Windows es tut. Dabei ist ein Mac der beste Ort, um eine große Fotorolle zu sortieren, mit großem Bildschirm, Maus und Vergleich nebeneinander. Das funktioniert.</p>

      <h2>Was macOS allein kann</h2>
      <ul>
        <li><strong>Digitale Bilder:</strong> sieht das Telefon eventuell, wenn du in der USB-Benachrichtigung „Fotos übertragen“ (PTP) wählst, aber nur als flache Dateiliste, ohne Gruppierung und ohne Vergleich ähnlicher Aufnahmen.</li>
        <li><strong>Android File Transfer von Google:</strong> wird nicht mehr gepflegt und kopiert ohnehin nur Dateien.</li>
        <li><strong>Cloud-Upload:</strong> alles an einen Online-Dienst zu senden, nur um es zu sortieren, ist langsam, verbraucht dein Datenvolumen und legt deine Fotos auf dem Server eines anderen ab.</li>
      </ul>

      <h2>Mit PixCuller, per USB, Schritt für Schritt</h2>
      <p><strong>1. PixCuller installieren.</strong> <a href="{mac}">PixCuller für Mac kostenlos herunterladen</a>. Zum Lesen eines Android-Telefons ist macOS 27 oder neuer nötig; auf einem älteren Mac zeigt die App eine entsprechende Meldung. Auf dem Telefon muss nichts installiert werden.</p>
      <p><strong>2. Telefon anschließen.</strong> Verbinde es per USB-Kabel, entsperre es und wähle in seiner USB-Benachrichtigung „Dateiübertragung“.</p>
      <p><strong>3. Verbinden.</strong> Klicke in PixCuller auf „Android-Telefon“ und dann auf „Per USB verbinden“.</p>
      <p><strong>4. Reise für Reise sortieren.</strong> Die Ansicht „Reisen“ gruppiert die Fotorolle nach Datum und Ort und zeigt, wie viel Platz jede Reise belegt. Ähnliche Fotos tragen ein Abzeichen: Vergleiche bis zu sechs nebeneinander, behalte das beste und markiere den Rest.</p>
      <p><strong>5. Sicher löschen.</strong> Klicke auf „Löschen“ und bestätige. PixCuller löscht die Fotos direkt über das Kabel: Das Löschen ist auf dem Telefon sofort und endgültig (die Fotos landen nicht in seinem Papierkorb), aber standardmäßig bewahrt PixCuller 30 Tage lang eine Kopie jedes gelöschten Elements auf deinem Mac auf, in einem Ordner „PixCuller Trash“ im Ordner Bilder, sodass sich ein Fehler rückgängig machen lässt.</p>

      <h2>Gut zu wissen</h2>
      <ul>
        <li>Alles bleibt auf deinem Mac und deinem Telefon: kein Konto, keine Cloud, kein Upload.</li>
        <li>PixCuller verändert nie deine Originale und löscht nur, was du bestätigst.</li>
        <li>PixCuller ist kostenlos, ohne Abo.</li>
        <li>Du hast auch ein iPhone? Es wird ebenfalls per USB-Kabel mit dem Mac verbunden.</li>
      </ul>"""),
dict(slug="sort-android-photos-on-pc",
     title="Android-Fotos am Windows-PC sortieren: so geht's",
     desc="Tausende Android-Fotos unter Windows 10 oder 11 sortieren: was Datei-Explorer und Fotos-App zeigen, und ein schnellerer Weg zum Vergleichen und Löschen.",
     h1="So sortierst du deine Android-Fotos am Windows-PC",
     body="""      <p>Windows liest Android-Telefone gut, aber Lesen ist noch kein Sortieren. Bei Tausenden Fotos lassen dich die integrierten Werkzeuge durch eine einzige lange Liste von Dateinamen scrollen. Hier steht, was sie können, und ein schnellerer Weg, das Telefon von deinem PC aus aufzuräumen.</p>

      <h2>Mit den Werkzeugen von Windows</h2>
      <ul>
        <li><strong>Datei-Explorer:</strong> Nachdem du am Telefon „Dateiübertragung“ gewählt hast, erscheint der Ordner DCIM als Dateien. Du kannst dort löschen, aber ohne Gruppierung und ohne Vergleich ähnlicher Aufnahmen.</li>
        <li><strong>Fotos-App:</strong> importiert eine Kopie auf den PC. Gut als Backup, aber sie sagt dir nicht, was du vom Telefon entfernen kannst.</li>
        <li><strong>Smartphone-Link:</strong> zeigt nur die letzten Fotos, eines nach dem anderen.</li>
      </ul>

      <h2>Mit PixCuller, Schritt für Schritt</h2>
      <p><strong>1. PixCuller installieren.</strong> Hole es dir kostenlos <a href="{win}">für Windows 10 oder 11</a> oder aus dem Microsoft Store. Auf dem Telefon muss nichts installiert werden.</p>
      <p><strong>2. Per USB verbinden.</strong> Schließe das Telefon an, entsperre es und wähle in seiner USB-Benachrichtigung „Dateiübertragung“. Klicke dann in PixCuller auf „Android-Telefon“ und auf „Per USB verbinden“.</p>
      <p><strong>3. Reise für Reise sortieren.</strong> Die Ansicht „Reisen“ gruppiert die Fotorolle nach Datum und Ort und zeigt, wie viel Platz jede Reise belegt. Fang mit der größten an.</p>
      <p><strong>4. Vergleichen und markieren.</strong> Ähnliche Fotos tragen ein Abzeichen: Öffne bis zu sechs nebeneinander, behalte das beste und markiere den Rest, dazu Screenshots und große Videos.</p>
      <p><strong>5. Sicher löschen.</strong> Bestätige, und PixCuller löscht die Fotos direkt über das Kabel. Das Löschen ist auf dem Telefon sofort und endgültig (kein Papierkorb), aber standardmäßig bewahrt PixCuller 30 Tage lang eine Kopie jedes gelöschten Elements auf deinem PC auf, in einem Ordner „PixCuller Trash“ im Ordner Bilder.</p>

      <h2>Gut zu wissen</h2>
      <ul>
        <li>Alles bleibt auf deinem PC und deinem Telefon: kein Konto, keine Cloud, kein Upload.</li>
        <li>Das Löschen im Datei-Explorer ist endgültig, ohne Kopie; PixCuller bewahrt standardmäßig die 30-Tage-Kopie auf dem PC auf.</li>
        <li>PixCuller ist kostenlos, und das Sortieren eines Ordners auf dem PC funktioniert genauso.</li>
      </ul>"""),
dict(slug="free-up-android-from-mac-or-pc",
     title="Android-Speicher freigeben: vom Mac oder PC aus aufräumen",
     desc="Verbinde dein Android-Telefon per USB, sortiere Fotos am großen Bildschirm und lösche, was du nicht brauchst, ohne Google One und ohne etwas hochzuladen.",
     h1="So gibst du Android-Speicher von einem Mac oder PC aus frei",
     body="""      <p>Wenn einem Android-Telefon der Platz ausgeht, sind fast immer Fotos und Videos der Grund. Sie am kleinen Bildschirm aufzuräumen ist mühsam. Am Computer siehst du mehr auf einmal und entscheidest schneller, ohne mehr Cloud-Speicher zu kaufen.</p>

      <h2>Warum ein Computer hilft</h2>
      <p>Ein großer Bildschirm zeigt Dutzende Fotos auf einmal, mit der Maus wählst du Hunderte in Sekunden aus, und fast identische Aufnahmen nebeneinander zu vergleichen ist viel einfacher, als hin und her zu wischen. Eine Fotorolle, die am Telefon einen ganzen Abend dauert, ist in Minuten erledigt.</p>

      <h2>Die Methode</h2>
      <p><strong>1. Das Telefon verbinden.</strong> Installiere <a href="{pc}">PixCuller</a> auf einem Windows-10/11-PC oder einem Mac mit macOS 27 oder neuer; auf dem Telefon muss nichts installiert werden. Schließe das Telefon per USB-Kabel an, entsperre es, wähle in seiner USB-Benachrichtigung „Dateiübertragung“ und klicke dann auf „Android-Telefon“ und „Per USB verbinden“.</p>
      <p><strong>2. Mit dem Schwersten beginnen.</strong> Die Ansicht „Reisen“ zeigt den Platz jeder Reise; lange Videos und alte Urlaube geben meist am meisten frei.</p>
      <p><strong>3. Die Beinahe-Kopien entfernen.</strong> Serienaufnahmen und wiederholte Aufnahmen derselben Szene tragen ein Abzeichen. Vergleiche sie nebeneinander, behalte die beste und markiere den Rest.</p>
      <p><strong>4. Screenshots und unscharfe Aufnahmen entfernen.</strong> Sie haben selten einen Platz verdient und sind als Stapel schnell markiert.</p>
      <p><strong>5. Das Löschen bestätigen.</strong> PixCuller löscht die Fotos direkt über das Kabel. Das Löschen ist auf dem Telefon sofort und endgültig (kein Papierkorb zu leeren, der Platz ist sofort wieder frei), und standardmäßig bewahrt PixCuller 30 Tage lang eine Kopie jedes gelöschten Elements auf deinem Computer auf, in einem Ordner „PixCuller Trash“ im Ordner Bilder.</p>

      <h2>Brauche ich Google One?</h2>
      <p>Cloud-Speicher ist ein gutes Backup, aber er behält alles, auch die Duplikate. Wer zuerst aufräumt, braucht weniger Speicherplatz, auf dem Telefon und in der Cloud.</p>

      <h2>Gut zu wissen</h2>
      <ul>
        <li>Kein Konto und kein Upload: Telefon und Computer sprechen über das USB-Kabel miteinander.</li>
        <li>PixCuller ist kostenlos, ohne Abo.</li>
      </ul>"""),
],
}
