# -*- coding: utf-8 -*-
# English source for the FAQ and blog of the PixCuller site. Tokens in answers/articles: {pc} {mac} {win} (see link_tokens).

BLOG_UI = dict(
    nav="Blog", privacy="Privacy", more="Keep reading",
    cta_mac="💻 Download PixCuller for Mac", cta_win="🪟 Download PixCuller for Windows",
    twin_android="Using an Android phone? Read the Android guide:",
    twin_iphone="Using an iPhone? Read the iPhone guide:",
    index={
        "pixculler": dict(
            title="PixCuller blog — sort photos on a Mac or PC",
            desc="Guides to sort thousands of photos faster on a big screen, compare similar shots side by side and clear your iPhone or Android phone from a Mac or PC.",
            h1="Guides to sort your photos on a computer",
            intro="Why a big screen changes how fast you can sort photos, and how to use it to clear your iPhone or Android phone."),
    },
)

FAQ_PIXCULLER = dict(
    title="PixCuller FAQ — sort and delete photos on a Mac or PC",
    desc="How to sort thousands of photos on a computer, compare similar shots, free up an iPhone or Android phone from a Mac or PC: answers about PixCuller.",
    nav_home="PixCuller",
    h1="Questions and answers",
    intro="How to sort your photos faster from a computer, clear your iPhone or Android phone from a Mac or PC, and what PixCuller does (and never does) with your photos.",
    qa=[
        ("How does PixCuller know a photo is already saved on my computer?",
         "Add the folders where you keep your photos (a disk, a USB drive) in “Backup folders”. PixCuller then looks for an identical copy of each photo in them: same content, not just the same name. Photos it finds get a green frame in the grid, and the menu has two filters, “Saved” and “Not saved”. Folders are remembered, and checking is fast from the second time on. Pick the folders where you really sort your photos rather than a whole disk: it is much quicker. A Live Photo counts as saved when its video is there too (an option lets you skip that check). Nothing leaves your computer."),
        ("Can I search my photos by place or date?",
         "Yes. Type a place, a country, a date or a file name in the search box: “Milan”, “Italy”, “August 2026”, “11.02.2025”. The place comes from the photos' GPS and is looked up offline, so nothing is sent anywhere. A calendar button filters by period, and the grid can show one section per day or stay dense."),
        ('How do I sort my iPhone photos on a computer, Mac or PC?',
         "Plug the iPhone into the computer with a USB cable, unlock it and tap Trust, then open <a href=\"{pc}\">PixCuller</a>: it groups your camera roll by trip, compares similar shots side by side and marks hundreds of photos in a few clicks. Step-by-step guides: <a href=\"{post:sort-iphone-photos-on-mac}\">on a Mac</a> and <a href=\"{post:sort-iphone-photos-on-pc}\">on a Windows PC</a>."),
        ("Why sort photos on a computer instead of on the iPhone?",
         "A big screen shows more photos at once, a mouse and keyboard select hundreds of them in seconds, and comparing shots side by side is easier than flipping back and forth. Sorting a camera roll of thousands of photos is a few sittings on a phone and a much shorter session on a Mac or PC."),
        ("What is PixCuller?",
         "PixCuller is a free desktop app for Mac and Windows that groups your photos by trip, compares similar shots side by side and bulk-deletes what is not worth keeping. It reads the camera roll of an iPhone or Android phone over a USB cable, or any folder of photos on your computer, and works 100% on-device."),
        ("How do I sort thousands of photos quickly?",
         "Open the Trips view: your library is grouped by trip with the space each one takes, so you start with the heaviest. Inside a trip, mark photos in bulk, compare the similar ones side by side and keep the best shot of each group. Filters (single-day trips, excluded places like home or work, size) narrow things down."),
        ("How do I free up my iPhone storage from a Mac or PC?",
         "Plug in your iPhone by USB, open PixCuller, mark the trips and photos you no longer need, and confirm. PixCuller deletes them directly over the USB cable, on Windows 10/11 or on a Mac with macOS 27 or later, as long as iCloud Photos is off. The deletion is immediate and permanent on the iPhone, with a copy kept on your computer for 30 days by default. On macOS 26 or earlier, PixCuller still shows and sorts the iPhone's photos, but you delete them in the iPhone's Photos app."),
        ("Can I delete photos from my iPhone directly from my computer?",
         "Yes. With an iPhone, PixCuller deletes the photos directly over the USB cable, from a Mac or a Windows PC, with nothing to buy. Three conditions: iCloud Photos is turned off on the iPhone (when it is on, Apple does not allow this deletion), a Mac runs macOS 27 or later (any Windows 10/11 PC works), and you accept that the deletion is immediate and permanent on the iPhone: the photos do not go to “Recently Deleted”. By default, PixCuller keeps a copy of each deleted item on your computer for 30 days, in a “PixCuller Trash” folder in Pictures (a checkbox when you confirm), so a mistake can be undone by importing the file again. Live Photos and edited photos are handled correctly (all their versions are deleted together), and PixCuller shows the edited version of an edited photo. If iCloud Photos is on, turn it off (Settings > [your name] > iCloud > Photos) or delete in the iPhone's Photos app. On macOS 26 or earlier, PixCuller can show and sort the iPhone's photos but not delete them: a banner in the app says so, and you delete in the iPhone's Photos app."),
        ("Is deleting from PixCuller permanent?",
         "On a phone, yes. With an iPhone or an Android phone, the deletion over the USB cable is immediate and permanent on the phone: the photos do not go to “Recently Deleted” or to the phone's trash. By default, PixCuller keeps a copy of each deleted item on your computer for 30 days, in a “PixCuller Trash” folder in Pictures (a checkbox when you confirm), so you can import it again. In a folder on your computer, files go to the Trash or Recycle Bin."),
        ("How do I connect my iPhone to PixCuller?",
         "Use a USB cable, unlock the iPhone and tap “Trust” when asked. On a Mac nothing else is needed. On Windows, install the free Apple Devices app from the Microsoft Store, which provides the driver that lets PixCuller read the iPhone."),
        ("Can I sort an Android phone's photos on my Mac or PC?",
         "Yes, over a USB cable: on any Windows 10/11 PC, and on a Mac with macOS 27 or later. You get the same trips view, side-by-side comparison and bulk deletion as with an iPhone. Nothing needs to be installed on the phone."),
        ("How do I connect my Android phone?",
         "Plug the phone into the computer with a USB cable, unlock it and choose “File transfer” in its USB notification. In PixCuller, click Android phone, then Connect over USB. Guides: <a href=\"{post:sort-android-photos-on-mac}\">on a Mac</a>, <a href=\"{post:sort-android-photos-on-pc}\">on a Windows PC</a>."),
        ("Why doesn't my Mac see my Android phone?",
         "PixCuller reads Android phones over USB on macOS 27 or later; on an older Mac, the app shows a message saying so. On macOS 27 or later, check that the phone is unlocked and that “File transfer” is chosen in its USB notification. On Windows 10/11, the USB connection works with any version."),
        ("Do I need to install anything on my phone?",
         "No. PixCuller works on its own, with nothing to install on the phone and no other app needed. An iPhone or an Android phone only needs a USB cable. On Windows, reading an iPhone also needs the free Apple Devices app on the PC, from the Microsoft Store."),
        ("What happens to photos I delete on an Android phone?",
         "PixCuller deletes them directly over the USB cable, after you confirm. The deletion is immediate and permanent: the photos do not go to the phone's trash. By default, PixCuller keeps a copy of each deleted item on your computer for 30 days, in a “PixCuller Trash” folder in Pictures (a checkbox when you confirm), so a mistake can be undone."),
        ("How do I find duplicate photos in a folder on my Mac or PC?",
         "Open the folder in PixCuller (Open folder, or drop it onto the window). It looks through the subfolders, compares what the photos show and puts the same “≈ N” badge on exact copies, bursts and near-identical shots. Keep the best of each group and send the rest to the Trash or Recycle Bin. Guides: <a href=\"{post:find-duplicate-photos-on-mac}\">on a Mac</a>, <a href=\"{post:find-duplicate-photos-on-windows}\">on Windows</a>."),
        ("Can I use PixCuller on photos stored on my computer, not on an iPhone?",
         "Yes. Open any folder: PixCuller finds similar photos in it, shows the badges on the similar ones and lets you compare and delete."),
        ("How does PixCuller find similar photos?",
         "It compares the content of your photos, not their file names, so bursts, near-identical shots and the same scene taken several times end up in the same group. You can compare up to 6 photos side by side and keep the sharpest, best-framed one."),
        ("How do I compare similar photos side by side?",
         "Select a group of similar photos and open the comparison: up to 6 photos are shown at the same size so you can judge focus, expressions and framing. Keep the best one and mark the rest."),
        ("Does PixCuller work on Windows?",
         "Yes: Windows 10 and 11 (64-bit). Reading an iPhone requires the free Apple Devices app from the Microsoft Store. The app is not code-signed yet, so Windows SmartScreen may show a warning on first launch: choose “More info” then “Run anyway”."),
        ("Which Macs does PixCuller support?",
         "Macs with Apple Silicon running macOS 11 or later. The app is signed and notarized by Apple, so it opens without a security warning."),
        ("Is PixCuller free? Is there a subscription?",
         "Yes, PixCuller is free, with no subscription and no in-app purchase. Browsing, comparing, sorting and deleting are free, on a phone as in a folder on your computer."),
        ("Does PixCuller send my photos to a server or the cloud?",
         "No. PixCuller works 100% on-device: no account, no cloud, no photo, video or location is ever sent anywhere. Place recognition and similar-photo detection run on your computer. Only optional, anonymous usage statistics can be sent."),
        ("Will PixCuller change or modify my original photos?",
         "No. PixCuller only reads your photos to show and compare them. The only change it ever makes is the deletion you confirm."),
        ("How do I hide my home and workplace from the trips view?",
         "Add them as excluded places: daily life then stops showing up as a trip and your real trips stand out."),
        ("Can I clean up after a vacation from my computer?",
         "Yes, it is the typical use. After a trip, plug in the phone, open that trip in PixCuller, compare the similar shots, keep the best of each and delete the rest."),
        ("Can I use PixCuller to prepare a photo album or a backup?",
         "PixCuller helps you decide what is worth keeping: sort the trip, remove the duplicates and near-identical shots, then back up or share what is left."),
    ],
    footer_copy="© 2026 PixCuller. Developed by Jeffrey Brignoli.",
    footer_privacy="Privacy", footer_kofi="Ko-fi",
)

