#!/usr/bin/env python3
"""Generate a Word document with English and Dutch website copy side by side."""

from docx import Document
from docx.shared import Inches, Pt, Cm, RGBColor
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn

doc = Document()

# -- Style setup --
style = doc.styles['Normal']
font = style.font
font.name = 'Calibri'
font.size = Pt(10)

# Page margins
for section in doc.sections:
    section.top_margin = Cm(1.5)
    section.bottom_margin = Cm(1.5)
    section.left_margin = Cm(1.5)
    section.right_margin = Cm(1.5)


def add_page_header(title):
    """Add a page-level header (e.g., 'HOMEPAGE')."""
    p = doc.add_paragraph()
    run = p.add_run(title)
    run.bold = True
    run.font.size = Pt(18)
    run.font.color.rgb = RGBColor(0x0D, 0x16, 0x4F)  # Ditto navy
    p.space_after = Pt(4)


def add_section_header(title):
    """Add a section-level header within a page."""
    p = doc.add_paragraph()
    run = p.add_run(title)
    run.bold = True
    run.font.size = Pt(13)
    run.font.color.rgb = RGBColor(0x58, 0xB6, 0xD2)  # Ditto teal
    p.space_before = Pt(12)
    p.space_after = Pt(2)


def add_copy_table(rows):
    """
    Add a two-column table with English | Dutch.
    rows: list of (label, english, dutch) tuples.
    """
    table = doc.add_table(rows=1 + len(rows), cols=3)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = True

    # Header row
    hdr = table.rows[0]
    for i, text in enumerate(['Element', 'English', 'Nederlands']):
        cell = hdr.cells[i]
        cell.text = ''
        p = cell.paragraphs[0]
        run = p.add_run(text)
        run.bold = True
        run.font.size = Pt(9)
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        # Navy background
        shading = cell._element.get_or_add_tcPr()
        shading_el = shading.makeelement(qn('w:shd'), {
            qn('w:val'): 'clear',
            qn('w:color'): 'auto',
            qn('w:fill'): '0D164F'
        })
        shading.append(shading_el)

    # Data rows
    for idx, (label, en, nl) in enumerate(rows):
        row = table.rows[idx + 1]
        # Label cell
        cell0 = row.cells[0]
        cell0.text = ''
        p0 = cell0.paragraphs[0]
        run0 = p0.add_run(label)
        run0.bold = True
        run0.font.size = Pt(9)

        # English cell
        cell1 = row.cells[1]
        cell1.text = ''
        p1 = cell1.paragraphs[0]
        run1 = p1.add_run(en)
        run1.font.size = Pt(9)

        # Dutch cell
        cell2 = row.cells[2]
        cell2.text = ''
        p2 = cell2.paragraphs[0]
        run2 = p2.add_run(nl)
        run2.font.size = Pt(9)

        # Alternate row shading
        if idx % 2 == 0:
            for cell in row.cells:
                shading = cell._element.get_or_add_tcPr()
                shading_el = shading.makeelement(qn('w:shd'), {
                    qn('w:val'): 'clear',
                    qn('w:color'): 'auto',
                    qn('w:fill'): 'F7F6F3'
                })
                shading.append(shading_el)

    # Set column widths
    for row in table.rows:
        row.cells[0].width = Cm(3.5)
        row.cells[1].width = Cm(7)
        row.cells[2].width = Cm(7)

    doc.add_paragraph()  # spacer


def add_separator():
    p = doc.add_paragraph()
    p.space_before = Pt(6)
    p.space_after = Pt(6)
    doc.add_page_break()


# ============================================================
# TITLE PAGE
# ============================================================
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.space_before = Pt(100)
run = p.add_run('Ditto Care')
run.bold = True
run.font.size = Pt(28)
run.font.color.rgb = RGBColor(0x0D, 0x16, 0x4F)

p2 = doc.add_paragraph()
p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
run2 = p2.add_run('Website Copy\nEnglish / Nederlands')
run2.font.size = Pt(16)
run2.font.color.rgb = RGBColor(0x58, 0xB6, 0xD2)

p3 = doc.add_paragraph()
p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
p3.space_before = Pt(30)
run3 = p3.add_run('Based on: fulfilled-screen-670844.framer.app\nReference: dittocare.com/nl\nDate: April 2026')
run3.font.size = Pt(10)
run3.font.color.rgb = RGBColor(0x7C, 0x82, 0x97)

doc.add_page_break()

# ============================================================
# PAGE 1: HOMEPAGE
# ============================================================
add_page_header('1. HOMEPAGE')

add_section_header('Navigation')
add_copy_table([
    ('Nav item 1', 'About', 'Over ons'),
    ('Nav item 2', 'Professionals', 'Zorgverleners'),
    ('Nav item 3', 'Privacy', 'Privacy'),
    ('Nav item 4', 'Support', 'Ondersteuning'),
    ('Nav item 5', 'Press', 'Pers'),
    ('Nav CTA', 'Download App', 'Download App'),
])

add_section_header('Hero')
add_copy_table([
    ('Headline',
     'Clarity when it matters most',
     'Duidelijkheid wanneer het ertoe doet'),
    ('Subheadline',
     'Record every medical appointment. Get a clear summary in language you understand. Share it with the people who matter. Because care is something you carry together.',
     'Neem elk medisch gesprek op. Krijg een duidelijke samenvatting in taal die je begrijpt. Deel het met de mensen om je heen. Want zorg draag je samen.'),
    ('Trust line',
     '4.7/5 rating | 75,000+ users',
     '4,7/5 beoordeling | 75.000+ gebruikers'),
    ('CTA primary',
     'Download App',
     'Download App'),
    ('CTA secondary',
     'Schedule Demo',
     'Plan een demo'),
])

add_section_header('The Problem')
add_copy_table([
    ('Section headline',
     'Healthcare can feel overwhelming',
     'Zorg kan overweldigend voelen'),
    ('Card 1 title',
     'Details fade',
     'De details vervagen'),
    ('Card 1 body',
     "You walk out of the appointment and think: 'Wait, what did they say?' The more serious the conversation, the harder it is to hold onto.",
     'Je loopt de spreekkamer uit en denkt: "Wacht, wat zeiden ze ook alweer?" Hoe zwaarder het gesprek, hoe minder je onthoudt.'),
    ('Card 2 title',
     "It's hard to keep up",
     'Het wordt te veel'),
    ('Card 2 body',
     "Some health journeys are straightforward. Many aren't. Suddenly there are specialists, letters, test results, scattered across systems, written in language that wasn't meant for you.",
     'Soms is je zorg eenvoudig. Maar vaak niet. Ineens zijn er meerdere artsen, brieven en uitslagen, bij verschillende ziekenhuizen, in taal die je niet begrijpt.'),
    ('Card 3 title',
     'Everyone wants to know',
     'Iedereen wil het weten'),
    ('Card 3 body',
     "'How did it go?' Your partner asks. Then your mother. Then your friend. Explaining what happened once is already hard. Repeating it for everyone is exhausting.",
     '"Hoe ging het?" Je partner vraagt het. Dan je moeder. Dan je vriendin. Eén keer uitleggen is al lastig. Het steeds opnieuw vertellen is vermoeiend.'),
])

