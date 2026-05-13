---
title: My Projects
nav_order: 3
---

# Projects

[Current Pursuits →](activedev)

---

## Featured

### ACCESS GRANTED
**Unity 6 · C# · URP · Released · WebGL + Windows**

Solo developed project—inspired loosely by the 1995 movie ***Hackers***: breakout with a unique twist, with the illusion of a CRT terminal display; typed command challenges finish special bricks while the ball stays in play. Runs in-browser and available for download.

<p align="center">
  <img src="/assets/images/access-granted.png" alt="Access Granted CRT-style gameplay" style="max-width: 600px; width: 100%;">
</p>

- Block breaker ↔ typing challenges respect the player—slow-mo triggers
- CRT effect is intentional: barrel distortion + scanlines attempt to imitate a 90's era terminal.
- **Two** strike tracks (ball drops vs mistypes); **word pools chunked in data**. Three tiers of difficulty from levels 1-15.

<div class="itch-embed-wrap" style="text-align: center; margin: 1.5rem 0;">
  <iframe id="itch-embed-access-granted-projects" title="Itch.io: Access Granted" frameborder="0" loading="lazy" src="https://itch.io/embed/4475328?linkback=true&amp;border_width=2&amp;bg_color=060d06&amp;fg_color=b9c6e4&amp;link_color=00edd6&amp;border_color=084808" width="552" height="167" class="itch-embed"></iframe>
</div>

