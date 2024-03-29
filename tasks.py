import pathlib
import re
import subprocess
import sys

from invoke import task
import proselint as plnt

import known


@task
def compile(c):
    """
    Compile the LaTeX document.
    """

    c.run(f"latexmk -xelatex main.tex")


@task
def spellcheck(c):
    """
    Check the spelling of all .tex files
    """

    all_tex_files = list(pathlib.Path().glob("**/*.tex"))
    exit_codes = [0]
    for path in all_tex_files:
        latex = path.read_text()
        aspell_output = subprocess.check_output(
            ["aspell", "-t", "--list", "--lang=en_GB"], input=latex, text=True
        )
        errors = set(aspell_output.split("\n")) - {""}
        incorrect_words = set()
        for error in errors:
            if not any(
                re.fullmatch(word.lower(), error.lower()) for word in known.words
            ):
                incorrect_words.add(error)

        if len(incorrect_words) > 0:
            print(f"In {path} the following words are not known: ")
            for string in sorted(incorrect_words):
                print(string)
            exit_codes.append(1)
    sys.exit(max(exit_codes))


@task
def proselint(c):
    """
    Check the spelling of all .tex files
    """

    def remove_expected_errors(errors):
        """
        Remove errors that were expected from the error list
        """
        expected_errors = (
            "annotations.misc",
            "leonard.exclamation.30ppm",
            "typography.symbols.ellipsis",
            "typography.symbols.sentence_spacing",
            "security.credit_card",
        )
        updated_errors = []
        for error in errors:
            if error[0] not in expected_errors:
                updated_errors.append(error)
        return updated_errors

    def clean_text(text):
        """
        Remove latex commands from text
        """
        cleaned_text = text.replace("\centering", "")
        return cleaned_text

    all_tex_files = list(pathlib.Path().glob("**/*.tex"))
    exit_codes = [0]
    for path in all_tex_files:
        with open(path, "r") as f:
            text = f.read()
            cleaned_text = clean_text(text)
            errors = plnt.tools.lint(cleaned_text)
        errors = remove_expected_errors(errors)
        if errors:
            print(f"In {path} the following errors were found: ")
            for error in errors:
                print(error)
            exit_codes.append(1)
    sys.exit(max(exit_codes))


@task
def alex(c):
    """
    Check for inconsiderate and insensitive writing of all .tex files
    """
    all_tex_files = list(pathlib.Path().glob("**/*.tex"))
    for file in all_tex_files:
        c.run(f"alex {file}")


@task
def doctests(c):
    """
    Run doctests
    """
    c.run('python -m pytest --doctest-glob="*.tex"')
