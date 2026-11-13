/* ===================================================================
   MAP DATA  —  Assignment 2
   ===================================================================

   Like data/artifacts.js this is a .js file rather than .json so the
   page works when opened directly from disk (file:// blocks fetch()).

   TO ADD A PIN: copy one block, change the fields, and make sure
   `category` is one of the ids in CATEGORIES below.

   Field guide
   -----------
   id          unique slug, also the image filename stem
   name        art form name
   state       state / region shown in the detail panel
   category    drives the marker colour and the legend
   lat, lon    decimal degrees; approximate centre of the tradition
   era         when the form originated
   artists     notable practitioners
   works       famous works or typical subjects
   technique   materials and method
   context     short historical paragraph
   image/alt   picture and alt text
   credit      image provenance, mirrored into CREDITS.md
   =================================================================== */

/* Marker categories. `color` is used for both the map pin and the
   legend swatch, so changing it here changes both. */
const CATEGORIES = [
  { id: "folk",    label: "Folk / Tribal",      color: "#b5533c" },
  { id: "court",   label: "Court / Miniature",  color: "#3b4d8f" },
  { id: "temple",  label: "Temple / Devotional", color: "#a67c1a" },
  { id: "modern",  label: "Modern / Urban",     color: "#4f7a5b" }
];

