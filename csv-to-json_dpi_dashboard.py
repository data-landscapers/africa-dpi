"""
Convert africa-dpi CSV to structured JSON for the dashboard.
Usage: python csv-to-json.py input.csv output.json

The CSV must have these column headers:
  Country, Country Name, Chapter, Chapter Details, Section, 
  Variable Name, Definition, Value Code, Value Name, Year, 
  Comments, Variable Id, Variable Sort, Source urls
"""

import csv, json, sys
from collections import OrderedDict, defaultdict

def convert(csv_path, json_path):
    with open(csv_path, 'r', encoding='utf-8-sig') as f:
        rows = list(csv.DictReader(f))
    
    print(f"Read {len(rows)} rows from {csv_path}")
    
    # Build variable metadata, scales, definitions
    var_scales = {}
    var_meta = {}
    var_defs = {}
    ch_details = {}
    
    for row in rows:
        vid = row['Variable Id']
        code = str(row['Value Code']).strip()
        vname = str(row['Value Name']).strip()
        ch = row['Chapter']
        sec = row['Section']
        
        if ch not in ch_details and row.get('Chapter Details'):
            ch_details[ch] = row['Chapter Details']
        
        if vid not in var_scales:
            var_scales[vid] = {}
        var_scales[vid][code] = vname
        
        if vid not in var_meta:
            try:
                sort_val = float(row['Variable Sort'])
            except:
                sort_val = 0
            var_meta[vid] = {
                'chapter': ch,
                'section': sec,
                'name': row['Variable Name'],
                'sort': sort_val
            }
        
        if vid not in var_defs and row.get('Definition'):
            var_defs[vid] = row['Definition']
    
    # Build hierarchy
    seen_chapters = OrderedDict()
    for vid, meta in sorted(var_meta.items(), 
            key=lambda x: (x[1]['chapter'], x[1]['section'], x[1]['sort'])):
        ch = meta['chapter']
        sec = meta['section']
        if ch not in seen_chapters:
            seen_chapters[ch] = OrderedDict()
        if sec not in seen_chapters[ch]:
            seen_chapters[ch][sec] = []
        seen_chapters[ch][sec].append({
            'id': vid,
            'name': meta['name'],
            'sort': meta['sort'],
            'scale': {k: v for k, v in sorted(var_scales[vid].items())},
            'definition': var_defs.get(vid, '')
        })
    
    hierarchy = []
    for ch, sections in seen_chapters.items():
        ch_obj = {'name': ch, 'details': ch_details.get(ch, ''), 'sections': []}
        for sec, variables in sections.items():
            ch_obj['sections'].append({'name': sec, 'variables': variables})
        hierarchy.append(ch_obj)
    
    # Build country data
    country_data = defaultdict(dict)
    country_names = {}
    for row in rows:
        iso = row['Country']
        vid = row['Variable Id']
        country_data[iso][vid] = {
            'code': int(row['Value Code']),
            'label': str(row['Value Name']).strip(),
            'year': str(row['Year']),
            'comments': row['Comments'],
            'sources': row.get('Source urls', '')
        }
        country_names[iso] = row['Country Name']
    
    countries = []
    for iso in sorted(country_names.keys()):
        countries.append({
            'iso3': iso,
            'name': country_names[iso],
            'data': country_data[iso]
        })
    
    output = {'hierarchy': hierarchy, 'countries': countries}
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(output, f)
    
    total_vars = sum(len(s['variables']) for ch in hierarchy for s in ch['sections'])
    print(f"Written: {len(hierarchy)} chapters, {total_vars} variables, {len(countries)} countries")
    print(f"Output: {json_path} ({len(json.dumps(output))/1024:.0f} KB)")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python csv-to-json.py input.csv output.json")
        sys.exit(1)
    convert(sys.argv[1], sys.argv[2])
