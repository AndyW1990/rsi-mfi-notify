

##################### PACKAGE SETUP #####################
setup_env:
	pyenv virtualenv rsi_mfi_nofity
	pyenv local rsi_mfi_nofity
	mv .env_sample .env
	direnv allow .
	pip install -e . 


##################### PREPARE CONTAINER #####################
IMAGE = ${IMAGE_NAME}:${TAG}
AWS_URI = ${AWS_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com
docker_push:
	docker build --tag=$(IMAGE) .
	aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin $(AWS_URI)
	docker tag $(IMAGE) $(AWS_URI)/$(IMAGE)
	docker push $(AWS_URI)/$(IMAGE)


##################### TESTS #####################
test_vals:
	@pytest \
	tests/test.py::TestVals::test_buy \
	tests/test.py::TestVals::test_sell \
	tests/test.py::TestVals::test_do_nothing_1 \
	tests/test.py::TestVals::test_do_nothing_2 \
	tests/test.py::TestVals::test_do_nothing_3

test_email:
	@pytest \
	tests/test.py::TestEmail::test_buy