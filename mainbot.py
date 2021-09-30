from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters
from src import gpayu, fbdown, igdown, ytdl, twdl, ymp3, rmbg
from bs4 import BeautifulSoup as Bs
import requests,re,sys,random,time,subprocess,json,ast,os

disable=[]
limit_rmbg=[]

def start(update,context):
    cek = update.message.from_user
    print("bot started from:",cek,"\n")
    msid=update.message.message_id
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hallo gans, perkenalkan saya linuxer^-^",reply_to_message_id=msid)

def helpme(update,context):
    cek = update.message.from_user
    cid = update.effective_chat.id
    msid=update.message.message_id
    helptxt="""
### Haii gan berikut ini adalah beberapa command yang bisa gua jalankan >//< ###

=============================
/mydog  -  Menampilkan gambar anjing imute
/mycat  -  Menampilkan gambar kucing imute
/myava  -  Menampilkan gambar avatar gaje tapi imute
/walhp  -  Menampilkan random wallpaper hp kece
/picstem - Menampilkan foto profile steam kece
/fbvid  -  Mendownload video dari fb
/igvid  -  Mendownload video dari ig
/twvid  -  Mendownload video dari twitter
/ytmp4  -  Mendownload video dari youtube
/ytmp3  -  Mendownload audio dari youtube
/sms    -  Mengirim sms gratis
=============================
"""
    context.bot.send_message(chat_id=cid,reply_to_message_id=msid,text=helptxt,parse_mode="Markdown")
    if cek.username == "alumni_corona" and update.message.chat.type == "private":
        context.bot.send_message(chat_id=cid, text="'!(command)' untuk mengakses command line \n'!on (command)' untuk enable command \n'!off (command)' untuk disable command \n'!up (filename)' untuk upload local file \n'!show-disable' untuk print command yg di disable \n'!debug' untuk menampilkan result json default \n'!rdebug' untuk menampilkan result json readable \n'!del (reply_to_message)' untuk menghapus pesan \n'!get (reply_to_message)' untuk mendownload file ke local storage bot \nPerintah\" ini khusus buat @alumni_corona aja ya gan hehe")

def newmem(update,context):
    new_members = update.message.new_chat_members
    cid=update.effective_chat.id
    msid=update.message.message_id
    ngrp=update.effective_chat.title
    for member in new_members:
        print(f"new member at grup [{ngrp}] : {member}\n")
        if not member.username:
            context.bot.send_message(chat_id=cid, text=f'Hai hallo agan {member.first_name} selamat datang di grup {ngrp} \nSemoga betah yah >//<', reply_to_message_id=msid)
        else:
            context.bot.send_message(chat_id=cid, text=f'Hai hallo agan {member.first_name} ( @{member.username} ) selamat datang di grup {ngrp} \nSemoga betah yah >//<', reply_to_message_id=msid)

def lefmem(update,context):
    lmember = update.message.left_chat_member
    cid=update.effective_chat.id
    msid=update.message.message_id
    ngrp=update.effective_chat.title
    if not lmember.first_name:
        pass
    elif not lmember.username:
        context.bot.send_message(chat_id=cid, text=f'Agan <i>{lmember.first_name}</i> meninggalkan grup {ngrp} :( \nGoodbye gan :\'(', reply_to_message_id=msid, parse_mode='html')
    else:
        context.bot.send_message(chat_id=cid, text=f'Agan <i>{lmember.first_name}</i> ( @{lmember.username} ) meninggalkan grup {ngrp} \nGoodbye gan :\'(', reply_to_message_id=msid, parse_mode='html')
    print(f"member left at grup [{ngrp}] : {lmember}\n")

