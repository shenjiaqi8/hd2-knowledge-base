#!/usr/bin/env python3
"""Generate a single enemies.md from wiki introductions. Safe: no synthetic combat stats.
Requires only Python standard library. Intended for HD2 GitHub repo/scripts/.
"""
import argparse
import html
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

WIKI = 'https://helldivers.wiki.gg'
API = WIKI + '/api.php'
# Seed names can be extended without touching generated knowledge files.
FACTIONS = {
 'Terminids': ['Scavenger','Pouncer','Warrior','Hunter','Hive Guard','Brood Commander','Alpha Commander','Stalker','Shrieker','Bile Spitter','Nursing Spewer','Bile Spewer','Charger','Charger Behemoth','Impaler','Bile Titan','Hive Lord','Spore Charger','Rupture Charger','Dragonroach'],
 'Automatons': ['Trooper','Raider','Commissar','Berserker','Devastator','Heavy Devastator','Rocket Devastator','Scout Strider','Reinforced Scout Strider','Hulk','Annihilator Tank','Shredder Tank','Factory Strider','Gunship','Dropship','Jet Brigade','Cyborg Legion'],
 'Illuminate': ['Voteless','Watcher','Overseer','Elevated Overseer','Crescent Overseer','Harvester','Warp Ship','Stingray','Leviathan','Fleshmob','Obtruder','Gatekeeper','Veracitor','Crusher'],
}

def wiki_intro(title):
    params = {'action':'query','format':'json','formatversion':2,'prop':'extracts', 'exintro':1,'explaintext':1,'redirects':1,'titles':title}
    url = API + '?' + urllib.parse.urlencode(params)
    req = urllib.request.Request(url,headers={'User-Agent':'HD2-KnowledgeSync/1.0 (personal knowledge base; wiki attribution)', 'Accept':'application/json'})
    with urllib.request.urlopen(req,timeout=25) as response:
        obj=json.loads(response.read(2_000_000).decode('utf-8'))
    p=obj.get('query',{}).get('pages',[{}])[0]
    if p.get('missing') or p.get('invalid'): return None
    text=html.unescape(re.sub(r'\s+',' ',p.get('extract',''))).strip()
    # Do not reproduce entire wiki articles; intros provide basic identity/context.
    text=text[:650].rsplit(' ',1)[0] if len(text)>650 else text
    return {'title':p.get('title',title),'text':text}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--out',default='knowledge/generated/enemies.md')
    ap.add_argument('--delay',type=float,default=.4)
    args=ap.parse_args()
    sections=['# 绝地潜兵2：敌人资料（Enemies）','','> 来源：The Helldivers Wiki（社区维护，非官方）。本文件为简要索引，详细参数应通过每条的 Wiki 链接核查。', '> 名称及版本会更新；未验证的血量、装甲等级、弱点数值一律不臆造。','','## 阵营和名称索引','']
    entries={}; errors=[]
    for faction,names in FACTIONS.items():
        sections.append(f'### {faction}')
        sections.append('、'.join(names));sections.append('')
        data=[]
        for name in names:
            try:
                x=wiki_intro(name)
                if not x: errors.append(f'{faction}/{name}: 页面不存在')
                data.append((name,x))
            except (OSError,ValueError,KeyError) as e:
                errors.append(f'{faction}/{name}: {e}')
                data.append((name,None))
            time.sleep(args.delay)
        entries[faction]=data
    sections.extend(['## 敌人条目',''])
    count=0
    for faction,data in entries.items():
        sections.extend([f'## {faction}',''])
        for name,x in data:
            title=x['title'] if x else name
            link=WIKI+'/wiki/'+urllib.parse.quote(title.replace(' ','_'),safe='()')
            sections.extend([f'### {name}','',f'- Wiki：[{title}]({link})'])
            if x and x['text']:
                sections.extend(['',x['text']]);count+=1
            else:
                sections.append('- 状态：尚未获取可靠介绍，请通过 Wiki 搜索或人工核实。')
            sections.append('')
    sections.extend(['## 说明','','- 本文档只提供敌人名称索引与简要介绍，不代表完整敌人图鉴。','- 战斗数值、部位血量、穿甲需求请以具体 Wiki 页面及最新游戏补丁为准。','- 许可与署名：来源 Wiki，使用时遵守各源页的许可与署名要求。',''])
    dest=Path(args.out);dest.parent.mkdir(parents=True,exist_ok=True)
    # Prevent an upstream outage from wiping a previously healthy file.
    if count<12: raise RuntimeError(f'Only {count} verified introductions fetched; refusing to overwrite {dest}. Errors: {errors[:4]}')
    new='\n'.join(sections)
    if not dest.exists() or dest.read_text(encoding='utf-8')!=new: dest.write_text(new,encoding='utf-8')
    print(f'Enemy index updated: {len(sum(entries.values(),[]))} seed names; {count} Wiki introductions; {len(errors)} unavailable entries')
    if errors: print('Unresolved (first 15):', '\n'.join(errors[:15]))
if __name__=='__main__': main()
