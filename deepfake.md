手法まとめ

- LoRA作成
  - できれば顔だけのほうが安定しやすい
  - 変なノイズが入るときは過学習。重みを下げるか回数を下げて学習させる。
  - 画質の良さはあまり関係なし。それよりはタグ付け
- LoRA適用
  - 本人の体系を反映させる。slender, lankyなどを入れると顔も痩せたりする。違和感がある場合は痩せさせる
  - どうしても似ない場合は、あきらめてFaceSwapで対応する。
- ADetail
  - 顔のディテールを挙げるため、元のプロンプトと同じプロンプトを適用すると安定しやすい
 
## 今のところのベスト
- LoRA＋ADetailで2回適用させて安定化
- FaceSwapを行い本人の顔にする。（写真は吟味して選ぶ）
- ControlNetのline artでポーズ決める。openposeやcannyは使わない
- 最後にGFPGANで画質上げる。

## 1枚法
本人が移った写真を用意
ControlNetのline artで画像を指定。normalmapとかのほうがいいかも？
FaceSwapにも同じ画像を指定。
あとは適当なプロンプトを指定すれば、その格好になる。controlnetのopenposeとsegmentationとかのほうがいいか？

## LoRa
学習の強さによっては荒れるのでパラメータを調整する

とりあえずchillout用
1girl,(RAW photo, best quality), (realistic, photo-realistic:1.4), masterpiece, an extremely delicate and beautiful, extremely detailed, 2k wallpaper, Amazing, finely detail, extremely detailed CG unity 8k wallpaper, ultra-detailed, highres, soft light, beautiful detailed girl, extremely detailed eyes and face, beautiful detailed nose, beautiful detailed eyes,cinematic lighting,perfect anatomy,slender body
(ここに服装)
(顔のLora)


## SDXL
chikaはうまくいったが、それ以外は思ったより微妙
parted bangs, collection of pose, hyper detailed face, nsfw, cute, light smile, 30 years old, slender, bent over, cleavage, 
1girl,(RAW photo, best quality), (realistic, photo-realistic:1.4), masterpiece, small breasts, upper body, navel, decorated lingerie,
Create an image of a girl in a changing room, partially dressed as he switches from formal wear to casual attire. The scene should show him in the act of changing his shirt, with various clothing items like suits, shirts, and shoes neatly arranged around him. The changing room should have mirrors and a bench, portraying a tidy and private space. The girl should appear focused and relaxed, reflecting a routine moment in a realistic setting

## IP-Adaptor face 
demoサイトより出来が悪い。モデルのせい？　原因不明 とりあえず photo realisticと入れればよさそう
extensionとloraを設定。weightを下げると表情変わる。

IP-Adapter と　line art を組み合わせると安定する、normalmapのほうがより柔軟化も
リアルなものが出たやつ。
thin hair, smile, nipples, realistic skin, hyper detailed eye, nose, mouth,
1girl, narrow waist, white background

## other
deepswap並みの速度が出ない　ローカルでグラボ使うほうが早いらしい。

## digenAi
アバター挙げたが学習で数日かかるらしい？

## supertone shift
簡単に学習できるため素晴らしい。





 