def unknown(update,context):
    cek = update.message.from_user
    cekg=update.message.chat
    msid=update.message.message_id
    cid=update.effective_chat.id
    pesan=update.message.text

    for i in disable:
        if i in pesan.split()[0].lower():
            print(f"[{pesan.split()[0]}] Status: DISABLE!")
            context.bot.sendMessage(chat_id=cid, text="This command is disabled!", reply_to_message_id=msid)
            time.sleep(1)
            context.bot.delete_message(chat_id=cid,message_id=msid + 1)
            return True

    #Special command
    if pesan.split()[0] == "!off" and cek.username == "alumni_corona":
        if len(pesan.split()[1]) == 1 and pesan[0] == "!":
            context.bot.sendMessage(chat_id=cid, text="!Warn! Maaf kang lu gak bisa disable root command:(", reply_to_message_id=msid)
            return True
        elif pesan.split()[1].lower() in disable:
            context.bot.sendMessage(chat_id=cid, text="Already disabled!", reply_to_message_id=msid)
            return True
        disable.append(pesan.split()[1])
        disable.append(pesan.split()[1]+"@nubii_bot")
        context.bot.sendMessage(chat_id=cid, text=f"Disable <code>{pesan.split()[1]}</code>", reply_to_message_id=msid, parse_mode="html")
    elif pesan.split()[0] == "!on" and cek.username == "alumni_corona":
        disable.remove(pesan.split()[1])
        disable.remove(pesan.split()[1]+"@nubii_bot")
        context.bot.sendMessage(chat_id=cid, text=f"Enable <code>{pesan.split()[1]}</code>", reply_to_message_id=msid, parse_mode="html")
    elif pesan.split()[0] == "!del" and cek.username == "alumni_corona":
        dell=update.message
        mssi=dell['reply_to_message']['message_id']
        time.sleep(1)
        context.bot.delete_message(chat_id=cid,message_id=mssi)
    elif pesan.split()[0] == "!rdebug" and cek.username == "alumni_corona":
        msu=update.message
        parsed=ast.literal_eval(str(msu))
        reable=json.dumps(parsed, indent=3, sort_keys=True)
        context.bot.sendMessage(chat_id=cid, text=f"<pre>{reable}</pre>", reply_to_message_id=msid, parse_mode="html")
    elif pesan.split()[0] == "!debug" and cek.username == "alumni_corona":
        context.bot.sendMessage(chat_id=cid, text=f"<pre>{update.message}</pre>", reply_to_message_id=msid, parse_mode="html")

    if pesan.split()[0] == "!up" and cek.username == "alumni_corona":
        context.bot.send_message(chat_id=cid, text=f"Uploading {pesan.split()[1]}", reply_to_message_id=msid)
        context.bot.send_document(chat_id=cid, document=open(pesan.split()[1],'rb'))
        return True
    elif pesan.split()[0] == "!get" and cek.username == "alumni_corona":
        rmsg=update.message.reply_to_message
        if not rmsg:
            context.bot.send_message(chat_id=cid, text="<b>Usage:</b> <code>!get(reply_to_message)</code>",reply_to_message_id=msid,parse_mode="html")
        else:
            context.bot.send_message(chat_id=cid, text="Downloading file into local storage", reply_to_message_id=msid)

        if "'document'" in str(rmsg):
            fid=rmsg['document']['file_id']
            fnm=rmsg['document']['file_name']
            url=context.bot.get_file(file_id=fid)['file_path']
            try:
                with open(fnm,'w') as dl:
                    req=requests.get(url)
                    dl.write(req.content)
            except:
                with open(fnm,'wb') as dl:
                    req=requests.get(url)
                    dl.write(req.content)
        elif "'video'" in str(rmsg):
            fid=rmsg['video']['file_id']
            fnm=random.randrange(9999)
            url=context.bot.get_file(file_id=fid)['file_path']
            with open(f'{fnm}.mp4','wb') as dl:
                req=requests.get(url)
                dl.write(req.content)
        elif "'photo'" in str(rmsg):
            fnm=random.randrange(9999)
            for i in rmsg['photo']:
                idd=i['file_id']
            url=context.bot.get_file(file_id=idd)['file_path']
            with open(f'{fnm}.png','wb') as dl:
                req=requests.get(url)
                dl.write(req.content)

        context.bot.send_message(chat_id=cid, text="OK, Done ^_^", reply_to_message_id=msid)
        return True
    elif pesan[0] == "!" and cek.username == "alumni_corona":
        if "!show-disable" in pesan:
            context.bot.sendMessage(chat_id=cid, text="command yg di disable:\n"+"\n".join(disable), reply_to_message_id=msid)
        doit=subprocess.check_output(pesan.replace('!',''), stderr=subprocess.STDOUT, shell=True, encoding="utf-8")
        context.bot.send_message(chat_id=cid, text=doit[:4096], reply_to_message_id=msid)
        return True

    if cekg['type'] != 'private':
        print(f'message from grup [{cekg["title"]}]: "{pesan}" \ndetail user: {cek}\n')
        return True

    print(f'message from user: "{pesan}" \ndetail user:{cek}\n')
    context.bot.send_message(chat_id=cid, text="Maap, gua kagak ngarti gan:( \nKetik /help untuk melihat command yang bisa gue execute gan hehe",reply_to_message_id=msid)
    print()

