FROM metacall/cli

RUN mkdir /app

WORKDIR /app

COPY . .

RUN metacall pip3 install -r requirements.txt

EXPOSE 3051

ENTRYPOINT metacall server.py && cat /root/metacall.log
