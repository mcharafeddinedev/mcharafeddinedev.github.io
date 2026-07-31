---
title: Projects
description: "Playable Unreal and Unity projects by Marwan Charafeddine: Trenchglow, BREATHE Arcade, Access Granted, OVERCLOCKED, and more."
nav_order: 2
---

<div class="projects-page" markdown="1">

# Game Projects

---

## In Development

- **WW2-era FPS wave-survival demo** (private IP). Built in Unreal Engine 5.5 (C++). Combat, enemy AI, VFX feedback systems,UI, escalating rounds and most other in-game features are in the playable loop. My current goal is to finish a public playtest build, gather feedback, and iterate toward a stronger demo for a future showcase or festival submission. No public build yet.

---

## Featured

### Access Granted
Unity 6 · C# · URP · Released · Browser & Windows

Released solo project that blends brick-breaker play with reactive typing challenges inside a CRT-terminal aesthetic.

<p align="center">
  <img src="/assets/images/access-granted.png" alt="Access Granted CRT-style gameplay" style="max-width: 600px; width: 100%;">
</p>

- Built the paddle/ball loop, command-brick slow motion, typed prompt resolution, menus, and browser/Windows release flow.
- Tuned separate failure tracks for ball drops and mistyped commands, with three difficulty tiers across levels 1-15.
- Used barrel distortion, scanlines, UI styling, and patch iteration to keep the CRT identity readable during play.

<div class="itch-embed-wrap" style="text-align: center; margin: 1.5rem 0;">
  <iframe id="itch-embed-access-granted-projects" title="Itch.io: Access Granted" frameborder="0" loading="lazy" src="https://itch.io/embed/4475328?linkback=true&amp;border_width=2&amp;bg_color=060d06&amp;fg_color=b9c6e4&amp;link_color=00edd6&amp;border_color=084808" width="552" height="167" class="itch-embed"></iframe>
</div>

