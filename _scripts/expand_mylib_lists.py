"""
One-off generator: writes mylib.md with large candidate game lists (1995+ focus).
User prunes entries they did not play.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "mylib.md"

HEADER = """---
title: My Library
nav_order: 4
---

# Games That Shaped Me

I grew up reading popular fantasy and fiction novels alongside every kind of game I could get to run. Games edged ahead as my favorite medium once I saw how purposeful mechanics braid with pacing, design, substantive narrative and cohesive worlds—immersive clarity and depth land harder that way than plain prose or passive screenings reliably reach, even weighed against standout fiction. Something I spotted early and never shook; many games molded my perspectives growing up, much like movies and literature.

Rough backlog below—meaningful hours that will steer what I prototype or publish next.

---
"""

NINTENDO_AA = """## Nintendo Systems (NES, SNES, N64, GameCube, Wii, Wii U, Switch, DS, 3DS, GBA, Game Boy)

### Action-Adventure / RPG
- The Legend of Zelda: A Link to the Past
- The Legend of Zelda: Link's Awakening / DX / (2019)
- The Legend of Zelda: Oracle of Ages / Oracle of Seasons
- The Legend of Zelda: Ocarina of Time / Master Quest
- The Legend of Zelda: Majora's Mask
- The Legend of Zelda: Four Swords Adventures
- The Legend of Zelda: The Minish Cap
- The Legend of Zelda: Twilight Princess
- The Legend of Zelda: Skyward Sword / HD
- The Legend of Zelda: Breath of the Wild
- The Legend of Zelda: Tears of the Kingdom
- The Legend of Zelda: Phantom Hourglass
- The Legend of Zelda: Spirit Tracks
- The Legend of Zelda: Wind Waker HD
- Metroid Fusion
- Metroid: Zero Mission
- Metroid Prime / Remastered
- Metroid Prime 2: Echoes
- Metroid Prime 3: Corruption
- Metroid: Other M
- Metroid Dread
- Super Metroid
- Metroid II: Return of Samus / Samus Returns (3DS)
- Castlevania: Symphony of the Night (GBA/PSN re-releases played on Nintendo counts)
- Pokémon Red / Blue / Yellow / Gold / Silver / Crystal / Ruby / Sapphire / Emerald / FireRed / LeafGreen / Diamond / Pearl / Platinum / HeartGold / SoulSilver / Black / White / BW2 / X / Y / ORAS / Sun / Moon / USUM / Let's Go / Sword / Shield / Scarlet / Violet
- Pokémon Colosseum / XD: Gale of Darkness
- Pokémon Mystery Dungeon (Explorers, etc.)
- Golden Sun / The Lost Age / Dark Dawn
- Xenoblade Chronicles / X / 2 / Torna / 3
- Fire Emblem: The Blazing Blade (GBA) / Sacred Stones / Path of Radiance / Radiant Dawn / Awakening / Fates / Echoes / Three Houses / Engage
- Fire Emblem Warriors / Three Hopes
- Paper Mario / The Thousand-Year Door / Super Paper Mario / Sticker Star / Color Splash / The Origami King
- Mario & Luigi: Superstar Saga / Partners in Time / Bowser's Inside Story / Dream Team / Paper Jam
- Advance Wars 1+2: Re-Boot Camp / Days of Ruin / Dual Strike
- Tales of Symphonia / Symphonia Dawn of the New World
- Baten Kaitos / Origins
- Okami (Wii / Switch)
- Monster Hunter Tri / 3 Ultimate / 4 Ultimate / Generations / Generations Ultimate / Rise / Stories / Stories 2 / World (Switch)
- Bravely Default / Second / Bravely Default II
- Octopath Traveler / II
- Triangle Strategy
- Live A Live (remake)
- Dragon Quest VIII (3DS) / IX / XI S / Builders / Builders 2 / Heroes (Switch)
- Shin Megami Tensei III (HD) / IV / Apocalypse / Strange Journey / V
- Tokyo Mirage Sessions #FE / Encore
- Persona Q / Q2 / Persona 5 Strikers / Persona 4 Arena Ultimax (Switch)
- Luigi's Mansion / Dark Moon / 3
- Kid Icarus: Uprising
- Ever Oasis
- Cadence of Hyrule
- Hyrule Warriors / Age of Calamity
- Mario + Rabbids Kingdom Battle / Sparks of Hope
- Astral Chain
- Bayonetta 2 / 3 (Switch)
- Daemon X Machina
- Pikmin 1 / 2 / 3 / 4
- Animal Crossing (GC) / Wild World / City Folk / New Leaf / New Horizons
- Resident Evil (REmake) / Zero / 4 / Revelations / Revelations 2 (Switch)
- The Witcher 3: Wild Hunt (Switch)
- Hollow Knight / Silksong (when released)
- Ori and the Blind Forest / Will of the Wisps (Switch)
- Cuphead
- Hades
- Dead Cells
- Slay the Spire
- Shovel Knight series
- Celeste
- Stardew Valley
- Undertale / Deltarune (Switch/PC)
- Eastward
- Tunic
"""

NINT_PLAT = """### Platformers / Party / Racing
- Super Mario 64 / Sunshine / Galaxy / Galaxy 2 / 3D Land / 3D World + Bowser's Fury / Odyssey
- Super Mario Bros. Deluxe / Advance series / New SMB (DS, Wii, Wii U, U Deluxe)
- Donkey Kong Country / DKC 2 / DKC 3 / Returns / Tropical Freeze
- Donkey Kong 64 / Jungle Beat
- Kirby's Dream Land series / Adventure / Super Star / 64 / Epic Yarn / Return to Dream Land / Triple Deluxe / Planet Robobot / Star Allies / Forgotten Land / Dream Buffet
- Kirby Air Ride
- Yoshi's Story / Island DS / Woolly World / Crafted World
- Star Fox 64 / Adventures / Assault / Zero
- Mario Kart 64 / Super Circuit / Double Dash / DS / Wii / 7 / 8 / 8 Deluxe / Tour (mobile)
- Mario Party (N64–Switch major entries)
- Super Smash Bros. Melee / Brawl / Wii U / Ultimate
- Rare Replay-exposed titles if played via NSO (Banjo-Kazooie / Tooie, etc.)
- Sonic Adventure DX / Sonic Colors / Sonic Lost World / Sonic Mania / Sonic Frontiers (Switch)
- Crash Bandicoot N. Sane Trilogy / Crash 4 (Switch)
- Spyro Reignited Trilogy (Switch)
- Mega Man X / X2 / X3 / legacy collections
- Mega Man Zero / ZX Legacy Collection
- Shovel Knight (also platformer)
- Rayman Legends (Wii U / Switch)
- New Super Lucky's Tale / Super Lucky's Tale
- Banjo-Kazooie: Nuts & Bolts (if played)
- Conker's Bad Fur Day (N64 / Rare Replay)
"""

NINT_LIC = """### Licensed / Kids / Adaptations / Misc
- Lego Star Wars / Complete Saga / The Skywalker Saga / many Lego franchise games
- Spider-Man 2 (GC/PS2 era ports)
- Star Wars Rogue Squadron series (N64/GC)
- Harry Potter (Chamber of Secrets through Deathly Hallows era console games)
- Lord of the Rings (Third Age, etc. on GC/GBA)
- GoldenEye 007 (N64 / future re-release)
- King Kong / movie tie-ins (GC era)
- Transformers (various)
- Disney Infinity (if played)
- Naruto: Clash of Ninja / Storm (if on Nintendo)
- Avatar: The Last Airbender (licensed)
- SpongeBob / Nickelodeon fighters
- Cars / Pixar games
- Toy Story / licensed platformers
- Tony Hawk's Pro Skater (Switch remasters)
- SSX Tricky / 3 (GC)
- F-Zero X / GX
- 1080° Avalanche
- Wave Race 64 / Blue Storm
- Excitebike 64 / Excite Truck / Bots
- Punch-Out!! (Wii)
- Wii Sports / Resort
- Nintendo Land
- ARMS
- Splatoon / Splatoon 2 / Splatoon 3
- Ring Fit Adventure
"""

SONY_AA = """## Sony Systems (PS1, PS2, PSP, PS Vita, PS3, PS4, PS5)

