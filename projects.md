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
- CRT effe is intentional: barrel + bezel/scan = **one** cohesive screen (**menus included**).
- **Two** strike tracks (drops vs mistypes/timeouts); **word pools chunked in data**; optional **scripted ring finale** instead of a rectangular grid-only finish.

<div class="itch-embed-wrap" style="text-align: center; margin: 1.5rem 0;">
  <iframe id="itch-embed-access-granted-projects" title="Itch.io: Access Granted" frameborder="0" loading="lazy" src="https://itch.io/embed/4475328?linkback=true&amp;border_width=2&amp;bg_color=060d06&amp;fg_color=b9c6e4&amp;link_color=00edd6&amp;border_color=084808" width="552" height="167" class="itch-embed"></iframe>
</div>

**[Play on Itch.io](https://goldleafinteractive.itch.io/access-granted)** · [Patch Notes v2](https://goldleafinteractive.itch.io/access-granted/devlog/1516113/patch-notes-v2)

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

**[Play on Itch.io](https://goldleafinteractive.itch.io/dread-and-breakfast)** · Started at *Mini Jam 208: Inverted* (2026) · [Patches](https://goldleafinteractive.itch.io/dread-and-breakfast/devlog/1489095/update-1-fixes-energy-bubbles-deep-freeze) · [v0.9 beta](https://goldleafinteractive.itch.io/dread-and-breakfast/devlog/1501963/patch-notes-v090-beta)(https://goldleafinteractive.itch.io/dread-and-breakfast/devlog/1489095/update-1-fixes-energy-bubbles-deep-freeze) · [v0.9 beta](https://goldleafinteractive.itch.io/dread-and-breakfast/devlog/1501963/patch-notes-v090-beta)

---

### Trenchglow
**Unity (2D URP) · C# · In development · WebGL playable slice**

*Deep*-themed jam: trench exploration in dark water—**ping-based reveals**, stamina boosts / moving rocks / gems—focused on curiosity more than twitch platforming alone.

<p align="center">
  <img src="/assets/images/trenchglow.png" alt="Trenchglow underwater key art" style="max-width: 600px; width: 100%;">
</p>

- Shader-driven pings for visibility with a toned-down fallback for **budget HTML5** targets.
- Vignette = local hole **plus** ping ring (**audio/visual lockstep**).
- **Clone** Scriptables per session so iterating never overwrites shared assets; kinematic boulder rigs for designers.

<div class="itch-embed-wrap" style="text-align: center; margin: 1.5rem 0;">
  <iframe id="itch-embed-trenchglow" title="Itch.io: Trenchglow" frameborder="0" loading="lazy" src="https://itch.io/embed/4513861?linkback=true&amp;bg_color=0a1628&amp;fg_color=cfe8ff&amp;link_color=f5a524&amp;border_color=1a3d5c" width="552" height="167" class="itch-embed"></iframe>
</div>

**[Play on Itch.io](https://goldleafinteractive.itch.io/trenchglow)** · Tutorial live; fuller trench roadmap.

---

### BREATHE Arcade
**Unity 6 · C# · 2D URP · Emergent Technologies capstone · WebGL + Windows**

Five micro-games (sailboat, constellations, balloons, bubbles, skydiving landings)—**breath-controlled** hardware with **microphone / keyboard** stand-ins for classrooms and booths.

<p align="center">
  <img src="/assets/images/breathe-arcade.png" alt="BREATHE Arcade promo art" style="max-width: 600px; width: 100%;">
</p>

- **One** breath-input abstraction drives fan / mic / simulated inputs without separate gameplay forks.
- Fan MCU → serial on a **worker thread** (discovery, smoothing, spike reject) + coursework wiring docs.
- Shared smoothing handles **motor coast-down** quirks when spin-down lags airflow; mini-games reuse **one completion shell** with per-mode tweak fields.

<div class="itch-embed-wrap" style="text-align: center; margin: 1.5rem 0;">
  <iframe id="itch-embed-breathe-arcade" title="Itch.io: BREATHE Arcade" frameborder="0" loading="lazy" src="https://itch.io/embed/4475446?linkback=true&amp;bg_color=d6f5ff&amp;fg_color=0b2d3f&amp;link_color=ff4f6e&amp;border_color=93cdea" width="552" height="167" class="itch-embed"></iframe>
</div>

**[Play / download on Itch.io](https://goldleafinteractive.itch.io/breathe-arcade)** · Employer wiring deep-dive on request · README / HOW_IT_WORKS cover Unity publicly.

---

### OVERCLOCKED: Data Dash MAX
**Unreal Engine 5.7 · C++ & Blueprints · Released (PC & Arcade Cabinet)**

Endless runner targeting **cabinet installs and desktop**: lane swaps, jumps, slides, pickups, escalating speed, medals, palettes, offline leaderboards—paced for **cabinet difficulty**.

<p align="center">
  <img src="/assets/images/overclocked-data-dash-max.png" alt="OVERCLOCKED: Data Dash MAX" style="max-width: 600px; width: 100%;">
</p>

- **C++** slices for spawn/move/pickups/HUD/nav—**no mouse-first** assumption.
- **Over 40** authored obstacle combos driven by structured data—not undifferentiated random spam.
- **Six** palettes; pickups + HUD tuned after **PC pass** landed and **arcade sticks** plugged in.

<div class="itch-embed-wrap" style="text-align: center; margin: 1.5rem 0;">
  <iframe id="itch-embed-overclocked-projects" title="Itch.io: Overclocked DDM" frameborder="0" loading="lazy" src="https://itch.io/embed/4278897?linkback=true&amp;border_width=5&amp;bg_color=000000&amp;fg_color=fffcbc&amp;link_color=46ffd4&amp;border_color=979797" width="552" height="167" class="itch-embed"></iframe>
</div>

**[Windows build on Itch.io](https://goldleafinteractive.itch.io/overclocked-ddm)** · [Patch v1.1.0](https://goldleafinteractive.itch.io/overclocked-ddm/devlog/1379247/v110-patch-notes-overclocked-ddm) · [Trailer](https://www.youtube.com/watch?v=dI9Ctq9LkLs)

---

### Quantum Tether
**Unity · C# · Released**

Roguelike sidescroller—**movement + grapple + momentum** first.

<p align="center">
  <img src="/assets/images/quantum-tether.png" alt="Quantum Tether" style="max-width: 600px; width: 100%;">
</p>

- **Vector grapple** swing; **10+** modular upgrades; **parametric anchor** variety; full **state/UI/HUD/difficulty** loop.

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
