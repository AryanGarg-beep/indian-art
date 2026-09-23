/* ===================================================================
   TIMELINE DATA  —  Assignment 1
   ===================================================================

   This file is a plain JavaScript file, not JSON, on purpose.
   Browsers block fetch() of a local .json file when you open the page
   by double-clicking it (the file:// origin is treated as opaque, so
   the request fails CORS). Declaring the data as a normal <script>
   avoids that entirely, so the site works both by double-click and on
   GitHub Pages with no server. See README.md for the full reasoning.

   TO ADD AN ARTIFACT: copy one block below, change the fields, and
   make sure `era` matches one of the ids in ERAS.

   Field guide
   -----------
   id            unique slug, also the image filename stem
   title         artifact name
   era           which era band it belongs to (must exist in ERAS)
   dateDisplay   human-readable date shown on screen
   dateSort      signed year used ONLY for ordering (negative = BCE)
   region        where it comes from
   medium        material / technique
   attribution   artist or patron; "Unknown" when genuinely unknown
   context       4-6 line historical background
   whyItMatters  single line on its significance
   image / alt   picture and its alt text for screen readers
   credit        image provenance, mirrored into CREDITS.md
   =================================================================== */

/* Era bands, oldest first. `label` appears on the timeline and in the
   filter bar. Keep this array in chronological order. */
const ERAS = [
  { id: "prehistoric", label: "Prehistoric",        span: "c. 10,000 – 2600 BCE" },
  { id: "indus",       label: "Indus Valley",       span: "c. 2600 – 1900 BCE" },
  { id: "mauryan",     label: "Mauryan",            span: "c. 322 – 185 BCE" },
  { id: "gandhara",    label: "Gandhara / Mathura", span: "c. 1st – 3rd c. CE" },
  { id: "gupta",       label: "Gupta",              span: "c. 4th – 6th c. CE" },
  { id: "medieval",    label: "Medieval / Chola",   span: "c. 9th – 13th c. CE" },
  { id: "mughal",      label: "Mughal / Rajput / Pahari", span: "c. 16th – early 19th c." },
  { id: "colonial",    label: "Colonial / Company School", span: "c. 18th – 19th c." },
  { id: "bengal",      label: "Bengal School",      span: "c. 1900 – 1930s" },
  { id: "modern",      label: "Modern",             span: "c. 1930s – 1947" },
  { id: "contemporary",label: "Contemporary",       span: "c. 1930s onward" }
];