add_section_header('Product Showcase')
add_copy_table([
    ('Section headline',
     'This is Ditto',
     'Dit is Ditto'),
    ('Section subheadline',
     'Everything from your doctor\'s visit, captured, clarified, and shared with the people who care about you.',
     'Al je zorg op één plek, en in handen van de mensen om je heen.'),
    ('Feature 1 title',
     'Summarise any medical appointment',
     'Neem elk gesprek op'),
    ('Feature 1 body',
     'Every word from your consultation, waiting for you when you\'re ready. Listen back, reread, and never lose an important detail again.',
     'Elk woord van je consult, klaar wanneer jij er klaar voor bent. Luister terug, lees het na en verlies nooit meer een belangrijk detail.'),
    ('Feature 2 title',
     'Prepare for what\'s next',
     'Voorbereid op wat komt'),
    ('Feature 2 body',
     'Ditto suggests questions for your next visit based on what was discussed. You show up ready, your doctor notices.',
     'Ditto stelt vragen voor je volgende afspraak voor, op basis van wat er besproken is. Je komt voorbereid, en je arts merkt het.'),
    ('Feature 3 title',
     'Invite those who matter',
     'Houd je naasten dichtbij'),
    ('Feature 3 body',
     "Invite the people who matter. They see your summaries, follow your journey, and can actually help. Instead of asking 'how did it go?' and getting a half-remembered answer.",
     'Voeg de mensen toe die ertoe doen. Zij zien je samenvattingen, volgen je traject en kunnen je echt helpen. In plaats van "hoe ging het?" en dan een half antwoord.'),
])

add_section_header('Social Proof / Testimonials')
add_copy_table([
    ('Section headline',
     'Success stories',
     'Ervaringen van anderen'),
    ('Review: Els',
     'This app is brilliant. Super clear. It gives an explanation of medical terms and an overview of what you recorded.',
     'Deze app is helemaal geweldig. Super duidelijk. Geeft uitleg over medische termen. Schrijft uit wat je opneemt.'),
    ('Review: Jeanette',
     "This app is fantastic. The doctor's language is explained in simple, easy-to-understand terms.",
     'Superfijn deze app. De dokterstaal wordt in simpel Jip en Janneke taal uitgelegd.'),
    ('Review: Jacky',
     'Nice app that can turn a visit to the specialist into understandable language.',
     'Fijne app die bezoek aan de specialist kan omzetten in begrijpelijke taal.'),
    ('Review: Jeanette (2)',
     'My diagnosis and treatment are described in understandable language.',
     'In begrijpelijke taal wordt mijn diagnose en behandeling beschreven.'),
])

add_section_header('Partners')
add_copy_table([
    ('Section headline',
     'Our partners in the medical field',
     'Onze partners in de zorg'),
    ('Body',
     'We work closely together with healthcare organisations to help more and more patients across the Netherlands.',
     'We werken nauw samen met zorgorganisaties om steeds meer patiënten in heel Nederland te helpen.'),
])

add_section_header('Why Ditto Works')
add_copy_table([
    ('Section headline',
     'Why Ditto works',
     'Waarom Ditto werkt'),
    ('Section label',
     'Built for you, with care.',
     'Gebouwd voor jou, met zorg.'),
    ('USP 1 title',
     'Everything in one place',
     'Alles op één plek'),
    ('USP 1 body',
     'Your GP, your specialist, your midwife. All in one app. Every appointment, every summary, every document. No matter where you get care.',
     'Je huisarts, je specialist, je verloskundige. Alles in één app. Elke afspraak, elke samenvatting, elk document. Het maakt niet uit waar je zorg krijgt.'),
    ('USP 2 title',
     'Built for you',
     'Gebouwd voor jou'),
    ('USP 2 body',
     'Patient portals are built for hospitals. Ditto is built for you, and the people around you.',
     'Patiëntportalen zijn gebouwd voor ziekenhuizen. Ditto is gebouwd voor jou, en de mensen om je heen.'),
    ('USP 3 title',
     'Private by design',
     'Privacy als basis'),
    ('USP 3 body',
     "Your data lives on your device. When Ditto processes a recording, it uses secure EU servers, then deletes it immediately. We can't read your summaries.",
     'Je gegevens staan op je eigen telefoon. Als Ditto een opname verwerkt, gebeurt dat op beveiligde servers in de EU. Daarna wordt alles direct verwijderd. Wij kunnen je samenvattingen niet lezen.'),
    ('USP 4 title',
     'Sharing is caring',
     'Delen is zorgen'),
    ('USP 4 body',
     "Your loved ones can receive and share care updates safely, with end-to-end encryption, within Ditto. You stay in control of who's in your Care Circle.",
     'Je naasten ontvangen updates veilig via Ditto. Alles is versleuteld. Jij bepaalt wie er in je Zorgcirkel zit.'),
])

add_section_header('Closing CTA')
add_copy_table([
    ('Headline',
     'Record your first appointment tomorrow',
     'Begin met Ditto. Het is gratis.'),
    ('Body',
     "Download Ditto, create an account in under a minute, and bring it to your next visit. It's free. No trial, no catch.",
     'Beschikbaar op iOS en Android. Maak binnen 1 minuut een account aan, voeg je naasten toe en neem morgen je eerste gesprek op.'),
    ('CTA',
     'App Store | Google Play',
     'App Store | Google Play'),
])

add_section_header('FAQ')
add_copy_table([
    ('Section headline',
     'More about Ditto',
     'Veelgestelde vragen'),
    ('Q1',
     'How does Ditto work in practice?',
     'Hoe werkt Ditto in de praktijk?'),
    ('A1',
     "During an appointment, you ask whether you can record the conversation. Afterward, Ditto creates a clear summary you can revisit. You can also take photos of medical letters to get easy-to-understand explanations.",
     'Tijdens een afspraak vraag je of je het gesprek mag opnemen. Daarna maakt Ditto een duidelijke samenvatting die je terug kunt lezen. Je kunt ook foto\'s maken van medische brieven voor uitleg in begrijpelijke taal.'),
    ('Q2',
     'When should I use Ditto?',
     'Wanneer gebruik ik Ditto?'),
    ('A2',
     'Use Ditto before, during, and after appointments, especially when you want to remember details, understand medical language, or share information with people you trust.',
     'Gebruik Ditto voor, tijdens en na je afspraken. Vooral als je details wilt onthouden, medische taal wilt begrijpen, of informatie wilt delen met mensen die je vertrouwt.'),
    ('Q3',
     'How do I share summaries with loved ones?',
     'Hoe deel ik samenvattingen met mijn naasten?'),
    ('A3',
     'You can securely share your summaries via message, email, or other apps you choose. You decide what to share and with whom.',
     'Je kunt je samenvattingen veilig delen via een bericht, e-mail of andere apps. Jij bepaalt wat je deelt en met wie.'),
    ('Q4',
     'What happens to my recordings and information?',
     'Wat gebeurt er met mijn opnames en informatie?'),
    ('A4',
     'Your data is stored securely and only on your device. You stay in control of your information.',
     'Je gegevens worden veilig opgeslagen, alleen op jouw apparaat. Jij houdt de controle over je informatie.'),
    ('Q5',
     'Is Ditto free to use?',
     'Is Ditto gratis?'),
    ('A5',
     'Yes. Ditto is currently available for free to download and use.',
     'Ja. Ditto is gratis te downloaden en te gebruiken.'),
    ('Q6',
     "Can Ditto help if I don't speak the language well?",
     'Kan Ditto helpen als ik de taal niet goed spreek?'),
    ('A6',
     'Yes. Ditto translates medical documents and explanations into language you can understand, helping bridge communication gaps.',
     'Ja. Ditto vertaalt medische documenten en uitleg naar taal die je begrijpt, zodat taalbarrières geen probleem meer zijn.'),
])