const LOCATIONS = [
  {
    id: "madhubani",
    name: "Madhubani (Mithila) Painting",
    state: "Bihar",
    category: "folk",
    lat: 26.35,
    lon: 86.07,
    era: "Traditionally very old as wall painting; recorded and put on paper from the 1930s",
    artists: "Sita Devi, Ganga Devi, Mahasundari Devi, Bua Devi",
    works: "Kohbar (wedding chamber) murals, Rama-Sita scenes, Durga and Kali images",
    technique: "Natural pigments and rice paste applied with twigs, nib-pens and fingers, on mud walls and later handmade paper",
    context:
      "Madhubani painting comes from the Mithila region of northern Bihar, where women traditionally painted the " +
      "walls and floors of the house for weddings and festivals. The kohbar, painted in the bridal chamber, is " +
      "its most important form. Outsiders first documented the tradition after the 1934 earthquake exposed " +
      "painted interiors, and in the 1960s a government relief effort encouraged artists to transfer the designs " +
      "onto paper, which turned a domestic ritual practice into a widely collected art form.",
    image: "images/madhubani.jpg",
    alt: "Madhubani painting with dense linework and bold natural colours filling the whole surface with figures and patterns.",
    credit: {
      title: "Madhubani painting by Bhuvana Meenakshi",
      author: "Bhuvana Meenakshi",
      licence: "CC BY-SA 3.0",
      source: "https://commons.wikimedia.org/wiki/File:Madhubani_painting_by_Bhuvana_Meenakshi.jpg"
    }
  },
  {
    id: "warli",
    name: "Warli Painting",
    state: "Maharashtra (Palghar / Thane)",
    category: "folk",
    lat: 19.70,
    lon: 73.07,
    era: "Ritual wall painting of long standing; brought to wider notice in the 1970s",
    artists: "Jivya Soma Mashe, Balu Mashe, Anil Vangad",
    works: "Chauk / Lagnachi chauk wedding paintings honouring the goddess Palaghata",
    technique: "White rice-paste pigment applied with a chewed bamboo stick onto a red-ochre mud wall",
    context:
      "The Warli are an Adivasi community of the hills north of Mumbai. Their painting reduces the world to " +
      "circles, triangles and lines: a human figure is two triangles joined at the point, and crowds of these " +
      "figures spiral into hunting scenes, harvests and the tarpa dance. The paintings were made by married " +
      "women for wedding rituals rather than for display. From the early 1970s Jivya Soma Mashe began painting " +
      "outside ritual occasions, and his work carried the style to national and international audiences.",
    image: "images/warli.jpg",
    alt: "Warli painting in white pigment on a red-brown ground showing stick-like human figures dancing and working.",
    credit: {
      title: "Warli painting",
      author: "Omrmankar",
      licence: "CC BY-SA 4.0",
      source: "https://commons.wikimedia.org/wiki/File:Warli_painting.jpg"
    }
  },
  {
    id: "gond",
    name: "Gond Painting",
    state: "Madhya Pradesh (Mandla / Dindori)",
    category: "folk",
    lat: 22.94,
    lon: 81.08,
    era: "Rooted in older wall and floor decoration; emerged as a painting school in the 1980s",
    artists: "Jangarh Singh Shyam, Bhajju Shyam, Durgabai Vyam, Venkat Raman Singh Shyam",
    works: "Depictions of the Gond deity Bada Dev, sacred trees, birds and animals",
    technique: "Originally natural pigments on mud walls; now acrylic and ink on paper and canvas, with surfaces filled by fine dots and dashes",
    context:
      "The Gond are one of India's largest Adivasi communities. Their painting is built from signature infill — " +
      "rows of dots, dashes, commas and fine lines that give every animal and tree a vibrating internal texture. " +
      "The contemporary school is usually traced to Jangarh Singh Shyam, who was noticed in his village in the " +
      "early 1980s and brought to Bharat Bhavan in Bhopal, where he developed the style on paper and canvas. " +
      "The movement he began is sometimes called Jangarh Kalam after him.",
    image: "images/gond.jpg",
    alt: "Gond painting of a stylised animal whose body is filled with rows of fine dots and dashes in bright colours.",
    credit: {
      title: "Gond Painting",
      author: "Roboture",
      licence: "CC BY-SA 3.0",
      source: "https://commons.wikimedia.org/wiki/File:Gond_Painting.JPG"
    }
  },
  {
    id: "phad",
    name: "Phad Painting",
    state: "Rajasthan (Bhilwara / Shahpura)",
    category: "folk",
    lat: 25.35,
    lon: 74.63,
    era: "A scroll-painting tradition several centuries old, associated with the Joshi families of Shahpura",
    artists: "Shree Lal Joshi, Prakash Joshi, Kalyan Joshi",
    works: "Pabuji ki Phad, Devnarayan ki Phad",
    technique: "Vegetable and mineral colours on a long cloth scroll stiffened with starch; figures drawn in profile and filled with flat colour",
    context:
      "A phad is a long painted cloth scroll that serves as a portable temple. Bhopa priest-singers carry it from " +
      "village to village, unrolling it at night and performing the epic of the folk deity Pabuji or Devnarayan " +
      "across many hours, lighting each episode with a lamp as they sing. The composition is not read left to " +
      "right: episodes are placed by importance, with the hero large and central, so the singer navigates the " +
      "cloth rather than following a sequence. Painting the phad has stayed largely within the Joshi families of " +
      "Shahpura.",
    image: "images/phad.jpg",
    alt: "Long Phad cloth scroll densely covered with profile figures, horses and episodes from the epic of Pabuji.",
    credit: {
      title: "Pabuji ki phad",
      author: "Ashoksaranbmr",
      licence: "CC BY-SA 4.0",
      source: "https://commons.wikimedia.org/wiki/File:Pabuji_ki_phad.jpg"
    }
  },
  {
    id: "cheriyal",
    name: "Cheriyal Scroll Painting",
    state: "Telangana (Cheriyal, Siddipet district)",
    category: "folk",
    lat: 17.95,
    lon: 79.02,
    era: "A surviving branch of the Nakashi scroll tradition, documented over several centuries",
    artists: "The Nakashi families of Cheriyal, including D. Vaikuntam and D. Chandraiah",
    works: "Narrative scrolls of the Markandeya Purana, Krishna Leela and caste-community epics",
    technique: "Khadi cloth primed with tamarind-seed paste, rice starch and white clay, then painted in natural pigments against a characteristic red ground",
    context:
      "Cheriyal scrolls were painted for the balladeer communities of Telangana, who used them as visual aids " +
      "while narrating the origin stories of particular castes. A scroll can run many metres, divided into " +
      "horizontal panels read from the top down, each panel in the vivid red that identifies the style at a " +
      "glance. Demand collapsed as film and television replaced travelling storytellers, and the tradition now " +
      "survives with very few practising families, supported by its GI tag and by smaller masks and figures made " +
      "for sale.",
    image: "images/cheriyal.jpg",
    alt: "Cheriyal scroll panel painted on a bright red ground showing figures tapping toddy from palm trees.",
    credit: {
      title: "Cheriyal painting — toddy tappers",
      author: "Subha murugan",
      licence: "CC BY-SA 3.0",
      source: "https://commons.wikimedia.org/wiki/File:Cheriyal_painting_-_toddy_tappers.jpg"
    }
  },
  {
    id: "bhil",
    name: "Bhil / Pithora Painting",
    state: "Madhya Pradesh – Gujarat border (Jhabua, Chhota Udaipur)",
    category: "folk",
    lat: 22.77,
    lon: 74.59,
    era: "Ritual wall painting of long standing among Bhil and Rathwa communities",
    artists: "Bhuri Bai, Lado Bai, Sher Singh Bhil; Pithora work is made by ritual specialists called lakhara",
    works: "Pithora horse murals painted on the inner wall of the house",
    technique: "Natural pigments, and now poster colour, on a mud-plastered wall; surfaces filled with dots of contrasting colour",
    context:
      "A Pithora painting is not decoration but a vow fulfilled. When a household has prayed for a child, a good " +
      "harvest or recovery from illness, a ritual painter is called to cover the front room wall with rows of " +
      "horses carrying the gods, surrounded by figures of daily life. The ceremony that accompanies it matters " +
      "as much as the image. Bhil painters such as Bhuri Bai later moved the idiom onto paper and canvas, and " +
      "her work made the dotted Bhil style widely known beyond the community.",
    image: "images/bhil.jpg",
    alt: "Pithora wall painting showing rows of brightly coloured horses and figures, the surfaces filled with contrasting dots.",
    credit: {
      title: "Pithora art form",
      author: "Sahakol41",
      licence: "CC0",
      source: "https://commons.wikimedia.org/wiki/File:Pithora_art_form.jpg"
    }
  },
  {
    id: "saura",
    name: "Saura (Idital) Painting",
    state: "Odisha (Rayagada, Gajapati)",
    category: "folk",
    lat: 19.17,
    lon: 83.42,
    era: "Ritual wall painting of the Saura Adivasi community",
    artists: "Community ritual painters; individual attribution is rarely recorded",
    works: "Idital / ikon wall paintings made to honour ancestors and deities",
    technique: "White rice paste on a red or ochre mud wall, drawn from the border inwards",
    context:
      "Saura paintings, called idital, are made on house walls to mark a vow, a birth, a harvest or a death, and " +
      "are addressed to ancestors and spirits rather than to viewers. They are often confused with Warli work " +
      "because both use white on earth-red, but the Saura method is distinct: the painter draws the enclosing " +
      "border first and fills the space inwards, producing a dense woven field of stick figures, animals, trees " +
      "and ladders. Horses, elephants and the sun recur, and a priest consecrates the finished image.",
    image: "images/saura.jpg",
    alt: "Saura wall painting in white pigment on a red ground, filled with small stick figures, animals and trees inside a border.",
    credit: {
      title: "Saura painting of Odisha DSCN1052 05",
      author: "Sumita Roy Dutta",
      licence: "CC BY-SA 4.0",
      source: "https://commons.wikimedia.org/wiki/File:Saura_painting_of_Odisha_DSCN1052_05.jpg"
    }
  },
  {
    id: "pahari-kangra",
    name: "Pahari Painting (Basohli · Guler · Kangra)",
    state: "Himachal Pradesh and Jammu hills",
    category: "court",
    lat: 32.10,
    lon: 76.27,
    era: "c. late 17th – early 19th century",
    artists: "Nainsukh of Guler, Manaku, Pandit Seu, Purkhu of Kangra",
    works: "Gita Govinda and Bhagavata Purana series, Rasamanjari sets, Baramasa cycles",
    technique: "Opaque watercolour and gold on paper; Basohli work adds iridescent beetle-wing cases for jewellery",
    context:
      "Pahari painting was produced in the small hill kingdoms of the western Himalaya, where painter families " +
      "moved between courts as patronage shifted. The earlier Basohli manner is hot and stylised, with flat " +
      "planes of red, enormous eyes and inset beetle-wing jewels. Over the 18th century, partly through painters " +
      "trained in Mughal naturalism such as Nainsukh, the style cooled into the lyrical Guler-Kangra idiom of " +
      "soft greens, fine line and delicate profiles. Its subject matter is overwhelmingly Krishna devotion and " +
      "Sanskrit love poetry.",
    image: "images/pahari-kangra.jpg",
    alt: "Pahari miniature in the Basohli manner showing Raja Mednipal seated and smoking a huqqa against a flat coloured ground.",
    credit: {
      title: "Raja Mednipal of Basohli smoking huqqa",
      author: "Unknown artist",
      licence: "CC BY-SA 4.0",
      source: "https://commons.wikimedia.org/wiki/File:Raja_Mednipal_of_Basohli_smoking_huqqa.jpg"
    }
  },
  {
    id: "mughal-delhi",
    name: "Mughal Miniature Painting",
    state: "Delhi and Agra (imperial ateliers)",
    category: "court",
    lat: 27.18,
    lon: 78.02,
    era: "c. mid-16th – 18th century",
    artists: "Basawan, Daswanth, Govardhan, Abu'l Hasan, Bichitr, Mansur",
    works: "Hamzanama, Akbarnama, Padshahnama, Jahangir's albums of birds and animals",
    technique: "Opaque watercolour, ink and gold on paper, often with several specialists sharing one page",
    context:
      "The Mughal atelier began when Humayun brought Persian masters back from Safavid Iran, and it grew under " +
      "Akbar into a large workshop where Persian, Indian and, increasingly, European conventions were combined. " +
      "Pages were frequently collaborative — one artist set the composition, another painted faces, a third the " +
      "colouring — and the names were recorded in the margin. Under Jahangir the scale shifted from crowded " +
      "narrative to close observation: portraits, and natural-history studies of birds and animals by painters " +
      "such as Mansur. Shah Jahan's reign brought a cooler, more formal court manner.",
    image: "images/mughal-delhi.jpg",
    alt: "Mughal miniature showing Abu'l Fazl presenting the Akbarnama manuscript to Emperor Akbar at court.",
    credit: {
      title: "Abu'l Fazl presenting the Akbarnama to Akbar",
      author: "Govardhan",
      licence: "Public domain",
      source: "https://commons.wikimedia.org/wiki/File:AbulFazlPresentingAkbarnama.jpg"
    }
  },
  {
    id: "bikaner",
    name: "Bikaner Miniature Painting",
    state: "Rajasthan (Bikaner)",
    category: "court",
    lat: 28.02,
    lon: 73.31,
    era: "c. 17th – 18th century",
    artists: "Ali Raza, Ruknuddin, Nathu, Ustad Murad",
    works: "Ragamala sets, Bhagavata Purana illustrations, royal portraits",
    technique: "Opaque watercolour and gold on paper, in a refined palette of muted greens, greys and pinks",
    context:
      "Bikaner sits apart from the other Rajput schools because its workshop was staffed by Muslim painter " +
      "families, the Ustas, many of whom had worked in or trained under the Mughal atelier at Delhi. The result " +
      "is a Rajasthani school with unusually Mughal manners: softer modelling, subtler colour and a taste for " +
      "delicate landscape backgrounds, rather than the flat saturated planes of Mewar or Bundi. Painters here " +
      "often signed and dated their work on the reverse, which makes Bikaner one of the better-documented Rajput " +
      "schools.",
    image: "images/bikaner.jpg",
    alt: "Bikaner miniature painting of Ragini Bilawal, a courtly female figure rendered in soft muted colours.",
    credit: {
      title: "Ragini Bilawal, 1700 CE, Bikaner Kalam of Rajasthani School of Art, State Museum, Lucknow",
      author: "SpeakingArch",
      licence: "CC BY-SA 4.0",
      source: "https://commons.wikimedia.org/wiki/File:Ragini_Bilawal,_1700_CE,_Bikaner_Kalam_of_Rajasthani_School_of_Art,_State_Museum,_Lucknow.jpg"
    }
  },
  {
    id: "kalamkari",
    name: "Kalamkari (Srikalahasti style)",
    state: "Andhra Pradesh (Srikalahasti; block-printed variant at Machilipatnam)",
    category: "temple",
    lat: 13.75,
    lon: 79.70,
    era: "Temple cloth tradition of long standing; the two styles diverged under different patronage",
    artists: "J. Gurappa Chetty, and the temple-cloth painter families of Srikalahasti",
    works: "Temple hangings of the Ramayana, Mahabharata and Puranic cycles",
    technique: "Cotton treated with myrobalan and buffalo milk, drawn freehand with a bamboo kalam, coloured with vegetable dyes and fixed by repeated washing",
    context:
      "Kalamkari means 'pen work'. The Srikalahasti style is entirely hand-drawn and grew up serving temples, " +
      "producing large narrative cloths hung behind deities and used to illustrate recitations of the epics. The " +
      "separate Machilipatnam style, shaped by Persian and export demand, is block-printed and more ornamental. " +
      "The process is slow and chemical-free: the cloth is prepared with myrobalan and milk so the dyes bite, " +
      "then washed many times between colours, with red from madder and blue from indigo.",
    image: "images/kalamkari.jpg",
    alt: "Kalamkari cloth painting with hand-drawn deities and dense floral borders in natural madder red, indigo and ochre.",
    credit: {
      title: "Kalamkari painting",
      author: "Anilbhardwajnoida",
      licence: "CC BY-SA 3.0",
      source: "https://commons.wikimedia.org/wiki/File:Kalamkari_painting.jpg"
    }
  },
  {
    id: "pattachitra",
    name: "Pattachitra",
    state: "Odisha (Raghurajpur, Puri)",
    category: "temple",
    lat: 19.87,
    lon: 85.83,
    era: "Closely tied to the Jagannath temple at Puri; documented over several centuries",
    artists: "The chitrakara families of Raghurajpur and Dandasahi",
    works: "Anasara Patti of Jagannath, Balabhadra and Subhadra; Krishna Leela and Dasavatara panels",
    technique: "Cloth layered with tamarind-seed paste and chalk to make a patta, painted in mineral and vegetable colour, then lacquered",
    context:
      "Pattachitra serves the Jagannath temple directly. During Anasara, the fortnight when the three deities are " +
      "hidden from view after their ritual bath, painted pattas stand in their place for worshippers. The style " +
      "is rigorously outlined, with elongated eyes, sharp noses and elaborate floral borders framing every panel. " +
      "Painters belong to hereditary chitrakara families, concentrated in the village of Raghurajpur near Puri, " +
      "where the same households also paint palm leaf, masks and painted toys.",
    image: "images/pattachitra.jpg",
    alt: "Odisha Pattachitra panel with sharply outlined figures, elongated eyes and a dense decorative floral border.",
    credit: {
      title: "Mathura Vijay — Pattachitra of Odisha",
      author: "Rajeshjena453",
      licence: "CC BY-SA 4.0",
      source: "https://commons.wikimedia.org/wiki/File:Mathura_Vijay_-_Pattachitra_of_Odisha.jpg"
    }
  },
  {
    id: "tanjore",
    name: "Thanjavur (Tanjore) Painting",
    state: "Tamil Nadu (Thanjavur)",
    category: "temple",
    lat: 10.79,
    lon: 79.14,
    era: "c. 18th – 19th century, under Maratha rule at Thanjavur",
    artists: "The Raju communities of Thanjavur and Trichy, and Naidu painters of Madurai",
    works: "Devotional panels of the infant Krishna, Rama pattabhishekam, Lakshmi and Murugan",
    technique: "Gesso relief built up on a wood-backed cloth panel, covered with 22-carat gold foil and set with glass or semi-precious stones",
    context:
      "A Tanjore painting is as much relief as painting. The artist builds raised gesso for crowns, pillars, " +
      "arches and jewellery, lays gold foil over it and inlays glass stones, so the surface catches lamplight in " +
      "a dim shrine. Figures are frontal, round-faced and almond-eyed, usually set within an arched niche with " +
      "attendant deities. The style developed under the Maratha rulers of Thanjavur in the 18th century and was " +
      "made for household worship as much as for temples; it holds a GI tag today.",
    image: "images/tanjore.jpg",
    alt: "Thanjavur painting of a deity in an arched niche, with raised gesso and gold foil ornament and inset glass stones.",
    credit: {
      title: "Thanjavur Painting",
      author: "Dr. M. Muthukrishnan",
      licence: "CC BY-SA 3.0",
      source: "https://commons.wikimedia.org/wiki/File:Thanjavur_Painting.jpg"
    }
  },
  {
    id: "mysore",
    name: "Mysore Painting",
    state: "Karnataka (Mysuru)",
    category: "temple",
    lat: 12.30,
    lon: 76.64,
    era: "c. 17th – 19th century, under Wodeyar patronage",
    artists: "Court painters of the Wodeyar dynasty; the tradition traces itself to the Vijayanagara school",
    works: "Devotional panels of Vishnu, Shiva, Ganesha and the goddess Chamundeshwari",
    technique: "Paper laid on wood, with low gesso relief and thin gold leaf, painted in delicate vegetable and mineral colours",
    context:
      "Mysore painting shares an ancestry with Tanjore work — both descend from the painting of the Vijayanagara " +
      "empire after its fall in 1565 scattered artists southwards — but it is noticeably more restrained. The " +
      "gesso relief is low and the gold thinner, so the effect is delicate rather than jewelled, and more " +
      "attention goes to fine modelling of faces, drapery and expression. The Wodeyar rulers of Mysore sustained " +
      "the school, and Krishnaraja Wodeyar III in the 19th century was an especially active patron.",
    image: "images/mysore.jpg",
    alt: "Mysore-style devotional painting of a deity with fine gold detailing and delicately modelled features.",
    credit: {
      title: "Cheluvarayaswamy",
      author: "Subha murugan",
      licence: "CC BY-SA 3.0",
      source: "https://commons.wikimedia.org/wiki/File:Cheluvarayaswamy.jpg"
    }
  },
  {
    id: "kalighat",
    name: "Kalighat Painting",
    state: "West Bengal (Kalighat, Kolkata)",
    category: "modern",
    lat: 22.52,
    lon: 88.34,
    era: "c. 19th – early 20th century",
    artists: "The patua (chitrakar) painters who worked around the Kalighat temple",
    works: "Deity images sold to pilgrims; satirical sheets such as the Tarakeswar affair and the 'Babu' series",
    technique: "Watercolour on cheap mill-made paper, painted with rapid sweeping brushstrokes and bold shaded outlines",
    context:
      "Patua scroll painters moving into colonial Calcutta set up near the Kalighat temple and began selling " +
      "single-sheet paintings to pilgrims. To work fast and cheaply they abandoned the detail of scroll painting " +
      "for broad, confident brushstrokes and flat shaded forms. Alongside Kali and Krishna they painted the city " +
      "itself, mocking the westernised 'babu' with his hookah and mistress, and illustrating scandals of the day. " +
      "Cheap printing eventually undercut them, but the style's economy of line was admired by later artists — " +
      "Jamini Roy built much of his mature work on it.",
    image: "images/kalighat.jpg",
    alt: "Kalighat painting of Radha and Krishna rendered in bold sweeping brushstrokes with flat shaded colour on plain paper.",
    credit: {
      title: "Radha-Krishna, Kalighat Painting",
      author: "Rajan Guptta",
      licence: "CC0",
      source: "https://commons.wikimedia.org/wiki/File:Radha-_Krishna,_Kalighat_Painting.jpg"
    }
  }
];
