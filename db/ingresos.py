import psycopg2

class Enfermedad:
    def __init__(self, nombre, descripcion, sintomas):
        self.nombre = nombre
        self.descripcion = descripcion
        self.sintomas = sintomas
    

enfermedades = [
        Enfermedad('Acné y Rosácea',
                    'El acné y la rosácea son afecciones cutáneas inflamatorias comunes que afectan principalmente la cara. El acné suele asociarse con espinillas y poros obstruidos, mientras que la rosácea se caracteriza por enrojecimiento persistente y vasos sanguíneos visibles.', 
                    ['espinillas', 'pústulas', 'enrojecimiento facial', 'piel sensible', 'poros obstruidos', 'vasos sanguíneos visibles', 'ardor o escozor', 'protuberancias inflamadas']),
        Enfermedad('Queratosis Actínica, Carcinoma Basocelular y Otras Lesiones Malignas',
                    'Estas son lesiones cutáneas precancerosas o cancerosas causadas principalmente por la exposición prolongada al sol. La queratosis actínica puede evolucionar hacia cáncer de piel si no se trata, mientras que el carcinoma basocelular es el tipo más común de cáncer cutáneo.', 
                    ['manchas ásperas y escamosas', 'protuberancias perladas', 'costras persistentes', 'lesiones que sangran', 'heridas que no sanan', 'piel engrosada', 'cambios de color en la piel']), 
        Enfermedad('Dermatitis Atópica',
                    'La dermatitis atópica es una enfermedad inflamatoria crónica de la piel, común en niños pero también presente en adultos. Se caracteriza por brotes de picazón intensa, sequedad y enrojecimiento en diferentes zonas del cuerpo.', 
                    ['piel seca', 'picazón intensa', 'enrojecimiento', 'descamación', 'grietas en la piel', 'engrosamiento de la piel', 'lesiones que supuran', 'irritación al rascarse']), 
        Enfermedad('Celulitis Bacteriana',
                    'La celulitis es una infección bacteriana de la piel y tejidos subyacentes que causa inflamación, enrojecimiento y dolor. Generalmente ocurre cuando bacterias entran a través de una herida o fisura en la piel.', 
                    ['enrojecimiento', 'hinchazón', 'dolor localizado', 'calor en la zona afectada', 'fiebre', 'piel sensible', 'rayas rojas', 'sensación de tensión en la piel']),
        Enfermedad('Impétigo Bacteriano',
                    'El impétigo es una infección cutánea muy contagiosa, común en niños, causada por bacterias como Staphylococcus aureus. Se manifiesta como llagas rojizas que se convierten en costras color miel.', 
                    ['llagas rojizas', 'ampollas', 'costras color miel', 'picazón', 'piel irritada', 'lesiones con pus', 'enrojecimiento']), 
        Enfermedad('Lesiones Malignas',
                    'Las lesiones malignas son áreas anormales de la piel que pueden ser cancerosas o precursores de cáncer. Su aspecto puede variar, pero suelen mostrar crecimiento, sangrado o cambios de color.', 
                    ['crecimiento anormal', 'sangrado espontáneo', 'cambio de color', 'bordes irregulares', 'picazón persistente', 'dolor en la lesión', 'ulceración']), 
        Enfermedad('Melanoma, Cáncer de Piel, Nevos y Lunares',
                    'El melanoma es un tipo agresivo de cáncer de piel que se origina en los melanocitos. Puede desarrollarse a partir de un lunar existente o como una nueva lesión pigmentada.', 
                    ['lunares asimétricos', 'bordes irregulares', 'cambios de color', 'aumento de tamaño', 'sangrado', 'picazón', 'nuevas manchas oscuras']),
        Enfermedad('Hongos en las Uñas y Otras Enfermedades Ungueales',
                    'Las infecciones por hongos en las uñas (onicomicosis) provocan cambios en el color, textura y forma de las uñas. También se incluyen otras condiciones como uñas encarnadas o psoriasis ungueal.', 
                    ['uñas engrosadas', 'cambio de color', 'fragilidad', 'desprendimiento de la uña', 'olor desagradable', 'dolor', 'deformidad ungueal']), 
        Enfermedad('Larva Migrans Cutánea',
                    'Es una infestación parasitaria de la piel causada por larvas de anquilostomas que penetran la epidermis al contacto con suelo contaminado. Produce lesiones serpentinas que avanzan lentamente bajo la piel.', 
                    ['lesiones en forma de serpiente', 'picazón intensa', 'enrojecimiento', 'hinchazón', 'sensación de movimiento bajo la piel', 'vesículas', 'dolor leve']), 
        Enfermedad('Hiedra Venenosa y Otras Dermatitis de Contacto',
                    'La dermatitis de contacto es una reacción inflamatoria de la piel al entrar en contacto con sustancias irritantes o alérgenas como la hiedra venenosa. Puede presentarse como sarpullido, ampollas o enrojecimiento.', 
                    ['erupción cutánea', 'enrojecimiento', 'ampollas', 'picazón intensa', 'descamación', 'hinchazón localizada', 'ardor']),
        Enfermedad('Lesiones Benignas',
                    'Las lesiones benignas de la piel son alteraciones no cancerosas que no representan peligro para la salud, aunque algunas pueden parecerse a lesiones malignas. Incluyen lunares, queratosis seborreica y fibromas blandos.', 
                    ['protuberancias suaves', 'lunares estables', 'cambios mínimos en tamaño o color', 'lesiones no dolorosas', 'superficie cerosa o escamosa', 'bordes definidos']), 
        Enfermedad('Psoriasis, Liquen Plano y Enfermedades Relacionadas',
                    'Estas son enfermedades inflamatorias crónicas de la piel con manifestaciones distintas pero patrones inmunológicos comunes. La psoriasis causa placas escamosas, mientras que el liquen plano genera pápulas violáceas.', 
                    ['placas escamosas', 'pápulas planas y violáceas', 'picazón', 'descamación', 'engrosamiento de la piel', 'cambios en uñas', 'lesiones en mucosas']), 
        Enfermedad('Enfermedades Ampollares',
                    'Las enfermedades ampollares son trastornos autoinmunes de la piel que causan la formación de ampollas o vesículas. Ejemplos incluyen pénfigo y penfigoide.', 
                    ['ampollas grandes y tensas', 'vesículas', 'dolor en la piel', 'enrojecimiento alrededor de las lesiones', 'descamación', 'lesiones que supuran', 'úlceras']),
        Enfermedad('Erupciones Cutáneas',
                    'Las erupciones son reacciones visibles en la piel que pueden deberse a alergias, infecciones, enfermedades autoinmunes o irritantes. Su apariencia y causa varían ampliamente.', 
                    ['enrojecimiento', 'inflamación', 'manchas o ronchas', 'picazón', 'descamación', 'ampollas', 'cambios en la textura de la piel']), 
        Enfermedad('Celulitis, Impétigo y Otras Infecciones Bacterianas',
                    'Estas infecciones cutáneas son causadas por bacterias comunes como Staphylococcus aureus o Streptococcus pyogenes. Varían desde impétigo superficial hasta celulitis más profunda.', 
                    ['enrojecimiento', 'dolor', 'calor en la piel', 'ampollas o costras', 'inflamación', 'fiebre', 'piel sensible', 'lesiones con pus']), 
        Enfermedad('Sarna, Enfermedad de Lyme y Otras Infestaciones y Picaduras',
                    'Estas condiciones son causadas por parásitos o picaduras de insectos. La sarna es altamente contagiosa y producida por ácaros; la enfermedad de Lyme proviene de la picadura de garrapatas infectadas.', 
                    ['picazón intensa', 'erupciones cutáneas', 'líneas finas bajo la piel', 'enrojecimiento', 'fatiga', 'dolores musculares', 'lesiones en forma de diana']),
        Enfermedad('Eccema',
                    'El eccema es una enfermedad inflamatoria crónica de la piel caracterizada por brotes de sequedad, picazón e irritación. Puede ser desencadenado por alérgenos o factores ambientales.', 
                    ['piel seca', 'picazón persistente', 'enrojecimiento', 'grietas en la piel', 'vesículas', 'engrosamiento cutáneo', 'descamación']), 
        Enfermedad('Queratosis Seborreica y Otros Tumores Benignos',
                    'Las queratosis seborreicas son crecimientos cutáneos benignos, comunes con la edad. Pueden confundirse con lesiones malignas por su aspecto verrugoso o pigmentado.', 
                    ['lesiones elevadas', 'color marrón o negro', 'superficie cerosa o verrugosa', 'no dolorosas', 'cambios lentos en tamaño', 'bordes definidos']), 
        Enfermedad('Exantemas y Erupciones por Medicamentos',
                    'Estas son erupciones cutáneas causadas por infecciones virales o reacciones adversas a medicamentos. Suelen presentarse de forma súbita y afectar grandes áreas del cuerpo.', 
                    ['manchas rojas', 'ronchas', 'picazón', 'fiebre', 'descamación', 'hinchazón', 'malestar general', 'lesiones simétricas']),
        Enfermedad('Enfermedades Sistémicas con Manifestaciones Cutáneas',
                    'Algunas enfermedades internas como lupus, diabetes o enfermedades hepáticas pueden manifestarse en la piel. Estas señales cutáneas pueden ayudar en el diagnóstico de afecciones subyacentes.', 
                    ['lesiones variables según la enfermedad', 'cambios de color en la piel', 'úlceras', 'erupciones en zonas específicas', 'caída de cabello', 'hinchazón', 'fragilidad capilar']), 
        Enfermedad('Pie de Atleta',
                    'El pie de atleta es una infección fúngica que afecta la piel entre los dedos del pie y la planta. Es común en ambientes húmedos y cálidos.', 
                    ['descamación', 'picazón entre los dedos', 'mal olor', 'enrojecimiento', 'grietas en la piel', 'ardor', 'vesículas pequeñas']), 
        Enfermedad('Tatuajes',
                    'Aunque los tatuajes son decorativos, pueden causar reacciones adversas como infecciones, alergias o granulomas. Las complicaciones dependen del tipo de tinta y la técnica.', 
                    ['enrojecimiento prolongado', 'hinchazón', 'picazón persistente', 'bultos', 'infección localizada', 'cambios en el color del tatuaje', 'formación de costras o úlceras']),
        Enfermedad('Hongos en las Uñas',
                    'Los hongos en las uñas, o onicomicosis, afectan principalmente las uñas de los pies, causando cambios en su color, grosor y forma. Es más frecuente en personas con sudoración excesiva o calzado cerrado.', 
                    ['uñas engrosadas', 'color amarillento o marrón', 'fragilidad', 'desprendimiento parcial de la uña', 'mal olor', 'dolor leve', 'deformidad']), 
        Enfermedad('Tiña, Candidiasis y Otras Infecciones Fúngicas',
                    'Las infecciones fúngicas de la piel pueden afectar distintas zonas del cuerpo y son causadas por dermatofitos o levaduras. Se propagan en ambientes húmedos y cálidos.', 
                    ['manchas circulares con borde elevado', 'picazón', 'descamación', 'enrojecimiento', 'grietas en la piel', 'vesículas', 'olor desagradable']), 
        Enfermedad('Tiña Corporis (Dermatofitosis)',
                    'La tiña es una infección por hongos en la piel con forma característica de anillo. Afecta principalmente tronco, extremidades y cara.', 
                    ['lesiones circulares con bordes elevados', 'descamación central', 'picazón', 'enrojecimiento', 'lesiones que se agrandan', 'apariencia anular']),
        Enfermedad('Urticaria (Ronchas)',
                    'La urticaria es una reacción cutánea caracterizada por la aparición repentina de ronchas rojas o pálidas que producen picazón intensa. Puede ser provocada por alergias, infecciones o estrés.', 
                    ['ronchas elevadas', 'picazón intensa', 'enrojecimiento', 'hinchazón transitoria', 'cambios rápidos en la forma de las lesiones', 'desaparición espontánea', 'ardor leve']), 
        Enfermedad('Pérdida de Cabello, Alopecia y Otras Enfermedades Capilares',
                    'Las enfermedades del cabello incluyen la alopecia, que es la pérdida anormal de cabello, y otras condiciones que afectan el cuero cabelludo o el folículo piloso. Pueden tener causas genéticas, autoinmunes o ambientales.', 
                    ['pérdida de cabello en parches', 'calvicie difusa', 'debilitamiento del cabello', 'picazón en el cuero cabelludo', 'inflamación', 'costras', 'cambios en la textura del cabello']), 
        Enfermedad('Tumores Vasculares',
                    'Los tumores vasculares son crecimientos anómalos formados por vasos sanguíneos. Pueden ser benignos, como los hemangiomas, o más complejos y raros.', 
                    ['lesiones rojizas o violáceas', 'crecimientos elevados', 'sangrado ocasional', 'cambio de tamaño con el tiempo', 'dolor si se inflaman', 'calor local']),
        Enfermedad('Piel Sana',
                    'La piel sana es uniforme, libre de lesiones, con buena hidratación y sin signos de inflamación o infección. Refleja buen cuidado cutáneo y salud general.', 
                    ['textura uniforme', 'hidratación adecuada', 'color homogéneo', 'ausencia de lesiones', 'elasticidad normal', 'sin picazón ni irritación']), 
        Enfermedad('Vasculitis',
                    'La vasculitis es una inflamación de los vasos sanguíneos que puede causar daño a la piel y otros órganos. Su presentación cutánea incluye manchas, úlceras o nódulos dolorosos.', 
                    ['manchas rojizas o moradas', 'petequias', 'úlceras cutáneas', 'dolor en la piel', 'inflamación localizada', 'fiebre', 'fatiga']), 
        Enfermedad('Herpes, VPH y Otras ETS',
                    'Estas infecciones de transmisión sexual afectan la piel y mucosas, y son causadas por virus como el herpes simple (HSV) y el virus del papiloma humano (VPH). Se transmiten por contacto íntimo.', 
                    ['ampollas dolorosas', 'lesiones genitales', 'picazón', 'ardor al orinar', 'verrugas genitales', 'úlceras recurrentes', 'enrojecimiento']),
        Enfermedad('Varicela',
                    'La varicela es una infección viral muy contagiosa causada por el virus varicela-zóster. Afecta principalmente a niños y se caracteriza por erupciones con picazón.', 
                    ['ampollas llenas de líquido', 'picazón intensa', 'manchas rojas', 'fiebre', 'malestar general', 'costras al cicatrizar']), 
        Enfermedad('Enfermedades de la Luz y Trastornos de la Pigmentación',
                    'Estas condiciones incluyen alteraciones provocadas por la exposición al sol (como la fotodermatitis) y trastornos de pigmentación como el vitiligo o melasma.', 
                    ['manchas blancas o oscuras', 'sensibilidad al sol', 'enrojecimiento', 'ardor al exponerse al sol', 'pérdida de pigmento', 'hiperpigmentación localizada']), 
        Enfermedad('Herpes Zóster (Culebrilla)',
                    'El herpes zóster es una reactivación del virus de la varicela que causa una erupción dolorosa en un solo lado del cuerpo. Común en adultos mayores o personas inmunodeprimidas.', 
                    ['dolor localizado', 'ampollas agrupadas', 'sensación de ardor', 'picazón', 'erupción unilateral', 'hormigueo previo a la erupción', 'costras al cicatrizar']),
        Enfermedad('Lupus y Otras Enfermedades del Tejido Conectivo',
                    'Estas enfermedades autoinmunes afectan la piel, las articulaciones y otros órganos. El lupus eritematoso sistémico es una de las formas más comunes, con signos cutáneos distintivos como el rash en alas de mariposa.', 
                    ['erupciones en mejillas y nariz', 'fatiga', 'dolor articular', 'fotosensibilidad', 'úlceras orales', 'caída de cabello', 'piel inflamada']), 
        Enfermedad('Verrugas, Molusco Contagioso y Otras Infecciones Virales',
                    'Son infecciones cutáneas causadas por virus como el VPH y el poxvirus. Afectan comúnmente a niños y personas inmunocomprometidas.', 
                    ['protuberancias elevadas', 'superficie rugosa (verrugas)', 'lesiones con centro umbilicado (molusco)', 'picazón', 'irritación local', 'crecimiento lento', 'distribución en grupos']),         
    ]

