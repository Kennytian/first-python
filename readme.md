# First Python

## Run
```shell
uvicorn main:app --reload --host 0.0.0.0 --port 8080
```
```shell
# 如果不加__name__，那么就执行正面的语句，quick-start 是文件名，app 是模块名
uvicorn quick-start:app --reload --host 127.0.0.1 --port 8080
```

## Development
```shell
curl http://127.0.0.1:8080
```
```shell
curl -H "access-key: s6FXdoiIxfp3uvlX" http://127.0.0.1:8080/protected
```
```shell
curl -X PUT -H "Content-Type: application/json" -H "Access-Key: s6FXdoiIxfp3uvlX" -d '{"name":"Tom","price":2.23}' http://127.0.0.1:8080/items/121
```
```shell
curl -X GET -H "Access-Key: s6FXdoiIxfp3uvlX" http://127.0.0.1:8080/items/121
```

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
