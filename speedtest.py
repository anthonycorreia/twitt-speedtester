#!/usr/bin/python
import os
import sys
import csv
import datetime
import time
import tweepy

def speedtest():

        #Demarage de  speedtest-cli
        print 'Demarage du test'
        a = os.popen("python /usr/local/bin/speedtest --simple").read()
        print 'ran'
        #Separation du resultat en 3 lignes (ping,down,up)
        lines = a.split('\n')
        print a
        ts = time.time()
        date =datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        #Si le speedtest ne peut se conecter mise a 0 des valeurs du debit
        if "Cannot" in a:
                p = 1000
                d = 0
                u = 0
        #Recuperation des valeurs du ping down et up
        else:
                p = lines[0][6:11]
                d = lines[1][10:14]
                u = lines[2][8:12]
        print date,p, d, u

        #Conection a twitter
        consumer_secret = "xxxxxxxx"
        consumer_key = "xxxxxxx"

        access_token = "xxxxxx"
        access_token_secret = "xxxxxx"

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

        #Tweet si le debit down est inferieur a ce qui est configure
        if eval(d)<5:
                print "Ecriture du  tweet"
                try:
                        #Mise en forme du Tweet
                        tweet="Hey @VOTRE_FAI pourquoi mon debit internet est de " + str(int(eval(d))) + "Mb/s en down et " + str(int(eval(u))) + "Mb/s en up avec un ping de " + str(int(eval(p))) + "ms quand je paie pour XXXMb/s en down ?"
                        api.update_status(status=tweet)
                except Exception,e:
                        print str(e)
                        pass
        return

if __name__ == '__main__':
        speedtest()
        print 'Terminer avec succes'
