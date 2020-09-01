#https://kanoki.org/2018/12/27/text-matching-cosine-similarity/

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import pandas as pd
count_vect = CountVectorizer()

india_no_vpn_domain= ".google.co.in"\
".google.co.in"\
".google.co.in"\
".google.com"\
".google.com"\
".google.com"\
"www.wikipedia.org"\
".wikipedia.org"\
".wikipedia.org"\
".yahoo.com"\
".yahoo.com"\
".yahoo.com"\
".yahoo.com"\
".yahoo.com"\
"www.yahoo.com"\
"www.yahoo.com"\
".scorecardresearch.com"\
".scorecardresearch.com"\
".scorecardresearch.com"\
".analytics.yahoo.com"\
".agkn.com"\
".advertising.com"\
".bluekai.com"\
".bluekai.com"\
".bluekai.com"\
".demdex.net"\
".dpm.demdex.net"\
".facebook.com"\
".facebook.com"\
".facebook.com"\
".facebook.com"\
".atdmt.com"\
".doubleclick.net"\
".amazon.com"\
".amazon.com"\
".amazon.com"\
".amazon.com"\
".amazon.com"\
".associates-amazon.com"\
".amazon.com"\
"www.amazon.com"\
".scorecardresearch.com"\
".scorecardresearch.com"\
".indiatimes.com"\
".indiatimes.com"\
".indiatimes.com"\
".facebook.com"\
"www.indiatimes.com"\
".indiatimes.com"\
"www.indiatimes.com"\
"www.indiatimes.com"\
".doubleclick.net"\
".indiatimes.com"\
"www.indiatimes.com"\
".indiatimes.com"\
".indiatimes.com"\
".indiatimes.com"\
".indiatimes.com"\
".amazon.in"\
".amazon.in"\
".amazon.in"\
"www.amazon.in"\
".amazon.in"\
".amazon.in"\
".flipkart.com"\
".flipkart.com"\
".flipkart.com"\
".flipkart.com"\
".demdex.net"\
".flipkart.com"\
".flipkart.com"\
".flipkart.com"\
".youtube.com"\
".youtube.com"\
".youtube.com"\
".doubleclick.net"\
".hdfcbank.com"\
".blogger.com"\
"accounts.google.com"\
"accounts.google.com"\
".blogger.com"\
".blogger.com"\
".blogger.com"\
".stackoverflow.com"\
".stackoverflow.com"\
".stackoverflow.com"\
".stackoverflow.com"\
".scorecardresearch.com"\
".scorecardresearch.com"\
".quantserve.com"\
".stackoverflow.com"\
".instagram.com"\
".instagram.com"\
".instagram.com"\
".whatsapp.com"\
".www.whatsapp.com"\
".whatsapp.com"\
".primevideo.com"\
".primevideo.com"\
"www.primevideo.com"\
".primevideo.com"\
".worldometers.info"\
".worldometers.info"\
".worldometers.info"\
".worldometers.info"\
".worldometers.info"\
".worldometers.info"\
".quantserve.com"\
".worldometers.info"\
".doubleclick.net"\
".doubleclick.net"\
"www.worldometers.info"\
"www.worldometers.info"\
".addthis.com"\
".addthis.com"\
".addthis.com"\
".addthis.com"\
".addthis.com"\
".addthis.com"\
".addthis.com"\
".addthis.com"\
".addthis.com"\
"www.hotstar.com"\
"www.hotstar.com"\
"www.hotstar.com"\
"www.hotstar.com"\
"www.hotstar.com"\
".hotstar.com"\
".netflix.com"\
".netflix.com"\
".netflix.com"\
".netflix.com"\
".netflix.com"\
".netflix.com"\
".www.netflix.com"\
".facebook.com"\
".doubleclick.net"\
".onlinesbi.com"\
".onlinesbi.com"\
".onlinesbi.com"\
"outlook.live.com"\
".live.com"\
".live.com"\
".microsoft.com"\
".microsoft.com"\
"outlook.live.com"\
".office.com"\
"www.office.com"\
"www.office.com"\
"www.office.com"\
"www.office.com"\
"www.office.com"\
".microsoft.com"\
".microsoft.com"\
".login.live.com"\
".login.live.com"\
"login.microsoftonline.com"\
".login.microsoftonline.com"\
"login.microsoftonline.com"\
"login.microsoftonline.com"\
"www.office.com"\
".bing.com"\
".c.bing.com"\
".c.bing.com"\
".c.bing.com"\
".twitter.com"\
".twitter.com"\
".twitter.com"\
".twitter.com"\
".twitter.com"\
".twitter.com"\
".twitter.com"\
".twitter.com"\
"www.moneycontrol.com"\
"www.moneycontrol.com"\
"www.moneycontrol.com"\
"www.moneycontrol.com"\
"www.moneycontrol.com"\
"www.moneycontrol.com"\
".moneycontrol.com"\
".doubleclick.net"\
".www.linkedin.com"\
".linkedin.com"\
".linkedin.com"\
".www.linkedin.com"\
".linkedin.com"\
".linkedin.com"\
".scorecardresearch.com"\
".scorecardresearch.com"\
".www.linkedin.com"\
".linkedin.com"\
".linkedin.com"\
".linkedin.com"\
".demdex.net"\
".linkedin.com"\
".linkedin.com"\
".linkedin.com"\
".facebook.com"\
".doubleclick.net"\
".demdex.net"\
".dpm.demdex.net"\
".twitter.com"\
".zoom.us"\
".zoom.us"\
".zoom.us"\
".zoom.us"\
".zoom.us"\
".zoom.us"\
".zoom.us"\
"www.zoom.us"\
".zoom.us"\
".zoom.us"\
".zoom.us"\
".zoom.us"\
".zoom.us"\
"www.icicibank.com"\
".icicibank.com"\
".icicibank.com"\
".icicibank.com"\
".linkedin.com"\
".ads.linkedin.com"\
".linkedin.com"\
".icicibank.com"\
".icicibank.com"\
".linkedin.com"\
"www.icicibank.com"\
"www.icicibank.com"\
"www.icicibank.com"\
".icicibank.com"\
".icicibank.com"\
".icicibank.com"\
".doubleclick.net"\
".linkedin.com"\
".linkedin.com"\
".www.linkedin.com"\
".linkedin.com"\
".icicibank.com"\
".icicibank.com"\
".icicibank.com"\
".icicibank.com"\
".icicibank.com"\
".icicibank.com"\
".facebook.com"\
".adsymptotic.com"\
".nanorep.co"\
".icici.nanorep.co"\
"www.icicibank.com"\
".icici.nanorep.co"\
".icicibank.com"\
"www.microsoft.com"\
"www.microsoft.com"\
"www.microsoft.com"\
"www.microsoft.com"\
"www.microsoft.com"\
".microsoft.com"\
".microsoft.com"\
".microsoft.com"\
".microsoft.com"\
".microsoft.com"\
"www.microsoft.com"\
".login.live.com"\
".login.live.com"\
".bing.com"\
".c.bing.com"\
".c.bing.com"\
".c.bing.com"\
".c1.microsoft.com"\
".microsoft.com"\
".c1.microsoft.com"\
".c1.microsoft.com"\
".microsoft.com"\
".demdex.net"\
".microsoft.com"\
".mathtag.com"\
".dpm.demdex.net"\
"www.microsoft.com"\
".rlcdn.com"\
".rlcdn.com"\
".doubleclick.net"\
".microsoft.com"\
".microsoft.com"\
".media6degrees.com"\
".media6degrees.com"\
".twitter.com"\
".quantserve.com"\
".quantserve.com"\
".rfihub.com"\
".rfihub.com"\
".rfihub.com"\
".rfihub.com"\
".rfihub.com"\
".flashtalking.com"\
".adsrvr.org"\
".adsrvr.org"\
".tribalfusion.com"\
".yahoo.com"\
".owneriq.net"\
".owneriq.net"\
".postrelease.com"\
".postrelease.com"\
".reson8.com"\
"bttrack.com"\
".adentifi.com"\
".crwdcntrl.net"\
".crwdcntrl.net"\
".crwdcntrl.net"\
".crwdcntrl.net"\
".3lift.com"\
".demdex.net"\
".reddit.com"\
".reddit.com"\
".reddit.com"\
".reddit.com"\
".youtube.com"\
".youtube.com"\
".aaxads.com"\
"www.reddit.com"\
"www.reddit.com"\
".doubleclick.net"\
".rlcdn.com"\
".scorecardresearch.com"\
".scorecardresearch.com"\
".reddit.com"\
".quantserve.com"\
".zerodha.com"\
".zerodha.com"\
".zerodha.com"\
".zerodha.com"\
"zerodha.com"\
".manoramaonline.com"\
"www.manoramaonline.com"\
"www.manoramaonline.com"\
".manoramaonline.com"\
".doubleclick.net"\
".bing.com"\
".bing.com"\
"www.bing.com"\
".bing.com"\
".bing.com"\
".bing.com"\
".bing.com"\
".bing.com"\
".bing.com"\
".bing.com"\
".bing.com"\
"www2.bing.com"\
".bing.com"\
".login.live.com"\
".login.live.com"\
".wordpress.com"\
".wordpress.com"\
".wordpress.com"\
"wordpress.com"\
".wordpress.com"\
".wordpress.com"\
".wordpress.com"\
"wordpress.com"\
".bing.com"\
".bat.bing.com"\
".wordpress.com"\
".wordpress.com"\
".wordpress.com"\
".wordpress.com"\
".wordpress.com"\
".wordpress.com"\
".facebook.com"\
".wordpress.com"\
".doubleclick.net"\
".wordpress.com"\
".ct.pinterest.com"\
"github.com"\
".github.com"\
".github.com"\
".github.com"\
".github.com"\
".github.com"\
".udemy.com"\
".udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
".udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
".udemy.com"\
".udemy.com"\
".udemy.com"\
".udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
"www.intoday.in"\
"www.indiatodaygroup.com"\
"www.indiatodaygroup.com"\
"www.indiatodaygroup.com"\
".scorecardresearch.com"\
".scorecardresearch.com"\
".indiatodaygroup.com"\
".indiatodaygroup.com"\
".indiatodaygroup.com"\
"www.indiatoday.in"\
".scorecardresearch.com"\
".scorecardresearch.com"\
".indiatoday.in"\
".indiatoday.in"\
".indiatoday.in"\
"www.indiatoday.in"\
".zedo.com"\
".zedo.com"\
".zedo.com"\
".zedo.com"\
".zedo.com"\
".zedo.com"\
".zedo.com"\
".app.link"\
".casalemedia.com"\
".casalemedia.com"\
".izooto.com"\
".pubmatic.com"\
".ads.pubmatic.com"\
".pubmatic.com"\
".rubiconproject.com"\
"eus.rubiconproject.com"\
".intoday.in"\
".pubmatic.com"\
".pubmatic.com"\
".pubmatic.com"\
".pubmatic.com"\
".indiatoday.in"\
".doubleclick.net"\
".turn.com"\
".adsymptotic.com"\
".mathtag.com"\
".rlcdn.com"\
".rlcdn.com"\
"id.sharedid.org"\
".pippio.com"\
".pippio.com"\
".pippio.com"\
".pippio.com"\
".pubmatic.com"\
".pubmatic.com"\
".pubmatic.com"\
".pubmatic.com"\
".adsrvr.org"\
".yahoo.com"\
".doubleclick.net"\
".simpli.fi"\
".pubmatic.com"\
".pubmatic.com"\
"www.indiatoday.in"\
".adsrvr.org"\
".rubiconproject.com"\
".pubmatic.com"\
".krxd.net"\
"www.indiatoday.in"\
"www.indiatoday.in"\
"www.indiatoday.in"\
".google.com"\
".w3schools.com"\
".w3schools.com"\
".w3schools.com"\
".w3schools.com"\
"www.w3schools.com"\
".casalemedia.com"\
".smartadserver.com"\
".smartadserver.com"\
".smartadserver.com"\
".smartadserver.com"\
".smartadserver.com"\
".smartadserver.com"\
".prg.smartadserver.com"\
".connectad.io"\
".lijit.com"\
".lijit.com"\
".imdb.com"\
".imdb.com"\
".imdb.com"\
".imdb.com"\
"www.imdb.com"\
".scorecardresearch.com"\
".scorecardresearch.com"\
".who.int"\
".youtube.com"\
".youtube.com"\
"www.who.int"\
"www.who.int"\
".addthis.com"\
".addthis.com"\
".addthis.com"\
".addthis.com"\
".addthis.com"\
".addthis.com"\
".addthis.com"\
".who.int"\
".who.int"\
".who.int"\
".addthis.com"\
".addthis.com"\
".twitter.com"\
".doubleclick.net"\
".quora.com"\
".quora.com"\
".quora.com"\
".quora.com"\
".quora.com"\
".quora.com"\
".quora.com"\
".quora.com"\
".quora.com"\
".rlcdn.com"\
".rlcdn.com"\
".quora.com"\
".quora.com"\
".www.quora.com"\
".taboola.com"\
".grammarly.com"\
".grammarly.com"\
".grammarly.com"\
".grammarly.com"\
".grammarly.com"\
".grammarly.com"\
".grammarly.com"\
".grammarly.com"\
".grammarly.com"\
".grammarly.com"\
".facebook.com"\
".bing.com"\
".bat.bing.com"\
".linkedin.com"\
".ads.linkedin.com"\
".linkedin.com"\
".grammarly.com"\
".grammarly.com"\
".grammarly.com"\
".taboola.com"\
".linkedin.com"\
".doubleclick.net"\
".linkedin.com"\
".linkedin.com"\
".www.linkedin.com"\
".linkedin.com"\
".grammarly.com"\
".adsymptotic.com"\
".twitter.com"\
".naukri.com"\
".naukri.com"\
".naukri.com"\
".naukri.com"\
".naukri.com"\
".naukri.com"\
"www.naukri.com"\
".naukri.com"\
".naukri.com"\
".naukri.com"\
".naukri.com"\
".naukri.com"\
".naukri.com"\
".facebook.com"\
".doubleclick.net"\
".naukri.com"\
".freepik.com"\
".freepik.com"\
".www.freepik.com"\
".freepik.com"\
".bing.com"\
".bat.bing.com"\
".www.freepik.com"\
".freepik.com"\
".statcounter.com"\
".doubleclick.net"\
".freepik.com"\
".freepik.com"\
".adform.net"\
".freepik.com"\
".freepik.com"\
".freepik.com"\
".freepik.com"\
".freepik.com"\
".freepik.com"\
".facebook.com"\
".adform.net"\
".freepik.com"\
".freepik.com"\
".freepik.com"\
"www.freepik.com"\
"www.freepik.com"\
".mathtag.com"\
".mathtag.com"\
".freepik.com"\
".freepik.com"\
".freepik.com"\
".freepik.com"\
".twitter.com"\
".aws.amazon.com"\
".amazon.com"\
".aws.amazon.com"\
".amazon.com"\
".amazon.com"\
".amazon.com"\
".amazon.com"\
".amazon.com"\
".amazon.com"\
".amazon.com"\
".amazon.com"\
".amazon.com"\
".amazonwebservices.d2.sc.omtrdc.net"\
".amazon.com"\
".linkedin.com"\
".ads.linkedin.com"\
".linkedin.com"\
".doubleclick.net"\
".linkedin.com"\
".linkedin.com"\
".linkedin.com"\
".www.linkedin.com"\
".linkedin.com"\
".adsymptotic.com"\
".amazon.com"\
".amazon.com"\
".amazon.com"\
"www.livejasmin.com"\
".livejasmin.com"\
".livejasmin.com"\
".livejasmin.com"\
".livejasmin.com"\
".livejasmin.com"\
".livejasmin.com"\
".livejasmin.com"\
".livejasmin.com"\
".livejasmin.com"\
".livejasmin.com"\
".livejasmin.com"\
"www.livejasmin.com"\
".livejasmin.com"\
".livejasmin.com"\
".livejasmin.com"\
".livejasmin.com"\
".livejasmin.com"\
".livejasmin.com"\
".livejasmin.com"\
".livejasmin.com"\
".livejasmin.com"\
".livejasmin.com"\
".livejasmin.com"\
".taboola.com"\
".ndtv.com"\
"www.ndtv.com"\
".scorecardresearch.com"\
".scorecardresearch.com"\
"www.ndtv.com"\
"www.ndtv.com"\
"www.ndtv.com"\
".ndtv.com"\
".ndtv.com"\
".ndtv.com"\
".ndtv.com"\
".taboola.com"\
".ndtv.com"\
".doubleclick.net"\
".lijit.com"\
".ndtv.com"\
".ndtv.com"\
".twitter.com"\
".openx.net"\
"www.ndtv.com"\
"bh.contextweb.com"\
".pubmatic.com"\
".ads.pubmatic.com"\
".pubmatic.com"\
".pubmatic.com"\
".pubmatic.com"\
".pubmatic.com"\
".pubmatic.com"\
".rubiconproject.com"\
".rlcdn.com"\
".adsymptotic.com"\
".turn.com"\
".mathtag.com"\
".pubmatic.com"\
".pubmatic.com"\
".pubmatic.com"\
".pubmatic.com"\
".pubmatic.com"\
".pubmatic.com"\
".adsrvr.org"\
".yahoo.com"\
".simpli.fi"\
".pippio.com"\
".pippio.com"\
".pippio.com"\
".adsrvr.org"\
".pubmatic.com"\
".pippio.com"\
".krxd.net"

