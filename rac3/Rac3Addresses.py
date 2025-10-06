CHECK_TYPE = {
    "bit": 0,
    "int": 1,
    "uint": 2,
    "byte": 3,
    "short": 4,
    "falseBit": 5,
    "long": 6,
    "nibble": 7,
}
COMPARE_TYPE = {
    "Match": 0,
    "GreaterThan": 1,
    "LessThan": 2,
}

ADDRESSES = {
    "SCUS-97353": {
        "Weapons": {
            "Shock Blaster": {"unlockAddress": 0x00142CC7, "id": 39, "ammoAddress": 0x0014288C, "lv1Ammo": 30, },
            "Nitro Launcher": {"unlockAddress": 0x00142D17, "id": 119, "ammoAddress": 0x001429CC, "lv1Ammo": 8, },
            "N60 Storm": {"unlockAddress": 0x00142CCF, "id": 47, "ammoAddress": 0x001428AC, "lv1Ammo": 150, },
            "Plasma Whip": {"unlockAddress": 0x00142D1F, "id": 127, "ammoAddress": 0x001429EC, "lv1Ammo": 25, },
            "Infector": {"unlockAddress": 0x00142CD7, "id": 55, "ammoAddress": 0x001428CC, "lv1Ammo": 15, },
            "Suck Cannon": {"unlockAddress": 0x00142D27, "id": 135, "ammoAddress": 0x00000000, "lv1Ammo": 0, },
            "Spitting Hydra": {"unlockAddress": 0x00142CE7, "id": 71, "ammoAddress": 0x0014290C, "lv1Ammo": 15, },
            "Agents of Doom": {"unlockAddress": 0x00142CF7, "id": 87, "ammoAddress": 0x0014294C, "lv1Ammo": 6, },
            "Flux Rifle": {"unlockAddress": 0x00142D0F, "id": 111, "ammoAddress": 0x001429AC, "lv1Ammo": 10, },
            "Annihilator": {"unlockAddress": 0x00142CDF, "id": 63, "ammoAddress": 0x001428EC, "lv1Ammo": 20, },
            "Holo-Shield Glove": {"unlockAddress": 0x00142D07, "id": 103, "ammoAddress": 0x0014298C, "lv1Ammo": 8, },
            "Disk-Blade Gun": {"unlockAddress": 0x00142CEF, "id": 79, "ammoAddress": 0x0014292C, "lv1Ammo": 25, },
            "Rift Inducer": {"unlockAddress": 0x00142CFF, "id": 95, "ammoAddress": 0x0014296C, "lv1Ammo": 8, },
            "Qwack-O-Ray": {"unlockAddress": 0x00142D2F, "id": 143, "ammoAddress": 0x00000000, "lv1Ammo": 0, },
            "RY3N0": {"unlockAddress": 0x00142D37, "id": 151, "ammoAddress": 0x00142A4C, "lv1Ammo": 25, },
            "Mini-Turret Glove": {"unlockAddress": 0x00142CB5, "id": 21, "ammoAddress": 0x00142844, "lv1Ammo": 10, },
            "Lava Gun": {"unlockAddress": 0x00142CB1, "id": 17, "ammoAddress": 0x00142834, "lv1Ammo": 150, },
            "Shield Charger": {"unlockAddress": 0x00142CB6, "id": 22, "ammoAddress": 0x00142848, "lv1Ammo": 3, },
            "Bouncer": {"unlockAddress": 0x00142CB3, "id": 19, "ammoAddress": 0x0014283C, "lv1Ammo": 10, },
            "Plasma Coil": {"unlockAddress": 0x00142CB0, "id": 16, "ammoAddress": 0x00142830, "lv1Ammo": 15, },
        },
        "Gadgets": {
            "Heli-Pack": {"unlockAddress": 0x00142CA2, "id": 0, },
            "Thruster-Pack": {"unlockAddress": 0x00142CA3, "id": 0, },
            "Hacker": {"unlockAddress": 0x00142CB4, "id": 0, },
            "Hypershot": {"unlockAddress": 0x00142CAB, "id": 11, },
            "Refractor": {"unlockAddress": 0x00142CB2, "id": 18, },
            "Tyhrra-Guise": {"unlockAddress": 0x00142CBE, "id": 30, },
            "Gravity-Boots": {"unlockAddress": 0x00142CAD, "id": 0, },
            "Bolt Grabber V2": {"unlockAddress": 0x00142CA7, "id": 0, },
            "Box Breaker": {"unlockAddress": 0x00142CBA, "id": 0, },
            "Map-O-Matic": {"unlockAddress": 0x00142CA5, "id": 0, },
            "Nano Pak": {"unlockAddress": 0x00142CC0, "id": 0, },
            "Warp Pad": {"unlockAddress": 0x00142CBF, "id": 31, },
            "Gadgetron PDA": {"unlockAddress": 0x00142CC3, "id": 35, },
            "Charge-Boots": {"unlockAddress": 0x00142CBD, "id": 0, },
            "Master Plan": {"unlockAddress": 0x00142CC2, "id": 0, },
        },
        "VidComics": {
            "Qwark VidComic 1": {"unlockAddress": 0x001D554F},
            "Qwark VidComic 2": {"unlockAddress": 0x001D5551},
            "Qwark VidComic 3": {"unlockAddress": 0x001D5552},
            "Qwark VidComic 4": {"unlockAddress": 0x001D5550},
            "Qwark VidComic 5": {"unlockAddress": 0x001D5553},
        },
        "PlanetSlots": [
            0x00143050, 0x00143054, 0x00143058, 0x0014305C,
            0x00143060, 0x00143064, 0x00143068, 0x0014306C,
            0x00143070, 0x00143074, 0x00143078, 0x0014307C,
            0x00143080, 0x00143084, 0x00143088, 0x0014308C,
            0x00143090, 0x00143094, 0x00143098, 0x0014309C,
        ],
        "PlanetValues": {
            "Veldin": 1,
            "Florana": 2,
            "Starship Phoenix": 3,
            "Marcadia": 4,
            "Daxx": 5,
            # "Phoenix Assault" : 6,
            "Annihilation Nation": 7,
            "Aquatos": 8,
            "Tyhrranosis": 9,
            "Zeldrin Starport": 10,
            "Obani Gemini": 11,
            "Blackwater City": 12,
            "Holostar Studios": 13,
            "Koros": 14,
            # "Unused": 15,
            "Metropolis": 16,
            "Crash Site": 17,
            "Aridia": 18,
            "Qwarks Hideout": 19,
            # "Command Center 2": 20,
            "Obani Draco": 21,
            "Command Center": 22,
            # "Holostar Studios Clank": 23,
            "Museum": 24,
            # "Unused": 25,
            # "Metropolis Arena": 26,
            # "Aquatos Base": 27,
            # "Aquatos Sewers": 28,
            # "Tyhrranosis: Mission": 29,
            # "Qwark VidComic Unused 1": 30
            # "Qwark VidComic 1": 31
            # "Qwark VidComic 4": 32
            # "Qwark VidComic 2": 33
            # "Qwark VidComic 3": 34
            # "Qwark VidComic 5": 35
            # "Qwark VidComic Unused 2": 36
            # 40-55 Multiplayer maps
        },
        "QuickSelectSlots": [
            # Slot 1
            0x001D4C60, 0x001D4C64, 0x001D4C68, 0x001D4C6C,
            0x001D4C70, 0x001D4C74, 0x001D4C78, 0x001D4C7C,
            # Slot 2(With R1 button)
            0x001D4C80, 0x001D4C84, 0x001D4C88, 0x001D4C8C,
            0x001D4C90, 0x001D4C94, 0x001D4C98, 0x001D4C9C,
        ],
        "MainMenu": 0x0016C598,
        "XCoord": 0x001A4C60,
        "YCoord": 0x001A4C64,
        "ZCoord": 0x001A4C68,                
        "XCoordRespawn": 0x002348D0,
        "YCoordRespawn": 0x002348D4,
        "ZCoordRespawn": 0x002348D8,
        "RotationRespawn": 0x002348E8,
        "RatchetCurrentColor": 0x01C8E3BC,
        "RatchetSize": 0x01C8E3AC,
        "RatchetTransparency": 0x01C8E3A0,
        "CurrentEquipped": 0x001D4C40,
        "HoldingWeapon": 0x001A5E08,
        "LastUsed": [0x00142670, 0x00142674, 0x00142678],
        "ArmorVersion": 0x001426A0,
        "boltXPMultiplier": 0x001426BA,
        "Bolt": 0x00142660,
        "JackpotActive": 0x001A74A8,
        "JackpotTimer": 0x001A4E10,
        "InfernoTimer": 0x001A4E14,
        "Challenge Mode Count": 0x00142692,
        "NanotechExp": 0x00142694,
        "CurrentHealth": 0x001A7430,
        "MaxHealth": 0x001A7438,
        "CurrentPlanet": 0x001D545C,
        "SewerCrystalsInPossession": 0x001426A2,
        "Robonoids active": 0x0014275C,
        "MonkeyHitCounter": 0x01D3C828,
        "Skill Points": {
            "Go for hang time": 0x001D54B0,
            "Stay Squeaky Clean": 0x001D54B1,
            "Strive for arcade perfection": 0x001D54B2,
            "Beat Helga's best time": 0x001D54B3,
            "Turn Up The Heat": 0x001D54B4,
            "Monkeying around": 0x001D54B5,
            "Reflect on how to score": 0x001D54B6,
            "Bugs to Birdie": 0x001D54B7,
            "Bash the bug": 0x001D54B8,
            "Be an eight time champ": 0x001D54B9,
            "Flee Flawlessly": 0x001D54BA,
            "Lights, camera action!": 0x001D54BB,
            "Search for sunken treasure": 0x001D54BC,
            "Be a Sharpshooter": 0x001D54BD,
            "Get to the belt": 0x001D54BE,
            "Bash the party": 0x001D54BF,
            "Feeling Lucky": 0x001D54C0,
            "You break it, you win it": 0x001D54C1,
            "2002 was a good year in the city": 0x001D54C2,
            "Suck it up!": 0x001D54C3,
            "Aim High": 0x001D54C4,
            "Zap back at ya'": 0x001D54C5,
            "Break the Dan": 0x001D54C6,
            "Spread your germs": 0x001D54C7,
            "Hit the motherload": 0x001D54C8,
            "Pirate booty - set a new record for qwark": 0x001D54C9,
            "Deja Q All over Again - set a new record for qwark": 0x001D54CA,
            "Arriba Amoeba! - set a new record for qwark": 0x001D54CB,
            "Shadow of the robot - set a new record for qwark": 0x001D54CC,
            "The Shaming of the Q - set a new record for qwark": 0x001D54CD
        },
        "Missions": {
            "First Ranger gives weapon": 0x001426E0,
            "Second Ranger gives weapon": 0x001426E1,
            "Zeldrin starport: Find Nefarious": 0x001426E2,
            "Save Veldin": 0x001426E3,
            "Veldin: Eliminate the Enemy Forces": 0x001426E4,
            "Florana: Find the mysterious man": 0x001426E5,
            "Florana: Walk the path of death!": 0x001426E6,
            "Defeat Qwark": 0x001426E7,
            "Take Qwark to Cage": 0x001426E8,
            "Meet Sasha bridge": 0x001426E9,
            "Meet Al on Marcadia": 0x001426EA,
            "Play VidComic1": 0x001426EB,
            "Marcadia: Get to the Palace": 0x001426EF,
            "Marcadia: Repair the LDS": 0x001426F1,
            "Marcadia: Secure the Area": 0x001426F2,
            "Annihilation Nation: Return": 0x001426F3,
            "Phoenix Rescue": 0x001426F4,
            "Annihilation Nation: Grand Prize Bout": 0x001426F5,
            "Return to Phoenix after Annihilation Nation 2": 0x001426F6,
            "Aquatos: Infiltrate the Base": 0x001426F7,
            "Tyhrranosis: Destroy the Plasma Cannon Turrets": 0x001426F9,
            "Obani Gemini: ???": 0x00142701,
            "Save Blackwater City": 0x00142704,
            "Blackwater: Destroy the Base": 0x00142705,
            "Metropolis: Defeat Klunk": 0x00142708,
            "Obani Draco: Defeat Courtney Gears": 0x0014270D,
            "Defeat Dr Nefarious": 0x0014270F,
            "Destroy the Biobliterator": 0x00142710,  # Doesn't get written to
            "Holostar: Film Episode": 0x00142712,
            "Holostar: Return to your ship": 0x00142713,
            "Metropolis: Complete Ranger Missions": 0x00142714,
            "Aquatos: Gather Sewer Crystals": 0x00142715,
            "Tyhrranosis: Destroy the Encampment": 0x00142717,
            "Tyhrranosis: Destroy the Momma Tyhrranoid": 0x0014271D,
        },
        "Enemies": {
            "First of two noids - Mylon Landing Point": 0x001C169E,
            "Second of two noids - Mylon Landing Point": 0x001C16F4,
            "Mechanoid after Blaster - Veldin": 0x001BC2C2,
        },
        "Crystals": {
            "Crystal - First sector, first way": 0x001C2EC4,
            "Crystal - First sector, second way - King Ameboid": 0x001C2E9B,
            "Crystal - First sector, second way": 0x001C2EC3,
        },
        "Crates": {
            "Nanotech Crate - 1": 0x001BC3B5,
        },
        "Checkpoints": {
        },
    }
}

