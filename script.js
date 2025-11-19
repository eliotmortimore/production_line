// Production Line Simulator State
const state = {
    // Materials
    materials: 30,
    
    // Forming
    forming_min: 28,
    forming_max: 30,
    forming_queue: 0,
    forming_prod: 0,
    
    // CNC
    cnc_min: 28,
    cnc_max: 30,
    cnc_queue: 0,
    cnc_prod: 0,
    
    // Buffing
    buffing_min: 28,
    buffing_max: 29,
    buffing_queue: 0,
    buffing_prod: 0,
    
    // Completed
    completed: 0,
    turn: 0
};

// DOM Elements
const elements = {
    turnCount: document.getElementById('turn-count'),
    materialsPerTurn: document.getElementById('materials-per-turn'),
    formingQueue: document.getElementById('forming-queue'),
    formingProduction: document.getElementById('forming-production'),
    formingRange: document.getElementById('forming-range'),
    cncQueue: document.getElementById('cnc-queue'),
    cncProduction: document.getElementById('cnc-production'),
    cncRange: document.getElementById('cnc-range'),
    buffingQueue: document.getElementById('buffing-queue'),
    buffingProduction: document.getElementById('buffing-production'),
    buffingRange: document.getElementById('buffing-range'),
    completedCount: document.getElementById('completed-count'),
    runBtn: document.getElementById('run-btn'),
    showBtn: document.getElementById('show-btn'),
    resetBtn: document.getElementById('reset-btn'),
    settingsBtn: document.getElementById('settings-btn'),
    settingsModal: document.getElementById('settings-modal'),
    closeModal: document.querySelector('.close')
};

// Utility Functions
function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Core Simulation Logic
function advance() {
    // Add active class to stations to show they're processing
    const stations = document.querySelectorAll('.station:not(.arrow)');
    stations.forEach(station => station.classList.add('active'));
    
    // Animate arrows
    const arrows = document.querySelectorAll('.arrow');
    arrows.forEach(arrow => arrow.classList.add('active'));
    
    // Materials supply
    const incoming = state.materials;
    state.forming_queue += incoming;
    
    // Highlight forming station
    const formingStation = document.getElementById('forming-station');
    formingStation.classList.add('active');
    
    // Forming
    state.forming_prod = getRandomInt(state.forming_min, state.forming_max);
    state.forming_prod = Math.min(state.forming_prod, state.forming_queue);
    state.forming_queue -= state.forming_prod;
    state.cnc_queue += state.forming_prod;
    
    // Highlight CNC station
    formingStation.classList.remove('active');
    const cncStation = document.getElementById('cnc-station');
    cncStation.classList.add('active');
    
    // CNC
    state.cnc_prod = getRandomInt(state.cnc_min, state.cnc_max);
    state.cnc_prod = Math.min(state.cnc_prod, state.cnc_queue);
    state.cnc_queue -= state.cnc_prod;
    state.buffing_queue += state.cnc_prod;
    
    // Highlight buffing station
    cncStation.classList.remove('active');
    const buffingStation = document.getElementById('buffing-station');
    buffingStation.classList.add('active');
    
    // Buffing
    state.buffing_prod = getRandomInt(state.buffing_min, state.buffing_max);
    state.buffing_prod = Math.min(state.buffing_prod, state.buffing_queue);
    state.buffing_queue -= state.buffing_prod;
    state.completed += state.buffing_prod;
    
    state.turn++;
    
    // Remove active classes after a delay
    setTimeout(() => {
        buffingStation.classList.remove('active');
        stations.forEach(station => station.classList.remove('active'));
        arrows.forEach(arrow => arrow.classList.remove('active'));
    }, 500);
}

function updateDisplay() {
    // Update stats
    elements.turnCount.textContent = state.turn;
    elements.materialsPerTurn.textContent = state.materials;
    
    // Update forming station
    elements.formingQueue.textContent = state.forming_queue;
    elements.formingProduction.textContent = state.forming_prod;
    elements.formingRange.textContent = `${state.forming_min}/${state.forming_max}`;
    
    // Update CNC station
    elements.cncQueue.textContent = state.cnc_queue;
    elements.cncProduction.textContent = state.cnc_prod;
    elements.cncRange.textContent = `${state.cnc_min}/${state.cnc_max}`;
    
    // Update buffing station
    elements.buffingQueue.textContent = state.buffing_queue;
    elements.buffingProduction.textContent = state.buffing_prod;
    elements.buffingRange.textContent = `${state.buffing_min}/${state.buffing_max}`;
    
    // Update completed
    elements.completedCount.textContent = state.completed;
}

