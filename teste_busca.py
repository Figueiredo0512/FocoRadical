import os
import requests
import time

token = os.getenv("GITHUB_TOKEN")
if not token:
    print("❌ GITHUB_TOKEN não encontrado. Exporte a variável de ambiente primeiro.")
    exit(1)

owner = "Figueiredo0512"
repo  = "FocoRadical"
paths = ["eventos_foco.csv", "eventos_foco.json"]

headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3.raw"
}

for path in paths:
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    print(f"\n🔗 Baixando {path}…")
    resp = requests.get(url, headers=headers)
    print("→ Status code:", resp.status_code)

    if resp.status_code == 403 and resp.headers.get("X-RateLimit-Remaining") == "0":
        reset_ts = int(resp.headers["X-RateLimit-Reset"])
        wait_secs = reset_ts - time.time() + 5
        print(f"🔒 Rate limit atingido. Esperando {int(wait_secs)}s…")
        time.sleep(wait_secs)
        resp = requests.get(url, headers=headers)
        print("→ Novo status code:", resp.status_code)

    resp.raise_for_status()

    data = resp.text
    # mostra as 5 primeiras linhas pra validar conteúdo
    lines = data.splitlines()
    preview = "\n".join(lines[:5])
    print(f"📄 Preview de {path}:\n{preview}")