add_section_header('Footer')
add_copy_table([
    ('Contact',
     'info@ditto.care | +31 85 115 5421',
     'info@ditto.care | +31 85 115 5421'),
    ('Links',
     'About, Professionals, Privacy, Support, Download App, Press, Contact, Terms & Conditions, Privacy Policy',
     'Over ons, Zorgverleners, Privacy, Ondersteuning, Download App, Pers, Contact, Algemene voorwaarden, Privacybeleid'),
    ('Social',
     'Instagram, LinkedIn',
     'Instagram, LinkedIn'),
    ('Tagline',
     '',
     'Met zorg gemaakt in Nederland'),
])

add_separator()

# ============================================================
# PAGE 2: ABOUT / OUR STORY
# ============================================================
add_page_header('2. ABOUT / OUR STORY')

add_section_header('Opening')
add_copy_table([
    ('Headline',
     'Ditto was born from the belief that healthcare conversations deserve clarity.',
     'Ditto is ontstaan vanuit de overtuiging dat gesprekken over je gezondheid helder horen te zijn.'),
    ('Body',
     "After seeing how often people leave medical appointments confused or overwhelmed, we set out to build something different; a companion that helps you capture, understand, and share what truly matters.",
     'We zagen hoe vaak mensen verward of overweldigd de spreekkamer verlaten. Dus besloten we iets te bouwen dat helpt om vast te leggen, te begrijpen en te delen wat er echt toe doet.'),
    ('Launch info',
     'Ditto app, Launched August 2025',
     'Ditto app, Gelanceerd augustus 2025'),
])

add_section_header('The Mission')
add_copy_table([
    ('Para 1',
     'Across Europe, millions of patients struggle to make sense of medical information and coordinate their care. Consultations are short, health literacy levels are low, and families often support loved ones without the tools to understand diagnoses, treatment plans, or next steps.',
     'In heel Europa hebben miljoenen patiënten moeite om medische informatie te begrijpen en hun zorg te coördineren. Consulten zijn kort, gezondheidsvaardigheden zijn laag, en families ondersteunen hun naasten vaak zonder de middelen om diagnoses, behandelplannen of vervolgstappen te begrijpen.'),
    ('Para 2',
     "Research shows that 40 to 80 percent of medical information is forgotten immediately after a consultation. The more serious the news, the less sticks. And what patients do remember, they pass on to their partner, their children, their parents, each time a little different, a little less precise.",
     'Onderzoek toont aan dat 40 tot 80 procent van medische informatie direct na een consult wordt vergeten. Hoe ernstiger het nieuws, hoe minder er blijft hangen. En wat patiënten wél onthouden, geven ze door aan hun partner, kinderen, ouders, elke keer net iets anders, net iets minder precies.'),
    ('Para 3',
     "Healthcare systems are designed for the providers. Patient portals speak in medical jargon. Records are scattered across hospitals and specialists. And the people who care about you are systematically left out of the information loop.",
     'Zorgsystemen zijn gebouwd voor de zorgverlener. Patiëntportalen spreken in medisch jargon. Dossiers zijn verspreid over ziekenhuizen en specialisten. En de mensen die om je geven, worden systematisch buiten de informatiekring gehouden.'),
    ('Para 4',
     "We thought this could and should be different. Not by fixing the system from the inside, but by building something new on the outside. Something that starts with the patient and the people around them. So we built Ditto.",
     'Wij vonden dat het anders kon en moest. Niet door het systeem van binnenuit te repareren, maar door iets nieuws te bouwen van buitenaf. Iets dat begint bij de patiënt en de mensen eromheen. Dus bouwden we Ditto.'),
])

add_section_header('The Founders')
add_copy_table([
    ('Section label',
     'The same pattern',
     'Hetzelfde patroon'),
    ('Tobias',
     "Tobias went with a friend to the oncologist. His friend was told he had cancer. In the car afterward, they started going over the conversation. What exactly had the doctor said about the prognosis? They couldn't agree. They'd been in the same room, heard the same words, and remembered two different versions.",
     'Tobias ging mee met een vriend naar de oncoloog. Zijn vriend hoorde dat hij kanker had. In de auto daarna begonnen ze het gesprek door te nemen. Wat had de dokter precies gezegd over de prognose? Ze kwamen er niet uit. Ze hadden in dezelfde kamer gezeten, dezelfde woorden gehoord, en twee verschillende versies onthouden.'),
    ('Bart',
     "Bart was diagnosed with type 1 diabetes at thirty. The people around you need to know what to do when your sugar drops too low. Bart tried to explain all of this at home. But what he passed on was already his version. Everyone understood it slightly differently.",
     'Bart kreeg op zijn dertigste de diagnose diabetes type 1. De mensen om je heen moeten weten wat ze moeten doen als je suiker te laag wordt. Bart probeerde dit thuis allemaal uit te leggen. Maar wat hij doorgaf was al zijn versie. Iedereen begreep het net iets anders.'),
    ('Merlijn',
     "Merlijn sees it with his 87-year-old grandmother, who is being treated for lung cancer. She always brings someone to the consultation room. But even that person doesn't remember everything. And what they relay to the rest of the family is already their own version.",
     'Merlijn ziet het bij zijn oma van 87, die behandeld wordt voor longkanker. Ze neemt altijd iemand mee naar de spreekkamer. Maar ook die persoon onthoudt niet alles. En wat die thuis doorvertelt aan de rest van de familie, is al een eigen versie.'),
    ('Closing',
     'Three people, the same pattern. They decided to do something about it.',
     'Drie mensen, hetzelfde patroon. Ze besloten er iets aan te doen.'),
])

