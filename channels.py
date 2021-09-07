
keras_json='{\n    "floatx": "float32",\n    "epsilon": 1e-07,\n    "backend": "tensorflow",\n    "image_data_format": "channels_last"\n}'
keras_json_dir="/Users/ngc7293/.keras/keras.json"
with open(keras_json_dir, "w") as fp:
  fp.write(keras_json)