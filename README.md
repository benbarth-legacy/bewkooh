# bewkooh
An obsessively simple webhook deployer for any project

If you want to deploy directly from your git repositry then *bewkooh* is for you.

```
usage: bewkooh.py [-h] [--port PORT] [--webhookPath WEBHOOKPATH] [--command COMMAND] path
```

Automatically ```git pull``` the _my-repo_ directory at http://localhost:8080/webhook
```
> python bewkooh.py my-repo
```

or

Automatically ```git pull``` the _my-repo_ directory at http://localhost:8081/thywebhook
```
> python bewkooh.py --port=8081 --webhookPath=thywebhook my-repo
```
