# path_source="/workspaces/pytouch/.devcontainer/.env"

# # Check if the file exists
# if [ -f "$path_source" ]; then
#     echo "$path_source found."
#     source $path_source
#     echo "Gitlab credentials"
#     echo "TOKEN: $GITLAB_TOKEN "
#     echo "USER: $GITLAB_ID "
#     /tmp/_install_python_modules.sh
#     exit 0
# else 
#     echo "$path_source not found."
#     echo "Creating a .env file in the .devcontainer folder with the following content:"
#     touch $path_source
#     echo "File created"
#     echo "export GITLAB_TOKEN={your_token}" >> $path_source
#     echo "export GITLAB_ID={your_id}" >> $path_source
#     echo "Please fill the {your_token} and {your_id} fields in $path_source"
#     exit 1
# fi

# echo 'PYTHONPATH="$PYTHONPATH:/workspaces/pycopo"' >> /home/vscode/.bashrc
# echo 'PYTHONPATH="$PYTHONPATH:/workspaces/pycama"' >> /home/vscode/.bashrc
# echo 'PYTHONPATH="$PYTHONPATH:/workspaces/image_datasets"' >> /home/vscode/.bashrc
# echo 'PYTHONPATH="$PYTHONPATH:/workspaces/igus"' >> /home/vscode/.bashrc
# echo 'PYTHONPATH="$PYTHONPATH:/workspaces/carmen/Client"' >> /home/vscode/.bashrc
# echo 'export PYTHONPATH' >> /home/vscode/.bashrc

