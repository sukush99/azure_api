crud-test:
	@echo "Running CRUD tests..."
	uv run pytest test_crud.py
	@echo "CRUD test results saved to crud_test_results.txt"

uvicorn:
	uv run uvicorn main:app 

docker-build:
	@echo "Building Docker image..."
	docker build -t sntj-api .

docker-run:
	@echo "Running Docker container..."
	docker run --env-file azure_conn.env  --publish 80:80 --name sntj-api-aws-container sntj-api