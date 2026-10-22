import json
from django.shortcuts import render
from django.conf import settings

def home(request):
    lang = request.GET.get('lang', 'it')
    if lang not in ['it', 'de', 'en']:
        lang = 'it'
    
    with open(settings.BASE_DIR / 'traduzioni.json', 'r', encoding='utf-8') as f:
        translations = json.load(f)
    
    context = {
        'lang': lang,
        'title': translations['title'][0] if lang == 'it' else translations['title'][1] if lang == 'de' else translations['title'][2],
        'header_title': translations['header_title'][0] if lang == 'it' else translations['header_title'][1] if lang == 'de' else translations['header_title'][2],
        'intro_title': translations['intro_title'][0] if lang == 'it' else translations['intro_title'][1] if lang == 'de' else translations['intro_title'][2],
        'intro_text_1': translations['intro_text_1'][0] if lang == 'it' else translations['intro_text_1'][1] if lang == 'de' else translations['intro_text_1'][2],
        'intro_text_2': translations['intro_text_2'][0] if lang == 'it' else translations['intro_text_2'][1] if lang == 'de' else translations['intro_text_2'][2],
        'intro_text_3': translations['intro_text_3'][0] if lang == 'it' else translations['intro_text_3'][1] if lang == 'de' else translations['intro_text_3'][2],
        'intro_text_4': translations['intro_text_4'][0] if lang == 'it' else translations['intro_text_4'][1] if lang == 'de' else translations['intro_text_4'][2],
        'intro_text_5': translations['intro_text_5'][0] if lang == 'it' else translations['intro_text_5'][1] if lang == 'de' else translations['intro_text_5'][2],
        'header_image_alt': translations['header_image_alt'][0] if lang == 'it' else translations['header_image_alt'][1] if lang == 'de' else translations['header_image_alt'][2],
        'nav_presentazione': translations['nav_presentazione'][0] if lang == 'it' else translations['nav_presentazione'][1] if lang == 'de' else translations['nav_presentazione'][2],
        'nav_consulenza': translations['nav_consulenza'][0] if lang == 'it' else translations['nav_consulenza'][1] if lang == 'de' else translations['nav_consulenza'][2],
        'nav_gestione': translations['nav_gestione'][0] if lang == 'it' else translations['nav_gestione'][1] if lang == 'de' else translations['nav_gestione'][2],
        'nav_consulenza_proprietari': translations['nav_consulenza_proprietari'][0] if lang == 'it' else translations['nav_consulenza_proprietari'][1] if lang == 'de' else translations['nav_consulenza_proprietari'][2],
        'nav_contatti': translations['nav_contatti'][0] if lang == 'it' else translations['nav_contatti'][1] if lang == 'de' else translations['nav_contatti'][2],
        'section_presentazione': translations['section_presentazione'][0] if lang == 'it' else translations['section_presentazione'][1] if lang == 'de' else translations['section_presentazione'][2],
        'profile_image_alt': translations['profile_image_alt'][0] if lang == 'it' else translations['profile_image_alt'][1] if lang == 'de' else translations['profile_image_alt'][2],
        'section_presentazione_text': translations['section_presentazione_text'][0] if lang == 'it' else translations['section_presentazione_text'][1] if lang == 'de' else translations['section_presentazione_text'][2],
        'section_consulenza': translations['section_consulenza'][0] if lang == 'it' else translations['section_consulenza'][1] if lang == 'de' else translations['section_consulenza'][2],
        'property_image_alt': translations['property_image_alt'][0] if lang == 'it' else translations['property_image_alt'][1] if lang == 'de' else translations['property_image_alt'][2],
        'section_consulenza_text': translations['section_consulenza_text'][0] if lang == 'it' else translations['section_consulenza_text'][1] if lang == 'de' else translations['section_consulenza_text'][2],
        'section_gestione': translations['section_gestione'][0] if lang == 'it' else translations['section_gestione'][1] if lang == 'de' else translations['section_gestione'][2],
        'section_gestione_list_1': translations['section_gestione_list_1'][0] if lang == 'it' else translations['section_gestione_list_1'][1] if lang == 'de' else translations['section_gestione_list_1'][2],
        'section_gestione_list_2': translations['section_gestione_list_2'][0] if lang == 'it' else translations['section_gestione_list_2'][1] if lang == 'de' else translations['section_gestione_list_2'][2],
        'section_gestione_list_3': translations['section_gestione_list_3'][0] if lang == 'it' else translations['section_gestione_list_3'][1] if lang == 'de' else translations['section_gestione_list_3'][2],
        'section_gestione_list_4': translations['section_gestione_list_4'][0] if lang == 'it' else translations['section_gestione_list_4'][1] if lang == 'de' else translations['section_gestione_list_4'][2],
        'section_gestione_list_5': translations['section_gestione_list_5'][0] if lang == 'it' else translations['section_gestione_list_5'][1] if lang == 'de' else translations['section_gestione_list_5'][2],
        'section_gestione_list_6': translations['section_gestione_list_6'][0] if lang == 'it' else translations['section_gestione_list_6'][1] if lang == 'de' else translations['section_gestione_list_6'][2],
        'section_consulenza_proprietari': translations['section_consulenza_proprietari'][0] if lang == 'it' else translations['section_consulenza_proprietari'][1] if lang == 'de' else translations['section_consulenza_proprietari'][2],
        'section_consulenza_proprietari_text': translations['section_consulenza_proprietari_text'][0] if lang == 'it' else translations['section_consulenza_proprietari_text'][1] if lang == 'de' else translations['section_consulenza_proprietari_text'][2],
        'section_contatti': translations['section_contatti'][0] if lang == 'it' else translations['section_contatti'][1] if lang == 'de' else translations['section_contatti'][2],
        'email': translations['email'][0] if lang == 'it' else translations['email'][1] if lang == 'de' else translations['email'][2],
        'phone': translations['phone'][0] if lang == 'it' else translations['phone'][1] if lang == 'de' else translations['phone'][2],
        'legal_info': translations['legal_info'][0] if lang == 'it' else translations['legal_info'][1] if lang == 'de' else translations['legal_info'][2],
        'footer_text': translations['footer_text'][0] if lang == 'it' else translations['footer_text'][1] if lang == 'de' else translations['footer_text'][2],
    }
    
    return render(request, 'myapp/index.html', context)
