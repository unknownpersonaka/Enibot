sudo apt-get update && sudo apt-get -y upgrade && sudo apt-get -y dist-upgrade
sudo apt-get install -y python3 python3-pip
mkdir -vp ~/Desktop/Books ~/Downloads/book_learning ~/Downloads/files_garbage
pip install -r ./requirements.txt
wget https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.63/linux64/chrome-linux64.zip
wget https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.63/linux64/chromedriver-linux64.zip
unzip ./chromedriver-linux64.zip
unzip ./chrome-linux64.zip -d ~/Downloads/
rm -rfv /usr/bin/chromedriver
rm -rfv /bin/chromedriver
cp -vf ./chromedriver-linux64/chromedriver /usr/bin/
mv -vf ./chromedriver-linux64/chromedriver /bin/
rm -rfv ./chrome*
echo -e "\n\e[1;32m[+] Done !\e[0m"