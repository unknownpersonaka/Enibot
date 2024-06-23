#!/usr/bin/python
import libperso.lib_bot as bot
import sys
import multiprocessing

def main()->None:
    if len(sys.argv)>1:
        if sys.argv[1]=="info":
            t2=multiprocessing.Process(target=bot.search_book_infos_ENI,args=[sys.argv[3]])
            t2.start()
            t2.join()
        elif sys.argv[1]=="download":
            t3=multiprocessing.Process(target=bot.downld_book,args=[])
            t3.start()
            t3.join()
        else:
            print(bot.color.yellow)
            print("[LOG]: error case")
            raise Exception()
    return

def main_script()->None:
    try:
        if sys.argv[1]=="download":
            bot.create_json({sys.argv[2]:sys.argv[3]},f"{bot.current_user}/Desktop/eni_bot/repos/book/book_list_download.json")
        print(bot.color.bold+bot.color.green+"[LOG]:","load book info")
        print(bot.color.norm+bot.color.bold+"[LOG]: Start of program")
        main()
    except(KeyboardInterrupt) as err11_:
        print(err11_)
    finally:
        print(bot.color.bold+bot.color.warning+"[LOG]: end of program")
    return 

if __name__=='__main__':
    try:
        if sys.argv[1]=="help":
            with open(f"{bot.current_user}/Desktop/eni_bot/repos/project_script/cli/cmd") as textIn:
                txt_:str=textIn.read().strip()
                print(bot.color.bold+bot.color.green)
                print(txt_)
        elif sys.argv[1]=="config":
            dc=bot.load_data_books(f"{bot.current_user}/Desktop/eni_bot/repos/config/config.json")
            dc["email"]=sys.argv[2]
            dc["password"]=sys.argv[3]
            dc["portail"]=sys.argv[4]
            bot.create_json(dc,f"{bot.current_user}/Desktop/eni_bot/repos/config/config.json")
        else:
            if len(bot.load_data_books(f"{bot.current_user}/Desktop/eni_bot/repos/config/config.json"))==3:
                main_script()
            else:
                print(bot.color.warning)
                print("[LOG]: Please enter your email, password and portail before running script")
                raise Exception()
    except Exception as err14_5:
        print(bot.color.bold+bot.color.warning)
        print(err14_5)
