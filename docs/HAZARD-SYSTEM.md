# Hazard System

The hazard rating used on donor-guide pages.

---

## Purpose

Donor pages rate hazard level so a reader can tell, before opening the device, whether the guide covers routine low-voltage salvage or a device class that can injure or seriously harm even after unplugging.

The rating is there to frame the job honestly. It does not replace the safety chapter or device-specific instructions.

---

## The Four Levels

| Level | Color | Symbol description | Meaning | Example devices |
|------:|-------|--------------------|---------|-----------------|
| 1 | Safety green | Circle with check-style low-risk mark | Low-voltage salvage, no stored-energy concern beyond normal batteries | battery devices |
| 2 | Safety yellow | Triangle caution mark | Usually low-risk if unplugged, but minor stored energy or battery precautions still matter | wall chargers, routers/modems, printers, desktop computers, laptops, LED bulbs |
| 3 | Safety orange | Triangle warning mark with stronger alert emphasis | Mains-powered gear with substantial stored charge or serious shock risk if opened carelessly | ATX power supplies, audio equipment |
| 4 | Safety red | Stop/danger symbol with severe-hazard emphasis | Device class can retain lethal voltage or deliver extreme current; untrained readers may need to stop entirely | microwave ovens, CRT monitors, UPS units |

These levels match the donor-guide outline:
- Level 1 — battery devices
- Level 2 — wall chargers, routers/modems, printers, desktop computers, laptops, LED bulbs
- Level 3 — ATX power supplies, audio equipment
- Level 4 — microwave ovens, CRT monitors, UPS units

---

## Icon Design

Hazard SVGs follow these rules:

- `48×48` viewBox.
- Inline-friendly, self-contained SVG only.
- No external references, linked images, web fonts, or filters.
- Must stay readable when rendered at `40px`.
- Colors are locked to standard safety colors (green, yellow, orange, red), not the Open Circuits brand palette.

The icon is a signal boost, not the whole warning. The page always carries the text level label and summary sentence too.

---

## Placement

Place the hazard banner once per donor-guide page.

- It sits above the page content and below the shared header.
- It appears at the top of the main column.
- It comes before any disassembly, testing, or removal instructions.
- It is never repeated further down the page.

This keeps the warning impossible to miss without turning the whole page into alarm graphics.

---

## Writing the Summary Line

The summary line is the one-sentence worst-case warning.

Rules:
- Use present tense.
- Name the specific hazard.
- State the real consequence plainly.
- Do not write a generic “be careful” sentence.

Preferred:
- `HV capacitor can hold lethal charge for hours.`
- `Large input caps hold 300V+ for minutes after unplugging.`
- `Batteries stay live and can deliver very high short-circuit current.`

Avoid:
- `Be careful inside this device.`
- `This can be dangerous if mishandled.`

---

## When NOT to Use a Banner

Do not add the hazard banner to:

- `foundations/02-safety.html` — that page defines the system itself.
- Components pages — testing guidance there is intentionally low-hazard and bench-focused.
- Projects pages — put project-specific warnings inline where they occur.
- The home page or section indexes.

The banner is for donor-device triage, not for every page that mentions risk.

---

## Accessibility

Accessibility requirements are mandatory:

- The icon needs alt text.
- The banner needs an `aria-label`.
- The visible text label must include the level number and meaning.
- Color must never be the sole signal.

A reader who cannot distinguish the colors still needs the same warning from the text alone.

---

## Print Rendering

In print:

- Remove box shadow.
- Keep a solid border.
- Keep the level label and summary text intact.

The banner should print as a clean warning box, not a soft UI card.