add_section_header('The Team')
add_copy_table([
    ('Section headline',
     'Meet the team',
     'Het team'),
    ('Section subheadline',
     'The beating heart of Ditto',
     'Het kloppend hart van Ditto'),
    ('Team intro',
     'A young yet ambitious and experienced team, with little patience for the status quo.',
     'Een jong maar ambitieus en ervaren team, met weinig geduld voor de status quo.'),
    ('Tobias Polak',
     'Strategy/Founder. Built healthtech app and clinical trials at myTomorrows, econometrician, PhD in biostatistics.',
     'Strategie/Oprichter. Bouwde healthtech-app en klinische trials bij myTomorrows, econometrist, PhD in biostatistiek.'),
    ('Merlijn van Breugel',
     'Product/Founder. Built and implemented AI for UMCG and Erasmus University Rotterdam. PhD candidate AI + health.',
     'Product/Oprichter. Bouwde en implementeerde AI voor UMCG en Erasmus Universiteit Rotterdam. Promovendus AI + gezondheid.'),
    ('Bart Voorn',
     "Operations/Founder. Ex-head of R&D in AI & Robotics at Ahold Delhaize, founder STRM: data privacy & security, PhD Eco & Bizz.",
     'Operaties/Oprichter. Voormalig hoofd R&D in AI & Robotics bij Ahold Delhaize, oprichter STRM: data privacy & security, PhD Eco & Bizz.'),
    ('Yury Sukhoverkhov',
     'Engineer/CTO. Computer Scientist. Tech lead myTomorrows, NewMotion. Built largest digital fishing app with 60M+ users.',
     'Engineer/CTO. Informaticus. Tech lead myTomorrows, NewMotion. Bouwde de grootste digitale hengelsport-app met 60M+ gebruikers.'),
    ('Ilayda Kucukosmanoglu',
     "Product/User Experience. Built and led UX at Erasmus MC's Digizorg, shaped complex platforms at global agency DEPT.",
     'Product/User Experience. Bouwde en leidde UX bij Digizorg van het Erasmus MC, vormgaf complexe platformen bij wereldwijd bureau DEPT.'),
])

add_section_header('Careers')
add_copy_table([
    ('Headline',
     'Want to help us build this?',
     'Wil je meehelpen dit te bouwen?'),
    ('Body',
     "Ditto is building something that doesn't exist yet. We're a small team in Rotterdam with a big mission and the traction to match.",
     'Ditto bouwt iets dat nog niet bestaat. We zijn een klein team in Rotterdam met een grote missie en de tractie om het waar te maken.'),
    ('CTA',
     'See open positions',
     'Bekijk onze vacatures'),
])

add_section_header('News / Press')
add_copy_table([
    ('Section headline',
     'Ditto in the News',
     'Ditto in het nieuws'),
    ('Body',
     'Published 20+ times in the news',
     'Meer dan 20 keer in het nieuws verschenen'),
])

add_separator()

# ============================================================
# PAGE 3: PROFESSIONALS
# ============================================================
add_page_header('3. PROFESSIONALS')

add_section_header('Hero')
add_copy_table([
    ('Headline',
     'Care doesn\'t end when the consultation does.',
     'Zorg stopt niet na het consult.'),
    ('Subheadline',
     'Ditto helps your patients understand what was discussed, remember what matters, and share it with their family, so they come back prepared, not confused.',
     'Ditto helpt uw patiënten te begrijpen wat er besproken is, te onthouden wat belangrijk is, en het te delen met hun naasten. Zodat ze de volgende keer voorbereid komen, niet verward.'),
    ('CTA 1',
     'Talk to a fellow doctor',
     'Praat met een collega-arts'),
    ('CTA 2',
     'Get a demo account',
     'Vraag een demo-account aan'),
    ('Trust line',
     '75,000+ patients use Ditto. Recommended by GPs, oncologists, and midwives across the Netherlands.',
     '75.000+ patiënten gebruiken Ditto. Aanbevolen door huisartsen, oncologen en verloskundigen door heel Nederland.'),
])

add_section_header('The Problem (Statistics)')
add_copy_table([
    ('Section headline',
     'Patient recollection directly determines whether your treatment plan succeeds',
     'Wat patiënten onthouden bepaalt of uw behandelplan slaagt'),
    ('Stat 1',
     '40-80% of medical information provided by clinicians is forgotten immediately.\nLangewitz et al. (2021)',
     '40-80% van medische informatie die zorgverleners geven, wordt direct vergeten.\nLangewitz et al. (2021)'),
    ('Stat 2',
     '50% of patients leave consultations with significant misunderstandings about their diagnosis or treatment.\nMakaryus & Friedman (2005)',
     '50% van de patiënten verlaat het consult met serieuze misverstanden over hun diagnose of behandeling.\nMakaryus & Friedman (2005)'),
    ('Stat 3',
     'Informed patients have measurably better treatment adherence and health outcomes.\nStacey et al. (2024)',
     'Goed geïnformeerde patiënten hebben aantoonbaar betere therapietrouw en gezondheidsuitkomsten.\nStacey et al. (2024)'),
    ('Transition',
     "You can't follow your patient home. But the right information can.",
     'U kunt uw patiënt niet naar huis volgen. Maar de juiste informatie wel.'),
])

add_section_header('How Ditto Works')
add_copy_table([
    ('Step 1 title',
     'Your patient records the consultation',
     'Uw patiënt neemt het consult op'),
    ('Step 1 body',
     "The patient opens the Ditto app and taps the record button. Nothing changes for you. No devices to set up, no integrations to configure, no workflow disruption.",
     'De patiënt opent de Ditto-app en drukt op opnemen. Er verandert niets voor u. Geen apparaten om op te zetten, geen integraties, geen verstoring van uw werkwijze.'),
    ('Step 2 title',
     "Ditto turns your conversation into a clear summary, in their preferred language",
     'Ditto zet uw gesprek om in een duidelijke samenvatting, in de taal van de patiënt'),
    ('Step 2 body',
     "Ditto's proprietary patient scribe produces a structured summary. The summary is automatically delivered in your patient's preferred language. Nothing added, nothing assumed. Only what was said in the room, in language your patient can actually understand.",
     'Ditto\'s eigen patiënt-schrijver maakt een gestructureerde samenvatting. De samenvatting wordt automatisch geleverd in de voorkeurstaal van uw patiënt. Niets toegevoegd, niets aangenomen. Alleen wat er gezegd is, in taal die uw patiënt daadwerkelijk begrijpt.'),
    ('Step 3 title',
     'The people caring for your patient get the facts they need',
     'De naasten van uw patiënt krijgen de feiten die ze nodig hebben'),
    ('Step 3 body',
     'The patient shares their summary directly with family and caretakers. Everyone involved in their care gets accurate information straight from the consultation. Fewer calls. Better support. Stronger treatment adherence.',
     'De patiënt deelt de samenvatting direct met familie en mantelzorgers. Iedereen betrokken bij de zorg krijgt accurate informatie, rechtstreeks uit het consult. Minder terugbelvragen. Betere ondersteuning. Sterkere therapietrouw.'),
    ('Step 4 title',
     'Your next appointment starts with progress, not repetition',
     'Uw volgende afspraak begint met voortgang, niet met herhaling'),
    ('Step 4 body',
     'The patient arrives informed, aligned with their family, and ready to move forward. You spend the time progressing, not catching up.',
     'De patiënt komt geïnformeerd, afgestemd met de familie, en klaar om verder te gaan. U besteedt de tijd aan voortgang, niet aan bijpraten.'),
])

