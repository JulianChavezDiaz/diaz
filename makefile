APP_NAME=diaz
IMAGE_NAME=ghcr.io/julianchavezdiaz/diaz:1.0.5
STACK_FILE=stack.yml

build:
	docker build -t $(IMAGE_NAME) .  # ✅ Usar IMAGE_NAME

deploy:
	docker stack deploy --with-registry-auth -c $(STACK_FILE) $(APP_NAME)

logs:
	docker service logs -f $(APP_NAME)_diaz

rm:
	docker stack rm $(APP_NAME)

ps:
	docker service ls

restart:
	make rm
	sleep 5
	make build
	make deploy