/* ════════════════════════════════════════════════
   STEMpathAI — main.js
   Starfield, scroll-reveal, navbar effects
   ════════════════════════════════════════════════ */

// ── Starfield ──
(function initStarfield() {
  const canvas = document.getElementById('starfield');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  function resize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }
  resize();
  window.addEventListener('resize', resize);

  const STAR_COUNT = 160;
  const stars = Array.from({ length: STAR_COUNT }, () => ({
    x: Math.random() * window.innerWidth,
    y: Math.random() * window.innerHeight,
    r: Math.random() * 1.4 + 0.2,
    opacity: Math.random() * 0.7 + 0.1,
    speed: Math.random() * 0.015 + 0.003,
    twinkleOffset: Math.random() * Math.PI * 2,
  }));

  let frame = 0;
  function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    frame++;
    stars.forEach(s => {
      const twinkle = 0.5 + 0.5 * Math.sin(frame * s.speed * 40 + s.twinkleOffset);
      ctx.beginPath();
      ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(255,255,255,${s.opacity * twinkle})`;
      ctx.fill();
    });
    requestAnimationFrame(draw);
  }
  draw();
})();

// ── Navbar scroll effect ──
(function initNavbar() {
  const nav = document.querySelector('.navbar');
  if (!nav) return;
  window.addEventListener('scroll', () => {
    const y = window.scrollY;
    if (y > 60) {
      nav.style.background = 'rgba(5,5,15,0.95)';
      nav.style.boxShadow = '0 4px 30px rgba(0,0,0,0.4)';
    } else {
      nav.style.background = 'rgba(5,5,15,0.8)';
      nav.style.boxShadow = 'none';
    }
    lastY = y;
  }, { passive: true });
})();

// ── Scroll-reveal ──
(function initReveal() {
  const els = document.querySelectorAll(
    '.step-card, .career-card, .info-card, .podium-card, .rank-row, .timeline-item'
  );
  if (!els.length) return;
  els.forEach(el => el.classList.add('reveal'));

  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) {
        // stagger sibling reveals
        const siblings = Array.from(e.target.parentElement.querySelectorAll('.reveal'));
        const idx = siblings.indexOf(e.target);
        setTimeout(() => {
          e.target.classList.add('visible');
        }, idx * 35);
        io.unobserve(e.target);
      }
    });
  }, { threshold: 0.05, rootMargin: '0px 0px 0px 0px' });

  els.forEach(el => io.observe(el));
})();

// ── Animate number counters on hero stats ──
(function initCounters() {
  const items = document.querySelectorAll('.stat-num');
  if (!items.length) return;
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (!e.isIntersecting) return;
      const el = e.target;
      const raw = el.textContent;
      const num = parseFloat(raw.replace(/[^0-9.]/g, ''));
      if (isNaN(num)) return;
      const prefix = raw.match(/^[^0-9]*/)[0];
      const suffix = raw.match(/[^0-9.]+$/)?.[0] || '';
      const duration = 1200;
      const startTime = performance.now();
      function tick(now) {
        const t = Math.min((now - startTime) / duration, 1);
        const ease = 1 - Math.pow(1 - t, 3);
        const cur = Math.round(ease * num * 10) / 10;
        el.textContent = prefix + (Number.isInteger(num) ? Math.round(cur) : cur) + suffix;
        if (t < 1) requestAnimationFrame(tick);
      }
      requestAnimationFrame(tick);
      io.unobserve(el);
    });
  }, { threshold: 0.5 });
  items.forEach(el => io.observe(el));
})();

// ── Career card tilt effect ──
(function initTilt() {
  const cards = document.querySelectorAll('.career-card');
  cards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const cx = rect.left + rect.width / 2;
      const cy = rect.top + rect.height / 2;
      const dx = (e.clientX - cx) / (rect.width / 2);
      const dy = (e.clientY - cy) / (rect.height / 2);
      card.style.transform = `translateY(-8px) rotateX(${-dy * 4}deg) rotateY(${dx * 4}deg)`;
    });
    card.addEventListener('mouseleave', () => {
      card.style.transform = '';
    });
  });
})();

// ── Typing effect for hero title (if present) ──
(function initTyping() {
  const hero = document.querySelector('.hero-title');
  if (!hero) return;
  // Just ensure it's visible — animation via CSS
})();

// ── Smooth page transitions ──
document.querySelectorAll('a[href]:not([target="_blank"])').forEach(link => {
  link.addEventListener('click', function (e) {
    const href = this.getAttribute('href');
    if (!href || href.startsWith('#') || href.startsWith('http') || href.startsWith('mailto')) return;
    e.preventDefault();
    document.body.style.opacity = '0';
    document.body.style.transition = 'opacity 0.25s ease';
    setTimeout(() => { window.location.href = href; }, 250);
  });
});
window.addEventListener('pageshow', () => {
  document.body.style.opacity = '1';
  document.body.style.transition = 'opacity 0.3s ease';
});
