# -*- coding: utf-8 -*-
# French version of the FAQ and blog of the PixCuller site. Tokens in answers/articles: {pc} {mac} {win} (see link_tokens).

BLOG_UI = dict(
    nav="Blog", privacy="Confidentialité", more="À lire aussi",
    cta_mac="💻 Télécharger PixCuller pour Mac", cta_win="🪟 Télécharger PixCuller pour Windows",
    twin_android="Vous avez un téléphone Android ? Lisez le guide Android :",
    twin_iphone="Vous avez un iPhone ? Lisez le guide iPhone :",
    index={
        "pixculler": dict(
            title="Blog PixCuller : trier ses photos sur Mac ou PC",
            desc="Guides pour trier des milliers de photos plus vite sur grand écran, comparer les photos similaires et vider votre iPhone ou Android depuis un Mac ou un PC.",
            h1="Guides pour trier vos photos sur ordinateur",
            intro="Pourquoi un grand écran change la vitesse à laquelle vous triez vos photos, et comment s'en servir pour vider votre iPhone ou votre téléphone Android."),
    },
)

FAQ_PIXCULLER = dict(
    title="FAQ PixCuller : trier et supprimer ses photos sur Mac ou PC",
    desc="Trier des milliers de photos sur ordinateur, comparer les similaires, libérer un iPhone ou un Android depuis un Mac ou un PC : les réponses sur PixCuller.",
    nav_home="PixCuller",
    h1="Questions et réponses",
    intro="Comment trier vos photos plus vite depuis un ordinateur, vider votre iPhone ou votre téléphone Android depuis un Mac ou un PC, et ce que PixCuller fait (et ne fait jamais) avec vos photos.",
    qa=[
        ("Comment PixCuller sait-il qu'une photo est déjà sauvegardée sur mon ordinateur ?",
         "Ajoutez les dossiers où vous rangez vos photos (un disque, une clé USB) dans « Dossiers de sauvegarde ». PixCuller cherche alors une copie identique de chaque photo dans ces dossiers : même contenu, pas seulement même nom. Les photos retrouvées sont encadrées de vert dans la grille, et le menu propose deux filtres, « Sauvées » et « Pas sauvées ». Les dossiers sont mémorisés, et la vérification est rapide dès la deuxième fois. Choisissez les dossiers où vous triez vraiment vos photos plutôt qu'un disque entier : c'est bien plus rapide. Une Live Photo compte comme sauvée si sa vidéo y est aussi (une option permet de ne pas la vérifier). Rien ne quitte votre ordinateur."),
        ("Puis-je chercher mes photos par lieu ou par date ?",
         "Oui. Tapez un lieu, un pays, une date ou un nom de fichier dans la barre de recherche : « Milan », « Italie », « août 2026 », « 11.02.2025 ». Le lieu vient du GPS des photos et se trouve hors ligne, donc rien n'est envoyé nulle part. Un bouton calendrier filtre par période, et la grille peut montrer une section par jour ou rester dense."),
        ('Comment trier les photos de mon iPhone sur ordinateur, Mac ou PC ?',
         "Branchez l'iPhone à l'ordinateur avec un câble USB, déverrouillez-le et touchez « Se fier », puis ouvrez <a href=\"{pc}\">PixCuller</a> : il regroupe votre pellicule par voyage, compare les photos similaires côte à côte et marque des centaines de photos en quelques clics. Guides pas à pas : <a href=\"{post:sort-iphone-photos-on-mac}\">sur Mac</a> et <a href=\"{post:sort-iphone-photos-on-pc}\">sur PC Windows</a>."),
        ("Pourquoi trier ses photos sur ordinateur plutôt que sur l'iPhone ?",
         "Un grand écran affiche plus de photos à la fois, une souris et un clavier en sélectionnent des centaines en quelques secondes, et comparer des photos côte à côte est plus facile que de faire des allers-retours. Trier une pellicule de plusieurs milliers de photos représente plusieurs séances sur un téléphone, et une session bien plus courte sur un Mac ou un PC."),
        ("Qu'est-ce que PixCuller ?",
         "PixCuller est une application de bureau gratuite pour Mac et Windows qui regroupe vos photos par voyage, compare les photos similaires côte à côte et supprime en masse ce qui ne mérite pas d'être gardé. Elle lit la pellicule d'un iPhone ou d'un téléphone Android par câble USB, ou n'importe quel dossier de photos de votre ordinateur, et fonctionne 100 % sur l'appareil."),
        ("Comment trier rapidement des milliers de photos ?",
         "Ouvrez la vue Voyages : votre photothèque est regroupée par voyage avec l'espace occupé par chacun, vous commencez donc par le plus lourd. Dans un voyage, sélectionnez les photos en masse, comparez les photos similaires côte à côte et gardez la meilleure de chaque groupe. Des filtres (voyages d'une seule journée, lieux exclus comme le domicile ou le travail, taille) permettent d'affiner."),
        ("Comment libérer de l'espace sur mon iPhone depuis un Mac ou un PC ?",
         "Branchez votre iPhone en USB, ouvrez PixCuller, sélectionnez les voyages et les photos dont vous n'avez plus besoin, puis confirmez. PixCuller les supprime directement par le câble USB, sous Windows 10/11 ou sur un Mac avec macOS 27 ou ultérieur, à condition que Photos iCloud soit désactivé. La suppression est immédiate et définitive sur l'iPhone, avec une copie gardée par défaut 30 jours sur votre ordinateur. Sous macOS 26 ou antérieur, PixCuller affiche et trie toujours les photos de l'iPhone, mais vous les supprimez dans l'app Photos de l'iPhone."),
        ("Puis-je supprimer des photos de mon iPhone directement depuis mon ordinateur ?",
         "Oui. Avec un iPhone, PixCuller supprime les photos directement par le câble USB, depuis un Mac ou un PC Windows, sans rien à acheter. Trois conditions : Photos iCloud est désactivé sur l'iPhone (quand il est activé, Apple n'autorise pas cette suppression), un Mac est sous macOS 27 ou ultérieur (n'importe quel PC Windows 10/11 fonctionne), et vous acceptez que la suppression soit immédiate et définitive sur l'iPhone : les photos ne passent pas par « Supprimés récemment ». Par défaut, PixCuller garde pendant 30 jours une copie de chaque élément supprimé sur votre ordinateur, dans un dossier « PixCuller Trash » du dossier Images (une case à cocher au moment de confirmer), de sorte qu'une erreur peut être annulée en réimportant le fichier. Les Live Photos et les photos retouchées sont gérées correctement (toutes leurs versions sont supprimées ensemble), et PixCuller affiche la version retouchée d'une photo retouchée. Si Photos iCloud est activé, désactivez-le (Réglages > [votre nom] > iCloud > Photos) ou supprimez dans l'app Photos de l'iPhone. Sous macOS 26 ou antérieur, PixCuller peut afficher et trier les photos de l'iPhone mais pas les supprimer : un bandeau dans l'app l'indique, et vous supprimez dans l'app Photos de l'iPhone."),
        ("La suppression depuis PixCuller est-elle définitive ?",
         "Sur un téléphone, oui. Avec un iPhone ou un téléphone Android, la suppression par le câble USB est immédiate et définitive sur le téléphone : les photos ne passent ni par « Supprimés récemment » ni par la corbeille du téléphone. Par défaut, PixCuller garde pendant 30 jours une copie de chaque élément supprimé sur votre ordinateur, dans un dossier « PixCuller Trash » du dossier Images (une case à cocher au moment de confirmer), pour pouvoir le réimporter. Dans un dossier de votre ordinateur, les fichiers vont à la Corbeille."),
        ("Comment connecter mon iPhone à PixCuller ?",
         "Utilisez un câble USB, déverrouillez l'iPhone et touchez « Se fier à cet ordinateur » quand on vous le demande. Sur Mac, rien d'autre n'est nécessaire. Sur Windows, installez l'app gratuite Apple Devices depuis le Microsoft Store, qui fournit le pilote permettant à PixCuller de lire l'iPhone."),
        ("Puis-je trier les photos d'un téléphone Android sur mon Mac ou mon PC ?",
         "Oui, par câble USB : sur n'importe quel PC Windows 10/11, et sur un Mac avec macOS 27 ou ultérieur. Vous retrouvez la même vue Voyages, la même comparaison côte à côte et la même suppression en masse qu'avec un iPhone. Rien n'est à installer sur le téléphone."),
        ("Comment connecter mon téléphone Android ?",
         "Branchez le téléphone à l'ordinateur avec un câble USB, déverrouillez-le et choisissez « Transfert de fichiers » dans sa notification USB. Dans PixCuller, cliquez sur « Téléphone Android », puis sur « Connecter en USB ». Guides : <a href=\"{post:sort-android-photos-on-mac}\">sur Mac</a>, <a href=\"{post:sort-android-photos-on-pc}\">sur PC Windows</a>."),
        ("Pourquoi mon Mac ne voit-il pas mon téléphone Android ?",
         "PixCuller lit les téléphones Android en USB sous macOS 27 ou ultérieur ; sur un Mac plus ancien, l'app affiche un message qui l'indique. Sous macOS 27 ou ultérieur, vérifiez que le téléphone est déverrouillé et que « Transfert de fichiers » est choisi dans sa notification USB. Sous Windows 10/11, la connexion USB fonctionne avec n'importe quelle version."),
        ("Dois-je installer quelque chose sur mon téléphone ?",
         "Non. PixCuller fonctionne seul, sans rien à installer sur le téléphone et sans aucune autre app. Un iPhone ou un téléphone Android n'a besoin que d'un câble USB. Sous Windows, la lecture d'un iPhone nécessite aussi l'app gratuite Apple Devices sur le PC, depuis le Microsoft Store."),
        ("Que deviennent les photos que je supprime sur un téléphone Android ?",
         "PixCuller les supprime directement par le câble USB, après votre confirmation. La suppression est immédiate et définitive : les photos ne passent pas par la corbeille du téléphone. Par défaut, PixCuller garde pendant 30 jours une copie de chaque élément supprimé sur votre ordinateur, dans un dossier « PixCuller Trash » du dossier Images (une case à cocher au moment de confirmer), de sorte qu'une erreur peut être annulée."),
        ("Comment trouver les photos en double dans un dossier sur mon Mac ou mon PC ?",
         "Ouvrez le dossier dans PixCuller (« Ouvrir un dossier », ou glissez-le sur la fenêtre). Il parcourt les sous-dossiers, compare ce que montrent les photos et appose le même badge « ≈ N » sur les copies exactes, les rafales et les prises quasi identiques. Gardez la meilleure de chaque groupe et envoyez le reste à la Corbeille. Guides : <a href=\"{post:find-duplicate-photos-on-mac}\">sur Mac</a>, <a href=\"{post:find-duplicate-photos-on-windows}\">sur Windows</a>."),
        ("Puis-je utiliser PixCuller sur des photos stockées sur mon ordinateur, et non sur un iPhone ?",
         "Oui. Ouvrez n'importe quel dossier : PixCuller y repère les photos similaires, affiche les badges sur celles-ci et vous laisse comparer et supprimer."),
        ("Comment PixCuller détecte-t-il les photos similaires ?",
         "Il compare le contenu de vos photos, pas leurs noms de fichiers : les rafales, les prises presque identiques et la même scène photographiée plusieurs fois se retrouvent dans le même groupe. Vous pouvez comparer jusqu'à 6 photos côte à côte et garder la plus nette, la mieux cadrée."),
        ("Comment comparer des photos similaires côte à côte ?",
         "Sélectionnez un groupe de photos similaires et ouvrez la comparaison : jusqu'à 6 photos s'affichent à la même taille pour juger la mise au point, les expressions et le cadrage. Gardez la meilleure et sélectionnez les autres."),
        ("PixCuller fonctionne-t-il sous Windows ?",
         "Oui : Windows 10 et 11 (64 bits). La lecture d'un iPhone nécessite l'app gratuite Apple Devices du Microsoft Store. L'application n'est pas encore signée numériquement, donc Windows SmartScreen peut afficher un avertissement au premier lancement : choisissez « Informations complémentaires » puis « Exécuter quand même »."),
        ("Quels Mac PixCuller prend-il en charge ?",
         "Les Mac avec puce Apple Silicon sous macOS 11 ou version ultérieure. L'application est signée et notarisée par Apple, elle s'ouvre donc sans avertissement de sécurité."),
        ("PixCuller est-il gratuit ? Y a-t-il un abonnement ?",
         "Oui, PixCuller est gratuit, sans abonnement et sans achat intégré. Parcourir, comparer, trier et supprimer est gratuit, sur un téléphone comme dans un dossier de votre ordinateur."),
        ("PixCuller envoie-t-il mes photos vers un serveur ou le cloud ?",
         "Non. PixCuller fonctionne 100 % sur l'appareil : pas de compte, pas de cloud, aucune photo, vidéo ni position n'est jamais envoyée où que ce soit. La reconnaissance des lieux et la détection des photos similaires s'exécutent sur votre ordinateur. Seules des statistiques d'usage anonymes, désactivables, peuvent être envoyées."),
        ("PixCuller modifie-t-il mes photos originales ?",
         "Non. PixCuller ne fait que lire vos photos pour les afficher et les comparer. La seule modification qu'il effectue est la suppression que vous confirmez."),
        ("Comment masquer mon domicile et mon lieu de travail dans la vue Voyages ?",
         "Ajoutez-les comme lieux exclus : le quotidien cesse alors d'apparaître comme un voyage et vos vrais voyages ressortent."),
        ("Puis-je faire le tri après des vacances depuis mon ordinateur ?",
         "Oui, c'est l'usage typique. Après un voyage, branchez le téléphone, ouvrez ce voyage dans PixCuller, comparez les photos similaires, gardez la meilleure de chaque groupe et supprimez le reste."),
        ("Puis-je utiliser PixCuller pour préparer un album photo ou une sauvegarde ?",
         "PixCuller vous aide à décider ce qui mérite d'être gardé : triez le voyage, supprimez les doublons et les photos quasi identiques, puis sauvegardez ou partagez ce qui reste."),
    ],
    footer_copy="© 2026 PixCuller. Développé par Jeffrey Brignoli.",
    footer_privacy="Confidentialité", footer_kofi="Ko-fi",
)