const ARTIFACTS = [
  {
    id: "bhimbetka",
    title: "Bhimbetka Rock Shelter Paintings",
    era: "prehistoric",
    dateDisplay: "c. 10,000 BCE onward (Mesolithic and later layers)",
    dateSort: -10000,
    region: "Raisen district, Madhya Pradesh",
    medium: "Natural earth pigments (red ochre, white kaolin) on sandstone rock shelter walls",
    attribution: "Unknown — successive communities of painters",
    context:
      "The Bhimbetka shelters hold one of the longest continuous records of human art anywhere in the world. " +
      "More than 700 shelters sit in the Vindhyan sandstone hills, with several hundred carrying paintings. " +
      "The images were added over an enormous span of time, so a single wall may layer Mesolithic hunting scenes " +
      "beneath later horse-riders and even historic-period figures. Hunters, dancers, animals and community " +
      "processions dominate, drawn in flat silhouette with red and white mineral pigment. Because the layers " +
      "overlap and cannot be radiocarbon-dated directly, individual paintings are dated by style and association " +
      "rather than by a precise year.",
    whyItMatters:
      "It is the starting point of Indian art — evidence that people here were making images tens of thousands of years before cities, temples or writing.",
    image: "images/bhimbetka.jpg",
    alt: "Prehistoric rock painting at Bhimbetka showing red-ochre figures of animals and human hunters on a weathered sandstone shelter wall.",
    credit: {
      title: "Rock Shelter 15, Bhimbetka 02",
      author: "Bernard Gagnon",
      licence: "CC BY-SA 3.0",
      source: "https://commons.wikimedia.org/wiki/File:Rock_Shelter_15,_Bhimbetka_02.jpg"
    }
  },
  {
    id: "dancing-girl",
    title: "Dancing Girl",
    era: "indus",
    dateDisplay: "c. 2500 BCE",
    dateSort: -2500,
    region: "Mohenjo-daro, Sindh (present-day Pakistan)",
    medium: "Bronze, cast by the lost-wax (cire perdue) method",
    attribution: "Unknown Harappan metalworker",
    context:
      "Just 10.5 cm tall, this figure was excavated by Ernest Mackay at Mohenjo-daro in 1926 and is now in the " +
      "National Museum, New Delhi. The girl stands with one hand on her hip and her weight thrown onto one leg, " +
      "her left arm stacked with bangles from shoulder to wrist. The casting is remarkably confident: the " +
      "Harappans were using the lost-wax process, in which a wax model is encased in clay, melted out, and " +
      "replaced by molten bronze. Her identity is unknown — the popular name 'Dancing Girl' is a modern label " +
      "given by archaeologists, not an ancient one, and there is no evidence she was a dancer.",
    whyItMatters:
      "It proves that Indus craftsmen had mastered bronze casting by 2500 BCE, and it remains the most famous single object from the civilisation.",
    image: "images/dancing-girl.jpg",
    alt: "Small bronze statuette of a standing young woman with one hand on her hip and a long stack of bangles on her left arm.",
    credit: {
      title: "Dancing girl of Mohenjo-daro",
      author: "Gary Todd",
      licence: "CC0",
      source: "https://commons.wikimedia.org/wiki/File:Dancing_girl_of_Mohenjo-daro.jpg"
    }
  },
  {
    id: "pashupati",
    title: "Pashupati Seal",
    era: "indus",
    dateDisplay: "c. 2600 – 1900 BCE",
    dateSort: -2350,
    region: "Mohenjo-daro, Sindh (present-day Pakistan)",
    medium: "Carved steatite (soapstone) seal",
    attribution: "Unknown Harappan seal-cutter",
    context:
      "This small steatite seal shows a horned figure seated in a cross-legged posture, surrounded by animals — " +
      "commonly read as an elephant, tiger, rhinoceros and buffalo, with deer below the seat. Sir John Marshall " +
      "named it 'Pashupati' in the 1920s, arguing it was a proto-Shiva as lord of the animals. That reading is " +
      "now heavily debated: other scholars see a buffalo deity, a seated bull-man, or simply a ruler figure. " +
      "Because the Indus script running along the top has never been deciphered, the seal cannot be read, only " +
      "interpreted. Seals like this were probably used to stamp clay tags on traded goods.",
    whyItMatters:
      "It sits at the centre of the biggest unresolved question in Indian art history — whether Harappan religion connects to later Hinduism.",
    image: "images/pashupati.jpg",
    alt: "Impression of a square Indus Valley steatite seal showing a horned seated figure surrounded by animals, with undeciphered script along the top.",
    credit: {
      title: "Pashupati seal impression",
      author: "Ernest John Henry Mackay (1880–1943)",
      licence: "Public domain",
      source: "https://commons.wikimedia.org/wiki/File:Pashupati_seal_impression.jpg"
    }
  },
  {
    id: "lion-capital",
    title: "Lion Capital of Ashoka",
    era: "mauryan",
    dateDisplay: "c. 250 BCE",
    dateSort: -250,
    region: "Sarnath, near Varanasi, Uttar Pradesh",
    medium: "Chunar sandstone with the characteristic Mauryan mirror polish",
    attribution: "Commissioned by the Mauryan emperor Ashoka",
    context:
      "Four lions stand back to back on a drum carved with an elephant, a bull, a horse and a lion, each " +
      "separated by a 24-spoked wheel, the whole resting on an inverted lotus. It originally crowned a polished " +
      "sandstone pillar at Sarnath, the deer park where the Buddha gave his first sermon, and was topped by a " +
      "large stone wheel that no longer survives intact. The extraordinary glassy polish is a Mauryan signature " +
      "that later Indian stone carving never repeated. Ashoka raised such pillars across his empire, inscribing " +
      "them with edicts on dhamma after the Kalinga war.",
    whyItMatters:
      "India adopted it as the State Emblem in 1950, making a 3rd-century-BCE Buddhist sculpture the visual signature of the modern republic.",
    image: "images/lion-capital.jpg",
    alt: "The polished sandstone Lion Capital of Ashoka: four lions standing back to back above a drum carved with animals and wheels.",
    credit: {
      title: "Lion capital of Ashoka, Sarnath",
      author: "lisa bat",
      licence: "CC BY 2.0",
      source: "https://commons.wikimedia.org/wiki/File:Lion_capital_of_Ashoka,_Sarnath.jpg"
    }
  },
  {
    id: "didarganj",
    title: "Didarganj Yakshi",
    era: "mauryan",
    dateDisplay: "c. 3rd century BCE – 2nd century CE (dating disputed)",
    dateSort: -200,
    region: "Didarganj, Patna, Bihar",
    medium: "Polished buff sandstone, roughly life-size",
    attribution: "Unknown",
    context:
      "Found on the bank of the Ganges at Didarganj in 1917, this near life-size female figure holds a fly-whisk " +
      "(chauri) in her raised right hand. She is carved with a heavy, rounded naturalism and finished with the " +
      "high polish usually associated with Mauryan workshops. That polish is the main argument for a 3rd-century " +
      "BCE date. Other scholars point to her jewellery, drapery and modelling as closer to Kushan-period Mathura " +
      "work of the 1st–2nd century CE, and the question is still genuinely open. A yakshi is a nature spirit " +
      "linked to fertility and abundance, a figure type that predates and then feeds into Buddhist, Jain and " +
      "Hindu sculpture alike.",
    whyItMatters:
      "It is a textbook case of how much Indian art history still rests on stylistic argument rather than settled dates.",
    image: "images/didarganj.jpg",
    alt: "Life-size polished sandstone sculpture of a standing woman holding a fly-whisk over her shoulder, wearing heavy jewellery and a draped lower garment.",
    credit: {
      title: "Didarganj Yakshi full length front",
      author: "SuzanneDee",
      licence: "CC BY 3.0",
      source: "https://commons.wikimedia.org/wiki/File:Didarganj_Yakshi_full_length_front.jpg"
    }
  },
  {
    id: "gandhara",
    title: "Standing Buddha, Gandhara",
    era: "gandhara",
    dateDisplay: "c. 2nd – 3rd century CE",
    dateSort: 200,
    region: "Ancient Gandhara (present-day north-west Pakistan and eastern Afghanistan)",
    medium: "Grey schist",
    attribution: "Unknown Gandharan workshop",
    context:
      "Gandhara sat on the trade routes where Indian, Iranian and Graeco-Roman worlds met, and its Buddhist " +
      "sculpture shows it. This standing Buddha wears a heavy monastic robe carved in deep, looping folds that " +
      "descend like a Roman toga, over a body with classically modelled proportions. The face is calm and " +
      "symmetrical, the hair arranged in wavy locks gathered into the ushnisha, the cranial bump marking his " +
      "enlightenment. Alongside Mathura in the Gangetic plain, Gandhara was one of the two schools where the " +
      "Buddha first began to be shown in human form at all — earlier Buddhist art had represented him only " +
      "through symbols such as a footprint, an empty throne or the bodhi tree.",
    whyItMatters:
      "It marks the moment the Buddha acquires a human face, in a style that carried Indian Buddhism along the Silk Road into Central Asia and China.",
    image: "images/gandhara.jpg",
    alt: "Grey schist sculpture of a standing Buddha in a heavily pleated monastic robe, with wavy hair drawn up into a topknot.",
    credit: {
      title: "Standing Buddha, Gandhara, c. 2nd–3rd century AD, gray schist — Matsuoka Museum of Art, Tokyo",
      author: "Daderot",
      licence: "Public domain",
      source: "https://commons.wikimedia.org/wiki/File:Standing_Buddha,_Gandhara,_c._2nd-3rd_century_AD,_gray_schist_-_Matsuoka_Museum_of_Art_-_Tokyo,_Japan_-_DSC07105.JPG"
    }
  },
  {
    id: "ajanta",
    title: "Bodhisattva Padmapani, Ajanta Cave 1",
    era: "gupta",
    dateDisplay: "c. 5th century CE (Vakataka phase)",
    dateSort: 470,
    region: "Ajanta caves, Aurangabad district, Maharashtra",
    medium: "Mineral pigments on a lime-plaster ground, applied to rock-cut cave walls",
    attribution: "Unknown painters; later caves patronised under the Vakataka ruler Harishena",
    context:
      "Ajanta's thirty rock-cut caves were carved in two campaigns, the first around the 2nd century BCE and the " +
      "second in the 5th century CE under Vakataka patronage. The Padmapani on the rear wall of Cave 1 is the " +
      "most reproduced Indian painting of its age: a bodhisattva holding a blue lotus, head inclined, eyes " +
      "lowered in an expression of enormous tenderness. The painters worked in earth and mineral colours over " +
      "plaster, modelling form with tonal shading rather than outline alone. Surrounding walls carry Jataka " +
      "tales, scenes of court life and crowded processions, giving an unusually full picture of contemporary " +
      "dress, ornament and architecture.",
    whyItMatters:
      "Ajanta is the finest surviving body of ancient Indian painting, and the benchmark against which all later Indian mural work is measured.",
    image: "images/ajanta.jpg",
    alt: "Mural painting of the Bodhisattva Padmapani holding a blue lotus, head gently tilted, wearing an elaborate jewelled crown.",
    credit: {
      title: "Ajanta Cave1 Padmapani",
      author: "Ranjan Das2",
      licence: "CC BY-SA 4.0",
      source: "https://commons.wikimedia.org/wiki/File:Ajanta_Cave1_Padmapani.jpg"
    }
  },
  {
    id: "nataraja",
    title: "Shiva as Nataraja, Lord of the Dance",
    era: "medieval",
    dateDisplay: "c. 11th century",
    dateSort: 1050,
    region: "Tamil Nadu",
    medium: "Bronze, cast by the lost-wax method",
    attribution: "Unknown Chola workshop",
    context:
      "The Chola bronze Nataraja compresses an entire cosmology into one figure. Shiva dances inside a ring of " +
      "flame, the arch of fire standing for the universe itself. His upper right hand holds the damaru drum that " +
      "sounds creation; the upper left holds agni, the fire of dissolution. The lower right hand is raised in " +
      "abhaya mudra, the gesture of fearlessness, while the lower left sweeps across the body to point at his " +
      "raised foot, the promise of release. Beneath his right foot he crushes Apasmara, the dwarf of ignorance. " +
      "Such bronzes were made as processional images, carried out of the temple on festival days.",
    whyItMatters:
      "It is the single most recognisable image in Indian art, and the high point of a bronze-casting tradition that Tamil Nadu still practises today.",
    image: "images/nataraja.jpg",
    alt: "Chola bronze of Shiva dancing within a circle of flames, one foot raised and one crushing a small dwarf figure.",
    credit: {
      title: "Shiva as the Lord of Dance (LACMA)",
      author: "Unknown artist; photograph via LACMA",
      licence: "Public domain",
      source: "https://commons.wikimedia.org/wiki/File:Shiva_as_the_Lord_of_Dance_LACMA_edit.jpg"
    }
  },
  {
    id: "konark",
    title: "Chariot Wheel, Konark Sun Temple",
    era: "medieval",
    dateDisplay: "c. 1250 CE",
    dateSort: 1250,
    region: "Konark, Puri district, Odisha",
    medium: "Carved khondalite and laterite stone",
    attribution: "Built under the Eastern Ganga king Narasimhadeva I",
    context:
      "The Konark temple was conceived as the chariot of Surya, the sun god, drawn by seven stone horses and " +
      "riding on twenty-four great wheels carved along its base. Each wheel is about three metres across, with " +
      "spokes, an ornamented hub and a rim covered in medallions of dancers, animals and erotic couples. The " +
      "wheels are often described as working sundials, the shadow of a spoke marking the time of day. The main " +
      "tower (deul) collapsed at some point before the 19th century and the reasons are still argued over, so " +
      "what survives today is mainly the audience hall (jagamohana) and the plinth.",
    whyItMatters:
      "Its wheel became a national symbol — the same form turns on the Indian rupee note and in the Odishan state emblem.",
    image: "images/konark.jpg",
    alt: "Large carved stone chariot wheel on the plinth of the Konark Sun Temple, with decorated spokes and a medallioned hub.",
    credit: {
      title: "Chariot wheel, Konârak 01",
      author: "Bernard Gagnon",
      licence: "CC BY-SA 3.0",
      source: "https://commons.wikimedia.org/wiki/File:Chariot_wheel,_Kon%C3%A2rak_01.jpg"
    }
  },
  {
    id: "mughal",
    title: "Jahangir Preferring a Sufi Shaikh to Kings",
    era: "mughal",
    dateDisplay: "c. 1615 – 18",
    dateSort: 1616,
    region: "Mughal imperial atelier, northern India",
    medium: "Opaque watercolour, gold and ink on paper",
    attribution: "Bichitr",
    context:
      "Bichitr painted the emperor Jahangir seated on an hourglass throne, handing a book not to a king but to " +
      "the Sufi shaikh Husain of the Chishti order. Below the shaikh wait an Ottoman sultan and, in a startling " +
      "touch, King James I of England, copied from an English portrait that had reached the Mughal court. At the " +
      "bottom left the artist has painted himself, holding a miniature showing two horses and an elephant — a " +
      "signature inside the picture. Winged putti borrowed from European prints hover at the edges, and the sand " +
      "in the hourglass runs down as cherubs write that the emperor should live a thousand years.",
    whyItMatters:
      "It shows Mughal painting at its most sophisticated: political allegory, European borrowings and personal signature folded into one page.",
    image: "images/mughal.jpg",
    alt: "Mughal miniature of Emperor Jahangir on an hourglass throne handing a book to a Sufi shaikh, with other rulers waiting below.",
    credit: {
      title: "Bichitr — Jahangir Preferring a Sufi Shaikh to Kings, St Petersburg album (Google Art Project)",
      author: "Bichitr",
      licence: "Public domain",
      source: "https://commons.wikimedia.org/wiki/File:Bichitr_-_Jahangir_Preferring_a_Sufi_Shaikh_to_Kings,_from_the_St._Petersburg_album_-_Google_Art_Project.jpg"
    }
  },
  {
    id: "kangra",
    title: "Companion Persuading Radha as Krishna Plays the Flute",
    era: "mughal",
    dateDisplay: "c. 1820 – 25, from the 'Lambagraon' Gita Govinda series",
    dateSort: 1822,
    region: "Kangra, Himachal Pradesh (Pahari hills)",
    medium: "Opaque watercolour with gold on paper",
    attribution: "Unknown Kangra workshop, in the Guler-Kangra idiom",
    context:
      "Pahari painting grew up in the small hill states of what is now Himachal Pradesh and Jammu, where families " +
      "of painters — many trained in the Mughal manner — worked for local rajas. The Kangra style that matured " +
      "in the later 18th century is the softest of these: cool greens, delicate line, and faces drawn with a " +
      "characteristic straight nose in continuous profile. This folio belongs to a Gita Govinda series, " +
      "illustrating Jayadeva's 12th-century Sanskrit poem about the love of Radha and Krishna. A sakhi, or female " +
      "companion, coaxes the hesitating Radha towards Krishna, whose flute is already sounding in the grove.",
    whyItMatters:
      "Pahari painting turned devotional poetry into intimate, human-scale romance, and is the last great tradition of Indian manuscript painting.",
    image: "images/kangra.jpg",
    alt: "Pahari miniature painting of Radha being encouraged by a female companion in a green grove while Krishna plays a flute nearby.",
    credit: {
      title: "Companion Persuading Radha as Krishna Flutes, folio from the 'Lambagraon' Gita Govinda (LACMA M.71.49.7)",
      author: "Anonymous Kangra artist",
      licence: "Public domain",
      source: "https://commons.wikimedia.org/wiki/File:Companion_Persuading_Radha_as_Krishna_Flutes,_Folio_from_the_%27Lambagraon%27_Gita_Govinda_(Song_of_the_Cowherd)_LACMA_M.71.49.7.jpg"
    }
  },
  {
    id: "ravi-varma",
    title: "There Comes Papa",
    era: "colonial",
    dateDisplay: "1893",
    dateSort: 1893,
    region: "Travancore (Kerala) and Bombay",
    medium: "Oil on canvas",
    attribution: "Raja Ravi Varma (1848 – 1906)",
    context:
      "Ravi Varma was born into an aristocratic family connected to the Travancore court and taught himself to " +
      "paint in oils, a European medium then almost unused in India. In this canvas his daughter Mahaprabha " +
      "stands holding her child, turning as the father approaches from outside the frame. The handling is " +
      "academic and European — modelled flesh, a carefully lit interior, a real sense of weight — but the sari, " +
      "the jewellery and the domestic setting are unmistakably Indian. Later Ravi Varma set up an oleograph press " +
      "so that cheap colour prints of his gods and heroines could reach ordinary households across the country.",
    whyItMatters:
      "He fused European oil technique with Indian subjects, and through mass-produced prints shaped how millions of Indians still picture their gods.",
    image: "images/ravi-varma.jpg",
    alt: "Oil painting of a young Indian woman in a white sari holding a small child, turning towards someone approaching from outside the picture.",
    credit: {
      title: "Raja Ravi Varma, There Comes Papa (1893)",
      author: "Raja Ravi Varma",
      licence: "Public domain",
      source: "https://commons.wikimedia.org/wiki/File:Raja_Ravi_Varma,_There_Comes_Papa_(1893).jpg"
    }
  },
  {
    id: "bharat-mata",
    title: "Bharat Mata",
    era: "bengal",
    dateDisplay: "1905",
    dateSort: 1905,
    region: "Calcutta (Kolkata), Bengal",
    medium: "Watercolour, painted in the wash technique on paper",
    attribution: "Abanindranath Tagore (1871 – 1951)",
    context:
      "Abanindranath painted this small watercolour in the year Bengal was partitioned and the Swadeshi movement " +
      "began. A four-armed woman in saffron robes stands on a pale ground, holding a book, sheaves of rice, a " +
      "white cloth and a rosary — learning, food, clothing and faith, the four things the nation should provide. " +
      "He originally conceived her as Banga Mata, mother Bengal, and the title shifted to Bharat Mata, mother " +
      "India, as the image spread. The soft washes and absence of modelling were deliberate: the Bengal School " +
      "rejected Ravi Varma's European oils in favour of a manner drawn from Mughal, Rajput and Japanese painting.",
    whyItMatters:
      "It gave Indian nationalism its first widely circulated visual icon, and launched the Bengal School as a conscious alternative to colonial academic art.",
    image: "images/bharat-mata.jpg",
    alt: "Watercolour of a serene four-armed woman in saffron robes holding a book, sheaves of rice, a white cloth and a rosary.",
    credit: {
      title: "Bharat Mata by Abanindranath Tagore",
      author: "Abanindranath Tagore",
      licence: "Public domain",
      source: "https://commons.wikimedia.org/wiki/File:Bharat_Mata_by_Abanindranath_Tagore.jpg"
    }
  },
  {
    id: "sher-gil",
    title: "Bride's Toilet",
    era: "modern",
    dateDisplay: "1937",
    dateSort: 1937,
    region: "Painted in Simla (Shimla); artist of Hungarian-Indian parentage",
    medium: "Oil on canvas",
    attribution: "Amrita Sher-Gil (1913 – 1941)",
    context:
      "Sher-Gil trained at the École des Beaux-Arts in Paris and returned to India in 1934 convinced that her " +
      "real subject lay there. 'Bride's Toilet' belongs to the South Indian trilogy she painted in 1937 after " +
      "travelling to Ajanta and the southern temple towns. Women gather around a seated bride in flattened, " +
      "simplified planes of ochre, brown and deep red, their faces grave rather than celebratory. The debt to " +
      "Ajanta's murals and to Gauguin is clear, but the mood is entirely her own — unsentimental, still, and " +
      "attentive to the interior lives of rural women. She died in Lahore in 1941, aged only twenty-eight.",
    whyItMatters:
      "She broke decisively with both colonial academic painting and Bengal School revivalism, and is usually counted the first major Indian modernist.",
    image: "images/sher-gil.jpg",
    alt: "Oil painting of several women in warm ochre and red tones gathered around a seated bride being prepared for her wedding.",
    credit: {
      title: "Amrita Sher-Gil, Bride's Toilet",
      author: "Amrita Sher-Gil",
      licence: "Public domain",
      source: "https://commons.wikimedia.org/wiki/File:Amrita_Sger-Gil_Bride%27s_Toilet.jpg"
    }
  },
  {
    id: "nandalal-bose",
    title: "Dinantika — fresco at Santiniketan",
    era: "contemporary",
    dateDisplay: "c. 1930s – 40s",
    dateSort: 1940,
    region: "Kala Bhavana, Santiniketan, Birbhum district, West Bengal",
    medium: "Fresco on a wall of the Ashram complex",
    attribution: "Nandalal Bose (1882 – 1966)",
    context:
      "Nandalal Bose studied under Abanindranath Tagore and went on to lead Kala Bhavana, the art school at " +
      "Rabindranath Tagore's Santiniketan, from 1922. He pushed Indian art away from studio easel painting and " +
      "back towards murals, craft and everyday rural subject matter, sending students to copy the Ajanta and " +
      "Bagh paintings at first hand. The Santiniketan frescoes were made directly on the buildings students " +
      "lived and worked in, so that art was part of the place rather than hung on its walls. Bose later " +
      "illustrated the manuscript of the Constitution of India and designed emblems for the Indian National " +
      "Congress.",
    whyItMatters:
      "Bose turned Santiniketan into the seedbed of modern Indian art education, teaching a generation to look at India's own visual traditions first.",
    image: "images/nandalal-bose.jpg",
    alt: "Fresco by Nandalal Bose on a wall of the Ashram complex at Santiniketan, showing stylised figures in earth tones.",
    credit: {
      title: "Fresco by Nandalal Bose — Dinantika — Ashram Complex, Santiniketan 01",
      author: "Bodhisattwa",
      licence: "CC BY-SA 4.0",
      source: "https://commons.wikimedia.org/wiki/File:Fresco_by_Nandalal_Bose_-_Dinantika_-_Ashram_Complex_-_Santiniketan_01.jpg"
    }
  }
];