add_section_header('Credibility')
add_copy_table([
    ('Section headline',
     'Built with healthcare professionals, not around them',
     'Gebouwd met zorgverleners, niet om hen heen'),
    ('Point 1 title',
     'Doctors on the team',
     'Artsen in het team'),
    ('Point 1 body',
     "Doctors are part of Ditto's core team. They validate summary quality, shape our product, and hold it to the standard you would apply to your own patients.",
     'Artsen maken deel uit van het kernteam van Ditto. Zij valideren de kwaliteit van samenvattingen, geven richting aan ons product en houden het op de standaard die u voor uw eigen patiënten zou hanteren.'),
    ('Point 2 title',
     'Validated with hospitals',
     'Gevalideerd met ziekenhuizen'),
    ('Point 2 body',
     'We work directly with academic hospitals, including UMCG, to validate and improve patient communication and healthcare journeys through technology.',
     'We werken direct samen met academische ziekenhuizen, waaronder het UMCG, om patiëntcommunicatie en zorgtrajecten te valideren en verbeteren met technologie.'),
    ('Point 3 title',
     'Trusted by leading insurers',
     'Vertrouwd door grote verzekeraars'),
    ('Point 3 body',
     'Menzis and CZ, some of the largest health insurers in the Netherlands, partner with Ditto to improve health literacy across their members.',
     'Menzis en CZ, twee van de grootste zorgverzekeraars van Nederland, werken samen met Ditto om gezondheidsvaardigheden onder hun verzekerden te verbeteren.'),
])

add_section_header('Testimonials')
add_copy_table([
    ('Section headline',
     'What your colleagues say',
     'Wat uw collega\'s zeggen'),
    ('Sanne de Vries',
     'Now I can listen back in the evening and explain everything clearly at home. That gives me real peace of mind.',
     'Nu kan ik \'s avonds terugluisteren en thuis alles duidelijk uitleggen. Dat geeft me echt rust.'),
    ('Mark van Dijk',
     "I review my summaries before follow-ups. I feel more prepared and less unsure.",
     'Ik lees mijn samenvattingen door voor controleafspraken. Ik voel me beter voorbereid en minder onzeker.'),
    ('Amina El Idrissi',
     'Ditto helps me understand what the doctor said so I can truly support my father.',
     'Ditto helpt me begrijpen wat de dokter heeft gezegd, zodat ik mijn vader echt kan helpen.'),
    ('Tim Jansen',
     'The letters finally make sense. That alone reduced my anxiety.',
     'De brieven zijn eindelijk begrijpelijk. Dat alleen al verminderde mijn ongerustheid.'),
    ('Talia Meijer',
     'I can revisit the plan and feel ready for what comes next.',
     'Ik kan het plan teruglezen en voel me klaar voor wat er komt.'),
])

add_section_header('Data Handling')
add_copy_table([
    ('Section headline',
     'How we handle patient data',
     'Hoe wij omgaan met patiëntgegevens'),
    ('Point 1',
     "On-device storage: Patient data stays on the patient's device. We cannot read, access, or share patient summaries.",
     'Opslag op het apparaat: Patiëntgegevens blijven op het apparaat van de patiënt. Wij kunnen samenvattingen niet lezen, openen of delen.'),
    ('Point 2',
     'EU servers only: When AI processing is needed, we use secure servers in the European Union.',
     'Alleen EU-servers: Wanneer AI-verwerking nodig is, gebruiken we beveiligde servers in de Europese Unie.'),
    ('Point 3',
     'Immediate deletion: Audio and data are deleted from our servers after processing.',
     'Direct verwijderd: Audio en gegevens worden na verwerking van onze servers verwijderd.'),
    ('Point 4',
     'GDPR compliant: Full compliance with European data protection regulations.',
     'AVG-conform: Volledige naleving van Europese gegevensbeschermingsregels.'),
])

add_section_header('Closing CTA')
add_copy_table([
    ('Headline',
     'Try it out for yourself',
     'Probeer het zelf'),
    ('Body',
     'Request a demo account and try out Ditto now.',
     'Vraag een demo-account aan en probeer Ditto nu.'),
    ('CTA',
     'App Store | Google Play | Get a demo account',
     'App Store | Google Play | Vraag een demo-account aan'),
])

add_section_header('FAQ')
add_copy_table([
    ('Q1',
     'Does Ditto give medical advice?',
     'Geeft Ditto medisch advies?'),
    ('A1',
     "No. Ditto captures what was said during the consultation and presents it in clear language. It doesn't interpret, diagnose, or recommend.",
     'Nee. Ditto legt vast wat er tijdens het consult gezegd is en presenteert het in duidelijke taal. Het interpreteert niet, stelt geen diagnoses en doet geen aanbevelingen.'),
    ('Q2',
     'How do you ensure the summaries are correct?',
     'Hoe zorgen jullie dat de samenvattingen kloppen?'),
    ('A2',
     "We built an extensive AI engine with evaluation and safeguard frameworks. If we suspect any errors in a summary, we don't return output. Our in-house doctors review and validate AI quality.",
     'We hebben een uitgebreide AI-engine gebouwd met evaluatie- en waarborgsystemen. Als we fouten vermoeden in een samenvatting, geven we geen resultaat terug. Onze huisartsen reviewen en valideren de AI-kwaliteit.'),
    ('Q3',
     'Can I access my patient recordings?',
     'Kan ik de opnames van mijn patiënt bekijken?'),
    ('A3',
     "Recordings and summaries are only stored on the device of the patient. They can share it with you directly, either by adding you to their Care Circle or sending it through another channel.",
     'Opnames en samenvattingen worden alleen opgeslagen op het apparaat van de patiënt. Zij kunnen het direct met u delen, door u toe te voegen aan hun Zorgcirkel of via een ander kanaal.'),
    ('Q4',
     'Does it work with all types of consultations?',
     'Werkt het bij alle soorten consulten?'),
    ('A4',
     'Ditto works with any in-person consultation. GP, specialist, midwife, physiotherapist, psychologist.',
     'Ditto werkt bij elk consult in persoon. Huisarts, specialist, verloskundige, fysiotherapeut, psycholoog.'),
    ('Q5',
     'How is patient data handled?',
     'Hoe wordt patiëntdata behandeld?'),
    ('A5',
     "All data stays on the patient's device. When AI processing is needed, we use secure EU servers and delete the data immediately after. We're fully GDPR compliant.",
     'Alle gegevens blijven op het apparaat van de patiënt. Wanneer AI-verwerking nodig is, gebruiken we beveiligde EU-servers en verwijderen de data direct daarna. We voldoen volledig aan de AVG.'),
])

add_separator()

# ============================================================
# PAGE 4: TRUST & PRIVACY
# ============================================================
add_page_header('4. TRUST & PRIVACY')

add_section_header('Hero')
add_copy_table([
    ('Headline',
     'Your health data, your rules.',
     'Jouw gezondheidsdata, jouw regels.'),
    ('Subheadline',
     "Healthcare is deeply personal, and so is the data that comes with it. Ditto is built with a privacy-by-design approach: we can never read or access what you do and store in the app. Here's exactly how it works.",
     'Zorg is diep persoonlijk, en dat geldt ook voor de data die erbij hoort. Ditto is gebouwd met privacy-by-design: wij kunnen nooit lezen of bekijken wat jij doet en opslaat in de app. Hier leggen we precies uit hoe het werkt.'),
])

