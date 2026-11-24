# -*- coding: utf-8 -*-
# Spanish translation of the FAQ and blog of the PixCuller site. Tokens in answers/articles: {pc} {mac} {win} (see link_tokens).

BLOG_UI = dict(
    nav="Blog", privacy="Privacidad", more="Sigue leyendo",
    cta_mac="💻 Descarga PixCuller para Mac", cta_win="🪟 Descarga PixCuller para Windows",
    twin_android="¿Usas un móvil Android? Lee la guía para Android:",
    twin_iphone="¿Usas un iPhone? Lee la guía para iPhone:",
    index={
        "pixculler": dict(
            title="Blog de PixCuller: ordena tus fotos en Mac o PC",
            desc="Guías para ordenar miles de fotos más rápido en una pantalla grande, comparar fotos parecidas y liberar un iPhone o un móvil Android desde un Mac o un PC.",
            h1="Guías para ordenar tus fotos en el ordenador",
            intro="Por qué una pantalla grande cambia la rapidez con la que ordenas fotos, y cómo aprovecharla para liberar espacio en tu iPhone o móvil Android."),
    },
)

FAQ_PIXCULLER = dict(
    title="FAQ de PixCuller: ordena y borra fotos desde un Mac o un PC",
    desc="Cómo ordenar miles de fotos en el ordenador, comparar fotos parecidas, liberar un iPhone o un móvil Android desde un Mac o PC: respuestas sobre PixCuller.",
    nav_home="PixCuller",
    h1="Preguntas y respuestas",
    intro="Cómo ordenar tus fotos más rápido desde un ordenador, liberar espacio en tu iPhone o móvil Android desde un Mac o PC, y qué hace (y qué nunca hace) PixCuller con tus fotos.",
    qa=[
        ("¿Cómo sabe PixCuller que una foto ya está guardada en mi ordenador?",
         "Añade las carpetas donde guardas tus fotos (un disco, una memoria USB) en «Carpetas de copia». PixCuller busca entonces una copia idéntica de cada foto en ellas: mismo contenido, no solo mismo nombre. Las fotos encontradas se enmarcan en verde en la cuadrícula y el menú ofrece dos filtros, «Guardadas» y «No guardadas». Las carpetas se recuerdan y la comprobación es rápida desde la segunda vez. Elige las carpetas donde de verdad ordenas tus fotos en lugar de un disco entero: es mucho más rápido. Una Live Photo cuenta como guardada si su vídeo también está (una opción permite no comprobarlo). Nada sale de tu ordenador."),
        ("¿Puedo buscar mis fotos por lugar o por fecha?",
         "Sí. Escribe un lugar, un país, una fecha o un nombre de archivo en la barra de búsqueda: «Milán», «Italia», «agosto 2026», «11.02.2025». El lugar viene del GPS de las fotos y se averigua sin conexión, así que no se envía nada. Un botón de calendario filtra por periodo y la cuadrícula puede mostrar una sección por día o quedarse densa."),
        ('¿Cómo ordeno las fotos del iPhone en el ordenador, Mac o PC?',
         "Conecta el iPhone al ordenador con un cable USB, desbloquéalo y toca Confiar, y abre <a href=\"{pc}\">PixCuller</a>: agrupa el carrete por viaje, compara las fotos parecidas lado a lado y marca cientos de fotos en pocos clics. Guías paso a paso: <a href=\"{post:sort-iphone-photos-on-mac}\">en el Mac</a> y <a href=\"{post:sort-iphone-photos-on-pc}\">en un PC con Windows</a>."),
        ("¿Por qué ordenar las fotos en el ordenador en lugar de en el iPhone?",
         "Una pantalla grande muestra más fotos a la vez, un ratón y un teclado seleccionan cientos en segundos, y comparar tomas lado a lado es más fácil que ir pasando de una a otra. Ordenar un carrete de miles de fotos son varias sesiones en el móvil y una sesión mucho más corta en un Mac o un PC."),
        ("¿Qué es PixCuller?",
         "PixCuller es una app de escritorio gratuita para Mac y Windows que agrupa tus fotos por viaje, compara tomas parecidas lado a lado y borra en bloque lo que no merece la pena conservar. Lee el carrete de un iPhone o de un móvil Android por un cable USB, o cualquier carpeta de fotos de tu ordenador, y funciona 100 % en el dispositivo."),
        ("¿Cómo ordeno miles de fotos rápidamente?",
         "Abre la vista Viajes: tu biblioteca aparece agrupada por viaje con el espacio que ocupa cada uno, así que empiezas por el más pesado. Dentro de un viaje, marca fotos en bloque, compara las parecidas lado a lado y conserva la mejor toma de cada grupo. Los filtros (viajes de un solo día, lugares excluidos como casa o trabajo, tamaño) te ayudan a acotar."),
        ("¿Cómo libero espacio en el iPhone desde un Mac o un PC?",
         "Conecta tu iPhone por USB, abre PixCuller, marca los viajes y las fotos que ya no necesitas y confirma. PixCuller las borra directamente por el cable USB, en Windows 10/11 o en un Mac con macOS 27 o posterior, siempre que Fotos en iCloud esté desactivado. El borrado es inmediato y definitivo en el iPhone, con una copia que se guarda por defecto 30 días en tu ordenador. Con macOS 26 o anterior, PixCuller sigue mostrando y ordenando las fotos del iPhone, pero las borras en la app Fotos del iPhone."),
        ("¿Puedo borrar fotos del iPhone directamente desde el ordenador?",
         "Sí. Con un iPhone, PixCuller borra las fotos directamente por el cable USB, desde un Mac o un PC con Windows, sin nada que comprar. Tres condiciones: Fotos en iCloud está desactivado en el iPhone (cuando está activado, Apple no permite este borrado), un Mac tiene macOS 27 o posterior (cualquier PC con Windows 10/11 funciona) y aceptas que el borrado es inmediato y definitivo en el iPhone: las fotos no pasan por « Eliminados recientemente ». Por defecto, PixCuller guarda durante 30 días una copia de cada elemento borrado en tu ordenador, en una carpeta « PixCuller Trash » dentro de Imágenes (una casilla al confirmar), de modo que un error se puede deshacer importando de nuevo el archivo. Las Live Photos y las fotos editadas se gestionan correctamente (todas sus versiones se borran juntas) y PixCuller muestra la versión editada de una foto editada. Si Fotos en iCloud está activado, desactívalo (Ajustes > [tu nombre] > iCloud > Fotos) o borra en la app Fotos del iPhone. Con macOS 26 o anterior, PixCuller puede mostrar y ordenar las fotos del iPhone, pero no borrarlas: un aviso en la app lo indica, y borras en la app Fotos del iPhone."),
        ("¿Borrar desde PixCuller es permanente?",
         "En un móvil, sí. Con un iPhone o un móvil Android, el borrado por el cable USB es inmediato y definitivo en el móvil: las fotos no pasan por « Eliminados recientemente » ni por la papelera del móvil. Por defecto, PixCuller guarda durante 30 días una copia de cada elemento borrado en tu ordenador, en una carpeta « PixCuller Trash » dentro de Imágenes (una casilla al confirmar), para poder importarlo de nuevo. En una carpeta de tu ordenador, los archivos van a la Papelera."),
        ("¿Cómo conecto mi iPhone a PixCuller?",
         "Usa un cable USB, desbloquea el iPhone y toca « Confiar » cuando te lo pida. En un Mac no hace falta nada más. En Windows, instala la app gratuita Apple Devices desde Microsoft Store, que incluye el controlador que permite a PixCuller leer el iPhone."),
        ("¿Puedo ordenar las fotos de un móvil Android en mi Mac o PC?",
         "Sí, por un cable USB: en cualquier PC con Windows 10/11 y en un Mac con macOS 27 o posterior. Tienes la misma vista Viajes, la misma comparación lado a lado y el mismo borrado en bloque que con un iPhone. No hace falta instalar nada en el móvil."),
        ("¿Cómo conecto mi móvil Android?",
         "Conecta el móvil al ordenador con un cable USB, desbloquéalo y elige « Transferencia de archivos » en su notificación USB. En PixCuller, haz clic en « Teléfono Android » y después en « Conectar por USB ». Guías: <a href=\"{post:sort-android-photos-on-mac}\">en el Mac</a> y <a href=\"{post:sort-android-photos-on-pc}\">en un PC con Windows</a>."),
        ("¿Por qué mi Mac no ve mi móvil Android?",
         "PixCuller lee los móviles Android por USB con macOS 27 o posterior; en un Mac más antiguo, la app muestra un mensaje que lo indica. Con macOS 27 o posterior, comprueba que el móvil está desbloqueado y que has elegido « Transferencia de archivos » en su notificación USB. En Windows 10/11, la conexión USB funciona con cualquier versión."),
        ("¿Tengo que instalar algo en el móvil?",
         "No. PixCuller funciona por sí solo, sin nada que instalar en el móvil y sin ninguna otra app. Un iPhone o un móvil Android solo necesita un cable USB. En Windows, para leer un iPhone también hace falta en el PC la app gratuita Apple Devices de Microsoft Store."),
        ("¿Qué pasa con las fotos que borro en un móvil Android?",
         "PixCuller las borra directamente por el cable USB, después de que confirmes. El borrado es inmediato y definitivo: las fotos no pasan por la papelera del móvil. Por defecto, PixCuller guarda durante 30 días una copia de cada elemento borrado en tu ordenador, en una carpeta « PixCuller Trash » dentro de Imágenes (una casilla al confirmar), de modo que un error se puede deshacer."),
        ("¿Cómo busco fotos duplicadas en una carpeta de mi Mac o PC?",
         "Abre la carpeta en PixCuller (« Abrir carpeta », o arrástrala a la ventana). Recorre las subcarpetas, compara lo que muestran las fotos y pone la misma insignia «≈ N» a las copias exactas, las ráfagas y las tomas casi idénticas. Conserva la mejor de cada grupo y manda el resto a la Papelera (Mac) o a la Papelera de reciclaje (Windows). Guías: <a href=\"{post:find-duplicate-photos-on-mac}\">en el Mac</a> y <a href=\"{post:find-duplicate-photos-on-windows}\">en Windows</a>."),
        ("¿Puedo usar PixCuller con fotos guardadas en mi ordenador, no en un iPhone?",
         "Sí. Abre cualquier carpeta: PixCuller encuentra las fotos parecidas, muestra las insignias en ellas y te permite comparar y borrar."),
        ("¿Cómo encuentra PixCuller las fotos parecidas?",
         "Compara el contenido de tus fotos, no el nombre de los archivos, así que las ráfagas, las tomas casi idénticas y la misma escena fotografiada varias veces acaban en el mismo grupo. Puedes comparar hasta 6 fotos lado a lado y quedarte con la más nítida y mejor encuadrada."),
        ("¿Cómo comparo fotos parecidas lado a lado?",
         "Selecciona un grupo de fotos parecidas y abre la comparación: se muestran hasta 6 fotos del mismo tamaño para que puedas juzgar el enfoque, las expresiones y el encuadre. Conserva la mejor y marca el resto."),
        ("¿Funciona PixCuller en Windows?",
         "Sí: Windows 10 y 11 (64 bits). Para leer un iPhone hace falta la app gratuita Apple Devices de Microsoft Store. La app todavía no está firmada digitalmente, así que Windows SmartScreen puede mostrar una advertencia la primera vez que la abras: elige « Más información » y luego « Ejecutar de todas formas »."),
        ("¿Qué Mac admite PixCuller?",
         "Mac con Apple Silicon y macOS 11 o posterior. La app está firmada y notarizada por Apple, así que se abre sin ninguna advertencia de seguridad."),
        ("¿PixCuller es gratis? ¿Hay suscripción?",
         "Sí, PixCuller es gratis, sin suscripción y sin compras dentro de la app. Explorar, comparar, ordenar y borrar es gratis, tanto en un móvil como en una carpeta de tu ordenador."),
        ("¿PixCuller envía mis fotos a un servidor o a la nube?",
         "No. PixCuller funciona 100 % en el dispositivo: sin cuenta, sin nube, y ninguna foto, vídeo ni ubicación se envía a ningún sitio. El reconocimiento de lugares y la detección de fotos parecidas se ejecutan en tu ordenador. Solo se pueden enviar estadísticas de uso anónimas y desactivables."),
        ("¿PixCuller cambiará o modificará mis fotos originales?",
         "No. PixCuller solo lee tus fotos para mostrarlas y compararlas. El único cambio que hace es el borrado que tú confirmas."),
        ("¿Cómo oculto mi casa y mi lugar de trabajo de la vista de viajes?",
         "Añádelos como lugares excluidos: así el día a día deja de aparecer como un viaje y tus viajes de verdad destacan."),
        ("¿Puedo hacer limpieza tras las vacaciones desde el ordenador?",
         "Sí, es el uso más habitual. Después de un viaje, conecta el móvil, abre ese viaje en PixCuller, compara las tomas parecidas, conserva la mejor de cada una y borra el resto."),
        ("¿Puedo usar PixCuller para preparar un álbum de fotos o una copia de seguridad?",
         "PixCuller te ayuda a decidir qué merece la pena conservar: ordena el viaje, elimina los duplicados y las tomas casi idénticas, y después haz una copia de seguridad o comparte lo que quede."),
    ],
    footer_copy="© 2026 PixCuller. Desarrollado por Jeffrey Brignoli.",
    footer_privacy="Privacidad", footer_kofi="Ko-fi",
)