def remove_bg(update, context):
    cid=update.effective_chat.id
    idu=update.message.from_user
    msid=update.message.message_id
    pesan=update.message.text
    rmsg=update.message.reply_to_message

    if idu.username == "alumni_corona":
            pass
    else:
        for i in disable:
            if i in pesan.split()[0].lower():
                print(f"[{pesan.split()[0]}] Status: DISABLE!")
                context.bot.sendMessage(chat_id=cid, text="This command is disabled!", reply_to_message_id=msid)
                time.sleep(1)
                context.bot.delete_message(chat_id=cid,message_id=msid + 1)
                return True

    c=0
    for x in limit_rmbg:
        if x == idu['id']:
            c+=1
    if c >= 5:
        context.bot.sendMessage(chat_id=cid, text="Oops, anda telah mencapai limit penggunaan. Mohon coba lagi besok :)", reply_to_message_id=msid)
        print(f"limit tercapai: {idu}")
        return True

    if len(pesan.split()) <= 1 and rmsg == None:
        context.bot.sendMessage(chat_id=cid, text="Usage:\n`(reply_to_message)/rmbg (bg-color, 'ex: red', 'default: transparant')` \nOR\n `/rmbg (url image) (bg-color, 'ex: red', 'default: transparant')`", reply_to_message_id=msid, parse_mode='MarkDown')
        return True

    teksna=pesan.split()
    crop=rmbg.Croper('A4NALxKfnKqXNrrgdXjhQ8jQ')
    if 'http://' in pesan or 'https://' in pesan:
        if len(teksna) > 2 and 'bg-color' in teksna[2]:
            dlg=crop.cropbgurl(teksna[1], bg_color=teksna[3])
        else:
            dlg=crop.cropbgurl(teksna[1], bg_color=None)
    elif rmsg != None:
        for i in rmsg['photo']:
            idd=i['file_id']
        url=context.bot.get_file(file_id=idd)['file_path']
        with open('gambarna.jpg','wb') as dl:
            req=requests.get(url)
            dl.write(req.content)
        if len(teksna) > 1 and 'bg-color' in teksna[1]:
            dlg=crop.cropbg('gambarna.jpg', bg_color=teksna[2])
        else:
            dlg=crop.cropbg('gambarna.jpg', bg_color=None)

    if 'Error: ' in str(dlg):
        context.bot.sendMessage(chat_id=cid, text=f"{dlg}", reply_to_message_id=msid)
        return True

    if len(teksna) > 1 and 'bg-color' in teksna[1]:
        context.bot.send_photo(chat_id=cid, photo=open('hasil-rmbg.png','rb'))
    elif len(teksna) > 2 and 'bg-color' in teksna[2]:
        context.bot.send_photo(chat_id=cid, photo=open('hasil-rmbg.png','rb'))
    else:
        context.bot.send_document(chat_id=cid, document=open('hasil-rmbg.png','rb'))

    limit_rmbg.append(idu['id'])
    print(f"id pengguna remove_bg: {limit_rmbg}")
    time.sleep(5)