add_section_header('How Recording Works')
add_copy_table([
    ('Section label',
     'What happens when you tap record',
     'Wat er gebeurt als je op opnemen drukt'),
    ('Step 1',
     "You record your consultation. You open Ditto and tap record. The audio is captured on your phone. Your doctor doesn't need to install anything or change their workflow.",
     'Je neemt je consult op. Je opent Ditto en drukt op opnemen. De audio wordt vastgelegd op je telefoon. Je arts hoeft niets te installeren en verandert niets aan de werkwijze.'),
    ('Step 2',
     'Transcription happens securely in the Netherlands. The audio is sent to NEN-certified Juvoly infrastructure in the Netherlands for transcription.',
     'Transcriptie gebeurt veilig in Nederland. De audio wordt verstuurd naar NEN-gecertificeerde Juvoly-infrastructuur in Nederland voor transcriptie.'),
    ('Step 3',
     'AI generates your summary. The transcribed text is processed on EU-based Azure servers to produce a structured, plain-language summary.',
     'AI maakt je samenvatting. De getranscribeerde tekst wordt verwerkt op Azure-servers in de EU tot een gestructureerde samenvatting in begrijpelijke taal.'),
    ('Step 4',
     "Your data is deleted from our servers. After processing, all audio and transcription data is deleted from our servers. We don't keep it. We can't replay it. It's gone.",
     'Je data wordt verwijderd van onze servers. Na verwerking worden alle audio- en transcriptiegegevens verwijderd van onze servers. We bewaren het niet. We kunnen het niet afspelen. Het is weg.'),
    ('Step 5',
     'Your summary arrives on your device. The summary lives on your phone. It never leaves your device unless you choose to share it.',
     'Je samenvatting komt op je apparaat. De samenvatting staat op je telefoon. Die verlaat je apparaat alleen als jij ervoor kiest om te delen.'),
])

add_section_header('How We Make Summaries')
add_copy_table([
    ('Section label',
     'What goes into the AI behind your summary',
     'Wat er zit achter de AI van je samenvatting'),
    ('Intro',
     "Ditto doesn't just run your recording through a generic AI model. We built a dedicated AI engine designed specifically for medical conversations.",
     'Ditto haalt je opname niet zomaar door een generiek AI-model. We hebben een eigen AI-engine gebouwd, speciaal ontworpen voor medische gesprekken.'),
    ('Structured output',
     'Every summary follows a consistent structure: what was discussed, your diagnosis explained, medications, next steps, and open questions.',
     'Elke samenvatting volgt een vaste structuur: wat er besproken is, je diagnose uitgelegd, medicijnen, vervolgstappen en openstaande vragen.'),
    ('Safeguards',
     "We built extensive evaluation and safeguard frameworks. If our AI is uncertain about something, it won't guess. It will tell you that it cannot reliably provide a summary rather than risk giving you something wrong.",
     'We hebben uitgebreide evaluatie- en waarborgsystemen gebouwd. Als onze AI ergens onzeker over is, gokt die niet. Dan krijg je de melding dat er geen betrouwbare samenvatting gemaakt kan worden, in plaats van iets dat mogelijk niet klopt.'),
    ('Validated',
     'Our in-house doctors review AI output continuously. We collaborate with academic institutions and hospitals to validate quality and accuracy.',
     'Onze huisartsen reviewen de AI-output continu. We werken samen met academische instellingen en ziekenhuizen om kwaliteit en nauwkeurigheid te valideren.'),
])

add_section_header('Data Storage')
add_copy_table([
    ('Section label',
     'Where your data lives',
     'Waar je data leeft'),
    ('Point 1',
     'Everything stays on your device. Your summaries, recordings, documents, and Care Circle updates are stored locally on your phone. Not on a server. Not in a cloud we control.',
     'Alles blijft op je apparaat. Je samenvattingen, opnames, documenten en Zorgcirkel-updates worden lokaal op je telefoon opgeslagen. Niet op een server. Niet in een cloud die wij beheren.'),
    ('Point 2',
     'You control access. Your app is protected by biometric login or passcode. No one, not even us, can access what\'s inside.',
     'Jij bepaalt de toegang. Je app is beveiligd met biometrische login of pincode. Niemand, ook wij niet, kan bij wat erin staat.'),
    ('Point 3',
     "EU servers for processing only. When you record a consultation or scan a document, the data is temporarily sent to secure servers in the EU. After processing, it's deleted.",
     'EU-servers alleen voor verwerking. Als je een consult opneemt of een document scant, wordt de data tijdelijk naar beveiligde servers in de EU gestuurd. Na verwerking wordt alles verwijderd.'),
    ('Point 4',
     "Your backup, your choice. Ditto uses your device's built-in backup (iCloud or Google Drive). We recommend enabling encrypted backups.",
     'Jouw back-up, jouw keuze. Ditto gebruikt de ingebouwde back-up van je apparaat (iCloud of Google Drive). We raden aan om versleutelde back-ups in te schakelen.'),
])

add_section_header('Care Circle Encryption')
add_copy_table([
    ('Section label',
     'How sharing stays private',
     'Hoe delen privé blijft'),
    ('Body',
     "When you share a summary with your Care Circle, it's protected by end-to-end encryption using a protocol similar to Signal. Only you and the people you've invited can read what's shared. Not us. Not anyone in between.",
     'Wanneer je een samenvatting deelt met je Zorgcirkel, is die beschermd met end-to-end-encryptie via een protocol vergelijkbaar met Signal. Alleen jij en de mensen die je hebt uitgenodigd kunnen lezen wat er gedeeld is. Wij niet. Niemand ertussen.'),
    ('Control',
     "You stay in full control of who's in your Care Circle and what they can see. You can add or remove people at any time.",
     'Jij houdt volledige controle over wie er in je Zorgcirkel zit en wat ze kunnen zien. Je kunt op elk moment mensen toevoegen of verwijderen.'),
])

add_section_header('AI Transparency')
add_copy_table([
    ('Section label',
     'How we use AI, and how we keep it safe',
     'Hoe we AI gebruiken, en hoe we het veilig houden'),
    ('What AI does',
     'Transcribes your medical conversation into text. Generates a plain-language summary. Translates medical jargon into everyday language. Explains medical documents you scan.',
     'Transcribeert je medische gesprek naar tekst. Genereert een samenvatting in begrijpelijke taal. Vertaalt medisch jargon naar alledaagse taal. Legt medische documenten uit die je scant.'),
    ('Safety 1',
     "We never train on your data. In fact, we don't even store it after processing.",
     'We trainen nooit op jouw data. Sterker nog, we slaan het niet eens op na verwerking.'),
    ('Safety 2',
     'EU infrastructure only. Transcription happens in the Netherlands via NEN-certified Juvoly. Summaries are generated on EU-based Azure servers.',
     'Alleen EU-infrastructuur. Transcriptie vindt plaats in Nederland via NEN-gecertificeerd Juvoly. Samenvattingen worden gegenereerd op Azure-servers in de EU.'),
    ('Safety 3',
     'Built-in uncertainty. If our AI is uncertain, it tells you, rather than guessing.',
     'Ingebouwde onzekerheid. Als onze AI ergens onzeker over is, meldt die dat, in plaats van te gokken.'),
    ('What AI does NOT do',
     "Ditto does not provide medical advice, recommend treatments, or make decisions about your care. It's a translator, not a doctor.",
     'Ditto geeft geen medisch advies, beveelt geen behandelingen aan en neemt geen beslissingen over je zorg. Het is een vertaler, geen dokter.'),
])

