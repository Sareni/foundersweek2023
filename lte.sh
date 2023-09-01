#!/bin/sh

MODEM_IP="192.168.8.1"
curl -s -X GET "http://$MODEM_IP/api/webserver/SesTokInfo" > ses_tok.xml
COOKIE=`grep "SessionID=" ses_tok.xml | cut -b 10-147`
TOKEN=`grep "TokInfo" ses_tok.xml | cut -b 10-41`
CONNECT_REQ="<request><dataswitch>1</dataswitch></request>"

curl -X POST -d $CONNECT_REQ "http://$MODEM_IP/api/dialup/mobile-dataswitch" \
--cookie $COOKIE --header "__RequestVerificationToken: $TOKEN" \
--header "Content-Type: text/xml"