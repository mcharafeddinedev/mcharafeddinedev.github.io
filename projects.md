---
title: My Projects
description: "Playable Unity and Unreal projects by Marwan Charafeddine, including Access Granted, Dread & Breakfast, BREATHE Arcade, OVERCLOCKED, and Trenchglow."
nav_order: 2
---

# Game Projects

[Current Pursuits →](activedev)

---

## Featured

### ACCESS GRANTED
**Unity 6 · C# · URP · Released · WebGL + Windows**

Released solo project that blends brick-breaker play with reactive typing challenges inside a CRT-terminal aesthetic.

<p align="center">
  <img src="/assets/images/access-granted.png" alt="Access Granted CRT-style gameplay" style="max-width: 600px; width: 100%;">
</p>

- Built the paddle/ball loop, command-brick slow motion, typed prompt resolution, menus, and WebGL/Windows release flow.
- Tuned separate failure tracks for ball drops and mistyped commands, with three difficulty tiers across levels 1-15.
- Used barrel distortion, scanlines, UI styling, and patch iteration to keep the CRT identity readable during play.

<div class="itch-embed-wrap" style="text-align: center; margin: 1.5rem 0;">
  <iframe id="itch-embed-access-granted-projects" title="Itch.io: Access Granted" frameborder="0" loading="lazy" src="https://itch.io/embed/4475328?linkback=true&amp;border_width=2&amp;bg_color=060d06&amp;fg_color=b9c6e4&amp;link_color=00edd6&amp;border_color=084808" width="552" height="167" class="itch-embed"></iframe>
</div>

