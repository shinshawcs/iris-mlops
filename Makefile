build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

train:
	docker-compose run --rm api python app/train_model.py

logs:
	docker-compose logs -f api

mlflow-ui:
	open http://localhost:5001

k8s-deploy:
	kubectl apply -f k8s/