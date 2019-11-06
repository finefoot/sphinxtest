git config user.name finefoot
git config user.email finefoot@finefoot.finefoot
git push -d origin gh-pages
git checkout -b gh-pages
cd docs
sphinx-build -b html . .
git add -A
git commit -m "Update Sphinx"
git push origin gh-pages