**[Play In Browser](https://goldleafinteractive.itch.io/access-granted)** · [Patch Notes v2](https://goldleafinteractive.itch.io/access-granted/devlog/1516113/patch-notes-v2)

---

### Dread & Breakfast
**Unity 6 · C# · Beta / Post-jam · WebGL & Windows**

Top-down ghost haunting simulator about scaring guests through escalating nights, shuffled rooms, haunt abilities, and a replayable fright economy.

<p align="center">
  <img src="/assets/images/dread-and-breakfast.png" alt="Dread & Breakfast floor plan gameplay" style="max-width: 600px; width: 100%;">
</p>

- Built PCG-style house layout support with readable room templates, props, and guest setups for night-to-night variety.
- Centralized guest behavior so visitors can wander, chatter, escalate fear, and trigger panic chains.
- Authored **17** reusable haunt abilities, persistent meta-shop progress, and event-driven feedback for browser play.

<div class="itch-embed-wrap" style="text-align: center; margin: 1.5rem 0;">
  <iframe id="itch-embed-dread-breakfast" title="Itch.io: Dread & Breakfast" frameborder="0" loading="lazy" src="https://itch.io/embed/4471600?linkback=true&amp;bg_color=000000&amp;fg_color=e6d699&amp;link_color=fa5c5c&amp;border_color=282828" width="552" height="167" class="itch-embed"></iframe>
</div>

**[Play In Browser](https://goldleafinteractive.itch.io/dread-and-breakfast)** · Started at *Mini Jam 208: Inverted* (2026) · [Patches](https://goldleafinteractive.itch.io/dread-and-breakfast/devlog/1489095/update-1-fixes-energy-bubbles-deep-freeze) · [v0.9 beta](https://goldleafinteractive.itch.io/dread-and-breakfast/devlog/1501963/patch-notes-v090-beta)

---

### Trenchglow
**Unity (2D URP) · C# · In development · WebGL playable slice**

WebGL deep-sea exploration slice built around sonar pings, dark-water navigation, collectibles, puzzles, and curiosity-first traversal.

<p align="center">
  <img src="/assets/images/trenchglow.png" alt="Trenchglow underwater key art" style="max-width: 600px; width: 100%;">
</p>

- Built shader-driven sonar reveals with a toned-down fallback for WebGL and lower-end GPUs.
- Layered local visibility, widening sonar rings, and timed SFX so audio and reveal feedback line up.
- Shipped a tutorial slice and started expanding toward additional trench layouts and puzzle spaces.

<div class="itch-embed-wrap" style="text-align: center; margin: 1.5rem 0;">
  <iframe id="itch-embed-trenchglow" title="Itch.io: Trenchglow" frameborder="0" loading="lazy" src="https://itch.io/embed/4513861?linkback=true&amp;bg_color=0a1628&amp;fg_color=cfe8ff&amp;link_color=f5a524&amp;border_color=1a3d5c" width="552" height="167" class="itch-embed"></iframe>
</div>

**[Play In Browser](https://goldleafinteractive.itch.io/trenchglow)** · Tutorial slice live; fuller trench roadmap.

---

### BREATHE Arcade
**Unity 6 · C# · 2D URP · Capstone Project · WebGL + Windows**

Five breath-controlled micro-games built around a shared input layer for custom hardware, USB mic input, and keyboard simulation.

<p align="center">
  <img src="/assets/images/breathe-arcade.png" alt="BREATHE Arcade promo art" style="max-width: 600px; width: 100%;">
</p>

- Designed one normalized breath-input path so fan hardware, USB mic, and keyboard fallback feed the same mini-game logic.
- Handled MCU/serial input on a worker thread with COM discovery, smoothing, and spike rejection for reliable demos.
- Shared scoring/results UX and per-mode tuning structs across all five games instead of duplicating flow per activity.

<div class="itch-embed-wrap" style="text-align: center; margin: 1.5rem 0;">
  <iframe id="itch-embed-breathe-arcade" title="Itch.io: BREATHE Arcade" frameborder="0" loading="lazy" src="https://itch.io/embed/4475446?linkback=true&amp;bg_color=d6f5ff&amp;fg_color=0b2d3f&amp;link_color=ff4f6e&amp;border_color=93cdea" width="552" height="167" class="itch-embed"></iframe>
</div>

**[Play In Browser](https://goldleafinteractive.itch.io/breathe-arcade)** · README / HOW_IT_WORKS cover the Unity project publicly.

---

### OVERCLOCKED: Data Dash MAX
**Unreal Engine 5 · C++ & Blueprints · Capstone Project · Released (PC & Arcade Cabinet)**

Released Unreal endless runner built for desktop and arcade cabinet play, with lane movement, speed escalation, pickups, medals, themes, and offline leaderboards.

<p align="center">
  <img src="/assets/images/overclocked-data-dash-max.png" alt="OVERCLOCKED: Data Dash MAX" style="max-width: 600px; width: 100%;">
</p>

- Built C++ gameplay systems for lane swap, jump/slide, spawning, pickups, HUD, menu flow, and gamepad-first control.
- Authored **40+** obstacle pattern chunks with difficulty tiers and weighted escalation so pressure rises without unreadable RNG spikes.
- Tuned pacing, HUD clarity, six visual themes, and arcade-cabinet input feel through PC and hardware playtesting.

<div class="itch-embed-wrap" style="text-align: center; margin: 1.5rem 0;">
  <iframe id="itch-embed-overclocked-projects" title="Itch.io: Overclocked DDM" frameborder="0" loading="lazy" src="https://itch.io/embed/4278897?linkback=true&amp;border_width=5&amp;bg_color=000000&amp;fg_color=fffcbc&amp;link_color=46ffd4&amp;border_color=979797" width="552" height="167" class="itch-embed"></iframe>
</div>

**[Windows build on Itch.io](https://goldleafinteractive.itch.io/overclocked-ddm)** · [Patch v1.1.0](https://goldleafinteractive.itch.io/overclocked-ddm/devlog/1379247/v110-patch-notes-overclocked-ddm) · [Trailer](https://www.youtube.com/watch?v=dI9Ctq9LkLs)

---

### Quantum Tether
**Unity · C# · Released · Texas Game Jam 2025 (EGaDs, UT Austin)**

**Endless roguelike sidescroller** made in a weekend: you **swing on stars and asteroids** with the mouse—**left-click** main grapple, **right-click** second rope once you unlock it, **Space** shortens the rope, **Shift** input **dashes toward the cursor** to save bad swings. **Red “corrupted” anchors** are traps, one touch will end the run; fall too far off-screen and the run ends as well. Grab **time crystals**, buy **upgrades** as they come over time, and push your **high score** (time survived). Inspired by the old flash game, *Spider-Man: City Raid*.

<p align="center">
  <img src="/assets/images/quantum-tether.png" alt="Quantum Tether" style="max-width: 600px; width: 100%;">
</p>

- **Grapple feel**: connects **where you point** your cursor; **damping** and **rope length** are tuned so you get an **arcade swing** feel, not floppy chaos—**dash** is there as an assist for the player when things get rough or too busy on screen, useful for repositioning.
- **Procedural levels (PCG)**: there’s **no single fixed map**. The game **layers hand-authored pieces**—patterns of collections of **safe anchors**, pockets of **danger** with corrupted (red) anchors, **pickups** for extra scoring—and it **picks the next piece by weighted rules** as your **run speeds up** over time. Difficulty rises in a **controlled** way instead of pure RNG with the pattern difficulty tiers.
- **Roguelike wrap-up**: **10+ upgrades** that change how you move and interact with the world; **normal vs corrupted** anchors; full **HUD and score** flow; when you wipe, you **start fresh as the next “clock spirit”** and try to beat your last time/score.

**[View on Itch.io](https://goldleafinteractive.itch.io/quantum-tether)** · [Trailer](https://www.youtube.com/watch?v=RNs4yKPhfGM)

---

### Mysteries of Tupni
**Unreal Engine 5 · Blueprints · Class Prototype**

Third-person fantasy "souls-like" action adventure. I worked on early concept/design, documentation, and scope management, then built a **Data Table driven inventory** system, interactables, and quest/NPC hooks. This was one of my first game projects, built with another student and market assets for art.

<p align="center">
  <img src="/assets/images/mysteries-of-tupni.png" alt="Mysteries of Tupni" style="max-width: 600px; width: 100%;">
</p>

**[View on Itch.io](https://goldleafinteractive.itch.io/mysteries-of-tupni)** · [Demo](https://www.youtube.com/watch?v=BQl2MkPxUl4)

---

### Ginger Shroom Journey
**Unity · C# · Steam · Class Prototype**

**Solo** developed, simple 2D adventure. Built everything except art assets: core systems, UI, SFX, 10 tilemap-painted levels, and **Steamworks** shipping.

<p align="center">
  <img src="/assets/images/ginger-shroom-journey.png" alt="Ginger Shroom Journey" style="max-width: 600px; width: 100%;">
</p>

**[Steam (free)](https://store.steampowered.com/app/3023100/Ginger_Shroom_Journey/)** · [Trailer](https://www.youtube.com/watch?v=-LGDr3DaUB8)

---

## Other Work

### Void Knights
**Unreal Engine 5 · Blueprints · Class Prototype**

*Persona*-inspired dual-world JRPG prototype—authored open-world mechanics -> **Reality / Void** realm swap, telekinesis, patrol AI, interactive props, save/load, & more; worked closely with the lead designer and lead programmer to achieve the vision that we concepted originally. Turn based combat, xp/leveling system, & more was authored by the lead programmer. Everything pertaining to open world mechanics or features used during exploration was done by myself under the guidance of the lead programmer.

<p align="center">
  <img src="/assets/images/void-knights.png" alt="Void Knights" style="max-width: 600px; width: 100%;">
</p>

**[View on Itch.io](https://goldleafinteractive.itch.io/void-knights)**

---

### Medieval Shop Game
**C++ · Windows · Class Prototype**

ASCII console shop simulator—**inventory, haggle, branching chat options**, using RAII/smart pointers, CMake → packed assets → installer → signed **.exe** (experimented with creating an installer & learning how security certificates work with Windows). Built for a class project, solo.

<p align="center">
  <img src="/assets/images/medieval-shop-game.png" alt="Medieval Shop Game" style="max-width: 600px; width: 100%;">
</p>

**[View on Itch.io](https://goldleafinteractive.itch.io/medieval-shop-game)**

---

### Million Miles Deep
**Unreal Engine 5 · Blueprints · Class Prototype**

Oceanic **2D** top-down bullet-hell/SHMUP — game design, enemy pattern authoring, projectile setup, playtesting, and QA.

<p align="center">
  <img src="/assets/images/million-miles-deep.png" alt="Million Miles Deep" style="max-width: 260px; width: 48%; display: inline-block;">
  <img src="/assets/images/million-miles-deep-2.png" alt="Million Miles Deep" style="max-width: 260px; width: 48%; display: inline-block;">
</p>

**[View on Itch.io](https://goldleafinteractive.itch.io/million-miles-deep)**

---

### Ragdoll Plainly Perilous
**Unreal Engine 5 · Blueprints · Class Prototype**

Made for Chillenium 2025 Game Jam. Experimental ragdoll-as-controller traversal with stable collision tuning. Modeled after and inspired by an old flash game (Ragdoll Avalanche 2).

<p align="center">
  <img src="/assets/images/ragdoll-plainly-perilous.png" alt="Ragdoll Plainly Perilous" style="max-width: 600px; width: 100%;">
</p>

**[View on Itch.io](https://goldleafinteractive.itch.io/ragdoll-plainly-perilous)** · [Demo](https://www.youtube.com/watch?v=GfrDt166KZI)

---

### Crimson Eclipse
**Unreal Engine 5 · Blueprints · Class Prototype**

Side-scrolling atmospheric horror—enemy/encounter logic, environment beats, HUD comms. Did the engine work, level design & implementation/build. Team project from my coursework, with artist teammates.

<p align="center">
  <img src="/assets/images/crimson-eclipse.png" alt="Crimson Eclipse" style="max-width: 600px; width: 100%;">
</p>

**[View on Itch.io](https://goldleafinteractive.itch.io/crimson-eclipse)** · [Demo](https://www.youtube.com/watch?v=R7KG3vuqHx4)

---

## More

~**16** jam/class loops if you count everything:

- **I AM INEVITABLE** (UE5 · Chillennium ’26) — defeats raise stats; platformer movement with wall interplay + dashing · **[Windows](https://goldleafinteractive.itch.io/i-am-inevitable)**
- **Doors n' Dice** · Class Prototype · Old coursework prototype/test project - [itch](https://goldleafinteractive.itch.io/doors-n-dice)
- **Escape Control** · Class Prototype · Old coursework prototype/test project - see [profile](https://goldleafinteractive.itch.io/)
- Misc mechanics labs · old capture exports for class submissions **maybe** later for archive

---