**[Play In Browser](https://goldleafinteractive.itch.io/access-granted)** · [Patch Notes v2](https://goldleafinteractive.itch.io/access-granted/devlog/1516113/patch-notes-v2)

---

### Dread & Breakfast
**Unity 6 · C# · Beta / Post-jam · WebGL & Windows**

Jam prototype that grew into a more polished and updated top-down ghost haunting **management** game: escalating nights, shuffled layouts, haunt kits vs guest fears, fright economy, upgrades, and the **Box of Tricks** shop provide a rogue-like gameplay style, enabling replayablity.

<p align="center">
  <img src="/assets/images/dread-and-breakfast.png" alt="Dread & Breakfast floor plan gameplay" style="max-width: 600px; width: 100%;">
</p>

- PCG house pass—currently only 2 templates but room to add more, same with readable different props & characters
- **One** central guest behavior controller—all visitors can wander, chatter, experience fear escalation, and cause panic chains by scaring other guests.
- **17** haunts (abilities) authored as reusable data points, plus a modest event/messaging layer for player feedback; meta-shop points & abilities are persistent, even in browser play.

<div class="itch-embed-wrap" style="text-align: center; margin: 1.5rem 0;">
  <iframe id="itch-embed-dread-breakfast" title="Itch.io: Dread & Breakfast" frameborder="0" loading="lazy" src="https://itch.io/embed/4471600?linkback=true&amp;bg_color=000000&amp;fg_color=e6d699&amp;link_color=fa5c5c&amp;border_color=282828" width="552" height="167" class="itch-embed"></iframe>
</div>

**[Play In Browser](https://goldleafinteractive.itch.io/dread-and-breakfast)** · Started at *Mini Jam 208: Inverted* (2026) · [Patches](https://goldleafinteractive.itch.io/dread-and-breakfast/devlog/1489095/update-1-fixes-energy-bubbles-deep-freeze) · [v0.9 beta](https://goldleafinteractive.itch.io/dread-and-breakfast/devlog/1501963/patch-notes-v090-beta)

---

### Trenchglow
**Unity (2D URP) · C# · In development · WebGL playable slice**

*Deep*-themed jam: trench exploration in dark water—**ping-based reveals**, stamina boosts / moving rocks / gems—focused on curiosity more than twitch platforming alone.

<p align="center">
  <img src="/assets/images/trenchglow.png" alt="Trenchglow underwater key art" style="max-width: 600px; width: 100%;">
</p>

- **Shader-driven sonar** paints each ping into a radiating reveal before it fades—**paired with a toned-down fallback** for strained WebGL / budget GPUs.
- **Layered vignette**: a tight local clear spot is maintainted **plus** vsibility rings that widen with sonar, **timed SFX** so what you hear matches what flashes on-screen.
- **More levels planned.**

<div class="itch-embed-wrap" style="text-align: center; margin: 1.5rem 0;">
  <iframe id="itch-embed-trenchglow" title="Itch.io: Trenchglow" frameborder="0" loading="lazy" src="https://itch.io/embed/4513861?linkback=true&amp;bg_color=0a1628&amp;fg_color=cfe8ff&amp;link_color=f5a524&amp;border_color=1a3d5c" width="552" height="167" class="itch-embed"></iframe>
</div>

**[Play In Browser](https://goldleafinteractive.itch.io/trenchglow)** · Tutorial slice live; fuller trench roadmap.

---

### BREATHE Arcade
**Unity 6 · C# · 2D URP · Emergent Technologies capstone · WebGL + Windows**

Five micro-games (sailboat, constellations, balloons, bubbles, skydiving landings)—built as an **Emergent Technologies capstone** where **actual breath drives play**, with **mic and keyboard simulations** so teachers and kiosk visitors are never blocked.

<p align="center">
  <img src="/assets/images/breathe-arcade.png" alt="BREATHE Arcade promo art" style="max-width: 600px; width: 100%;">
</p>

- **One breath-driven input layer** for the **custom fan**, **USB mic**, and **keyboard simulator**—same normalized signal for every mini-game, so gameplay never forks into duplicate code paths per device.
- **MCU firmware → UART** enters Unity on a **worker thread** with **automatic COM discovery**, **moving-window smoothing**, and **glitch spike rejection**; coursework includes **hardware/wiring docs** reviewers can follow without guesswork.
- **Shared smoothing** compensates **fan motor spin-down lag** versus real airflow decay; five experiences **share one scoring/results shell** with lightweight **per-mode tuning structs** instead of reinventing UX each time.

<div class="itch-embed-wrap" style="text-align: center; margin: 1.5rem 0;">
  <iframe id="itch-embed-breathe-arcade" title="Itch.io: BREATHE Arcade" frameborder="0" loading="lazy" src="https://itch.io/embed/4475446?linkback=true&amp;bg_color=d6f5ff&amp;fg_color=0b2d3f&amp;link_color=ff4f6e&amp;border_color=93cdea" width="552" height="167" class="itch-embed"></iframe>
</div>

**[Play In Browser](https://goldleafinteractive.itch.io/breathe-arcade)** · README / HOW_IT_WORKS cover the Unity project publicly.

---

### OVERCLOCKED: Data Dash MAX
**Unreal Engine 5.7 · C++ & Blueprints · Released (PC & Arcade Cabinet)**

**Released** endless runner built for **arcade cabinets and desktop** alike: lane swapping, jumps, slides, pickups, escalating speed, obstacles to dodge, medals to earn, six palettes/themes to choose from, and an **offline leaderboard** to prove your skill to your friends, and see who can be the best.

<p align="center">
  <img src="/assets/images/overclocked-data-dash-max.png" alt="OVERCLOCKED: Data Dash MAX" style="max-width: 600px; width: 100%;">
</p>

- **C++ gameplay layer** owns spawning, locomotion (**lane swap / jump / slide**), pickups, HUD, and **menu flow** — gamepad-first playtesting was done so sticks and cabinet buttons never feel like a ported mouse hack.
- **40+ obstacle combos** are **named pattern chunks** authored in structured data—each chunk sits in a **difficulty tier** (early tiers teach dodge spacing and lane reads; higher tiers shorten gaps and overlap hazards deliberately). During a run, **speed ramps** and **heavier tiers enter the weighted pool**, so escalating pressure stays **readable and authored**, not just RNG spikes.
- **Six** visual palettes or themes provided; **pickup pacing and HUD clarity** was iterated and playtested on **PC**, then **re-balanced on real arcade hardware** once inputs were wired.

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
**Unreal Engine 5 · Blueprints · Prototype**

Third-person fantasy "souls-like" action adventure— worked on concepting, game design, documentation, and scope management in the early development. During production, built several systems --> **Data Table driven inventory** system (drag & drop, tooltips for details, inventory persistence between levels), other world interactables, and helped design/implement some quest/NPC hooks. This was one of my first projects ever, if not the first. Built with another student and with market assets for art.

<p align="center">
  <img src="/assets/images/mysteries-of-tupni.png" alt="Mysteries of Tupni" style="max-width: 600px; width: 100%;">
</p>

**[View on Itch.io](https://goldleafinteractive.itch.io/mysteries-of-tupni)** · [Demo](https://www.youtube.com/watch?v=BQl2MkPxUl4)

---

### Ginger Shroom Journey
**Unity · C# · Steam**

**Solo** developed, simple 2D adventure— built everything except art assets --> core systems, UI, SFX, 10 tilemap-painted levels, **Steamworks** shipping.

<p align="center">
  <img src="/assets/images/ginger-shroom-journey.png" alt="Ginger Shroom Journey" style="max-width: 600px; width: 100%;">
</p>

**[Steam (free)](https://store.steampowered.com/app/3023100/Ginger_Shroom_Journey/)** · [Trailer](https://www.youtube.com/watch?v=-LGDr3DaUB8)

---

## Other Work

### Void Knights
**Unreal Engine 5 · Blueprints**

*Persona*-inspired dual-world JRPG prototype—authored open-world mechanics -> **Reality / Void** realm swap, telekinesis, patrol AI, interactive props, save/load, & more; worked closely with the lead designer and lead programmer to achieve the vision that we concepted originally. Turn based combat, xp/leveling system, & more was authored by the lead programmer. Everything pertaining to open world mechanics or features used during exploration was done by myself under the guidance of the lead programmer.

<p align="center">
  <img src="/assets/images/void-knights.png" alt="Void Knights" style="max-width: 600px; width: 100%;">
</p>

**[View on Itch.io](https://goldleafinteractive.itch.io/void-knights)**

---

### Medieval Shop Game
**C++ · Windows**

ASCII console shop simulator—**inventory, haggle, branching chat options**, using RAII/smart pointers, CMake → packed assets → installer → signed **.exe** (experimented with creating an installer & learning how security certificates work with Windows). Built for a class project, solo.

<p align="center">
  <img src="/assets/images/medieval-shop-game.png" alt="Medieval Shop Game" style="max-width: 600px; width: 100%;">
</p>

**[View on Itch.io](https://goldleafinteractive.itch.io/medieval-shop-game)**

---

### Million Miles Deep
**Unreal Engine 5 · Blueprints**

Oceanic **2D** top-down bullet-hell/SHMUP — game design & concepting, authored enemy patterns and projectiles, playtesting & QA

<p align="center">
  <img src="/assets/images/million-miles-deep.png" alt="Million Miles Deep" style="max-width: 260px; width: 48%; display: inline-block;">
  <img src="/assets/images/million-miles-deep-2.png" alt="Million Miles Deep" style="max-width: 260px; width: 48%; display: inline-block;">
</p>

**[View on Itch.io](https://goldleafinteractive.itch.io/million-miles-deep)**

---

### Ragdoll Plainly Perilous
**Unreal Engine 5 · Blueprints**

Made for Chillenium 2025 Game Jam. Experimental ragdoll-as-controller traversal with stable collision tuning. Modeled after and inspired by an old flash game (Ragdoll Avalanche 2).

<p align="center">
  <img src="/assets/images/ragdoll-plainly-perilous.png" alt="Ragdoll Plainly Perilous" style="max-width: 600px; width: 100%;">
</p>

**[View on Itch.io](https://goldleafinteractive.itch.io/ragdoll-plainly-perilous)** · [Demo](https://www.youtube.com/watch?v=GfrDt166KZI)

---

### Crimson Eclipse
**Unreal Engine 5 · Blueprints**

Side-scrolling atmospheric horror—enemy/encounter logic, environment beats, HUD comms. Did the engine work, level design & implementation/build. Team project from my coursework, with artist teammates.

<p align="center">
  <img src="/assets/images/crimson-eclipse.png" alt="Crimson Eclipse" style="max-width: 600px; width: 100%;">
</p>

**[View on Itch.io](https://goldleafinteractive.itch.io/crimson-eclipse)** · [Demo](https://www.youtube.com/watch?v=R7KG3vuqHx4)

---

## More

~**16** jam/class loops if you count everything:

- **I AM INEVITABLE** (UE5 · Chillennium ’26) — defeats raise stats; platformer movement with wall interplay + dashing · **[Windows](https://goldleafinteractive.itch.io/i-am-inevitable)**
- **Doors n' Dice** · Old coursework prototype/test project - [itch](https://goldleafinteractive.itch.io/doors-n-dice)
- **Escape Control** · Old coursework prototype/test project - see [profile](https://goldleafinteractive.itch.io/)
- Misc mechanics labs · old capture exports for class submissions **maybe** later for archive

---

 [← Back to Home](index)
