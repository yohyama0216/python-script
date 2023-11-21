# python-script



## 一覧
### 画像、動画ファイル系
#### ファイルを拡張仕事に分類
* moveImage.py
  * beforeに入っているfileを形式とmetadataで分類するスクリプト

画像のリサイズ

### 画像生成
#### Stable Diffusion
Stable Diffusion Web UI
#### LoRA作成
kohya

#### 顔の入れ替え
todo inswapper.py

### 画質向上
CodeFormer
顔に特化したもの。

### sample.py
動作確認用。

### データ分析系
#### 可視化


#### 回帰
* random_forest.py ランダムフォレストのサンプル。
* deep_learning.py ディープラーニング用のサンプル

# 逆引きPythonメモ
## 画像系
だいたい以下の使えばOK
OpenCV: OpenCVは、画像処理およびコンピュータビジョンのための強力なライブラリで、画像のリサイズ、フィルタリング、シャープニング、コントラスト調整、ノイズ除去などの操作を行うことができます。
PIL (Pillow): Python Imaging Library（PIL）またはそのフォークであるPillowは、画像の開閉、変換、リサイズ、エンハンスメントなどのためのツールを提供します。

### 画質を上げたい
Codeformerがよさげ

### 顔の表情を変える
Dlibで出来るようだが、調査必要

### 髪型、顔の年齢を変える
GAN？調査必要

### 顔の入れ替え
insightface

## 動画
### 動画から画像取得
ffmpeg

### 字幕を入れる
MoviePy

## ファイル編集
### ofice編集
PyPDF
Python-docx
python-pptx

### 3DCG
基本的にソフトに付属したPython拡張を利用

### 


## データ系
### グラフ、可視化
Matplotlib

### 回帰、分類
scikit-learn

### Deeplearning
Tensorflow, kelas

## マウス、キーボード操作
pyautogui: pyautoguiは、キーボードとマウスの操作を自動化するためのPythonライブラリです。マウスのクリック、ドラッグ、カーソルの移動などを制御できます。
selenium: SeleniumはWebブラウザの自動化ツールであり、Webページ上でのマウスクリックやドラッグをシミュレートするために使用できます。特にWebテストやWebスクレイピングに便利です。
pyinput: pyinputは、マウスとキーボードの操作を自動化するためのライブラリで、クリック、ドラッグ、キー入力などを実行できます。
keyboard: keyboardライブラリは、キーボードの入力を自動化するためのライブラリですが、マウスのクリックとドラッグも制御できます。
pygetwindow: pygetwindowは、ウィンドウとデスクトップの情報を取得し、特定のウィンドウ上でのマウス操作を制御するためのライブラリです

## Webサイト関連
### CMS
Django CMS: Django CMSは、PythonのWebフレームワークであるDjangoをベースにしたCMSです。Djangoを使用してカスタマイズ可能なウェブサイトを簡単に構築できます。

Wagtail: Wagtailは、PythonのDjangoフレームワークをベースにしたオープンソースのCMSです。シンプルで使いやすく、カスタマイズが容易です。

Mezzanine: Mezzanineは、DjangoベースのCMSで、ブログ、ページ、フォーラムなどのコンテンツを管理できます。多くのプラグインとカスタマイズオプションがあります。

Plone: Ploneは、Pythonで開発されたオープンソースのCMSで、堅牢なセキュリティと豊富な機能を提供します。企業向けの大規模なウェブプロジェクトに適しています。

FeinCMS: FeinCMSは、DjangoをベースにしたCMSフレームワークで、カスタマイズ可能なコンテンツブロックを使用してページを構築できます。


## パズル
Pythonで様々な種類のパズルを作成するためのライブラリやツールはたくさんあります。以下はいくつかの例です。

Pygame: Pygameは2Dゲームやパズルを作成するためのPythonライブラリで、グラフィックスやサウンドの処理を簡単に行うことができます。

PyPuzzle: PyPuzzleは、画像パズルを生成するためのライブラリで、画像を分割してシャッフルし、元の画像を復元するゲームを作成できます。

