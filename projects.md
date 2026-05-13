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

Solo hobby project—inspired more by *Hackers* than realism. Paddle = your way in; breakout blocks peel back layers of a faux terminal, and typed commands finish off special bricks while the ball is still moving. Built to feel playable in a browser and clean on a portfolio page.

<p align="center">
  <img src="/assets/images/access-granted.png" alt="Access Granted CRT-style gameplay" style="max-width: 600px; width: 100%;">
</p>

- Pause-friendly flow between ball play and typing modes (slow-mo prompts, timers that behave when you pause the game).
- CRT look is stacked on purpose—barrel distortion plus a bezel/scan overlay so it reads as “one cohesive screen,” not one filter pasted on menus.
- Two separate counters for run-ending mistakes: misses from dropping the ball vs. missing or timing out prompts.
- Word pools are chunked in authoring data so later levels tighten phrases without refactoring the typing loop entirely.
- Optional secret finale uses a scripted ring layout (not a rectangular grid grab-bag).

<div class="itch-embed-wrap" style="text-align: center; margin: 1.5rem 0;">
  <iframe id="itch-embed-access-granted-projects" title="Itch.io: Access Granted" frameborder="0" loading="lazy" src="https://itch.io/embed/4475328?linkback=true&amp;border_width=2&amp;bg_color=060d06&amp;fg_color=b9c6e4&amp;link_color=00edd6&amp;border_color=084808" width="552" height="167" class="itch-embed"></iframe>
</div>

