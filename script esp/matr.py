f = open("Mat_GradCiclo_Sex_Nac_Campo_CA.conv.px").read()

i = 0
corsi = []
stato = 0;
lines = f.split("\n")
region = ""
regions = {}
type = ""
presence = ""
gender = ""

def merge_dicts(d, r, b):
    try:
        return {**d[r], **b}
    except:
        return b

while True:
    if i >= len(lines):
        break
    line = lines[i]

    #corsi
    if i == 1:
        for field in line.split(";"):
            if len(field) == 0:
                continue
            corsi += [field]
    #ignora date
    i = 2

    #regions
    region_i = 0
    while True:
        if i >= len(lines):
            break
        line = lines[i]
        region = line
        i += 1
        for type_i in range(0, 3):
            try:
                line = lines[i]
            except:
                pass
            type = line
            regions[region] = merge_dicts(regions, region, {type: {}})
            i += 1 

            for presence_i in range(0, 3):
                try:
                    presence = lines[i]
                except:
                    break
                regions[region][type] = merge_dicts(regions[region], type, {presence: {}})
                i += 1

                for gender_i in range(0, 3):
                    try:
                        gender = lines[i]
                    except:
                        break
                    regions[region][type][presence] = merge_dicts(regions[region][type], presence, {gender: {}})
                    i += 1

                    for location_i in range(0, 3):
                        try:
                            location = lines[i]
                        except:
                            break
                        i += 1
                        location, *value = location.split(";")
                        value = value[0:-1]
                        regions[region][type][presence][gender] = merge_dicts(regions[region][type][presence], gender, {location: value})

    i += 1
    
"""
{region: {type(public, private): {precence: {gender: {location: [values]}}}}}
"""

