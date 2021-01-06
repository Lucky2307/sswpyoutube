# Holoinfo
_A website that keeps track of virtual YouTubers and their live streaming activities_

## Quickstart
This quickstart will help you to ready the app immediately without having to input dozens of channel manually

Install the dependencies listed in requirements.txt:
```bash
pip install -r requirements.txt
```

From here, you can use our default configurations set in .env or customize it for your own purpose.

If you're using Linux, you may want to automate the process of refreshing the video feeds and watchlist using celery. Again, you can use our configuration on .env however, if you plan on using your own choice of message broker e.g. redis, make sure that the server is online. For redis, you can check this by using:
```bash
redis-cli ping
```

After that, start your worker:
```bash
celery -A sswpyoutube beat -l INFO
```

And on a separate terminal:
```bash
$ celery -A sswpyoutube worker -l INFO
```

This will refresh the video feeds to check on any new streams (every 15 min by default) and refresh the watchlist (every 5 min by default). You can run the server with:
```bash
python manage.py runserver
```
