APP_NAME=multimodal_rag
IMAGE_NAME=multimodal_rag:latest

.PHONY: build run test clean

# Build docker image
build:
	docker build -t $(IMAGE_NAME) .

# Run container (requires OPENAI_API_KEY env var)
run:
	docker run --rm -it \
		-e OPENAI_API_KEY=$$OPENAI_API_KEY \
		$(IMAGE_NAME)

# Run tests inside container
test:
	docker run --rm -it \
		-e OPENAI_API_KEY=$$OPENAI_API_KEY \
		$(IMAGE_NAME) pytest tests/


# Clean up local cache and docker image
clean:
	docker rmi -f $(IMAGE_NAME) || true
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +

# Run FastAPI service
serve:
	docker run --rm -it \
		-p 8000:8000 \
		-e OPENAI_API_KEY=$$OPENAI_API_KEY \
		$(IMAGE_NAME)