### Action-Adventure / RPG
- God of War (2005) / II / III / Ascension / (2018) / Ragnarök
- Shadow of the Colossus / ICO (remasters)
- MediEvil / Remake
- Spider-Man (PS1) / 2 / 3 / Web of Shadows / Shattered Dimensions / Edge of Time
- Marvel's Spider-Man / Miles Morales / Spider-Man 2 (PS5)
- Final Fantasy VII / VIII / IX / X / X-2 / XII / XIII trilogy / XV / VII Remake / Rebirth
- Final Fantasy Tactics (PS1/PSP)
- Kingdom Hearts / II / Birth by Sleep / Dream Drop Distance / III / Melody of Memory
- Shadow Hearts / Covenant
- Vagrant Story
- Parasite Eve
- Suikoden I / II (if played)
- Persona 3 / 4 / 5 / Royal / Strikers
- Dragon Quest VIII / XI (PS)
- Tales of series on PlayStation (Symphonia-related, Vesperia, Arise, etc.)
- Bloodborne
- Demon's Souls (PS3 / PS5 remake)
- Elden Ring (PS)
- Dark Souls / II / III (PS)
- Sekiro: Shadows Die Twice (PS)
- Horizon Zero Dawn / Forbidden West
- Ghost of Tsushima / Director's Cut
- The Last of Us / Part II / Part I remake
- Uncharted 1–4 / Lost Legacy / Collection
- Ratchet & Clank (PS2–PS5 major entries) / Rift Apart
- Jak and Daxter trilogy
- Sly Cooper trilogy / Thieves in Time
- Infamous / Second Son / First Light
- Gravity Rush / 2
- Ico
- Nier / Nier: Automata / Replicant ver.1.22
- Bayonetta / Vanquish (PS)
- Devil May Cry HD / 4 / 5 / DmC
- Metal Gear Solid (PS1–PS4 as applicable)
- Silent Hill 1–4 / others
- Resident Evil 1–6 / 7 / Village / remakes
- Assassin's Creed (many console entries)
- Batman: Arkham Asylum / City / Knight / Origins
- Middle-earth: Shadow of Mordor / War
- Horizon (above)
- Death Stranding / Director's Cut
- Returnal
- Astro's Playroom / Bot
- Control (PS4/5)
- Star Wars Jedi: Fallen Order / Survivor
- Hogwarts Legacy (PS)
- Cyberpunk 2077 (PS)
- Mass Effect Legendary Edition (PS)
- Dragon's Dogma / Dark Arisen / II (PS)
- Yakuza / Like a Dragon series (PS)
- Judgment / Lost Judgment
- Ghostwire: Tokyo
- Days Gone
- Until Dawn / The Quarry / Dark Pictures Anthology
- Heavy Rain / Beyond: Two Souls / Detroit: Become Human
"""

SONY_SHOOT = """### Shooters / Tactical / Looter
- Killzone (PS2–PS4)
- Resistance: Fall of Man / 2 / 3
- SOCOM series
- Tom Clancy's Splinter Cell / Rainbow Six / Ghost Recon (PS entries)
- Call of Duty (Modern Warfare trilogy, Black Ops, etc. on PS)
- Battlefield (3, 4, 1, V, 2042 on PS)
- Medal of Honor series (PS era)
- Wolfenstein: The New Order / II / Youngblood (PS)
- DOOM / DOOM Eternal (PS)
- Destiny / Destiny 2
- Borderlands 1–3 / Wonderlands (PS)
- Titanfall 2 (PS)
- Apex Legends
- Overwatch / 2
- Paladins
- Warframe
- The Division / 2
- Left 4 Dead (if via BC) / Back 4 Blood
- Metro series (PS)
- Far Cry series (PS)
- Crysis Remastered Trilogy
- Rainbow Six Extraction
- Helldivers / Helldivers 2
"""

SONY_MISC = """### Fighting / Racing / Rhythm / Misc
- Tekken 3–8 (as played)
- Street Fighter III / IV / V / 6
- Mortal Kombat (PS era entries)
- SoulCalibur II–VI
- Guilty Gear Strive / Xrd
- Gran Turismo 3–7 / Sport
- WipEout series
- Twisted Metal (PS1–PS3)
- Guitar Hero / Rock Band era
- PaRappa / Um Jammer Lammy
- Patapon
- LocoRoco
- LittleBigPlanet 1–3
- Dreams
- Catherine / Full Body
- Katamari Damacy REROLL
- Crash Team Racing / Nitro-Fueled
- Spyro (PS1 classics)
- Tony Hawk's Pro Skater 1+2 (PS)
- Need for Speed (Underground through modern)
- Burnout 3 / Revenge / Paradise
"""

MS_SHOOT = """## Microsoft Systems (Xbox, Xbox 360, Xbox One, Series X|S)