**[Play on Itch.io](https://goldleafinteractive.itch.io/access-granted)** · [Patch Notes v2](https://goldleafinteractive.itch.io/access-granted/devlog/1516113/patch-notes-v2)

---

### Dread & Breakfast
**Unity 6 · C# · Beta / Post-jam · WebGL & Windows**

Mini Jam prototype that kept growing—a top-down “you’re the ghost” management puzzle. Nights get harder, layouts reshuffle, you match abilities to scared guests’ weaknesses, chase fright points between runs, crack open upgrades and a shop (“Box of Tricks”), and poke at quieter drag-and-scare experimentation.

<p align="center">
  <img src="/assets/images/dread-and-breakfast.png" alt="Dread & Breakfast floor plan gameplay" style="max-width: 600px; width: 100%;">
</p>

- Procedural house pass: picks a template (avoids repeats when there are several), lays out rooms/doors to connect, fills walls with readable prop placement—including props that visually “pay off” versus room entrances where it matters on TV setups.
- Guest brain lives in one main AI script today: wandering, chatting, escalating fear off matching scare types, chaining panic when somebody bolts, tweaking presentation as fear climbs.
- 17 haunt abilities are authored as reusable data; perk picks between nights and the meta shop stay on a simple event bus rather than messy cross-calls.
- Night length, headcount ramps, hourly guests after harder nights—all tunable knobs so escalation feels authored, not chaotic.

<div class="itch-embed-wrap" style="text-align: center; margin: 1.5rem 0;">
  <iframe id="itch-embed-dread-breakfast" title="Itch.io: Dread & Breakfast" frameborder="0" loading="lazy" src="https://itch.io/embed/4471600?linkback=true&amp;bg_color=000000&amp;fg_color=e6d699&amp;link_color=fa5c5c&amp;border_color=282828" width="552" height="167" class="itch-embed"></iframe>
</div>

**[Play on Itch.io](https://goldleafinteractive.itch.io/dread-and-breakfast)** · Started at *Mini Jam 208: Inverted* (2026), still iterating — notes: [Energy bubbles · update](https://goldleafinteractive.itch.io/dread-and-breakfast/devlog/1489095/update-1-fixes-energy-bubbles-deep-freeze) · [v0.9 beta UI pass](https://goldleafinteractive.itch.io/dread-and-breakfast/devlog/1501963/patch-notes-v090-beta)

---

### Trenchglow
**Unity (2D URP) · C# · In development · WebGL playable slice**

Mini Jam starter for *Deep*: you poke through black-water trenches mostly by guesswork until sonar pings give you brief “memory maps.” Stamina on swim boosts, puzzles that move rock geometry, collectible gems—it’s deliberately more exploration than pure platform twitch.

<p align="center">
  <img src="/assets/images/trenchglow.png" alt="Trenchglow underwater key art" style="max-width: 600px; width: 100%;">
</p>

- Terrain reveals lean on shaders for each sonar ping, while a toned-down fallback covers weaker GPUs when you ship HTML5 builds.
- On-screen darkness is a mix of a small “local” hole around the diver and the ring that opens with each ping, so the info you get always lines up with audio and motion.
- Scriptable settings are cloned per run so iterating a level doesn’t silently rewrite the shared assets you reuse everywhere.
- Big moving rocks are scripted as designer-friendly kinematic rigs (reset hooks, sfx timing, chaining via Unity events).

<div class="itch-embed-wrap" style="text-align: center; margin: 1.5rem 0;">
  <iframe id="itch-embed-trenchglow" title="Itch.io: Trenchglow" frameborder="0" loading="lazy" src="https://itch.io/embed/4513861?linkback=true&amp;bg_color=0a1628&amp;fg_color=cfe8ff&amp;link_color=f5a524&amp;border_color=1a3d5c" width="552" height="167" class="itch-embed"></iframe>
</div>

**[Play on Itch.io](https://goldleafinteractive.itch.io/trenchglow)** · Tutorial demo public now; fuller trench rollout still on the roadmap.

---

### BREATHE Arcade
**Unity 6 · C# · 2D URP · Emergent Technologies capstone · WebGL + Windows**

Five miniature games (sailboat race, constellation reveal, balloons, bubbles, skydiving target landings). Breath feeds everything when you plug in hardware; microphone or keyboard stand-in kicks in elsewhere so teachers and booth visitors aren’t stranded.

<p align="center">
  <img src="/assets/images/breathe-arcade.png" alt="BREATHE Arcade promo art" style="max-width: 600px; width: 100%;">
</p>

- Breath source is routed through one interchangeable interface fan / mic / simulated so play logic never forks per device.
- Custom fan MCU sends serial lines interpreted on a worker thread—COM auto-discovery, smoothing, rejecting spikes—in parallel with coursework documentation for wiring details.
- The shared breath smoothing layer trims “motor coastdown” artefacts on hardware that physically stops slower than airflow did.
- Minigames share the same results/pacing shell, with lightweight per-mode settings so one tune-up doesn’t fork the whole codebase.

<div class="itch-embed-wrap" style="text-align: center; margin: 1.5rem 0;">
  <iframe id="itch-embed-breathe-arcade" title="Itch.io: BREATHE Arcade" frameborder="0" loading="lazy" src="https://itch.io/embed/4475446?linkback=true&amp;bg_color=d6f5ff&amp;fg_color=0b2d3f&amp;link_color=ff4f6e&amp;border_color=93cdea" width="552" height="167" class="itch-embed"></iframe>
</div>

**[Play / download on Itch.io](https://goldleafinteractive.itch.io/breathe-arcade)** · Hardware deep-dive available for employers privately; README / HOW_IT_WORKS summarise the Unity side publicly.

---

### OVERCLOCKED: Data Dash MAX
**Unreal Engine 5.7 · C++ & Blueprints · Released (PC & Arcade Cabinet)**

An endless runner for arcade cabinets **and** PC: race as an electric impulse through neon tunnels—lane changes, jumps, slides, overclock bursts, pickups, escalating speed, medals, themed looks, offline leaderboards, all tuned so cabinet builds stay smooth.

<p align="center">
  <img src="/assets/images/overclocked-data-dash-max.png" alt="OVERCLOCKED: Data Dash MAX" style="max-width: 600px; width: 100%;">
</p>

- Modular C++ components split spawning, movement, pickups, presentation swaps, leaderboard flow, navigable HUD without assuming mouse-first players.
- 40-plus handcrafted obstacle combos pipeline through authored data feeds so repeats feel rhythmic instead of sloppy randomness.
- Six visual themes rotate look without changing fundamentals; pickups and UX feedback were tuned once PC feedback landed and arcade controls came online.

<div class="itch-embed-wrap" style="text-align: center; margin: 1.5rem 0;">
  <iframe id="itch-embed-overclocked-projects" title="Itch.io: Overclocked DDM" frameborder="0" loading="lazy" src="https://itch.io/embed/4278897?linkback=true&amp;border_width=5&amp;bg_color=000000&amp;fg_color=fffcbc&amp;link_color=46ffd4&amp;border_color=979797" width="552" height="167" class="itch-embed"></iframe>
</div>

**[Windows build on Itch.io](https://goldleafinteractive.itch.io/overclocked-ddm)** · [Patch notes v1.1.0](https://goldleafinteractive.itch.io/overclocked-ddm/devlog/1379247/v110-patch-notes-overclocked-ddm) · [Trailer](https://www.youtube.com/watch?v=dI9Ctq9LkLs)

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

Shorter prototypes and jam-complete builds (~16 playable loops counting coursework plus jams):

- **I AM INEVITABLE** (UE5 · Chillennium 2026 jam) — failure ramps your stats; chunky retro visuals; traversal loop with wall tricks and eventual dash · **[Windows download](https://goldleafinteractive.itch.io/i-am-inevitable)**
- **Doors n' Dice** (UE5) — [Itch.io](https://goldleafinteractive.itch.io/doors-n-dice)
- **Escape Control** (UE5) — Listed on **[itch profile](https://goldleafinteractive.itch.io/)**
- Misc classroom mechanics labs · Some old class capture videos might go public eventually for archival completeness

---

 [← Back to Home](index)
