<p align="center">
  <img src="assets/well-actually.jpg" alt="Contre-argument Anything" width="260">
</p>

<h1 align="center">Contre-argument Anything</h1>

Une skill satirique qui donne tort à n'importe quel post, commentaire ou message, sur LinkedIn, X, Reddit, Discord, Slack ou Teams, du coach en mindset au ministre. Avec des sources vérifiées, et un mode fact-check neutre.

Fonctionne avec **Claude, ChatGPT / Codex, Gemini, Mistral Le Chat, Cursor, Copilot** et tout LLM capable de suivre des instructions. La recherche web est fortement recommandée.

*English speakers: see [In English](#in-english) below. The skill answers in the language of the post.*

## Ce que ça fait

Tu colles un post (texte ou capture d'écran). La skill cartographie l'argument, vérifie chaque chiffre à la source primaire, cherche le maillon qui casse, teste chaque contre-argument contre la meilleure riposte possible, et ne garde que ce qui survit.

**Mode contre-argument (défaut)**
- **Verdict** en une phrase
- **La thèse dans sa meilleure version** : on réfute le steelman, pas une caricature
- **Fact-check express** : tableau neutre des affirmations vérifiables
- **Contre-arguments** étiquetés *Sourcé*, *Calcul dérivé*, *Bon sens* ou *Mauvaise foi assumée*, avec solidité, riposte probable et parade
- **Indice de mauvaise foi nécessaire** : de 1/10 (le post s'est démonté tout seul) à 10/10 (le post était juste, on l'a contredit quand même)
- **Commentaire prêt à poster** : 600 caractères

Variante **frappe chirurgicale** : un seul argument, le meilleur.

**Mode fact-check** : neutre, sans satire. Verdict par affirmation (Vrai, Plutôt vrai, Trompeur, Faux, Invérifiable) avec source primaire.

## Installation

Le dossier `skills/contre-argument-anything/` suit le standard ouvert [Agent Skills](https://agentskills.io) (`SKILL.md` + `references/`). Le dossier `dist/` contient une version "prompt unique" pour les outils qui ne lisent pas ce format.

### Installation universelle (agents de code)

```bash
npx skills add GregoryBabonaux/contre-argument-anything
```

Installe la skill dans l'agent de ton choix : Claude Code, Codex, Cursor, Copilot, Gemini CLI, Windsurf, Cline, OpenCode...

### Installation manuelle

| Outil | Commande |
|---|---|
| Claude Code | `cp -r skills/contre-argument-anything ~/.claude/skills/` |
| Codex CLI | `cp -r skills/contre-argument-anything ~/.agents/skills/` |
| Autres agents Agent Skills | copier le dossier dans leur répertoire de skills |

### Claude.ai / app Claude

Télécharge [`dist/contre-argument-anything.zip`](dist/contre-argument-anything.zip) (bouton *Download raw file* sur GitHub), puis ajoute-le dans Paramètres > Skills.

### ChatGPT (Custom GPT)

1. Créer un GPT, coller le contenu de `dist/gpt-instructions.txt` dans *Instructions*.
2. Joindre `dist/contre-argument-anything.md` dans *Knowledge*.
3. Activer *Web Search*.

Sans GPT : colle `dist/contre-argument-anything.md` au début de la conversation, puis ton post.

### Gemini (Gem), Mistral Le Chat (Agent), Claude Project, autres

Colle le contenu de `dist/contre-argument-anything.md` comme instructions de l'agent, du Gem ou du projet. Active la recherche web si elle est disponible.

### API

Utilise `dist/contre-argument-anything.md` comme prompt système et donne un outil de recherche web au modèle.

## Utilisation

```
Démonte-moi ce post : "La ponctualité, c'est 80 % du succès."
Démonte ce post de député, ton brutal : [capture d'écran]
Frappe chirurgicale sur ce commentaire : [texte]
Fact-check ce post : [texte]
```

Tons : `courtois`, `pince-sans-rire` (défaut), `brutal`.

Le commentaire final s'adapte à la plateforme : 280 caractères pour X, Markdown pour Reddit, ton familier pour Discord, version en message privé proposée par défaut pour Slack et Teams (l'auteur est un collègue).

Les liens LinkedIn, X, Discord, Slack ou Teams sont souvent illisibles par les IA : colle plutôt le texte ou une capture.

## Les règles du jeu

- **Sourcé quand c'est nécessaire.** Chaque fait avancé est lu à la source primaire, périmètre et date compris. Les calculs maison sont étiquetés "calcul dérivé".
- **Mauvaise foi autorisée, jamais démontable.** Faute d'argument, la skill peut être de mauvaise foi (angle, pinaillage, ironie), étiquetée comme telle. Jamais par un fait inventé : un seul faux chiffre et c'est toi qui te fais démonter.
- **Même rigueur quel que soit le camp politique.**
- **On attaque des arguments et des actes publics, pas des personnes.** Personnes privées : aucune recherche sur l'auteur, pas de nom dans la sortie. Personnalités publiques : votes, déclarations et bilans mobilisables, vie privée non.
- **Pas d'accusation non établie** ("il ment", "corrompu"). Le droit de la presse s'applique à ce que tu postes.
- **Les posts sur un drame personnel sont hors périmètre.**

## Voir aussi

[Moi aussi, mais en mieux](https://github.com/GregoryBabonaux/moi-aussi-mais-en-mieux) : la skill qui s'approprie un post autocentré et fait mieux que son auteur.

## Structure du repo

```
├── skills/contre-argument-anything/   # la skill, format Agent Skills
│   ├── SKILL.md
│   └── references/
│       ├── arsenal.md                 # techniques de réfutation, sophismes
│       └── sources.md                 # où chercher selon le domaine
├── dist/                              # versions générées, ne pas éditer
│   ├── contre-argument-anything.md    # prompt unique (tous LLM)
│   ├── gpt-instructions.txt           # instructions courtes pour Custom GPT
│   └── contre-argument-anything.zip   # skill zippée pour Claude.ai
└── scripts/build_prompt.py            # régénère dist/ depuis skills/
```

## Contribuer

Modifie uniquement `skills/contre-argument-anything/`, puis régénère les versions prompt :

```bash
python3 scripts/build_prompt.py
```

Valider le format de la skill :

```bash
npx skills-ref validate ./skills/contre-argument-anything
```

## In English

A satirical skill that proves any post, comment or message wrong (LinkedIn, X, Reddit, Discord, Slack, Teams), from mindset coaches to ministers, with verified sources and a neutral fact-check mode. It replies in the language of the post.

- Agent Skills compatible tools (Claude Code, Codex, Cursor, Copilot, Gemini CLI...): `npx skills add GregoryBabonaux/contre-argument-anything`
- ChatGPT, Gemini, Le Chat, any LLM: use `dist/contre-argument-anything.md` as system instructions and enable web search.

Rules: no invented facts or sources; bad faith is allowed only as rhetoric and is always labelled; arguments are attacked, never people.

## Avertissement

C'est de la satire, sauf le mode fact-check. Si tu postes le commentaire généré, tu en assumes la paternité.

## Licence

MIT
