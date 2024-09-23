# Metrics Agent
This project is responsible for acquiring system resources such as CPU and memory.

このプロジェクトはCPUやメモリーなどのシステムのリソース取得を行います。

## Description: 概要
This project acquires system resources and sends them to the MQTT broker.
The sense of acquisition is every 5 seconds. (*The sense of acquisition can be changed in the yaml file)

このプロジェクトはシステムのリソースを取得し、MQTTブローカーへ送信します。
取得の感覚は5秒間隔で取得します。(※取得感覚はyamlファイルで変更可能です)

## Usage: 使用方法
### Define .env file: .envファイルの準備
Create an .env file in the project directory and set the following environment variables
```
MQTT_BROKER="<MQTT Broker IP>"
MQTT_PORT="<MQTT Broker Port>"
```

## Execution: 実行方法
```
$ python main.py
```
* 必要な場合はcronなどを用いて実行する。
* If necessary, run it by cron or other means.

## Requirement
* requirements.txtを参照すること
* Please refer to requirements.txt

## Author
Tomoki.H