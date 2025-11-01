REPO_URL=https://github.com/odoo/odoo.git
FOLDER_PATH=./odoo
git clone --depth=1 --filter=blob:none --no-checkout $REPO_URL $FOLDER_PATH
cd $FOLDER_PATH
git sparse-checkout init
# echo '/*\n!/addons/' >> ./.git/info/sparse-checkout
echo '/*\n' >> ./.git/info/sparse-checkout # currently we do not determined which module is add so just clone it community version
git checkout
git remote set-url "origin" git@github.com:Ecom-Consulting/ecom.git