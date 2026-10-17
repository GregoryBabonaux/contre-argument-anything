#!/usr/bin/env python3
"""Génère les versions "prompt unique" de la skill pour les LLM qui ne lisent pas le format Agent Skills.

Sorties :
  dist/contre-argument-anything.md  : prompt complet (SKILL.md + annexes), à coller ou joindre
  dist/contre-argument-anything.zip : skill zippée pour Claude.ai
  dist/gpt-instructions.txt         : instructions courtes pour un Custom GPT (limite 8000 caractères),
                                      le fichier complet étant joint en "Knowledge"

Usage : python3 scripts/build_prompt.py
"""
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "contre-argument-anything"
DIST = ROOT / "dist"

ANNEXES = [
    ("A", "arsenal.md", "Arsenal de réfutation"),
    ("B", "sources.md", "Où chercher"),
]


def strip_frontmatter(text: str) -> str:
    return re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S).lstrip()


def demote_headings(text: str) -> str:
    # "# Titre" -> "### Titre", etc., pour imbriquer les annexes sous "## Annexe"
    return re.sub(r"^(#+) ", lambda m: "#" * (len(m.group(1)) + 1) + " ", text, flags=re.M)


def build_full() -> str:
    body = strip_frontmatter((SKILL / "SKILL.md").read_text(encoding="utf-8"))
    body = body.replace(
        "Avant de commencer, lis `references/arsenal.md` (techniques de réfutation) et "
        "`references/sources.md` (où chercher selon le domaine).",
        "Les techniques de réfutation sont en annexe A, les sources à consulter selon le domaine en annexe B.",
    )
    body = body.replace("`references/arsenal.md`", "l'annexe A").replace("`references/sources.md`", "l'annexe B")

    header = (
        "<!-- Fichier généré par scripts/build_prompt.py à partir de skills/contre-argument-anything/. "
        "Ne pas modifier à la main. -->\n\n"
        "> Usage : colle ce texte comme instructions système (ChatGPT, Gemini Gem, Le Chat, Claude Project, "
        "API...) ou joins-le à la conversation. Active la recherche web si l'outil la propose.\n\n"
    )
    parts = [header, body.rstrip(), "\n"]
    for letter, filename, title in ANNEXES:
        content = strip_frontmatter((SKILL / "references" / filename).read_text(encoding="utf-8"))
        content = re.sub(r"\A# .*\n+", "", content)  # retire le titre H1 d'origine
        parts.append(f"\n## Annexe {letter} : {title}\n\n{demote_headings(content).rstrip()}\n")
    return "".join(parts)


GPT_INSTRUCTIONS = """Tu es "Contre-argument Anything", un contradicteur satirique de posts et commentaires LinkedIn.

Ta méthode complète est dans le fichier joint contre-argument-anything.md. Avant chaque réponse, applique-la intégralement : étapes, règles de preuve, limites, mauvaise foi assumée, format de sortie et mode fact-check.

Règles qui priment sur tout :
- Aucune source, aucun chiffre, aucune citation inventés. Tout fait avancé est vérifié par recherche web et lu à la source.
- La mauvaise foi est permise quand on manque d'arguments, uniquement par la rhétorique (angle, ironie, pinaillage), jamais par un fait faux. Chaque argument est étiqueté : Sourcé, Calcul dérivé, Bon sens ou Mauvaise foi assumée.
- On attaque des arguments et des actes publics, jamais la personne. Pas d'accusation non établie ("il ment", "corrompu").
- Personne privée : pas de nom dans la sortie, aucune recherche sur elle. Personnalité publique : ses votes, déclarations et bilans sont mobilisables, pas sa vie privée.
- Post relatant un drame personnel : ne pas contredire le vécu.
- Réponds dans la langue du post. Pas de tiret cadratin.

Si l'utilisateur fournit un lien que tu ne peux pas ouvrir, demande-lui de coller le texte du post.
"""


def main() -> None:
    DIST.mkdir(exist_ok=True)
    full = build_full()
    (DIST / "contre-argument-anything.md").write_text(full, encoding="utf-8")
    (DIST / "gpt-instructions.txt").write_text(GPT_INSTRUCTIONS, encoding="utf-8")
    with zipfile.ZipFile(DIST / "contre-argument-anything.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(SKILL.rglob("*")):
            if f.is_file():
                z.write(f, Path("contre-argument-anything") / f.relative_to(SKILL))
    assert len(GPT_INSTRUCTIONS) < 8000, "Les instructions GPT dépassent 8000 caractères"
    print(f"dist/contre-argument-anything.md : {len(full)} caractères")
    print(f"dist/gpt-instructions.txt        : {len(GPT_INSTRUCTIONS)} caractères")


if __name__ == "__main__":
    main()
