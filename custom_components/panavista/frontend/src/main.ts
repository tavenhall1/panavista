// PanaVista Calendar v1.0
// Single entry point — imports all cards and registers them with HA

// Reusable sub-components
import './components/color-swatch-picker';
import './components/onboarding-wizard';

import './cards/panavista-calendar-card';
import './cards/panavista-grid-card';
import './cards/panavista-agenda-card';
import './cards/panavista-clock-card';
import './cards/panavista-weather-card';
import './cards/panavista-toggles-card';

// Register all cards with the HA card picker
window.customCards = window.customCards || [];
window.customCards.push(
  {
    type: 'panavista-calendar-card',
    name: 'PanaVista Calendar (Unified)',
    description: 'All-in-one calendar with clock, weather, toggles, and views',
    preview: true,
  },
  {
    type: 'panavista-grid-card',
    name: 'PanaVista Grid',
    description: 'Calendar grid with day, week, and month views',
    preview: true,
  },
  {
    type: 'panavista-agenda-card',
    name: 'PanaVista Agenda',
    description: 'Upcoming events list',
    preview: true,
  },
  {
    type: 'panavista-clock-card',
    name: 'PanaVista Clock',
    description: 'Time and date display',
    preview: true,
  },
  {
    type: 'panavista-weather-card',
    name: 'PanaVista Weather',
    description: 'Weather conditions and forecast',
    preview: true,
  },
  {
    type: 'panavista-toggles-card',
    name: 'PanaVista Toggles',
    description: 'Calendar visibility toggles',
    preview: true,
  },
);

console.info(
  '%c PANAVISTA %c v1.0.0 ',
  'color: white; background: #6366F1; font-weight: bold; border-radius: 4px 0 0 4px; padding: 2px 6px;',
  'color: #6366F1; background: #EEF2FF; font-weight: bold; border-radius: 0 4px 4px 0; padding: 2px 6px;',
);
