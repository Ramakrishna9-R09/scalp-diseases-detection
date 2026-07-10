// ScalpAI — Frontend Logic (Multi-Image Edition)
'use strict';

const API_BASE = window.location.origin;
let selectedModel = 'ensemble';
let selectedFiles  = [];   // array of File objects

/* ════════════════════════════════════════════════════════
   PARTICLES
════════════════════════════════════════════════════════ */
(function initParticles() {
  const canvas = document.getElementById('particles-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  let W, H, particles = [];

  function resize() {
    W = canvas.width  = window.innerWidth;
    H = canvas.height = window.innerHeight;
  }
  resize();
  window.addEventListener('resize', resize);

  const COLORS = ['#7c3aed','#06b6d4','#ec4899','#10b981'];
  for (let i = 0; i < 55; i++) {
    particles.push({
      x: Math.random() * window.innerWidth,
      y: Math.random() * window.innerHeight,
      r: Math.random() * 1.8 + 0.4,
      vx: (Math.random() - 0.5) * 0.35,
      vy: (Math.random() - 0.5) * 0.35,
      color: COLORS[Math.floor(Math.random() * COLORS.length)],
      alpha: Math.random() * 0.5 + 0.15,
    });
  }

  function draw() {
    ctx.clearRect(0, 0, W, H);
    particles.forEach(p => {
      p.x += p.vx; p.y += p.vy;
      if (p.x < 0) p.x = W; if (p.x > W) p.x = 0;
      if (p.y < 0) p.y = H; if (p.y > H) p.y = 0;
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = p.color + Math.round(p.alpha * 255).toString(16).padStart(2,'0');
      ctx.fill();
    });
    // draw faint connecting lines
    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const dx = particles[i].x - particles[j].x;
        const dy = particles[i].y - particles[j].y;
        const dist = Math.sqrt(dx*dx + dy*dy);
        if (dist < 130) {
          ctx.beginPath();
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          ctx.strokeStyle = `rgba(124,58,237,${0.07 * (1 - dist/130)})`;
          ctx.lineWidth = 0.8;
          ctx.stroke();
        }
      }
    }
    requestAnimationFrame(draw);
  }
  draw();
})();

/* ════════════════════════════════════════════════════════
   API STATUS CHECK
════════════════════════════════════════════════════════ */
window.addEventListener('load', async () => {
  const dot  = document.getElementById('status-dot');
  const text = document.getElementById('status-text');
  try {
    const r = await fetch(`${API_BASE}/health`, { signal: AbortSignal.timeout(3500) });
    const d = await r.json();
    dot.classList.add('online');
    if (d.simulation_mode) {
      text.textContent = 'Demo Mode';
      showToast('⚠️ Running in Demo Mode — train models for real AI predictions', 'error');
    } else {
      text.textContent = 'API Online';
      showToast('✅ AI models loaded and ready!', 'success');
    }
  } catch {
    dot.classList.add('offline');
    text.textContent = 'API Offline';
    showToast('⚠️ Flask backend not running. Start it with start.bat', 'error');
  }
});

/* ════════════════════════════════════════════════════════
   MODEL SELECTOR
════════════════════════════════════════════════════════ */
document.querySelectorAll('.model-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.model-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    selectedModel = btn.dataset.model;
    showToast(`Model: ${btn.textContent.trim()}`, 'success');
  });
});

/* ════════════════════════════════════════════════════════
   UPLOAD ZONE
════════════════════════════════════════════════════════ */
const uploadZone = document.getElementById('upload-zone');
const fileInput  = document.getElementById('file-input');

uploadZone.addEventListener('dragover',  e => { e.preventDefault(); uploadZone.classList.add('dragover'); });
uploadZone.addEventListener('dragleave', () => uploadZone.classList.remove('dragover'));
uploadZone.addEventListener('drop', e => {
  e.preventDefault();
  uploadZone.classList.remove('dragover');
  const files = Array.from(e.dataTransfer.files).filter(f => f.type.startsWith('image/'));
  if (files.length) addFiles(files);
  else showToast('Please drop image files only.', 'error');
});
uploadZone.addEventListener('click', e => {
  if (e.target.classList.contains('uz-btn') || e.target.closest('.uz-btn')) return;
  fileInput.click();
});
fileInput.addEventListener('change', () => {
  if (fileInput.files.length) addFiles(Array.from(fileInput.files));
  fileInput.value = '';
});