def dog(update,context):
    cek = update.message.from_user
    cid = update.effective_chat.id
    msid=update.message.message_id
    pesan=update.message.text

    if cek.username == "alumni_corona":
            pass
    else:
        for i in disable:
            if i in pesan.split()[0].lower():
                print(f"[{pesan.split()[0]}] Status: DISABLE!")
                context.bot.sendMessage(chat_id=cid, text="This command is disabled!", reply_to_message_id=msid)
                time.sleep(1)
                context.bot.delete_message(chat_id=cid,message_id=msid + 1)
                return True

    print("[GAMBAR ANJING]",cek)
    url = requests.get('https://random.dog/woof.json').json()['url']

    context.bot.send_message(chat_id=cid, text="Ini dia si anjing imute >.<",reply_to_message_id=msid)
    if '.mp4' in url or '.gif' in url:
        context.bot.send_document(chat_id=cid, document=url)
    else:
        context.bot.send_photo(chat_id=cid, photo=url)

    if update.message['chat']['type'] == 'private':
        print(update.message['chat']['username']+" : "+update.message['text'])
    else:
        print(update.message['chat']['title']+" (grup) : "+update.message['text'])
    print("dog img :",url,"\n")

def cat(update,context):
    cek = update.message.from_user
    cid = update.effective_chat.id
    msid=update.message.message_id
    pesan=update.message.text

    if cek.username == "alumni_corona":
            pass
    else:
        for i in disable:
            if i in pesan.split()[0].lower():
                print(f"[{pesan.split()[0]}] Status: DISABLE!")
                context.bot.sendMessage(chat_id=cid, text="This command is disabled!", reply_to_message_id=msid)
                time.sleep(1)
                context.bot.delete_message(chat_id=cid,message_id=msid + 1)
                return True

    print("[GAMBAR KUCING]",cek)
    url = requests.get('https://api.thecatapi.com/v1/images/search').json()[0]['url']

    context.bot.send_message(chat_id=cid, text="Ini dia si kucing imute >.<",reply_to_message_id=msid)
    if '.mp4' in url or '.gif' in url:
        context.bot.send_document(chat_id=cid, document=url)
    else:
        context.bot.send_photo(chat_id=cid, photo=url)

    if update.message['chat']['type'] == 'private':
        print(update.message['chat']['username']+" : "+update.message['text'])
    else:
        print(update.message['chat']['title']+" (grup) : "+update.message['text'])
    print("cat img :",url,"\n")

def smsgra(update,context):
    cek = update.message.from_user
    cid=update.effective_chat.id
    msid=update.message.message_id
    pesan=update.message.text

    if cek.username == "alumni_corona":
            pass
    else:
        for i in disable:
            if i in pesan.split()[0].lower():
                print(f"[{pesan.split()[0]}] Status: DISABLE!")
                context.bot.sendMessage(chat_id=cid, text="This command is disabled!", reply_to_message_id=msid)
                time.sleep(1)
                context.bot.delete_message(chat_id=cid,message_id=msid + 1)
                return True
    if len(pesan.split()) <= 2:
        context.bot.send_message(chat_id=cid, text="<b>Usage:</b> <code>/sms (no) (pesan)</code>",reply_to_message_id=msid,parse_mode="html")
        return True

    no=pesan.split()[1]
    ms=pesan.split()[2:]
    msg=str(' '.join(ms)).replace('\\n','\n')
    
    print("[SMS GRATIS]",cek)
    context.bot.send_message(chat_id=cid, text="Sedang mengirim pesan ke "+no+" sabar ya gan hehe",reply_to_message_id=msid)
    hasil=gpayu.Gratis(no,msg)
    if 'SMS Gratis Telah Dikirim' in hasil:
        pon="Berhasil mengirim sms ke "+no
        stat="Berhasil"
    elif 'Mohon Tunggu' in hasil:
        pon="Mohon tunggu beberapa saat untuk mengirim sms yang sama"
        stat="Gagal"
    else:
        pon="<b>Unknow error try again! \nusage:</b> <code>/sms (no) (pesan)</code>"
        stat="Unknow"

    context.bot.send_message(chat_id=cid, text=pon,reply_to_message_id=msid,parse_mode="html")
    if update.message['chat']['type'] == 'private':
        print(update.message['chat']['username']+" : "+update.message['text'])
    else:
        print(update.message['chat']['title']+" (grup) : "+update.message['text'])
    print("status : "+stat+"\n")

