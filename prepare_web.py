"""CI માં ચાલે છે: PDF લાઇબ્રેરી ઓફલાઇન (લોકલ) કરે છે, અને APK માટે ડાઉનલોડ-શિમ ઉમેરે છે.
ઉપયોગ: python3 scripts/prepare_web.py <web_dir> <node_modules_dir> [--android]"""
import sys,os,shutil
web,nm=sys.argv[1],sys.argv[2]; android='--android' in sys.argv
idx=os.path.join(web,'index.html'); h=open(idx,encoding='utf-8').read()
os.makedirs(os.path.join(web,'lib'),exist_ok=True)
libs=[('https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js',os.path.join(nm,'html2canvas','dist','html2canvas.min.js'),'lib/html2canvas.min.js'),
      ('https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js',os.path.join(nm,'jspdf','dist','jspdf.umd.min.js'),'lib/jspdf.umd.min.js')]
for url,src,dst in libs:
    if os.path.exists(src):
        shutil.copy(src,os.path.join(web,dst)); h=h.replace(url,dst); print('local:',dst)
    else:
        print('WARNING: missing',src,'- CDN જ રહેશે (ઓફલાઇન PDF નહીં બને)')
if android:
    shim=open(os.path.join(os.path.dirname(__file__),'native-shim.js'),encoding='utf-8').read()
    h=h.replace('</head>','<script>'+shim+'</script></head>',1); print('android shim added')
open(idx,'w',encoding='utf-8').write(h)
