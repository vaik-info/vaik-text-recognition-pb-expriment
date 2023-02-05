import argparse
import os
import glob
import json

from vaik_text_recognition_pb_inference.pb_model import PbModel
from PIL import Image
import numpy as np


def main(input_saved_model_dir_path, input_classes_json_path, input_image_dir_path, output_json_dir_path, batch_size, top_path, beam_width):
    os.makedirs(output_json_dir_path, exist_ok=True)
    classes = PbModel.char_json_read(input_classes_json_path)
    model = PbModel(input_saved_model_dir_path, classes, top_paths=top_path, beam_width=beam_width)

    types = ('*.jpg', '*.jpeg', '*.png', '*.JPG', '*.JPEG', '*.PNG')
    image_path_list = []
    for files in types:
        image_path_list.extend(glob.glob(os.path.join(input_image_dir_path, '**', files), recursive=True))
    image_list = []
    for image_path in image_path_list:
        image = np.asarray(Image.open(image_path).convert('RGB'))
        image_list.append(image)

    output, raw_pred = model.inference(image_list[:1], batch_size=1)

    import time
    start = time.time()
    output, raw_pred = model.inference(image_list, batch_size=batch_size)
    end = time.time()

    for image_path, output_elem in zip(image_path_list, output):
        output_json_path = os.path.join(output_json_dir_path, os.path.splitext(os.path.basename(image_path))[0]+'.json')
        output_elem['answer'] = os.path.basename(image_path).split('_')[0]
        output_elem['image_path'] = image_path
        with open(output_json_path, 'w') as f:
            json.dump(output_elem, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
    print(f'{len(image_list) / (end - start)}[images/sec]')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='inference')
    parser.add_argument('--input_saved_model_dir_path', type=str,
                        default='/home/kentaro/.vaik_text_recognition_pb_trainer/output_model/2023-02-05-14-37-56/step-5000_batch-16_epoch-8_loss_2.5069_val_loss_1.3024')
    parser.add_argument('--input_classes_json_path', type=str,
                        default=os.path.join(os.path.dirname(__file__), 'test_default_fonts_images/jpn_character.json'))
    parser.add_argument('--input_image_dir_path', type=str,
                        default=os.path.join(os.path.dirname(__file__), 'test_default_fonts_images'))
    parser.add_argument('--output_json_dir_path', type=str,
                        default='~/.vaik_text_recognition_pb_experiment/test_default_fonts_images_inference')
    parser.add_argument('--batch_size', type=int, default=4)
    parser.add_argument('--top_path', type=int, default=1)
    parser.add_argument('--beam_width', type=int, default=1)
    args = parser.parse_args()

    args.input_saved_model_dir_path = os.path.expanduser(args.input_saved_model_dir_path)
    args.input_classes_json_path = os.path.expanduser(args.input_classes_json_path)
    args.input_image_dir_path = os.path.expanduser(args.input_image_dir_path)
    args.output_json_dir_path = os.path.expanduser(args.output_json_dir_path)

    main(**args.__dict__)
