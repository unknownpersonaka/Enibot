sudo apt-get -y remove python3 python3-pip
rm -rfv /usr/bin/chromedriver
rm -rfv /bin/chromedriver
rm -rfv $HOME/Downloads/chrome-linux64
sudo apt-get -y autoremove && sudo apt-get -y autoclean
echo -e "\e[1;32m[+] Done !\e[0m"
echo -e "\e[1;32m[-] You must remove this 3 directories if they are empty\e[0m"
echo -e "\n\e[1;33m ~> $HOME/Downloads/book_learning\e[0m"
echo -e "\e[1;33m ~> $HOME/Downloads/files_garbage\e[0m"
echo -e "\e[1;33m ~> $HOME/Desktop/Books\e[0m"
echo -e "\e[1;31m[!] Don't forget to delete others directories associated to this project if you're not going to use it again :) !\e[0m"
