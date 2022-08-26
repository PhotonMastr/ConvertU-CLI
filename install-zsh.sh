mkdir $HOME/ConvertU_CLI/
pip install pyinstaller
pyinstaller --onefile ConvertU.py
mv $HOME/ConvertU-CLI/dist/ConvertU $HOME/ConvertU_CLI/
echo "alias ConvertU='~/ConvertU_CLI/./ConvertU'" >> $HOME/.zshrc
source $HOME/.zshrc 
echo "ConvertU-CLI is installed!"
