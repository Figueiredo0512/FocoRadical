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
            city_state = card.select_one('.icon-text-card .fa-map-marker-alt').find_all('span')
            city = city_state[0].get_text(strip=True) if city_state else ''
            state = city_state[1].get_text(strip=True) if len(city_state) > 1 else ''
        except AttributeError:
            city, state = '', ''
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

    # Salva como JSON
    with open('eventos_foco.json', 'w', encoding='utf-8') as f:
        json.dump(events, f, indent=2, ensure_ascii=False)

    print(f'Processados {len(events)} eventos com sucesso!')

if __name__ == "__main__":
    with open('pagina_capturada.html', encoding='utf-8') as f:
        html = f.read()
    processar_eventos(html)