def ranav(update,context):
    cek = update.message.from_user
    cid=update.effective_chat.id
    msid=update.message.message_id
    pesan=update.message.text

    if cek.username == "alumni_corona":
            pass
    else:
        for i in disable:
            if i in pesan.split()[0].lower():
                print(f"[{pesan.split()[0]}] Status: DISABLE!")
                context.bot.sendMessage(chat_id=cid, text="This command is disabled!", reply_to_message_id=msid)
                time.sleep(1)
                context.bot.delete_message(chat_id=cid,message_id=msid + 1)
                return True

    nran=random.randrange(9999)
    url="https://api.adorable.io/avatars/"+str(nran)+".png"
    context.bot.send_message(chat_id=cid, reply_to_message_id=msid, text="Nih gan avatar adorable lo XD")
    context.bot.send_photo(chat_id=cid, photo=url)

    print(f"[ADORABLE] {cek}")
    if update.message['chat']['type'] == 'private':
        print(update.message['chat']['username']+" : "+update.message['text'])
    else:
        print(update.message['chat']['title']+" (grup) : "+update.message['text'])
    print(f"avatar img : {url}\n")

def fbdl(update,context):
    cek = update.message.from_user
    cid=update.effective_chat.id
    msid=update.message.message_id
    pesan=update.message.text

    if cek.username == "alumni_corona":
            pass
    else:
        for i in disable:
            if i in pesan.split()[0].lower():
                print(f"[{pesan.split()[0]}] Status: DISABLE!")
                context.bot.sendMessage(chat_id=cid, text="This command is disabled!", reply_to_message_id=msid)
                time.sleep(1)
                context.bot.delete_message(chat_id=cid,message_id=msid + 1)
                return True
    if len(pesan.split()) <= 1 or len(pesan.split()) >= 3:
        context.bot.send_message(chat_id=cid, text="<b>Usage:</b> <code>/fbvid (link)</code>",reply_to_message_id=msid,parse_mode="html")
        return True

    print("[FB-DL]",cek)
    lina=pesan.split()[1]
    context.bot.send_message(chat_id=cid,reply_to_message_id=msid,text="Sebentar ya gan lagi gue cariin video fbnya ^.^")
    don=fbdown.Fbdl(lina)
    url=don.split('.{"')[0]
    context.bot.sendVideo(chat_id=cid,video=url)

    if update.message['chat']['type'] == 'private':
        print(update.message['chat']['username']+" : "+update.message['text'])
    else:
        print(update.message['chat']['title']+" (grup) : "+update.message['text'])
    print("fb video :",url,"\n")

def igdl(update,context):
    cek = update.message.from_user
    cid=update.effective_chat.id
    msid=update.message.message_id
    pesan=update.message.text

    if cek.username == "alumni_corona":
            pass
    else:
        for i in disable:
            if i in pesan.split()[0].lower():
                print(f"[{pesan.split()[0]}] Status: DISABLE!")
                context.bot.sendMessage(chat_id=cid, text="This command is disabled!", reply_to_message_id=msid)
                time.sleep(1)
                context.bot.delete_message(chat_id=cid,message_id=msid + 1)
                return True
    if len(pesan.split()) <= 1 or len(pesan.split()) >= 3:
        context.bot.sendMessage(chat_id=cid, text="<b>Usage:</b> <code>/igvid (link)</code>",reply_to_message_id=msid,parse_mode="html")
        return True

    print("[IG-DL]",cek)
    lina=pesan.split()[1]
    context.bot.send_message(chat_id=cid,reply_to_message_id=msid,text="Sebentar ya gan lagi gue cariin video ignya ^.^")
    don=igdown.Igdl(lina)
    url=don.response()
    context.bot.sendVideo(chat_id=cid,video=url)

    if update.message['chat']['type'] == 'private':
        print(update.message['chat']['username']+" : "+update.message['text'])
    else:
        print(update.message['chat']['title']+" (grup) : "+update.message['text'])
    print("ig video :",url,"\n")

