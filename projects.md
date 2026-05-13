---
title: Projects
nav_order: 3
---

# Projects

[Current Pursuits →](activedev)

---

## Featured

### ACCESS GRANTED
**Unity 6 · C# · URP · Released · WebGL + Windows**

A *Hackers*-inspired breach fantasy: your paddle is the access point into a terminal firewall; **command bricks** force strict **A→Z typing** under pressure while the ball keeps negotiating geometry you never fully simplify away.

<p align="center">
  <img src="/assets/images/access-granted.png" alt="ACCESS GRANTED CRT gameplay" style="max-width: 600px; width: 100%;">
</p>

- **Hybrid flow state machine (`GameFlowController`)** orchestrates Paddle/Ball ↔ **Typing Mode** swaps with unscaled timers so slowdown stays fair (`timeScale`-aware sequencing + pause recovery documented in code/architecture docs).  
- **URP barrel distortion feature** authored as **`ScriptableRendererFeature`/Render Graph** path paired with a **matching CRT bezel + scan shader** tuned to curvature—presentation reads intentional, not a single stock filter slapped onto UGUI.  
- **Dual-track failure authoring** separates **paddle misses vs typing fouls**, each gated by serialized counters with secret **HACKERMAN** allowances for spectacle runs.  
- **Tiered `WordList` ScriptableObjects** gate lexicon difficulty per campaign band and reduce back-to-back duplicates—shows content iteration without ripping core gameplay apart.  
- **Procedural HACKERMAN ring layout** interpolates constellation arcs/rungs in ellipse space (`HackermanRingLayout`) instead of brute grid snapping, layered above handcrafted tiers.  

<div class="itch-embed-wrap" style="text-align: center; margin: 1.5rem 0;">
  <iframe frameborder="0" src="https://itch.io/embed/4475328?linkback=true&amp;bg_color=060d06&amp;fg_color=b9c6e4&amp;link_color=00edd6&amp;border_color=084808" width="552" height="167" class="itch-embed"></iframe>
</div>

