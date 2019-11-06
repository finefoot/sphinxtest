git config user.name finefoot
git config user.email finefoot@finefoot.finefoot
git config --list
git remote remove origin
git remote add origin https://${GITHUB_TOKEN}@github.com/${TRAVIS_REPO_SLUG}.git
git config --list
# darf auch failen
git push -d origin gh-pages
git checkout -b gh-pages
sphinx-build -b html docs docs/_build
git add -A
git commit -m "Update Sphinx"
git push origin gh-pages
