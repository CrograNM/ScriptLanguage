class City:
  def __init__(self, name, x, y, index=0):
    self.name = name
    self.x, self.y = x, y
    self.index = index
  def __repr__(self):
    return '%s(%d:%3d,%3d)' % (self.name, self.index, self.x, self.y)

five_letter_cities = [
  City("Clean", 1336, 536),
  City("Prosy", 977, 860),
  City("Rabbi", 6, 758),
  City("Addle", 222, 261),
  City("Smell", 1494, 836),
  City("Quite", 905, 345),
  City("Lives", 72, 714),
  City("Cross", 23, 680),
  City("Synth", 1529, 785),
  City("Tweak", 1046, 426),
  City("Medic", 1485, 514),
  City("Glade", 660, 476),
  City("Breve", 1586, 448),
  City("Hotel", 1269, 576),
  City("Toing", 398, 561),
  City("Scorn", 617, 373),
  City("Tweet", 1253, 403),
  City("Zilch", 1289, 29),
  City("React", 296, 659),
  City("Fiche", 787, 278),
  City("Stunt", 1123, 699),
  City("Swing", 1113, 156),
  City("Merry", 1002, 231),
  City("Brine", 431, 53),
  City("Miter", 126, 609),
  City("Withy", 936, 432),
  City("Brink", 1336, 404),
  City("Madly", 1487, 104),
  City("Spicy", 130, 498),
  City("Cleft", 425, 506),
  City("Cheep", 1511, 604),
  City("Grief", 659, 683),
  City("Links", 529, 850),
  City("Write", 1345, 271),
  City("Fixed", 434, 772),
  City("Yobbo", 920, 848),
  City("Grave", 868, 577),
  City("Cress", 869, 678),
  City("Ensue", 1209, 877),
  City("Imply", 1544, 390),
  City("Datum", 796, 235),
  City("Quoit", 1281, 379),
  City("Twain", 1220, 488),
  City("Allow", 1192, 401),
  City("Kiosk", 1131, 611),
  City("Wheat", 1044, 133),
  City("Birch", 1240, 519),
  City("Flail", 1415, 72),
  City("Thong", 190, 385),
  City("Bongo", 528, 455),
  City("Quilt", 800, 365),
  City("Satyr", 1315, 172),
  City("Alibi", 133, 245),
  City("Auger", 442, 866),
  City("Event", 218, 174),
  City("Scowl", 206, 61),
  City("Shelf", 928, 242),
  City("Melon", 527, 416),
  City("Scrap", 471, 625),
  City("Drupe", 880, 13),
  City("Nadir", 1163, 145),
  City("Kudos", 1426, 806),
  City("Pushy", 14, 429),
  City("Bases", 742, 531),
  City("Atone", 1037, 630),
  City("Knife", 1025, 879),
  City("Seise", 377, 257),
  City("Odour", 614, 553),
  City("Venom", 481, 676),
  City("Filmy", 943, 53),
  City("Barre", 88, 9),
  City("Davit", 28, 271),
  City("Smart", 952, 279),
  City("Canon", 1426, 519),
  City("Dixie", 699, 698),
  City("Pease", 925, 716),
  City("Adorn", 1132, 414),
  City("Liver", 1371, 238),
  City("Druid", 1389, 689),
  City("Baked", 1573, 774),
  City("Tulip", 915, 636),
  City("Unzip", 941, 763),
  City("Nervy", 1083, 385),
  City("Hubby", 1297, 588),
  City("Sweat", 764, 389),
  City("Scald", 1536, 186),
  City("Deity", 1098, 515),
  City("Nutty", 1308, 65),
  City("Mourn", 1111, 550),
  City("Unbar", 566, 422),
  City("Logic", 124, 105),
  City("Stage", 620, 332),
  City("Sisal", 784, 623),
  City("Curvy", 182, 555),
  City("Issue", 1413, 451),
  City("Pilot", 1092, 660),
  City("Wrote", 30, 217),
  City("Quiff", 525, 148),
  City("Willy", 1311, 887),
  City("Plate", 1228, 353),
  City("Nobel", 54, 68),
  City("Chubb", 1155, 838),
  City("Banjo", 467, 563),
  City("Dirge", 86, 535),
  City("Audit", 32, 630),
  City("Rosin", 739, 766),
  City("Scrag", 1386, 16),
  City("Papal", 1565, 828),
  City("Ducky", 868, 264),
  City("Creed", 1301, 786),
  City("Thief", 883, 415),
  City("Pinko", 479, 534),
  City("Hairy", 1101, 35),
  City("Cobra", 671, 405),
  City("Waken", 1478, 230),
  City("Chime", 1343, 834),
  City("Cower", 647, 97),
  City("Whelp", 972, 447),
  City("Milky", 327, 334),
  City("Fauna", 716, 151),
  City("Carob", 233, 411),
  City("Locum", 486, 431),
  City("Month", 1017, 381),
  City("Check", 329, 830),
  City("Dicey", 1286, 739),
  City("Debit", 1528, 248),
  City("Women", 216, 294),
  City("Calve", 1306, 540),
  City("Weepy", 204, 715),
  City("Crash", 77, 120),
  City("Durex", 97, 178),
  City("Ovoid", 809, 28),
  City("Aside", 354, 205),
  City("Blame", 123, 551),
  City("Stela", 248, 828),
  City("Humph", 888, 139),
  City("Amino", 594, 494),
  City("Smash", 576, 702),
  City("Sorry", 64, 218),
  City("Muzzy", 1458, 739),
  City("Camel", 1168, 460),
  City("Sales", 1221, 19),
  City("Biddy", 717, 594),
  City("Indue", 1222, 414),
  City("Jural", 1366, 204),
  City("Tress", 1339, 366),
  City("Egret", 179, 104),
  City("Error", 1205, 547),
  City("Ogive", 851, 719),
  City("Frizz", 357, 152),
  City("Quern", 1187, 204),
  City("Divvy", 194, 886),
  City("Style", 1137, 804),
  City("Silky", 1592, 731),
  City("Elver", 902, 886),
  City("Strum", 1462, 398),
  City("Sweep", 1437, 562),
  City("Taste", 142, 403),
  City("Largo", 794, 870),
  City("There", 1036, 589),
  City("Doric", 487, 266),
  City("Slick", 610, 705),
  City("Waive", 1536, 294),
  City("Rejig", 729, 360),
  City("Comet", 663, 136),
  City("Punch", 347, 896),
  City("Frill", 232, 751),
  City("Dolby", 898, 597),
  City("Saver", 1075, 694),
  City("Brash", 1135, 268),
  City("Sepoy", 195, 430),
  City("Nippy", 842, 89),
  City("Batty", 50, 190),
  City("Unite", 1295, 460),
  City("Promo", 1002, 705),
  City("Towel", 692, 13),
  City("Facia", 1581, 35),
  City("Digit", 658, 26),
  City("Ripen", 398, 445),
  City("Sylph", 1177, 683),
  City("Softy", 472, 391),
  City("Radio", 159, 633),
  City("Aback", 1490, 351),
  City("Afore", 125, 772),
  City("Sedan", 274, 798),
  City("Ghyll", 698, 630),
  City("Tying", 903, 794),
  City("Mulch", 958, 209),
  City("Caber", 174, 584),
  City("Ghost", 82, 315),
  City("Sheaf", 1547, 744),
  City("Elfin", 1175, 361),
  City("Squad", 340, 603),
  City("Patch", 1057, 836),
  City("Ester", 734, 281),
  City("Roger", 145, 436),
  City("Newel", 266, 193),
  City("Tokay", 1296, 240),
  City("Hydro", 1465, 190),
  City("Tutti", 748, 109),
  City("Infer", 76, 860),
  City("Widow", 698, 437),
  City("Hives", 1501, 417),
  City("Inure", 831, 443),
  City("Globe", 540, 553),
  City("Cobol", 191, 679),
  City("Annex", 514, 753),
  City("Stout", 856, 367),
  City("Ovary", 640, 761),
  City("Wormy", 779, 427),
  City("Pique", 57, 787),
  City("Empty", 503, 478),
  City("Snowy", 823, 569),
  City("Oxbow", 104, 353),
  City("Cinch", 21, 860),
  City("Plumy", 434, 110),
  City("Piety", 305, 46),
  City("Craft", 1014, 149),
  City("Fetch", 1121, 217),
  City("Mosey", 699, 564),
  City("Sense", 952, 696),
  City("Tease", 1326, 324),
  City("Handy", 625, 48),
  City("Gismo", 1, 571),
  City("Ditty", 1241, 896),
  City("Coypu", 1270, 489),
  City("Lunch", 1341, 118),
  City("Screw", 338, 744),
  City("Pager", 546, 626),
  City("Ferry", 1564, 93),
  City("Kinky", 331, 490),
  City("Owlet", 1105, 440),
  City("Guess", 912, 2),
  City("Whisk", 465, 823),
  City("Epoch", 287, 153),
  City("Coney", 1433, 482),
  City("Flour", 267, 525),
  City("Spout", 328, 223),
  City("Awoke", 639, 282),
  City("Gnash", 467, 121),
  City("Dinky", 701, 850),
  City("Manic", 913, 385),
  City("Nacho", 932, 469),
  City("Rerun", 991, 780),
  City("Serge", 1446, 442),
  City("Flier", 1194, 849),
  City("Waltz", 1570, 253),
  City("Pubis", 1075, 761),
  City("Shove", 1014, 822),
  City("Bossa", 963, 410),
  City("Swath", 376, 478),
  City("Mousy", 526, 105),
  City("Pivot", 1187, 769),
  City("Frock", 1067, 16),
  City("Muzak", 136, 23),
  City("Bogie", 1272, 288),
  City("Tenet", 1011, 428),
  City("Impel", 77, 480),
  City("Ahead", 1313, 206),
  City("Stuck", 1294, 695),
  City("Rural", 223, 495),
  City("Judge", 321, 407),
  City("Pommy", 644, 611),
  City("Papaw", 1416, 714),
  City("Senna", 273, 256),
  City("Testa", 608, 437),
  City("Slash", 564, 342),
  City("Unity", 885, 53),
  City("Roost", 1394, 512),
  City("Dhoti", 1043, 319),
  City("Solid", 1569, 196),
  City("Dicky", 1223, 693),
  City("Crier", 671, 644),
  City("Seven", 590, 262),
  City("Stick", 1531, 429),
  City("Curse", 293, 756),
  City("Haiku", 1026, 469),
  City("Laver", 212, 609),
  City("Amuse", 1281, 433),
  City("Store", 711, 485),
  City("Union", 961, 497),
  City("Build", 1530, 535),
  City("Knurl", 921, 319),
  City("Rough", 706, 396),
  City("Anion", 560, 268),
  City("Nappy", 124, 215),
  City("Solve", 821, 330),
  City("Halal", 878, 185),
  City("Assay", 414, 385),
  City("Stile", 739, 642),
  City("Bunny", 663, 566),
  City("Ember", 38, 303),
  City("Baron", 1470, 554),
  City("Sauce", 531, 51),
  City("Boost", 511, 517),
  City("Spoof", 420, 632),
  City("Ledge", 1365, 322),
  City("Jolly", 768, 78),
  City("Swift", 1539, 40),
  City("Krone", 311, 793),
  City("Fecal", 803, 156),
  City("Badge", 359, 828),
  City("Fusty", 889, 852),
  City("Tumid", 1116, 292),
  City("Leger", 1543, 872),
  City("Waver", 768, 332),
  City("Folly", 1396, 102),
  City("Islam", 991, 57),
  City("Squid", 1347, 652),
  City("Fuzzy", 484, 16),
  City("Hammy", 1552, 591),
  City("Ducks", 354, 548),
  City("Tongs", 217, 143),
  City("Final", 1464, 9),
  City("Foray", 454, 737),
  City("Femme", 164, 868),
  City("Groan", 1541, 121),
  City("Vapid", 489, 882),
  City("Iliac", 775, 24),
  City("Crest", 1110, 786),
  City("Skull", 143, 716),
  City("Drive", 110, 470),
  City("Melba", 351, 690),
  City("Dingy", 1435, 126),
  City("Wrack", 955, 825),
  City("Emery", 616, 786),
  City("Lucky", 1083, 107),
  City("Savoy", 584, 748),
  City("Trawl", 802, 501),
  City("Zebra", 938, 130),
  City("Tepid", 1360, 485),
  City("Thick", 612, 91),
  City("Objet", 270, 724),
  City("Gouda", 1145, 750),
  City("Sleep", 284, 104),
  City("Downy", 134, 326),
  City("Twine", 959, 557),
  City("Penal", 1154, 553),
  City("Owner", 504, 175),
  City("Tangy", 852, 863),
  City("Yield", 288, 898),
  City("Mimic", 1111, 884),
  City("Craze", 686, 512),
  City("Dalai", 1049, 55),
  City("Brand", 164, 823),
  City("Wreak", 1599, 222),
  City("Cameo", 301, 303),
  City("Trump", 1034, 549),
  City("Oakum", 568, 198),
  City("Scrim", 38, 739),
  City("Stray", 34, 898),
  City("Clung", 259, 878),
  City("Winch", 472, 321),
  City("Brawl", 546, 718),
  City("Crake", 471, 459),
  City("Ducal", 1460, 59),
  City("Gunny", 1364, 417),
  City("Lapis", 411, 728),
  City("Serum", 233, 680),
  City("Split", 1115, 63),
  City("Soggy", 1025, 31),
  City("Fiend", 411, 137),
  City("Taffy", 617, 890),
  City("Crave", 1277, 630),
  City("Lorry", 1528, 81),
  City("Lurex", 1266, 348),
  City("Seamy", 363, 413),
  City("Polio", 607, 832),
  City("Pools", 635, 511),
  City("Jehad", 881, 522),
  City("Cumin", 35, 542),
  City("Hooch", 461, 595),
  City("Humor", 428, 536),
  City("Boron", 1322, 493),
  City("Hippo", 1392, 627),
  City("Axiom", 607, 407),
  City("Spool", 355, 105),
  City("Loyal", 179, 739),
  City("Sumac", 47, 657),
  City("Shalt", 437, 412),
  City("Treat", 825, 205),
  City("Taunt", 1415, 414),
  City("Mayor", 964, 380),
  City("Gripe", 1204, 586),
  City("Hedge", 1028, 665),
  City("Hajji", 1349, 745),
  City("Spank", 266, 609),
  City("Abaft", 1512, 150),
  City("Hunch", 633, 162),
  City("Swizz", 552, 486),
  City("Bravo", 699, 342),
  City("Nifty", 1057, 525),
  City("Jihad", 992, 553),
  City("Heart", 1155, 34),
  City("Renal", 668, 263),
  City("Curly", 782, 827),
  City("Track", 14, 48),
  City("Hello", 280, 851),
  City("Creek", 1040, 699),
  City("Maybe", 463, 52),
  City("Resat", 237, 371),
  City("Mealy", 809, 699),
  City("Valid", 136, 372),
  City("Aster", 1443, 777),
  City("Umbra", 1380, 555),
  City("April", 647, 197),
  City("Ethos", 1205, 294),
  City("Canal", 498, 349),
  City("Fleck", 322, 152),
  City("Could", 1160, 72),
  City("Messy", 850, 153),
  City("Honey", 1172, 803),
  City("Litre", 943, 597),
  City("Grist", 1365, 709),
  City("Whore", 841, 396),
  City("Paten", 1159, 398),
  City("Mucus", 513, 609),
  City("Whiff", 1194, 510),
  City("Momma", 1591, 407),
  City("Labor", 1201, 96),
  City("Hobby", 836, 823),
  City("Quake", 1228, 272),
  City("Light", 1407, 208),
  City("Crook", 1371, 156),
  City("Gleam", 691, 296),
  City("Bloom", 19, 370),
  City("Cleat", 350, 50),
  City("Pitta", 1159, 215),
  City("Reign", 281, 357),
  City("Twerp", 807, 744),
  City("Aloft", 285, 425),
  City("Abyss", 996, 500),
  City("Decoy", 1420, 855),
  City("Sperm", 309, 528),
  City("Tilde", 996, 108),
  City("Purge", 994, 333),
  City("Debag", 813, 799),
  City("Lousy", 863, 610),
  City("Canst", 1012, 735),
  City("Teeth", 855, 209),
  City("Flood", 916, 214),
  City("Borax", 121, 49),
  City("Welch", 761, 232),
  City("Ouija", 440, 218),
  City("Salon", 707, 668),
  City("Rebus", 1258, 800),
  City("Pally", 522, 272),
  City("Abbot", 1561, 419),
  City("Poesy", 87, 400),
  City("Stash", 682, 160),
  City("Topee", 496, 807),
  City("Fruit", 133, 180),
  City("Yonks", 1564, 364),
  City("Fatwa", 1511, 671),
  City("Salty", 668, 72),
  City("Shone", 800, 306),
  City("Batch", 142, 281),
  City("Apace", 1138, 457),
  City("Usage", 502, 316),
  City("Crime", 178, 327),
  City("Catty", 1405, 760),
  City("Phial", 867, 459),
  City("Crone", 757, 474),
  City("Appal", 381, 122),
  City("Prank", 225, 340),
  City("Plank", 592, 225),
  City("Press", 1448, 622),
  City("Virus", 168, 458),
  City("Choir", 240, 93),
  City("Dirty", 1407, 343),
  City("Prise", 423, 177),
  City("Chomp", 1216, 152),
  City("Dower", 852, 506),
  City("Phone", 394, 9),
  City("Whale", 476, 89),
  City("Bulky", 410, 841),
  City("Thigh", 978, 744),
  City("Shirk", 102, 816),
  City("Scurf", 404, 271),
  City("Worry", 1240, 49),
  City("March", 732, 842),
  City("Facer", 809, 115),
  City("Soupy", 967, 621),
  City("Shorn", 703, 883),
  City("Piles", 980, 657),
  City("Harem", 178, 212),
  City("Olden", 1182, 611),
  City("Ionic", 576, 148),
  City("Genie", 1555, 152),
  City("Mafia", 729, 443),
  City("Bafta", 1118, 729),
  City("Teddy", 864, 321),
  City("Carib", 1488, 891),
  City("Tabor", 402, 327),
  City("Dogma", 568, 841),
  City("Rider", 1485, 790),
  City("Doggo", 1, 625),
  City("Horse", 278, 388),
  City("Blimp", 450, 265),
  City("Slimy", 1399, 145),
  City("Cloth", 246, 453),
  City("Lease", 1151, 872),
  City("Livid", 321, 184),
  City("Tiara", 6, 107),
  City("Tarty", 1514, 456),
  City("Ocher", 944, 867),
  City("Rondo", 1120, 114),
  City("Bowie", 823, 56),
  City("Crate", 876, 824),
  City("Spick", 1426, 656),
  City("Noose", 88, 251),
  City("Seize", 744, 692),
  City("Fiord", 1064, 481),
  City("Music", 428, 671),
  City("Front", 1351, 575),
  City("Usury", 1264, 767),
  City("Youth", 701, 238),
  City("Jiffy", 1253, 95),
  City("Gassy", 1248, 168),
  City("Dolma", 1444, 237),
  City("Trash", 553, 663),
  City("Flora", 869, 889),
  City("Newsy", 783, 899),
  City("Weird", 597, 624),
  City("Award", 211, 28),
  City("Couch", 518, 378),
  City("Bezel", 1560, 636),
  City("Prowl", 55, 589),
  City("Quirk", 2, 727),
  City("Tench", 374, 768),
  City("Brute", 1053, 207),
  City("Salsa", 580, 391),
  City("Exert", 205, 810),
  City("Souse", 741, 197),
  City("Khaki", 906, 86),
  City("Dairy", 1477, 631),
  City("Dumpy", 588, 867),
  City("Venal", 180, 280),
  City("Plain", 1069, 899),
  City("Miser", 251, 150),
  City("Squab", 1127, 660),
  City("Sadhu", 1351, 25),
  City("Borne", 351, 280),
  City("Skiff", 162, 665),
  City("Which", 1240, 847),
  City("Going", 23, 147),
  City("Femur", 1566, 488),
  City("Chock", 274, 327),
  City("Bract", 716, 743),
  City("Prick", 214, 529),
  City("Telly", 680, 795),
  City("Hemal", 172, 784),
  City("Whirr", 337, 660),
  City("Offer", 735, 43),
  City("Vaunt", 1525, 723),
  City("Drawl", 762, 804),
  City("Aware", 1480, 663),
  City("Bidet", 1040, 264),
  City("Lobar", 1219, 212),
  City("Maple", 470, 193),
  City("Moire", 250, 11),
  City("Noise", 683, 763),
  City("Vying", 1510, 639),
  City("Parka", 1195, 56),
  City("Donna", 105, 847),
  City("Trice", 744, 570),
  City("Drape", 1576, 698),
  City("Train", 1495, 284),
  City("Smite", 1098, 607),
  City("Muggy", 650, 843),
  City("Indie", 482, 718),
  City("Viral", 1590, 805),
  City("Flair", 1397, 278),
  City("Weeny", 62, 623),
  City("Clerk", 1198, 457),
  City("Cigar", 411, 84),
  City("Pipit", 1467, 590),
  City("Unify", 432, 311),
  City("Baulk", 997, 297),
  City("Liege", 1097, 341),
  City("Levee", 178, 172),
  City("Capon", 156, 68),
  City("Means", 1503, 551),
  City("Twirp", 393, 617),
  City("Elude", 668, 439),
  City("Bream", 762, 664),
  City("Bleep", 1297, 406),
  City("Relax", 327, 72),
  City("Prose", 1453, 270),
  City("Hovel", 1586, 525),
  City("Snail", 913, 169),
  City("Mommy", 367, 664),
  City("Uniat", 1468, 819),
  City("Ethyl", 907, 754),
  City("Vivid", 415, 802),
  City("Abate", 1167, 115),
  City("Erect", 1432, 886),
  City("Motto", 694, 200),
  City("Savor", 654, 377),
  City("Busby", 1324, 602),
  City("Tango", 375, 350),
  City("Uncut", 1433, 373),
  City("Snack", 1376, 807),
  City("Slime", 532, 347),
  City("Eagle", 799, 539),
  City("Their", 51, 439),
  City("Lisle", 199, 840),
  City("Align", 25, 511),
  City("Swiss", 945, 89),
  City("Stoke", 1089, 823),
  City("Nasal", 757, 144),
  City("Queen", 1245, 618),
  City("Lapse", 781, 589),
  City("Marge", 319, 634),
  City("Hades", 920, 566),
  City("Vigil", 1179, 719),
  City("Uvula", 985, 831),
  City("Flaky", 1178, 324),
  City("Adage", 381, 714),
  City("Chain", 113, 741),
  City("Obese", 1140, 6),
  City("Therm", 319, 264),
  City("Yukky", 14, 829),
  City("Laird", 1503, 313),
  City("Comma", 368, 873),
  City("Evoke", 937, 523),
  City("Fiber", 1483, 711),
  City("Bread", 598, 187),
  City("Nerve", 1292, 839),
  City("Urban", 36, 92),
  City("Tamil", 1241, 668),
  City("Cycle", 1334, 786),
  City("Newly", 524, 789),
  City("Sappy", 175, 494),
  City("Bitty", 1283, 122),
  City("Least", 222, 205),
  City("Torch", 279, 555),
  City("Haste", 137, 685),
  City("Nanny", 577, 112),
  City("Bribe", 446, 3),
  City("Human", 1295, 311),
  City("Finch", 639, 660),
  City("Broad", 175, 2),
  City("Hymen", 1102, 186),
  City("Dream", 1467, 485),
  City("Blank", 1329, 692),
  City("Slant", 1023, 345),
  City("Dryly", 104, 289),
  City("Lupus", 551, 131),
  City("Terra", 829, 672),
  City("Tutor", 901, 674),
  City("Pedal", 219, 650),
  City("Bough", 452, 156),
  City("Abbey", 566, 586),
  City("Picky", 531, 189),
  City("Grime", 1508, 4),
  City("Exult", 1376, 873),
  City("Runny", 397, 882),
  City("Bosom", 1253, 313),
  City("Growl", 1025, 769),
  City("Oasis", 1580, 311),
  City("Sotto", 314, 709),
  City("Bodge", 102, 144),
  City("Brick", 387, 532),
  City("Quire", 1149, 517),
  City("Mushy", 209, 103),
  City("Toxin", 261, 287),
  City("Sever", 730, 83),
  City("Stoic", 463, 490),
  City("Sprig", 1069, 630),
  City("Magic", 1401, 591),
  City("Tubby", 822, 899),
  City("Roman", 790, 55),
  City("Fluid", 543, 221),
  City("Blurt", 1176, 10),
  City("Recto", 550, 767),
  City("Title", 895, 443),
  City("Jenny", 1447, 162),
  City("Riven", 297, 824),
  City("Fence", 86, 41),
  City("Jelly", 800, 464),
  City("Cubic", 1370, 365),
  City("Quick", 313, 1),
  City("Wroth", 1576, 573),
  City("Friar", 82, 679),
  City("Pinny", 1074, 281),
  City("Tribe", 688, 119),
  City("Pious", 1573, 891),
  City("Xerox", 358, 631),
  City("Tooth", 1074, 162),
  City("Carat", 42, 410),
  City("Spurn", 992, 5),
  City("Worse", 210, 568),
  City("Icing", 87, 604),
  City("Kopek", 280, 463),
  City("Cover", 634, 578),
  City("Norse", 1032, 185),
  City("Bacon", 621, 121),
  City("Arris", 822, 280),
  City("Sneak", 269, 68),
  City("Crape", 502, 205),
  City("Smoky", 1259, 714),
  City("Lunge", 1459, 860),
  City("Relay", 626, 247),
  City("Jingo", 1358, 447),
  City("Hurry", 1428, 9),
  City("Renew", 672, 728),
  City("Frame", 753, 601),
  City("China", 286, 694),
  City("Yacht", 387, 215),
  City("Amity", 56, 361),
  City("Flank", 113, 897),
  City("Evict", 1075, 247),
  City("Crazy", 550, 386),
  City("Glint", 1324, 725),
  City("Witty", 1219, 743),
  City("Surly", 633, 2),
  City("Cozen", 601, 582),
  City("Craps", 59, 275),
  City("Heavy", 507, 237),
  City("Hover", 504, 646),
  City("Satin", 410, 477),
  City("Gross", 716, 313),
  City("Horny", 1443, 340),
  City("Nones", 1150, 585),
  City("Reran", 30, 461),
  City("Arrow", 598, 7),
  City("Wreck", 199, 471),
  City("Faddy", 995, 590),
  City("Leery", 242, 42),
  City("Prism", 1076, 451),
  City("Honor", 1156, 628),
  City("Baize", 1453, 305),
  City("Vicar", 674, 896),
  City("Cling", 1528, 360),
  City("Scarp", 1536, 495),
  City("Coach", 53, 13),
  City("Squat", 79, 85),
  City("Plaid", 535, 14),
  City("Flout", 791, 196),
  City("Fault", 1142, 369),
  City("Udder", 43, 245),
  City("Furry", 49, 833),
  City("Nudge", 566, 69),
  City("Fudge", 101, 440),
  City("Huffy", 44, 122),
  City("Bijou", 873, 647),
  City("Grant", 1242, 467),
  City("Image", 476, 237),
  City("Sword", 565, 890),
  City("Fatty", 305, 870),
  City("Meths", 1306, 281),
  City("Farce", 1477, 436),
  City("Staff", 1397, 384),
  City("Unsex", 58, 516),
  City("Sherd", 445, 707),
  City("Guest", 1064, 561),
  City("Homey", 1593, 857),
  City("Cheer", 567, 311),
  City("Maria", 947, 2),
  City("Forgo", 972, 149),
  City("Decry", 853, 551),
  City("Tough", 1009, 261),
  City("Mambo", 1405, 43),
  City("Wrest", 1504, 213),
  City("Local", 1593, 339),
  City("Lynch", 1365, 80),
  City("Nasty", 853, 768),
  City("Bigot", 1243, 126),
  City("Hound", 1395, 176),
  City("Ponce", 297, 605),
  City("Stank", 1168, 289),
  City("Cream", 99, 640),
  City("Shaky", 1195, 238),
  City("Bland", 389, 167),
  City("Radii", 868, 110),
  City("Smote", 1293, 93),
  City("Zippy", 1270, 222),
  City("Tunic", 1272, 668),
  City("Helix", 524, 671),
  City("Break", 884, 720),
  City("Audio", 3, 339),
  City("Guise", 976, 180),
  City("Space", 1377, 839),
  City("Small", 531, 304),
  City("Amine", 1214, 182),
  City("Admin", 817, 601),
  City("Ducat", 891, 493),
  City("Knell", 1138, 175),
  City("Brace", 577, 541),
  City("Saucy", 1099, 4),
  City("Lupin", 458, 892),
  City("Olive", 361, 447),
  City("Whist", 627, 464),
  City("Brain", 1170, 426),
  City("Aglow", 8, 4),
  City("Minim", 429, 600),
  City("Irony", 81, 570),
  City("Slurp", 1104, 482),
  City("Sunny", 1059, 794),
  City("Civil", 1524, 843),
  City("Deter", 1113, 389),
  City("Skirt", 344, 369),
  City("Gooey", 81, 766),
  City("Jammy", 648, 793),
  City("Cease", 594, 674),
  City("Jerry", 310, 123),
  City("Shawl", 1074, 865),
  City("Gamut", 892, 305),
  City("Siege", 1221, 322),
  City("Trite", 248, 569),
  City("Force", 942, 663),
  City("Manky", 510, 704),
  City("Hoist", 1552, 5),
  City("Glitz", 528, 882),
  City("Laugh", 1363, 515),
  City("Robin", 1498, 756),
  City("Goner", 1588, 663),
  City("Libra", 72, 156),
  City("Allay", 782, 780),
  City("Slake", 906, 266),
  City("Chant", 1116, 580),
  City("Fixer", 1002, 621),
  City("Macho", 339, 859),
  City("Canoe", 1219, 792),
  City("Midst", 960, 321),
  City("Dipso", 276, 29),
  City("Maize", 1215, 628),
  City("Tight", 1445, 687),
  City("Shell", 378, 36),
  City("Snipe", 1161, 248),
  City("Mater", 525, 819),
  City("Taupe", 1577, 122),
  City("Shoot", 839, 13),
  City("Trout", 953, 898),
  City("Servo", 375, 306),
  City("Blare", 496, 852),
  City("Trews", 176, 248),
  City("Blond", 1441, 93),
  City("Still", 248, 635),
  City("Taper", 261, 665),
  City("Aegis", 967, 251),
  City("Plush", 1106, 245),
  City("Dwarf", 713, 781),
  City("Prove", 504, 553),
  City("Ounce", 377, 589),
  City("Pagan", 158, 144),
  City("Short", 828, 480),
  City("Unman", 970, 28),
  City("Cater", 1375, 774),
  City("Woman", 1, 183),
  City("Verve", 485, 766),
  City("Gippy", 651, 316),
  City("Croft", 1596, 491),
  City("Blush", 438, 453),
  City("Width", 74, 897),
  City("Waged", 566, 800),
  City("Gypsy", 572, 29),
  City("Swung", 1032, 85),
  City("Wader", 582, 454),
  City("Grasp", 1320, 440),
  City("Facet", 1306, 351),
  City("Linen", 935, 350),
  City("Eland", 1177, 889),
  City("Peril", 311, 459),
  City("Sahib", 840, 244),
  City("Puppy", 1148, 327),
  City("Mingy", 313, 577),
  City("Thank", 1373, 603),
  City("Clunk", 1548, 322),
  City("Snick", 1590, 618),
  City("Boule", 227, 886),
  City("Spasm", 1243, 549),
  City("Swoop", 657, 532),
  City("Firry", 806, 411),
  City("Panda", 1280, 874),
  City("Taboo", 294, 232),
  City("Knack", 414, 239),
  City("Bimbo", 428, 344),
  City("Imbed", 259, 770),
  City("Clash", 1068, 358),
  City("Polar", 1561, 542),
  City("Pause", 1064, 600),
  City("Leper", 398, 673),
  City("Basso", 1489, 36),
  City("Shire", 358, 3),
  City("Filly", 1030, 503),
  City("Prior", 463, 350),
  City("Rumba", 1, 77),
  City("Cheat", 381, 82),
  City("Gutsy", 759, 742),
  City("Provo", 741, 881),
  City("Caret", 314, 374),
  City("Magus", 1583, 164),
  City("Dolor", 489, 143),
  City("Shift", 140, 580),
  City("Atoll", 1428, 287),
  City("Demur", 720, 121),
  City("Erase", 1295, 509),
  City("Scots", 499, 54),
  City("Opine", 1398, 308),
  City("Tulle", 255, 495),
  City("Miras", 27, 785),
  City("Aisle", 1320, 2),
  City("Adieu", 155, 541),
  City("Knoll", 707, 535),
  City("Bitch", 731, 6),
  City("Yodel", 231, 784),
  City("Legit", 1593, 78),
  City("Hindi", 677, 829),
  City("Every", 1079, 60),
  City("Boric", 453, 653),
  City("Lathe", 1552, 224),
  City("Enemy", 827, 174),
  City("Greed", 808, 85),
  City("Awful", 824, 632),
  City("Slice", 5, 303),
  City("Easel", 635, 419),
  City("Amiss", 1312, 140),
  City("Thing", 167, 362),
  City("Farsi", 402, 413),
  City("Rusty", 615, 302),
  City("Burin", 1495, 75),
  City("Corny", 687, 45),
  City("Tommy", 1245, 436),
  City("Stead", 1599, 1),
  City("Lunar", 855, 55),
  City("Recce", 388, 817),
  City("Death", 205, 233),
  City("Magna", 591, 358),
  City("Ideal", 463, 790),
  City("Poste", 297, 492),
  City("Nomen", 1552, 679),
  City("Aloud", 673, 597),
  City("Sarky", 1005, 201),
  City("Stork", 998, 897),
  City("Aries", 1466, 137),
  City("Cufic", 1599, 287),
  City("Moult", 732, 809),
  City("Skint", 1181, 172),
  City("Avail", 1227, 384),
  City("Divot", 1204, 658),
  City("Cissy", 1085, 723),
  City("Cough", 799, 653),
  City("Rouse", 467, 291),
  City("Frisk", 660, 226),
  City("Murky", 781, 126),
  City("Slope", 1238, 583),
  City("Genus", 174, 42),
  City("Spree", 699, 82),
  City("Patty", 554, 169),
  City("Cello", 780, 707),
  City("Moron", 886, 232),
  City("Lento", 945, 173),
  City("Sweet", 1127, 852),
  City("Cryer", 361, 796),
  City("Feast", 373, 380),
  City("Loopy", 912, 37),
  City("Funky", 1137, 487),
  City("Snood", 1306, 652),
  City("Thump", 1221, 73),
  City("Combo", 1520, 899),
  City("Stale", 1277, 59),
  City("Whelm", 1215, 824),
  City("Maser", 1340, 873),
  City("Glare", 426, 893),
  City("Buddy", 769, 516),
  City("Primp", 1262, 12),
  City("Floss", 1339, 237),
  City("Crane", 1378, 654),
  City("Ocean", 1509, 387),
  City("Onset", 883, 384),
  City("Baddy", 1051, 727),
  City("Spiel", 1457, 525),
  City("Shirt", 248, 222),
  City("Curia", 946, 796),
  City("Trunk", 6, 887),
  City("Scamp", 16, 599),
  City("Entry", 2, 254),
  City("Carte", 199, 765),
  City("Iraqi", 194, 633),
  City("Chaos", 227, 854),
  City("Crass", 443, 373),
  City("Pesky", 2, 474),
  City("Lotto", 132, 804),
  City("Jesus", 1285, 190),
  City("Shack", 110, 708),
  City("Lover", 1248, 248),
  City("Muddy", 1342, 186),
  City("Liven", 500, 402),
  City("Balmy", 1495, 178),
  City("Donut", 1047, 395),
  City("Lapel", 1371, 121),
  City("Dippy", 446, 79),
  City("Ratio", 1562, 63),
  City("Gamma", 38, 708),
  City("Knock", 259, 121),
  City("Syrup", 1273, 544),
  City("Neigh", 99, 503),
  City("Washy", 660, 347),
]
