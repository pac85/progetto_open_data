f = open("Egr_GradCiclo_Sex_Nac_Campo_CA.conv.px").read()

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
    years = ["2015-2016", "2016-2017", "2017-2018", "2018-2019", "2019-2020"]
    subjects = ["Total", "01 - Educacion", "011101 - Pedagogía", "011201 - Educacion infantil", "011301 - Educacion primaria", "011401 - Otros maestros", "011901 - Educacion social", "02 - Artes y humanidades", "021101 - Audiovisual, imagen y multimedia", "021201 - Diseno", "021301 - Bellas artes", "021302 - Historia del arte", "021401 - Conservacion y restauracion", "021501 - Artes escénicas", "021502 - Música", "021988 - Otras artes", "022101 - Religion y teología", "022201 - Arqueología", "022202 - Historia", "022203 - Patrimonio Historico-Artístico", "022301 - Filosofía", "022901 - Humanidades", "022988 - Otras humanidades", "023101 - Lengua inglesa", "023102 - Lenguas clásicas", "023103 - Otras lenguas extranjeras", "023104 - Traduccion e interpretacion", "023201 - Lenguas y dialectos espanoles", "023202 - Literatura", "023901 - Lenguas modernas y aplicadas", "023988 - Otras lenguas", "03 - Ciencias sociales, periodismo y documentacion", "031101 - Economía", "031201 - Política y gestion pública", "031202 - Relaciones internacionales", "031301 - Psicología", "031401 - Antropología social y cultural", "031402 - Criminología", "031403 - Estudios y gestion de la cultura", "031404 - Geografía", "031405 - Igualdad de género", "031406 - Sociología", "031408 - Estudios regionales", "031988 - Otras ciencias sociales y jurídicas", "032101 - Comunicacion", "032102 - Periodismo", "032201 - Informacion y documentacion", "04 - Negocios, administracion y derecho", "041201 - Financiera y actuarial", "041202 - Finanzas y contabilidad", "041301 - Administracion y empresa", "041302 - Relaciones laborales y recursos humanos", "041303 - Gestion y administracion pública", "041401 - Marketing", "041402 - Protocolo y eventos", "041403 - Publicidad y relaciones públicas", "041601 - Comercio", "042101 - Derecho", "042102 - Abogacía", "05 - Ciencias", "051101 - Biología", "051201 - Bioquímica", "051202 - Biotecnología", "051901 - Biomedicina", "051988 - Otras ciencias de la vida", "052101 - Ciencias ambientales", "053101 - Química", "053201 - Ciencias del mar", "053202 - Geografía y ordenacion del territorio", "053203 - Geología", "053301 - Física", "053988 - Otras ciencias", "054101 - Matemáticas", "054201 - Estadística", "054988 - Otras matemáticas y estadística", "06 - Informática", "061201 - Diseno y administracion de bases de datos y redes", "061301 - Desarrollo de software y de aplicaciones", "061302 - Desarrollo de videojuegos", "061303 - Ingeniería multimedia", "061901 - Informática", "061988 - Otras informática", "07 - Ingeniería, industria y construccion", "071101 - Ingeniería química industrial", "071201 - Ingeniería medioambiental", "071301 - Ingeniería de la energía", "071302 - Ingeniería eléctrica", "071401 - Ingeniería de computadores", "071402 - Ingeniería de sonido e imagen", "071403 - Ingeniería de telecomunicacion", "071404 - Ingeniería electronica industrial y automática", "071405 - Ingeniería en electronica", "071501 - Ingeniería en diseno industrial y desarrollo del producto", "071502 - Ingeniería en tecnologías industriales", "071503 - Ingeniería mecánica", "071601 - Ingeniería aeronáutica", "071602 - Ingeniería del automovil", "071603 - Ingeniería naval y oceánica", "071901 - Ingeniería de organizacion industrial", "071902 - Nanotecnología", "071988 - Otras ingeniería", "072101 - Ciencia y tecnología de los alimentos", "072102 - Enología", "072103 - Ingeniería alimentaria", "072201 - Ingeniería de materiales", "072301 - Ingeniería textil", "072401 - Ingeniería de minas y  energía", "073101 - Arquitectura", "073102 - Ingeniería geomática, topografía y cartografía", "073103 - Urbanismo y paisajismo", "073201 - Arquitectura técnica", "073202 - Ingeniería civil", "08 - Agricultura, ganadería,  silvicultura, pesca, y veterinaria", "081102 - Ingeniería agraria y agroalimentaria", "081103 - Ingeniería agrícola, agropecuaria y medio rural", "081201 - Ingeniería horticultura y jardinería", "082101 - Ingeniería forestal y montes", "084101 - Veterinaria", "09 - Salud y servicios sociales", "091101 - Odontología", "091201 - Medicina", "091301 - Enfermería", "091401 - Ingeniería biomédica y de la salud", "091402 - optica y optometría", "091501 - Fisioterapia", "091502 - Logopedia", "091503 - Nutricion humana y dietética", "091504 - Podología", "091505 - Terapia ocupacional", "091601 - Farmacia", "091988 - Otras ciencias de la salud", "092301 - Trabajo social", "10 - Servicios", "101301 - Gastronomía y artes culinarias", "101302 - Gestion hotelera", "101401 - Actividad física y del deporte", "101402 - Gestion deportiva", "101501 - Turismo", "102201 - Prevencion y seguridad laboral", "103101 - Ensenanza militar", "103201 - Proteccion de la propiedad y las personas", "104101 - Náutica y transporte marítimo", "104102 - Servicio de transporte terrestre", "104103 - Servicios de transporte aéreo"]

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
