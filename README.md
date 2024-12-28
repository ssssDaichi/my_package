## robosys_kabai2
### 概要
このプロジェクトは、ROS 2を使用した日時出力ノードのサンプルプログラムを含むパッケージです。日時を秒単位で出力するノードを提供し、ROS 2の基本的なパブリッシャーの使い方を学ぶことを目的としています。
### パッケージ内容
my_package: ROS 2の日時出力ノードを含むパッケージ。
talker.py: 日時を出力するパブリッシャーノード。
### セットアップ
ROS 2環境がインストールされていることを確認してください。
リポジトリをクローンします
```
git clone https://github.com/ssssDaichi/robosys_kabai2.git
cd robosys_kabai2
```
ビルドとセットアップ
```
colcon build
source install/setup.bash
```
### 使用方法
日時出力ノードを実行するには以下を使用してください
```
ros2 run mypkg datetime_publisher
```
### ライセンス
このプロジェクトは [Apache License 2.0](LICENSE) のもとで公開されています。