function doRun() {
    // Show running indicator
    document.querySelector('.controls').classList.add('running');
    
    advance();
    updateDisplay();
    
    // Hide running indicator after a delay
    setTimeout(() => {
        document.querySelector('.controls').classList.remove('running');
    }, 600);
}

function doShow() {
    updateDisplay();
}

function doReset() {
    state.materials = 30;
    state.forming_queue = state.forming_prod = 0;
    state.cnc_queue = state.cnc_prod = 0;
    state.buffing_queue = state.buffing_prod = 0;
    state.completed = 0;
    state.turn = 0;
    
    // Reset settings inputs to default values
    document.getElementById('materials-input').value = 30;
    document.getElementById('forming-min').value = 28;
    document.getElementById('forming-max').value = 30;
    document.getElementById('cnc-min').value = 28;
    document.getElementById('cnc-max').value = 30;
    document.getElementById('buffing-min').value = 28;
    document.getElementById('buffing-max').value = 29;
    
    updateDisplay();
}

// Settings Functions
function openSettings() {
    // Populate settings with current values
    document.getElementById('materials-input').value = state.materials;
    document.getElementById('forming-min').value = state.forming_min;
    document.getElementById('forming-max').value = state.forming_max;
    document.getElementById('cnc-min').value = state.cnc_min;
    document.getElementById('cnc-max').value = state.cnc_max;
    document.getElementById('buffing-min').value = state.buffing_min;
    document.getElementById('buffing-max').value = state.buffing_max;
    
    elements.settingsModal.style.display = 'block';
}

function closeSettings() {
    elements.settingsModal.style.display = 'none';
}

function saveMaterials() {
    const value = parseInt(document.getElementById('materials-input').value);
    if (!isNaN(value) && value > 0) {
        state.materials = value;
        updateDisplay();
        alert(`Materials per turn set to ${value}.`);
    } else {
        alert('Please enter a positive integer.');
    }
}

function saveFormingSettings() {
    const min = parseInt(document.getElementById('forming-min').value);
    const max = parseInt(document.getElementById('forming-max').value);
    
    if (!isNaN(min) && !isNaN(max) && min > 0 && max >= min) {
        state.forming_min = min;
        state.forming_max = max;
        updateDisplay();
        alert(`Forming range set to ${min}-${max}.`);
    } else {
        alert('Invalid range. MAX must be ≥ MIN and both > 0.');
    }
}

function saveCNCSettings() {
    const min = parseInt(document.getElementById('cnc-min').value);
    const max = parseInt(document.getElementById('cnc-max').value);
    
    if (!isNaN(min) && !isNaN(max) && min > 0 && max >= min) {
        state.cnc_min = min;
        state.cnc_max = max;
        updateDisplay();
        alert(`CNC range set to ${min}-${max}.`);
    } else {
        alert('Invalid range. MAX must be ≥ MIN and both > 0.');
    }
}

function saveBuffingSettings() {
    const min = parseInt(document.getElementById('buffing-min').value);
    const max = parseInt(document.getElementById('buffing-max').value);
    
    if (!isNaN(min) && !isNaN(max) && min > 0 && max >= min) {
        state.buffing_min = min;
        state.buffing_max = max;
        updateDisplay();
        alert(`Buffing range set to ${min}-${max}.`);
    } else {
        alert('Invalid range. MAX must be ≥ MIN and both > 0.');
    }
}

// Event Listeners
document.addEventListener('DOMContentLoaded', () => {
    // Initialize display
    updateDisplay();
    
    // Button event listeners
    elements.runBtn.addEventListener('click', doRun);
    elements.showBtn.addEventListener('click', doShow);
    elements.resetBtn.addEventListener('click', doReset);
    elements.settingsBtn.addEventListener('click', openSettings);
    
    // Modal event listeners
    elements.closeModal.addEventListener('click', closeSettings);
    window.addEventListener('click', (event) => {
        if (event.target === elements.settingsModal) {
            closeSettings();
        }
    });
    
    // Settings save buttons
    document.getElementById('save-materials').addEventListener('click', saveMaterials);
    document.getElementById('save-forming').addEventListener('click', saveFormingSettings);
    document.getElementById('save-cnc').addEventListener('click', saveCNCSettings);
    document.getElementById('save-buffing').addEventListener('click', saveBuffingSettings);
    
    // Keyboard shortcuts
    document.addEventListener('keydown', (event) => {
        if (event.key === 'Enter' || event.key === ' ') {
            doRun();
        } else if (event.key === 's' || event.key === 'S') {
            doShow();
        } else if (event.key === 'r' || event.key === 'R') {
            doRun();
        }
    });
});