[Play In Browser](https://goldleafinteractive.itch.io/access-granted) · [Patch Notes v2](https://goldleafinteractive.itch.io/access-granted/devlog/1516113/patch-notes-v2)

---

### Dread & Breakfast
Unity 6 · C# · Beta / Post-jam · Browser & Windows

Top-down ghost haunting simulator about scaring guests through escalating nights, shuffled rooms, haunt abilities, and a replayable fright economy.

<p align="center">
  <img src="/assets/images/dread-and-breakfast.png" alt="Dread & Breakfast floor plan gameplay" style="max-width: 600px; width: 100%;">
</p>

- Built PCG-style house layout support with readable room templates, props, and guest setups for night-to-night variety.
- Centralized guest behavior so visitors can wander, chatter, escalate fear, and trigger panic chains.
- Authored 17 reusable haunt abilities, persistent meta-shop progress, and event-driven feedback for browser play.

<div class="itch-embed-wrap" style="text-align: center; margin: 1.5rem 0;">
  <iframe id="itch-embed-dread-breakfast" title="Itch.io: Dread & Breakfast" frameborder="0" loading="lazy" src="https://itch.io/embed/4471600?linkback=true&amp;bg_color=000000&amp;fg_color=e6d699&amp;link_color=fa5c5c&amp;border_color=282828" width="552" height="167" class="itch-embed"></iframe>
</div>

[Play In Browser](https://goldleafinteractive.itch.io/dread-and-breakfast) · Started at *Mini Jam 208: Inverted* (2026) · [Patches](https://goldleafinteractive.itch.io/dread-and-breakfast/devlog/1489095/update-1-fixes-energy-bubbles-deep-freeze) · [v0.9 beta](https://goldleafinteractive.itch.io/dread-and-breakfast/devlog/1501963/patch-notes-v090-beta)

---

### Trenchglow {#trenchglow}
Unity (2D URP) · C# · Released · Browser

Deep-sea exploration game built around sonar pings, dark-water navigation, collectibles, puzzles, and curiosity-first traversal.

<p align="center">
  <img src="/assets/images/trenchglow.png" alt="Trenchglow underwater key art" style="max-width: 600px; width: 100%;">
</p>

- Built shader-driven sonar reveals with a toned-down fallback for browser builds and lower-end GPUs.
- Layered local visibility, widening sonar rings, and timed SFX so audio and reveal feedback line up.
- Finished beyond the tutorial with additional trench levels and puzzle spaces; playable browser build is live on itch.

<div class="itch-embed-wrap" style="text-align: center; margin: 1.5rem 0;">
  <iframe id="itch-embed-trenchglow" title="Itch.io: Trenchglow" frameborder="0" loading="lazy" src="https://itch.io/embed/4513861?linkback=true&amp;bg_color=0a1628&amp;fg_color=cfe8ff&amp;link_color=f5a524&amp;border_color=1a3d5c" width="552" height="167" class="itch-embed"></iframe>
</div>

[Play In Browser](https://goldleafinteractive.itch.io/trenchglow) · Released with tutorial plus extra trench levels.

---

### BREATHE Arcade {#breathe-arcade}
Unity 6 · C# · 2D URP · Capstone Project · Browser & Windows

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

[Play In Browser](https://goldleafinteractive.itch.io/breathe-arcade) · README / HOW_IT_WORKS cover the Unity project publicly.

---

### OVERCLOCKED: Data Dash MAX
Unreal Engine 5 · C++ & Blueprints · Capstone Project · Released (PC & Arcade Cabinet)

Released Unreal endless runner built for desktop and arcade cabinet play, with lane movement, speed escalation, pickups, medals, themes, and offline leaderboards.

<p align="center">
  <img src="/assets/images/overclocked-data-dash-max.png" alt="OVERCLOCKED: Data Dash MAX" style="max-width: 600px; width: 100%;">
</p>

- Built C++ gameplay systems for lane swap, jump/slide, spawning, pickups, HUD, menu flow, and gamepad-first control.
- Authored 40+ obstacle pattern chunks with difficulty tiers and weighted escalation so pressure rises without unreadable RNG spikes.
- Tuned pacing, HUD clarity, six visual themes, and arcade-cabinet input feel through PC and hardware playtesting.

<div class="itch-embed-wrap" style="text-align: center; margin: 1.5rem 0;">
  <iframe id="itch-embed-overclocked-projects" title="Itch.io: Overclocked DDM" frameborder="0" loading="lazy" src="https://itch.io/embed/4278897?linkback=true&amp;border_width=5&amp;bg_color=000000&amp;fg_color=fffcbc&amp;link_color=46ffd4&amp;border_color=979797" width="552" height="167" class="itch-embed"></iframe>
</div>

[Windows build on Itch.io](https://goldleafinteractive.itch.io/overclocked-ddm) · [Patch v1.1.0](https://goldleafinteractive.itch.io/overclocked-ddm/devlog/1379247/v110-patch-notes-overclocked-ddm) · [Trailer](https://www.youtube.com/watch?v=dI9Ctq9LkLs)

---

### Quantum Tether
Unity · C# · Released · Texas Game Jam 2025 (EGaDs, UT Austin)

Endless roguelike sidescroller made in a weekend: swing on stars and asteroids with the mouse, unlock a second rope, shorten the rope, and dash toward the cursor to recover bad swings. Red corrupted anchors are traps, one touch ends the run, and time crystals feed upgrades and score progression. Inspired by the old flash game *Spider-Man: City Raid*.

<p align="center">
  <img src="/assets/images/quantum-tether.png" alt="Quantum Tether" style="max-width: 600px; width: 100%;">
</p>

- Grapple feel: cursor-based anchors, tuned damping, rope length control, and dash recovery keep the swing readable.
- Procedural levels: hand-authored anchor/pickup/hazard chunks enter the run through weighted rules as speed increases.
- Roguelike wrap-up: 10+ upgrades, normal vs. corrupted anchors, HUD/score flow, and fresh-run structure.

[View on Itch.io](https://goldleafinteractive.itch.io/quantum-tether) · [Trailer](https://www.youtube.com/watch?v=RNs4yKPhfGM)

---

### Mysteries of Tupni
Unreal Engine 5 · Blueprints · Class Prototype

Third-person fantasy "souls-like" action adventure. I worked on early concept/design, documentation, and scope management, then built a Data Table driven inventory system, interactables, and quest/NPC hooks. This was one of my first game projects, built with another student and market assets for art.

<p align="center">
  <img src="/assets/images/mysteries-of-tupni.png" alt="Mysteries of Tupni" style="max-width: 600px; width: 100%;">
</p>

[View on Itch.io](https://goldleafinteractive.itch.io/mysteries-of-tupni) · [Demo](https://www.youtube.com/watch?v=BQl2MkPxUl4)

---

### Ginger Shroom Journey
Unity · C# · Steam · Class Prototype

Solo developed, simple 2D adventure. Built everything except art assets: core systems, UI, SFX, 10 tilemap-painted levels, and Steamworks shipping.

<p align="center">
  <img src="/assets/images/ginger-shroom-journey.png" alt="Ginger Shroom Journey" style="max-width: 600px; width: 100%;">
</p>

[Steam (free)](https://store.steampowered.com/app/3023100/Ginger_Shroom_Journey/) · [Trailer](https://www.youtube.com/watch?v=-LGDr3DaUB8)

---

## Earlier Prototypes & Jams

### Void Knights
Unreal Engine 5 · Blueprints · Class Prototype

*Persona*-inspired dual-world JRPG prototype. I authored exploration mechanics including Reality/Void realm swap, telekinesis, patrol AI, interactive props, save/load hooks, and related traversal features while collaborating with the lead designer and lead programmer.

<p align="center">
  <img src="/assets/images/void-knights.png" alt="Void Knights" style="max-width: 600px; width: 100%;">
</p>

[View on Itch.io](https://goldleafinteractive.itch.io/void-knights)

---

### Medieval Shop Game
C++ · Windows · Class Prototype

ASCII console shop simulator with inventory, haggling, branching chat options, RAII/smart pointers, CMake, packed assets, installer work, and signed .exe experiments. Built solo for a class project.

<p align="center">
  <img src="/assets/images/medieval-shop-game.png" alt="Medieval Shop Game" style="max-width: 600px; width: 100%;">
</p>

[View on Itch.io](https://goldleafinteractive.itch.io/medieval-shop-game)

---

### Million Miles Deep
Unreal Engine 5 · Blueprints · Class Prototype

Oceanic 2D top-down bullet-hell/SHMUP. Contributions: game design, enemy pattern authoring, projectile setup, playtesting, and QA.

<p align="center">
  <img src="/assets/images/million-miles-deep.png" alt="Million Miles Deep" style="max-width: 260px; width: 48%; display: inline-block;">
  <img src="/assets/images/million-miles-deep-2.png" alt="Million Miles Deep" style="max-width: 260px; width: 48%; display: inline-block;">
</p>

[View on Itch.io](https://goldleafinteractive.itch.io/million-miles-deep)

---

### Ragdoll Plainly Perilous
Unreal Engine 5 · Blueprints · Class Prototype

Made for Chillenium 2025 Game Jam. Experimental ragdoll-as-controller traversal with stable collision tuning. Modeled after and inspired by an old flash game (Ragdoll Avalanche 2).

<p align="center">
  <img src="/assets/images/ragdoll-plainly-perilous.png" alt="Ragdoll Plainly Perilous" style="max-width: 600px; width: 100%;">
</p>

[View on Itch.io](https://goldleafinteractive.itch.io/ragdoll-plainly-perilous) · [Demo](https://www.youtube.com/watch?v=GfrDt166KZI)

---

### Crimson Eclipse
Unreal Engine 5 · Blueprints · Class Prototype

Side-scrolling atmospheric horror. Worked on enemy/encounter logic, environment beats, and HUD comms. Did the engine work, level design, and build. Team project from my coursework, with artist teammates.

<p align="center">
  <img src="/assets/images/crimson-eclipse.png" alt="Crimson Eclipse" style="max-width: 600px; width: 100%;">
</p>

[View on Itch.io](https://goldleafinteractive.itch.io/crimson-eclipse) · [Demo](https://www.youtube.com/watch?v=R7KG3vuqHx4)

---

## More

- [I AM INEVITABLE](https://goldleafinteractive.itch.io/i-am-inevitable) (UE5 · Chillennium '26): defeat-scaling stats, wall movement, dashing
- [Doors n' Dice](https://goldleafinteractive.itch.io/doors-n-dice) · Class prototype
- [Escape Control](https://goldleafinteractive.itch.io/) · Class prototype (see [itch profile](https://goldleafinteractive.itch.io/))

---

</div>
