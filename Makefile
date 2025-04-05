# Running without docker
run:
	cd backend && uvicorn main:app --reload

init:
	cd backend && alembic init migrations

migrations:
	cd backend && alembic revision --autogenerate -m "Initial migration"

upgrades:
	cd backend && alembic upgrade head

downgrade:
	cd backend && alembic downgrade -1


install:
	cd backend && pip install -r requirements.txt

ps:
	docker compose ps

up:
	docker compose up -d

stop:
	docker compose stop

rm: stop
	docker compose rm -f

# Running with Docker

# Generate a new migration
migration:
	docker compose run --rm backend alembic revision --autogenerate -m "Add claim_status enum"

# Upgrade to a specific version
upgrade:
	docker compose run --rm backend alembic upgrade +1

# Downgrade if needed
downg:
	docker compose run --rm backend alembic downgrade -1

# Check migration history
history:
	docker compose run --rm backend alembic history

db:
	docker compose exec db psql -U admin -d insurance_db