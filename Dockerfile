# Pythonのバージョンを3.8にアップグレード
FROM python:3.8

USER root

# ロケールの設定
RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

# 必要なパッケージのインストール
RUN apt-get install -y vim less
# Tkinterのインストール
RUN apt-get install -y python3-tk
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

# JupyterLab、TensorFlow、およびPillowのインストール
RUN pip install jupyterlab
RUN pip install pandas
RUN pip install matplotlib
RUN pip install scikit-learn
# RUN pip install tensorflow
RUN pip install Pillow
RUN pip install statsmodels

# その他の必要な設定やコマンドがあればここに追加