def twvd(update,context):
    cek = update.message.from_user
    cid=update.effective_chat.id
    msid=update.message.message_id
    pesan=update.message.text

    if cek.username == "alumni_corona":
            pass
    else:
        for i in disable:
            if i in pesan.split()[0].lower():
                print(f"[{pesan.split()[0]}] Status: DISABLE!")
                context.bot.sendMessage(chat_id=cid, text="This command is disabled!", reply_to_message_id=msid)
                time.sleep(1)
                context.bot.delete_message(chat_id=cid,message_id=msid + 1)
                return True
    if len(pesan.split()) <= 1 or len(pesan.split()) >= 3:
        context.bot.sendMessage(chat_id=cid, text="<b>Usage:</b> <code>/twvid (link)</code>",reply_to_message_id=msid,parse_mode="html")
        return True

    print("[TWIT-DL]",cek)
    lina=pesan.split()[1]
    context.bot.send_message(chat_id=cid,reply_to_message_id=msid,text="Sebentar ya gan lagi gue cariin video twitternya ^.^")
    don=twdl.twDown(lina)
    url=don.response()
    context.bot.sendVideo(chat_id=cid,video=url)

    if update.message['chat']['type'] == 'private':
        print(update.message['chat']['username']+" : "+update.message['text'])
    else:
        print(update.message['chat']['title']+" (grup) : "+update.message['text'])
    print("twiter video :",url,"\n")

def ytvd(update,context):
    cek = update.message.from_user
    cid=update.effective_chat.id
    msid=update.message.message_id
    pesan=update.message.text

    if cek.username == "alumni_corona":
            pass
    else:
        for i in disable:
            if i in pesan.split()[0].lower():
                print(f"[{pesan.split()[0]}] Status: DISABLE!")
                context.bot.sendMessage(chat_id=cid, text="This command is disabled!", reply_to_message_id=msid)
                time.sleep(1)
                context.bot.delete_message(chat_id=cid,message_id=msid + 1)
                return True
    if len(pesan.split()) <= 1 or len(pesan.split()) >= 3:
        context.bot.sendMessage(chat_id=cid, text="<b>Usage:</b> <code>/ytmp4 (link)</code>",reply_to_message_id=msid,parse_mode="html")
        return True

    print("[YT-DL]",cek)
    lina=pesan.split()[1]
    context.bot.send_message(chat_id=cid,reply_to_message_id=msid,text="Sebentar ya gan lagi gue cariin video ytnya ^.^")
    don=ytdl.Ytdl(lina)
    url=don.response()
    try:
        context.bot.sendDocument(chat_id=cid, reply_to_message_id=msid, document=url, caption="Nah jumpa nih gan videonya silahkan didownload ^.^")
    except:
        context.bot.sendMessage(chat_id=cid, reply_to_message_id=msid, text=f"Oops sepertinya ada masalah pas mau gue upload videonya gan:( download [Disini]({url}) ae yak", parse_mode="MarkDown")

    if update.message['chat']['type'] == 'private':
        print(update.message['chat']['username']+" : "+update.message['text'])
    else:
        print(update.message['chat']['title']+" (grup) : "+update.message['text'])
    print("yutub video :",url,"\n")

def ytmp3(update,context):
    cek = update.message.from_user
    cid=update.effective_chat.id
    msid=update.message.message_id
    pesan=update.message.text

    if cek.username == "alumni_corona":
            pass
    else:
        for i in disable:
            if i in pesan.split()[0].lower():
                print(f"[{pesan.split()[0]}] Status: DISABLE!")
                context.bot.sendMessage(chat_id=cid, text="This command is disabled!", reply_to_message_id=msid)
                time.sleep(1)
                context.bot.delete_message(chat_id=cid,message_id=msid + 1)
                return True
    if len(pesan.split()) <= 1 or len(pesan.split()) >= 3:
        context.bot.sendMessage(chat_id=cid, text="<b>Usage:</b> <code>/ytmp3 (link)</code>",reply_to_message_id=msid,parse_mode="html")
        return True

    print("[YTMP3-DL]",cek)
    lina=pesan.split()[1]
    context.bot.send_message(chat_id=cid,reply_to_message_id=msid,text="Sebentar ya gan lagi gue cariin MP3nya ^.^")
    url=ymp3.Ymp3(lina)
    if url:
        context.bot.sendMessage(chat_id=cid, text=f"Nih gan jumpa MP3nya silahkan di [Download]({url}) gan ^.^", reply_to_message_id=msid, parse_mode="MarkDown")
    else:
        context.bot.sendMessage(chat_id=cid, text="Oops gue gak nemu MP3nya gan. maap:(", reply_to_message_id=msid)

    if update.message['chat']['type'] == 'private':
        print(update.message['chat']['username']+" : "+update.message['text'])
    else:
        print(update.message['chat']['title']+" (grup) : "+update.message['text'])
    print("yutub audio :",url,"\n")

