# vaik-text-recognition-pb-experiment

Create json file by text recognition model. Calc Levenshtein ratio.


## Install

```shell
pip install -r requirements.txt
```

## Usage

### Create json file

```shell
python inference.py --input_saved_model_dir_path '~/.vaik_text_recognition_pb_trainer/output_model/2023-02-04-20-58-00/step-5000_batch-16_epoch-24_loss_0.3250_val_loss_0.1010' \
                --input_classes_json_path '~/vaik-text-recognition-pb-trainer/test_default_fonts_images/jpn_character.json' \
                --input_image_dir_path '~/vaik-text-recognition-pb-trainer/test_default_fonts_images/' \
                --output_json_dir_path '~/.vaik_text_recognition_pb_experiment/test_default_fonts_images_inference'
```

- input_image_dir_path
    - example

```shell
.
├── なにわ_3932.png
├── 京都_0656.png
├── 倉敷_0488.png
・・・
```

#### Output
- output_json_dir_path
    - example

```json
{
  "answer": "倉敷",
  "classes": [
    [
      0,
      1926,
      2691,
      0
    ],
    [
      0,
      1926,
      2691,
      0,
      680,
      0
    ],
    [
      0,
      1926,
      2691,
      0,
      1772,
      0
    ],
    [
      0,
      1926,
      2691,
      0,
      1076,
      0
    ],
    [
      0,
      1926,
      2691,
      0,
      977,
      0
    ],
    [
      0,
      1926,
      2691,
      0,
      2814,
      0
    ],
    [
      0,
      1926,
      2691,
      0,
      863,
      0
    ],
    [
      0,
      1926,
      2691,
      0,
      2492,
      0
    ],
    [
      0,
      1926,
      2691,
      0,
      1146,
      0
    ],
    [
      0,
      1926,
      2691,
      0,
      2801,
      0
    ]
  ],
  "image_path": "~/Github/vaik-text-recognition-pb-expriment/test_default_fonts_images/倉敷_0488.png",
  "scores": [
    0.9883286952972412,
    0.0018064073519781232,
    0.0013198809465393424,
    0.0012730812886729836,
    0.0011223482433706522,
    0.0009223314118571579,
    0.0006044754409231246,
    0.0003985347575508058,
    0.00034090629196725786,
    0.0002123780141118914
  ],
  "text": [
    "倉敷",
    "倉敷敢",
    "倉敷数",
    "倉敷故",
    "倉敷敬",
    "倉敷放",
    "倉敷教",
    "倉敷敗",
    "倉敷攻",
    "倉敷倣"
  ]
}
```
-----

### Calc ACC

```shell
python calc_levenshtein_ratio.py --input_json_dir_path '~/.vaik_text_recognition_pb_experiment/test_default_fonts_images_inference'
```

#### Output

``` text
ratio:1.0, answer:和泉, predict:和泉
ratio:1.0, answer:倉敷, predict:倉敷
ratio:1.0, answer:山形, predict:山形
ratio:1.0, answer:京都, predict:京都
ratio:0.0, answer:京都, predict:四祖
ratio:1.0, answer:大分, predict:大分
ratio:1.0, answer:室蘭, predict:室蘭
ratio:1.0, answer:嘆福, predict:嘆福
Average Ratio: 0.875
```