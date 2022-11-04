# global değişkenler
text_path = '/Users/oykukaplan/Desktop/ödev/all_data.txt'
output_file = 'updated_text.txt'

def main():
    
    lines_seen = list()
    
    # dosyayı satır satır okurken veri işleme gerçekleştirme
    with open(text_path, 'r') as file:
    
        for line in file:
            line = process(line.rstrip())
            
            # her satıra bir cümle gelcek şekilde ayarlama
            if line in [" ", "\n", ""]:
                continue
            line = line.lstrip(' ')
                
            # duplicated kaldır
            # satır önceden karşımıza çıkmış mı kaydet
            if line not in lines_seen:  # not a duplicate
                lines_seen.append(line)
                
    # güncellenmiş halini text'e kaydetme
    with open(output_file, 'w') as f:
        for line in lines_seen:
            f.write("%s\n" % line)
        

# tüm veri işleme operasyonları
def process(line):
    line = text_to_lower(line)
    line = tr_to_en(line)
    line = remove_puncs(line)
    
    if is_number(line):
        return ""
    
    return line

# satırı küçük harflere çevirme
def text_to_lower(line):
    return line.lower()

# harfleri türkçeden ingilizceye çevirme
def tr_to_en(line):
    tr_chars = ["ş","ç","ö","ğ","ü","ı"]
    en_chars = ["s","c","o","g","u","i"]
    for i in range(len(tr_chars)):
        line = line.replace(tr_chars[i],en_chars[i])
    return line

# noktalama işaretlerini kaldır
def remove_puncs(line):
    all_puncs = '''!(')-[]{};,:'"\;,<>./?@#©$%^&*▼_~'''
    for element in all_puncs:
        line = line.replace(element, "")
    return line

# satır sadece sayıdan olusup olusmadıgına bakar
def is_number(line):
    try:
        for n in line.split():
            f = float(n)
        return True
    except:
        return False

if __name__ == '__main__':
    main()
