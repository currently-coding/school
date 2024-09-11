import json

# Example JSON data
json_data = '''[{"featured":true,"text":"house","pos":"noun","forms":[],"grammar_info":null,"audio_links":[{"url":"https://www.linguee.com/mp3/EN_US/2c/2ca63cddd54f9490efad22421891a9d1-101.mp3","lang":"American English"},{"url":"https://www.linguee.com/mp3/EN_UK/2c/2ca63cddd54f9490efad22421891a9d1-101.mp3","lang":"British English"}],"translations":[{"featured":true,"text":"Haus","pos":"noun, neuter","audio_links":[{"url":"https://www.linguee.com/mp3/DE/eb/ebacf61946ee81f386960ad2a09a147e-105.mp3","lang":"German"}],"examples":[{"src":"My house has three bedrooms and a large kitchen.","dst":"Mein Haus hat drei Schlafzimmer und eine große Küche."},{"src":"There is a yard behind the house.","dst":"Hinter dem Haus ist ein Hof."}],"usage_frequency":null},{"featured":true,"text":"Familie","pos":"noun, feminine","audio_links":[{"url":"https://www.linguee.com/mp3/DE/8a/8a5a0eae251267eb349bf9db3e09712d-104.mp3","lang":"German"}],"examples":[{"src":"The magnificent house belonged to a count and his family.","dst":"Das prachtvolle Haus gehörte einem Grafen und seiner Familie."}],"usage_frequency":null},{"featured":true,"text":"Geschlecht","pos":"noun, neuter","audio_links":[{"url":"https://www.linguee.com/mp3/DE/b3/b33509e4101693a82829fd320a7394ef-105.mp3","lang":"German"}],"examples":[],"usage_frequency":null},{"featured":false,"text":"Gebäude","pos":"noun, neuter","audio_links":[{"url":"https://www.linguee.com/mp3/DE/d5/d5c15bbee76b3d8f59d7192dd2a12526-105.mp3","lang":"German"}],"examples":[],"usage_frequency":null}]},{"featured":true,"text":"house","pos":"verb","forms":["housed","housed"],"grammar_info":null,"audio_links":[{"url":"https://www.linguee.com/mp3/EN_US/2c/2ca63cddd54f9490efad22421891a9d1-200.mp3","lang":"American English"},{"url":"https://www.linguee.com/mp3/EN_UK/2c/2ca63cddd54f9490efad22421891a9d1-200.mp3","lang":"British English"}],"translations":[{"featured":true,"text":"unterbringen","pos":"verb","audio_links":[{"url":"https://www.linguee.com/mp3/DE/82/82041c308a77b75bb117c19f31e47f87-201.mp3","lang":"German"}],"examples":[{"src":"The wedding guests were housed in a few rented cabins.","dst":"Die Hochzeitsgäste wurden in einigen gemieteten Hütten untergebracht."}],"usage_frequency":null},{"featured":false,"text":"aufnehmen","pos":"verb","audio_links":[{"url":"https://www.linguee.com/mp3/DE/13/1317ac6f7665a220b6502e3c9eee7e57-201.mp3","lang":"German"}],"examples":[],"usage_frequency":null},{"featured":false,"text":"beherbergen","pos":"verb","audio_links":[{"url":"https://www.linguee.com/mp3/DE/45/45bd8bdc125a2dbc9b16c9e14b7a7a3b-200.mp3","lang":"German"}],"examples":[],"usage_frequency":null}]},{"featured":true,"text":"House","pos":"noun, neuter","forms":[],"grammar_info":null,"audio_links":[{"url":"https://www.linguee.com/mp3/DE/ae/aebfe46795575772b7cf413e25caeab9-103.mp3","lang":"German"}],"translations":[{"featured":true,"text":"house music","pos":"noun","audio_links":[{"url":"https://www.linguee.com/mp3/EN_US/88/887d7af731b97d72d4152ed90b06667a-100.mp3","lang":"American English"},{"url":"https://www.linguee.com/mp3/EN_UK/88/887d7af731b97d72d4152ed90b06667a-100.mp3","lang":"British English"}],"examples":[],"usage_frequency":null}]}]'''

# Parse JSON data
data = json.loads(json_data)

# Extract useful information
for entry in data:
    word = entry.get('text', 'N/A')
    pos = entry.get('pos', 'N/A')
    print(f"Word: {word}")
    print(f"Part of Speech: {pos}")
    
    # Extract and print audio links
    for audio in entry.get('audio_links', []):
        print(f"Audio ({audio.get('lang', 'Unknown')}): {audio.get('url', 'No URL')}")
    
    # Extract translations
    for translation in entry.get('translations', []):
        trans_word = translation.get('text', 'N/A')
        trans_pos = translation.get('pos', 'N/A')
        print(f"  Translation: {trans_word} ({trans_pos})")
        
        # Extract and print example sentences
        for example in translation.get('examples', []):
            print(f"    Example: {example.get('src', 'No source')} -> {example.get('dst', 'No destination')}")
    
    print()