Crossword Puzzle Generator: クロスワードパズルを生成するためのPythonツールです。カスタムのクロスワードを作成することができます。

Sudoku Solver and Generator: 数独ゲームのソルバーとジェネレーターを作成するためのライブラリやコードサンプルが多数存在します。

Word Search Generator: 単語検索パズルを生成するためのPythonコードやライブラリも利用可能です。

Cryptogram Solver and Generator: 暗号パズルを生成し、解くためのツールもPythonで実装できます。

これらのライブラリやツールを使用することで、さまざまな種類のパズルゲームを作成できます。また、それぞれのプロジェクトには詳細なドキュメンテーションやサンプルコードが提供されていることが多いため、簡単に始めることができます。
### クロスワード


### 数独


### ピクロス


### 迷路


## 作曲
作曲に関連するPythonのライブラリを教えて

ChatGPT
Pythonを使用して作曲や音楽生成を行うために、いくつかの音楽関連ライブラリやツールが利用可能です。以下は、作曲に関連するPythonのライブラリやフレームワークの一部です。

MIDIUtil: MIDIUtilはPythonのライブラリで、MIDIファイルを生成するためのツールを提供します。音符、和音、リズムなどを指定して楽曲を作成できます。

FluidSynth-PyWrapper: FluidSynth-PyWrapperは、FluidSynthソフトウェアシンセサイザーをPythonでラップしたもので、PythonからMIDIデータを生成してサウンドを生成できます。

music21: music21は、音楽理論をサポートするPythonライブラリで、楽譜の作成、解析、操作が可能です。作曲の補助や音楽教育に使用できます。

PyDub: PyDubは音声処理ライブラリで、音声ファイルを操作し、合成するためのツールを提供します。音楽のサンプルやエフェクトを組み合わせて音楽を生成するのに役立ちます。

Csound: Csoundは、高度な音楽合成と信号処理のためのオープンソースの音楽プログラミング言語およびフレームワークです。PythonからCsoundを制御するためのラッパーが提供されています。

## ゲーム
Pygame: Pygameは、2Dゲーム開発のための非常に人気のあるライブラリです。ゲームループ、グラフィックス、サウンド、入力などの基本的なゲーム機能をサポートしています。

Godot Engine: Godot Engineは、2Dおよび3Dゲームを開発するためのオープンソースのゲームエンジンです。Pythonスクリプトを使用してゲームロジックを記述できます。

Panda3D: Panda3Dは、Pythonを使用して3Dゲームを開発するためのオープンソースのゲームエンジンです。高度な3Dグラフィックスと物理エンジンを備えています。

Ren'Py: Ren'Pyは、ビジュアルノベルやアドベンチャーゲームを作成するための専用のエンジンで、スクリプト言語としてPythonを使用します。

Arcade: Arcadeは、Pythonで2Dゲームを開発するためのシンプルで直感的なライブラリです。Pygameと同様に、ゲームのエンジンやフレームワークとして使用できます。

## 金融など
backtrader: backtraderは、Pythonでのトレード戦略のバックテストとライブトレーディングをサポートする強力なライブラリです。カスタムのトレード戦略を実装し、過去の市場データを使用して戦略を評価できます。多くのデータフィードやインジケータをサポートしており、FXの取引戦略のシミュレーションに適しています。

MetaTrader 4（MT4）: MetaTrader 4は、人気のある外国為替取引プラットフォームで、Pythonを統合するためのAPIが提供されています。MT4を使用して取引シミュレーションを行い、Pythonを使用して取引ロジックをカスタマイズすることができます。

Zipline: Ziplineは、アルゴリズム取引のバックテストと実行を行うためのオープンソースのPythonライブラリです。独自のデータフィードを作成し、カスタムの取引アルゴリズムをテストできます。

ccxt: ccxt（Cryptocurrency Exchange Trading Library）は、仮想通貨取引所とのインターフェースを提供するPythonライブラリです。外国為替市場ではなく、仮想通貨取引所を対象としていますが、外国為替市場と同様の原則が適用される場合があります。