**[Play on Itch.io (browser)](https://goldleafinteractive.itch.io/access-granted)** · [Patch Notes v2](https://goldleafinteractive.itch.io/access-granted/devlog/1516113/patch-notes-v2) · Indie City Games · *The Movie The Game The Jam* (2026)

---

### Dread & Breakfast
**Unity 6 · C# · Beta / Post-jam · WebGL & Windows**

Top-down haunting strategy where **you deploy props and synergistic abilities**, read visitor fear spreadsheets on the fly, and clear a procedurally reconstructed B&B before dawn—Roguelike night modifiers, escalating cast pressure, FP meta-shop (“Box of Tricks”), latent ghost-drag interactions.

<p align="center">
  <img src="/assets/images/dread-and-breakfast.png" alt="Dread & Breakfast house layout" style="max-width: 600px; width: 100%;">
</p>

- **`HouseGenerator` pipeline** stitches templates, doorway connectivity, biased room mixes, inverse-scale prop anchors, heuristic prop placement (+ TV-vs-entry readability) rivaling coursework-level PCG assignments.  
- **`HumanAI` core** centralizes fear curves, patrol/pathing, reactive speech, flee “hurry,” and **panic ripple propagation** with presentation-driven sprite states—a single readable surface where a jam-scale sim outgrew scattered one-off scripts.  
- **17 `AbilitySO` Scriptable definitions** spanning instant AoE pings, lingering VFX corridors, cooldown/energy coupling, nightly upgrade drafts—all orchestrated behind a static **`GameEvents` bus**.  
- **Night escalation & meta currency** handled through `NightConstants`, spawn controllers, `FrightPointsBank` persistence bridging runs & shop churn.  

<div class="itch-embed-wrap" style="text-align: center; margin: 1.5rem 0;">
  <iframe frameborder="0" src="https://itch.io/embed/4471600?linkback=true&amp;bg_color=000000&amp;fg_color=e6d699&amp;link_color=fa5c5c&amp;border_color=282828" width="552" height="167" class="itch-embed"></iframe>
</div>

**[Play on Itch.io](https://goldleafinteractive.itch.io/dread-and-breakfast)** · *Mini Jam 208: Inverted* (2026) — [Update 1 · Energy bubbles](https://goldleafinteractive.itch.io/dread-and-breakfast/devlog/1489095/update-1-fixes-energy-bubbles-deep-freeze) · [v0.9.0 Beta UI overhaul](https://goldleafinteractive.itch.io/dread-and-breakfast/devlog/1501963/patch-notes-v090-beta)

---

### Trenchglow
**Unity (2D URP) · C# · In development · WebGL playable slice**

Tutorial slice for **Mini Jam 209 — Deep**. Underwater trenches where visibility is scarce: **timed sonar pings** widen then contract your mental map—stamina swim + boost pacing, puzzles via pressure pads + moving geometry, procedural hazards flagged in UI/tooling docs.

<p align="center">
  <img src="/assets/images/trenchglow.png" alt="Trenchglow underwater key art" style="max-width: 600px; width: 100%;">
</p>

- **`VisibilityController`** toggles shader-driven **`Trenchglow/PulseReveal`** globals versus explicit **WebGL fallback** (preserve shipping confidence on thinner GPUs vs editor-only fidelity).  
- **`DarknessRadialOverlay`** draws dual radial “holes”—persistent player bubble vs fired pulse ring—with serialized shader refs to dodge `Shader.Find` stripping nightmares.  
- **`PulsePolicy` runtime cloning (`CreateRuntimeInstance`)** avoids mutating authoring assets/session bleed—shows SO hygiene often skipped in jams.  
- **`TrenchChunk` kinematic actors** chained through UnityEvents: sliding/rotating geometry with reset hooks, sfx-synced durations, pooled impacts—great talking point for level scripting interviews.  

<div class="itch-embed-wrap" style="text-align: center; margin: 1.5rem 0;">
  <iframe frameborder="0" src="https://itch.io/embed/4513861?linkback=true&amp;bg_color=0a1628&amp;fg_color=cfe8ff&amp;link_color=f5a524&amp;border_color=1a3d5c" width="552" height="167" class="itch-embed"></iframe>
</div>

**[Play on Itch.io](https://goldleafinteractive.itch.io/trenchglow)** · Tutorial / tech-demo status — more trench levels inbound

---

### BREATHE Arcade
**Unity 6 · C# · 2D URP · Course capstone (“Emergent Game Technologies”) · WebGL + Windows**

Five breath-driven microgames (**Sailboat, Balloon, Bubbles, Stargaze, Skydive**) using a unified **hardware/mic/simulated pipeline**: Arduino tach-style serial stream feeding Unity’s smoothing & spin-down heuristics, procedural audio scaffolding, PB tracking, telemetry-friendly logging.

<p align="center">
  <img src="/assets/images/breathe-arcade.png" alt="BREATHE Arcade Skydive title art" style="max-width: 600px; width: 100%;">
</p>

- **`IBreathInput` + trio of concrete providers** isolate gameplay from sensor acquisition—WebGL clamps to simulated/mic responsibly.  
- **Fan pipeline**: background serial reader (`FanBreathInput`), COM probing, asymmetric filtering emulating inhale spikes vs fan inertia; docs note accurate sensor physics vs marketing labels.  
- **`BreathPowerSystem` merges calibration curves, smoothing, spin-down veto** so each minigame can bias intensity without forked controller code; Scriptable **`MinigameDefinition`** knobs keep tuning approachable.  

<div class="itch-embed-wrap" style="text-align: center; margin: 1.5rem 0;">
  <iframe frameborder="0" src="https://itch.io/embed/4475446?linkback=true&amp;bg_color=d6f5ff&amp;fg_color=0b2d3f&amp;link_color=ff4f6e&amp;border_color=93cdea" width="552" height="167" class="itch-embed"></iframe>
</div>

**[Play / download on Itch.io](https://goldleafinteractive.itch.io/breathe-arcade)** · Breath hardware doc pack available privately for employers on request · Public engineering notes summarized in-repo README/`HOW_IT_WORKS`

---

### OVERCLOCKED: Data Dash MAX
**Unreal Engine 5.7 · C++ & Blueprints · Released (PC & Arcade Cabinet)**

An endless runner for arcade cabinets **and** PC: race as an electric impulse through procedural neon corridors, lane-change + jump/slide choreography, escalating threat density, OVERCLOCK risk pacing, pickups, medals, themed presentation, offline leaderboards—all tuned for kiosk reliability.

<p align="center">
  <img src="/assets/images/overclocked-data-dash-max.png" alt="OVERCLOCKED: Data Dash MAX" style="max-width: 600px; width: 100%;">
</p>

- **Component-heavy C++ architecture** with cleanly separated spawning, pickups, locomotion tuning, thematic presentation swaps, leaderboard flows, menus that never assume mouse.  
- **40+ authored obstacle patterns** driven through data subsystems feeding spawn pools/time evolution—replayable without feeling “RNG noise.”  
- **Six interchangeable visual themes**, combo stack, EMP/magnet pickups, countdown clarity, HUD “MAX SPEED” feedback when difficulty caps—all tuned post-jam toward cabinet & PC parity.  

<div class="itch-embed-wrap" style="text-align: center; margin: 1.5rem 0;">
  <iframe frameborder="0" src="https://itch.io/embed/4278897?linkback=true&amp;bg_color=000000&amp;fg_color=fffcbc&amp;link_color=46ffd4&amp;border_color=979797" width="552" height="167" class="itch-embed"></iframe>
</div>

**[Windows build on Itch.io](https://goldleafinteractive.itch.io/overclocked-ddm)** · [Patch Notes / v1.1.0 recap](https://goldleafinteractive.itch.io/overclocked-ddm/devlog/1379247/v110-patch-notes-overclocked-ddm) · [Watch Trailer](https://www.youtube.com/watch?v=dI9Ctq9LkLs)

---

### Quantum Tether
**Unity · C# · Released**

A 2D roguelike sidescroller built around precision movement, grappling physics, and momentum-based traversal.

<p align="center">
  <img src="/assets/images/quantum-tether.png" alt="Quantum Tether" style="max-width: 600px; width: 100%;">
</p>

- Designed a **vector-based grappling system** for dynamic swinging between anchor points
- Built a **modular upgrade framework** (10+ abilities: dash cooldowns, dual threads, range modifiers)
- Implemented **procedural anchor generation** using parametric math to vary level rhythm
- Developed **player movement state handling**, responsive UI, HUD, scoring, collectibles, and difficulty scaling

**[View on Itch.io](https://goldleafinteractive.itch.io/quantum-tether)** · [Watch Trailer](https://www.youtube.com/watch?v=RNs4yKPhfGM)

---

### Mysteries of Tupni
**Unreal Engine 5 · Blueprints · Prototype**

A third-person fantasy adventure with gameplay systems, inventory architecture, and interactive environments.

<p align="center">
  <img src="/assets/images/mysteries-of-tupni.png" alt="Mysteries of Tupni" style="max-width: 600px; width: 100%;">
</p>

- Created **interactive world elements** (doors, chests, teleporters, UI prompts)
- Built a **Data Table–driven inventory system** with drag/drop, tooltips, and persistence
- Integrated quests and NPC interactions to support player progression

**[View on Itch.io](https://goldleafinteractive.itch.io/mysteries-of-tupni)** · [Watch Demo](https://www.youtube.com/watch?v=BQl2MkPxUl4)

---

### Ginger Shroom Journey
**Unity · C# · Steam**

A fully released 2D adventure game with responsibility for core gameplay systems, UI, and optimization.

<p align="center">
  <img src="/assets/images/ginger-shroom-journey.png" alt="Ginger Shroom Journey" style="max-width: 600px; width: 100%;">
</p>

- Implemented **player movement, physics, enemies, and interactions**
- Built UI, HUD, camera systems, and environmental triggers
- Managed **Steamworks integration and publishing pipeline**

**[Get on Steam (Free)](https://store.steampowered.com/app/3023100/Ginger_Shroom_Journey/)** · [Watch Trailer](https://www.youtube.com/watch?v=-LGDr3DaUB8)

---

## Other Work

### Void Knights
**Unreal Engine 5 · Blueprints**

A Persona-inspired RPG prototype centered on dual-world traversal and psychic mechanics.

<p align="center">
  <img src="/assets/images/void-knights.png" alt="Void Knights" style="max-width: 600px; width: 100%;">
</p>

- Built a **world-shifting system** between Reality and the Void Verse
- Implemented **telekinetic object manipulation** using physics and vector targeting
- Developed **modular AI patrol and sensing behaviors**; partnered with designers to iterate on stealth and puzzle gameplay
- Built exploration systems, NPC behaviors, and branching dialogue

**[View on Itch.io](https://goldleafinteractive.itch.io/void-knights)**

---

### Medieval Shop Game
**C++ · Windows**

A text-based shop simulation exploring low-level architecture and game systems in C++.

<p align="center">
  <img src="/assets/images/medieval-shop-game.png" alt="Medieval Shop Game" style="max-width: 600px; width: 100%;">
</p>

- Implemented **inventory, negotiation, branching dialogue**, and state-driven interactions
- Built custom **console UI with ASCII rendering and input handling**
- Integrated **DirectSound audio** for music and effects
- Architected with RAII, smart pointers, modular state machines
- Full **CMake/Ninja → resource packing → installer → signed .exe** pipeline

**[View on Itch.io](https://goldleafinteractive.itch.io/medieval-shop-game)**

---

### Million Miles Deep
**Unreal Engine 5 · Blueprints**

High-intensity 2D bullet hell set on an alien ocean world.

<p align="center">
  <img src="/assets/images/million-miles-deep.png" alt="Million Miles Deep" style="max-width: 260px; width: 48%; display: inline-block;">
  <img src="/assets/images/million-miles-deep-2.png" alt="Million Miles Deep" style="max-width: 260px; width: 48%; display: inline-block;">
</p>

- Designed **enemy AI patterns** and attack behaviors
- Implemented **projectile systems** and optimized collision handling
- Built menus, HUD, and responsive UI

**[View on Itch.io](https://goldleafinteractive.itch.io/million-miles-deep)**

---

### Ragdoll Plainly Perilous
**Unreal Engine 5 · Blueprints**

An experimental physics-driven game exploring ragdoll-based movement.

<p align="center">
  <img src="/assets/images/ragdoll-plainly-perilous.png" alt="Ragdoll Plainly Perilous" style="max-width: 600px; width: 100%;">
</p>

- Built **ragdoll-controlled player mechanics** using UE physics
- Designed **interactive, physics-driven environments**
- Optimized collision stability for consistent behavior

**[View on Itch.io](https://goldleafinteractive.itch.io/ragdoll-plainly-perilous)** · [Watch Demo](https://www.youtube.com/watch?v=GfrDt166KZI)

---

### Crimson Eclipse
**Unreal Engine 5 · Blueprints**

A 2D side-scroller horror project focused on tension, pacing, and survival-style encounters.

<p align="center">
  <img src="/assets/images/crimson-eclipse.png" alt="Crimson Eclipse" style="max-width: 600px; width: 100%;">
</p>

- Implemented enemy behaviors and encounter logic for horror pacing
- Built interactive environment systems and gameplay triggers
- Developed UI/HUD elements for player state communication

**[View on Itch.io](https://goldleafinteractive.itch.io/crimson-eclipse)** · [Watch Demo](https://www.youtube.com/watch?v=R7KG3vuqHx4)

---

## More

Shorter prototypes and jam-complete builds (~16 playable loops shipped to date counting coursework + jams + ongoing slices):

- **I AM INEVITABLE** (UE5 · Blueprint-heavy vertical slice · Chillennium 2026 jam) — “failure strengthens” ascent loop, traversal scaling, retro post stack; **[Windows download · Itch.io](https://goldleafinteractive.itch.io/i-am-inevitable)**
- **Doors n' Dice** (UE5) — 2D platformer with chance-based door outcomes · [Itch.io](https://goldleafinteractive.itch.io/doors-n-dice)
- **Escape Control** (UE5) — Top-down sci-fi shooter · listed on [itch profile](https://goldleafinteractive.itch.io/)
- **Void Knights / coursework prototypes** — additional classroom vertical slices & mechanics labs (some unlisted class submission captures may go public later for archival depth)

---

[← Back to Home](index)
