# Loxala Task - Cocktails API

A FastAPI-based REST API for cocktails.

## Fly.io App & Database Setup

1. **Create the Fly.io apps for the application:**
   ```bash
   # Create production app
   flyctl apps create loxala-task-cocktails
   
   # Create development app
   flyctl apps create loxala-task-cocktails-dev
   ```

2. **Create the managed Postgres instance:**
   ```bash
   flyctl postgres create -n loxala-task-db
   ```
   > **Note:** During the creation process, you will be prompted to select a region and database type. We selected the development type of database for this setup.

3. **Get Fly.io API Token:**
     - Go to [Fly.io Dashboard](https://fly.io/dashboard)
     - Click on your profile picture in the top right
     - Select "Organization Tokens"
     - Give it a name (e.g., "GitHub Actions")
     - Copy the token immediately (you won't be able to see it again)
   

4. **Add Fly.io Token to GitHub Secrets:**
   - Go to your GitHub repository
   - Click on "Settings"
   - Click on "Secrets and variables" → "Actions"
   - Click "New repository secret"
   - Name: `FLY_API_TOKEN`
   - Value: Paste the token from step 3

5. **Create a GitHub Personal Access Token:**
   - Go to GitHub → Settings → Developer Settings → Personal Access Tokens → Tokens (classic)
   - Click "Generate new token"
   - Give it a name (e.g., "Fly.io Integration")
   - Select scopes: `repo` and `workflow`
   - Click "Generate token"
   - Copy the token immediately (you won't be able to see it again)

6. **Add GitHub Token to Fly.io:**
   ```bash
   # Add GitHub token as a secret to your Fly.io app
   flyctl secrets set GITHUB_TOKEN=your_github_token -a your-app-name
   ```

## PostgreSQL Setup

1. **Setup database connection - run proxy:**
   ```bash
   # Make sure you are logged in to Fly.io
   flyctl auth login

   # Start the proxy in a separate terminal
   flyctl proxy 5432:5432 -a loxala-task-db

   Keep this terminal running while performing database operations.

### Create Dev and Prod Environments with Separate User Roles
2. **Create a development database and user:**
   ```sql
   CREATE DATABASE loxala_task_dev;
   CREATE USER dev_user WITH PASSWORD '<db_pass>';
   GRANT ALL PRIVILEGES ON DATABASE loxala_task_dev TO dev_user;
   ```

3. **Create a production database and user:**
   ```sql
   CREATE DATABASE loxala_task_prod;
   CREATE USER prod_user WITH PASSWORD '<db_pass>';
   GRANT ALL PRIVILEGES ON DATABASE loxala_task_prod TO prod_user;
   ```

4. **Create the cocktails table(+schema) in both databases:**
   ```sql
   CREATE SCHEMA loxala_task; 
   ALTER ROLE dev_user SET search_path TO loxala_task;
   CREATE TABLE cocktails (
       id SERIAL PRIMARY KEY,
       name VARCHAR UNIQUE NOT NULL,
       description TEXT,
       ingredients TEXT,
       instructions TEXT
   );
   CREATE INDEX ix_cocktails_name ON cocktails(name);
   ```

5. **Seed the databases with initial data:**
   Export DATABASE_URL=<ENV_URL>
   The `data/seed.py` script will populate both databases with initial cocktail data.
   
6. **Set Database URL as Secret:**
   ```bash
   # For production
   flyctl secrets set DATABASE_URL="postgresql://prod_user:<password>@loxala-task-db.flycast:5432/loxala_task_prod" -a loxala-task-cocktails

   # For development
   flyctl secrets set DATABASE_URL="postgresql://dev_user:<password>@loxala-task-db.flycast:5432/loxala_task_dev" -a loxala-task-cocktails-dev
   ```

Continue with the rest of the setup as described below.

## Local Development Setup

1. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run PostgreSQl local - docker container:
```bash
docker-compose up
```

4. Seed data for local developement:
```bash
python `data/seed.py`
```

5. Run application for local developement:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the application is running, you can access:
- Swagger UI documentation: `http://localhost:8000/docs`


## Testing

Run tests with:
```bash
pytest
```

## Deployment Strategy

The application uses different environments based on the branch:
- `main` branch → Production environment (`loxala-task-cocktails`)
- `development` branch → Development environment (`loxala-task-cocktails-dev`)

The deployment is handled by GitHub Actions workflow which:
1. Runs tests
2. Builds Docker image
3. Pushes to GitHub Container Registry
4. Deploys to the appropriate Fly.io environment

### Manual Deployment

To deploy manually:
```bash
# For production
flyctl deploy -a loxala-task-cocktails --config fly.toml 

# For development
flyctl deploy -a loxala-task-cocktails-dev --config fly.dev.toml 

#Note: image and tag are defined in toml files
```

## API Endpoints

- `GET /api/v1/cocktails` - List all cocktails
- `POST /api/v1/cocktails` - Create a new cocktail
- `GET /api/v1/cocktails/{id}` - Get a specific cocktail
- `PUT /api/v1/cocktails/{id}` - Update a cocktail
- `DELETE /api/v1/cocktails/{id}` - Delete a cocktail 

## App URLs
- PROD: https://loxala-task-cocktails.fly.dev/
- DEV: https://loxala-task-cocktails-dev.fly.dev/