FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml uv.lock ./
COPY README.md ./
COPY src/ ./src/
COPY tests/ ./tests/
COPY pages/ ./pages/

RUN uv sync --locked

RUN uv run playwright install --with-deps chromium

CMD ["uv", "run", "pytest", "-v", "--html=reports/report.html", "--self-contained-html", "--alluredir=allure-results"]