add_section_header('Our Commitments')
add_copy_table([
    ('Section label',
     'What we will never do',
     'Wat we nooit zullen doen'),
    ('Commitment 1',
     'We will never sell your data. Not to insurers. Not to advertisers. Not to anyone.',
     'We zullen nooit je data verkopen. Niet aan verzekeraars. Niet aan adverteerders. Aan niemand.'),
    ('Commitment 2',
     'We will never share data with your insurer. Even if your insurer partners with us, they cannot see your personal health information.',
     'We zullen nooit data delen met je verzekeraar. Ook als je verzekeraar met ons samenwerkt, kunnen zij je persoonlijke gezondheidsinformatie niet zien.'),
    ('Commitment 3',
     "We will never train AI on your recordings. Your conversations are processed and deleted. They don't become training data.",
     'We zullen nooit AI trainen op jouw opnames. Je gesprekken worden verwerkt en verwijderd. Ze worden geen trainingsdata.'),
    ('Commitment 4',
     "We will never access your summaries. They live on your device. We have no technical ability to read them.",
     'We zullen nooit je samenvattingen bekijken. Ze staan op jouw apparaat. We hebben technisch geen mogelijkheid om ze te lezen.'),
])

add_section_header('GDPR / AVG Compliance')
add_copy_table([
    ('Section label',
     'Your rights under EU law',
     'Je rechten onder Europese wetgeving'),
    ('Intro',
     'Ditto is fully compliant with the General Data Protection Regulation (GDPR).',
     'Ditto voldoet volledig aan de Algemene Verordening Gegevensbescherming (AVG).'),
    ('Right 1',
     'Right to access. You can request a copy of any data we hold about you.',
     'Recht op inzage. Je kunt een kopie opvragen van alle gegevens die we over je hebben.'),
    ('Right 2',
     'Right to deletion. You can delete your account and all associated data at any time.',
     'Recht op verwijdering. Je kunt op elk moment je account en alle bijbehorende gegevens verwijderen.'),
    ('Right 3',
     'Right to portability. Your data belongs to you. You can export it whenever you want.',
     'Recht op overdraagbaarheid. Je data is van jou. Je kunt het exporteren wanneer je wilt.'),
    ('DPA',
     'Healthcare professionals and organizations can request a DPA for formal compliance documentation.',
     'Zorgverleners en organisaties kunnen een verwerkersovereenkomst aanvragen voor formele compliancedocumentatie.'),
])

add_section_header('CTA')
add_copy_table([
    ('Headline',
     'Questions about privacy or security?',
     'Vragen over privacy of beveiliging?'),
    ('Body',
     "Reach out to Yury, our CTO, who genuinely loves talking about keeping your data safe. Because clarity shouldn't come at the cost of privacy.",
     'Neem contact op met Yury, onze CTO, die oprecht graag praat over het veilig houden van je data. Want duidelijkheid mag nooit ten koste gaan van privacy.'),
    ('CTA',
     'Talk to Yury',
     'Praat met Yury'),
])

add_separator()

# ============================================================
# PAGE 5: HELP & CONTACT
# ============================================================
add_page_header('5. HELP & CONTACT')

add_section_header('Hero')
add_copy_table([
    ('Headline',
     'We are here for support',
     'We staan voor je klaar'),
    ('Subheadline',
     "Tell us your question or how we can help. We'll get back to you within 1-2 business days.",
     'Stel je vraag of vertel hoe we je kunnen helpen. We reageren binnen 1-2 werkdagen.'),
])

add_section_header('Contact Details')
add_copy_table([
    ('Email', 'info@ditto.care', 'info@ditto.care'),
    ('Phone', '+31 85 115 5421', '+31 85 115 5421'),
    ('WhatsApp', 'WhatsApp us', 'Stuur ons een WhatsApp'),
    ('Address', 'Aert van Nesstraat 45, Rotterdam', 'Aert van Nesstraat 45, Rotterdam'),
])

add_section_header('FAQ — For Patients')
add_copy_table([
    ('Q1',
     'What is Ditto?',
     'Wat is Ditto?'),
    ('A1',
     "Ditto is a free app that helps you understand and manage your healthcare. Record your doctor's visit, get a clear summary in plain language, understand medical letters, and share your health information with the people who matter to you.",
     'Ditto is een gratis app die je helpt je zorg te begrijpen en te organiseren. Neem je doktersbezoek op, krijg een duidelijke samenvatting in begrijpelijke taal, begrijp medische brieven en deel je gezondheidsinformatie met de mensen die ertoe doen.'),
    ('Q2',
     'How do I record a consultation?',
     'Hoe neem ik een consult op?'),
    ('A2',
     "Open Ditto, tap the record button before your appointment starts, and tap stop when it's finished. Within minutes, you'll have a plain-language summary.",
     'Open Ditto, druk op de opnameknop voor je afspraak begint, en druk op stop als het klaar is. Binnen een paar minuten heb je een duidelijke samenvatting.'),
    ('Q3',
     'Do I need my doctor\'s permission to record?',
     'Heb ik toestemming van mijn arts nodig om op te nemen?'),
    ('A3',
     "In the Netherlands, patients have the legal right to record their own medical consultations. We recommend letting your doctor know. Most are supportive, and many already recommend Ditto.",
     'In Nederland hebben patiënten het wettelijke recht om hun eigen medische gesprekken op te nemen. We raden aan om het even te melden bij je arts. De meesten staan er positief tegenover, en veel artsen bevelen Ditto zelf al aan.'),
    ('Q4',
     'How do I share a summary with my family?',
     'Hoe deel ik een samenvatting met mijn familie?'),
    ('A4',
     'Open any summary and tap "Share." You can invite people to your Care Circle. Each person sees what you decide to share with them.',
     'Open een samenvatting en tik op "Delen". Je kunt mensen uitnodigen voor je Zorgcirkel. Elke persoon ziet wat jij besluit te delen.'),
    ('Q5',
     'How much does it cost?',
     'Wat kost het?'),
    ('A5',
     'Ditto is free. No subscriptions, no trial periods, no hidden costs.',
     'Ditto is gratis. Geen abonnementen, geen proefperiodes, geen verborgen kosten.'),
    ('Q6',
     'Is Ditto available in my language?',
     'Is Ditto beschikbaar in mijn taal?'),
    ('A6',
     'Ditto currently works best in Dutch and English. The app can process conversations in other languages.',
     'Ditto werkt momenteel het beste in het Nederlands en Engels. De app kan ook gesprekken in andere talen verwerken.'),
])

