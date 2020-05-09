from tkinter import *
from PIL import ImageTk, Image
import pyttsx3
import datetime, time
import speech_recognition as sr
import wikipedia
import webbrowser
import pygame
import pyaudio
import subprocess
import os
import sys
import random
import smtplib
import wolframalpha
import socket
import wmi
import ctypes
import pyautogui
import psutil
import glob
import socket
import psutil
from selenium import webdriver
import win32clipboard
import playsound
from gtts import gTTS
import psutil
import logging




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# print(voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate)
client = wolframalpha.Client('XXJPKQ-KJQQY8K6HA')

b_music = ['Jarvis']
pygame.mixer.init()
pygame.mixer.music.load( random.choice(b_music) + '.mp3')
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)

static_remind_speech = 'alright, i will remind '
remind_speech = ''

def speak(audio):
    print('JARVIS: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def wifi():
    REMOTE_SERVER = "www.google.com"
    def is_connected():
        try:
            host = socket.gethostbyname(REMOTE_SERVER)
            s = socket.create_connection((host, 80), 2)
            return True
        except:
            pass
        return False

def brightness(query):
    if 'decrease ' in query:
        print('ok Sir.......')
        dec = wmi.WMI(namespace='wmi')
        methods = dec.WmiMonitorBrightnessMethods()[0]
        methods.WmiSetBrightness(30, 0)
    elif 'increase ' in query:
        print('ok Sir.......')
        ins = wmi.WMI(namespace='wmi')
        methods = ins.WmiMonitorBrightnessMethods()[0]
        methods.WmiSetBrightness(100, 0)

def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%02d hour, %02d minute, %02s seconds" % (hh, mm, ss)

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Your Email-ID@gmail.com', 'Your-PASSWORD')
    server.sendmail('Your Email-ID@gmail.com', to, content)
    server.close()


# def gspeak():
#     # the read mode thing.
#     rcmd = takeCommand().lower()
#     keyboard = Controller()
#     if 'start' in rcmd or 'reading' in rcmd or 'start reading' in rcmd or 'read' in rcmd:
#         # copying selected text
#         keyboard.press(Key.ctrl)
#         keyboard.press('c')
#         time.sleep(1)
#         keyboard.release(Key.ctrl)
#         keyboard.release('c')
#         win32clipboard.OpenClipboard()
#         # reading copied data
#         rdata = win32clipboard.GetClipboardData()
#         win32clipboard.CloseClipboard()
#         ddata = TextBlob(rdata)
#         # detecting the language of selected text.
#         dlang = ddata.detect_language()
#         if dlang=='en':
#             playsound('istart.mp3')
#             speak(rdata)
#             playsound('istop.mp3')
#         else:
#             # pyttsx3 can't read some languages. so, here we use gTTs to read the detected language.
#             speak("Sorry sir! I don't know the language you are selected! But, my friend friday can read it for you!")
#             r1 = random.randint(1, 10000000)
#             r2 = random.randint(1, 10000000)
#             audout = str(r2) + "audio" + str(r1) + ".mp3"
#             gtspeak = gTTS(text=rdata, lang=dlang, slow=False)
#             gtspeak.save(audout)
#             playsound('istart.mp3')
#             playsound(audout)
#             playsound('istop.mp3')
#             os.chmod(audout, 0o777)
#             os.remove(audout)
#     else:
#         # repeating if there is an error.
#         speak("I didn't get that! say once more!" )
#         gspeak()
#
#
#
# def fb():
#         speak('opening facebook!')
#         driver = webdriver.Chrome('chromedriver.exe')
#         driver.get('https://www.facebook.com')
#
#         email_input = driver.find_element_by_id('email')
#         email_input.send_keys(FBEMAIL)
#
#         psd_input = driver.find_element_by_id('pass')
#         psd_input.send_keys(FBPASSWORD)
#
#         # while loop causing bug here. now it's better.
#
#         try:
#             login_btn = driver.find_element_by_id(f'u_0_1')
#             time.sleep(1)
#             login_btn.click()
#             speak('Logged in to facebook!')
#
#         except Exception as e:
#             try:
#                 login_btn = driver.find_element_by_id(f'u_0_2')
#                 time.sleep(1)
#                 login_btn.click()
#                 speak('Logged in to facebook!')
#
#             except Exception as e:
#                 try:
#                     login_btn = driver.find_element_by_id(f'u_0_3')
#                     time.sleep(1)
#                     login_btn.click()
#                     speak('Logged in to facebook!')
#
#                 except Exception as e:
#                     try:
#                         login_btn = driver.find_element_by_id(f'u_0_4')
#                         time.sleep(1)
#                         login_btn.click()
#                         speak('Logged in to facebook!')
#
#                     except Exception as e:
#                         try:
#                             login_btn = driver.find_element_by_id(f'u_0_5')
#                             time.sleep(1)
#                             login_btn.click()
#                             speak('Logged in to facebook!')
#
#                         except Exception as e:
#                             try:
#                                 login_btn = driver.find_element_by_id(f'u_0_6')
#                                 time.sleep(1)
#                                 login_btn.click()
#                                 speak('Logged in to facebook!')
#
#                             except Exception as e:
#                                 try:
#                                     login_btn = driver.find_element_by_id(f'u_0_7')
#                                     time.sleep(1)
#                                     login_btn.click()
#                                     speak('Logged in to facebook!')
#
#                                 except Exception as e:
#                                     try:
#                                         login_btn = driver.find_element_by_id(f'u_0_8')
#                                         time.sleep(1)
#                                         login_btn.click()
#                                         speak('Logged in to facebook!')
#
#                                     except Exception as e:
#                                         try:
#                                             login_btn = driver.find_element_by_id(f'u_0_9')
#                                             time.sleep(1)
#                                             login_btn.click()
#                                             speak('Logged in to facebook!')
#
#                                         except Exception as e:
#                                             print(e)
#                                             speak('Sorry sir! an error occurred! unable to log in.')
#
#         time.sleep(2)
#         speak('Do you want to share a post?')
#
#         # again loop problem. multiple nested while loop causing bugs. Now, tried with this, same problem.
#         try:
#             pinput = takeCommand().lower()
#             if 'yes' in pinput:
#                 speak("ok! What should I post for you?")
#                 try:
#                     pcont = takeCommand().lower()
#                     speak("please confirm! Do you want to post this?")
#                     print(pcont)
#
#                     try:
#                         postconf = takeCommand().lower()
#                         if 'yes' in postconf or 's' in postconf:
#                             try:
#                                 status = driver.find_element_by_xpath("//textarea[@name='xhpc_message']")
#                                 status.send_keys(pcont);
#                                 postbutton = driver.find_element_by_css_selector(("button[class*='selected']"))
#                                 # postbutton = driver.find_element_by_xpath("//button[contains(.,'selected')]")
#                                 postbutton.click()
#                                 print("post done")
#                                 speak("Post created! Check your wall!")
#                                 loopout()
#
#                             except Exception as e:
#                                 print('error')
#                                 print(e)
#                                 speak("sorry sir! an error occurred. Post creation failed!")
#                                 loopout()
#                         elif 'no' in postconf:
#                             speak('ok sir!')
#                             loopout()
#                     except Exception as e:
#                         speak("Sorry! I didn't get that! Say once again!")
#                         return "None"
#                 except Exception as e:
#                     speak("I didn't hear that! say once again")
#                     return "None"
#
#             elif 'no' in pinput or 'n' in pinput:
#                 speak("ok sir!")
#                 loopout()
#         except Exception as e:
#             speak("Sorry! I didn't get that! Say once again!")
#             return "None"
#
#
# time.sleep(30)





def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 6 and hour < 12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon Sir")
    elif hour >= 16 and hour < 21:
        speak("Good Evening Sir")
    else:
        speak("Good Night Sir")

    speak('Starting system sir!')
    speak('Loading Dependencies!')
    speak("System is online!")
    speak("I am Jarvis. please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listing...")
        r.pouse_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        # print(e)
        print("none")
        speak("none")
        return "None"
    return query


#===========================================================================================================
class jarvis:
    def __init__(self):
        root = Tk()
        root.title('JARVIS')
        root.config(background='pink')
        root.geometry("1910x985+0+0")
        root.resizable(width=False, height=False)
        root.wm_iconbitmap('ICON.ico')
        t1 = Label(root, text="J.A.R.V.I.S.", relief=GROOVE, font="times 40 bold", bg="yellow", fg="red", bd=5)
        t1.pack(side=TOP, fill=X)

        text_frame = Frame(root, bg="crimson", bd=8, relief=RIDGE)
        text_frame.place(x=5, y=160, width=720, height=820)
        m_title = Label(text_frame, bg="crimson", fg="white", font="lusica 20 bold underline")
        m_title.place(x=150, y=15)

        img_frame = Frame(root, bg="crimson", bd=8, relief=RIDGE)
        img_frame.place(x=730, y=90, width=1180, height=885)

        image = Image.open("JARVIS.jpg")
        image = image.resize((990, 690), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)
        panel = Label(img_frame, image=img)
        panel.pack(fill="both", expand="yes")

        self.compText = StringVar()
        self.userText = StringVar()

        self.userText.set('Click \'Start Listening\' to Give commands')

        userFrame = LabelFrame(text_frame, text="USER", font=('Black ops one', 25, 'bold'))
        userFrame.pack(fill="both", expand="yes")

        left2 = Message(userFrame, textvariable=self.userText, bg='dodgerBlue', fg='white')
        left2.config(font=("Comic Sans MS", 15, 'bold'))
        left2.pack(fill='both', expand='yes')

        compFrame = LabelFrame(text_frame, text="JARVIS", font=('Black ops one', 25, 'bold'))
        compFrame.pack(fill="both", expand="yes")

        left1 = Message(compFrame, textvariable=self.compText, bg='crimson', fg='white')
        left1.config(font=("Comic Sans MS", 15, 'bold'))
        left1.pack(fill='both', expand='yes')

        image1 = Image.open("mic.png")
        image1 = image1.resize((160, 60), Image.ANTIALIAS)
        img1 = ImageTk.PhotoImage(image1)

        b1 = Button(root, image = img1, bd=10, bg="lightgreen", fg="black", font="times 25 bold", command=self.clicked)
        b1.place(x=25, y=80)
        b2 = Button(root, text="Close!", bd=10, bg="red", fg="black", font="times 25 bold",command=root.destroy)
        b2.place(x=355, y=60)

        # wishMe()
        self.compText.set('Hello, I am Jarvis. please tell me how may I help you')

        root.bind("<Return>", self.clicked)  # handle the enter key event of your keyboard
        root.mainloop()

    def clicked(self):
        print('Working')
        query = takeCommand()
        self.userText.set('Listening...')
        self.userText.set(query)
        query = query.lower()

        if 'wikipedia' in query:
            speak('okay')
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", " ")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia...")
            self.compText.set(result)
            speak(result)

        elif 'please remind' in query or 'remind it' in query:
            speak('what should i remind?')
            self.compText.set('ok.......')
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listing...")
                r.pouse_threshold = 1
                audio = r.listen(source)
                global remind_speech
                remind_speech = r.recognize_google(audio)
                speak(static_remind_speech + remind_speech)

        elif 'reminder' in query:
            self.compText.set('ok this is your reminder .......')
            if remind_speech is None:
                speak('you do not have any reminder for today')
            else:
                speak('you have one reminder' + remind_speech)

        elif 'hello' in query:
            speak('Hello Sir!')

        #SYSTEM CALL PROGRAMS-------------------------------------------------------------------------------
        #===================================================================================================
        elif 'open window' in query:
            os.system('explorer This PC {}'.format(query.replace('Open' ,'')))

        elif 'brightness' in query:
            brightness(query)

        elif 'sleep mode' in query:
            rand = ['good night, sir']
            speak(rand)
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')

        elif 'lock my' in query:
            speak('ok, sir')
            ctypes.windll.user32.LockWorkStation()

        elif 'sutdown window' in query:
            ch = takeCommand().lower()
            if 'yes' in ch:
                speak('System shutting down in, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1')
                os.system("shutdown /s /t 1")
            elif 'no' in ch:
                speak('System shut down, terminated!')
            else:
                speak("I didn't get that! say once more!")

        elif 'restart window' in query:
            ch = takeCommand().lower()
            if 'yes' in ch:
                speak('System restarting in, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1')
                os.system("shutdown /r /t 1")
            elif 'no' in ch:
                speak('System reboot, terminated!')
            else:
                speak("I didn't get that! say once more!")

        elif 'wi-fi' in query:
            REMOTE_SERVER = "www.google.com"
            wifi()
            rand = ['We are connected']
            speak(rand)

        elif 'power status' in query:
            battery = psutil.sensors_battery()
            plugged = battery.power_plugged
            percent = int(battery.percent)
            time_left = secs2hours(battery.secsleft)
            self.compText.set(percent)
            print(f"charge = {percent}, time left = {time_left}, Charger Plugged-in = {plugged}")
            if percent < 20 and plugged == False:
                speak(f'sir, Battery level is, {percent}  percent! System status: Critical! Time remaining: {time_left}. We are now running on backup power! Charger Plugged-in: {plugged}')
            if percent < 20 and plugged == True:
                speak(f"sir, Battery level is, {percent}  percent! System status: Critical! Time remaining: {time_left} but don't worry, sir charger is connected")
            elif percent > 20 and percent <= 59 and plugged == False:
                speak(f'sir, Battery level is, {percent}  percent! System status: Average! Time remaining: {time_left}. We are now running on backup power! Charger Plugged-in: {plugged}')
            elif percent > 20 and percent <= 59 and plugged == True:
                speak(f"sir, Battery level is, {percent}  percent! System status: Average! Time remaining: {time_left} but don't worry, sir charger is connected")
            elif percent > 59 and percent < 100 and plugged == False:
                speak(f'sir, Battery level is, {percent}  percent! System status: Good! Time remaining: {time_left}. We are now running on backup power! Charger Plugged-in: {plugged}')
            elif percent > 59 and percent < 100 and plugged == True:
                speak(f"sir, Battery level is, {percent}  percent! System status: Good! Time remaining: {time_left} but don't worry, sir charger is connected")
            else:
                speak(f'sir, no need to connect the charger because Battery is fully charged! Charger Plugged-in: {plugged}')



        elif 'screenshot' in query or 'screen shot' in query or 'snapshot' in query:
            speak('ok, sir let me take a snapshot ')
            speak('ok done')
            speak('check your desktop, i saved there')
            pic = pyautogui.screenshot()
            pic.save('C:\\Users\\Akash Singh\\Pictures\\Saved Pictures.png')

        # elif 'read' in query or 'read screen' in query or 'read it' in query:
        #     speak('Select the text to read, then say, Start reading!')
        #     gspeak()


        elif 'install' in query:
            quer = query
            stopwords = ['install']
            querywords = quer.split()
            resultwords = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            rand = [('installing ' + result)]
            speak(rand)
            os.system('python -m pip install ' + result)

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "Your Email-ID@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                self.compText.set(e)
                speak("Sorry my friend Akash. I am not able to sent this email")

        elif 'google maps' in query:
            quer = query
            stopwords = ['google', 'maps']
            querywords = quer.split()
            resultwords = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            Chrome = ("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe %s")
            webbrowser.get(Chrome).open("https://www.google.co.in/maps/@23.9740114,78.422961,7z?hl=en" + result + "/")
            rand = [result + 'on google maps']
            speak(rand)

        elif 'where is' in query:
            query = query.split(" ")
            location = query[2]
            speak("Please, hold on Sir, I will show you where " + location + "is. ")
            os.system('''chromium-browser  https://www.google.co.in/maps/@23.9740114,78.422961,7z?hl=en''' + location + "/&amp;")

        # elif 'open' in query:
        #     speak('okey')
        #     os.system('explorer C:\\{}'.format(query.replace('Open', '')))

        elif 'open google' in query:
            speak('okay')
            webbrowser.open("google.com")

        elif 'open youtube' in query:
            speak('okay')
            webbrowser.open("youtube.com")

        elif 'open g-mail' in query:
            speak('okay')
            webbrowser.open('www.g-mail.com')

        elif 'play music' in query:
            speak('okay')
            music_dir = "C:\\Users\\Akash Singh\\Music"
            songs = os.listdir(music_dir)
            self.compText.set(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        # elif 'stop music' in query:
        #     speak('okey')
        #     os.system("TASKKILL /F /IM AIMP3.exe")

        elif 'play video' in query:
            speak('okay')
            video_dir = "C:\\Users\\Akash Singh\\Videos"
            songs = os.listdir(video_dir)
            self.compText.set(songs)
            os.startfile(os.path.join(video_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H hour:%M minute:%S second")
            speak(f"Akash, the time is {strTime}")

        elif 'open code blocks' in query:
            speak('okay')
            codePath = "C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe"
            os.startfile(codePath)

        elif 'open chrome' in query:
            speak('okay')
            chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)

        elif '.com' in query:
            speak('okay')
            rand = ['Opening' + query]
            Chrome = ("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe %s")
            speak(rand)
            webbrowser.get(Chrome).open('http://www.' + query)
            self.compText.set('')

        elif query != 'start music' and 'start' in query:
            quer = query
            stopwords = ['start']
            querywords = quer.split()
            resultwords = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            os.system('start ' + result)
            rand = [('starting ' + result)]
            speak(rand)

        elif query != 'close music' and 'close' in query:
            quer = query
            stopwords = ['close']
            querywords = quer.split()
            resultwords = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            os.system('taskkill /im ' + result + '.exe /f')
            rand = [('closing ' + result)]
            speak(rand)

        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'your name' in query:
            rand = ['My name is Jarvis, at your service, sir']
            speak(rand)

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'goodbye' in query:
            Jarvis_Off = "Good Bye Akash! Jarvis off, 3, 2, 1, 0"
            speak(Jarvis_Off)
            sys.exit()

        elif 'thanks' in query or 'tanks' in query or 'thank you' in query:
            rand = ['You are welcome, sir', 'no problem']
            speak(rand)

        elif '*' in query:
            rand = ['Be polite please, sir']
            speak(rand)

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    self.compText.set('According to WOLFRAM-ALPHA ...')
                    self.compText.set('Got it.')
                    self.compText.set(results)
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)


                except:
                    results = wikipedia.summary(query, sentences=2)
                    self.compText.set('Got it.')
                    self.compText.set('According to Wikipedia... ')
                    self.compText.set(results)
                    speak('Got it.')
                    speak('According to Wikipedia... ')
                    speak(results)

            except:
                speak('I don\'t know Sir! Google is smarter than me!')
                self.compText.set('I don\'t know Sir! Google is smarter than me!')
                webbrowser.open('www.google.com')


if __name__ == '__main__':
    wishMe()
    obj = jarvis()

#===========================================================================================================
# if __name__ == "__main__":
#     wishMe()
#     while True:
#         # if 1:
#         query = takeCommand().lower()
#
#         if 'wikipedia' in query:
#             speak('okay')
#             speak("Searching Wikipedia...")
#             query = query.replace("wikipedia", " ")
#             result = wikipedia.summary(query, sentences=2)
#             speak("According to Wikipedia...")
#             print(result)
#             speak(result)
#
#         elif 'please remind' in query or 'remind it' in query:
#             speak('what should i remind?')
#             print('ok.....')
#             r = sr.Recognizer()
#             with sr.Microphone() as source:
#                 print("Listing...")
#                 r.pouse_threshold = 1
#                 audio = r.listen(source)
#                 global remind_speech
#                 remind_speech = r.recognize_google(audio)
#                 speak(static_remind_speech + remind_speech)
#
#         elif 'reminder' in query:
#             print('ok this is your reminder .......')
#             if remind_speech is None:
#                 speak('you do not have any reminder for today')
#             else:
#                 speak('you have one reminder' + remind_speech)
#
#         elif 'hello' in query:
#             speak('Hello Sir!')
#
#         elif 'wi-fi' in query:
#             REMOTE_SERVER = "www.google.com"
#             wifi()
#             rand = ['We are connected']
#             speak(rand)
#
#         elif 'the time' in query:
#             strTime = datetime.datetime.now().strftime("%H hour:%M minute:%S second")
#             speak(f"Akash, the time is {strTime}")
#
#         elif 'sleep mode' in query:
#             rand = ['good night, sir']
#             speak(rand)
#             os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
#
#         elif 'install' in query:
#             quer = query
#             stopwords = ['install']
#             querywords = quer.split()
#             resultwords = [word for word in querywords if word.lower() not in stopwords]
#             result = ' '.join(resultwords)
#             rand = [('installing ' + result)]
#             speak(rand)
#             os.system('python -m pip install ' + result)
#
#         elif 'open google' in query:
#             speak('okay')
#             webbrowser.open("google.com")
#
#         elif 'open youtube' in query:
#             speak('okay')
#             webbrowser.open("youtube.com")
#
#         elif 'open gmail' in query:
#             speak('okay')
#             webbrowser.open('www.gmail.com')
#
#         elif 'play music' in query:
#             speak('okay')
#             music_dir = "C:\\Users\\Akash Singh\\Videos"
#             songs = os.listdir(music_dir)
#             print(songs)
#             os.startfile(os.path.join(music_dir, songs[0]))
#
#         elif 'open code blocks' in query:
#             speak('okay')
#             codePath = "C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe"
#             os.startfile(codePath)
#
#         elif 'open chrome' in query:
#             speak('okay')
#             chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
#             os.startfile(chromePath)
#
#         elif '.com' in query:
#             speak('okay')
#             rand = ['Opening' + query]
#             Chrome = ("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe %s")
#             speak(rand)
#             webbrowser.get(Chrome).open('http://www.' + query)
#             print('')
#
#         elif 'open window' in query:
#             os.system('explorer This PC {}'.format(query.replace('Open' ,'')))
#
#         elif query != ('start music') and ('start') in query:
#             quer = query
#             stopwords = ['start']
#             querywords = quer.split()
#             resultwords = [word for word in querywords if word.lower() not in stopwords]
#             result = ' '.join(resultwords)
#             os.system('start ' + result)
#             rand = [('starting ' + result)]
#             speak(rand)
#
#         elif query != ('close music') and ('close') in query:
#             quer = query
#             stopwords = ['close']
#             querywords = quer.split()
#             resultwords = [word for word in querywords if word.lower() not in stopwords]
#             result = ' '.join(resultwords)
#             os.system('taskkill /im ' + result + '.exe /f')
#             rand = [('closing ' + result)]
#             speak(rand)
#
#         elif ('google maps') in query:
#             quer = query
#             stopwords = ['google', 'maps']
#             querywords = quer.split()
#             resultwords = [word for word in querywords if word.lower() not in stopwords]
#             result = ' '.join(resultwords)
#             Chrome = ("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe %s")
#             webbrowser.get(Chrome).open("https://www.google.be/maps/place/" + result + "/")
#             rand = [result + 'on google maps']
#             speak(rand)
#
#         elif 'where is' in query:
#             query = query.split("  ")
#             location = query[2]
#             speak("Please, hold on Akash, I will show you where " + location + "is. ")
#             os.system('''chromium-browser https://www.google.nl/maps/place/''' + location + "/&amp;")
#
#         elif 'nothing' in query or 'abort' in query or 'stop' in query:
#             speak('okay')
#             speak('Bye Sir, have a good day.')
#             sys.exit()
#
#         elif 'your name' in query:
#             rand = ['My name is Jarvis, at your service, sir']
#             speak(rand)
#
#         elif "what\'s up" in query or 'how are you' in query:
#             stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
#             speak(random.choice(stMsgs))
#
#         elif 'goodbye' in query:
#             Jarvis_Off = "Good Bye Akash! Jarvis off, 3, 2, 1, 0"
#             speak(Jarvis_Off)
#             sys.exit()
#
#         elif ('thanks') in query or ('tanks') in query or ('thank you') in query:
#             rand = ['You are welcome, sir', 'no problem']
#             speak(rand)
#
#         elif '*' in query:
#             rand = ['Be polite please, sir']
#             speak(rand)
#
#         elif 'email' in query:
#             try:
#                 speak("What should I say?")
#                 content = takeCommand()
#                 to = "Your Email-ID@gmail.com"
#                 sendEmail(to, content)
#                 speak("Email has been sent")
#             except Exception as e:
#                 print(e)
#                 speak("Sorry my friend Akash. I am not able to sent this email")
#
#         else:
#             query = query
#             speak('Searching...')
#             try:
#                 try:
#                     res = client.query(query)
#                     results = next(res.results).text
#                     print('According to WOLFRAM-ALPHA ...')
#                     print('Got it.')
#                     print(results)
#                     speak('WOLFRAM-ALPHA says - ')
#                     speak('Got it.')
#                     speak(results)
#
#                 except:
#                     results = wikipedia.summary(query, sentences=2)
#                     print('Got it.')
#                     print('According to Wikipedia... ')
#                     print(results)
#                     speak('Got it.')
#                     speak('According to Wikipedia... ')
#                     speak(results)
#
#             except:
#                 speak('I don\'t know Sir! Google is smarter than me!')
#                 print('I don\'t know Sir! Google is smarter than me!')
#                 webbrowser.open('www.google.com')
#
#         speak('Next Command! Sir!')




