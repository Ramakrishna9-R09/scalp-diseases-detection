DISEASE_INFO = {
    "acne-keloidalis": {
        "name": "Acne Keloidalis Nuchae",
        "description": "A chronic inflammatory condition causing keloid-like scarring on the back of the scalp and neck.",
        "severity": "Moderate",
        "urgency_level": 2,
        "days_to_doctor": 14,
        "urgency_color": "yellow",
        "symptoms": ["Itchy bumps on scalp/neck", "Scarring alopecia", "Pus-filled lesions", "Thick raised scars"],
        "medications": {
            "prescription": [
                {"name": "Clindamycin 1% Gel", "dosage": "Apply twice daily", "duration": "8 weeks"},
                {"name": "Triamcinolone Injection", "dosage": "Intralesional, 4 weeks apart", "duration": "3 sessions"},
                {"name": "Doxycycline 100mg", "dosage": "Once daily", "duration": "3 months"}
            ],
            "otc": [
                {"name": "Benzoyl Peroxide Wash 5%", "dosage": "Daily wash", "duration": "Ongoing"},
                {"name": "Salicylic Acid Shampoo", "dosage": "3x per week", "duration": "Ongoing"}
            ],
            "natural": [
                {"name": "Tea Tree Oil (diluted)", "dosage": "Apply 2x daily", "duration": "4 weeks"},
                {"name": "Aloe Vera Gel", "dosage": "Apply nightly", "duration": "Ongoing"}
            ]
        },
        "home_care": ["Avoid tight collars", "No shaving affected area", "Keep area dry and clean"],
        "specialist": "Dermatologist"
    },
    "alopecia-areata": {
        "name": "Alopecia Areata",
        "description": "An autoimmune disorder causing unpredictable, patchy hair loss on the scalp and body.",
        "severity": "Moderate to Severe",
        "urgency_level": 2,
        "days_to_doctor": 7,
        "urgency_color": "yellow",
        "symptoms": ["Round patches of hair loss", "Exclamation mark hairs", "Nail pitting", "Smooth bald patches"],
        "medications": {
            "prescription": [
                {"name": "Minoxidil 5% Solution", "dosage": "Apply twice daily", "duration": "6 months"},
                {"name": "Corticosteroid Cream", "dosage": "Apply twice daily", "duration": "3 months"},
                {"name": "Baricitinib (Olumiant)", "dosage": "2-4mg once daily", "duration": "6 months"}
            ],
            "otc": [
                {"name": "Minoxidil 2% Rogaine", "dosage": "Twice daily", "duration": "6 months"},
                {"name": "Biotin Supplement 5000mcg", "dosage": "Once daily", "duration": "Ongoing"}
            ],
            "natural": [
                {"name": "Rosemary Oil", "dosage": "Massage daily", "duration": "6 months"},
                {"name": "Onion Juice", "dosage": "Apply 30 min before wash", "duration": "8 weeks"}
            ]
        },
        "home_care": ["Reduce stress", "Wear sunscreen on bald patches", "Gentle scalp massage"],
        "specialist": "Dermatologist / Trichologist"
    },
    "androgenic-alopecia": {
        "name": "Androgenic Alopecia (Pattern Baldness)",
        "description": "Hereditary hair thinning due to DHT sensitivity, the most common form of hair loss.",
        "severity": "Progressive",
        "urgency_level": 1,
        "days_to_doctor": 30,
        "urgency_color": "green",
        "symptoms": ["Receding hairline", "Thinning at crown", "Gradual widening part", "Miniaturized hairs"],
        "medications": {
            "prescription": [
                {"name": "Finasteride 1mg", "dosage": "Once daily (men only)", "duration": "12+ months"},
                {"name": "Minoxidil 5% Foam", "dosage": "Once daily", "duration": "12 months"},
                {"name": "Spironolactone 100mg", "dosage": "Once daily (women)", "duration": "6 months"}
            ],
            "otc": [
                {"name": "Minoxidil 5% Rogaine", "dosage": "Twice daily", "duration": "12 months"},
                {"name": "Saw Palmetto Supplement", "dosage": "320mg daily", "duration": "Ongoing"}
            ],
            "natural": [
                {"name": "Pumpkin Seed Oil", "dosage": "400mg daily supplement", "duration": "6 months"},
                {"name": "Rosemary Essential Oil", "dosage": "Scalp massage nightly", "duration": "6 months"}
            ]
        },
        "home_care": ["Avoid heat styling", "Balanced diet rich in iron and protein", "Scalp massage 4 min daily"],
        "specialist": "Dermatologist / Hair Transplant Surgeon"
    },
    "discoid-lupus": {
        "name": "Discoid Lupus Erythematosus",
        "description": "A chronic autoimmune skin disorder causing scarring, inflammatory lesions on scalp and face.",
        "severity": "Severe",
        "urgency_level": 3,
        "days_to_doctor": 3,
        "urgency_color": "red",
        "symptoms": ["Red scaly patches", "Permanent scarring alopecia", "Pigmentation changes", "Atrophy of skin"],
        "medications": {
            "prescription": [
                {"name": "Hydroxychloroquine 200mg", "dosage": "Twice daily", "duration": "6 months"},
                {"name": "Clobetasol Propionate 0.05%", "dosage": "Apply twice daily", "duration": "4 weeks"},
                {"name": "Methotrexate 15mg", "dosage": "Once weekly", "duration": "6 months"}
            ],
            "otc": [
                {"name": "SPF 50+ Sunscreen", "dosage": "Every 2 hours outdoors", "duration": "Ongoing"},
                {"name": "Vitamin D3 2000IU", "dosage": "Once daily", "duration": "Ongoing"}
            ],
            "natural": [
                {"name": "Turmeric Supplement", "dosage": "500mg twice daily", "duration": "3 months"},
                {"name": "Fish Oil 1000mg", "dosage": "Twice daily", "duration": "Ongoing"}
            ]
        },
        "home_care": ["Strict sun avoidance", "Wear protective clothing", "No smoking"],
        "specialist": "Rheumatologist / Dermatologist"
    },
    "dissecting-cellulitis": {
        "name": "Dissecting Cellulitis of the Scalp",
        "description": "A rare neutrophilic follicular occlusion disorder causing deep abscesses and scarring alopecia.",
        "severity": "Severe",
        "urgency_level": 3,
        "days_to_doctor": 2,
        "urgency_color": "red",
        "symptoms": ["Painful nodules and cysts", "Draining sinuses", "Permanent hair loss", "Interconnected tunnels under skin"],
        "medications": {
            "prescription": [
                {"name": "Isotretinoin 0.5mg/kg/day", "dosage": "Daily", "duration": "6 months"},
                {"name": "Rifampicin + Clindamycin", "dosage": "300mg twice daily each", "duration": "10 weeks"},
                {"name": "Adalimumab (Humira)", "dosage": "40mg every 2 weeks", "duration": "6 months"}
            ],
            "otc": [
                {"name": "Zinc Supplement 30mg", "dosage": "Once daily", "duration": "3 months"},
                {"name": "Benzoyl Peroxide Wash", "dosage": "Daily", "duration": "Ongoing"}
            ],
            "natural": [
                {"name": "Tea Tree Oil Shampoo", "dosage": "Daily wash", "duration": "Ongoing"},
                {"name": "Warm Compress", "dosage": "15 min, 3x daily", "duration": "As needed"}
            ]
        },
        "home_care": ["Avoid tight hairstyles", "Keep scalp clean and dry", "Do not squeeze lesions"],
        "specialist": "Dermatologist (Urgent)"
    },
    "folliculitis-decalvans": {
        "name": "Folliculitis Decalvans",
        "description": "A progressive neutrophilic cicatricial alopecia causing recurrent pustular folliculitis.",
        "severity": "Moderate to Severe",
        "urgency_level": 2,
        "days_to_doctor": 7,
        "urgency_color": "yellow",
        "symptoms": ["Recurring pustules around hair follicles", "Tufted hairs", "Scarring alopecia", "Crusting"],
        "medications": {
            "prescription": [
                {"name": "Rifampicin 300mg + Clindamycin 300mg", "dosage": "Twice daily", "duration": "10 weeks"},
                {"name": "Dapsone 50-100mg", "dosage": "Once daily", "duration": "3 months"},
                {"name": "Fusidic Acid Cream", "dosage": "Apply twice daily", "duration": "4 weeks"}
            ],
            "otc": [
                {"name": "Antibacterial Shampoo (Ketoconazole)", "dosage": "Twice weekly", "duration": "Ongoing"},
                {"name": "Zinc Pyrithione Shampoo", "dosage": "3x per week", "duration": "Ongoing"}
            ],
            "natural": [
                {"name": "Manuka Honey", "dosage": "Apply as mask 2x weekly", "duration": "8 weeks"},
                {"name": "Apple Cider Vinegar rinse", "dosage": "Weekly rinse", "duration": "Ongoing"}
            ]
        },
        "home_care": ["Keep scalp very clean", "Use antifungal shampoos regularly", "Avoid sharing combs"],
        "specialist": "Dermatologist"
    },
    "hirsutism": {
        "name": "Hirsutism",
        "description": "Excessive dark, coarse hair growth on scalp edges and body in a male pattern, due to elevated androgens.",
        "severity": "Mild to Moderate",
        "urgency_level": 1,
        "days_to_doctor": 30,
        "urgency_color": "green",
        "symptoms": ["Excessive coarse hair", "Hair in unusual locations", "Acne", "Irregular periods (women)"],
        "medications": {
            "prescription": [
                {"name": "Spironolactone 100-200mg", "dosage": "Once daily", "duration": "6 months"},
                {"name": "Oral Contraceptives", "dosage": "As prescribed", "duration": "6 months"},
                {"name": "Flutamide 250mg", "dosage": "Twice daily", "duration": "6 months"}
            ],
            "otc": [
                {"name": "Eflornithine Cream (Vaniqa)", "dosage": "Apply twice daily", "duration": "Ongoing"},
                {"name": "Spearmint Tea", "dosage": "2 cups daily", "duration": "Ongoing"}
            ],
            "natural": [
                {"name": "Spearmint Tea", "dosage": "2 cups daily", "duration": "3 months"},
                {"name": "Saw Palmetto", "dosage": "320mg daily", "duration": "3 months"}
            ]
        },
        "home_care": ["Weight management", "Low glycemic index diet", "Regular exercise"],
        "specialist": "Endocrinologist / Gynecologist"
    },
    "hot-comb-alopecia": {
        "name": "Hot Comb Alopecia (CCCA)",
        "description": "Central centrifugal cicatricial alopecia caused by heat, tension and chemical damage to hair follicles.",
        "severity": "Moderate",
        "urgency_level": 2,
        "days_to_doctor": 14,
        "urgency_color": "yellow",
        "symptoms": ["Hair loss starting from crown", "Brittle hair", "Scalp tenderness", "Permanent scarring"],
        "medications": {
            "prescription": [
                {"name": "Clobetasol Propionate Shampoo 0.05%", "dosage": "Weekly", "duration": "3 months"},
                {"name": "Tetracycline 500mg", "dosage": "Twice daily", "duration": "3 months"},
                {"name": "Minoxidil 5%", "dosage": "Twice daily", "duration": "6 months"}
            ],
            "otc": [
                {"name": "Minoxidil 2% Women", "dosage": "Once daily", "duration": "6 months"},
                {"name": "Biotin 5000mcg", "dosage": "Daily", "duration": "Ongoing"}
            ],
            "natural": [
                {"name": "Castor Oil Scalp Treatment", "dosage": "Weekly overnight treatment", "duration": "3 months"},
                {"name": "Protein Hair Masks", "dosage": "Bi-weekly", "duration": "Ongoing"}
            ]
        },
        "home_care": ["Stop heat styling completely", "Avoid tight braids and weaves", "Use heat protectant"],
        "specialist": "Trichologist / Dermatologist"
    },
    "lichen-planopilaris": {
        "name": "Lichen Planopilaris",
        "description": "A form of primary cicatricial alopecia causing progressive permanent hair loss with perifollicular inflammation.",
        "severity": "Severe",
        "urgency_level": 3,
        "days_to_doctor": 5,
        "urgency_color": "red",
        "symptoms": ["Perifollicular erythema", "Follicular hyperkeratosis", "Permanent scarring alopecia", "Scalp itching/burning"],
        "medications": {
            "prescription": [
                {"name": "Hydroxychloroquine 200mg", "dosage": "Twice daily", "duration": "6 months"},
                {"name": "Clobetasol Propionate 0.05%", "dosage": "Apply twice daily", "duration": "8 weeks"},
                {"name": "Cyclosporine 3-5mg/kg/day", "dosage": "Daily", "duration": "6 months"}
            ],
            "otc": [
                {"name": "Ketoconazole Shampoo 2%", "dosage": "Twice weekly", "duration": "Ongoing"},
                {"name": "Vitamin D3 Supplement", "dosage": "2000IU daily", "duration": "Ongoing"}
            ],
            "natural": [
                {"name": "Omega-3 Fish Oil", "dosage": "1000mg 3x daily", "duration": "6 months"},
                {"name": "Evening Primrose Oil", "dosage": "1g twice daily", "duration": "3 months"}
            ]
        },
        "home_care": ["Avoid harsh hair products", "Sun protection for scalp", "Gentle hair washing"],
        "specialist": "Dermatologist (Specialist)"
    },
    "pseudopelade": {
        "name": "Pseudopelade of Brocq",
        "description": "A slowly progressive primary cicatricial alopecia causing irregular patchy hair loss resembling footprints in snow.",
        "severity": "Moderate to Severe",
        "urgency_level": 2,
        "days_to_doctor": 10,
        "urgency_color": "yellow",
        "symptoms": ["Irregular white atrophic patches", "No follicular inflammation", "Slow progression", "Permanent hair loss"],
        "medications": {
            "prescription": [
                {"name": "Topical Corticosteroids", "dosage": "Apply twice daily", "duration": "3 months"},
                {"name": "Hydroxychloroquine 200mg", "dosage": "Twice daily", "duration": "6 months"},
                {"name": "Doxycycline 100mg", "dosage": "Once daily", "duration": "3 months"}
            ],
            "otc": [
                {"name": "Biotin Supplement", "dosage": "5000mcg daily", "duration": "Ongoing"},
                {"name": "Minoxidil 5%", "dosage": "Twice daily", "duration": "6 months"}
            ],
            "natural": [
                {"name": "Rosemary Oil Scalp Massage", "dosage": "Daily", "duration": "6 months"},
                {"name": "Vitamin E Oil", "dosage": "Apply nightly", "duration": "3 months"}
            ]
        },
        "home_care": ["Protect from sun", "Gentle hair care routine", "Manage stress"],
        "specialist": "Dermatologist"
    },
    "telogen-effluvium": {
        "name": "Telogen Effluvium",
        "description": "Diffuse hair shedding triggered by physiological stress causing premature entry of hair into the resting phase.",
        "severity": "Mild to Moderate",
        "urgency_level": 1,
        "days_to_doctor": 21,
        "urgency_color": "green",
        "symptoms": ["Diffuse hair shedding", "Thinning across scalp", "Hair loss after stress/illness", "Increased shedding on washing"],
        "medications": {
            "prescription": [
                {"name": "Minoxidil 5%", "dosage": "Twice daily", "duration": "6 months"},
                {"name": "Iron Supplements (if deficient)", "dosage": "As prescribed", "duration": "3 months"},
                {"name": "Thyroid Medication (if indicated)", "dosage": "As prescribed", "duration": "Ongoing"}
            ],
            "otc": [
                {"name": "Biotin 5000mcg", "dosage": "Daily", "duration": "3 months"},
                {"name": "Viviscal Hair Supplement", "dosage": "Twice daily", "duration": "6 months"}
            ],
            "natural": [
                {"name": "Saw Palmetto Extract", "dosage": "320mg daily", "duration": "3 months"},
                {"name": "Ashwagandha 500mg", "dosage": "Once daily", "duration": "3 months"}
            ]
        },
        "home_care": ["Manage stress", "Balanced nutrition (iron, zinc, protein)", "Gentle hair handling"],
        "specialist": "Dermatologist / General Practitioner"
    },
    "trichorrhexis-nodosa": {
        "name": "Trichorrhexis Nodosa",
        "description": "A structural hair defect causing nodular thickenings on the hair shaft leading to easy breakage.",
        "severity": "Mild",
        "urgency_level": 1,
        "days_to_doctor": 30,
        "urgency_color": "green",
        "symptoms": ["White nodes on hair shaft", "Easy hair breakage", "Dull, brittle hair", "Reduced hair length"],
        "medications": {
            "prescription": [
                {"name": "Biotin-rich prescription supplement", "dosage": "As prescribed", "duration": "6 months"},
                {"name": "Amino Acid Infusion Treatment", "dosage": "Monthly in-office", "duration": "6 months"}
            ],
            "otc": [
                {"name": "Biotin 10,000mcg", "dosage": "Daily", "duration": "6 months"},
                {"name": "Keratin Hair Treatment", "dosage": "Monthly", "duration": "Ongoing"}
            ],
            "natural": [
                {"name": "Egg Protein Hair Mask", "dosage": "Weekly", "duration": "Ongoing"},
                {"name": "Argan Oil Treatment", "dosage": "Apply daily to hair", "duration": "Ongoing"}
            ]
        },
        "home_care": ["Avoid chemical treatments", "No heat styling", "Use wide-tooth comb", "Satin pillowcase"],
        "specialist": "Trichologist"
    },
    "trichotillomania": {
        "name": "Trichotillomania",
        "description": "A mental health disorder characterized by recurrent, compulsive urges to pull out hair from scalp and body.",
        "severity": "Moderate (Psychological)",
        "urgency_level": 2,
        "days_to_doctor": 7,
        "urgency_color": "yellow",
        "symptoms": ["Irregular bald patches", "Broken hairs of varying lengths", "Urge to pull hair", "Regrowth after stopping"],
        "medications": {
            "prescription": [
                {"name": "N-Acetylcysteine 1200-2400mg", "dosage": "Daily", "duration": "12 weeks"},
                {"name": "Clomipramine 25-250mg", "dosage": "Daily", "duration": "6 months"},
                {"name": "Olanzapine (adjunct)", "dosage": "As prescribed", "duration": "3 months"}
            ],
            "otc": [
                {"name": "Melatonin for sleep", "dosage": "3mg nightly", "duration": "Ongoing"},
                {"name": "Stress Relief Supplement", "dosage": "As directed", "duration": "Ongoing"}
            ],
            "natural": [
                {"name": "Lavender Aromatherapy", "dosage": "Daily", "duration": "Ongoing"},
                {"name": "Mindfulness Meditation", "dosage": "15-30 min daily", "duration": "Ongoing"}
            ]
        },
        "home_care": ["Cognitive Behavioral Therapy (CBT)", "HRT - Habit Reversal Training", "Support groups"],
        "specialist": "Psychiatrist / Psychologist"
    },
    "tufted-folliculitis": {
        "name": "Tufted Folliculitis",
        "description": "A form of scarring alopecia where multiple hair shafts emerge from a single dilated follicular opening.",
        "severity": "Moderate to Severe",
        "urgency_level": 2,
        "days_to_doctor": 7,
        "urgency_color": "yellow",
        "symptoms": ["Tufts of 5-20 hairs from single follicle", "Crusting and pustules", "Scarring alopecia", "Scalp tenderness"],
        "medications": {
            "prescription": [
                {"name": "Rifampicin 300mg + Clindamycin 300mg", "dosage": "Twice daily", "duration": "10 weeks"},
                {"name": "Fusidic Acid 2% Cream", "dosage": "Apply twice daily", "duration": "4 weeks"},
                {"name": "Clobetasol Shampoo 0.05%", "dosage": "Twice weekly", "duration": "3 months"}
            ],
            "otc": [
                {"name": "Antibacterial Shampoo", "dosage": "Daily wash", "duration": "Ongoing"},
                {"name": "Zinc Supplement 30mg", "dosage": "Daily", "duration": "3 months"}
            ],
            "natural": [
                {"name": "Neem Oil Treatment", "dosage": "Apply weekly", "duration": "Ongoing"},
                {"name": "Tea Tree Oil Shampoo", "dosage": "Daily", "duration": "Ongoing"}
            ]
        },
        "home_care": ["Keep scalp bacteria-free", "Don't share hair tools", "Gentle scalp hygiene"],
        "specialist": "Dermatologist"
    }
}