function addFiles(files) {
  const imageFiles = files.filter(f => f.type.startsWith('image/'));
  if (!imageFiles.length) { showToast('No valid image files found.', 'error'); return; }

  // Merge, avoiding duplicates by name+size
  imageFiles.forEach(f => {
    const exists = selectedFiles.some(sf => sf.name === f.name && sf.size === f.size);
    if (!exists && selectedFiles.length < 10) selectedFiles.push(f);
  });

  if (selectedFiles.length >= 10) showToast('Maximum 10 images allowed.', 'error');
  renderPreviews();
}

function renderPreviews() {
  const section = document.getElementById('previews-section');
  const grid    = document.getElementById('previews-grid');
  const count   = document.getElementById('previews-count');

  if (!selectedFiles.length) { section.style.display = 'none'; return; }
  section.style.display = 'block';
  count.textContent = `${selectedFiles.length} image${selectedFiles.length > 1 ? 's' : ''} selected`;

  grid.innerHTML = '';
  selectedFiles.forEach((file, idx) => {
    const url = URL.createObjectURL(file);
    const thumb = document.createElement('div');
    thumb.className = 'preview-thumb';
    thumb.innerHTML = `
      <img src="${url}" alt="${file.name}" loading="lazy"/>
      <div class="preview-thumb-num">${idx + 1}</div>
      <div class="preview-thumb-remove" onclick="removeImage(${idx}, event)" title="Remove">✕</div>
    `;
    grid.appendChild(thumb);
  });
}

window.removeImage = function(idx, e) {
  e.stopPropagation();
  selectedFiles.splice(idx, 1);
  renderPreviews();
};

window.clearAllImages = function() {
  selectedFiles = [];
  renderPreviews();
  document.getElementById('results-section').classList.remove('visible');
};

/* ════════════════════════════════════════════════════════
   ANALYSIS
════════════════════════════════════════════════════════ */
window.runAnalysis = async function() {
  if (!selectedFiles.length) { showToast('Please upload at least one image.', 'error'); return; }

  const btn  = document.getElementById('analyze-btn');
  const btext = document.getElementById('analyze-btn-text');
  btn.disabled = true;
  btext.textContent = 'Analyzing…';

  document.getElementById('results-section').classList.remove('visible');
  showLoading(true);
  animatePipeline();

  try {
    // Use the first image for prediction (backend takes one image; multi-image for UX)
    const formData = new FormData();
    formData.append('image', selectedFiles[0]);
    formData.append('model', selectedModel);

    const resp = await fetch(`${API_BASE}/predict`, { method: 'POST', body: formData });
    if (!resp.ok) throw new Error(`Server error ${resp.status}`);
    const data = await resp.json();

    await new Promise(r => setTimeout(r, 2400));
    showLoading(false);
    renderResults(data);

  } catch (err) {
    showLoading(false);
    showToast(`Error: ${err.message}. Make sure Flask is running.`, 'error');
  } finally {
    btn.disabled = false;
    btext.textContent = 'Analyze Scalp Condition';
  }
};

function showLoading(show) {
  const el = document.getElementById('loading-section');
  if (show) el.classList.add('visible');
  else       el.classList.remove('visible');
}

const PIPELINE_MSGS = [
  'Normalizing image resolution…',
  'Extracting texture features…',
  'Running CNN deep analysis…',
  'Running MobileNetV2 inference…',
  'Combining ensemble predictions…',
  'Generating treatment report…',
];
function animatePipeline() {
  const steps = ['step1','step2','step3','step4','step5','step6'];
  const sub   = document.getElementById('loading-sub');
  steps.forEach(s => {
    const el = document.getElementById(s);
    el.classList.remove('active','done');
  });
  steps.forEach((s, i) => {
    setTimeout(() => {
      const el = document.getElementById(s);
      el.classList.add('active');
      sub.textContent = PIPELINE_MSGS[i];
      if (i > 0) {
        const prev = document.getElementById(steps[i - 1]);
        prev.classList.remove('active');
        prev.classList.add('done');
      }
    }, i * 380);
  });
}

