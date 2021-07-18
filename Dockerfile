# Kampret USERBOT
FROM jokokendil/ambohju1:buster

#
# Kampret
#
RUN git clone -b Kaisar-userbot https://github.com/MrRih/Kampret-Userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/kenkansaja/Kaisar-userbot/Kaisar-userbot/requirements.txt

EXPOSE 443 80

CMD ["python3","-m","userbot"]