BLOG = {
"pixculler": [
dict(slug="sort-iphone-photos-on-mac",
     title="How to sort your iPhone photos on a Mac",
     desc="Sort thousands of iPhone photos on your Mac: what Photos and Image Capture can and can't do, and a faster way to group, compare and delete.",
     h1="How to sort your iPhone photos on a Mac",
     body="""      <p>Sorting a full camera roll on the iPhone means hours of tapping. On a Mac you see far more photos at once, select with the mouse and compare shots on a big screen. Here is how to do it, with the tools built into macOS and with a dedicated app.</p>

      <h2>With the tools built into macOS</h2>
      <ul>
        <li><strong>Photos:</strong> imports a copy of your iPhone photos to the Mac. Useful as a backup, but it doesn't tell you what to delete on the iPhone.</li>
        <li><strong>Image Capture:</strong> lists the iPhone's photos as plain files, with no grouping by trip and no way to compare similar shots.</li>
      </ul>
      <p>Both work, but with thousands of photos you are still scrolling one long list.</p>

      <h2>With PixCuller, step by step</h2>
      <p><strong>1. Install PixCuller.</strong> <a href="{mac}">Download it for free</a>: macOS 11 or later on Apple Silicon, signed and notarized by Apple.</p>
      <p><strong>2. Plug in the iPhone.</strong> Connect it with a USB cable, unlock it and tap Trust.</p>
      <p><strong>3. Sort trip by trip.</strong> The Trips view groups your camera roll by date and place and shows the space each trip takes. Start with the heaviest.</p>
      <p><strong>4. Compare and mark.</strong> Similar photos carry a badge: open up to six side by side, keep the best and mark the rest, along with screenshots and big videos you don't need.</p>
      <p><strong>5. Delete safely.</strong> With iCloud Photos off and macOS 27 or later, PixCuller deletes the photos directly over the USB cable. The deletion is immediate and permanent on the iPhone: the photos do not go to “Recently Deleted”. By default, PixCuller keeps a copy of each deleted item on your Mac for 30 days, in a “PixCuller Trash” folder in Pictures, so a mistake can be undone by importing the file again. If iCloud Photos is on, turn it off (Settings > [your name] > iCloud > Photos) or delete in the iPhone's Photos app.</p>

      <h2>Good to know</h2>
      <ul>
        <li>Everything stays on your Mac and your iPhone: no account, no cloud, no upload.</li>
        <li>PixCuller never modifies your originals and only deletes what you confirm.</li>
        <li>On macOS 26 or earlier, PixCuller shows and sorts the iPhone's photos but cannot delete them: a banner in the app says so, and you delete in the iPhone's Photos app.</li>
        <li>PixCuller is free, and sorting a folder of photos on the Mac works the same way.</li>
      </ul>"""),
dict(slug="sort-iphone-photos-on-pc",
     title="How to sort your iPhone photos on a Windows PC",
     desc="Sort thousands of iPhone photos on Windows 10 or 11: what the Photos app and File Explorer show, and a faster way to group, compare and delete.",
     h1="How to sort your iPhone photos on a Windows PC",
     body="""      <p>An iPhone and a Windows computer? You can still sort your photos on a big screen instead of the phone. Here is what Windows can do on its own, and a faster method.</p>

      <h2>With the tools built into Windows</h2>
      <ul>
        <li><strong>Photos app:</strong> imports a copy of your iPhone photos to the PC. Good for a backup, but it doesn't help you choose what to delete.</li>
        <li><strong>File Explorer:</strong> shows the iPhone's photos in folders such as 100APPLE, named IMG_0001 and so on, with no trips and no comparison of similar shots.</li>
      </ul>

      <h2>With PixCuller, step by step</h2>
      <p><strong>1. Install Apple Devices.</strong> Get the free Apple Devices app from the Microsoft Store: Windows needs it to read an iPhone.</p>
      <p><strong>2. Install PixCuller.</strong> Get it from the Microsoft Store or <a href="{win}">download it for free</a> (Windows 10/11, 64-bit). The download is not code-signed yet, so SmartScreen may warn on first launch.</p>
      <p><strong>3. Plug in the iPhone.</strong> Connect it with a USB cable, unlock it and tap Trust.</p>
      <p><strong>4. Sort trip by trip.</strong> The Trips view groups your camera roll by date and place and shows the space each trip takes. Start with the heaviest.</p>
      <p><strong>5. Compare, mark, delete.</strong> Similar photos carry a badge: compare up to six side by side, keep the best and mark the rest. With iCloud Photos off, PixCuller deletes them directly over the USB cable. The deletion is permanent on the iPhone (no “Recently Deleted”), but by default PixCuller keeps a copy of each deleted item on your PC for 30 days, in a “PixCuller Trash” folder in Pictures. If iCloud Photos is on, turn it off (Settings > [your name] > iCloud > Photos) or delete in the iPhone's Photos app.</p>

      <h2>Good to know</h2>
      <ul>
        <li>Everything stays on your PC and your iPhone: no account, no cloud, no upload.</li>
        <li>PixCuller never modifies your originals and only deletes what you confirm.</li>
        <li>Browsing and sorting are free, and sorting a folder of photos already on the PC is never limited.</li>
      </ul>"""),
dict(slug="sort-photos-on-computer",
     title="How to sort thousands of photos faster on a Mac or PC",
     desc="Why sorting photos on a big screen is so much faster than on a phone, and a simple method to go through thousands of photos in one sitting.",
     h1="How to sort thousands of photos faster on a Mac or PC",
     body="""      <p>If your camera roll holds ten thousand photos, sorting it on a phone screen is a project you will never finish. On a computer it can be a single evening. Here is why, and a method that works.</p>

      <h2>Why a computer is faster</h2>
      <ul>
        <li><strong>More on screen:</strong> dozens of photos at once instead of a handful.</li>
        <li><strong>Precise selection:</strong> a mouse and keyboard select hundreds of photos in seconds.</li>
        <li><strong>Real comparison:</strong> similar photos next to each other at a size where focus and expressions are visible.</li>
      </ul>

      <h2>A method that works</h2>
      <p><strong>1. Group by trip.</strong> Sorting by date and place breaks the library into manageable pieces. Start with the trip that takes the most space.</p>
      <p><strong>2. Remove the near-copies.</strong> Compare each group of similar shots, keep the best and mark the rest.</p>
      <p><strong>3. Filter the noise.</strong> Hide places you don't care about (home, work) so real trips stand out, and filter by size to find heavy files.</p>
      <p><strong>4. Delete in one go.</strong> Mark hundreds of photos and confirm once.</p>

      <h2>PixCuller does exactly this</h2>
      <p><a href="{pc}">PixCuller</a> is a free desktop app for Mac and Windows. Its Trips view groups the library by trip and shows the space each takes, similar photos carry a badge, and you can compare up to six side by side. It reads an iPhone or Android phone over a USB cable, or any folder on your computer, works 100% on-device and never modifies your originals.</p>
      <p>On a phone, PixCuller deletes directly over the USB cable, on Windows 10/11 or on a Mac with macOS 27 or later (with iCloud Photos off on an iPhone). The deletion is permanent on the phone, with a copy kept on your computer for 30 days by default. In a folder, files go to the Trash or Recycle Bin. Sorting is never limited.</p>

      <h2>Tips for a long session</h2>
      <ul>
        <li>Work trip by trip, not by scrolling the whole library.</li>
        <li>Decide fast: if two shots look alike, keep one.</li>
        <li>Delete at the end of each trip, so progress is visible.</li>
      </ul>"""),
dict(slug="free-up-iphone-from-mac-or-pc",
     title="How to free up your iPhone storage from a Mac or Windows PC",
     desc="Plug in your iPhone, sort photos on a big screen and delete what you don't need, without iCloud and without sending anything online.",
     h1="How to free up your iPhone from a Mac or Windows PC",
     body="""      <p>Cleaning a full iPhone on the iPhone is tedious. From a computer you can see far more photos at once and decide faster. Here is the whole process.</p>

      <h2>What you need</h2>
      <ul>
        <li>A Mac (Apple Silicon, macOS 11+) or a Windows 10/11 PC.</li>
        <li>A USB cable. On Windows, also the free Apple Devices app from the Microsoft Store.</li>
        <li><a href="{pc}">PixCuller</a>, free for both systems.</li>
        <li>For deleting from the iPhone: iCloud Photos turned off and, on a Mac, macOS 27 or later. On macOS 26 or earlier, PixCuller still shows and sorts the photos, and you delete them in the iPhone's Photos app.</li>
      </ul>

      <h2>Step by step</h2>
      <p><strong>1. Plug in and trust.</strong> Connect the iPhone, unlock it and tap Trust.</p>
      <p><strong>2. Open the Trips view.</strong> PixCuller groups your camera roll by trip and shows the space each takes.</p>
      <p><strong>3. Sort the heaviest trips.</strong> Compare similar shots, keep the best, and mark the rest, plus screenshots and big videos you don't need.</p>
      <p><strong>4. Confirm the deletion.</strong> With iCloud Photos off (and macOS 27 or later on a Mac), PixCuller deletes the photos directly over the USB cable, on Windows too. The deletion is immediate and permanent on the iPhone, but by default PixCuller keeps a copy of each deleted item on your computer for 30 days, in a “PixCuller Trash” folder in Pictures.</p>
      <p><strong>5. If iCloud Photos is on.</strong> PixCuller refuses the deletion: turn iCloud Photos off (Settings > [your name] > iCloud > Photos) or delete in the iPhone's Photos app.</p>

      <h2>Is it safe?</h2>
      <p>Yes: your photos stay on your devices, with no account, no cloud and no upload. PixCuller only reads your photos until you confirm. A deletion is permanent on the iPhone, but a copy stays on your computer for 30 days by default.</p>


      <h2>On Windows</h2>
      <p>The steps are the same on Windows 10 and 11. Install the free Apple Devices app from the Microsoft Store first, so PixCuller can read the iPhone. The app is not code-signed yet, so SmartScreen may warn on first launch.</p>"""),
dict(slug="compare-similar-photos-keep-the-best",
     title="How to compare similar photos and keep the best one",
     desc="A simple routine to choose the best shot among near-identical photos: what to look at, and how to do it quickly on a big screen.",
     h1="How to compare similar photos and keep the best one",
     body="""      <p>You took six photos of the same moment and they all look fine. Choosing the best takes seconds with the right method, and a few minutes with the wrong one.</p>

      <h2>What to check, in this order</h2>
      <ol>
        <li><strong>Focus.</strong> Zoom on the eyes or the main subject. A blurry subject is disqualifying.</li>
        <li><strong>Expressions.</strong> Eyes open, natural smiles, nobody mid-blink.</li>
        <li><strong>Framing.</strong> Nothing cut off, a clean background, the horizon straight.</li>
        <li><strong>Moment.</strong> If two shots are equal, keep the one that feels more alive.</li>
      </ol>

      <h2>Why side by side matters</h2>
      <p>Flipping between photos makes small differences hard to see. Seeing them next to each other at the same size makes the sharpest or best-framed one obvious. A computer screen shows up to six at once, where a phone shows one.</p>

      <h2>A faster routine</h2>
      <p>Group similar photos first, so you never hunt for them in the library. For each group, open the comparison, pick one and mark the others. You decide in seconds, not minutes.</p>

      <h2>Do it with PixCuller</h2>
      <p><a href="{pc}">PixCuller</a> shows a badge on similar photos, opens up to six side by side and lets you mark the rest in one click. It works on an iPhone connected by USB or on any folder on your Mac or PC, offline, and it never modifies your originals.</p>

      <h2>Keep, don't regret</h2>
      <p>When you are unsure, keep two. When PixCuller deletes from a phone, it keeps a copy on your computer for 30 days by default; in a folder, files go to the Trash or Recycle Bin. Either way, you can still change your mind.</p>"""),
dict(slug="find-duplicate-photos-on-mac",
     title="How to find duplicate and similar photos on a Mac",
     desc="Find exact copies, bursts and near-identical shots in your Mac's photo folders or on an external drive, keep the best and send the rest to the Trash.",
     h1="How to find duplicate and similar photos on a Mac",
     body="""      <p>Years of imports, camera cards and backups leave the same photos scattered across folders on a Mac. Some are exact copies; most are near-identical shots of the same moment. Here is how to find both, keep the best and free the space, without touching your Photos library.</p>

      <h2>What macOS offers</h2>
      <ul>
        <li><strong>Finder:</strong> sorting a folder by name or size helps spot obvious copies such as “IMG_1234 copy.jpg”, but not two different shots of the same scene.</li>
        <li><strong>Photos:</strong> its Duplicates album only covers photos already in the Photos library, not your other folders or drives.</li>
      </ul>

      <h2>With PixCuller, step by step</h2>
      <p><strong>1. Install PixCuller.</strong> <a href="{mac}">Download it for free</a>: macOS 11 or later on Apple Silicon, signed and notarized by Apple.</p>
      <p><strong>2. Open the folder.</strong> Click Open folder, or drop a folder onto the window. Subfolders are included, and so are external drives.</p>
      <p><strong>3. Look at the badges.</strong> PixCuller compares the content of the photos, not their names: exact copies, bursts and near-identical shots get the same “≈ N” badge.</p>
      <p><strong>4. Keep the best one.</strong> Open a group to compare up to six photos side by side, keep the sharpest and mark the rest.</p>
      <p><strong>5. Delete safely.</strong> Marked files go to the Mac's Trash, where Put Back restores them if you change your mind.</p>

      <h2>Good to know</h2>
      <ul>
        <li>JPEG, HEIC, PNG, TIFF, WebP and RAW files (CR2, CR3, NEF, ARW, RAF, ORF, RW2, DNG) are supported, as well as MOV and MP4 videos.</li>
        <li>Photos are dated from their EXIF data, so copied folders still sort by the day they were taken.</li>
        <li>Sorting a folder is free and never limited. Everything runs on your Mac: no account, no upload.</li>
        <li>Photos libraries and app bundles inside the folder are skipped, so PixCuller never digs into another app's files.</li>
      </ul>"""),
dict(slug="find-duplicate-photos-on-windows",
     title="How to find duplicate and similar photos on Windows",
     desc="Find exact copies, bursts and near-identical shots in your PC's photo folders or on an external drive, keep the best and send the rest to the Recycle Bin.",
     h1="How to find duplicate and similar photos on Windows 10 or 11",
     body="""      <p>Phone backups, camera cards and old copies leave the same photos in several folders on a PC. Some are exact duplicates, most are near-identical shots. Here is how to find both and clean them up safely.</p>

      <h2>What Windows offers</h2>
      <ul>
        <li><strong>File Explorer:</strong> sorting by name, size or date helps with obvious copies, but it can't tell that two different files show the same scene.</li>
        <li><strong>The Photos app:</strong> good for viewing and importing, with no tool to find similar shots and pick the best.</li>
      </ul>

      <h2>With PixCuller, step by step</h2>
      <p><strong>1. Install PixCuller.</strong> Get it for free <a href="{win}">for Windows 10 or 11</a> (64-bit), or from the Microsoft Store.</p>
      <p><strong>2. Open the folder.</strong> Click Open folder, or drop a folder onto the window. Subfolders and external drives are included.</p>
      <p><strong>3. Look at the badges.</strong> PixCuller compares what the photos show, not their file names: exact copies, bursts and near-identical shots get the same “≈ N” badge.</p>
      <p><strong>4. Keep the best one.</strong> Compare up to six photos side by side, keep the sharpest, mark the rest.</p>
      <p><strong>5. Delete safely.</strong> Marked files go to the Recycle Bin, so you can restore them.</p>

      <h2>Good to know</h2>
      <ul>
        <li>JPEG, HEIC, PNG, TIFF, WebP and RAW files (CR2, CR3, NEF, ARW, RAF, ORF, RW2, DNG) are supported, as well as MOV and MP4 videos. HEIC thumbnails need Microsoft's free HEIF Image Extensions.</li>
        <li>Photos are dated from their EXIF data, so copied folders still sort by the day they were taken.</li>
        <li>Sorting a folder is free and never limited. Everything runs on your PC: no account, no upload.</li>
      </ul>"""),
dict(slug="sort-photo-folder-external-drive",
     title="How to sort a big folder of photos on a Mac or PC",
     desc="Old backups, camera cards, an external drive full of photos: a simple method to sort thousands of files by trip, remove near-duplicates and keep the best.",
     h1="How to sort a big folder of photos, or a whole external drive",
     body="""      <p>Everyone has one: a folder called “Photos to sort”, an old phone backup, an external drive filled over ten years. Thousands of files, no order, many near-duplicates. Here is a method to get through it in one sitting.</p>

      <h2>1. Open the whole folder at once</h2>
      <p>Don't go folder by folder. Open the top folder in <a href="{pc}">PixCuller</a> (Open folder, or drop it onto the window): subfolders are included, and each photo is dated from its EXIF data rather than from the day it was copied.</p>

      <h2>2. Let the trips appear</h2>
      <p>The Trips view groups photos by date and place and shows the space each group takes. Ten years of files become a list of trips and events, and you start with the heaviest.</p>

      <h2>3. Collapse the near-duplicates</h2>
      <p>Bursts, repeated takes and copies of the same shot carry a “≈ N” badge. Compare up to six side by side, keep the best one, mark the rest. This step alone often removes a large share of the files.</p>

      <h2>4. Mark the obvious leftovers</h2>
      <p>Screenshots, blurry shots, accidental videos: mark them as you go. Nothing is deleted until you confirm.</p>

      <h2>5. Delete safely</h2>
      <p>Confirmed files go to the Trash on a Mac or the Recycle Bin on Windows, so a mistake can be undone. Empty it once you are sure.</p>

      <h2>Good to know</h2>
      <ul>
        <li>RAW files from cameras (CR2, CR3, NEF, ARW, RAF, ORF, RW2, DNG) are supported alongside JPEG, HEIC, PNG and videos.</li>
        <li>Sorting folders is free and never limited, on Mac (<a href="{mac}">download</a>) and Windows (<a href="{win}">download</a>).</li>
        <li>Your originals are never modified: the only change PixCuller makes is the deletion you confirm.</li>
      </ul>"""),
dict(slug="sort-android-photos-on-mac",
     title="How to sort your Android photos on a Mac",
     desc="A Mac has long struggled to read Android phones over USB. How to sort thousands of Android photos on a Mac with macOS 27 and delete what you don't need.",
     h1="How to sort your Android photos on a Mac",
     body="""      <p>Plug an Android phone into a Mac and, most of the time, nothing useful happens: macOS has never read Android phones over USB the way Windows does. Yet a Mac is the best place to sort a big camera roll, with a large screen, a mouse and side-by-side comparison. Here is what works.</p>

      <h2>What macOS can do on its own</h2>
      <ul>
        <li><strong>Image Capture:</strong> may see the phone if you choose “Transfer photos” (PTP) in its USB notification, but only as a flat list of files, with no grouping and no way to compare similar shots.</li>
        <li><strong>Google's Android File Transfer:</strong> no longer maintained, and it only copies files anyway.</li>
        <li><strong>Cloud upload:</strong> sending everything to an online service just to sort it is slow, uses your data plan and puts your photos on someone else's server.</li>
      </ul>

      <h2>With PixCuller, over USB, step by step</h2>
      <p><strong>1. Install PixCuller.</strong> <a href="{mac}">Download PixCuller for Mac</a> for free. Reading an Android phone needs macOS 27 or later; on an older Mac, the app shows a message saying so. Nothing needs to be installed on the phone.</p>
      <p><strong>2. Plug in the phone.</strong> Connect it with a USB cable, unlock it and choose “File transfer” in its USB notification.</p>
      <p><strong>3. Connect.</strong> In PixCuller, click Android phone, then Connect over USB.</p>
      <p><strong>4. Sort trip by trip.</strong> The Trips view groups the camera roll by date and place, with the space each trip takes. Similar photos carry a badge: compare up to six side by side, keep the best, mark the rest.</p>
      <p><strong>5. Delete safely.</strong> Click Delete and confirm. PixCuller deletes the photos directly over the cable: the deletion is immediate and permanent on the phone (the photos do not go to its trash), but by default PixCuller keeps a copy of each deleted item on your Mac for 30 days, in a “PixCuller Trash” folder in Pictures, so a mistake can be undone.</p>

      <h2>Good to know</h2>
      <ul>
        <li>Everything stays on your Mac and your phone: no account, no cloud, no upload.</li>
        <li>PixCuller never modifies your originals and only deletes what you confirm.</li>
        <li>PixCuller is free, with no subscription.</li>
        <li>Got an iPhone too? It connects to the Mac with a USB cable as well.</li>
      </ul>"""),
dict(slug="sort-android-photos-on-pc",
     title="How to sort your Android photos on a Windows PC",
     desc="Sort thousands of Android photos on Windows 10 or 11: what File Explorer and the Photos app show, and a faster way to group, compare and delete.",
     h1="How to sort your Android photos on a Windows PC",
     body="""      <p>Windows reads Android phones well, but reading is not sorting. With thousands of photos, the built-in tools leave you scrolling one long list of file names. Here is what they do, and a faster way to clear the phone from your PC.</p>

      <h2>With the tools built into Windows</h2>
      <ul>
        <li><strong>File Explorer:</strong> after you choose “File transfer” on the phone, its DCIM folder shows up as files. You can delete from there, but with no grouping and no way to compare similar shots.</li>
        <li><strong>The Photos app:</strong> imports a copy to the PC. A good backup, but it doesn't tell you what to remove from the phone.</li>
        <li><strong>Phone Link:</strong> shows recent photos only, one at a time.</li>
      </ul>

      <h2>With PixCuller, step by step</h2>
      <p><strong>1. Install PixCuller.</strong> Get it for free <a href="{win}">for Windows 10 or 11</a>, or from the Microsoft Store. Nothing needs to be installed on the phone.</p>
      <p><strong>2. Connect by USB.</strong> Plug in the phone, unlock it and choose “File transfer” in its USB notification. Then click Android phone in PixCuller, and Connect over USB.</p>
      <p><strong>3. Sort trip by trip.</strong> The Trips view groups the camera roll by date and place and shows the space each trip takes. Start with the heaviest.</p>
      <p><strong>4. Compare and mark.</strong> Similar photos carry a badge: open up to six side by side, keep the best and mark the rest, along with screenshots and big videos.</p>
      <p><strong>5. Delete safely.</strong> Confirm, and PixCuller deletes the photos directly over the cable. The deletion is immediate and permanent on the phone (no trash), but by default PixCuller keeps a copy of each deleted item on your PC for 30 days, in a “PixCuller Trash” folder in Pictures.</p>

      <h2>Good to know</h2>
      <ul>
        <li>Everything stays on your PC and your phone: no account, no cloud, no upload.</li>
        <li>Deleting from File Explorer is permanent with no copy kept; PixCuller keeps the 30-day copy on the PC by default.</li>
        <li>PixCuller is free, and sorting a folder on the PC works the same way.</li>
      </ul>"""),
dict(slug="free-up-android-from-mac-or-pc",
     title="How to free up Android storage from a Mac or Windows PC",
     desc="Connect your Android phone by USB, sort photos on a big screen and delete what you don't need, without paying for Google One and without uploading anything.",
     h1="How to free up your Android phone's storage from a Mac or PC",
     body="""      <p>When an Android phone runs out of space, photos and videos are almost always the reason. Clearing them on a small screen is slow. From a computer you see more at once and decide faster, without buying more cloud storage.</p>

      <h2>Why a computer helps</h2>
      <p>A big screen shows dozens of photos at once, a mouse selects hundreds in seconds, and comparing near-identical shots side by side is far easier than swiping back and forth. A camera roll that would take an evening on the phone takes minutes.</p>

      <h2>The method</h2>
      <p><strong>1. Connect the phone.</strong> Install <a href="{pc}">PixCuller</a> on a Windows 10/11 PC or on a Mac with macOS 27 or later; nothing needs to be installed on the phone. Plug in the phone with a USB cable, unlock it, choose “File transfer” in its USB notification, then click Android phone and Connect over USB.</p>
      <p><strong>2. Start with what weighs the most.</strong> The Trips view shows the space each trip takes; long videos and old vacations usually free the most.</p>
      <p><strong>3. Remove the near-duplicates.</strong> Bursts and repeated shots of the same scene carry a badge. Compare them side by side, keep the best one, mark the rest.</p>
      <p><strong>4. Clear screenshots and blurry shots.</strong> They rarely deserve to stay and are quick to mark as a batch.</p>
      <p><strong>5. Confirm the deletion.</strong> PixCuller deletes the photos directly over the cable. The deletion is immediate and permanent on the phone (no trash to empty, the space comes back right away), and by default PixCuller keeps a copy of each deleted item on your computer for 30 days, in a “PixCuller Trash” folder in Pictures.</p>

      <h2>Do I need Google One?</h2>
      <p>Cloud storage is a fine backup, but it keeps everything, duplicates included. Cleaning first means you need less storage, on the phone and in the cloud.</p>

      <h2>Good to know</h2>
      <ul>
        <li>No account and no upload: the phone and the computer talk over the USB cable.</li>
        <li>PixCuller is free, with no subscription.</li>
      </ul>"""),
],
}