/* ════════════════════════════════════════════════════════
   RENDER RESULTS
════════════════════════════════════════════════════════ */
function renderResults(data) {
  const p = data.prediction;

  // ── Banner ──
  document.getElementById('res-disease-name').textContent = p.disease_name;
  document.getElementById('doc-for-disease').textContent  = p.disease_name;
  document.getElementById('res-model').textContent  = data.model_used.toUpperCase();
  document.getElementById('res-time').textContent   = `${data.inference_time}s`;
  document.getElementById('res-images').textContent = `${selectedFiles.length} image${selectedFiles.length > 1 ? 's' : ''}`;

  document.getElementById('res-badges').innerHTML = `
    <span class="badge badge-severity">${p.severity}</span>
    <span class="badge badge-specialist">🩺 ${p.specialist}</span>
    ${data.simulation_mode ? '<span class="badge badge-demo">⚠️ Demo Mode</span>' : ''}
  `;

  // ── Confidence arc ──
  const pct = p.confidence;
  const circ = 2 * Math.PI * 50;
  const offset = circ - (pct / 100) * circ;
  document.getElementById('db-pct').textContent = `${pct.toFixed(1)}%`;
  setTimeout(() => { document.getElementById('db-arc').style.strokeDashoffset = offset; }, 120);

  // ── Overview: about ──
  document.getElementById('res-description').textContent = p.description;
  document.getElementById('res-symptoms').innerHTML =
    p.symptoms.map(s => `<span class="symptom-tag">${s}</span>`).join('');

  // ── Overview: top-3 ──
  document.getElementById('top3-list').innerHTML = data.top3.map((item, i) => `
    <li class="top3-item">
      <div class="top3-hd">
        <span class="top3-rank">#${i+1}</span>
        <span class="top3-name">${item.name}</span>
        <span class="top3-pct">${item.confidence.toFixed(1)}%</span>
      </div>
      <div class="top3-bar">
        <div class="top3-fill" style="width:0" data-w="${item.confidence}"></div>
      </div>
    </li>
  `).join('');
  // animate bars after paint
  requestAnimationFrame(() => {
    document.querySelectorAll('.top3-fill').forEach(el => {
      el.style.width = el.dataset.w + '%';
    });
  });

  // ── Analyzed images thumbs ──
  const aiRow = document.getElementById('analyzed-images-row');
  aiRow.innerHTML = '';
  selectedFiles.forEach(file => {
    const url = URL.createObjectURL(file);
    const d = document.createElement('div');
    d.className = 'ai-thumb';
    d.innerHTML = `<img src="${url}" alt="${file.name}"/>`;
    aiRow.appendChild(d);
  });

  // ── Urgency ──
  const col  = p.urgency_color;
  const days = p.days_to_doctor;
  const icons  = { green: '✅', yellow: '⚠️', red: '🚨' };
  const titles = {
    green:  'Low Urgency — Schedule at your convenience',
    yellow: 'Moderate Urgency — Book an appointment soon',
    red:    'HIGH URGENCY — See a doctor immediately',
  };
  const subs = {
    green:  'Manageable with home care and OTC treatment',
    yellow: 'Condition may worsen without professional care',
    red:    'Delay may cause permanent scarring or hair loss',
  };
  const ud = document.getElementById('urgency-display');
  ud.className = `urgency-display urgency-${col}`;
  document.getElementById('urgency-icon').textContent   = icons[col];
  document.getElementById('urgency-days').className     = `urgency-days ${col}`;
  document.getElementById('urgency-days').textContent   = days;
  document.getElementById('urgency-text').textContent   = titles[col];
  document.getElementById('urgency-sub').textContent    = subs[col];
  document.getElementById('res-specialist').textContent = `🩺 ${p.specialist}`;

  // ── Medications ──
  renderMedications(p.medications);

  // ── Home care ──
  document.getElementById('home-care-list').innerHTML =
    p.home_care.map(tip => `
      <li class="care-item">
        <span class="ci-icon">✅</span>
        <div><strong>${tip}</strong></div>
      </li>
    `).join('');

  // ── Doctors ──
  if (data.doctors) renderDoctors(data.doctors);

  // ── Show results ──
  document.getElementById('results-section').classList.add('visible');
  document.getElementById('results-section').scrollIntoView({ behavior: 'smooth', block: 'start' });
  showToast(`Diagnosed: ${p.disease_name} (${pct.toFixed(1)}% confidence)`, 'success');

  // ── Geolocation ──
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(pos => {
      document.getElementById('location-badge').textContent =
        `📍 ${pos.coords.latitude.toFixed(3)}°, ${pos.coords.longitude.toFixed(3)}°`;
    }, () => {
      document.getElementById('location-badge').textContent = '📍 Nearby Specialists';
    });
  }
}

