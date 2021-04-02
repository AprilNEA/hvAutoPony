<p align="center">
  <a href="https://github.com/GreenSulley/AutoPony">
    <img src="https://cdn.jsdelivr.net/npm/autopony@1.0.0/medal.webp" alt="banner">
  </a>
</p>

<div align="center">

# AutoPony Pure 
_Automated RidderMaster based on [TensorFlow](https://github.com/tensorflow/tensorflow)
 & [OpenCV](https://github.com/opencv/opencv-python)_

_基于 [TensorFlow](https://github.com/tensorflow/tensorflow) 和 [OpenCV](https://github.com/opencv/opencv-python) 实现的全自动化解御迷士小马谜题_

<p align="center">

![GitHub](https://img.shields.io/github/license/GreenSulley/AutoPony)
![](https://img.shields.io/github/v/release/GreenSulley/AutoPony?color=blueviolet&include_prereleases)
![GitHub last commit](https://img.shields.io/github/last-commit/GreenSulley/AutoPony)
![GitHub Repo stars](https://img.shields.io/github/stars/GreenSulley/AutoPony?style=social)
</div>




## Pure Version eatures
- [x] RestFul API base on [FastAPI](https://github.com/tiangolo/fastapi)
- [x] Check UID to determine whether the user is allowed to use
- [ ] Database optimization _(no database in this version)_
- [x] Enhanced verification, Prevent uid spoofing by verifying the image url
- [ ] One-click UserScript generation _(no need, just use `user.js`)_
- [ ] Exclusive test site for ignoring check codes

## Demo
![Demo](https://cdn.jsdelivr.net/npm/autopony@1.0.0/demo.gif)

## Install 

### Binary installation
```bash

./model/tensorflow_model_server --port=8500 --rest_api_port=8501 --model_base_path=/tmp/mounted_model/ --tensorflow_session_parallelism=0 --file_system_poll_wait_seconds=31540000'
```

### Docker Install
Need: Docker Community Edition
```bash
sudo docker pull ${gcr.io/cloud-devrel-public-resources/gcloud-container-1.14.0:latest}
docker run --rm --name autopony -p 8501:8501 -v ${YOUR_MODEL_FULLPATH}:/tmp/mounted_model/model -t gcr.io/cloud-devrel-public-resources/gcloud-container-1.14.0:latest
```

./model/tensorflow_model_server --port=8500 --rest_api_port=8501 --model_base_path=/Users/Grandmasters/Github/autoPony-S --tensorflow_session_parallelism=0 --file_system_poll_wait_seconds=31540000
