## robosys_kabai2
ロボットシステム学課題2
### 課題用リポジトリ
このリポジトリは、ロボットシステム学の課題で作成したものです。

## 説明

### 日時を出力するノード

#### 概要
日時を秒単位で出力するノードを提供する。

### パッケージ内容
my_package: ROS 2の日時出力ノードを含むパッケージ。

talker.py: 日時を出力するパブリッシャーノード。

### クローン方法
以下のコマンドを実行して、リポジトリをクローンしてください。
```
git clone https://github.com/ssssDaichi/robosys_kabai2.git
```
#### クローン後の作業
1.クローンしたディレクトリに移動します。
```
cd ~/ros2_ws
```
2.ビルドとセットアップ
```
colcon build
source install/setup.bash
```

## 使用方法

日時出力ノードを実行するには以下を使用してください
```
ros2 run mypkg datetime_publisher
```

### 実行例
```
[INFO] [1735457445.103320422] [datetime_publisher]: Publishing: 2024-12-29 16:30:45
[INFO] [1735457446.090982457] [datetime_publisher]: Publishing: 2024-12-29 16:30:46
[INFO] [1735457447.092086779] [datetime_publisher]: Publishing: 2024-12-29 16:30:47
[INFO] [1735457448.090799816] [datetime_publisher]: Publishing: 2024-12-29 16:30:48
[INFO] [1735457449.091110696] [datetime_publisher]: Publishing: 2024-12-29 16:30:49
[INFO] [1735457450.090897724] [datetime_publisher]: Publishing: 2024-12-29 16:30:50
[INFO] [1735457451.091282452] [datetime_publisher]: Publishing: 2024-12-29 16:30:51
[INFO] [1735457452.091590611] [datetime_publisher]: Publishing: 2024-12-29 16:30:52
```

## 動作環境
#### ソフトウェア
Python
テスト済みバージョン3.7~3.12
#### テスト環境
ubuntu 22.04 LTS
#### ライセンス
このプロジェクトは [Apache License 2.0](LICENSE) のもとで公開されています。
#### Copyright
© 2024 Daichi Hirose
