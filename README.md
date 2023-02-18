# ELK-FSCrawler

## 啟動ELK

帳號預設為"elastic"，密碼預設為"changeme"，可在[.env](https://github.com/Ben950128/ELK-FSCrawler/blob/main/.env)設定elasticsearch、logstash及kibana的密碼，在此已改成"password"，並可啟動ELK。

``` console
docker compose up -d
```

## 啟動FSCrawler

輸入以下指令啟動FSCrawler。第一次啟動下面指令時，若無 ~/docker/docker-elk/.fscrawler 檔案，便會詢問是否創建，輸入Y即可。

要上傳至Elasticsearch的檔案存放的資料夾位於 ~/docker/docker-elk/tmp/docs。

為了建立FSCrawler和Elasticsearch的container之間的連線，可用 --add-host=host.docker.internal:host-gateway 指令。

fscrawler upload_files 為建立upload_files這個index的指令。

``` console
docker run -it --rm -v ~/docker/docker-elk/.fscrawler:/root/.fscrawler -v ~/docker/docker-elk/tmp/docs:/tmp/es:ro --add-host=host.docker.internal:host-gateway dadoonet/fscrawler fscrawler upload_files
```

設定[_settings.yml](https://github.com/Ben950128/ELK-FSCrawler/blob/main/.fscrawler/upload_files/_settings.yml)

* update_rate: 可調每隔幾分鐘去撈資料夾(~/docker/docker-elk/tmp/docs)內的檔案並上傳至Elasticsearch
* url: "http://host.docker.internal:9200"
* username: "elastic"
* password: "password"
* ssl_verification: false

若要調整檔案上傳後於Elasticsearch上的Mapping type，可於[_settings.json](https://github.com/Ben950128/ELK-FSCrawler/blob/main/.fscrawler/_default/8/_settings.json)進行設定。像是這裡將"filename"的"type"從"keyword"改成"text"。

若一切調整完畢，即可再次輸入下面指令進行啟動FSCrawler

``` console
docker run -it --rm -v ~/docker/docker-elk/.fscrawler:/root/.fscrawler -v ~/docker/docker-elk/tmp/docs:/tmp/es:ro --add-host=host.docker.internal:host-gateway dadoonet/fscrawler fscrawler upload_files
```

> **Warning**  
> 正常來說啟動時會出現 [f.p.e.c.f.t.TikaInstance] OCR is enabled. This might slowdown the process。
> 但第一次啟動後會在[upload_files](https://github.com/Ben950128/ELK-FSCrawler/blob/main/.fscrawler/upload_files)出現_status.json檔案，導致以後不會再進行OCR辨識，因此必須時時刻刻刪除_status.json檔案(有點怪QQ)。


## 刪除ELK

帶-v參數，順便刪除volume
``` console
docker-compose down -v
```