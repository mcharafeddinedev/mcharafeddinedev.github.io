(function () {
  'use strict';

  var canvas = document.getElementById('matrix-bg');
  if (!canvas) return;
  var ctx = canvas.getContext('2d');

  var animationTime = 0;
  var lastFrameTime = 0;

  var shards = [];
  var embers = [];
  var streamLines = [];
  var lightSweepY = 0;

  var W = 0;
  var H = 0;

  // --- Helpers ---

  function rand(min, max) {
    return min + Math.random() * (max - min);
  }

  function rotatePoint(px, py, cx, cy, angle) {
    var cos = Math.cos(angle);
    var sin = Math.sin(angle);
    var dx = px - cx;
    var dy = py - cy;
    return { x: cx + dx * cos - dy * sin, y: cy + dx * sin + dy * cos };
  }

  function spawnPosition() {
    var side = Math.floor(Math.random() * 5);
    var x, y, vx, vy;
    switch (side) {
      case 0: // top
        x = rand(0, W); y = -30; vx = rand(-15, 15); vy = rand(10, 40); break;
      case 1: // right
        x = W + 30; y = rand(0, H); vx = rand(-40, -10); vy = rand(-15, 15); break;
      case 2: // bottom
        x = rand(0, W); y = H + 30; vx = rand(-15, 15); vy = rand(-40, -10); break;
      case 3: // left
        x = -30; y = rand(0, H); vx = rand(10, 40); vy = rand(-15, 15); break;
      default: // center
        x = rand(W * 0.2, W * 0.8); y = rand(H * 0.2, H * 0.8);
        var angle = rand(0, Math.PI * 2);
        var speed = rand(15, 35);
        vx = Math.cos(angle) * speed; vy = Math.sin(angle) * speed; break;
    }
    return { x: x, y: y, vx: vx, vy: vy };
  }

  // --- Initialization ---

  function resize() {
    W = window.innerWidth;
    H = window.innerHeight;
    canvas.width = W;
    canvas.height = H;
  }

  function initStreamLines(count) {
    streamLines = [];
    for (var i = 0; i < count; i++) {
      streamLines.push({
        x: rand(0, W),
        y: rand(0, H),
        length: rand(50, 150),
        speed: rand(10, 30),
        alpha: rand(0.1, 0.3)
      });
    }
  }

  function initShards(count) {
    shards = [];
    for (var i = 0; i < count; i++) {
      var sp = spawnPosition();
      var speed = rand(30, 65);
      var mag = Math.sqrt(sp.vx * sp.vx + sp.vy * sp.vy) || 1;
      shards.push({
        x: sp.x, y: sp.y,
        vx: (sp.vx / mag) * speed,
        vy: (sp.vy / mag) * speed,
        size: rand(12, 28),
        rotation: rand(0, Math.PI * 2),
        rotSpeed: rand(1.5, 4.0),
        phase: rand(0, Math.PI * 2)
      });
    }
  }

  function initEmbers(count) {
    embers = [];
    for (var i = 0; i < count; i++) {
      var sp = spawnPosition();
      var speed = rand(25, 60);
      var mag = Math.sqrt(sp.vx * sp.vx + sp.vy * sp.vy) || 1;
      embers.push({
        x: sp.x, y: sp.y,
        vx: (sp.vx / mag) * speed,
        vy: (sp.vy / mag) * speed,
        size: rand(4, 12),
        rotation: rand(0, Math.PI * 2),
        phase: rand(0, Math.PI * 2)
      });
    }
  }

  // --- Drawing ---

  function drawGradientBackground() {
    var grad = ctx.createLinearGradient(0, 0, 0, H);
    grad.addColorStop(0, 'rgb(3, 5, 3)');
    grad.addColorStop(0.5, 'rgb(6, 10, 7)');
    grad.addColorStop(1, 'rgb(8, 14, 9)');
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, W, H);
  }

  function drawDataStreamLines(dt) {
    for (var i = 0; i < streamLines.length; i++) {
      var sl = streamLines[i];
      sl.y -= sl.speed * dt;
      if (sl.y + sl.length < 0) {
        sl.y = H + rand(10, 50);
        sl.x = rand(0, W);
        sl.alpha = rand(0.1, 0.3);
      }

      // glow pass
      ctx.beginPath();
      ctx.moveTo(sl.x, sl.y);
      ctx.lineTo(sl.x, sl.y + sl.length);
      ctx.strokeStyle = 'rgba(10, 90, 10, ' + (sl.alpha * 0.3) + ')';
      ctx.lineWidth = 2.5;
      ctx.stroke();

      // core line
      ctx.beginPath();
      ctx.moveTo(sl.x, sl.y);
      ctx.lineTo(sl.x, sl.y + sl.length);
      ctx.strokeStyle = 'rgba(20, 180, 20, ' + sl.alpha + ')';
      ctx.lineWidth = 1;
      ctx.stroke();
    }
  }

  function drawCRTScanlines() {
    var opacity = 0.15 + Math.sin(animationTime * 2.0) * 0.05;
    ctx.strokeStyle = 'rgba(0, 50, 0, ' + opacity + ')';
    ctx.lineWidth = 1;
    ctx.beginPath();
    for (var y = 0; y < H; y += 8) {
      ctx.moveTo(0, y);
      ctx.lineTo(W, y);
    }
    ctx.stroke();
  }

  function drawLightSweep(dt) {
    lightSweepY -= 200 * dt;
    if (lightSweepY < -120) {
      lightSweepY = H + 200;
    }

    var sweepHeight = 120;
    var opacity = 0.12 + Math.sin(animationTime * 1.5) * 0.04;
    var grad = ctx.createLinearGradient(0, lightSweepY, 0, lightSweepY + sweepHeight);
    grad.addColorStop(0, 'rgba(20, 200, 20, 0)');
    grad.addColorStop(0.5, 'rgba(20, 200, 20, ' + opacity + ')');
    grad.addColorStop(1, 'rgba(20, 200, 20, 0)');
    ctx.fillStyle = grad;
    ctx.fillRect(0, lightSweepY, W, sweepHeight);
  }

  function wrapCoord(val, max, margin) {
    if (val < -margin) return max + margin;
    if (val > max + margin) return -margin;
    return val;
  }

  function updateAndDrawShards(dt) {
    for (var i = 0; i < shards.length; i++) {
      var s = shards[i];

      // perpendicular sinusoidal drift
      var driftAngle = Math.atan2(s.vy, s.vx) + Math.PI * 0.5;
      var drift = Math.sin(animationTime * 0.3 + s.phase) * 12 * dt;
      s.x += s.vx * dt + Math.cos(driftAngle) * drift;
      s.y += s.vy * dt + Math.sin(driftAngle) * drift;

      s.rotation += s.rotSpeed * dt;

      s.x = wrapCoord(s.x, W, 50);
      s.y = wrapCoord(s.y, H, 50);

      var alpha = 0.4 + Math.sin(animationTime * 2.5 + s.phase) * 0.2;
      var shimmer = 0.5 + 0.5 * Math.sin(animationTime * 4 + s.phase * 2 + s.rotation);

      var sz = s.size;
      // Triangle vertices (pointing up, then rotated)
      var p0 = rotatePoint(s.x, s.y - sz, s.x, s.y, s.rotation);
      var p1 = rotatePoint(s.x - sz * 0.5, s.y + sz * 0.5, s.x, s.y, s.rotation);
      var p2 = rotatePoint(s.x + sz * 0.5, s.y + sz * 0.5, s.x, s.y, s.rotation);

      // dark body fill
      var fr = Math.round(5 + shimmer * 8);
      var fg = Math.round(8 + shimmer * 15);
      var fb = Math.round(8 + shimmer * 12);
      ctx.globalAlpha = alpha;
      ctx.beginPath();
      ctx.moveTo(p0.x, p0.y);
      ctx.lineTo(p1.x, p1.y);
      ctx.lineTo(p2.x, p2.y);
      ctx.closePath();
      ctx.fillStyle = 'rgb(' + fr + ',' + fg + ',' + fb + ')';
      ctx.fill();

      // neon green edge stroke
      var er = 0;
      var eg = Math.round(150 + shimmer * 105);
      var eb = Math.round(75 + shimmer * 80);
      ctx.strokeStyle = 'rgba(' + er + ',' + eg + ',' + eb + ',' + (alpha * (0.7 + shimmer * 0.3)) + ')';
      ctx.lineWidth = 2 + shimmer * 1;
      ctx.stroke();

      // shimmer highlight on one edge
      var highlightPhase = (s.rotation + animationTime * 2) % (Math.PI * 2);
      if (highlightPhase < Math.PI) {
        ctx.beginPath();
        ctx.moveTo(p0.x, p0.y);
        ctx.lineTo(p1.x, p1.y);
        ctx.strokeStyle = 'rgba(0, 255, 128, ' + (alpha * shimmer) + ')';
        ctx.lineWidth = 3 * shimmer;
        ctx.stroke();
      }

      ctx.globalAlpha = 1;
    }
  }

  function updateAndDrawEmbers(dt) {
    for (var i = 0; i < embers.length; i++) {
      var e = embers[i];

      var driftAngle = Math.atan2(e.vy, e.vx) + Math.PI * 0.5;
      var drift = Math.sin(animationTime * 0.4 + e.phase) * 8 * dt;
      e.x += e.vx * dt + Math.cos(driftAngle) * drift;
      e.y += e.vy * dt + Math.sin(driftAngle) * drift;

      e.rotation += 2.0 * dt;

      e.x = wrapCoord(e.x, W, 30);
      e.y = wrapCoord(e.y, H, 30);

      var alpha = 0.5 + Math.sin(animationTime * 3.0 + e.phase) * 0.3;
      var shimmer = 0.5 + 0.5 * Math.sin(animationTime * 5 + e.phase * 3);
      var sz = e.size * (0.8 + shimmer * 0.4);

      // Diamond: 4 points rotated
      var top = rotatePoint(e.x, e.y - sz, e.x, e.y, e.rotation);
      var right = rotatePoint(e.x + sz * 0.6, e.y, e.x, e.y, e.rotation);
      var bottom = rotatePoint(e.x, e.y + sz, e.x, e.y, e.rotation);
      var left = rotatePoint(e.x - sz * 0.6, e.y, e.x, e.y, e.rotation);

      var eg = Math.round(180 + shimmer * 75);
      var eb = Math.round(90 + shimmer * 90);
      ctx.globalAlpha = alpha * shimmer;

      ctx.beginPath();
      ctx.moveTo(top.x, top.y);
      ctx.lineTo(right.x, right.y);
      ctx.lineTo(bottom.x, bottom.y);
      ctx.lineTo(left.x, left.y);
      ctx.closePath();
      ctx.fillStyle = 'rgb(0,' + eg + ',' + eb + ')';
      ctx.fill();

      ctx.strokeStyle = 'rgba(0, 255, 150, ' + (alpha * shimmer * 0.9) + ')';
      ctx.lineWidth = 1.5 * shimmer;
      ctx.stroke();

      ctx.globalAlpha = 1;
    }
  }

  // --- Main loop ---

  function animate(timestamp) {
    if (!lastFrameTime) lastFrameTime = timestamp;
    var dt = (timestamp - lastFrameTime) / 1000;
    if (dt > 0.1) dt = 0.1; // clamp to prevent spiral on tab-switch
    lastFrameTime = timestamp;
    animationTime += dt;

    drawGradientBackground();
    drawDataStreamLines(dt);
    drawCRTScanlines();
    drawLightSweep(dt);
    updateAndDrawShards(dt);
    updateAndDrawEmbers(dt);

    requestAnimationFrame(animate);
  }

  function init() {
    resize();
    initStreamLines(15);
    initShards(25);
    initEmbers(15);
    lightSweepY = H + 200;
    requestAnimationFrame(animate);
  }

  window.addEventListener('resize', function () {
    resize();
    // reinit stream lines so they distribute across new width
    initStreamLines(15);
  });

  init();
})();
