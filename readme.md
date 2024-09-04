# First Python


## Build image
```shell
docker rmi -f first-py:latest
docker build -t first-py --no-cache --progress=plain .
```

## Run
```shell
# 开发时退出就删除
docker rm -f first-py
docker run --name first-py --rm --env-file .env -p 8000:80 first-py:latest
```

```shell
# 生产环境
docker rm -f first-py
docker run --name first-py -d --restart=on-failure:10 --env-file .env -p 8000:80 first-py:latest
```