### Shooters / Action RPG / Looter
- Halo: CE / 2 / 3 / ODST / Reach / 4 / 5 / Infinite
- Gears of War 1–5 / Judgment / Tactics
- Perfect Dark Zero / Perfect Dark (360)
- Call of Duty (all Xbox-era entries)
- Battlefield: Bad Company 1 & 2 / 3 / 4 / 1 / Hardline / V / 2042
- Titanfall / Titanfall 2
- Destiny / Destiny 2
- The Division / 2
- Left 4 Dead / 2
- Borderlands series
- Fallout 3 / New Vegas / 4 / 76
- The Elder Scrolls III / IV / V / Online
- Starfield
- Mass Effect trilogy / Andromeda / Legendary Edition
- Cyberpunk 2077
- Doom / Doom Eternal
- Wolfenstein series
- Metro series
- Remnant: From the Ashes / II
- Outriders
"""

MS_MULTI = """### Multiplayer / Live / Co-op
- Sea of Thieves
- Grounded
- Deep Rock Galactic
- Apex Legends
- Fortnite
- Minecraft (Bedrock)
- Roblox (if counts)
- Among Us
- Phasmophobia
- Lethal Company
- Valheim
- Overwatch 2
- Rainbow Six Siege
- Smite
- Paladins
- Warframe
- Elder Scrolls Online
- Lost Ark
- New World
- Diablo III / IV
- Path of Exile
"""

MS_OPEN = """### Open World / Adventure / Misc
- Fable / II / III / Anniversary
- Forza Horizon 3–5 / Motorsport series
- Microsoft Flight Simulator
- Sunset Overdrive
- Crackdown 1–3
- State of Decay / 2
- Obsidian: The Outer Worlds / Avowed (when out) / Grounded
- Psychonauts / Psychonauts 2
- Ori and the Blind Forest / Will of the Wisps
- Hellblade: Senua's Sacrifice
- Hi-Fi Rush
- Pentiment
- As Dusk Falls
- Telltale Walking Dead / Wolf Among Us (Xbox)
- Grand Theft Auto III–V / Online / Trilogy DE
- Red Dead Redemption / II / Online
- Assassin's Creed (many)
- Watch Dogs 1–3 / Legion
- Far Cry series
- Just Cause 2–4
- Saints Row series
- Mafia series
- Sleeping Dogs
- Mad Max
- Middle-earth series
- Batman Arkham series
- Elden Ring
- Star Wars Jedi series
- Hogwarts Legacy
- Atomic Heart
- No Man's Sky
- Subnautica / Below Zero
- The Forest / Sons of the Forest
- ARK: Survival Evolved / Ascended
- Conan Exiles
- Rust (Xbox)
- DayZ
- PUBG: Battlegrounds
"""

PC_MELEE = """## PC (Windows & Mac / Linux)