BLOG = {
"pixculler": [
dict(slug="sort-iphone-photos-on-mac",
     title="Comment trier les photos de son iPhone sur Mac",
     desc="Triez des milliers de photos d'iPhone sur votre Mac : ce que Photos et Transfert d'images savent faire, et une méthode plus rapide pour trier.",
     h1="Comment trier les photos de son iPhone sur Mac",
     body="""      <p>Trier une pellicule pleine sur l'iPhone, ce sont des heures de tapotements. Sur un Mac, vous voyez bien plus de photos à la fois, vous sélectionnez à la souris et vous comparez sur grand écran. Voici comment faire, avec les outils de macOS et avec une application dédiée.</p>

      <h2>Avec les outils intégrés à macOS</h2>
      <ul>
        <li><strong>Photos :</strong> importe une copie des photos de l'iPhone sur le Mac. Pratique comme sauvegarde, mais il ne vous dit pas quoi supprimer sur l'iPhone.</li>
        <li><strong>Transfert d'images :</strong> liste les photos de l'iPhone comme de simples fichiers, sans regroupement par voyage ni comparaison des photos similaires.</li>
      </ul>
      <p>Les deux fonctionnent, mais avec des milliers de photos, vous faites toujours défiler une seule longue liste.</p>

      <h2>Avec PixCuller, étape par étape</h2>
      <p><strong>1. Installez PixCuller.</strong> <a href="{mac}">Téléchargez-le gratuitement</a> : macOS 11 ou ultérieur sur Apple Silicon, signé et notarisé par Apple.</p>
      <p><strong>2. Branchez l'iPhone.</strong> Connectez-le avec un câble USB, déverrouillez-le et touchez « Se fier ».</p>
      <p><strong>3. Triez voyage par voyage.</strong> La vue Voyages regroupe votre pellicule par date et par lieu et indique la place prise par chaque voyage. Commencez par le plus lourd.</p>
      <p><strong>4. Comparez et marquez.</strong> Les photos similaires portent un badge : ouvrez-en jusqu'à six côte à côte, gardez la meilleure et marquez les autres, ainsi que les captures d'écran et les grosses vidéos inutiles.</p>
      <p><strong>5. Supprimez sans risque.</strong> Avec Photos iCloud désactivé et macOS 27 ou ultérieur, PixCuller supprime les photos directement par le câble USB. La suppression est immédiate et définitive sur l'iPhone : les photos ne passent pas par « Supprimés récemment ». Par défaut, PixCuller garde pendant 30 jours une copie de chaque élément supprimé sur votre Mac, dans un dossier « PixCuller Trash » du dossier Images, de sorte qu'une erreur peut être annulée en réimportant le fichier. Si Photos iCloud est activé, désactivez-le (Réglages > [votre nom] > iCloud > Photos) ou supprimez dans l'app Photos de l'iPhone.</p>

      <h2>Bon à savoir</h2>
      <ul>
        <li>Tout reste sur votre Mac et votre iPhone : pas de compte, pas de cloud, aucun envoi.</li>
        <li>PixCuller ne modifie jamais vos originaux et ne supprime que ce que vous confirmez.</li>
        <li>Sous macOS 26 ou antérieur, PixCuller affiche et trie les photos de l'iPhone mais ne peut pas les supprimer : un bandeau dans l'app l'indique, et vous supprimez dans l'app Photos de l'iPhone.</li>
        <li>PixCuller est gratuit, et trier un dossier de photos sur le Mac fonctionne de la même façon.</li>
      </ul>"""),
dict(slug="sort-iphone-photos-on-pc",
     title="Comment trier les photos de son iPhone sur PC Windows",
     desc="Triez des milliers de photos d'iPhone sur Windows 10 ou 11 : ce que montrent l'app Photos et l'Explorateur, et une méthode plus rapide pour trier.",
     h1="Comment trier les photos de son iPhone sur PC Windows",
     body="""      <p>Un iPhone et un ordinateur Windows ? Vous pouvez quand même trier vos photos sur grand écran plutôt que sur le téléphone. Voici ce que Windows sait faire seul, et une méthode plus rapide.</p>

      <h2>Avec les outils intégrés à Windows</h2>
      <ul>
        <li><strong>App Photos :</strong> importe une copie des photos de l'iPhone sur le PC. Bien pour une sauvegarde, mais elle ne vous aide pas à choisir quoi supprimer.</li>
        <li><strong>Explorateur de fichiers :</strong> affiche les photos de l'iPhone dans des dossiers comme 100APPLE, nommées IMG_0001 et ainsi de suite, sans voyages ni comparaison des photos similaires.</li>
      </ul>

      <h2>Avec PixCuller, étape par étape</h2>
      <p><strong>1. Installez Apple Devices.</strong> Installez l'app gratuite Apple Devices depuis le Microsoft Store : Windows en a besoin pour lire un iPhone.</p>
      <p><strong>2. Installez PixCuller.</strong> Depuis le Microsoft Store ou en <a href="{win}">le téléchargeant gratuitement</a> (Windows 10/11, 64 bits). Le téléchargement n'est pas encore signé, SmartScreen peut donc afficher un avertissement au premier lancement.</p>
      <p><strong>3. Branchez l'iPhone.</strong> Connectez-le avec un câble USB, déverrouillez-le et touchez « Se fier ».</p>
      <p><strong>4. Triez voyage par voyage.</strong> La vue Voyages regroupe votre pellicule par date et par lieu et indique la place prise par chaque voyage. Commencez par le plus lourd.</p>
      <p><strong>5. Comparez, marquez, supprimez.</strong> Les photos similaires portent un badge : comparez-en jusqu'à six côte à côte, gardez la meilleure et marquez les autres. Avec Photos iCloud désactivé, PixCuller les supprime directement par le câble USB. La suppression est définitive sur l'iPhone (pas de « Supprimés récemment »), mais PixCuller garde par défaut pendant 30 jours une copie de chaque élément supprimé sur votre PC, dans un dossier « PixCuller Trash » du dossier Images. Si Photos iCloud est activé, désactivez-le (Réglages > [votre nom] > iCloud > Photos) ou supprimez dans l'app Photos de l'iPhone.</p>

      <h2>Bon à savoir</h2>
      <ul>
        <li>Tout reste sur votre PC et votre iPhone : pas de compte, pas de cloud, aucun envoi.</li>
        <li>PixCuller ne modifie jamais vos originaux et ne supprime que ce que vous confirmez.</li>
        <li>Parcourir et trier est gratuit, et trier un dossier de photos déjà sur le PC n'est jamais limité.</li>
      </ul>"""),
dict(slug="sort-photos-on-computer",
     title="Trier des milliers de photos plus vite sur Mac ou PC Windows",
     desc="Pourquoi trier ses photos sur grand écran va bien plus vite que sur un téléphone, et une méthode simple pour en trier des milliers en une séance.",
     h1="Comment trier des milliers de photos plus vite sur Mac ou PC",
     body="""      <p>Si votre pellicule contient dix mille photos, la trier sur l'écran d'un téléphone est un chantier que vous ne finirez jamais. Sur un ordinateur, ça peut tenir en une soirée. Voici pourquoi, et une méthode qui marche.</p>

      <h2>Pourquoi un ordinateur est plus rapide</h2>
      <ul>
        <li><strong>Plus à l'écran :</strong> des dizaines de photos à la fois au lieu de quelques-unes.</li>
        <li><strong>Sélection précise :</strong> une souris et un clavier sélectionnent des centaines de photos en quelques secondes.</li>
        <li><strong>Vraie comparaison :</strong> les photos similaires côte à côte, à une taille où l'on voit la netteté et les expressions.</li>
      </ul>

      <h2>Une méthode qui marche</h2>
      <p><strong>1. Regroupez par voyage.</strong> Trier par date et par lieu découpe la photothèque en morceaux gérables. Commencez par le voyage qui prend le plus de place.</p>
      <p><strong>2. Supprimez les quasi-copies.</strong> Comparez chaque groupe de photos similaires, gardez la meilleure et sélectionnez les autres.</p>
      <p><strong>3. Filtrez le bruit.</strong> Masquez les lieux qui ne vous intéressent pas (domicile, travail) pour que les vrais voyages ressortent, et filtrez par taille pour trouver les fichiers lourds.</p>
      <p><strong>4. Supprimez d'un coup.</strong> Sélectionnez des centaines de photos et confirmez une seule fois.</p>

      <h2>PixCuller fait exactement ça</h2>
      <p><a href="{pc}">PixCuller</a> est une application de bureau gratuite pour Mac et Windows. Sa vue Voyages regroupe la photothèque par voyage et indique l'espace occupé par chacun, les photos similaires portent un badge, et vous pouvez en comparer jusqu'à six côte à côte. Elle lit un iPhone ou un téléphone Android par câble USB, ou n'importe quel dossier de votre ordinateur, fonctionne 100 % sur l'appareil et ne modifie jamais vos originaux.</p>
      <p>Sur un téléphone, PixCuller supprime directement par le câble USB, sous Windows 10/11 ou sur un Mac avec macOS 27 ou ultérieur (avec Photos iCloud désactivé sur un iPhone). La suppression est définitive sur le téléphone, avec une copie gardée par défaut 30 jours sur votre ordinateur. Dans un dossier, les fichiers vont à la Corbeille. Le tri n'est jamais limité.</p>

      <h2>Conseils pour une longue séance</h2>
      <ul>
        <li>Travaillez voyage par voyage, plutôt qu'en faisant défiler toute la photothèque.</li>
        <li>Décidez vite : si deux photos se ressemblent, gardez-en une.</li>
        <li>Supprimez à la fin de chaque voyage, pour voir votre progression.</li>
      </ul>"""),
dict(slug="free-up-iphone-from-mac-or-pc",
     title="Libérer de l'espace sur iPhone depuis un Mac ou un PC",
     desc="Branchez votre iPhone, triez vos photos sur grand écran et supprimez ce dont vous n'avez pas besoin, sans iCloud et sans rien envoyer en ligne.",
     h1="Comment libérer de l'espace sur votre iPhone depuis un Mac ou un PC Windows",
     body="""      <p>Faire le ménage dans un iPhone plein, directement sur l'iPhone, est fastidieux. Depuis un ordinateur, vous voyez bien plus de photos à la fois et décidez plus vite. Voici toute la démarche.</p>

      <h2>Ce qu'il vous faut</h2>
      <ul>
        <li>Un Mac (Apple Silicon, macOS 11 ou ultérieur) ou un PC Windows 10/11.</li>
        <li>Un câble USB. Sous Windows, aussi l'app gratuite Apple Devices du Microsoft Store.</li>
        <li><a href="{pc}">PixCuller</a>, gratuit sur les deux systèmes.</li>
        <li>Pour supprimer depuis l'iPhone : Photos iCloud désactivé et, sur un Mac, macOS 27 ou ultérieur. Sous macOS 26 ou antérieur, PixCuller affiche et trie toujours les photos, et vous les supprimez dans l'app Photos de l'iPhone.</li>
      </ul>

      <h2>Pas à pas</h2>
      <p><strong>1. Branchez et faites confiance.</strong> Connectez l'iPhone, déverrouillez-le et touchez « Se fier ».</p>
      <p><strong>2. Ouvrez la vue Voyages.</strong> PixCuller regroupe votre pellicule par voyage et indique l'espace occupé par chacun.</p>
      <p><strong>3. Triez les voyages les plus lourds.</strong> Comparez les photos similaires, gardez la meilleure et sélectionnez le reste, ainsi que les captures d'écran et les grosses vidéos dont vous n'avez pas besoin.</p>
      <p><strong>4. Confirmez la suppression.</strong> Avec Photos iCloud désactivé (et macOS 27 ou ultérieur sur un Mac), PixCuller supprime les photos directement par le câble USB, sous Windows aussi. La suppression est immédiate et définitive sur l'iPhone, mais PixCuller garde par défaut pendant 30 jours une copie de chaque élément supprimé sur votre ordinateur, dans un dossier « PixCuller Trash » du dossier Images.</p>
      <p><strong>5. Si Photos iCloud est activé.</strong> PixCuller refuse la suppression : désactivez Photos iCloud (Réglages > [votre nom] > iCloud > Photos) ou supprimez dans l'app Photos de l'iPhone.</p>

      <h2>Est-ce sûr ?</h2>
      <p>Oui : vos photos restent sur vos appareils, sans compte, sans cloud et sans envoi. PixCuller ne fait que lire vos photos tant que vous n'avez pas confirmé. Une suppression est définitive sur l'iPhone, mais une copie reste par défaut 30 jours sur votre ordinateur.</p>


      <h2>Sous Windows</h2>
      <p>Les étapes sont les mêmes sous Windows 10 et 11. Installez d'abord l'app gratuite Apple Devices du Microsoft Store, pour que PixCuller puisse lire l'iPhone. L'application n'est pas encore signée numériquement, donc SmartScreen peut afficher un avertissement au premier lancement.</p>"""),
dict(slug="compare-similar-photos-keep-the-best",
     title="Comparer des photos similaires et garder la meilleure",
     desc="Une routine simple pour choisir la meilleure prise parmi des photos quasi identiques : ce qu'il faut regarder, et comment aller vite sur grand écran.",
     h1="Comment comparer des photos similaires et garder la meilleure",
     body="""      <p>Vous avez pris six photos du même moment et elles ont toutes l'air bien. Choisir la meilleure prend quelques secondes avec la bonne méthode, et plusieurs minutes avec la mauvaise.</p>

      <h2>Ce qu'il faut vérifier, dans cet ordre</h2>
      <ol>
        <li><strong>La netteté.</strong> Zoomez sur les yeux ou sur le sujet principal. Un sujet flou est éliminatoire.</li>
        <li><strong>Les expressions.</strong> Yeux ouverts, sourires naturels, personne en plein clignement.</li>
        <li><strong>Le cadrage.</strong> Rien de coupé, un arrière-plan propre, l'horizon droit.</li>
        <li><strong>Le moment.</strong> Si deux photos se valent, gardez celle qui paraît la plus vivante.</li>
      </ol>

      <h2>Pourquoi le côte à côte compte</h2>
      <p>Passer d'une photo à l'autre rend les petites différences difficiles à voir. Les voir l'une à côté de l'autre, à la même taille, rend évidente la plus nette ou la mieux cadrée. Un écran d'ordinateur en affiche jusqu'à six à la fois, là où un téléphone en montre une.</p>

      <h2>Une routine plus rapide</h2>
      <p>Regroupez d'abord les photos similaires, pour ne jamais avoir à les chercher dans la photothèque. Pour chaque groupe, ouvrez la comparaison, choisissez-en une et sélectionnez les autres. Vous décidez en quelques secondes, pas en minutes.</p>

      <h2>Faites-le avec PixCuller</h2>
      <p><a href="{pc}">PixCuller</a> affiche un badge sur les photos similaires, en ouvre jusqu'à six côte à côte et vous laisse sélectionner les autres en un clic. Il fonctionne avec un iPhone connecté en USB ou avec n'importe quel dossier de votre Mac ou PC, hors ligne, et ne modifie jamais vos originaux.</p>

      <h2>Gardez, sans regret</h2>
      <p>Quand vous hésitez, gardez-en deux. Quand PixCuller supprime sur un téléphone, il garde par défaut une copie sur votre ordinateur pendant 30 jours ; dans un dossier, les fichiers vont à la Corbeille. Dans les deux cas, vous pouvez encore changer d'avis.</p>"""),
dict(slug="find-duplicate-photos-on-mac",
     title="Trouver les photos en double et similaires sur Mac",
     desc="Trouvez copies exactes, rafales et prises quasi identiques dans vos dossiers photos ou sur un disque externe, gardez la meilleure et supprimez le reste.",
     h1="Comment trouver les photos en double et similaires sur Mac",
     body="""      <p>Des années d'imports, de cartes mémoire et de sauvegardes laissent les mêmes photos éparpillées dans des dossiers sur un Mac. Certaines sont des copies exactes ; la plupart sont des prises quasi identiques du même instant. Voici comment trouver les deux, garder la meilleure et libérer de la place, sans toucher à votre photothèque Photos.</p>

      <h2>Ce que propose macOS</h2>
      <ul>
        <li><strong>Finder :</strong> trier un dossier par nom ou par taille aide à repérer les copies évidentes comme « IMG_1234 copie.jpg », mais pas deux prises différentes de la même scène.</li>
        <li><strong>Photos :</strong> son album Doublons ne couvre que les photos déjà présentes dans la photothèque Photos, pas vos autres dossiers ni vos disques.</li>
      </ul>

      <h2>Avec PixCuller, étape par étape</h2>
      <p><strong>1. Installez PixCuller.</strong> <a href="{mac}">Téléchargez-le gratuitement</a> : macOS 11 ou ultérieur sur Apple Silicon, signé et notarisé par Apple.</p>
      <p><strong>2. Ouvrez le dossier.</strong> Cliquez sur « Ouvrir un dossier », ou glissez un dossier sur la fenêtre. Les sous-dossiers sont inclus, les disques externes aussi.</p>
      <p><strong>3. Regardez les badges.</strong> PixCuller compare le contenu des photos, pas leurs noms : les copies exactes, les rafales et les prises quasi identiques portent le même badge « ≈ N ».</p>
      <p><strong>4. Gardez la meilleure.</strong> Ouvrez un groupe pour comparer jusqu'à six photos côte à côte, gardez la plus nette et marquez les autres.</p>
      <p><strong>5. Supprimez sans risque.</strong> Les fichiers marqués vont dans la Corbeille du Mac, où « Remettre » les restaure si vous changez d'avis.</p>

      <h2>Bon à savoir</h2>
      <ul>
        <li>Les fichiers JPEG, HEIC, PNG, TIFF, WebP et RAW (CR2, CR3, NEF, ARW, RAF, ORF, RW2, DNG) sont pris en charge, ainsi que les vidéos MOV et MP4.</li>
        <li>Les photos sont datées d'après leurs données EXIF : des dossiers copiés restent classés selon le jour de la prise de vue.</li>
        <li>Trier un dossier est gratuit et jamais limité. Tout se passe sur votre Mac : pas de compte, aucun envoi.</li>
        <li>Les photothèques Photos et les paquets d'applications présents dans le dossier sont ignorés : PixCuller ne fouille jamais les fichiers d'une autre application.</li>
      </ul>"""),
dict(slug="find-duplicate-photos-on-windows",
     title="Trouver les photos en double et similaires sur Windows",
     desc="Trouvez copies exactes, rafales et prises quasi identiques dans vos dossiers photos ou sur un disque externe, gardez la meilleure et supprimez le reste.",
     h1="Comment trouver les photos en double et similaires sur Windows 10 ou 11",
     body="""      <p>Sauvegardes de téléphone, cartes mémoire et anciennes copies laissent les mêmes photos dans plusieurs dossiers d'un PC. Certaines sont de vrais doublons, la plupart sont des prises quasi identiques. Voici comment trouver les deux et faire le ménage sans risque.</p>

      <h2>Ce que propose Windows</h2>
      <ul>
        <li><strong>Explorateur de fichiers :</strong> trier par nom, taille ou date aide pour les copies évidentes, mais il ne sait pas que deux fichiers différents montrent la même scène.</li>
        <li><strong>L'app Photos :</strong> pratique pour afficher et importer, mais sans outil pour repérer les prises similaires et choisir la meilleure.</li>
      </ul>

      <h2>Avec PixCuller, étape par étape</h2>
      <p><strong>1. Installez PixCuller.</strong> Obtenez-le gratuitement <a href="{win}">pour Windows 10 ou 11</a> (64 bits), ou depuis le Microsoft Store.</p>
      <p><strong>2. Ouvrez le dossier.</strong> Cliquez sur « Ouvrir un dossier », ou glissez un dossier sur la fenêtre. Les sous-dossiers et les disques externes sont inclus.</p>
      <p><strong>3. Regardez les badges.</strong> PixCuller compare ce que montrent les photos, pas leurs noms de fichiers : les copies exactes, les rafales et les prises quasi identiques portent le même badge « ≈ N ».</p>
      <p><strong>4. Gardez la meilleure.</strong> Comparez jusqu'à six photos côte à côte, gardez la plus nette, marquez les autres.</p>
      <p><strong>5. Supprimez sans risque.</strong> Les fichiers marqués vont dans la Corbeille de Windows : vous pouvez les restaurer.</p>

      <h2>Bon à savoir</h2>
      <ul>
        <li>Les fichiers JPEG, HEIC, PNG, TIFF, WebP et RAW (CR2, CR3, NEF, ARW, RAF, ORF, RW2, DNG) sont pris en charge, ainsi que les vidéos MOV et MP4. Les miniatures HEIC nécessitent l'extension gratuite Extensions d'image HEIF de Microsoft.</li>
        <li>Les photos sont datées d'après leurs données EXIF : des dossiers copiés restent classés selon le jour de la prise de vue.</li>
        <li>Trier un dossier est gratuit et jamais limité. Tout se passe sur votre PC : pas de compte, aucun envoi.</li>
      </ul>"""),
dict(slug="sort-photo-folder-external-drive",
     title="Trier un gros dossier de photos ou un disque dur externe",
     desc="Vieilles sauvegardes, cartes mémoire, disque externe plein de photos : une méthode simple pour trier des milliers de fichiers par voyage et garder le meilleur.",
     h1="Comment trier un gros dossier de photos, ou tout un disque dur externe",
     body="""      <p>Tout le monde en a un : un dossier « Photos à trier », une vieille sauvegarde de téléphone, un disque externe rempli en dix ans. Des milliers de fichiers, aucun ordre, beaucoup de quasi-doublons. Voici une méthode pour en venir à bout en une seule séance.</p>

      <h2>1. Ouvrez tout le dossier d'un coup</h2>
      <p>N'avancez pas dossier par dossier. Ouvrez le dossier racine dans <a href="{pc}">PixCuller</a> (« Ouvrir un dossier », ou glissez-le sur la fenêtre) : les sous-dossiers sont inclus, et chaque photo est datée d'après ses données EXIF plutôt que d'après le jour où elle a été copiée.</p>

      <h2>2. Laissez les voyages apparaître</h2>
      <p>La vue Voyages regroupe les photos par date et par lieu et indique la place prise par chaque groupe. Dix ans de fichiers deviennent une liste de voyages et d'événements, et vous commencez par les plus lourds.</p>

      <h2>3. Réduisez les quasi-doublons</h2>
      <p>Les rafales, les prises répétées et les copies d'une même photo portent un badge « ≈ N ». Comparez-en jusqu'à six côte à côte, gardez la meilleure, marquez les autres. Cette étape seule supprime souvent une grande partie des fichiers.</p>

      <h2>4. Marquez les restes évidents</h2>
      <p>Captures d'écran, photos floues, vidéos accidentelles : marquez-les au passage. Rien n'est supprimé tant que vous n'avez pas confirmé.</p>

      <h2>5. Supprimez sans risque</h2>
      <p>Les fichiers confirmés vont dans la Corbeille sur Mac ou dans la Corbeille de Windows, une erreur peut donc être rattrapée. Videz-la quand vous êtes sûr de vous.</p>

      <h2>Bon à savoir</h2>
      <ul>
        <li>Les fichiers RAW d'appareils photo (CR2, CR3, NEF, ARW, RAF, ORF, RW2, DNG) sont pris en charge, comme les JPEG, HEIC, PNG et les vidéos.</li>
        <li>Trier des dossiers est gratuit et jamais limité, sur Mac (<a href="{mac}">télécharger</a>) comme sous Windows (<a href="{win}">télécharger</a>).</li>
        <li>Vos originaux ne sont jamais modifiés : la seule modification de PixCuller est la suppression que vous confirmez.</li>
      </ul>"""),
dict(slug="sort-android-photos-on-mac",
     title="Comment trier les photos de son Android sur Mac",
     desc="Un Mac a longtemps eu du mal à lire les Android en USB. Comment trier des milliers de photos Android sur Mac avec macOS 27 et supprimer le superflu.",
     h1="Comment trier les photos de son téléphone Android sur Mac",
     body="""      <p>Branchez un téléphone Android à un Mac et, la plupart du temps, il ne se passe rien d'utile : macOS n'a jamais lu les téléphones Android en USB comme le fait Windows. Pourtant, un Mac est le meilleur endroit pour trier une grosse pellicule, avec un grand écran, une souris et la comparaison côte à côte. Voici ce qui marche.</p>

      <h2>Ce que macOS sait faire seul</h2>
      <ul>
        <li><strong>Transfert d'images :</strong> peut voir le téléphone si vous choisissez « Transférer des photos » (PTP) dans la notification USB, mais seulement comme une simple liste de fichiers, sans regroupement ni comparaison des photos similaires.</li>
        <li><strong>Transfert de fichiers Android de Google :</strong> n'est plus maintenu, et il ne fait de toute façon que copier des fichiers.</li>
        <li><strong>Envoi dans le cloud :</strong> envoyer tout sur un service en ligne juste pour trier est lent, consomme votre forfait et place vos photos sur le serveur d'un tiers.</li>
      </ul>

      <h2>Avec PixCuller, en USB, étape par étape</h2>
      <p><strong>1. Installez PixCuller.</strong> <a href="{mac}">Téléchargez PixCuller pour Mac</a> gratuitement. La lecture d'un téléphone Android nécessite macOS 27 ou ultérieur ; sur un Mac plus ancien, l'app affiche un message qui l'indique. Rien n'est à installer sur le téléphone.</p>
      <p><strong>2. Branchez le téléphone.</strong> Connectez-le avec un câble USB, déverrouillez-le et choisissez « Transfert de fichiers » dans sa notification USB.</p>
      <p><strong>3. Connectez-le.</strong> Dans PixCuller, cliquez sur « Téléphone Android », puis sur « Connecter en USB ».</p>
      <p><strong>4. Triez voyage par voyage.</strong> La vue Voyages regroupe la pellicule par date et par lieu, avec la place prise par chaque voyage. Les photos similaires portent un badge : comparez-en jusqu'à six côte à côte, gardez la meilleure, marquez les autres.</p>
      <p><strong>5. Supprimez sans risque.</strong> Cliquez sur Supprimer et confirmez. PixCuller supprime les photos directement par le câble : la suppression est immédiate et définitive sur le téléphone (les photos ne passent pas par sa corbeille), mais PixCuller garde par défaut pendant 30 jours une copie de chaque élément supprimé sur votre Mac, dans un dossier « PixCuller Trash » du dossier Images, une erreur est donc réversible.</p>

      <h2>Bon à savoir</h2>
      <ul>
        <li>Tout reste sur votre Mac et votre téléphone : pas de compte, pas de cloud, aucun envoi.</li>
        <li>PixCuller ne modifie jamais vos originaux et ne supprime que ce que vous confirmez.</li>
        <li>PixCuller est gratuit, sans abonnement.</li>
        <li>Vous avez aussi un iPhone ? Il se connecte lui aussi au Mac avec un câble USB.</li>
      </ul>"""),
dict(slug="sort-android-photos-on-pc",
     title="Comment trier les photos de son Android sur PC Windows",
     desc="Triez des milliers de photos Android sur Windows 10 ou 11 : ce que montrent l'Explorateur et l'app Photos, et une méthode plus rapide pour trier et supprimer.",
     h1="Comment trier les photos de son téléphone Android sur PC Windows",
     body="""      <p>Windows lit bien les téléphones Android, mais lire n'est pas trier. Avec des milliers de photos, les outils intégrés vous laissent devant une longue liste de noms de fichiers. Voici ce qu'ils font, et une méthode plus rapide pour vider le téléphone depuis votre PC.</p>

      <h2>Avec les outils intégrés à Windows</h2>
      <ul>
        <li><strong>Explorateur de fichiers :</strong> une fois « Transfert de fichiers » choisi sur le téléphone, son dossier DCIM apparaît sous forme de fichiers. Vous pouvez y supprimer, mais sans regroupement ni comparaison des photos similaires.</li>
        <li><strong>L'app Photos :</strong> importe une copie sur le PC. Une bonne sauvegarde, mais elle ne vous dit pas quoi retirer du téléphone.</li>
        <li><strong>Mobile connecté :</strong> n'affiche que les photos récentes, une par une.</li>
      </ul>

      <h2>Avec PixCuller, étape par étape</h2>
      <p><strong>1. Installez PixCuller.</strong> Obtenez-le gratuitement <a href="{win}">pour Windows 10 ou 11</a>, ou depuis le Microsoft Store. Rien n'est à installer sur le téléphone.</p>
      <p><strong>2. Connectez en USB.</strong> Branchez le téléphone, déverrouillez-le et choisissez « Transfert de fichiers » dans sa notification USB. Puis cliquez sur « Téléphone Android » dans PixCuller, et sur « Connecter en USB ».</p>
      <p><strong>3. Triez voyage par voyage.</strong> La vue Voyages regroupe la pellicule par date et par lieu et indique la place prise par chaque voyage. Commencez par le plus lourd.</p>
      <p><strong>4. Comparez et marquez.</strong> Les photos similaires portent un badge : ouvrez-en jusqu'à six côte à côte, gardez la meilleure et marquez les autres, ainsi que les captures d'écran et les grosses vidéos.</p>
      <p><strong>5. Supprimez sans risque.</strong> Confirmez, et PixCuller supprime les photos directement par le câble. La suppression est immédiate et définitive sur le téléphone (pas de corbeille), mais PixCuller garde par défaut pendant 30 jours une copie de chaque élément supprimé sur votre PC, dans un dossier « PixCuller Trash » du dossier Images.</p>

      <h2>Bon à savoir</h2>
      <ul>
        <li>Tout reste sur votre PC et votre téléphone : pas de compte, pas de cloud, aucun envoi.</li>
        <li>Supprimer depuis l'Explorateur est définitif, sans copie conservée ; PixCuller garde par défaut la copie de 30 jours sur le PC.</li>
        <li>PixCuller est gratuit, et trier un dossier sur le PC fonctionne de la même façon.</li>
      </ul>"""),
dict(slug="free-up-android-from-mac-or-pc",
     title="Libérer de l'espace sur Android depuis un Mac ou un PC",
     desc="Connectez votre Android en USB, triez vos photos sur grand écran et supprimez le superflu, sans payer Google One et sans rien envoyer en ligne.",
     h1="Comment libérer de l'espace sur votre téléphone Android depuis un Mac ou un PC",
     body="""      <p>Quand un téléphone Android n'a plus de place, ce sont presque toujours les photos et les vidéos. Les trier sur un petit écran est lent. Depuis un ordinateur, vous voyez plus de choses à la fois et décidez plus vite, sans acheter de stockage cloud supplémentaire.</p>

      <h2>Pourquoi un ordinateur aide</h2>
      <p>Un grand écran affiche des dizaines de photos à la fois, une souris en sélectionne des centaines en quelques secondes, et comparer des prises quasi identiques côte à côte est bien plus facile que de faire des allers-retours. Une pellicule qui demanderait une soirée sur le téléphone se traite en quelques minutes.</p>

      <h2>La méthode</h2>
      <p><strong>1. Connectez le téléphone.</strong> Installez <a href="{pc}">PixCuller</a> sur un PC Windows 10/11 ou sur un Mac avec macOS 27 ou ultérieur ; rien n'est à installer sur le téléphone. Branchez le téléphone avec un câble USB, déverrouillez-le, choisissez « Transfert de fichiers » dans sa notification USB, puis cliquez sur « Téléphone Android » et « Connecter en USB ».</p>
      <p><strong>2. Commencez par ce qui pèse le plus.</strong> La vue Voyages indique la place prise par chaque voyage ; les longues vidéos et les anciennes vacances libèrent généralement le plus.</p>
      <p><strong>3. Retirez les quasi-doublons.</strong> Les rafales et les prises répétées d'une même scène portent un badge. Comparez-les côte à côte, gardez la meilleure, marquez les autres.</p>
      <p><strong>4. Faites le ménage dans les captures d'écran et les photos floues.</strong> Elles méritent rarement de rester et se marquent vite d'un seul bloc.</p>
      <p><strong>5. Confirmez la suppression.</strong> PixCuller supprime les photos directement par le câble. La suppression est immédiate et définitive sur le téléphone (pas de corbeille à vider, l'espace revient tout de suite), et PixCuller garde par défaut pendant 30 jours une copie de chaque élément supprimé sur votre ordinateur, dans un dossier « PixCuller Trash » du dossier Images.</p>

      <h2>Ai-je besoin de Google One ?</h2>
      <p>Le stockage cloud est une bonne sauvegarde, mais il garde tout, doublons compris. Faire le ménage d'abord, c'est avoir besoin de moins de stockage, sur le téléphone comme dans le cloud.</p>

      <h2>Bon à savoir</h2>
      <ul>
        <li>Pas de compte et aucun envoi : le téléphone et l'ordinateur communiquent par le câble USB.</li>
        <li>PixCuller est gratuit, sans abonnement.</li>
      </ul>"""),
],
}