india_vpn_domains= "www.wikipedia.org"\
".wikipedia.org"\
".wikipedia.org"\
".google.com"\
".google.com"\
".facebook.com"\
".facebook.com"\
".facebook.com"\
".facebook.com"\
".amazon.com"\
".amazon.com"\
".amazon.com"\
".amazon.com"\
".amazon.com"\
".amazon.com"\
".amazon.com"\
"www.amazon.com"\
".youtube.com"\
".youtube.com"\
".youtube.com"\
".indiatimes.com"\
".indiatimes.com"\
"www.indiatimes.com"\
".indiatimes.com"\
".indiatimes.com"\
".facebook.com"\
"www.indiatimes.com"\
"www.indiatimes.com"\
".indiatimes.com"\
".doubleclick.net"\
"www.indiatimes.com"\
".indiatimes.com"\
".indiatimes.com"\
".indiatimes.com"\
".indiatimes.com"\
".amazon.in"\
".amazon.in"\
".amazon.in"\
".amazon.in"\
".amazon.in"\
"www.amazon.in"\
".amazon.in"\
".flipkart.com"\
".flipkart.com"\
".flipkart.com"\
".demdex.net"\
".flipkart.com"\
".flipkart.com"\
".flipkart.com"\
".flipkart.com"\
".yahoo.com"\
".yahoo.com"\
".yahoo.com"\
".yahoo.com"\
".yahoo.com"\
"www.yahoo.com"\
"www.yahoo.com"\
".analytics.yahoo.com"\
"www.yahoo.com"\
".scorecardresearch.com"\
".scorecardresearch.com"\
".scorecardresearch.com"\
".agkn.com"\
".advertising.com"\
".demdex.net"\
".bluekai.com"\
".bluekai.com"\
".bluekai.com"\
".dpm.demdex.net"\
".google.co.in"\
".google.co.in"\
".google.co.in"\
".instagram.com"\
".instagram.com"\
".instagram.com"\
".whatsapp.com"\
".www.whatsapp.com"\
".whatsapp.com"\
".onlinesbi.com"\
".onlinesbi.com"\
".onlinesbi.com"\
".stackoverflow.com"\
".scorecardresearch.com"\
".scorecardresearch.com"\
".primevideo.com"\
".primevideo.com"\
".primevideo.com"\
"www.primevideo.com"\
".primevideo.com"\
"www.hotstar.com"\
"www.hotstar.com"\
"www.hotstar.com"\
"www.hotstar.com"\
".hotstar.com"\
".hotstar.com"\
".hotstar.com"\
".hotstar.com"\
".hotstar.com"\
".hotstar.com"\
".hotstar.com"\
".hotstar.com"\
".hotstar.com"\
".doubleclick.net"\
".bing.com"\
".bat.bing.com"\
".hotstar.com"\
".hotstar.com"\
".facebook.com"\
".twitter.com"\
".worldometers.info"\
".worldometers.info"\
".worldometers.info"\
".worldometers.info"\
".worldometers.info"\
".doubleclick.net"\
".quantserve.com"\
".worldometers.info"\
".worldometers.info"\
".hdfcbank.com"\
".hdfcbank.com"\
".hdfcbank.com"\
".hdfcbank.com"\
".demdex.net"\
".hdfcbank.com"\
".hdfcbank.com"\
".hdfcbank.com"\
".hdfcbank.com"\
".hdfcbank.com"\
".hdfcbank.com"\
".dpm.demdex.net"\
".hdfcbank.com"\
".demdex.net"\
".doubleclick.net"\
".agkn.com"\
".rlcdn.com"\
".rlcdn.com"\
".scorecardresearch.com"\
".scorecardresearch.com"\
".zeotap.com"\
".zeotap.com"\
".eyeota.net"\
".eyeota.net"\
".crwdcntrl.net"\
".crwdcntrl.net"\
".crwdcntrl.net"\
".crwdcntrl.net"\
".hdfcbank.com"\
".hdfcbank.com"\
".hdfcbank.com"\
".hdfcbank.com"\
"hbchat.senseforth.com"\
".hdfcbank.com"\
"hbsearch.senseforth.com"\
".facebook.com"\
".blogger.com"\
"accounts.google.com"\
"accounts.google.com"\
".netflix.com"\
".netflix.com"\
".netflix.com"\
".netflix.com"\
".netflix.com"\
".netflix.com"\
".www.netflix.com"\
".facebook.com"\
".www.linkedin.com"\
".linkedin.com"\
".linkedin.com"\
".www.linkedin.com"\
".linkedin.com"\
".linkedin.com"\
".www.linkedin.com"\
".scorecardresearch.com"\
".scorecardresearch.com"\
".linkedin.com"\
".linkedin.com"\
".linkedin.com"\
".demdex.net"\
".linkedin.com"\
".linkedin.com"\
"www.microsoft.com"\
"www.microsoft.com"\
".microsoft.com"\
"www.microsoft.com"\
"www.microsoft.com"\
"www.microsoft.com"\
".microsoft.com"\
".microsoft.com"\
".microsoft.com"\
".microsoft.com"\
".microsoft.com"\
"www.microsoft.com"\
".demdex.net"\
".microsoft.com"\
".demdex.net"\
".twitter.com"\
".doubleclick.net"\
".dpm.demdex.net"\
".microsoft.com"\
".microsoft.com"\
".rlcdn.com"\
".adsrvr.org"\
".adsrvr.org"\
".rlcdn.com"\
".quantserve.com"\
".quantserve.com"\
".bing.com"\
".c.bing.com"\
".yahoo.com"\
".flashtalking.com"\
".tribalfusion.com"\
".postrelease.com"\
".postrelease.com"\
".owneriq.net"\
".owneriq.net"\
".rfihub.com"\
".rfihub.com"\
".rfihub.com"\
".rfihub.com"\
".3lift.com"\
".mathtag.com"\
"bttrack.com"\
".crwdcntrl.net"\
".crwdcntrl.net"\
".crwdcntrl.net"\
".crwdcntrl.net"\
".adentifi.com"\
".login.live.com"\
".login.live.com"\
"sync.srv.stackadapt.com"\
".srv.stackadapt.com"\
".office.com"\
"www.office.com"\
"www.office.com"\
"www.office.com"\
"www.office.com"\
"www.office.com"\
".microsoft.com"\
".microsoft.com"\
"www.office.com"\
"login.microsoftonline.com"\
".login.microsoftonline.com"\
"login.microsoftonline.com"\
"login.microsoftonline.com"\
".login.live.com"\
".login.live.com"\
"www.moneycontrol.com"\
"www.moneycontrol.com"\
"www.moneycontrol.com"\
"www.moneycontrol.com"\
"www.moneycontrol.com"\
"www.moneycontrol.com"\
"outlook.live.com"\
".live.com"\
".live.com"\
".microsoft.com"\
".microsoft.com"\
"outlook.live.com"\
".twitter.com"\
".twitter.com"\
".twitter.com"\
".twitter.com"\
".twitter.com"\
".twitter.com"\
".twitter.com"\
".twitter.com"\
".app.link"\
".zoom.us"\
".zoom.us"\
".zoom.us"\
".zoom.us"\
".zoom.us"\
".zoom.us"\
".zoom.us"\
".zoom.us"\
".zoom.us"\
"www.zoom.us"\
".zoom.us"\
".zoom.us"\
"static.zoom.us"\
".zoom.us"\
".zoom.us"\
".zoom.us"\
"www.icicibank.com"\
"www.icicibank.com"\
"www.icicibank.com"\
"www.icicibank.com"\
".icicibank.com"\
".icicibank.com"\
".icicibank.com"\
".icicibank.com"\
".icicibank.com"\
".icicibank.com"\
".icicibank.com"\
".icicibank.com"\
".icicibank.com"\
".icicibank.com"\
".icicibank.com"\
".icicibank.com"\
".icicibank.com"\
".doubleclick.net"\
".icicibank.com"\
".facebook.com"\
".nanorep.co"\
".icici.nanorep.co"\
"www.icicibank.com"\
".linkedin.com"\
".ads.linkedin.com"\
".linkedin.com"\
".icici.nanorep.co"\
".linkedin.com"\
".icicibank.com"\
".linkedin.com"\
".linkedin.com"\
".www.linkedin.com"\
".linkedin.com"\
".reddit.com"\
".reddit.com"\
".reddit.com"\
".reddit.com"\
".youtube.com"\
".youtube.com"\
".doubleclick.net"\
".aaxads.com"\
"www.reddit.com"\
"www.reddit.com"\
".scorecardresearch.com"\
".scorecardresearch.com"\
".rlcdn.com"\
".rlcdn.com"\
".quantserve.com"\
".reddit.com"\
".bing.com"\
".bing.com"\
"www.bing.com"\
".bing.com"\
".bing.com"\
".bing.com"\
".bing.com"\
".bing.com"\
".bing.com"\
"github.com"\
".github.com"\
".github.com"\
".github.com"\
".manoramaonline.com"\
"www.manoramaonline.com"\
"www.manoramaonline.com"\
".udemy.com"\
".udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
".udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
".udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
".udemy.com"\
".udemy.com"\
".udemy.com"\
".udemy.com"\
".intljs.rmtag.com"\
".intljs.rmtag.com"\
".www.udemy.com"\
".udemy.com"\
".udemy.com"\
".pointmediatracker.com"\
".udemy.com"\
".udemy.com"\
".udemy.com"\
".linksynergy.com"\
".linksynergy.com"\
".facebook.com"\
".rlcdn.com"\
".rlcdn.com"\
".dc-storm.com"\
"www.intoday.in"\
"www.indiatodaygroup.com"\
"www.indiatodaygroup.com"\
"www.indiatodaygroup.com"\
".indiatodaygroup.com"\
".indiatodaygroup.com"\
".indiatodaygroup.com"\
".scorecardresearch.com"\
".scorecardresearch.com"\
".indiatoday.in"\
".indiatoday.in"\
".scorecardresearch.com"\
".scorecardresearch.com"\
"www.indiatoday.in"\
"www.indiatoday.in"\
".zedo.com"\
".zedo.com"\
".zedo.com"\
".zedo.com"\
".zedo.com"\
".zedo.com"\
".zedo.com"\
".izooto.com"\
".casalemedia.com"\
".casalemedia.com"\
".indiatoday.in"\
".doubleclick.net"\
".rubiconproject.com"\
"eus.rubiconproject.com"\
".adsrvr.org"\
".mathtag.com"\
".app.link"\
"id.sharedid.org"\
".yahoo.com"\
".rubiconproject.com"\
".intoday.in"\
".pubmatic.com"\
".pubmatic.com"\
".pubmatic.com"\
".pubmatic.com"\
".pubmatic.com"\
".pubmatic.com"\
".adsrvr.org"\
".simpli.fi"\
".pubmatic.com"\
".pubmatic.com"\
".pubmatic.com"\
".pippio.com"\
".pippio.com"\
".pippio.com"\
".pippio.com"\
".quantserve.com"\
".quantserve.com"\
".pubmatic.com"\
".turn.com"\
".pubmatic.com"\
".rlcdn.com"\
".rlcdn.com"\
".pubmatic.com"\
".pubmatic.com"\
".pubmatic.com"\
".zerodha.com"\
".zerodha.com"\
".zerodha.com"\
".zerodha.com"\
"zerodha.com"\
".wordpress.com"\
".wordpress.com"\
".wordpress.com"\
".wordpress.com"\
"wordpress.com"\
".wordpress.com"\
".wordpress.com"\
".wordpress.com"\
".wordpress.com"\
".bing.com"\
".bat.bing.com"\
".wordpress.com"\
".wordpress.com"\
".doubleclick.net"\
".wordpress.com"\
".facebook.com"\
".wordpress.com"\
".ct.pinterest.com"\
".wordpress.com"\
".wordpress.com"\
".wordpress.com"\
".wordpress.com"\
".imdb.com"\
".imdb.com"\
".imdb.com"\
".imdb.com"\
"www.imdb.com"\
".naukri.com"\
".naukri.com"\
".naukri.com"\
".naukri.com"\
".naukri.com"\
".naukri.com"\
"www.naukri.com"\
".naukri.com"\
".naukri.com"\
".naukri.com"\
".naukri.com"\
".naukri.com"\
".naukri.com"\
".naukri.com"\
".doubleclick.net"\
".facebook.com"\
".quora.com"\
".quora.com"\
".quora.com"\
".quora.com"\
".quora.com"\
".quora.com"\
".quora.com"\
".quora.com"\
".quora.com"\
".grammarly.com"\
".grammarly.com"\
".grammarly.com"\
".grammarly.com"\
".grammarly.com"\
".grammarly.com"\
".grammarly.com"\
".grammarly.com"\
".grammarly.com"\
".grammarly.com"\
".freepik.com"\
".www.freepik.com"\
".www.freepik.com"\
".freepik.com"\
".doubleclick.net"\
".freepik.com"\
".facebook.com"\
".freepik.com"\
".freepik.com"\
"www.freepik.com"\
".freepik.com"\
".freepik.com"\
".statcounter.com"\
".adform.net"\
".adform.net"\
".w3schools.com"\
".w3schools.com"\
".w3schools.com"\
".pubmatic.com"\
".connectad.io"\
".pubmatic.com"\
".pubmatic.com"\
".rubiconproject.com"\
"eus.rubiconproject.com"\
".openx.net"\
".lijit.com"\
".bidswitch.net"\
".casalemedia.com"\
".bidswitch.net"\
".bidswitch.net"\
".casalemedia.com"\
".pubmatic.com"\
".pubmatic.com"\
".ads.pubmatic.com"\
".sportradarserving.com"\
".sportradarserving.com"\
".sportradarserving.com"\
".connectad.io"\
".adform.net"\
".impact-ad.jp"\
".impact-ad.jp"\
".impact-ad.jp"\
"m.one.impact-ad.jp"\
"ads.playground.xyz"\
"ads.playground.xyz"\
".simpli.fi"\
".turn.com"\
".gumgum.com"\
".quantserve.com"\
".quantserve.com"\
"beacon.lynx.cognitivlabs.com"\
"beacon.lynx.cognitivlabs.com"\
".pubmatic.com"\
".doubleclick.net"\
".adsrvr.org"\
".demdex.net"\
".pubmatic.com"\
".pubmatic.com"\
".dpm.demdex.net"\
".pubmatic.com"\
".mathtag.com"\
".pubmatic.com"\
".adsrvr.org"\
".pubmatic.com"\
".pubmatic.com"\
".pubmatic.com"\
".tapad.com"\
".tapad.com"\
".pubmatic.com"\
".pubmatic.com"\
".rfihub.com"\
".rfihub.com"\
".rfihub.com"\
".rfihub.com"\
".casalemedia.com"\
".ctnsnet.com"\
".w55c.net"\
".pubmatic.com"\
".w55c.net"\
".tribalfusion.com"\
".pubmatic.com"\
".pubmatic.com"\
".pubmatic.com"\
".rubiconproject.com"\
".pubmatic.com"\
".advertising.com"\
".casalemedia.com"\
".casalemedia.com"\
".pippio.com"\
".pippio.com"\
".pippio.com"\
".pippio.com"\
".rlcdn.com"\
".rlcdn.com"\
".ads.pubmatic.com"\
".yahoo.com"\
".google.com"\
"www.w3schools.com"\
".aws.amazon.com"\
".amazon.com"\
".aws.amazon.com"\
".amazon.com"\
".amazon.com"\
".amazon.com"\
".amazon.com"\
".amazon.com"\
".amazon.com"\
".amazon.com"\
".amazon.com"\
".amazon.com"\
".amazon.com"\
".amazonwebservices.d2.sc.omtrdc.net"\
".amazon.com"\
".amazon.com"\
".youtube.com"\
".youtube.com"\
"www.who.int"\
"www.who.int"\
".addthis.com"\
".addthis.com"\
".addthis.com"\
".addthis.com"\
".addthis.com"\
".addthis.com"\
".addthis.com"\
".addthis.com"\
".addthis.com"\
".who.int"\
".taboola.com"\
".ndtv.com"\
".ndtv.com"\
".ndtv.com"\
".ndtv.com"\
".scorecardresearch.com"\
".scorecardresearch.com"\
".taboola.com"\
"www.ndtv.com"\
".ndtv.com"\
"www.ndtv.com"\
"www.ndtv.com"\
".ndtv.com"\
".doubleclick.net"\
".serving-sys.com"\
".ndtv.com"\
".ndtv.com"


