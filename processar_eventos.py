from bs4 import BeautifulSoup
import json
import csv

def processar_eventos(html):
    soup = BeautifulSoup(html, 'html.parser')
    events = []

    for card in soup.select('div.event-card-fc'):
        try:
            name = card.select_one('h3.event-title-fc').get_text(strip=True)
        except AttributeError:
            name = ''
        try:
            category = card.select_one('.left-card-column .icon-text-card:nth-of-type(1) .event-text-fc').get_text(strip=True)
        except AttributeError:
            category = ''
        try:
            icon = card.find('i', class_='fa-map-marker-alt')
            if icon:
                loc_block = icon.find_parent('div', class_='icon-text-card')
                city = loc_block.select_one('.event-city-fc').get_text(strip=True)
        except AttributeError:
            city = ''

        try:
            state = card.select_one('.event-state-fc').get_text(strip=True)
        except AttributeError:
            state = ''
        try:
            date = card.select_one('.right-card-column .icon-text-card:last-of-type .event-text-fc').get_text(strip=True)
        except AttributeError:
            date = ''
        oficial = bool(card.select_one('span.event-badge-fc'))
        photographers = 0

        # modal associated by ID:
        try:
            card_id = card.find('a', id=lambda i: i and i.startswith('link-event-')).get('id')
            modal = soup.select_one(f'div.modal-schedule#view-event-modal-{card_id.split("-")[-1]}')
            if modal:
                import re
                m = re.search(r'Fotógrafos:\s*(\d+)', modal.get_text())
                if m:
                    photographers = int(m.group(1))
        except Exception:
            photographers = 0

        events.append({
            'nome': name,
            'categoria': category,
            'cidade': city,
            'estado': state,
            'data': date,
            'oficial': oficial,
            'fotografos': photographers
        })

    if not events:
        print("Nenhum evento encontrado! Verifique o seletor ou o HTML.")
        return

    # Salva como CSV
    with open('eventos_foco.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=events[0].keys())
        writer.writeheader()
        writer.writerows(events)
        print("Criado arquivo .CSV!")

    # Salva como JSON
    with open('eventos_foco.json', 'w', encoding='utf-8') as f:
        json.dump(events, f, indent=2, ensure_ascii=False)
        print("Criado arquivo .json!")
            # Aqui dispara o envio de mensagem
    import subprocess
    try:
        subprocess.run(["python3", "mensagem.py"], check=True)
        print("mensagem.py executado com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar mensagem.py: {e}")

    print(f'Processados {len(events)} eventos com sucesso!')

if __name__ == "__main__":
    with open('pagina_capturada.html', encoding='utf-8') as f:
        html = f.read()
    