# Configuración de conexión
conn = psycopg2.connect(
    host="127.0.0.1",
    database="dermascan",
    user="felipep",
    password="mariapaz28",
    port=5432
)

cur = conn.cursor()

sintoma_cache = {}

try:
    for enf in enfermedades:
        # Insertar enfermedad
        cur.execute("""
            INSERT INTO enfermedades (nombre_enfermedad, descripcion)
            VALUES (%s, %s)
            RETURNING id_enfermedad;
        """, (enf.nombre, enf.descripcion))
        id_enfermedad = cur.fetchone()[0]

        for sintoma in enf.sintomas:
            # Verificar si el síntoma ya fue insertado
            if sintoma not in sintoma_cache:
                # Buscar si ya existe en DB
                cur.execute("SELECT id_sintoma FROM sintomas WHERE nombre_sintoma = %s;", (sintoma,))
                row = cur.fetchone()

                if row:
                    id_sintoma = row[0]
                else:
                    # Insertar síntoma
                    cur.execute("INSERT INTO sintomas (nombre_sintoma) VALUES (%s) RETURNING id_sintoma;", (sintoma,))
                    id_sintoma = cur.fetchone()[0]

                sintoma_cache[sintoma] = id_sintoma
            else:
                id_sintoma = sintoma_cache[sintoma]

            # Insertar relación en tabla intermedia
            cur.execute("""
                INSERT INTO enfermedad_sintoma (id_enfermedad, id_sintoma)
                VALUES (%s, %s)
                ON CONFLICT DO NOTHING;
            """, (id_enfermedad, id_sintoma))

    conn.commit()
    print("Datos insertados correctamente")
except Exception as e:
    print("Error:", e)
    conn.rollback()
finally:
    cur.close()
    conn.close()
    print("Conexión cerrada")