add_section_header('FAQ — For Healthcare Professionals')
add_copy_table([
    ('Q1',
     'How does Ditto work in my practice?',
     'Hoe werkt Ditto in mijn praktijk?'),
    ('A1',
     "Patients use Ditto on their own phone. There's nothing to install, integrate, or configure on your end. Your workflow doesn't change.",
     'Patiënten gebruiken Ditto op hun eigen telefoon. U hoeft niets te installeren, integreren of configureren. Uw werkwijze verandert niet.'),
    ('Q2',
     'Is the AI summary accurate?',
     'Is de AI-samenvatting accuraat?'),
    ('A2',
     "Ditto's AI generates summaries that capture the key points in plain language. We collaborate with medical professionals and academic institutions to continuously validate and improve accuracy.",
     'Ditto\'s AI genereert samenvattingen die de kernpunten vastleggen in begrijpelijke taal. We werken samen met medisch professionals en academische instellingen om de nauwkeurigheid continu te valideren en verbeteren.'),
    ('Q3',
     'Do I need to do anything differently?',
     'Moet ik iets anders doen?'),
    ('A3',
     'No. Speak naturally. The AI handles medical terminology, multiple speakers, and varying audio quality.',
     'Nee. Spreek gewoon natuurlijk. De AI verwerkt medische terminologie, meerdere sprekers en wisselende audiokwaliteit.'),
    ('Q4',
     'Can I recommend Ditto to my patients?',
     'Kan ik Ditto aanbevelen aan mijn patiënten?'),
    ('A4',
     "Yes. Many healthcare professionals already do. If you'd like materials, a demo, or want to discuss implementation, talk to our medical team.",
     'Ja. Veel zorgverleners doen dit al. Wilt u materiaal, een demo of wilt u de implementatie bespreken? Neem contact op met ons medisch team.'),
])

add_section_header('FAQ — Privacy & Data')
add_copy_table([
    ('Q1',
     'Where is my data stored?',
     'Waar worden mijn gegevens opgeslagen?'),
    ('A1',
     'On your device. Summaries, documents, and Care Circle connections live on your phone, not on our servers.',
     'Op je apparaat. Samenvattingen, documenten en Zorgcirkel-verbindingen staan op je telefoon, niet op onze servers.'),
    ('Q2',
     'What happens to my audio recording?',
     'Wat gebeurt er met mijn audio-opname?'),
    ('A2',
     "When you record a consultation, the audio is temporarily sent to secure EU servers for processing. After your summary is generated, the audio is deleted. We can't replay it.",
     'Wanneer je een consult opneemt, wordt de audio tijdelijk naar beveiligde EU-servers gestuurd voor verwerking. Na het genereren van je samenvatting wordt de audio verwijderd. We kunnen het niet afspelen.'),
    ('Q3',
     'Can Ditto read my summaries?',
     'Kan Ditto mijn samenvattingen lezen?'),
    ('A3',
     "No. We don't have technical access to your summaries. They're stored on your device, encrypted, and under your control.",
     'Nee. Wij hebben technisch geen toegang tot je samenvattingen. Ze staan versleuteld op je apparaat, onder jouw controle.'),
    ('Q4',
     'Can I delete my data?',
     'Kan ik mijn gegevens verwijderen?'),
    ('A4',
     'Yes. You can delete any summary, recording, or your entire account at any time. Deletion is immediate and permanent.',
     'Ja. Je kunt elke samenvatting, opname of je hele account op elk moment verwijderen. Verwijdering is direct en definitief.'),
    ('Q5',
     'Does my insurer see my data?',
     'Kan mijn verzekeraar mijn gegevens zien?'),
    ('A5',
     'No. Even if your insurer partners with Ditto, they cannot access your personal health information.',
     'Nee. Ook als je verzekeraar samenwerkt met Ditto, kunnen zij niet bij je persoonlijke gezondheidsinformatie.'),
])

add_section_header('Contact Form')
add_copy_table([
    ('Intro',
     "Can't find what you're looking for? We're here to help.",
     'Kun je niet vinden wat je zoekt? We helpen je graag.'),
    ('Field: Name',
     'Your name',
     'Je naam'),
    ('Field: Email',
     'Email address',
     'E-mailadres'),
    ('Field: Type',
     'I am a... [Patient / Healthcare Professional / Partner / Press / Other]',
     'Ik ben een... [Patiënt / Zorgverlener / Partner of organisatie / Pers / Anders]'),
    ('Field: Subject',
     'Subject',
     'Onderwerp'),
    ('Field: Message',
     'Message',
     'Bericht'),
    ('Pro note',
     'Prefer a conversation? Talk to a fellow doctor.',
     'Liever een gesprek? Praat met een collega-arts.'),
])

add_separator()

# ============================================================
# PAGE 6: PRESS
# ============================================================
add_page_header('6. PRESS')

add_section_header('Intro')
add_copy_table([
    ('Body',
     "Up to sixty percent of Dutch people do not remember or properly understand medical information from conversations. This percentage is particularly high in cases of serious diagnoses, low language comprehension, or old age. As a result, unnecessary costs are incurred and treatment outcomes worsen. Ditto, a Rotterdam-based startup, has developed a free app that translates complex medical information into plain language, which can be easily shared with family and friends.",
     'Tot zestig procent van de Nederlanders onthoudt of begrijpt medische informatie uit gesprekken niet goed. Dit percentage is bijzonder hoog bij ernstige diagnoses, laag taalbegrip of hoge leeftijd. Het gevolg: onnodige kosten en slechtere behandelresultaten. Ditto, een Rotterdamse startup, heeft een gratis app ontwikkeld die complexe medische informatie omzet naar begrijpelijke taal, die eenvoudig gedeeld kan worden met familie en vrienden.'),
])

add_section_header('Press Mentions')
add_copy_table([
    ('Publication 1', 'Het Parool (2025)', 'Het Parool (2025)'),
    ('Publication 2', 'Skipr (2025)', 'Skipr (2025)'),
    ('Publication 3', 'Margriet (2025)', 'Margriet (2025)'),
    ('Publication 4', 'Algemeen Dagblad (2025)', 'Algemeen Dagblad (2025)'),
    ('Publication 5', 'Innovation Origins (2025)', 'Innovation Origins (2025)'),
    ('Publication 6', 'Nationale zorggids (2025)', 'Nationale zorggids (2025)'),
    ('Publication 7', 'Hart van Nederland', 'Hart van Nederland'),
    ('Publication 8', 'NOS Radio 1 Journaal', 'NOS Radio 1 Journaal'),
    ('Publication 9', 'NPO Radio 5', 'NPO Radio 5'),
    ('Publication 10', '3FM', '3FM'),
])

add_section_header('Press Contact')
add_copy_table([
    ('Intro',
     'For press inquiries:',
     'Voor persvragen:'),
    ('Email',
     'press@ditto.care',
     'press@ditto.care'),
])

# ============================================================
# SAVE
# ============================================================
output_path = '/Users/merlijnvanbreugel/Documents/GitHub/Ditto/claude-care-clarified/brand/website/Ditto-Website-Copy-EN-NL.docx'
doc.save(output_path)
print(f'Saved to: {output_path}')