/* ════════════════════════════════════════════════════════
   MEDICATIONS
════════════════════════════════════════════════════════ */
const MED_ICONS = { prescription: '💊', otc: '🏪', natural: '🌿' };

function renderMedications(meds) {
  ['prescription','otc','natural'].forEach(type => {
    const panel = document.getElementById(`medpanel-${type}`);
    const badge = document.getElementById(`mtt-badge-${type}`);
    const list  = meds[type] || [];
    badge.textContent = list.length;
    panel.innerHTML = list.map(m => `
      <div class="med-card">
        <div class="med-card-icon">${MED_ICONS[type]}</div>
        <div class="med-name">${m.name}</div>
        <div class="med-pills">
          <span class="med-pill"><span class="med-pill-icon">📋</span>${m.dosage}</span>
          <span class="med-pill"><span class="med-pill-icon">⏱️</span>${m.duration}</span>
        </div>
      </div>
    `).join('');
  });
}

window.switchMedTab = function(type, btn) {
  document.querySelectorAll('.mtt').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.med-panel').forEach(p => p.classList.remove('active'));
  btn.classList.add('active');
  document.getElementById(`medpanel-${type}`).classList.add('active');
};

/* ════════════════════════════════════════════════════════
   RESULT TABS
════════════════════════════════════════════════════════ */
window.switchResultTab = function(tab, btn) {
  document.querySelectorAll('.rtab').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.rtab-panel').forEach(p => p.classList.remove('active'));
  if (btn) btn.classList.add('active');
  else document.querySelector(`[data-tab="${tab}"]`).classList.add('active');
  document.getElementById(`tab-${tab}`).classList.add('active');
};

/* ════════════════════════════════════════════════════════
   DOCTORS
════════════════════════════════════════════════════════ */
function renderDoctors(doctors) {
  document.getElementById('doctors-grid').innerHTML = doctors.map(doc => {
    const initials = doc.name.split(' ').slice(1, 3).map(n => n[0]).join('');
    const stars    = '★'.repeat(Math.floor(doc.rating)) + (doc.rating % 1 >= 0.5 ? '½' : '');
    return `
    <div class="doctor-card">
      <div class="doctor-header">
        <div class="doctor-avatar" style="background:linear-gradient(135deg,${doc.image_color},${doc.image_color}99)">${initials}</div>
        <div>
          <div class="doctor-name">${doc.name}</div>
          <div class="doctor-specialty">${doc.specialty}</div>
        </div>
      </div>
      <div class="doctor-rating">
        <span class="stars">${stars}</span>
        <span class="rating-num">${doc.rating}</span>
        <span class="rating-count">(${doc.reviews} reviews)</span>
      </div>
      <div class="doctor-meta">
        <span class="meta-item">📍 ${doc.distance}</span>
        <span class="meta-item">💰 ${doc.fee}</span>
        <span class="meta-item">🏥 ${doc.hospital}</span>
        <span class="meta-item">⏰ ${doc.available}</span>
        <span class="meta-item">🎓 ${doc.experience}</span>
        <span class="meta-item">⭐ ${doc.rating}/5.0</span>
      </div>
      <div class="doctor-footer">
        <button class="btn-book" onclick="showToast('Booking with ${doc.name}…', 'success')">📅 Book Appointment</button>
        <button class="btn-call" onclick="showToast('Calling ${doc.phone}…', 'success')" title="Call">📞</button>
      </div>
    </div>`;
  }).join('');
}

/* ════════════════════════════════════════════════════════
   TOAST
════════════════════════════════════════════════════════ */
let toastTimer;
window.showToast = function(msg, type = 'success') {
  const t    = document.getElementById('toast');
  const icon = document.getElementById('toast-icon');
  const msgEl= document.getElementById('toast-msg');
  icon.textContent = type === 'success' ? '✅' : '⚠️';
  msgEl.textContent = msg;
  t.className = `toast ${type} show`;
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => t.classList.remove('show'), 4500);
};
