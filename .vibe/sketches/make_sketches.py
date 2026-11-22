# Skizzen der Bildfamilie (Entwurf; das fertige Skript make_partitur.py entsteht im Muster-Task).
BG="#f4efe2"
def head(h=230): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 {h}" role="img"><rect width="480" height="{h}" fill="{BG}"/>'
def row_label(y,t,dim=False): return f'<text x="8" y="{y}" font-family="sans-serif" font-size="16" fill="{"#8a8577" if dim else "#333"}">{t}</text>'
def card(x,y,w,t,fill="#2c6fd8",tc="#fff"): return f'<rect x="{x}" y="{y}" width="{w}" height="46" rx="8" fill="{fill}"/><text x="{x+w/2}" y="{y+30}" text-anchor="middle" font-family="sans-serif" font-size="20" fill="{tc}">{t}</text>'
def word(x,y,w,t): return f'<text x="{x+w/2}" y="{y}" text-anchor="middle" font-family="sans-serif" font-size="16" fill="#333">{t}</text>'
def legend(top_dim=True,mid_dim=True):
    return row_label(30,"Melodie",top_dim)+row_label(100,"Betonung",mid_dim)+row_label(160,"Laute",False)
def partitur_laute():
    s=head()+legend()
    s+='<rect x="100" y="12" width="364" height="44" rx="8" fill="none" stroke="#8a8577" stroke-dasharray="6 4"/><text x="282" y="40" text-anchor="middle" font-family="sans-serif" font-size="16" fill="#8a8577">kommt in Kapitel 3</text>'
    s+='<rect x="100" y="78" width="364" height="34" rx="8" fill="none" stroke="#8a8577" stroke-dasharray="6 4"/><text x="282" y="101" text-anchor="middle" font-family="sans-serif" font-size="16" fill="#8a8577">kommt später</text>'
    x=100
    for w,t,tx in [(110,"aɪm","I’m"),(110,"səʊ","So"),(110,"fi","phie")]:
        s+=card(x,130,w,t)+word(x,210,w,tx); x+=122
    open('skizze-partitur-lautschrift.svg','w').write(s+'</svg>')
def partitur_melodie():
    s=head()+legend(False,True)
    s+='<path d="M110 52 L200 52 L330 20" stroke="#c0392b" stroke-width="4" fill="none"/><polygon points="330,20 316,20 322,32" fill="#c0392b"/>'
    s+='<path d="M342 20 L440 52" stroke="#138d75" stroke-width="4" fill="none" stroke-dasharray="6 4"/>'
    s+='<rect x="100" y="78" width="364" height="34" rx="8" fill="none" stroke="#8a8577" stroke-dasharray="6 4"/>'
    x=100
    for w,t,tx in [(86,"duː","do"),(86,"juː","you"),(86,"laɪk","like"),(86,"tiː","tea")]:
        s+=card(x,130,w,t)+word(x,210,w,tx); x+=94
    open('skizze-partitur-melodie.svg','w').write(s+'</svg>')
def werkstatt():
    s=head(200)
    s+='<text x="240" y="26" text-anchor="middle" font-family="sans-serif" font-size="18" fill="#333">Werkstatt: was passiert vor der Endung?</text>'
    for i,(a,b,c,m) in enumerate([("stop","ed","stopped","doppeln"),("cry","s","cries","y → ie"),("make","ing","making","e fällt weg")]):
        y=44+i*50
        s+=card(8,y,100,a,"#138d75")+card(120,y,150,m,"#e6b800","#222")+card(282,y,60,b,"#2c6fd8")+f'<text x="352" y="{y+30}" font-family="sans-serif" font-size="22" fill="#333">= {c}</text>'
    open('skizze-werkstatt-endungen.svg','w').write(s+'</svg>')
partitur_laute(); partitur_melodie(); werkstatt()
