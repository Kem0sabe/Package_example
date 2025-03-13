 `git submodule add https://github.com/Kem0sabe/CTAB_XTRA_DP.git ctab_xtra_dp` to make the subfolder for the actuall github repository

`pip install .` to install it for local testing (pip freeze should show local version)



`python -m build` to build new version to be deployed

`python -m twine upload dist/* --username __token__ --password *api_key*`