FROM python:3.11-slim

WORKDIR /app

# 直接安裝，不使用 poetry 的鎖定檢查
RUN pip install poetry

# 只複製零件清單
COPY pyproject.toml ./

# 強制安裝，不理會任何鎖定檔
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

COPY . .

CMD ["python", "main.py"]