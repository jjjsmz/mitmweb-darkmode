# mitmweb-darkmode

mitmweb の UI をダークモードにする mitmproxy addon。

```sh
mitmweb -s darkmode.py
```

常用するなら `~/.mitmproxy/config.yaml` に:

```yaml
scripts:
  - /path/to/mitmweb-darkmode/darkmode.py
```