BLOG = {
"pixculler": [
dict(slug="sort-iphone-photos-on-mac",
     title="Cómo ordenar las fotos del iPhone en el Mac",
     desc="Ordena miles de fotos del iPhone en tu Mac: qué hacen Fotos y Captura de Imagen, y una forma más rápida de agrupar, comparar y borrar.",
     h1="Cómo ordenar las fotos del iPhone en el Mac",
     body="""      <p>Ordenar un carrete lleno en el iPhone son horas de toques. En un Mac ves muchas más fotos a la vez, seleccionas con el ratón y comparas en una pantalla grande. Así se hace, con las herramientas de macOS y con una app dedicada.</p>

      <h2>Con las herramientas de macOS</h2>
      <ul>
        <li><strong>Fotos:</strong> importa una copia de las fotos del iPhone al Mac. Útil como copia de seguridad, pero no te dice qué borrar en el iPhone.</li>
        <li><strong>Captura de Imagen:</strong> muestra las fotos del iPhone como simples archivos, sin agruparlas por viaje ni comparar las fotos parecidas.</li>
      </ul>
      <p>Las dos funcionan, pero con miles de fotos sigues desplazándote por una única lista larga.</p>

      <h2>Con PixCuller, paso a paso</h2>
      <p><strong>1. Instala PixCuller.</strong> <a href="{mac}">Descárgalo gratis</a>: macOS 11 o posterior en Apple Silicon, firmado y notarizado por Apple.</p>
      <p><strong>2. Conecta el iPhone.</strong> Conéctalo con un cable USB, desbloquéalo y toca Confiar.</p>
      <p><strong>3. Ordena viaje a viaje.</strong> La vista Viajes agrupa el carrete por fecha y lugar y muestra el espacio que ocupa cada viaje. Empieza por el más pesado.</p>
      <p><strong>4. Compara y marca.</strong> Las fotos parecidas llevan una insignia: abre hasta seis lado a lado, quédate con la mejor y marca el resto, junto con capturas de pantalla y vídeos grandes que no necesites.</p>
      <p><strong>5. Borra con seguridad.</strong> Con Fotos en iCloud desactivado y macOS 27 o posterior, PixCuller borra las fotos directamente por el cable USB. El borrado es inmediato y definitivo en el iPhone: las fotos no pasan por « Eliminados recientemente ». Por defecto, PixCuller guarda durante 30 días una copia de cada elemento borrado en tu Mac, en una carpeta « PixCuller Trash » dentro de Imágenes, de modo que un error se puede deshacer importando de nuevo el archivo. Si Fotos en iCloud está activado, desactívalo (Ajustes > [tu nombre] > iCloud > Fotos) o borra en la app Fotos del iPhone.</p>

      <h2>Conviene saber</h2>
      <ul>
        <li>Todo se queda en tu Mac y tu iPhone: sin cuenta, sin nube, sin envíos.</li>
        <li>PixCuller nunca modifica tus originales y solo borra lo que confirmas.</li>
        <li>Con macOS 26 o anterior, PixCuller muestra y ordena las fotos del iPhone, pero no puede borrarlas: un aviso en la app lo indica, y borras en la app Fotos del iPhone.</li>
        <li>PixCuller es gratis, y ordenar una carpeta de fotos en el Mac funciona igual.</li>
      </ul>"""),
dict(slug="sort-iphone-photos-on-pc",
     title="Cómo ordenar las fotos del iPhone en un PC con Windows",
     desc="Ordena miles de fotos del iPhone en Windows 10 u 11: qué muestran la app Fotos y el Explorador, y una forma más rápida de ordenar y borrar.",
     h1="Cómo ordenar las fotos del iPhone en un PC con Windows",
     body="""      <p>¿iPhone pero ordenador con Windows? Puedes ordenar tus fotos en una pantalla grande en lugar del teléfono. Esto es lo que Windows hace por sí solo, y un método más rápido.</p>

      <h2>Con las herramientas de Windows</h2>
      <ul>
        <li><strong>App Fotos:</strong> importa una copia de las fotos del iPhone al PC. Sirve como copia de seguridad, pero no te ayuda a elegir qué borrar.</li>
        <li><strong>Explorador de archivos:</strong> muestra las fotos del iPhone en carpetas como 100APPLE, con nombres como IMG_0001, sin viajes ni comparación de fotos parecidas.</li>
      </ul>

      <h2>Con PixCuller, paso a paso</h2>
      <p><strong>1. Instala Apple Devices.</strong> Instala la app gratuita Apple Devices de Microsoft Store: Windows la necesita para leer un iPhone.</p>
      <p><strong>2. Instala PixCuller.</strong> Desde Microsoft Store o <a href="{win}">descargándolo gratis</a> (Windows 10/11, 64 bits). La descarga aún no está firmada, así que SmartScreen puede avisar en el primer inicio.</p>
      <p><strong>3. Conecta el iPhone.</strong> Conéctalo con un cable USB, desbloquéalo y toca Confiar.</p>
      <p><strong>4. Ordena viaje a viaje.</strong> La vista Viajes agrupa el carrete por fecha y lugar y muestra el espacio que ocupa cada viaje. Empieza por el más pesado.</p>
      <p><strong>5. Compara, marca, borra.</strong> Las fotos parecidas llevan una insignia: compara hasta seis lado a lado, quédate con la mejor y marca el resto. Con Fotos en iCloud desactivado, PixCuller las borra directamente por el cable USB. El borrado es definitivo en el iPhone (sin « Eliminados recientemente »), pero por defecto PixCuller guarda durante 30 días una copia de cada elemento borrado en tu PC, en una carpeta « PixCuller Trash » dentro de Imágenes. Si Fotos en iCloud está activado, desactívalo (Ajustes > [tu nombre] > iCloud > Fotos) o borra en la app Fotos del iPhone.</p>

      <h2>Conviene saber</h2>
      <ul>
        <li>Todo se queda en tu PC y tu iPhone: sin cuenta, sin nube, sin envíos.</li>
        <li>PixCuller nunca modifica tus originales y solo borra lo que confirmas.</li>
        <li>Explorar y ordenar es gratis, y ordenar una carpeta de fotos que ya está en el PC nunca tiene límite.</li>
      </ul>"""),
dict(slug="sort-photos-on-computer",
     title="Cómo ordenar miles de fotos más rápido en un Mac o PC",
     desc="Por qué ordenar fotos en una pantalla grande es mucho más rápido que en el móvil, y un método sencillo para repasar miles de fotos en una sola sesión.",
     h1="Cómo ordenar miles de fotos más rápido en un Mac o un PC",
     body="""      <p>Si tu carrete tiene diez mil fotos, ordenarlas en la pantalla del móvil es un proyecto que nunca acabarás. En un ordenador puede ser cosa de una tarde. Aquí te explico por qué y un método que funciona.</p>

      <h2>Por qué un ordenador es más rápido</h2>
      <ul>
        <li><strong>Más en pantalla:</strong> decenas de fotos a la vez en lugar de un puñado.</li>
        <li><strong>Selección precisa:</strong> un ratón y un teclado seleccionan cientos de fotos en segundos.</li>
        <li><strong>Comparación de verdad:</strong> fotos parecidas una junto a otra, a un tamaño en el que se ven el enfoque y las expresiones.</li>
      </ul>

      <h2>Un método que funciona</h2>
      <p><strong>1. Agrupa por viaje.</strong> Ordenar por fecha y lugar divide la biblioteca en partes manejables. Empieza por el viaje que más espacio ocupa.</p>
      <p><strong>2. Elimina las casi copias.</strong> Compara cada grupo de tomas parecidas, conserva la mejor y marca el resto.</p>
      <p><strong>3. Filtra el ruido.</strong> Oculta los lugares que no te interesan (casa, trabajo) para que los viajes de verdad destaquen, y filtra por tamaño para encontrar los archivos pesados.</p>
      <p><strong>4. Borra de una vez.</strong> Marca cientos de fotos y confirma una sola vez.</p>

      <h2>PixCuller hace justo esto</h2>
      <p><a href="{pc}">PixCuller</a> es una app de escritorio gratuita para Mac y Windows. Su vista Viajes agrupa la biblioteca por viaje y muestra el espacio que ocupa cada uno, las fotos parecidas llevan una insignia y puedes comparar hasta seis lado a lado. Lee un iPhone o un móvil Android por un cable USB, o cualquier carpeta de tu ordenador, funciona 100 % en el dispositivo y nunca modifica tus originales.</p>
      <p>En un móvil, PixCuller borra directamente por el cable USB, en Windows 10/11 o en un Mac con macOS 27 o posterior (con Fotos en iCloud desactivado en un iPhone). El borrado es definitivo en el móvil, con una copia que se guarda por defecto 30 días en tu ordenador. En una carpeta, los archivos van a la Papelera. Ordenar nunca tiene límite.</p>

      <h2>Consejos para una sesión larga</h2>
      <ul>
        <li>Trabaja viaje por viaje, sin recorrer toda la biblioteca.</li>
        <li>Decide rápido: si dos tomas se parecen, conserva una.</li>
        <li>Borra al final de cada viaje, para que se note el avance.</li>
      </ul>"""),
dict(slug="free-up-iphone-from-mac-or-pc",
     title="Cómo liberar espacio en el iPhone desde un Mac o PC",
     desc="Conecta tu iPhone, ordena fotos en una pantalla grande y borra lo que no necesitas, sin iCloud y sin enviar nada a internet.",
     h1="Cómo liberar espacio en el iPhone desde un Mac o un PC con Windows",
     body="""      <p>Limpiar un iPhone lleno desde el propio iPhone es tedioso. Desde un ordenador ves muchas más fotos a la vez y decides más rápido. Este es el proceso completo.</p>

      <h2>Qué necesitas</h2>
      <ul>
        <li>Un Mac (Apple Silicon, macOS 11 o posterior) o un PC con Windows 10/11.</li>
        <li>Un cable USB. En Windows, además, la app gratuita Apple Devices de Microsoft Store.</li>
        <li><a href="{pc}">PixCuller</a>, gratuito para ambos sistemas.</li>
        <li>Para borrar desde el iPhone: Fotos en iCloud desactivado y, en un Mac, macOS 27 o posterior. Con macOS 26 o anterior, PixCuller sigue mostrando y ordenando las fotos, y las borras en la app Fotos del iPhone.</li>
      </ul>

      <h2>Paso a paso</h2>
      <p><strong>1. Conecta y confía.</strong> Conecta el iPhone, desbloquéalo y toca Confiar.</p>
      <p><strong>2. Abre la vista Viajes.</strong> PixCuller agrupa tu carrete por viaje y muestra el espacio que ocupa cada uno.</p>
      <p><strong>3. Ordena los viajes más pesados.</strong> Compara las tomas parecidas, conserva la mejor y marca el resto, además de las capturas de pantalla y los vídeos grandes que no necesites.</p>
      <p><strong>4. Confirma el borrado.</strong> Con Fotos en iCloud desactivado (y macOS 27 o posterior en un Mac), PixCuller borra las fotos directamente por el cable USB, también en Windows. El borrado es inmediato y definitivo en el iPhone, pero por defecto PixCuller guarda durante 30 días una copia de cada elemento borrado en tu ordenador, en una carpeta « PixCuller Trash » dentro de Imágenes.</p>
      <p><strong>5. Si Fotos en iCloud está activado.</strong> PixCuller rechaza el borrado: desactiva Fotos en iCloud (Ajustes > [tu nombre] > iCloud > Fotos) o borra en la app Fotos del iPhone.</p>

      <h2>¿Es seguro?</h2>
      <p>Sí: tus fotos se quedan en tus dispositivos, sin cuenta, sin nube y sin subir nada. PixCuller solo lee tus fotos hasta que tú confirmas. Un borrado es definitivo en el iPhone, pero por defecto queda una copia 30 días en tu ordenador.</p>


      <h2>En Windows</h2>
      <p>Los pasos son los mismos en Windows 10 y 11. Instala primero la app gratuita Apple Devices de Microsoft Store, para que PixCuller pueda leer el iPhone. La app todavía no está firmada digitalmente, así que SmartScreen puede mostrar una advertencia la primera vez que la abras.</p>"""),
dict(slug="compare-similar-photos-keep-the-best",
     title="Cómo comparar fotos parecidas y quedarte con la mejor",
     desc="Una rutina sencilla para elegir la mejor toma entre fotos casi idénticas: en qué fijarte y cómo hacerlo rápido en una pantalla grande.",
     h1="Cómo comparar fotos parecidas y quedarte con la mejor",
     body="""      <p>Hiciste seis fotos del mismo momento y todas se ven bien. Elegir la mejor lleva segundos con el método adecuado, y varios minutos con el equivocado.</p>

      <h2>Qué revisar, en este orden</h2>
      <ol>
        <li><strong>Enfoque.</strong> Haz zoom en los ojos o en el sujeto principal. Un sujeto borroso queda descartado.</li>
        <li><strong>Expresiones.</strong> Ojos abiertos, sonrisas naturales, nadie parpadeando.</li>
        <li><strong>Encuadre.</strong> Nada cortado, un fondo limpio, el horizonte recto.</li>
        <li><strong>Momento.</strong> Si dos tomas están igual, quédate con la que transmita más vida.</li>
      </ol>

      <h2>Por qué importa verlas lado a lado</h2>
      <p>Pasar de una foto a otra hace difícil ver las pequeñas diferencias. Verlas una junto a otra, al mismo tamaño, hace evidente cuál es la más nítida o la mejor encuadrada. La pantalla de un ordenador muestra hasta seis a la vez, mientras que el móvil muestra una.</p>

      <h2>Una rutina más rápida</h2>
      <p>Agrupa primero las fotos parecidas, para no tener que buscarlas en la biblioteca. En cada grupo, abre la comparación, elige una y marca las demás. Decides en segundos, no en minutos.</p>

      <h2>Hazlo con PixCuller</h2>
      <p><a href="{pc}">PixCuller</a> muestra una insignia en las fotos parecidas, abre hasta seis lado a lado y te deja marcar el resto con un clic. Funciona con un iPhone conectado por USB o con cualquier carpeta de tu Mac o PC, sin conexión, y nunca modifica tus originales.</p>

      <h2>Conserva sin arrepentirte</h2>
      <p>Cuando dudes, quédate con dos. Cuando PixCuller borra en un móvil, guarda por defecto una copia en tu ordenador durante 30 días; en una carpeta, los archivos van a la Papelera. En ambos casos aún puedes cambiar de opinión.</p>"""),
dict(slug="find-duplicate-photos-on-mac",
     title="Cómo buscar fotos duplicadas y parecidas en un Mac",
     desc="Encuentra copias exactas, ráfagas y tomas casi idénticas en las carpetas de tu Mac o en un disco externo, conserva la mejor y manda el resto a la Papelera.",
     h1="Cómo buscar fotos duplicadas y parecidas en un Mac",
     body="""      <p>Años de importaciones, tarjetas de cámara y copias de seguridad dejan las mismas fotos repartidas por las carpetas de un Mac. Algunas son copias exactas; la mayoría son tomas casi idénticas del mismo momento. Así se encuentran las dos, te quedas con la mejor y recuperas espacio, sin tocar tu biblioteca de Fotos.</p>

      <h2>Qué ofrece macOS</h2>
      <ul>
        <li><strong>Finder:</strong> ordenar una carpeta por nombre o tamaño ayuda a detectar copias evidentes como «IMG_1234 copia.jpg», pero no dos tomas distintas de la misma escena.</li>
        <li><strong>Fotos:</strong> su álbum Duplicados solo abarca las fotos que ya están en la biblioteca de Fotos, no tus otras carpetas ni discos.</li>
      </ul>

      <h2>Con PixCuller, paso a paso</h2>
      <p><strong>1. Instala PixCuller.</strong> <a href="{mac}">Descárgalo gratis</a>: macOS 11 o posterior en Apple Silicon, firmado y notarizado por Apple.</p>
      <p><strong>2. Abre la carpeta.</strong> Pulsa « Abrir carpeta » o arrastra una carpeta a la ventana. Se incluyen las subcarpetas y también los discos externos.</p>
      <p><strong>3. Mira las insignias.</strong> PixCuller compara el contenido de las fotos, no sus nombres: las copias exactas, las ráfagas y las tomas casi idénticas llevan la misma insignia «≈ N».</p>
      <p><strong>4. Quédate con la mejor.</strong> Abre un grupo para comparar hasta seis fotos lado a lado, conserva la más nítida y marca el resto.</p>
      <p><strong>5. Borra con seguridad.</strong> Los archivos marcados van a la Papelera del Mac, donde « Recuperar » los devuelve si cambias de opinión.</p>

      <h2>Conviene saber</h2>
      <ul>
        <li>Admite JPEG, HEIC, PNG, TIFF, WebP y archivos RAW (CR2, CR3, NEF, ARW, RAF, ORF, RW2, DNG), además de vídeos MOV y MP4.</li>
        <li>Las fotos se fechan con sus datos EXIF, así que las carpetas copiadas se siguen ordenando por el día en que se hicieron.</li>
        <li>Ordenar una carpeta es gratis y nunca tiene límite. Todo se ejecuta en tu Mac: sin cuenta, sin envíos.</li>
        <li>Las bibliotecas de Fotos y los paquetes de apps que haya dentro de la carpeta se omiten, así que PixCuller nunca husmea en los archivos de otra app.</li>
      </ul>"""),
dict(slug="find-duplicate-photos-on-windows",
     title="Cómo buscar fotos duplicadas y parecidas en Windows",
     desc="Encuentra copias exactas, ráfagas y tomas casi idénticas en tu PC o en un disco externo, conserva la mejor y manda el resto a la Papelera de reciclaje.",
     h1="Cómo buscar fotos duplicadas y parecidas en Windows 10 u 11",
     body="""      <p>Las copias de seguridad del móvil, las tarjetas de cámara y las copias antiguas dejan las mismas fotos en varias carpetas de un PC. Algunas son duplicados exactos, la mayoría son tomas casi idénticas. Así se encuentran las dos y se limpia todo con seguridad.</p>

      <h2>Qué ofrece Windows</h2>
      <ul>
        <li><strong>Explorador de archivos:</strong> ordenar por nombre, tamaño o fecha ayuda con las copias evidentes, pero no sabe que dos archivos distintos muestran la misma escena.</li>
        <li><strong>La app Fotos:</strong> buena para ver e importar, pero sin ninguna herramienta para encontrar tomas parecidas y elegir la mejor.</li>
      </ul>

      <h2>Con PixCuller, paso a paso</h2>
      <p><strong>1. Instala PixCuller.</strong> Consíguelo gratis <a href="{win}">para Windows 10 u 11</a> (64 bits), o en Microsoft Store.</p>
      <p><strong>2. Abre la carpeta.</strong> Pulsa « Abrir carpeta » o arrastra una carpeta a la ventana. Se incluyen las subcarpetas y los discos externos.</p>
      <p><strong>3. Mira las insignias.</strong> PixCuller compara lo que muestran las fotos, no los nombres de archivo: las copias exactas, las ráfagas y las tomas casi idénticas llevan la misma insignia «≈ N».</p>
      <p><strong>4. Quédate con la mejor.</strong> Compara hasta seis fotos lado a lado, conserva la más nítida y marca el resto.</p>
      <p><strong>5. Borra con seguridad.</strong> Los archivos marcados van a la Papelera de reciclaje, así que puedes restaurarlos.</p>

      <h2>Conviene saber</h2>
      <ul>
        <li>Admite JPEG, HEIC, PNG, TIFF, WebP y archivos RAW (CR2, CR3, NEF, ARW, RAF, ORF, RW2, DNG), además de vídeos MOV y MP4. Las miniaturas HEIC requieren las Extensiones de imagen HEIF gratuitas de Microsoft.</li>
        <li>Las fotos se fechan con sus datos EXIF, así que las carpetas copiadas se siguen ordenando por el día en que se hicieron.</li>
        <li>Ordenar una carpeta es gratis y nunca tiene límite. Todo se ejecuta en tu PC: sin cuenta, sin envíos.</li>
      </ul>"""),
dict(slug="sort-photo-folder-external-drive",
     title="Cómo ordenar una carpeta enorme de fotos en un Mac o PC",
     desc="Copias antiguas, tarjetas de cámara, un disco externo lleno: un método sencillo para ordenar miles de fotos por viaje, quitar casi copias y conservar lo mejor.",
     h1="Cómo ordenar una carpeta enorme de fotos, o un disco externo entero",
     body="""      <p>Todos tenemos una: una carpeta llamada «Fotos por ordenar», una copia antigua del móvil, un disco externo que se ha ido llenando durante diez años. Miles de archivos, sin orden y con muchas casi copias. Este es un método para despacharlo en una sola sesión.</p>

      <h2>1. Abre toda la carpeta de una vez</h2>
      <p>No vayas carpeta por carpeta. Abre la carpeta principal en <a href="{pc}">PixCuller</a> (« Abrir carpeta », o arrástrala a la ventana): se incluyen las subcarpetas y cada foto se fecha con sus datos EXIF, no por el día en que se copió.</p>

      <h2>2. Deja que aparezcan los viajes</h2>
      <p>La vista Viajes agrupa las fotos por fecha y lugar y muestra el espacio que ocupa cada grupo. Diez años de archivos se convierten en una lista de viajes y eventos, y empiezas por el más pesado.</p>

      <h2>3. Reduce las casi copias</h2>
      <p>Las ráfagas, las tomas repetidas y las copias de una misma foto llevan una insignia «≈ N». Compara hasta seis lado a lado, conserva la mejor y marca el resto. Solo con este paso suele desaparecer buena parte de los archivos.</p>

      <h2>4. Marca lo que sobra a simple vista</h2>
      <p>Capturas de pantalla, fotos movidas, vídeos accidentales: márcalos sobre la marcha. No se borra nada hasta que confirmes.</p>

      <h2>5. Borra con seguridad</h2>
      <p>Los archivos confirmados van a la Papelera en un Mac o a la Papelera de reciclaje en Windows, así que un error se puede deshacer. Vacíala cuando estés seguro.</p>

      <h2>Conviene saber</h2>
      <ul>
        <li>Se admiten los archivos RAW de cámara (CR2, CR3, NEF, ARW, RAF, ORF, RW2, DNG) junto con JPEG, HEIC, PNG y vídeos.</li>
        <li>Ordenar carpetas es gratis y nunca tiene límite, en Mac (<a href="{mac}">descarga</a>) y en Windows (<a href="{win}">descarga</a>).</li>
        <li>Tus originales no se modifican nunca: el único cambio que hace PixCuller es el borrado que confirmas.</li>
      </ul>"""),
dict(slug="sort-android-photos-on-mac",
     title="Cómo ordenar las fotos de Android en un Mac",
     desc="A un Mac siempre le ha costado leer los móviles Android por USB. Cómo ordenar miles de fotos de Android en un Mac con macOS 27 y borrar lo que no necesitas.",
     h1="Cómo ordenar las fotos de Android en un Mac",
     body="""      <p>Conecta un móvil Android a un Mac y, casi siempre, no pasa nada útil: macOS nunca ha leído los móviles Android por USB como lo hace Windows. Y sin embargo un Mac es el mejor sitio para ordenar un carrete grande, con una pantalla amplia, un ratón y comparación lado a lado. Esto es lo que funciona.</p>

      <h2>Lo que macOS puede hacer por sí solo</h2>
      <ul>
        <li><strong>Captura de Imagen:</strong> puede ver el móvil si eliges « Transferir fotos » (PTP) en la notificación USB, pero solo como una lista plana de archivos, sin agrupar y sin forma de comparar fotos parecidas.</li>
        <li><strong>Android File Transfer de Google:</strong> ya no tiene mantenimiento y, de todos modos, solo copia archivos.</li>
        <li><strong>Subir a la nube:</strong> enviarlo todo a un servicio online solo para ordenarlo es lento, gasta tus datos y deja tus fotos en el servidor de otra persona.</li>
      </ul>

      <h2>Con PixCuller, por USB, paso a paso</h2>
      <p><strong>1. Instala PixCuller.</strong> <a href="{mac}">Descarga PixCuller para Mac</a> gratis. Para leer un móvil Android hace falta macOS 27 o posterior; en un Mac más antiguo, la app muestra un mensaje que lo indica. No hace falta instalar nada en el móvil.</p>
      <p><strong>2. Conecta el móvil.</strong> Conéctalo con un cable USB, desbloquéalo y elige « Transferencia de archivos » en su notificación USB.</p>
      <p><strong>3. Conéctate.</strong> En PixCuller, haz clic en « Teléfono Android » y después en « Conectar por USB ».</p>
      <p><strong>4. Ordena viaje a viaje.</strong> La vista Viajes agrupa el carrete por fecha y lugar, con el espacio que ocupa cada viaje. Las fotos parecidas llevan una insignia: compara hasta seis lado a lado, quédate con la mejor y marca el resto.</p>
      <p><strong>5. Borra con seguridad.</strong> Haz clic en Borrar y confirma. PixCuller borra las fotos directamente por el cable: el borrado es inmediato y definitivo en el móvil (las fotos no pasan por su papelera), pero por defecto PixCuller guarda durante 30 días una copia de cada elemento borrado en tu Mac, en una carpeta « PixCuller Trash » dentro de Imágenes, de modo que un error se puede deshacer.</p>

      <h2>Conviene saber</h2>
      <ul>
        <li>Todo se queda en tu Mac y tu móvil: sin cuenta, sin nube, sin envíos.</li>
        <li>PixCuller nunca modifica tus originales y solo borra lo que confirmas.</li>
        <li>PixCuller es gratis, sin suscripción.</li>
        <li>¿Tienes también un iPhone? También se conecta al Mac con un cable USB.</li>
      </ul>"""),
dict(slug="sort-android-photos-on-pc",
     title="Cómo ordenar las fotos de Android en un PC con Windows",
     desc="Ordena miles de fotos de Android en Windows 10 u 11: qué muestran el Explorador y la app Fotos, y una forma más rápida de agrupar y borrar.",
     h1="Cómo ordenar las fotos de Android en un PC con Windows",
     body="""      <p>Windows lee bien los móviles Android, pero leer no es ordenar. Con miles de fotos, las herramientas integradas te dejan desplazándote por una lista interminable de nombres de archivo. Esto es lo que hacen, y una forma más rápida de liberar el móvil desde tu PC.</p>

      <h2>Con las herramientas de Windows</h2>
      <ul>
        <li><strong>Explorador de archivos:</strong> tras elegir « Transferencia de archivos » en el móvil, su carpeta DCIM aparece como archivos. Puedes borrar desde ahí, pero sin agrupar y sin forma de comparar fotos parecidas.</li>
        <li><strong>App Fotos:</strong> importa una copia al PC. Una buena copia de seguridad, pero no te dice qué quitar del móvil.</li>
        <li><strong>Enlace Móvil:</strong> solo muestra las fotos recientes, de una en una.</li>
      </ul>

      <h2>Con PixCuller, paso a paso</h2>
      <p><strong>1. Instala PixCuller.</strong> Consíguelo gratis <a href="{win}">para Windows 10 u 11</a>, o en Microsoft Store. No hace falta instalar nada en el móvil.</p>
      <p><strong>2. Conecta por USB.</strong> Conecta el móvil, desbloquéalo y elige « Transferencia de archivos » en su notificación USB. Después haz clic en « Teléfono Android » en PixCuller, y en « Conectar por USB ».</p>
      <p><strong>3. Ordena viaje a viaje.</strong> La vista Viajes agrupa el carrete por fecha y lugar y muestra el espacio que ocupa cada viaje. Empieza por el más pesado.</p>
      <p><strong>4. Compara y marca.</strong> Las fotos parecidas llevan una insignia: abre hasta seis lado a lado, quédate con la mejor y marca el resto, junto con capturas de pantalla y vídeos grandes.</p>
      <p><strong>5. Borra con seguridad.</strong> Confirma, y PixCuller borra las fotos directamente por el cable. El borrado es inmediato y definitivo en el móvil (sin papelera), pero por defecto PixCuller guarda durante 30 días una copia de cada elemento borrado en tu PC, en una carpeta « PixCuller Trash » dentro de Imágenes.</p>

      <h2>Conviene saber</h2>
      <ul>
        <li>Todo se queda en tu PC y tu móvil: sin cuenta, sin nube, sin envíos.</li>
        <li>Borrar desde el Explorador de archivos es definitivo y no guarda ninguna copia; PixCuller guarda por defecto la copia de 30 días en el PC.</li>
        <li>PixCuller es gratis, y ordenar una carpeta del PC funciona igual.</li>
      </ul>"""),
dict(slug="free-up-android-from-mac-or-pc",
     title="Cómo liberar espacio en Android desde un Mac o un PC",
     desc="Conecta tu móvil Android por USB, ordena las fotos en una pantalla grande y borra lo que no necesitas, sin pagar Google One y sin subir nada.",
     h1="Cómo liberar espacio en tu móvil Android desde un Mac o un PC",
     body="""      <p>Cuando un móvil Android se queda sin espacio, casi siempre la causa son las fotos y los vídeos. Limpiarlos en una pantalla pequeña es lento. Desde un ordenador ves más a la vez y decides más rápido, sin comprar más almacenamiento en la nube.</p>

      <h2>Por qué ayuda un ordenador</h2>
      <p>Una pantalla grande muestra decenas de fotos a la vez, un ratón selecciona cientos en segundos y comparar tomas casi idénticas lado a lado es mucho más fácil que ir deslizando de una a otra. Un carrete que en el móvil te llevaría una tarde, se despacha en minutos.</p>

      <h2>El método</h2>
      <p><strong>1. Conecta el móvil.</strong> Instala <a href="{pc}">PixCuller</a> en un PC con Windows 10/11 o en un Mac con macOS 27 o posterior; no hace falta instalar nada en el móvil. Conecta el móvil con un cable USB, desbloquéalo, elige « Transferencia de archivos » en su notificación USB y después haz clic en « Teléfono Android » y en « Conectar por USB ».</p>
      <p><strong>2. Empieza por lo que más pesa.</strong> La vista Viajes muestra el espacio que ocupa cada viaje; los vídeos largos y las vacaciones antiguas suelen liberar más.</p>
      <p><strong>3. Elimina las tomas casi idénticas.</strong> Las ráfagas y las tomas repetidas de la misma escena llevan una insignia. Compáralas lado a lado, quédate con la mejor y marca el resto.</p>
      <p><strong>4. Limpia capturas de pantalla y fotos borrosas.</strong> Rara vez merecen quedarse y se marcan rápido todas juntas.</p>
      <p><strong>5. Confirma el borrado.</strong> PixCuller borra las fotos directamente por el cable. El borrado es inmediato y definitivo en el móvil (no hay papelera que vaciar, el espacio se recupera enseguida), y por defecto PixCuller guarda durante 30 días una copia de cada elemento borrado en tu ordenador, en una carpeta « PixCuller Trash » dentro de Imágenes.</p>

      <h2>¿Necesito Google One?</h2>
      <p>El almacenamiento en la nube es una buena copia de seguridad, pero lo guarda todo, duplicados incluidos. Limpiar primero significa que necesitas menos almacenamiento, en el móvil y en la nube.</p>

      <h2>Conviene saber</h2>
      <ul>
        <li>Sin cuenta y sin envíos: el móvil y el ordenador se comunican por el cable USB.</li>
        <li>PixCuller es gratis, sin suscripción.</li>
      </ul>"""),
],
}
