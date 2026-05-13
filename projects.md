---
title: Projects
nav_order: 3
---

# Projects

[Current Pursuits →](activedev)

---

## Featured

*Flagship write-ups below; **[Other Work](#other-work)** is shorter on purpose.*

### ACCESS GRANTED
**Unity 6 · C# · URP · Released · WebGL + Windows**

Solo hobby build—in the **spirit of *Hackers*** (not realism): breakout peels back a faux terminal layer; typed commands finish special bricks while the ball stays in play. Fits a portfolio page and runs in-browser.

<p align="center">
  <img src="/assets/images/access-granted.png" alt="Access Granted CRT-style gameplay" style="max-width: 600px; width: 100%;">
</p>

- Breaker ↔ typing respects pauses—slow-mo cues, timers that behave when you freeze the game.
- CRT effect is intentional: barrel distortion + scan = **one** cohesive screen (**menus included**).
- **Two** strike tracks (drops vs mistypes/timeouts); **word pools chunked in data**; optional **scripted ring finale** instead of a rectangular grid-only finish.

<div class="itch-embed-wrap" style="text-align: center; margin: 1.5rem 0;">
  <iframe id="itch-embed-access-granted-projects" title="Itch.io: Access Granted" frameborder="0" loading="lazy" src="https://itch.io/embed/4475328?linkback=true&amp;border_width=2&amp;bg_color=060d06&amp;fg_color=b9c6e4&amp;link_color=00edd6&amp;border_color=084808" width="552" height="167" class="itch-embed"></iframe>
</div>

**[Play In Browser](https://goldleafinteractive.itch.io/access-granted)** · [Patch Notes v2](https://goldleafinteractive.itch.io/access-granted/devlog/1516113/patch-notes-v2)

---

### Dread & Breakfast
**Unity 6 · C# · Beta / Post-jam · WebGL & Windows**

Jam prototype that grew into a top-down ghost **management** game: escalating nights, shuffled layouts, haunt kits vs guest fears, fright economy, upgrades, **Box of Tricks** shop.

<p align="center">
  <img src="/assets/images/dread-and-breakfast.png" alt="Dread & Breakfast floor plan gameplay" style="max-width: 600px; width: 100%;">
</p>

- PCG house pass—templates, readable props versus door visibility (**living-room-friendly** framing).
- **One** central guest behavior controller—wander, chatter, fear escalation, panic chains.
- **17** haunts authored as reusable data plus a modest event/message layer; nightly and meta-shop tuning stay orderly.

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

- **Shader-fed sonar** paints each ping into a readable flash before it fades—**paired with a toned-down fallback** for strained WebGL / budget GPUs.
- **Layered vignette**: a tight local clear spot **plus** rings that widen with pings, **timed with audio** so what you hear matches what flashes on-screen.
- **Clone Scriptables per session** so level iteration never silently overwrites shared assets; **moving rocks stay kinematic rigs** with designer-friendly resets and event hooks.

<div class="itch-embed-wrap" style="text-align: center; margin: 1.5rem 0;">
  <iframe id="itch-embed-trenchglow" title="Itch.io: Trenchglow" frameborder="0" loading="lazy" src="https://itch.io/embed/4513861?linkback=true&amp;bg_color=0a1628&amp;fg_color=cfe8ff&amp;link_color=f5a524&amp;border_color=1a3d5c" width="552" height="167" class="itch-embed"></iframe>
</div>

**[Play In Browser](https://goldleafinteractive.itch.io/trenchglow)** · Tutorial live; fuller trench roadmap.

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

**[Play In Browser](https://goldleafinteractive.itch.io/breathe-arcade)** · Employer wiring deep-dive on request · README / HOW_IT_WORKS cover Unity publicly.

---

### OVERCLOCKED: Data Dash MAX
**Unreal Engine 5.7 · C++ & Blueprints · Released (PC & Arcade Cabinet)**

**Released** endless runner built for **arcade cabinets and desktop** alike: lane swaps, jumps, slides, pickups, escalating speed, medals, six palettes, **offline leaderboards**—paced so **cabinet-hard** stays fair on sticks, not borrowed from KB&M defaults.

<p align="center">
  <img src="/assets/images/overclocked-data-dash-max.png" alt="OVERCLOCKED: Data Dash MAX" style="max-width: 600px; width: 100%;">
</p>

- **C++ gameplay layer** owns spawn, locomotion (**lane swap / jump / slide**), pickups, HUD, and **menu flow—gamepad-first inputs** so sticks and cabinet buttons never feel like a ported mouse hack.
- **40+ obstacle combos** are **named pattern chunks** authored in structured data—each chunk sits in a **difficulty tier** (early tiers teach dodge spacing and lane reads; higher tiers shorten gaps and overlap hazards deliberately). During a run **speed ramps** and **heavier tiers enter the weighted pool**, so escalating pressure stays **readable and authored**, not opaque RNG spikes.
- **Six** visual palettes; **pickup pacing and HUD clarity** nailed on **PC**, then **re-balanced on real arcade hardware** once controllers were wired—a second pass purely for sticks and cabinet latency.

<div class="itch-embed-wrap" style="text-align: center; margin: 1.5rem 0;">
  <iframe id="itch-embed-overclocked-projects" title="Itch.io: Overclocked DDM" frameborder="0" loading="lazy" src="https://itch.io/embed/4278897?linkback=true&amp;border_width=5&amp;bg_color=000000&amp;fg_color=fffcbc&amp;link_color=46ffd4&amp;border_color=979797" width="552" height="167" class="itch-embed"></iframe>
</div>

**[Windows build on Itch.io](https://goldleafinteractive.itch.io/overclocked-ddm)** · [Patch v1.1.0](https://goldleafinteractive.itch.io/overclocked-ddm/devlog/1379247/v110-patch-notes-overclocked-ddm) · [Trailer](https://www.youtube.com/watch?v=dI9Ctq9LkLs)

---

### Quantum Tether
**Unity · C# · Released · Texas Game Jam 2025 (EGaDs, UT Austin)**

**Endless roguelike sidescroller** made in a weekend: you **swing on stars and asteroids** with the mouse—**left-click** main grapple, **right-click** second rope once you unlock it, **Space** shortens the rope, **Shift** **dashes toward the cursor** to save bad swings. **Red “corrupted” anchors** are traps; fall off-screen and the run ends. Grab **time crystals**, buy **upgrades**, and push your **high score** (time survived). The feel is **old flash web swingers** like *Spider-Man: City Raid*, updated for **clear, fast mouse control**.

<p align="center">
  <img src="/assets/images/quantum-tether.png" alt="Quantum Tether" style="max-width: 600px; width: 100%;">
</p>

- **Grapple feel**: pulls aim **where you point**; **damping** and **rope length** are tuned so you get **arcade swing**, not floppy chaos—**dash** is there to fix a bad line when the field gets crowded.
- **Procedural levels (PCG)**: there’s **no single fixed map**. The game **layers hand-authored pieces**—patches of **safe anchors**, pockets of **danger**, lines of **pickups**—and **picks the next piece by weighted rules** as your **run speeds up**, so difficulty rises in a **controlled** way instead of pure random spam.
- **Roguelike wrap-up**: **10+ upgrades** that change how you move; **normal vs corrupted** anchors; full **HUD and score** flow; when you wipe, you **start fresh as the next “clock spirit”** and try to beat your time.

**[View on Itch.io](https://goldleafinteractive.itch.io/quantum-tether)** · [Trailer](https://www.youtube.com/watch?v=RNs4yKPhfGM)

---

### Mysteries of Tupni
**Unreal Engine 5 · Blueprints · Prototype**

Third-person fantasy—systems, **Data Table inventory** (drag, tooltips, persistence), world interactables, quest/NPC hooks.

<p align="center">
  <img src="/assets/images/mysteries-of-tupni.png" alt="Mysteries of Tupni" style="max-width: 600px; width: 100%;">
</p>

**[View on Itch.io](https://goldleafinteractive.itch.io/mysteries-of-tupni)** · [Demo](https://www.youtube.com/watch?v=BQl2MkPxUl4)

---

### Ginger Shroom Journey
**Unity · C# · Steam**

**Solo** 2D adventure—core systems, UI, optimization, **Steamworks** shipping.

<p align="center">
  <img src="/assets/images/ginger-shroom-journey.png" alt="Ginger Shroom Journey" style="max-width: 600px; width: 100%;">
</p>

**[Steam (free)](https://store.steampowered.com/app/3023100/Ginger_Shroom_Journey/)** · [Trailer](https://www.youtube.com/watch?v=-LGDr3DaUB8)

---

## Other Work

### Void Knights
**Unreal Engine 5 · Blueprints**

*Persona*-inspired dual-world RPG prototype—**Reality / Void** swap, telekinesis, patrol AI; worked with designers on stealth and puzzles.

<p align="center">
  <img src="/assets/images/void-knights.png" alt="Void Knights" style="max-width: 600px; width: 100%;">
</p>

**[View on Itch.io](https://goldleafinteractive.itch.io/void-knights)**

---

### Medieval Shop Game
**C++ · Windows**

Ascii console shop—**inventory, haggle, branching chat**, RAII/smart pointers, CMake → packed assets → installer → signed **.exe**.

<p align="center">
  <img src="/assets/images/medieval-shop-game.png" alt="Medieval Shop Game" style="max-width: 600px; width: 100%;">
</p>

**[View on Itch.io](https://goldleafinteractive.itch.io/medieval-shop-game)**

---

### Million Miles Deep
**Unreal Engine 5 · Blueprints**

Oceanic bullet-hell **2D**—enemy patterns, tight projectiles/UI.

<p align="center">
  <img src="/assets/images/million-miles-deep.png" alt="Million Miles Deep" style="max-width: 260px; width: 48%; display: inline-block;">
  <img src="/assets/images/million-miles-deep-2.png" alt="Million Miles Deep" style="max-width: 260px; width: 48%; display: inline-block;">
</p>

**[View on Itch.io](https://goldleafinteractive.itch.io/million-miles-deep)**

---

### Ragdoll Plainly Perilous
**Unreal Engine 5 · Blueprints**

Experimental ragdoll-as-controller traversal with stable collision tuning.

<p align="center">
  <img src="/assets/images/ragdoll-plainly-perilous.png" alt="Ragdoll Plainly Perilous" style="max-width: 600px; width: 100%;">
</p>

**[View on Itch.io](https://goldleafinteractive.itch.io/ragdoll-plainly-perilous)** · [Demo](https://www.youtube.com/watch?v=GfrDt166KZI)

---

### Crimson Eclipse
**Unreal Engine 5 · Blueprints**

Side-scrolling horror pacing—enemy/encounter logic, environment beats, HUD comms.

<p align="center">
  <img src="/assets/images/crimson-eclipse.png" alt="Crimson Eclipse" style="max-width: 600px; width: 100%;">
</p>

**[View on Itch.io](https://goldleafinteractive.itch.io/crimson-eclipse)** · [Demo](https://www.youtube.com/watch?v=R7KG3vuqHx4)

---

## More

~**16** jam/class loops if you count everything:

- **I AM INEVITABLE** (UE5 · Chillennium ’26) — defeats raise stats; retro movement with wall interplay leading to dash · **[Windows](https://goldleafinteractive.itch.io/i-am-inevitable)**
- **Doors n' Dice** · [itch](https://goldleafinteractive.itch.io/doors-n-dice)
- **Escape Control** · see [profile](https://goldleafinteractive.itch.io/)
- Misc mechanics labs · old capture exports **maybe** later for archive

---

 [← Back to Home](index)