### Melee / Souls-likes / Character Action
- Dark Souls: Prepare to Die / Remastered / II / III
- Elden Ring
- Sekiro: Shadows Die Twice
- Bloodborne (if streamed/PS)
- Demon's Souls
- Lies of P
- Wo Long: Fallen Dynasty
- Nioh / Nioh 2
- Mortal Shell
- Remnant I / II
- Chivalry: Medieval Warfare / Chivalry 2
- Mordhau
- For Honor
- Mount & Blade: Warband / Bannerlord
- Kingdom Come: Deliverance
- Hellish Quart
- Half-Sword (early)
- Devil May Cry series (PC)
- Bayonetta / Vanquish (PC)
- Metal Gear Rising: Revengeance
- Ryse: Son of Rome
"""

PC_SHOOT = """### Shooters / Tactical / Extraction
- Half-Life / Opposing Force / Blue Shift / 2 / Episodes / Alyx
- Counter-Strike 1.6 / Source / GO / 2
- Team Fortress 2
- Left 4 Dead / 2
- Portal / 2
- DOOM (1993+) / DOOM II / DOOM 3 / DOOM (2016) / Eternal / Quake series
- Wolfenstein 3D through modern
- Rainbow Six (Rogue Spear through Siege)
- SWAT 4
- Insurgency / Sandstorm
- Squad
- Hell Let Loose
- Post Scriptum / Beyond The Wire
- ARMA 3
- Operation Flashpoint / Dragon Rising
- Ghost Recon (PC)
- Splinter Cell (PC)
- Battlefield 1942 through 2042
- Call of Duty (PC entries)
- Titanfall 2
- Apex Legends
- Valorant
- Overwatch / 2
- Paladins
- Escape from Tarkov
- Hunt: Showdown
- The Cycle: Frontier
- Marauders
- Ready or Not
- GTFO
- Deep Rock Galactic
- PayDay 2 / 3
- Killing Floor / 2
- Serious Sam series
- Painkiller
- Black Mesa
- ULTRAKILL
- Prodeus
- Bright Memory: Infinite
"""

PC_RPG = """### RPG / ARPG / CRPG / Immersive Sim
- Baldur's Gate / II / III
- Planescape: Torment / Icewind Dale / Neverwinter Nights
- Pillars of Eternity / II
- Divinity: Original Sin / II
- Pathfinder: Kingmaker / Wrath of the Righteous
- Tyranny
- Torment: Tides of Numenera
- Disco Elysium
- The Witcher / II / III / expansions
- Gothic / Risen / Elex (Piranha Bytes)
- Kingdoms of Amalur: Reckoning / Re-Reckoning
- Dragon Age: Origins / II / Inquisition
- Mass Effect trilogy / Andromeda
- Star Wars: Knights of the Old Republic / II
- Jade Empire
- Deus Ex / Invisible War / Human Revolution / Mankind Divided
- Prey (2017)
- System Shock / System Shock 2 / remake
- BioShock / 2 / Infinite / Collection
- Dishonored / 2 / Death of the Outsider
- Thief: The Dark Project / II / Deadly Shadows / (2014)
- Vampire: The Masquerade – Bloodlines
- Fallout 1 / 2 / Tactics / 3 / New Vegas / 4 / 76
- The Elder Scrolls II–V / Online
- Starfield
- Cyberpunk 2077
- ELEX / II
- GreedFall
- Outward
- Two Worlds / II
- Risen series
- Dark Messiah of Might and Magic
- ARK / Conan / Valheim / V Rising (survival-RPG adjacent)
- Monster Hunter: World / Rise (PC)
- Nioh / II (PC)
- Code Vein
- Scarlet Nexus
- Tales of Arise (PC)
- Final Fantasy XIV / XI (if played on PC)
- Lost Ark
- Path of Exile / Diablo II Resurrected / III / IV
- Grim Dawn
- Last Epoch
- Torchlight / II / III
- Sacred / II
"""

PC_STORY = """### Narrative / Adventure / Walking Sim / Horror
- The Last of Us (if PC)
- Detroit: Become Human / Heavy Rain / Beyond: Two Souls
- Life is Strange / Before the Storm / True Colors
- Telltale: Walking Dead / Wolf Among Us / Tales from the Borderlands
- What Remains of Edith Finch
- Firewatch
- Gone Home
- Dear Esther
- The Stanley Parable / Ultra Deluxe
- Outer Wilds
- Return of the Obra Dinn
- Her Story / Telling Lies / Immortality
- Alan Wake / AW2
- Control
- Quantum Break
- Resident Evil (PC ports)
- Silent Hill (PC / emulation)
- Dead Space / remake / 2 / 3
- Alien: Isolation
- SOMA
- Amnesia series
- Outlast / 2
- Visage
- Phasmophobia
- Lethal Company
- Little Nightmares / II
- Inside / Limbo
- Little Misfortune / Fran Bow (if played)
- Doki Doki Literature Club
"""

PC_STRAT = """### Strategy / 4X / RTS / City Builders / Roguelites
- Age of Empires II–IV / Definitive Editions
- StarCraft / Brood War / II
- Warcraft III / Reforged
- Command & Conquer / Red Alert / Generals / remasters
- Company of Heroes / II / III
- Total War (many historical / Warhammer)
- Civilization III–VI
- Crusader Kings II / III
- Europa Universalis IV
- Stellaris
- Cities: Skylines / II
- SimCity 4 / 2013
- Factorio
- Satisfactory
- Dyson Sphere Program
- RimWorld
- Dwarf Fortress (Steam)
- Oxygen Not Included
- Terraria
- Starbound
- Core Keeper
- Noita
- Risk of Rain / 2
- Enter the Gungeon
- The Binding of Isaac / Rebirth / Repentance
- Hades
- Dead Cells
- Slay the Spire
- Balatro
- Inscryption
- Monster Train
- FTL: Faster Than Light
- Into the Breach
- XCOM: Enemy Unknown / 2 / Chimera Squad
- Phoenix Point
- Mutant Year Zero
- Wartales
- Darkest Dungeon / II
"""

PC_COOP = """### Co-op / Sandbox / Vehicle / Sports (PC)
- Minecraft Java / Bedrock
- Terraria / Starbound
- Valheim
- Project Zomboid
- 7 Days to Die
- Rust
- ARK
- Space Engineers
- Satisfactory (co-op)
- It Takes Two / A Way Out
- Portal 2 (co-op)
- Deep Rock Galactic
- Warhammer: Vermintide / Darktide
- Left 4 Dead 2
- GTFO
- Ghost Exorcism Inc. / Phasmo
- Sea of Thieves (PC)
- Rocket League
- Forza Horizon (PC)
- Assetto Corsa / Competizione
- BeamNG.drive
- Euro Truck Simulator 2 / American Truck Simulator
- Farming Simulator series
- CS2 / Valorant (comp)
- League of Legends / Dota 2 (if played)
- Smite
- Multiversus
- Fall Guys
- Among Us
"""

FOOTER = """---

**Closing** — Headings prioritize **easy skimming**, not airtight chronology. Bundled names and blurred platform lines signal **influence fingerprints**, not a consumer CV—or a tally of completions.

---
"""

def main() -> None:
    parts = [
        HEADER,
        NINTENDO_AA,
        NINT_PLAT,
        NINT_LIC,
        SONY_AA,
        SONY_SHOOT,
        SONY_MISC,
        MS_SHOOT,
        MS_MULTI,
        MS_OPEN,
        PC_MELEE,
        PC_SHOOT,
        PC_RPG,
        PC_STORY,
        PC_STRAT,
        PC_COOP,
        FOOTER,
    ]
    OUT.write_text("\n".join(parts), encoding="utf-8", newline="\n")
    print(f"Wrote {OUT} ({len(OUT.read_text(encoding='utf-8'))} chars)")


if __name__ == "__main__":
    main()
