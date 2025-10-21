import os

def getEnvContent(env: str, default):
    envContent = os.getenv(f"{env}__FILE")
    if envContent is not None:
        with open(envContent) as f:
            envContent = f.read()

    return envContent or os.getenv(env, default)