# Hearth Integration

How the Hearth offline community hub consumes Salvage Electronics release artifacts.

> This document describes the integration contract. Implementation lives in the `hearth` repo, not here.

---

## Release Artifacts

Each tagged release of this repo is expected to publish the following Hearth-facing artifacts:

| Artifact | Description |
|----------|-------------|
| `salvage-vX.Y.Z.tar.gz` | Self-contained HTML site — served by nginx in static mode |
| `salvage.zim` | Kiwix ZIM file — reserved for Phase 2 packaging |

The tarball is the current deployment artifact. The ZIM filename is documented now so Hearth can treat it as a future-stable contract when Phase 2 packaging lands.

---

## Static Mode (nginx)

### How the Hearth Ansible Role Consumes the Tarball

The `hearth` repo contains an ansible role that:

1. Downloads the pinned release tarball from GitHub releases.
2. Extracts it to a directory on the server (for example `/srv/hearth/salvage/`).
3. Configures nginx to serve the directory at `/salvage/`.

The `hearth.yaml` configuration (in the `hearth` repo) pins the release version:

```yaml
services:
  salvage:
    enabled: true
    version: "v0.1.0"
    mode: static
```

### nginx Path Convention

Content is served at `/salvage/`. The stable public paths are the content contract that other Hearth services, especially Open Circuits, can link against:

```
/salvage/index.html                        # root
/salvage/foundations/01-why-salvage.html
/salvage/foundations/02-safety.html
/salvage/foundations/03-tools-and-workspace.html
/salvage/foundations/04-core-techniques.html
/salvage/donor-guides/NN-{slug}.html       # NN is the zero-padded index
/salvage/components/NN-{slug}.html
/salvage/projects/NN-{slug}.html
```

A minimal nginx location block:

```nginx
location /salvage/ {
    alias /srv/hearth/salvage/;
    index index.html;
    try_files $uri $uri/ =404;
}
```

---

## URL Stability Contract

**Paths must not change across versions.**

Open Circuits may deep-link into Salvage Electronics, and Salvage content already uses absolute `/open-circuits/...` links back into Open Circuits. The following `/salvage/...` paths are stable by contract:

| Area | Stable URL pattern |
|------|--------------------|
| Root | `/salvage/index.html` |
| Foundations | `/salvage/foundations/01-why-salvage.html` through `/salvage/foundations/04-core-techniques.html` |
| Donor guides | `/salvage/donor-guides/NN-{slug}.html` |
| Components | `/salvage/components/NN-{slug}.html` |
| Projects | `/salvage/projects/NN-{slug}.html` |

**Do not:**
- Rename the top-level `/salvage/` prefix.
- Replace the zero-padded `NN-` filename scheme.
- Flatten section directories.
- Add version numbers to public URLs.

If a structural change ever becomes necessary, it must be coordinated with both the `hearth` and `open-circuits` repos before release.

---

## Cross-references into Open Circuits

Salvage Electronics links into Open Circuits with absolute `/open-circuits/...` paths only. The current cross-reference map is:

| Salvage topic | Open Circuits chapter URL | Used for |
|---------------|---------------------------|----------|
| DC measurements, continuity, polarity, discharge verification | `/open-circuits/DC/DC_5.html` | donor guides, most component pages, and every project stub that depends on bench measurements |
| Semiconductors, rectifiers, MOSFETs, regulators, inverter devices | `/open-circuits/Semi/SEMI_6.html` | power-focused donor guides, active-device component pages, and PSU / charger projects |
| Bench experiments, quick test rigs, low-voltage fixtures | `/open-circuits/Exper/EXPER_1.html` | battery-device and low-voltage donor guides, passive/mechanical component pages, and simple project builds |

Keep these links short and inline. Do not use copied theory text, footnotes, or relative cross-project paths.

---

## How Open Circuits Links Back

If Open Circuits ever adds “See the salvage guide” links, it should do so with absolute `/salvage/...` paths, for example:

- `/salvage/foundations/02-safety.html`
- `/salvage/donor-guides/07-atx-power-supplies.html`
- `/salvage/components/05-mosfets.html`
- `/salvage/projects/02-cap-discharge-tool.html`

Do not use relative links like `../salvage/...`; nginx resolves the shared contract at the site root.

---

## Upgrading to a New Release

To update the pinned version on a Hearth deployment:

1. Tag a new release in this repo.
2. Confirm the release includes the expected HTML tarball artifact.
3. Update `version:` in `hearth.yaml` in the `hearth` repo.
4. Run the Hearth ansible playbook so nginx is updated to the new tarball.

When Phase 2 ZIM packaging exists, the same upgrade flow will apply to `salvage.zim` for Kiwix-based deployments.