def walp(update,context):
    cek = update.message.from_user
    cid=update.effective_chat.id
    msid=update.message.message_id
    pesan=update.message.text

    if cek.username == "alumni_corona":
            pass
    else:
        for i in disable:
            if i in pesan.split()[0].lower():
                print(f"[{pesan.split()[0]}] Status: DISABLE!")
                context.bot.sendMessage(chat_id=cid, text="This command is disabled!", reply_to_message_id=msid)
                time.sleep(1)
                context.bot.delete_message(chat_id=cid,message_id=msid + 1)
                return True

    nran=random.randrange(1080)
    url=f"https://picsum.photos/id/{nran}/720/1280"
    context.bot.send_message(chat_id=cid, reply_to_message_id=msid, text="Nih gan wallpaper hp kece yang cocok buat lo hehe")
    context.bot.send_photo(chat_id=cid, photo=url)

    print(f"[WALP - HP] {cek}")
    if update.message['chat']['type'] == 'private':
        print(update.message['chat']['username']+" : "+update.message['text'])
    else:
        print(update.message['chat']['title']+" (grup) : "+update.message['text'])
    print(f"walp img : {url}\n")

def steampic(update,context):
    lst = []
    cek = update.message.from_user
    cid=update.effective_chat.id
    msid=update.message.message_id
    pesan=update.message.text
    nran=random.randrange(1,100)

    if cek.username == "alumni_corona":
            pass
    else:
        for i in disable:
            if i in pesan.split()[0].lower():
                print(f"[{pesan.split()[0]}] Status: DISABLE!")
                context.bot.sendMessage(chat_id=cid, text="This command is disabled!", reply_to_message_id=msid)
                time.sleep(1)
                context.bot.delete_message(chat_id=cid,message_id=msid + 1)
                return True

    req=requests.get("http://randomavatar.com/")
    bs1=Bs(req.text,'html.parser')
    for i in bs1.find_all('img',{'class':'img-responsive MainSpace RAFade'}):
        lst.append(i['src'])

    url=lst[nran]
    context.bot.send_message(chat_id=cid, reply_to_message_id=msid, text="Nih gan random foto profile steam buat lo hehe")
    context.bot.send_photo(chat_id=cid, photo=url)

    print(f"[WALP - STEAM] {cek}")
    if update.message['chat']['type'] == 'private':
        print(update.message['chat']['username']+" : "+update.message['text'])
    else:
        print(update.message['chat']['title']+" (grup) : "+update.message['text'])
    print(f"steam img : {url}\n")

def main():
    updaterr = Updater(('2028064853:AAFR_mJyClcfc7JOc3WHq4O5adi9_zDLKfs'),use_context=True)
    dp = updaterr.dispatcher
    dp.add_handler(CommandHandler('help',helpme))
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('mycat',cat))
    dp.add_handler(CommandHandler('mydog',dog))
    dp.add_handler(CommandHandler('myava',ranav))
    dp.add_handler(CommandHandler('walhp',walp))
    dp.add_handler(CommandHandler('picstem',steampic))
    dp.add_handler(CommandHandler('fbvid',fbdl))
    dp.add_handler(CommandHandler('igvid',igdl))
    dp.add_handler(CommandHandler('twvid',twvd))
    dp.add_handler(CommandHandler('ytmp4',ytvd))
    dp.add_handler(CommandHandler('ytmp3',ytmp3))
    dp.add_handler(CommandHandler('rmbg',remove_bg))
    dp.add_handler(CommandHandler('sms',smsgra))
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, newmem))
    dp.add_handler(MessageHandler(Filters.status_update, lefmem))
    dp.add_handler(MessageHandler(Filters.all, unknown))
    updaterr.start_polling()
    print(f"\n[ BOT SERVER STARTED AT {time.ctime()} ]\n")
    updaterr.idle()
try:
    main()
except Exception as Err:
    print(f"[SysErr] {Err}")
