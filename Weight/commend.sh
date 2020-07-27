git add .
git commit -m "$1 pull" || "autometic commit pull"
git pull origin weight
git add .
git commit -m "$1 push" || "autometic commit push"
git push origin weight