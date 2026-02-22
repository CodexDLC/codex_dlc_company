# 🏛️ System Architecture & Orchestration (WaaS Platform)

## 1. Overview
The **CodexDLC** platform implements the WaaS (Website as a Service) business model. The architecture is built on the **Isolated Multi-Tenancy** principle. Instead of a single monolithic database for all clients, each business receives its own isolated environment (Docker container, DB, Redis), deployed from a standardized `project-template`.

This ensures zero mutual influence between clients, maximum data security, and ease of updating or migrating a specific customer's infrastructure.

## 2. Core Nodes

### 2.1. Gateway Node (codex-dlc.com)
The main storefront and distribution gateway of the platform.
* **Stack:** Django, HTMX, PostgreSQL.
* **Functions:**
    * Presentation of services and "gateways" for various niches (Z-Pattern Landing).
    * Lead generation and primary qualification via interactive FSM forms (HTMX).
    * Admin panel (CRM module) for managing subscriptions and deployment statuses of client projects.

### 2.2. Orchestrator & Deployment Pipeline
Automated assembly factory.
* **Stack:** Bash, Python (CLI `init_project`), GitHub Actions, Docker Compose.
* **Functions:**
    * Upon receiving a new request, the `init_project` script is triggered, cloning the required branch of `project-template` (Django or FastAPI).
    * Automatic substitution of `.env` variables (DB names, bot tokens, ports).
    * Generation of Nginx configurations (via `site.conf.template`) to route the client's domain to a dedicated port.
    * Deployment of a new isolated stack (Backend, Redis, Worker, Bot) on the server.

### 2.3. Tenant Instances (Client Nodes)
Ready-to-use products for local businesses (e.g., LILY salon or OCS installers).
* **Stack:** Django/FastAPI, Redis, Celery/Arq (Workers), PostgreSQL.
* **Functions:**
    * Autonomous operation of client business logic (appointment booking, cart, surveys).
    * Own admin panel and independent database.
    * Communication with the central system (CodexDLC) via Webhooks or Redis Pub/Sub for sending telemetry (Uptime, errors).

### 2.4. Central Telegram Hub (Nervous System)
A single command center for communication and management.
* **Stack:** Aiogram 3, Redis, Webhooks.
* **Functions:**
    * Aggregation of all leads from the `Gateway Node`.
    * FSM scenarios for onboarding new clients (surveys in the bot).
    * Alert notifications from `Tenant Instances` (e.g., client container failure).

## 3. Data Flow (Subscription Creation Flow)

1.  **Lead Capture:** User leaves a request on `codex-dlc.com` (Gateway Node).
2.  **Notification:** Data is pushed to Redis Queue -> Telegram Hub notifies the Architect (you).
3.  **Provisioning:** Via CLI tool (Orchestrator), the command is executed:
    `python -m tools.init_project --type django --client "new_salon" --domain "new-salon.de"`
4.  **Deployment:** CI/CD pipeline builds Docker images, updates Nginx reverse-proxy, and issues an SSL certificate (Certbot).
5.  **Delivery:** The system sends the client the credentials for their independent instance.
