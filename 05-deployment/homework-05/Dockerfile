FROM agrigorev/zoomcamp-model:2025

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Add the virtual environment's bin directory to the PATH so Python tools work globally
ENV PATH="/code/.venv/bin:$PATH"

# Put the files with dependencies for uv to install them
COPY ".python-version" "pyproject.toml" "uv.lock" "./"

# Install dependencies exactly as locked in uv.lock, without updating them
RUN uv sync --locked

COPY "predict.py" "./"

EXPOSE 9696

ENTRYPOINT ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "9696"]