def year_subject_from_i(i):
    years = ["2015-2016", "2016-2017", "2017-2018", "2018-2019", "2019-2020", "2020-2021"]
    subjects = ["Total", "01 - Educaci?n", "011101 - Pedagog?a", "011201 - Educaci?n infantil", "011301 - Educaci?n primaria", "011401 - Otros maestros", "011901 - Educaci?n social", "02 - Artes y humanidades", "021101 - Audiovisual, imagen y multimedia", "021201 - Dise?o", "021301 - Bellas artes", "021302 - Historia del arte", "021401 - Conservaci?n y restauraci?n", "021501 - Artes esc?nicas", "021502 - M?sica", "021988 - Otras artes", "022101 - Religi?n y teolog?a", "022201 - Arqueolog?a", "022202 - Historia", "022203 - Patrimonio Hist?rico-Art?stico", "022301 - Filosof?a", "022901 - Humanidades", "022988 - Otras humanidades", "023101 - Lengua inglesa", "023102 - Lenguas cl?sicas", "023103 - Otras lenguas extranjeras", "023104 - Traducci?n e interpretaci?n", "023201 - Lenguas y dialectos espa?oles", "023202 - Literatura", "023901 - Lenguas modernas y aplicadas", "023988 - Otras lenguas", "03 - Ciencias sociales, periodismo y documentaci?n", "031101 - Econom?a", "031201 - Pol?tica y gesti?n p?blica", "031202 - Relaciones internacionales", "031301 - Psicolog?a", "031401 - Antropolog?a social y cultural", "031402 - Criminolog?a", "031403 - Estudios y gesti?n de la cultura", "031404 - Geograf?a", "031405 - Igualdad de g?nero", "031406 - Sociolog?a", "031408 - Estudios regionales", "031988 - Otras ciencias sociales y jur?dicas", "032101 - Comunicaci?n", "032102 - Periodismo", "032201 - Informaci?n y documentaci?n", "04 - Negocios, administraci?n y derecho", "041201 - Financiera y actuarial", "041202 - Finanzas y contabilidad", "041301 - Administraci?n y empresa", "041302 - Relaciones laborales y recursos humanos", "041303 - Gesti?n y administraci?n p?blica", "041401 - Marketing", "041402 - Protocolo y eventos", "041403 - Publicidad y relaciones p?blicas", "041601 - Comercio", "042101 - Derecho", "042102 - Abogac?a", "05 - Ciencias", "051101 - Biolog?a", "051201 - Bioqu?mica", "051202 - Biotecnolog?a", "051901 - Biomedicina", "051988 - Otras ciencias de la vida", "052101 - Ciencias ambientales", "053101 - Qu?mica", "053201 - Ciencias del mar", "053202 - Geograf?a y ordenaci?n del territorio", "053203 - Geolog?a", "053301 - F?sica", "053988 - Otras ciencias", "054101 - Matem?ticas", "054201 - Estad?stica", "054988 - Otras matem?ticas y estad?stica", "06 - Inform?tica", "061201 - Dise?o y administraci?n de bases de datos y redes", "061301 - Desarrollo de software y de aplicaciones", "061302 - Desarrollo de videojuegos", "061303 - Ingenier?a multimedia", "061304 - Inteligencia artificial", "061901 - Inform?tica", "061988 - Otras inform?tica", "07 - Ingenier?a, industria y construcci?n", "071101 - Ingenier?a qu?mica industrial", "071201 - Ingenier?a medioambiental", "071301 - Ingenier?a de la energ?a", "071302 - Ingenier?a el?ctrica", "071401 - Ingenier?a de computadores", "071402 - Ingenier?a de sonido e imagen", "071403 - Ingenier?a de telecomunicaci?n", "071404 - Ingenier?a electr?nica industrial y autom?tica", "071405 - Ingenier?a en electr?nica", "071501 - Ingenier?a en dise?o industrial y desarrollo del producto", "071502 - Ingenier?a en tecnolog?as industriales", "071503 - Ingenier?a mec?nica", "071601 - Ingenier?a aeron?utica", "071602 - Ingenier?a del autom?vil", "071603 - Ingenier?a naval y oce?nica", "071901 - Ingenier?a de organizaci?n industrial", "071902 - Nanotecnolog?a", "071988 - Otras ingenier?a", "072101 - Ciencia y tecnolog?a de los alimentos", "072102 - Enolog?a", "072103 - Ingenier?a alimentaria", "072201 - Ingenier?a de materiales", "072301 - Ingenier?a textil", "072401 - Ingenier?a de minas y  energ?a", "073101 - Arquitectura", "073102 - Ingenier?a geom?tica, topograf?a y cartograf?a", "073103 - Urbanismo y paisajismo", "073201 - Arquitectura t?cnica", "073202 - Ingenier?a civil", "08 - Agricultura, ganader?a,  silvicultura, pesca, y veterinaria", "081102 - Ingenier?a agraria y agroalimentaria", "081103 - Ingenier?a agr?cola, agropecuaria y medio rural", "081201 - Ingenier?a horticultura y jardiner?a", "082101 - Ingenier?a forestal y montes", "084101 - Veterinaria", "09 - Salud y servicios sociales", "091101 - Odontolog?a", "091201 - Medicina", "091301 - Enfermer?a", "091401 - Ingenier?a biom?dica y de la salud", "091402 - ?ptica y optometr?a", "091501 - Fisioterapia", "091502 - Logopedia", "091503 - Nutrici?n humana y diet?tica", "091504 - Podolog?a", "091505 - Terapia ocupacional", "091601 - Farmacia", "091988 - Otras ciencias de la salud", "092301 - Trabajo social", "10 - Servicios", "101301 - Gastronom?a y artes culinarias", "101302 - Gesti?n hotelera", "101401 - Actividad f?sica y del deporte", "101402 - Gesti?n deportiva", "101501 - Turismo", "102201 - Prevenci?n y seguridad laboral", "103101 - Ense?anza militar", "103201 - Protecci?n de la propiedad y las personas", "104101 - N?utica y transporte mar?timo", "104102 - Servicio de transporte terrestre", "104103 - Servicios de transporte a?reo"]

    if i // len(years) >= len(subjects):
        return ("err", f"err {i // len(years)} {len(subjects)}")
    return (years[i%len(years)], subjects[i // len(years)])

import re
def clean_str(s):
    s = re.sub(" *", "", s)
    s = re.sub(";", "", s)
    return s

def clean_strs(ss):
    return map(clean_str, ss)

row_i = 0

import csv
csvf = open('cleaned.csv', 'w')
fields = ["region", "type(public, private)", "precence", "location", "gender", "values", "year", "subject"]
csvw = csv.DictWriter(csvf, fieldnames=fields)
csvw.writeheader()

for region, region_v in regions.items():
    for type, type_v in region_v.items():
        for precence, precence_v in type_v.items():
            for gender, gender_v in precence_v.items():
                for location, location_v in gender_v.items():
                    for value_i, value in enumerate(location_v):
                        year, subject = year_subject_from_i(value_i)
                        [region, type, precence, gender, location] = clean_strs([region, type, precence, gender, location])
                        csvw.writerow({
                            "region": region, 
                            "type(public, private)": type, 
                            "precence": precence, 
                            "location": location, 
                            "gender": gender, 
                            "values": value, 
                            "year": year, 
                            "subject": subject
                        })
                        row_i += 1
csvf.close()