india_local_domains = ".google.com"\
".google.com"\
".google.com"\
".google.co.in"\
".google.co.in"\
".google.co.in"\
".facebook.com"\
".facebook.com"\
".amazon.in"\
".amazon.in"\
".amazon.in"\
"www.amazon.in"\
".amazon.in"\
".amazon.in"\
".flipkart.com"\
".demdex.net"\
".flipkart.com"\
".flipkart.com"\
".flipkart.com"\
".flipkart.com"\
".flipkart.com"\
".flipkart.com"\
".flipkart.com"\
"www.wikipedia.org"\
".wikipedia.org"\
".wikipedia.org"\
".www.yahoo.com"\
".yahoo.com"\
".yahoo.com"\
".yahoo.com"\
".yahoo.com"\
".yahoo.com"\
".scorecardresearch.com"\
".scorecardresearch.com"\
".scorecardresearch.com"\
".analytics.yahoo.com"\
".demdex.net"\
".advertising.com"\
".dpm.demdex.net"\
".bluekai.com"\
".bluekai.com"\
".bluekai.com"\
".agkn.com"\
".amazon.com"\
".amazon.com"\
".amazon.com"\
".amazon.com"\
".amazon.com"\
".amazon.com"\
".associates-amazon.com"\
"www.amazon.com"\
".amazon.com"\
"www.indiatimes.com"\
".indiatimes.com"\
".indiatimes.com"\
".scorecardresearch.com"\
".scorecardresearch.com"\
".indiatimes.com"\
".indiatimes.com"\
"www.indiatimes.com"\
"www.indiatimes.com"\
".indiatimes.com"\
".indiatimes.com"\
".indiatimes.com"\
".indiatimes.com"\
".facebook.com"\
".indiatimes.com"\
".doubleclick.net"\
"www.indiatimes.com"\
".youtube.com"\
".youtube.com"\
".youtube.com"\
".doubleclick.net"\
".instagram.com"\
".instagram.com"\
".instagram.com"\
".onlinesbi.com"\
".onlinesbi.com"\
".onlinesbi.com"\
".primevideo.com"\
".primevideo.com"\
".primevideo.com"\
"www.primevideo.com"\
".primevideo.com"\
".whatsapp.com"\
".www.whatsapp.com"\
".whatsapp.com"\
".stackoverflow.com"\
".scorecardresearch.com"\
".scorecardresearch.com"\
".stackoverflow.com"\
".stackoverflow.com"\
".stackoverflow.com"\
".quantserve.com"\
".stackoverflow.com"\
"www.hotstar.com"\
"www.hotstar.com"\
"www.hotstar.com"\
".hotstar.com"\
"www.hotstar.com"\
".hotstar.com"\
".netflix.com"\
".netflix.com"\
".netflix.com"\
".netflix.com"\
".netflix.com"\
".netflix.com"\
".www.netflix.com"\
".facebook.com"\
".doubleclick.net"\
".worldometers.info"\
".worldometers.info"\
".worldometers.info"\
".worldometers.info"\
".worldometers.info"\
".worldometers.info"\
".quantserve.com"\
".worldometers.info"\
".doubleclick.net"\
".doubleclick.net"\
".hdfcbank.com"\
".hdfcbank.com"\
".hdfcbank.com"\
".demdex.net"\
".hdfcbank.com"\
".hdfcbank.com"\
".agkn.com"\
".hdfcbank.com"\
".hdfcbank.com"\
".hdfcbank.com"\
"hbchat.senseforth.com"\
".dpm.demdex.net"\
".hdfcbank.com"\
".hdfcbank.com"\
".hdfcbank.com"\
".hdfcbank.com"\
".hdfcbank.com"\
".hdfcbank.com"\
".hdfcbank.com"\
".doubleclick.net"\
".rlcdn.com"\
".rlcdn.com"\
".eyeota.net"\
".eyeota.net"\
".hdfcbank.com"\
".scorecardresearch.com"\
".scorecardresearch.com"\
".facebook.com"\
".demdex.net"\
".zeotap.com"\
".zeotap.com"\
".crwdcntrl.net"\
".crwdcntrl.net"\
".crwdcntrl.net"\
".crwdcntrl.net"\
".blogger.com"\
"accounts.google.com"\
".blogger.com"\
".blogger.com"\
".blogger.com"\
"outlook.live.com"\
".live.com"\
".live.com"\
".microsoft.com"\
".microsoft.com"\
"outlook.live.com"\
".office.com"\
"www.office.com"\
"www.office.com"\
"www.office.com"\
".microsoft.com"\
".microsoft.com"\
"www.office.com"\
".twitter.com"\
".twitter.com"\
".twitter.com"\
".twitter.com"\
".twitter.com"\
".twitter.com"\
".twitter.com"\
".www.linkedin.com"\
".linkedin.com"\
".linkedin.com"\
".www.linkedin.com"\
".linkedin.com"\
".linkedin.com"\
".www.linkedin.com"\
".scorecardresearch.com"\
".scorecardresearch.com"\
".linkedin.com"\
".linkedin.com"\
".linkedin.com"\
".demdex.net"\
".linkedin.com"\
".linkedin.com"\
".demdex.net"\
".linkedin.com"\
".twitter.com"\
".facebook.com"\
".doubleclick.net"\
".dpm.demdex.net"\
"www.icicibank.com"\
"www.icicibank.com"\
"www.icicibank.com"\
"www.icicibank.com"\
".icicibank.com"\
".icicibank.com"\
".icicibank.com"\
".icicibank.com"\
".icicibank.com"\
".icicibank.com"\
".icicibank.com"\
".linkedin.com"\
".ads.linkedin.com"\
".linkedin.com"\
".icicibank.com"\
".icicibank.com"\
".icicibank.com"\
".icicibank.com"\
".icicibank.com"\
".nanorep.co"\
".icicibank.com"\
".linkedin.com"\
".icici.nanorep.co"\
"www.icicibank.com"\
".icici.nanorep.co"\
".doubleclick.net"\
".linkedin.com"\
".linkedin.com"\
".www.linkedin.com"\
".linkedin.com"\
".icicibank.com"\
".facebook.com"\
".icicibank.com"\
"www.microsoft.com"\
"www.microsoft.com"\
"www.microsoft.com"\
"www.microsoft.com"\
"www.microsoft.com"\
".microsoft.com"\
".microsoft.com"\
".microsoft.com"\
".microsoft.com"\
".microsoft.com"\
"www.microsoft.com"\
".microsoft.com"\
".demdex.net"\
".microsoft.com"\
".login.live.com"\
".login.live.com"\
".bing.com"\
".c.bing.com"\
".c.bing.com"\
".c.bing.com"\
".c1.microsoft.com"\
".microsoft.com"\
".c1.microsoft.com"\
".c1.microsoft.com"\
".rlcdn.com"\
".doubleclick.net"\
".dpm.demdex.net"\
".twitter.com"\
".adsrvr.org"\
".rlcdn.com"\
".microsoft.com"\
".microsoft.com"\
".mathtag.com"\
".adsrvr.org"\
".quantserve.com"\
".quantserve.com"\
".owneriq.net"\
".owneriq.net"\
".yahoo.com"\
".flashtalking.com"\
".rfihub.com"\
".rfihub.com"\
".rfihub.com"\
".tribalfusion.com"\
".3lift.com"\
".postrelease.com"\
".postrelease.com"\
".crwdcntrl.net"\
".crwdcntrl.net"\
".crwdcntrl.net"\
".crwdcntrl.net"\
"bttrack.com"\
".adentifi.com"\
".demdex.net"\
".zoom.us"\
".zoom.us"\
".zoom.us"\
".zoom.us"\
".zoom.us"\
".zoom.us"\
".zoom.us"\
"www.zoom.us"\
".zoom.us"\
".zoom.us"\
".zoom.us"\
".zoom.us"\
".zoom.us"\
".reddit.com"\
".reddit.com"\
".reddit.com"\
".reddit.com"\
".aaxads.com"\
"www.reddit.com"\
"www.reddit.com"\
".scorecardresearch.com"\
".scorecardresearch.com"\
".rlcdn.com"\
".reddit.com"\
".quantserve.com"\
"widgets.outbrain.com"\
"bs.serving-sys.com"\
"www.moneycontrol.com"\
".scorecardresearch.com"\
".scorecardresearch.com"\
".moneycontrol.com"\
".moneycontrol.com"\
".moneycontrol.com"\
".moneycontrol.com"\
".moneycontrol.com"\
".moneycontrol.com"\
".facebook.com"\
".doubleclick.net"\
".izooto.com"\
".serving-sys.com"\
".outbrain.com"\
".moneycontrol.com"\
".moneycontrol.com"\
".demdex.net"\
".samsungindiaelectronics.demdex.net"\
".adsrvr.org"\
".dpm.demdex.net"\
".bluekai.com"\
".bluekai.com"\
".bluekai.com"\
".adsrvr.org"\
".agkn.com"\
".mfadsrvr.com"\
".mfadsrvr.com"\
".mfadsrvr.com"\
".krxd.net"\
".mfadsrvr.com"\
".zemanta.com"\
".pippio.com"\
".pippio.com"\
".pippio.com"\
".pippio.com"\
".adfarm1.adition.com"\
".eyeota.net"\
".eyeota.net"\
".outbrain.com"\
".exelator.com"\
".outbrain.com"\
".outbrain.com"\
".rlcdn.com"\
".outbrain.com"\
".exelator.com"\
".exelator.com"\
".bidswitch.net"\
".creativecdn.com"\
".creativecdn.com"\
".bidswitch.net"\
".bidswitch.net"\
".geistm.com"\
".adotmob.com"\
".adotmob.com"\
".adotmob.com"\
".outbrain.com"\
".outbrain.com"\
"bttrack.com"\
".connexity.net"\
".rubiconproject.com"\
".rubiconproject.com"\
".impact-ad.jp"\
".impact-ad.jp"\
".impact-ad.jp"\
".outbrain.com"\
"m.one.impact-ad.jp"\
".bing.com"\
".bing.com"\
"www.bing.com"\
".bing.com"\
".bing.com"\
".bing.com"\
".bing.com"\
".bing.com"\
".bing.com"\
".bing.com"\
"4.bing.com"\
".bing.com"\
".manoramaonline.com"\
"www.manoramaonline.com"\
"www.manoramaonline.com"\
".doubleclick.net"\
".manoramaonline.com"\
"www.intoday.in"\
"www.indiatodaygroup.com"\
"www.indiatodaygroup.com"\
"www.indiatodaygroup.com"\
".indiatodaygroup.com"\
".indiatodaygroup.com"\
".indiatodaygroup.com"\
".scorecardresearch.com"\
".scorecardresearch.com"\
"github.com"\
".github.com"\
".github.com"\
".github.com"\
".github.com"\
".github.com"\
".udemy.com"\
".udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
".udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
".udemy.com"\
".udemy.com"\
".udemy.com"\
".udemy.com"\
"www.udemy.com"\
"www.udemy.com"\
".wordpress.com"\
".wordpress.com"\
".wordpress.com"\
".wordpress.com"\
".wordpress.com"\
"wordpress.com"\
".wordpress.com"\
".wordpress.com"\
".wordpress.com"\
".bing.com"\
".bat.bing.com"\
".wordpress.com"\
".wordpress.com"\
".wordpress.com"\
".facebook.com"\
".doubleclick.net"\
".wordpress.com"\
".wordpress.com"\
".wordpress.com"\
".ct.pinterest.com"\
".wordpress.com"\
".wordpress.com"\
"www.indiatoday.in"\
".scorecardresearch.com"\
".scorecardresearch.com"\
"www.indiatoday.in"\
".indiatoday.in"\
".indiatoday.in"\
".indiatoday.in"\
".zedo.com"\
".zedo.com"\
".zedo.com"\
".zedo.com"\
".zedo.com"\
".izooto.com"\
".zedo.com"\
".zedo.com"\
".app.link"\
".intoday.in"\
".casalemedia.com"\
".casalemedia.com"\
".casalemedia.com"\
"www.indiatoday.in"\
"www.indiatoday.in"\
"www.indiatoday.in"\
".pubmatic.com"\
".pubmatic.com"\
".doubleclick.net"\
".indiatoday.in"\
".pubmatic.com"\
".pubmatic.com"\
".pubmatic.com"\
".pubmatic.com"\
".yahoo.com"\
".adsrvr.org"\
".simpli.fi"\
".zedo.com"\
".quantserve.com"\
".pubmatic.com"\
".pubmatic.com"\
".pubmatic.com"\
".pubmatic.com"\
".casalemedia.com"\
".mathtag.com"\
".pubmatic.com"\
".turn.com"\
".adsrvr.org"\
".quantserve.com"\
".pubmatic.com"\
".pubmatic.com"\
".owneriq.net"\
".owneriq.net"\
".pippio.com"\
".pippio.com"\
".pippio.com"\
".pippio.com"\
".rlcdn.com"\
".rlcdn.com"\
".bidswitch.net"\
".bidswitch.net"\
".bidswitch.net"\
".pubmatic.com"\
".casalemedia.com"\
".casalemedia.com"\
".naukri.com"\
".naukri.com"\
".naukri.com"\
".naukri.com"\
".naukri.com"\
".naukri.com"\
"www.naukri.com"\
".naukri.com"\
".naukri.com"\
".naukri.com"\
".naukri.com"\
".naukri.com"\
".naukri.com"\
".naukri.com"\
".facebook.com"\
".doubleclick.net"\
".imdb.com"\
".imdb.com"\
".imdb.com"\
".imdb.com"\
"www.imdb.com"\
".scorecardresearch.com"\
".scorecardresearch.com"\
".quora.com"\
".quora.com"\
".quora.com"\
".quora.com"\
".quora.com"\
".quora.com"\
".quora.com"\
".www.quora.com"\
".w3schools.com"\
".w3schools.com"\
".google.com"\
"mypage.w3schools.com"\
".w3schools.com"\
".w3schools.com"\
".casalemedia.com"\
".casalemedia.com"\
".casalemedia.com"\
".connectad.io"\
".lijit.com"\
".lijit.com"\
".smartadserver.com"\
".smartadserver.com"\
".smartadserver.com"\
".smartadserver.com"\
".smartadserver.com"\
".smartadserver.com"\
".prg.smartadserver.com"\
".youtube.com"\
".youtube.com"\
"www.who.int"\
"www.who.int"\
".who.int"\
".addthis.com"\
".twitter.com"\
".addthis.com"\
".addthis.com"\
".addthis.com"\
".addthis.com"\
".addthis.com"\
".addthis.com"\
".addthis.com"\
".doubleclick.net"\
".who.int"\
".who.int"\
".who.int"\
".addthis.com"\
".taboola.com"\
".taboola.com"\
".grammarly.com"\
".grammarly.com"\
".grammarly.com"\
".grammarly.com"\
".grammarly.com"\
".grammarly.com"\
".grammarly.com"\
".grammarly.com"\
".grammarly.com"\
".grammarly.com"\
".grammarly.com"\
".facebook.com"\
".bing.com"\
".bat.bing.com"\
".grammarly.com"\
".grammarly.com"\
".grammarly.com"\
".taboola.com"\
".linkedin.com"\
".ads.linkedin.com"\
".linkedin.com"\
".doubleclick.net"\
".linkedin.com"\
".linkedin.com"\
".linkedin.com"\
".www.linkedin.com"\
".linkedin.com"\
".twitter.com"\
".freepik.com"\
".freepik.com"\
".www.freepik.com"\
".freepik.com"\
".bing.com"\
".bat.bing.com"\
".freepik.com"\
".www.freepik.com"\
".freepik.com"\
".freepik.com"\
".freepik.com"\
".freepik.com"\
".adform.net"\
".doubleclick.net"\
".statcounter.com"\
".freepik.com"\
".freepik.com"\
".freepik.com"\
".adform.net"\
".freepik.com"\
".criteo.com"\
".facebook.com"\
".freepik.com"\
".freepik.com"\
"www.freepik.com"\
".mathtag.com"\
".freepik.com"\
".mathtag.com"\
".freepik.com"\
".freepik.com"\
".freepik.com"\
".freepik.com"\
".3lift.com"\
".twitter.com"\
".yahoo.com"\
".advertising.com"\
".smaato.net"\
".pubmatic.com"\
".pubmatic.com"\
".pubmatic.com"\
".smaato.net"\
".smaato.net"\
".revcontent.com"\
".revcontent.com"\
"sync.outbrain.com"\
".media.net"\
".media.net"\
".addthis.com"\
".addthis.com"\
".addthis.com"\
".outbrain.com"\
".outbrain.com"\
".sharethrough.com"\
".rubiconproject.com"\
".rubiconproject.com"\
".postrelease.com"\
".postrelease.com"\
".casalemedia.com"\
".casalemedia.com"\
".turn.com"\
".aws.amazon.com"\
".amazon.com"\
".aws.amazon.com"\
".amazon.com"\
".amazon.com"\
".amazon.com"\
".amazon.com"\
".amazon.com"\
".amazon.com"\
".amazon.com"\
".amazon.com"\
".amazon.com"\
".amazonwebservices.d2.sc.omtrdc.net"\
".amazon.com"\
".linkedin.com"\
".ads.linkedin.com"\
".linkedin.com"\
".linkedin.com"\
".linkedin.com"\
".linkedin.com"\
".www.linkedin.com"\
".linkedin.com"\
".amazon.com"\
".youtube.com"\
".youtube.com"\
".doubleclick.net"\
".amazon.com"\
".amazon.com"\
".taboola.com"\
"www.ndtv.com"\
"www.ndtv.com"\
".ndtv.com"\
".scorecardresearch.com"\
".scorecardresearch.com"\
".taboola.com"\
".ndtv.com"\
".lijit.com"\
".ndtv.com"\
".ndtv.com"\
".ndtv.com"\
".ndtv.com"\
"www.ndtv.com"\
"www.ndtv.com"\
".ndtv.com"\
"www.ndtv.com"\
".ndtv.com"\
".twitter.com"\
".doubleclick.net"\
".openx.net"\
".dotomi.com"\
"bh.contextweb.com"\
".pubmatic.com"\
".pubmatic.com"\
".pubmatic.com"\
".pubmatic.com"\
".pubmatic.com"\
".pubmatic.com"\
".rubiconproject.com"\
".adsrvr.org"\
".yahoo.com"\
".simpli.fi"\
".adsrvr.org"\
".quantserve.com"\
".quantserve.com"\
".pubmatic.com"\
".pubmatic.com"\
".pubmatic.com"\
".rlcdn.com"\
".pubmatic.com"\
".pubmatic.com"\
".turn.com"\
".pippio.com"\
".pippio.com"\
".pippio.com"\
".pippio.com"\
".pubmatic.com"\
".mathtag.com"\
".pubmatic.com"\
".pubmatic.com"\
".rlcdn.com"\
".rubiconproject.com"\
".rubiconproject.com"\
"eus.rubiconproject.com"


corpus = [india_no_vpn_domain, india_vpn_domains, india_local_domains]

X_train_counts = count_vect.fit_transform(corpus)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df_1 = pd.DataFrame(X_train_counts.toarray(),columns=count_vect.get_feature_names(),index=['india_no_vpn_domain', 'india_vpn_domains','india_local_domains'])

df_trans = df_1.T

#df_trans.to_html('india.html')


vectorizer = TfidfVectorizer()
trsfm=vectorizer.fit_transform(corpus)
pd.DataFrame(trsfm.toarray(),columns=vectorizer.get_feature_names(),index=['india_no_vpn_domain', 'india_vpn_domains','india_local_domains'])



df_2 = pd.DataFrame(cosine_similarity(trsfm[0:3], trsfm),index=['india_no_vpn_domain', 'india_vpn_domains','india_local_domains'], columns = ['india_no_vpn_domain', 'india_vpn_domains','india_local_domains'])

print(df_2)

list_df = [df_2, df_trans]
output = ""
for index,df in enumerate(list_df):
    output += df.to_html() + '<br>'

with open('india.html', 'w') as f:
    f.writelines(output)    