LOCATIONS = [
    {
        "Name": "First Ranger gives weapon",
        "Id": 50010000,
        "Address": "0x001426E0",
        # Use event flag rather than weapon unlock address to avoid issues with weapon randomizer
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Second Ranger gives weapon",
        "Id": 50010001,
        "Address": "0x001426E1",
        # Use event flag rather than weapon unlock address to avoid issues with weapon randomizer
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Save Veldin",
        "Id": 50010002,
        "Address": "0x001426E4",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Received Plasma Whip",
        "Id": 50020000,
        "Address": "0x00142D1F",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Received N60 Storm",
        "Id": 50020001,
        "Address": "0x00142CCF",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "T-Bolt: Below Gadgetron Vendor",
        "Id": 50020002,
        "Address": "0x001BBB29",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "T-Bolt: Path of Death",
        "Id": 50020003,
        "Address": "0x001BBB2A",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Defeat Qwark",
        "Id": 50020004,
        "Address": "0x001426E7",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Received Suck Cannon",
        "Id": 50030000,
        "Address": "0x00142D27",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Received Infector",
        "Id": 50030001,
        "Address": "0x00142CD7",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "T-Bolt: Nerves of Titanium",
        "Id": 50030027,
        "Address": "0x001BBB30",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "T-Bolt: VR Gadget Training",
        "Id": 50030015,
        "Address": "0x001BBB31",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Received Magna Plate Armor",
        "Id": 50030002,
        "Address": "0x001426A0",
        "CheckValue": "1",
        "CheckType": 3
    },
    {
        "Name": "Received Adamantine Armor",
        "Id": 50030003,
        "Address": "0x001426A0",
        "CheckValue": "2",
        "CheckType": 3
    },
    {
        "Name": "Received Aegis Mark V Armor",
        "Id": 50030004,
        "Address": "0x001426A0",
        "CheckValue": "3",
        "CheckType": 3
    },
    {
        "Name": "Received Infernox Armor",
        "Id": 50030005,
        "Checks": [
            {
                "Address": "0x001D54B4",
                "CheckType": 0,
                "AddressBit": 0
            },
            {
                "Address": "0x001D545C",
                "CheckValue": "3",
                "CheckType": 0
            }
        ]
    },
    {
        "Name": "Received Hacker",
        "Id": 50030016,
        #"Address": "0x00142CB4",
        "Address": "0x00142765",  # Same as VR Gadget Training mission completion
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Received Hypershot",
        "Id": 50030017,
        #"Address": "0x00142CAB",
        "Address": "0x00142765",  # Same as VR Gadget Training mission completion
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Marcadia Invaded",
        "Id": 50030006,
        "Checks": [
            {
                "Address": "0x001426E9",
                "CheckValue": "1",
                "CheckType": 0
            },
            {
                "Address": "0x001D545C",
                "CheckValue": "3",
                "CheckType": 0
            }
        ]
    },
    {
        "Name": "Infobot: Koros",
        "Id": 50030007,
        "Address": "0x001D553E",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Play VidComic1",
        "Id": 50030008,
        "Address": "0x001426EB",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Aquatos Mission Briefing",
        "Id": 50030009,
        # " Address": 0x001426F6, #  Correct Infobot address
        "Address": "0x0014276F",  # Same as Tyhrra-Guise Getting event. This event behinds Phoenix Ship event.
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Infiltrate Aquatos Base",
        "Id": 50030010,
        # "Address": "0x00142C1B",
        "Address": "0x0014275E",  # Same as 1 Sewer Crystal Traded
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "VR Gadget Training",
        "Id": 50030011,
        #  "Address": "0x00142765",
        "Address": "0x00142765",  # Same as T-Bolt: VR training
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Infobot: Crash Site",
        "Id": 50160004,
        #  "Address": "0x001D5541",
        "Address": "0x00142708",  # Same as defeat Giant Cronk
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Learn Qwarks Hideout from VidComic 5",
        "Id": 50030014,
        "Address": "0x00142734",
        "CheckType": 0,
        "AddressBit": 5  # 3E 00X0_0000
    },
    {
        "Name": "Escape the Leviathan",
        "Id": 50100003,
        "Address": "0x001426E2",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Gave Al the Master Plan",
        "Id": 50030029,
        "Address": "0x001D5553",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Infobot: Metropolis",
        "Id": 50030012,
        "Address": "0x001D5550",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Received Spitting Hydra",
        "Id": 50040000,
        "Address": "0x00142CE7",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Received Refractor",
        "Id": 50040001,
        # "Address": "0x00142CB2", # item flag
        "Address": "0x00142C29",  # Marcadia Mission event Flag
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "T-Bolt: After Pool of Water",
        "Id": 50040002,
        "Address": "0x001BBB39",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "T-Bolt: Last Refractor Room",
        "Id": 50040003,
        "Address": "0x001BBB3A",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "T-Bolt: Ceiling just before Al",
        "Id": 50040004,
        "Address": "0x001BBB3B",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Meet Al",
        "Id": 50040005,
        "Address": "0x001426ea",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Received Agents of Doom",
        "Id": 50070000,
        "Address": "0x00142CF7",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Received Tyhrra-Guise",
        "Id": 50070001,
        "Address": "0x0014276F",  # Same as Grand Prize Bout(Tyhrra-Guise Getting event)
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "T-Bolt: Heat Street",
        "Id": 50070002,
        "Address": "0x001BBB51",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "T-Bolt: Maze of Blaze",
        "Id": 50070003,
        "Address": "0x001BBB52",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Grand Prize Bout",
        "Id": 50070004,
        "Address": "0x0014276F",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "The Terrible Two",
        "Id": 50070005,
        "Address": "0x00142772",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Robot Rampage",
        "Id": 50070006,
        "Address": "0x00142773",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Two Minute Warning",
        "Id": 50070007,
        "Address": "0x00142774",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "90 Seconds of Carnage",
        "Id": 50070008,
        "Address": "0x00142775",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Onslaught",
        "Id": 50070009,
        "Address": "0x00142776",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Whip It Good",
        "Id": 50070010,
        "Address": "0x00142777",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Hydra N' Seek",
        "Id": 50070011,
        "Address": "0x00142778",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Championship Bout",
        "Id": 50070012,
        "Address": "0x00142779",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Ninja Challenge",
        "Id": 50070014,
        "Address": "0x0014277D",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Counting Ducks",
        "Id": 50070015,
        "Address": "0x0014277E",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Cycling Weapons",
        "Id": 50070016,
        "Address": "0x0014277F",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "One Hit Wonder",
        "Id": 50070017,
        "Address": "0x00142780",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Time to Suck",
        "Id": 50070018,
        "Address": "0x00142781",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Naptime",
        "Id": 50070019,
        "Address": "0x00142782",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Meet Courtney - Arena",
        "Id": 50070013,
        "Address": "0x00142771",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "More Cycling Weapons",
        "Id": 50070020,
        "Address": "0x00142783",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Dodge the Twins",
        "Id": 50070021,
        "Address": "0x00142784",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Chop Chop",
        "Id": 50070022,
        "Address": "0x00142785",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Sleep Inducer",
        "Id": 50070023,
        "Address": "0x00142786",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "The Other White Meat",
        "Id": 50070024,
        "Address": "0x00142787",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Championship Bout II",
        "Id": 50070025,
        "Address": "0x00142788",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Qwarktastic Battle",
        "Id": 50070026,
        "Address": "0x00142789",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Heat Street",
        "Id": 50070027,
        "Address": "0x0014276E",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Crispy Critter",
        "Id": 50070028,
        "Address": "0x0014277A",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Pyro Playground",
        "Id": 50070029,
        "Address": "0x0014277B",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Suicide Run",
        "Id": 50070030,
        "Address": "0x0014277C",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "BBQ Boulevard",  # (Meet Courtney - Gauntlet)
        "Id": 50070031,
        "Address": "0x00142770",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Maze of Blaze",
        "Id": 50070032,
        "Address": "0x0014278A",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Cremation Station",
        "Id": 50070033,
        "Address": "0x0014278B",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "The Annihilator (Gauntlet)",
        "Id": 50070034,
        "Address": "0x0014278C",
        "CheckType": 0,
        "AddressBit": 0
    },
    # {
    #     "Name": "Qwark VidComic 2",
    #     "Id": 50070035,
    #     "Address": "0x001D5551",
    #     "CheckType": 0,
    #     "AddressBit": 0
    # },
    # {
    #     "Name": "Qwark VidComic 3",
    #     "Id": 50070036,
    #     "Address": "0x001D5552",
    #     "CheckType": 0,
    #     "AddressBit": 0
    # },
    {
        "Name": "Received Flux Rifle",
        "Id": 50080000,
        "Address": "0x00142D0F",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "T-Bolt: Under the Bridge",
        "Id": 50080001,
        "Address": "0x001BBB5A",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "T-Bolt: Underwater Bolt",
        "Id": 50080002,
        "Address": "0x001BBB5B",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "T-Bolt: Behind the Locked Gate",
        "Id": 50080003,
        "Address": "0x001BBB59",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "T-Bolt: Top Left Bolt",
        "Id": 50280000,
        "Address": "0x001BBBF9",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "T-Bolt: Swinging Bolt",
        "Id": 50280001,
        "Address": "0x001BBBFA",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "1 Sewer Crystal Traded",
        "Id": 50280002,
        "Address": "0x0014275E",  # JP: 1426DE,
        "CompareType": 1,  # Greater than
        "CheckType": 3,  # Byte type
        "CheckValue": "0"
    },
    {
        "Name": "5 Sewer Crystals Traded",
        "Id": 50280003,
        "Address": "0x0014275E",  # JP: 1426DE,
        "CheckType": 3,  # Byte type
        "CompareType": 1,  # Greater than
        "CheckValue": "4"
    },
    {
        "Name": "10 Sewer Crystals Traded",
        "Id": 50280004,
        "Address": "0x0014275E",  # JP: 1426DE,
        "CheckType": 3,  # Byte type
        "CompareType": 1,  # Greater than
        "CheckValue": "9"  # 0x9
    },
    {
        "Name": "20 Sewer Crystals Traded",
        "Id": 50280005,
        "Address": "0x0014275E",  # JP: 1426DE,
        "CheckType": 3,  # Byte type
        "CompareType": 1,  # Greater than
        "CheckValue": "19"  # 0x13
    },
    {
        "Name": "Received Annihilator",
        "Id": 50090000,
        "Address": "0x00142CDF",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Received Holo-Shield Glove",
        "Id": 50090001,
        "Address": "0x00142D07",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "T-Bolt: South East Cannon",
        "Id": 50090002,
        "Address": "0x001BBB62",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "T-Bolt: Underground Cave Bolt",
        "Id": 50090003,
        "Address": "0x001BBB61",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "T-Bolt: Right of the Taxi",
        "Id": 50050001,
        "Address": "0x001BBB41",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "T-Bolt: Time-Sensitive Door",
        "Id": 50050002,
        "Address": "0x001BBB42",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Received Charge Boots",
        "Id": 50050003,
        "Address": "0x00142CBD",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Infiltrate Weapons Facility",
        "Id": 50050000,
        "Address": "0x001D553B",
        # Infobot Address: "0x00142C29" bit 3
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Gunship",
        "Id": 50050004,
        # "Address": "0x00143B39", #  ??
        "Address": "0x0014275B",  # Daxx Courtney Room
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Received Disk Blade Gun",
        "Id": 50110000,
        "Address": "0x00142CEF",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "T-Bolt: Follow the Lava",
        "Id": 50110001,
        "Address": "0x001BBB72",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "T-Bolt: Between the Twin Towers",
        "Id": 50110002,
        "Address": "0x001BBB71",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Infobot: Blackwater City",
        "Id": 50110003,
        "Address": "0x00142BB2",
        "CheckType": 0,
        "AddressBit": 3  # 08: 0000_X000
    },
    {
        "Name": "Received Grav Boots",
        "Id": 50120000,
        #  "Address": "0x00142CAD",
        "Address": "0x00142C40",
        "CheckType": 0,
        "AddressBit": 3  # 0x08: 0000_X000
    },
    {
        "Name": "Infobot: Holostar Studios",
        "Id": 50120001,
        "Address": "0x00142705",
        #  "Address": "0x00142771", #  WA: Same as Meet Courtney - Arena
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Received Rift Inducer",
        "Id": 50130000,
        "Address": "0x00142CFF",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "T-Bolt: Atop the Chairs",
        "Id": 50130001,
        "Address": "0x001BBB82",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "T-Bolt: Lot 42's Grav Ramp",
        "Id": 50130002,
        "Address": "0x001BBB83",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "T-Bolt: Kamikaze Noids",
        "Id": 50130003,
        "Address": "0x001BBB81",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Infobot: Obani Draco",
        "Id": 50130004,
        "Address": "0x00142713",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Defeat Courtney Gears",
        "Id": 50210000,
        "Address": "0x0014270D",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Received Bolt Grabber V2",
        "Id": 50100000,
        "Address": "0x00142CA7",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "T-Bolt: Inside the Second Ship",
        "Id": 50100001,
        "Address": "0x001BBB6A",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "T-Bolt: Atop the Twin Shooters",
        "Id": 50100002,
        "Address": "0x001BBB69",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Received Map-O-Matic",
        "Id": 50260006,
        #  "Address": "0x00142CA5", #  item flag
        "Address": "0x00142C64",  # Metropolis Mission Clear
        "CheckType": 0,
        "AddressBit": 5  # 0x20 : 00X0_0000
    },
    {
        "Name": "T-Bolt: Across the Gap",
        "Id": 50160000,
        "Address": "0x001BBB99",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "T-Bolt: Before Grav-wall",
        "Id": 50160003,
        "Address": "0x001BBB9A",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "T-Bolt: Tall Tower (Hovership)",
        "Id": 50260000,
        "Address": "0x001BBBE9",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Metal-Noids",
        "Id": 50160002,
        "Address": "0x0014275C",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Received Nano-Pak",
        "Id": 50170001,
        "Address": "0x00142CC0",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "T-Bolt: Turn Around",
        "Id": 50170000,
        "Address": "0x001BBBA1",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Infobot: Aridia",
        "Id": 50170003,
        "Address": "0x00142C52",
        # "Address": "0x00142722",
        # Correct Address: 0x00142C52(4bit: 0x07->0x0f) (US), but Event is not happened in some case.
        "CheckType": 0,
        "AddressBit": 3  # / 0x02: 0000_00X0
    },
    {
        "Name": "Received Warp Pad",
        "Id": 50180000,
        # "Address": "0x00142CBF", #  Item flag
        "Address": "0x00142C56",  # Clear Aridia
        "CheckType": 0,
        "AddressBit": 4  # 0x10: 000X_0000
    },
    {
        "Name": "Received Qwack-O-Ray",
        "Id": 50180001,
        "Address": "0x00142D2F",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "T-Bolt: Under the Bridge (Assassination)",
        "Id": 50180002,
        "Address": "0x001BBBAA",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "T-Bolt: Behind the Base (X12 Endgame)",
        "Id": 50180003,
        "Address": "0x001BBBA9",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Received Gadgetron PDA",
        "Id": 50190000,
        "Address": "0x00142CC3",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "T-Bolt: Glide from the Ramp",
        "Id": 50190001,
        "Address": "0x001BBBB1",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "T-Bolt: Behind the Metal Fence",
        "Id": 50140000,
        "Address": "0x001BBB89",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "T-Bolt: Pair of Towers",
        "Id": 50140001,
        "Address": "0x001BBB8A",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Infobot: Command Center",
        "Id": 50140002,
        "Address": "0x00142C49",
        "CheckType": 0,
        "AddressBit": 3  # 04 -> 0C: 0000_X000
    },
    {
        "Name": "T-Bolt: Behind the Forcefield",
        "Id": 50220000,
        "Address": "0x001BBBC9",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Dr. Nefarious Defeated!",
        "Id": 50200000,
        "Address": "0x0014270F",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Biobliterator Defeated!",
        "Id": 50200001,
        "Address": "0x00142BB6",
        "CheckType": 0,
        "AddressBit": 6  # 40: 0X00_0000
    },
    {
        "Name": "T-Bolt: VidComic 1",
        "Id": 50310001,
        "Address": "0x001BBB32",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "T-Bolt: VidComic 2",
        "Id": 50330001,
        "Address": "0x001BBB33",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "T-Bolt: VidComic 3",
        "Id": 50340001,
        "Address": "0x001BBB34",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "T-Bolt: VidComic 4",
        "Id": 50320001,
        "Address": "0x001BBB35",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "T-Bolt: VidComic 5",
        "Id": 50350001,
        "Address": "0x001BBB36",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Shock Blaster: V2",
        "Id": 50150000,
        "Address": "0x00142E7C",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "4800"
    },
    {
        "Name": "Shock Blaster: V3",
        "Id": 50150001,
        "Address": "0x00142E7C",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "12800"
    },
    {
        "Name": "Shock Blaster: V4",
        "Id": 50150002,
        "Address": "0x00142E7C",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "22400"
    },
    {
        "Name": "Shock Blaster: V5",
        "Id": 50150003,
        "Address": "0x001425E7",
        "CompareType": 0,
        "CheckType": 1,
        "CheckValue": "43"
    },
    {
        "Name": "Nitro Launcher: V2",
        "Id": 50150004,
        "Address": "0x00142FBC",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "6400"
    },
    {
        "Name": "Nitro Launcher: V3",
        "Id": 50150005,
        "Address": "0x00142FBC",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "16000"
    },
    {
        "Name": "Nitro Launcher: V4",
        "Id": 50150006,
        "Address": "0x00142FBC",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "35200"
    },
    {
        "Name": "Nitro Launcher: V5",
        "Id": 50150007,
        "Address": "0x00142FBC",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "83200"
    },
    {
        "Name": "N60 Storm: V2",
        "Id": 50150008,
        "Address": "0x00142E9C",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "6400"
    },
    {
        "Name": "N60 Storm: V3",
        "Id": 50150009,
        "Address": "0x00142E9C",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "16000"
    },
    {
        "Name": "N60 Storm: V4",
        "Id": 50150010,
        "Address": "0x00142E9C",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "48000"
    },
    {
        "Name": "N60 Storm: V5",
        "Id": 50150011,
        "Address": "0x00142E9C",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "57600"
    },
    {
        "Name": "Plasma Whip: V2",
        "Id": 50150012,
        "Address": "0x00142FDC",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "6400"
    },
    {
        "Name": "Plasma Whip: V3",
        "Id": 50150013,
        "Address": "0x00142FDC",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "25600"
    },
    {
        "Name": "Plasma Whip: V4",
        "Id": 50150014,
        "Address": "0x00142FDC",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "57600"
    },
    {
        "Name": "Plasma Whip: V5",
        "Id": 50150015,
        "Address": "0x00142FDC",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "105600"
    },
    {
        "Name": "Infector: V2",
        "Id": 50150016,
        "Address": "0x00142EBC",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "12800"
    },
    {
        "Name": "Infector: V3",
        "Id": 50150017,
        "Address": "0x00142EBC",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "25600"
    },
    {
        "Name": "Infector: V4",
        "Id": 50150018,
        "Address": "0x00142EBC",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "64000"
    },
    {
        "Name": "Infector: V5",
        "Id": 50150019,
        "Address": "0x00142EBC",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "121600"
    },
    {
        "Name": "Suck Cannon: V2",
        "Id": 50150020,
        "Address": "0x00142FFC",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "6400"
    },
    {
        "Name": "Suck Cannon: V3",
        "Id": 50150021,
        "Address": "0x00142FFC",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "19200"
    },
    {
        "Name": "Suck Cannon: V4",
        "Id": 50150022,
        "Address": "0x00142FFC",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "38400"
    },
    {
        "Name": "Suck Cannon: V5",
        "Id": 50150023,
        "Address": "0x00142FFC",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "76800"
    },
    {
        "Name": "Spitting Hydra: V2",
        "Id": 50150024,
        "Address": "0x00142EFC",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "9600"
    },
    {
        "Name": "Spitting Hydra: V3",
        "Id": 50150025,
        "Address": "0x00142EFC",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "28800"
    },
    {
        "Name": "Spitting Hydra: V4",
        "Id": 50150026,
        "Address": "0x00142EFC",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "57600"
    },
    {
        "Name": "Spitting Hydra: V5",
        "Id": 50150027,
        "Address": "0x00142EFC",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "96000"
    },
    {
        "Name": "Agents of Doom: V2",
        "Id": 50150028,
        "Address": "0x00142F3C",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "12800"
    },
    {
        "Name": "Agents of Doom: V3",
        "Id": 50150029,
        "Address": "0x00142F3C",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "32000"
    },
    {
        "Name": "Agents of Doom: V4",
        "Id": 50150030,
        "Address": "0x00142F3C",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "96000"
    },
    {
        "Name": "Agents of Doom: V5",
        "Id": 50150031,
        "Address": "0x00142F3C",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "192000"
    },
    {
        "Name": "Flux Rifle: V2",
        "Id": 50150032,
        "Address": "0x00142F9C",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "6400"
    },
    {
        "Name": "Flux Rifle: V3",
        "Id": 50150033,
        "Address": "0x00142F9C",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "19200"
    },
    {
        "Name": "Flux Rifle: V4",
        "Id": 50150034,
        "Address": "0x00142F9C",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "48000"
    },
    {
        "Name": "Flux Rifle: V5",
        "Id": 50150035,
        "Address": "0x00142F9C",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "92800"
    },
    {
        "Name": "Annihilator: V2",
        "Id": 50150036,
        "Address": "0x00142EDC",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "25600"
    },
    {
        "Name": "Annihilator: V3",
        "Id": 50150037,
        "Address": "0x00142EDC",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "76800"
    },
    {
        "Name": "Annihilator: V4",
        "Id": 50150038,
        "Address": "0x00142EDC",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "204800"
    },
    {
        "Name": "Annihilator: V5",
        "Id": 50150039,
        "Address": "0x00142EDC",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "396800"
    },
    {
        "Name": "Holo-Shield Glove: V2",
        "Id": 50150040,
        "Address": "0x00142F7C",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "4800"
    },
    {
        "Name": "Holo-Shield Glove: V3",
        "Id": 50150041,
        "Address": "0x00142F7C",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "14400"
    },
    {
        "Name": "Holo-Shield Glove: V4",
        "Id": 50150042,
        "Address": "0x00142F7C",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "43200"
    },
    {
        "Name": "Holo-Shield Glove: V5",
        "Id": 50150043,
        "Address": "0x00142F7C",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "86400"
    },
    {
        "Name": "Disk-Blade Gun: V2",
        "Id": 50150044,
        "Address": "0x00142F1C",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "22400"
    },
    {
        "Name": "Disk-Blade Gun: V3",
        "Id": 50150045,
        "Address": "0x00142F1C",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "67200"
    },
    {
        "Name": "Disk-Blade Gun: V4",
        "Id": 50150046,
        "Address": "0x00142F1C",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "195200"
    },
    {
        "Name": "Disk-Blade Gun: V5",
        "Id": 50150047,
        "Address": "0x00142F1C",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "387200"
    },
    {
        "Name": "Rift Inducer: V2",
        "Id": 50150048,
        "Address": "0x00142F5C",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "25600"
    },
    {
        "Name": "Rift Inducer: V3",
        "Id": 50150049,
        "Address": "0x00142F5C",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "76800"
    },
    {
        "Name": "Rift Inducer: V4",
        "Id": 50150050,
        "Address": "0x00142F5C",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "204800"
    },
    {
        "Name": "Rift Inducer: V5",
        "Id": 50150051,
        "Address": "0x00142F5C",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "396800"
    },
    {
        "Name": "Qwack-O-Ray: V2",
        "Id": 50150052,
        "Address": "0x0014301C",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "32000"
    },
    {
        "Name": "Qwack-O-Ray: V3",
        "Id": 50150053,
        "Address": "0x0014301C",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "96000"
    },
    {
        "Name": "Qwack-O-Ray: V4",
        "Id": 50150054,
        "Address": "0x0014301C",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "256000"
    },
    {
        "Name": "Qwack-O-Ray: V5",
        "Id": 50150055,
        "Address": "0x0014301C",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "512000"
    },
    {
        "Name": "RY3N0: V2",
        "Id": 50150056,
        "Address": "0x0014303C",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "640000"
    },
    {
        "Name": "RY3N0: V3",
        "Id": 50150057,
        "Address": "0x0014303C",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "1600000"
    },
    {
        "Name": "RY3N0: V4",
        "Id": 50150058,
        "Address": "0x0014303C",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "2880000"
    },
    {
        "Name": "RY3N0: V5",
        "Id": 50150059,
        "Address": "0x0014303C",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "4480000"
    },
    {
        "Name": "Mini-Turret Glove: V2",
        "Id": 50150060,
        "Address": "0x00142E34",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "12800"
    },
    {
        "Name": "Mini-Turret Glove: V3",
        "Id": 50150061,
        "Address": "0x00142E34",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "32000"
    },
    {
        "Name": "Mini-Turret Glove: V4",
        "Id": 50150062,
        "Address": "0x00142E34",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "64000"
    },
    {
        "Name": "Mini-Turret Glove: V5",
        "Id": 50150063,
        "Address": "0x00142E34",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "112000"
    },
    {
        "Name": "Lava Gun: V2",
        "Id": 50150064,
        "Address": "0x00142E24",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "19200"
    },
    {
        "Name": "Lava Gun: V3",
        "Id": 50150065,
        "Address": "0x00142E24",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "48000"
    },
    {
        "Name": "Lava Gun: V4",
        "Id": 50150066,
        "Address": "0x00142E24",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "86400"
    },
    {
        "Name": "Lava Gun: V5",
        "Id": 50150067,
        "Address": "0x00142E24",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "134400"
    },
    {
        "Name": "Shield Charger: V2",
        "Id": 50150068,
        "Address": "0x00142E38",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "70400"
    },
    {
        "Name": "Shield Charger: V3",
        "Id": 50150069,
        "Address": "0x00142E38",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "160000"
    },
    {
        "Name": "Shield Charger: V4",
        "Id": 50150070,
        "Address": "0x00142E38",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "307200"
    },
    {
        "Name": "Shield Charger: V5",
        "Id": 50150071,
        "Address": "0x00142E38",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "537600"
    },
    {
        "Name": "Bouncer: V2",
        "Id": 50150072,
        "Address": "0x00142E2C",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "80000"
    },
    {
        "Name": "Bouncer: V3",
        "Id": 50150073,
        "Address": "0x00142E2C",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "272000"
    },
    {
        "Name": "Bouncer: V4",
        "Id": 50150074,
        "Address": "0x00142E2C",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "592000"
    },
    {
        "Name": "Bouncer: V5",
        "Id": 50150075,
        "Address": "0x00142E2C",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "976000"
    },
    {
        "Name": "Plasma Coil: V2",
        "Id": 50150076,
        "Address": "0x00142E20",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "256000"
    },
    {
        "Name": "Plasma Coil: V3",
        "Id": 50150077,
        "Address": "0x00142E20",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "576000"
    },
    {
        "Name": "Plasma Coil: V4",
        "Id": 50150078,
        "Address": "0x00142E20",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "960000"
    },
    {
        "Name": "Plasma Coil: V5",
        "Id": 50150079,
        "Address": "0x00142E20",
        "CompareType": 1,
        "CheckType": 1,
        "CheckValue": "1408000"
    },
    {
        "Name": "Operation IRON SHIELD: Secure the Area",
        "Id": 50040006,
        "Address": "0x00142738",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Operation IRON SHIELD: Air Assault",
        "Id": 50040007,
        "Address": "0x00142739",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Operation IRON SHIELD: Turret Command",
        "Id": 50040008,
        "Address": "0x0014273A",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Operation IRON SHIELD: Under the Gun",
        "Id": 50040009,
        "Address": "0x0014273B",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Operation IRON SHIELD: Hit n' Run",
        "Id": 50040010,
        "Address": "0x0014273C",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Operation BLACK TIDE: The Battle of Blackwater City",
        "Id": 50120002,
        "Address": "0x0014273D",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Operation BLACK TIDE: The Bridge",
        "Id": 50120003,
        "Address": "0x0014273E",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Operation BLACK TIDE: Counterattack",
        "Id": 50120004,
        "Address": "0x00142C40",  # As same as Gravity-Boots event
        "CheckType": 0,
        "AddressBit": 3
    },
    {
        "Name": "Operation URBAN STORM: Countdown",
        "Id": 50260001,
        "Address": "0x00142747",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Operation URBAN STORM: Urban Combat",
        "Id": 50260002,
        "Address": "0x00142748",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Operation URBAN STORM: Tower Attack",
        "Id": 50260003,
        "Address": "0x00142749",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Operation URBAN STORM: Air Superiority",
        "Id": 50260004,
        "Address": "0x0014274A",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Operation URBAN STORM: Turret Command",
        "Id": 50260005,
        "Address": "0x0014274B",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Operation DEATH VALLEY: The Tunnels of Outpost X12",
        "Id": 50180004,
        "Address": "0x00142742",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Operation DEATH VALLEY: Ambush in Red Rock Valley",
        "Id": 50180005,
        "Address": "0x00142743",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Operation DEATH VALLEY: Assassination",
        "Id": 50180006,
        "Address": "0x00142744",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Operation DEATH VALLEY: Reclaim the Valley",
        "Id": 50180007,
        "Address": "0x00142745",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Operation DEATH VALLEY: X12 Endgame",
        "Id": 50180008,
        "Address": "0x00142746",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Qwark VidComic 1 Clear",
        "Id": 50310000,
        "Address": "0x00142734",
        "CheckType": 0,
        "AddressBit": 1
    },
    {
        "Name": "Qwark VidComic 2 Clear",
        "Id": 50330000,
        "Address": "0x00142734",
        "CheckType": 0,
        "AddressBit": 3
    },
    {
        "Name": "Qwark VidComic 3 Clear",
        "Id": 50340000,
        "Address": "0x00142734",
        "CheckType": 0,
        "AddressBit": 2
    },
    {
        "Name": "Qwark VidComic 4 Clear",
        "Id": 50320000,
        "Address": "0x00142734",
        "CheckType": 0,
        "AddressBit": 4
    },
    {
        "Name": "Qwark VidComic 5 Clear",
        "Id": 50350000,
        "Address": "0x00142734",
        "CheckType": 0,
        "AddressBit": 5
    },
    {
        "Name": "Destroy the Momma Tyhrranoid",
        "Id": 50090004,
        "Address": "0x0014271D",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Operation ISLAND STRIKE: Assault on Kavu Island",
        "Id": 50290000,
        "Address": "0x0014274C",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Operation ISLAND STRIKE: Dogfight over Kavu Island",
        "Id": 50290001,
        "Address": "0x0014274D",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Operation ISLAND STRIKE: Operation Thunderbolt",
        "Id": 50290002,
        "Address": "0x0014274F",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Operation ISLAND STRIKE: The Final Battle",
        "Id": 50290003,
        "Address": "0x00142750",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Skill Point: Stay Squeaky Clean",
        "Id": 50020005,
        "Address": "0x001D54B1",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Skill Point: Turn Up The Heat",
        "Id": 50030030,
        "Address": "0x001D54B4",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Skill Point: Strive for arcade perfection",
        "Id": 50030031,
        "Address": "0x001D54B2",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Skill Point: Beat Helga's best VR time",
        "Id": 50030032,
        "Address": "0x001D54B3",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Skill Point: Monkeying around",
        "Id": 50030033,
        "Address": "0x001D54B5",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Skill Point: Reflect on how to score",
        "Id": 50040011,
        "Address": "0x001D54B6",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Skill Point: Bugs to Birdie",
        "Id": 50050005,
        "Address": "0x001D54B7",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Skill Point: Bash the bug",
        "Id": 50070037,
        "Address": "0x001D54B8",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Skill Point: Be an eight time champ",
        "Id": 50070038,
        "Address": "0x001D54B9",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Skill Point: Flee Flawlessly",
        "Id": 50070039,
        "Address": "0x001D54BA",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Skill Point: Lights, camera action!",
        "Id": 50070040,
        "Address": "0x001D54BB",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Skill Point: Search for sunken treasure",
        "Id": 50080004,
        "Address": "0x001D54BC",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Skill Point: Be a Sharpshooter",
        "Id": 50090005,
        "Address": "0x001D54BD",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Skill Point: Get to the belt",
        "Id": 50110004,
        "Address": "0x001D54BE",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Skill Point: Bash the party",
        "Id": 50120005,
        "Address": "0x001D54BF",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Skill Point: Feeling Lucky",
        "Id": 50130005,
        "Address": "0x001D54C0",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Skill Point: You break it, you win it",
        "Id": 50140003,
        "Address": "0x001D54C1",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Skill Point: 2002 was a good year in the city",
        "Id": 50160001,
        "Address": "0x001D54C2",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Skill Point: Suck it up!",
        "Id": 50170004,
        "Address": "0x001D54C3",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Skill Point: Aim High",
        "Id": 50170005,
        "Address": "0x001D54C4",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Skill Point: Go for hang time",
        "Id": 50180009,
        "Address": "0x001D54B0",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Skill Point: Zap back at ya'",
        "Id": 50180010,
        "Address": "0x001D54C5",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Skill Point: Break the Dan",
        "Id": 50190002,
        "Address": "0x001D54C6",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Skill Point: Spread your germs",
        "Id": 50220001,
        "Address": "0x001D54C7",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Skill Point: Hit the motherload",
        "Id": 50280006,
        "Address": "0x001D54C8",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Skill Point: Pirate booty - set a new record for qwark",
        "Id": 50310003,
        "Address": "0x001D54C9",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Skill Point: Deja Q All over Again - set a new record for qwark",
        "Id": 50330003,
        "Address": "0x001D54CA",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Skill Point: Arriba Amoeba! - set a new record for qwark",
        "Id": 50340003,
        "Address": "0x001D54CB",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Skill Point: Shadow of the robot - set a new record for qwark",
        "Id": 50320003,
        "Address": "0x001D54CC",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Skill Point: The Shaming of the Q - set a new record for qwark",
        "Id": 50350003,
        "Address": "0x001D54CD",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "VR Gadget Training",
        "Id": 50030018,
        "Address": "0x00142765",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "VR: Warm Up",
        "Id": 50030019,
        "Address": "0x00142766",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "VR: Don't Look Down",
        "Id": 50030020,
        "Address": "0x00142767",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "VR: Speed Round",
        "Id": 50030021,
        "Address": "0x00142768",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "VR: Hot Stepper",
        "Id": 50030022,
        "Address": "0x00142769",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "VR: 90 Second Slayer",
        "Id": 50030023,
        "Address": "0x0014276A",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "VR: The Shocker",
        "Id": 50030024,
        "Address": "0x0014276B",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "VR: Wrench Beatdown",
        "Id": 50030025,
        "Address": "0x0014276C",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "VR: Nerves of Titanium",
        "Id": 50030026,
        "Address": "0x0014276D",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Received Mini-Turret Glove",
        "Id": 50080005,
        "Address": "0x00142CB5",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Received Lava Gun",
        "Id": 50080006,
        "Address": "0x00142CB1",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Received Shield Charger",
        "Id": 50080007,
        "Address": "0x00142CB6",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Received Bouncer",
        "Id": 50080008,
        "Address": "0x00142CB3",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Received Plasma Coil",
        "Id": 50080009,
        "Address": "0x00142CB0",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Escape Pod",
        "Id": 50170002,
        "Address": "0x00142C52",  # weird address but it's correct
        "CheckType": 0,
        "AddressBit": 2
    },
    {
        "Name": "Ratchet trophy",
        "Id": 50020006,
        "Address": "0x00142790",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Clank trophy",
        "Id": 50130006,
        "Address": "0x00142791",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Qwark trophy",
        "Id": 50190003,
        "Address": "0x00142792",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Dr Nefarious trophy",
        "Id": 50170006,
        "Address": "0x00142793",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Skrunch trophy",
        "Id": 50160005,
        "Address": "0x00142794",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Lawrence trophy",
        "Id": 50220001,
        "Address": "0x00142795",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Plumber trophy",
        "Id": 50050006,
        "Address": "0x00142796",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "Courtney Gears trophy",
        "Id": 50140004,
        "Address": "0x00142797",
        "CheckType": 0,
        "AddressBit": 0
    },
    {
        "Name": "AL trophy",
        "Id": 50090006,
        "Address": "0x00142798",
        "CheckType": 0,
        "AddressBit": 0
    },
    # Todo: Long term trophies
    # Titanium collector trophy 0x00142799
    # Skill master trophy 0x0014279a
    # Nano Finder trophy 0x0014279b
    # Annihilation Nation Champion trophy 0x0014279c
    # Friend of the Rangers trophy 0x0014279d
    # Omega Arsenal trophy 0x0014279e
    # Todo: Nanotech levels
    {
        "Name": "Nanotech Level Up - 11",
        "Id": 50250011,
        "Checks": [
            {
                "Address": "0x001A4E18",
                "CheckType": 0,
                "AddressBit": 0
            },
            {
                "Address": "0x001A7430",
                "CompareType": 0,
                "CheckType": 1,
                "CheckValue": "11"
            }
        ]
    },
]
