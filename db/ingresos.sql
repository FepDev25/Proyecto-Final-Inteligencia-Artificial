-- Inserción de Enfermedades y Síntomas

-- Insertar Síntomas
INSERT INTO sintomas (nombre_sintoma) VALUES
('espinillas'), ('pústulas'), ('enrojecimiento facial'), ('piel sensible'), ('poros obstruidos'), ('vasos sanguíneos visibles'), ('ardor o escozor'), ('protuberancias inflamadas'),
('manchas ásperas y escamosas'), ('protuberancias perladas'), ('costras persistentes'), ('lesiones que sangran'), ('heridas que no sanan'), ('piel engrosada'), ('cambios de color en la piel'),
('piel seca'), ('picazón intensa'), ('enrojecimiento'), ('descamación'), ('grietas en la piel'), ('engrosamiento de la piel'), ('lesiones que supuran'), ('irritación al rascarse'),
('hinchazón'), ('dolor localizado'), ('calor en la zona afectada'), ('fiebre'), ('rayas rojas'), ('sensación de tensión en la piel'),
('llagas rojizas'), ('ampollas'), ('costras color miel'), ('picazón'), ('piel irritada'), ('lesiones con pus'),
('crecimiento anormal'), ('sangrado espontáneo'), ('cambio de color'), ('bordes irregulares'), ('picazón persistente'), ('dolor en la lesión'), ('ulceración'),
('lunares asimétricos'), ('aumento de tamaño'), ('nuevas manchas oscuras'),
('uñas engrosadas'), ('fragilidad'), ('desprendimiento de la uña'), ('olor desagradable'), ('dolor'), ('deformidad ungueal'),
('lesiones en forma de serpiente'), ('sensación de movimiento bajo la piel'), ('vesículas'), ('dolor leve'),
('erupción cutánea'), ('ampollas'), ('hinchazón localizada'), ('ardor'),
('protuberancias suaves'), ('lunares estables'), ('cambios mínimos en tamaño o color'), ('lesiones no dolorosas'), ('superficie cerosa o escamosa'), ('bordes definidos'),
('placas escamosas'), ('pápulas planas y violáceas'), ('cambios en uñas'), ('lesiones en mucosas'),
('ampollas grandes y tensas'), ('dolor en la piel'), ('úlceras'),
('inflamación'), ('manchas o ronchas'), ('cambios en la textura de la piel'),
('calor en la piel'),
('líneas finas bajo la piel'), ('fatiga'), ('dolores musculares'), ('lesiones en forma de diana'),
('picazón persistente'), ('engrosamiento cutáneo'),
('lesiones elevadas'), ('color marrón o negro'), ('superficie cerosa o verrugosa'), ('cambios lentos en tamaño'),
('manchas rojas'), ('ronchas'), ('malestar general'), ('lesiones simétricas'),
('lesiones variables según la enfermedad'), ('caída de cabello'), ('fragilidad capilar'),
('picazón entre los dedos'), ('mal olor'),
('enrojecimiento prolongado'), ('bultos'), ('infección localizada'), ('cambios en el color del tatuaje'), ('formación de costras o úlceras'),
('color amarillento o marrón'), ('desprendimiento parcial de la uña'),
('manchas circulares con borde elevado'),
('lesiones circulares con bordes elevados'), ('descamación central'), ('apariencia anular'),
('ronchas elevadas'), ('hinchazón transitoria'), ('cambios rápidos en la forma de las lesiones'), ('desaparición espontánea'), ('ardor leve'),
('pérdida de cabello en parches'), ('calvicie difusa'), ('debilitamiento del cabello'), ('picazón en el cuero cabelludo'), ('costras'), ('cambios en la textura del cabello'),
('lesiones rojizas o violáceas'), ('crecimientos elevados'), ('sangrado ocasional'), ('cambio de tamaño con el tiempo'), ('calor local'),
('textura uniforme'), ('hidratación adecuada'), ('color homogéneo'), ('ausencia de lesiones'), ('elasticidad normal'), ('sin picazón ni irritación'),
('manchas rojizas o moradas'), ('petequias'), ('úlceras cutáneas'),
('ampollas dolorosas'), ('lesiones genitales'), ('ardor al orinar'), ('verrugas genitales'), ('úlceras recurrentes'),
('ampollas llenas de líquido'), ('costras al cicatrizar'),
('manchas blancas o oscuras'), ('sensibilidad al sol'), ('ardor al exponerse al sol'), ('pérdida de pigmento'), ('hiperpigmentación localizada'),
('dolor localizado'), ('ampollas agrupadas'), ('sensación de ardor'), ('erupción unilateral'), ('hormigueo previo a la erupción'),
('erupciones en mejillas y nariz'), ('dolor articular'), ('fotosensibilidad'), ('úlceras orales'),
('protuberancias elevadas'), ('superficie rugosa (verrugas)'), ('lesiones con centro umbilicado (molusco)'), ('irritación local'), ('crecimiento lento'), ('distribución en grupos');

-- Insertar Enfermedades
INSERT INTO enfermedades (nombre_enfermedad, descripcion) VALUES
('Acné y Rosácea', 'El acné y la rosácea son afecciones cutáneas inflamatorias comunes que afectan principalmente la cara. El acné suele asociarse con espinillas y poros obstruidos, mientras que la rosácea se caracteriza por enrojecimiento persistente y vasos sanguíneos visibles.'),
('Queratosis Actínica, Carcinoma Basocelular y Otras Lesiones Malignas', 'Estas son lesiones cutáneas precancerosas o cancerosas causadas principalmente por la exposición prolongada al sol. La queratosis actínica puede evolucionar hacia cáncer de piel si no se trata, mientras que el carcinoma basocelular es el tipo más común de cáncer cutáneo.'),
('Dermatitis Atópica', 'La dermatitis atópica es una enfermedad inflamatoria crónica de la piel, común en niños pero también presente en adultos. Se caracteriza por brotes de picazón intensa, sequedad y enrojecimiento en diferentes zonas del cuerpo.'),
('Celulitis Bacteriana', 'La celulitis es una infección bacteriana de la piel y tejidos subyacentes que causa inflamación, enrojecimiento y dolor. Generalmente ocurre cuando bacterias entran a través de una herida o fisura en la piel.'),
('Impétigo Bacteriano', 'El impétigo es una infección cutánea muy contagiosa, común en niños, causada por bacterias como Staphylococcus aureus. Se manifiesta como llagas rojizas que se convierten en costras color miel.'),
('Lesiones Malignas', 'Las lesiones malignas son áreas anormales de la piel que pueden ser cancerosas o precursores de cáncer. Su aspecto puede variar, pero suelen mostrar crecimiento, sangrado o cambios de color.'),
('Melanoma, Cáncer de Piel, Nevos y Lunares', 'El melanoma es un tipo agresivo de cáncer de piel que se origina en los melanocitos. Puede desarrollarse a partir de un lunar existente o como una nueva lesión pigmentada.'),
('Hongos en las Uñas y Otras Enfermedades Ungueales', 'Las infecciones por hongos en las uñas (onicomicosis) provocan cambios en el color, textura y forma de las uñas. También se incluyen otras condiciones como uñas encarnadas o psoriasis ungueal.'),
('Larva Migrans Cutánea', 'Es una infestación parasitaria de la piel causada por larvas de anquilostomas que penetran la epidermis al contacto con suelo contaminado. Produce lesiones serpentinas que avanzan lentamente bajo la piel.'),
('Hiedra Venenosa y Otras Dermatitis de Contacto', 'La dermatitis de contacto es una reacción inflamatoria de la piel al entrar en contacto con sustancias irritantes o alérgenas como la hiedra venenosa. Puede presentarse como sarpullido, ampollas o enrojecimiento.'),
('Lesiones Benignas', 'Las lesiones benignas de la piel son alteraciones no cancerosas que no representan peligro para la salud, aunque algunas pueden parecerse a lesiones malignas. Incluyen lunares, queratosis seborreica y fibromas blandos.'),
('Psoriasis, Liquen Plano y Enfermedades Relacionadas', 'Estas son enfermedades inflamatorias crónicas de la piel con manifestaciones distintas pero patrones inmunológicos comunes. La psoriasis causa placas escamosas, mientras que el liquen plano genera pápulas violáceas.'),
('Enfermedades Ampollares', 'Las enfermedades ampollares son trastornos autoinmunes de la piel que causan la formación de ampollas o vesículas. Ejemplos incluyen pénfigo y penfigoide.'),
('Erupciones Cutáneas', 'Las erupciones son reacciones visibles en la piel que pueden deberse a alergias, infecciones, enfermedades autoinmunes o irritantes. Su apariencia y causa varían ampliamente.'),
('Celulitis, Impétigo y Otras Infecciones Bacterianas', 'Estas infecciones cutáneas son causadas por bacterias comunes como Staphylococcus aureus o Streptococcus pyogenes. Varían desde impétigo superficial hasta celulitis más profunda.'),
('Sarna, Enfermedad de Lyme y Otras Infestaciones y Picaduras', 'Estas condiciones son causadas por parásitos o picaduras de insectos. La sarna es altamente contagiosa y producida por ácaros; la enfermedad de Lyme proviene de la picadura de garrapatas infectadas.'),
('Eccema', 'El eccema es una enfermedad inflamatoria crónica de la piel caracterizada por brotes de sequedad, picazón e irritación. Puede ser desencadenado por alérgenos o factores ambientales.'),
('Queratosis Seborreica y Otros Tumores Benignos', 'Las queratosis seborreicas son crecimientos cutáneos benignos, comunes con la edad. Pueden confundirse con lesiones malignas por su aspecto verrugoso o pigmentado.'),
('Exantemas y Erupciones por Medicamentos', 'Estas son erupciones cutáneas causadas por infecciones virales o reacciones adversas a medicamentos. Suelen presentarse de forma súbita y afectar grandes áreas del cuerpo.'),
('Enfermedades Sistémicas con Manifestaciones Cutáneas', 'Algunas enfermedades internas como lupus, diabetes o enfermedades hepáticas pueden manifestarse en la piel. Estas señales cutáneas pueden ayudar en el diagnóstico de afecciones subyacentes.'),
('Pie de Atleta', 'El pie de atleta es una infección fúngica que afecta la piel entre los dedos del pie y la planta. Es común en ambientes húmedos y cálidos.'),
('Tatuajes', 'Aunque los tatuajes son decorativos, pueden causar reacciones adversas como infecciones, alergias o granulomas. Las complicaciones dependen del tipo de tinta y la técnica.'),
('Hongos en las Uñas', 'Los hongos en las uñas, o onicomicosis, afectan principalmente las uñas de los pies, causando cambios en su color, grosor y forma. Es más frecuente en personas con sudoración excesiva o calzado cerrado.'),
('Tiña, Candidiasis y Otras Infecciones Fúngicas', 'Las infecciones fúngicas de la piel pueden afectar distintas zonas del cuerpo y son causadas por dermatofitos o levaduras. Se propagan en ambientes húmedos y cálidos.'),
('Tiña Corporis (Dermatofitosis)', 'La tiña es una infección por hongos en la piel con forma característica de anillo. Afecta principalmente tronco, extremidades y cara.'),
('Urticaria (Ronchas)', 'La urticaria es una reacción cutánea caracterizada por la aparición repentina de ronchas rojas o pálidas que producen picazón intensa. Puede ser provocada por alergias, infecciones o estrés.'),
('Pérdida de Cabello, Alopecia y Otras Enfermedades Capilares', 'Las enfermedades del cabello incluyen la alopecia, que es la pérdida anormal de cabello, y otras condiciones que afectan el cuero cabelludo o el folículo piloso. Pueden tener causas genéticas, autoinmunes o ambientales.'),
('Tumores Vasculares', 'Los tumores vasculares son crecimientos anómalos formados por vasos sanguíneos. Pueden ser benignos, como los hemangiomas, o más complejos y raros.'),
('Piel Sana', 'La piel sana es uniforme, libre de lesiones, con buena hidratación y sin signos de inflamación o infección. Refleja buen cuidado cutáneo y salud general.'),
('Vasculitis', 'La vasculitis es una inflamación de los vasos sanguíneos que puede causar daño a la piel y otros órganos. Su presentación cutánea incluye manchas, úlceras o nódulos dolorosos.'),
('Herpes, VPH y Otras ETS', 'Estas infecciones de transmisión sexual afectan la piel y mucosas, y son causadas por virus como el herpes simple (HSV) y el virus del papiloma humano (VPH). Se transmiten por contacto íntimo.'),
('Varicela', 'La varicela es una infección viral muy contagiosa causada por el virus varicela-zóster. Afecta principalmente a niños y se caracteriza por erupciones con picazón.'),
('Enfermedades de la Luz y Trastornos de la Pigmentación', 'Estas condiciones incluyen alteraciones provocadas por la exposición al sol (como la fotodermatitis) y trastornos de pigmentación como el vitiligo o melasma.'),
('Herpes Zóster (Culebrilla)', 'El herpes zóster es una reactivación del virus de la varicela que causa una erupción dolorosa en un solo lado del cuerpo. Común en adultos mayores o personas inmunodeprimidas.'),
('Lupus y Otras Enfermedades del Tejido Conectivo', 'Estas enfermedades autoinmunes afectan la piel, las articulaciones y otros órganos. El lupus eritematoso sistémico es una de las formas más comunes, con signos cutáneos distintivos como el rash en alas de mariposa.'),
('Verrugas, Molusco Contagioso y Otras Infecciones Virales', 'Son infecciones cutáneas causadas por virus como el VPH y el poxvirus. Afectan comúnmente a niños y personas inmunocomprometidas.');

-- Insertar Relaciones Enfermedad-Síntoma
DO $$
DECLARE
    enf_id INT;
    sint_id INT;
BEGIN
    -- Acné y Rosácea
    SELECT id_enfermedad INTO enf_id FROM enfermedades WHERE nombre_enfermedad = 'Acné y Rosácea';
    FOR sint_id IN (SELECT id_sintoma FROM sintomas WHERE nombre_sintoma IN ('espinillas', 'pústulas', 'enrojecimiento facial', 'piel sensible', 'poros obstruidos', 'vasos sanguíneos visibles', 'ardor o escozor', 'protuberancias inflamadas'))
    LOOP
        INSERT INTO enfermedad_sintoma (id_enfermedad, id_sintoma) VALUES (enf_id, sint_id);
    END LOOP;

    -- Queratosis Actínica, Carcinoma Basocelular y Otras Lesiones Malignas
    SELECT id_enfermedad INTO enf_id FROM enfermedades WHERE nombre_enfermedad = 'Queratosis Actínica, Carcinoma Basocelular y Otras Lesiones Malignas';
    FOR sint_id IN (SELECT id_sintoma FROM sintomas WHERE nombre_sintoma IN ('manchas ásperas y escamosas', 'protuberancias perladas', 'costras persistentes', 'lesiones que sangran', 'heridas que no sanan', 'piel engrosada', 'cambios de color en la piel'))
    LOOP
        INSERT INTO enfermedad_sintoma (id_enfermedad, id_sintoma) VALUES (enf_id, sint_id);
    END LOOP;

    -- Dermatitis Atópica
    SELECT id_enfermedad INTO enf_id FROM enfermedades WHERE nombre_enfermedad = 'Dermatitis Atópica';
    FOR sint_id IN (SELECT id_sintoma FROM sintomas WHERE nombre_sintoma IN ('piel seca', 'picazón intensa', 'enrojecimiento', 'descamación', 'grietas en la piel', 'engrosamiento de la piel', 'lesiones que supuran', 'irritación al rascarse'))
    LOOP
        INSERT INTO enfermedad_sintoma (id_enfermedad, id_sintoma) VALUES (enf_id, sint_id);
    END LOOP;

    -- Celulitis Bacteriana
    SELECT id_enfermedad INTO enf_id FROM enfermedades WHERE nombre_enfermedad = 'Celulitis Bacteriana';
    FOR sint_id IN (SELECT id_sintoma FROM sintomas WHERE nombre_sintoma IN ('enrojecimiento', 'hinchazón', 'dolor localizado', 'calor en la zona afectada', 'fiebre', 'piel sensible', 'rayas rojas', 'sensación de tensión en la piel'))
    LOOP
        INSERT INTO enfermedad_sintoma (id_enfermedad, id_sintoma) VALUES (enf_id, sint_id);
    END LOOP;

    -- Impétigo Bacteriano
    SELECT id_enfermedad INTO enf_id FROM enfermedades WHERE nombre_enfermedad = 'Impétigo Bacteriano';
    FOR sint_id IN (SELECT id_sintoma FROM sintomas WHERE nombre_sintoma IN ('llagas rojizas', 'ampollas', 'costras color miel', 'picazón', 'piel irritada', 'lesiones con pus', 'enrojecimiento'))
    LOOP
        INSERT INTO enfermedad_sintoma (id_enfermedad, id_sintoma) VALUES (enf_id, sint_id);
    END LOOP;

    -- Lesiones Malignas
    SELECT id_enfermedad INTO enf_id FROM enfermedades WHERE nombre_enfermedad = 'Lesiones Malignas';
    FOR sint_id IN (SELECT id_sintoma FROM sintomas WHERE nombre_sintoma IN ('crecimiento anormal', 'sangrado espontáneo', 'cambio de color', 'bordes irregulares', 'picazón persistente', 'dolor en la lesión', 'ulceración'))
    LOOP
        INSERT INTO enfermedad_sintoma (id_enfermedad, id_sintoma) VALUES (enf_id, sint_id);
    END LOOP;

    -- Melanoma, Cáncer de Piel, Nevos y Lunares
    SELECT id_enfermedad INTO enf_id FROM enfermedades WHERE nombre_enfermedad = 'Melanoma, Cáncer de Piel, Nevos y Lunares';
    FOR sint_id IN (SELECT id_sintoma FROM sintomas WHERE nombre_sintoma IN ('lunares asimétricos', 'bordes irregulares', 'cambios de color', 'aumento de tamaño', 'sangrado', 'picazón', 'nuevas manchas oscuras'))
    LOOP
        INSERT INTO enfermedad_sintoma (id_enfermedad, id_sintoma) VALUES (enf_id, sint_id);
    END LOOP;

    -- Hongos en las Uñas y Otras Enfermedades Ungueales
    SELECT id_enfermedad INTO enf_id FROM enfermedades WHERE nombre_enfermedad = 'Hongos en las Uñas y Otras Enfermedades Ungueales';
    FOR sint_id IN (SELECT id_sintoma FROM sintomas WHERE nombre_sintoma IN ('uñas engrosadas', 'cambio de color', 'fragilidad', 'desprendimiento de la uña', 'olor desagradable', 'dolor', 'deformidad ungueal'))
    LOOP
        INSERT INTO enfermedad_sintoma (id_enfermedad, id_sintoma) VALUES (enf_id, sint_id);
    END LOOP;

    -- Larva Migrans Cutánea
    SELECT id_enfermedad INTO enf_id FROM enfermedades WHERE nombre_enfermedad = 'Larva Migrans Cutánea';
    FOR sint_id IN (SELECT id_sintoma FROM sintomas WHERE nombre_sintoma IN ('lesiones en forma de serpiente', 'picazón intensa', 'enrojecimiento', 'hinchazón', 'sensación de movimiento bajo la piel', 'vesículas', 'dolor leve'))
    LOOP
        INSERT INTO enfermedad_sintoma (id_enfermedad, id_sintoma) VALUES (enf_id, sint_id);
    END LOOP;

    -- Hiedra Venenosa y Otras Dermatitis de Contacto
    SELECT id_enfermedad INTO enf_id FROM enfermedades WHERE nombre_enfermedad = 'Hiedra Venenosa y Otras Dermatitis de Contacto';
    FOR sint_id IN (SELECT id_sintoma FROM sintomas WHERE nombre_sintoma IN ('erupción cutánea', 'enrojecimiento', 'ampollas', 'picazón intensa', 'descamación', 'hinchazón localizada', 'ardor'))
    LOOP
        INSERT INTO enfermedad_sintoma (id_enfermedad, id_sintoma) VALUES (enf_id, sint_id);
    END LOOP;

    -- Lesiones Benignas
    SELECT id_enfermedad INTO enf_id FROM enfermedades WHERE nombre_enfermedad = 'Lesiones Benignas';
    FOR sint_id IN (SELECT id_sintoma FROM sintomas WHERE nombre_sintoma IN ('protuberancias suaves', 'lunares estables', 'cambios mínimos en tamaño o color', 'lesiones no dolorosas', 'superficie cerosa o escamosa', 'bordes definidos'))
    LOOP
        INSERT INTO enfermedad_sintoma (id_enfermedad, id_sintoma) VALUES (enf_id, sint_id);
    END LOOP;

    -- Psoriasis, Liquen Plano y Enfermedades Relacionadas
    SELECT id_enfermedad INTO enf_id FROM enfermedades WHERE nombre_enfermedad = 'Psoriasis, Liquen Plano y Enfermedades Relacionadas';
    FOR sint_id IN (SELECT id_sintoma FROM sintomas WHERE nombre_sintoma IN ('placas escamosas', 'pápulas planas y violáceas', 'picazón', 'descamación', 'engrosamiento de la piel', 'cambios en uñas', 'lesiones en mucosas'))
    LOOP
        INSERT INTO enfermedad_sintoma (id_enfermedad, id_sintoma) VALUES (enf_id, sint_id);
    END LOOP;

    -- Enfermedades Ampollares
    SELECT id_enfermedad INTO enf_id FROM enfermedades WHERE nombre_enfermedad = 'Enfermedades Ampollares';
    FOR sint_id IN (SELECT id_sintoma FROM sintomas WHERE nombre_sintoma IN ('ampollas grandes y tensas', 'vesículas', 'dolor en la piel', 'enrojecimiento alrededor de las lesiones', 'descamación', 'lesiones que supuran', 'úlceras'))
    LOOP
        INSERT INTO enfermedad_sintoma (id_enfermedad, id_sintoma) VALUES (enf_id, sint_id);
    END LOOP;

    -- Erupciones Cutáneas
    SELECT id_enfermedad INTO enf_id FROM enfermedades WHERE nombre_enfermedad = 'Erupciones Cutáneas';
    FOR sint_id IN (SELECT id_sintoma FROM sintomas WHERE nombre_sintoma IN ('enrojecimiento', 'inflamación', 'manchas o ronchas', 'picazón', 'descamación', 'ampollas', 'cambios en la textura de la piel'))
    LOOP
        INSERT INTO enfermedad_sintoma (id_enfermedad, id_sintoma) VALUES (enf_id, sint_id);
    END LOOP;

    -- Celulitis, Impétigo y Otras Infecciones Bacterianas
    SELECT id_enfermedad INTO enf_id FROM enfermedades WHERE nombre_enfermedad = 'Celulitis, Impétigo y Otras Infecciones Bacterianas';
    FOR sint_id IN (SELECT id_sintoma FROM sintomas WHERE nombre_sintoma IN ('enrojecimiento', 'dolor', 'calor en la piel', 'ampollas o costras', 'inflamación', 'fiebre', 'piel sensible', 'lesiones con pus'))
    LOOP
        INSERT INTO enfermedad_sintoma (id_enfermedad, id_sintoma) VALUES (enf_id, sint_id);
    END LOOP;

    -- Sarna, Enfermedad de Lyme y Otras Infestaciones y Picaduras
    SELECT id_enfermedad INTO enf_id FROM enfermedades WHERE nombre_enfermedad = 'Sarna, Enfermedad de Lyme y Otras Infestaciones y Picaduras';
    FOR sint_id IN (SELECT id_sintoma FROM sintomas WHERE nombre_sintoma IN ('picazón intensa', 'erupciones cutáneas', 'líneas finas bajo la piel', 'enrojecimiento', 'fatiga', 'dolores musculares', 'lesiones en forma de diana'))
    LOOP
        INSERT INTO enfermedad_sintoma (id_enfermedad, id_sintoma) VALUES (enf_id, sint_id);
    END LOOP;

    -- Eccema
    SELECT id_enfermedad INTO enf_id FROM enfermedades WHERE nombre_enfermedad = 'Eccema';
    FOR sint_id IN (SELECT id_sintoma FROM sintomas WHERE nombre_sintoma IN ('piel seca', 'picazón persistente', 'enrojecimiento', 'grietas en la piel', 'vesículas', 'engrosamiento cutáneo', 'descamación'))
    LOOP
        INSERT INTO enfermedad_sintoma (id_enfermedad, id_sintoma) VALUES (enf_id, sint_id);
    END LOOP;

    -- Queratosis Seborreica y Otros Tumores Benignos
    SELECT id_enfermedad INTO enf_id FROM enfermedades WHERE nombre_enfermedad = 'Queratosis Seborreica y Otros Tumores Benignos';
    FOR sint_id IN (SELECT id_sintoma FROM sintomas WHERE nombre_sintoma IN ('lesiones elevadas', 'color marrón o negro', 'superficie cerosa o verrugosa', 'no dolorosas', 'cambios lentos en tamaño', 'bordes definidos'))
    LOOP
        INSERT INTO enfermedad_sintoma (id_enfermedad, id_sintoma) VALUES (enf_id, sint_id);
    END LOOP;

    -- Exantemas y Erupciones por Medicamentos
    SELECT id_enfermedad INTO enf_id FROM enfermedades WHERE nombre_enfermedad = 'Exantemas y Erupciones por Medicamentos';
    FOR sint_id IN (SELECT id_sintoma FROM sintomas WHERE nombre_sintoma IN ('manchas rojas', 'ronchas', 'picazón', 'fiebre', 'descamación', 'hinchazón', 'malestar general', 'lesiones simétricas'))
    LOOP
        INSERT INTO enfermedad_sintoma (id_enfermedad, id_sintoma) VALUES (enf_id, sint_id);
    END LOOP;

    -- Enfermedades Sistémicas con Manifestaciones Cutáneas
    SELECT id_enfermedad INTO enf_id FROM enfermedades WHERE nombre_enfermedad = 'Enfermedades Sistémicas con Manifestaciones Cutáneas';
    FOR sint_id IN (SELECT id_sintoma FROM sintomas WHERE nombre_sintoma IN ('lesiones variables según la enfermedad', 'cambios de color en la piel', 'úlceras', 'erupciones en zonas específicas', 'caída de cabello', 'hinchazón', 'fragilidad capilar'))
    LOOP
        INSERT INTO enfermedad_sintoma (id_enfermedad, id_sintoma) VALUES (enf_id, sint_id);
    END LOOP;

    -- Pie de Atleta
    SELECT id_enfermedad INTO enf_id FROM enfermedades WHERE nombre_enfermedad = 'Pie de Atleta';
    FOR sint_id IN (SELECT id_sintoma FROM sintomas WHERE nombre_sintoma IN ('descamación', 'picazón entre los dedos', 'mal olor', 'enrojecimiento', 'grietas en la piel', 'ardor', 'vesículas pequeñas'))
    LOOP
        INSERT INTO enfermedad_sintoma (id_enfermedad, id_sintoma) VALUES (enf_id, sint_id);
    END LOOP;

    -- Tatuajes
    SELECT id_enfermedad INTO enf_id FROM enfermedades WHERE nombre_enfermedad = 'Tatuajes';
    FOR sint_id IN (SELECT id_sintoma FROM sintomas WHERE nombre_sintoma IN ('enrojecimiento prolongado', 'hinchazón', 'picazón persistente', 'bultos', 'infección localizada', 'cambios en el color del tatuaje', 'formación de costras o úlceras'))
    LOOP
        INSERT INTO enfermedad_sintoma (id_enfermedad, id_sintoma) VALUES (enf_id, sint_id);
    END LOOP;

    -- Hongos en las Uñas
    SELECT id_enfermedad INTO enf_id FROM enfermedades WHERE nombre_enfermedad = 'Hongos en las Uñas';
    FOR sint_id IN (SELECT id_sintoma FROM sintomas WHERE nombre_sintoma IN ('uñas engrosadas', 'color amarillento o marrón', 'fragilidad', 'desprendimiento parcial de la uña', 'mal olor', 'dolor leve', 'deformidad'))
    LOOP
        INSERT INTO enfermedad_sintoma (id_enfermedad, id_sintoma) VALUES (enf_id, sint_id);
    END LOOP;

    -- Tiña, Candidiasis y Otras Infecciones Fúngicas
    SELECT id_enfermedad INTO enf_id FROM enfermedades WHERE nombre_enfermedad = 'Tiña, Candidiasis y Otras Infecciones Fúngicas';
    FOR sint_id IN (SELECT id_sintoma FROM sintomas WHERE nombre_sintoma IN ('manchas circulares con borde elevado', 'picazón', 'descamación', 'enrojecimiento', 'grietas en la piel', 'vesículas', 'olor desagradable'))
    LOOP
        INSERT INTO enfermedad_sintoma (id_enfermedad, id_sintoma) VALUES (enf_id, sint_id);
    END LOOP;

    -- Tiña Corporis (Dermatofitosis)
    SELECT id_enfermedad INTO enf_id FROM enfermedades WHERE nombre_enfermedad = 'Tiña Corporis (Dermatofitosis)';
    FOR sint_id IN (SELECT id_sintoma FROM sintomas WHERE nombre_sintoma IN ('lesiones circulares con bordes elevados', 'descamación central', 'picazón', 'enrojecimiento', 'lesiones que se agrandan', 'apariencia anular'))
    LOOP
        INSERT INTO enfermedad_sintoma (id_enfermedad, id_sintoma) VALUES (enf_id, sint_id);
    END LOOP;

    -- Urticaria (Ronchas)
    SELECT id_enfermedad INTO enf_id FROM enfermedades WHERE nombre_enfermedad = 'Urticaria (Ronchas)';
    FOR sint_id IN (SELECT id_sintoma FROM sintomas WHERE nombre_sintoma IN ('ronchas elevadas', 'picazón intensa', 'enrojecimiento', 'hinchazón transitoria', 'cambios rápidos en la forma de las lesiones', 'desaparición espontánea', 'ardor leve'))
    LOOP
        INSERT INTO enfermedad_sintoma (id_enfermedad, id_sintoma) VALUES (enf_id, sint_id);
    END LOOP;

    -- Pérdida de Cabello, Alopecia y Otras Enfermedades Capilares
    SELECT id_enfermedad INTO enf_id FROM enfermedades WHERE nombre_enfermedad = 'Pérdida de Cabello, Alopecia y Otras Enfermedades Capilares';
    FOR sint_id IN (SELECT id_sintoma FROM sintomas WHERE nombre_sintoma IN ('pérdida de cabello en parches', 'calvicie difusa', 'debilitamiento del cabello', 'picazón en el cuero cabelludo', 'inflamación', 'costras', 'cambios en la textura del cabello'))
    LOOP
        INSERT INTO enfermedad_sintoma (id_enfermedad, id_sintoma) VALUES (enf_id, sint_id);
    END LOOP;

    -- Tumores Vasculares
    SELECT id_enfermedad INTO enf_id FROM enfermedades WHERE nombre_enfermedad = 'Tumores Vasculares';
    FOR sint_id IN (SELECT id_sintoma FROM sintomas WHERE nombre_sintoma IN ('lesiones rojizas o violáceas', 'crecimientos elevados', 'sangrado ocasional', 'cambio de tamaño con el tiempo', 'dolor si se inflaman', 'calor local'))
    LOOP
        INSERT INTO enfermedad_sintoma (id_enfermedad, id_sintoma) VALUES (enf_id, sint_id);
    END LOOP;

    -- Piel Sana
    SELECT id_enfermedad INTO enf_id FROM enfermedades WHERE nombre_enfermedad = 'Piel Sana';
    FOR sint_id IN (SELECT id_sintoma FROM sintomas WHERE nombre_sintoma IN ('textura uniforme', 'hidratación adecuada', 'color homogéneo', 'ausencia de lesiones', 'elasticidad normal', 'sin picazón ni irritación'))
    LOOP
        INSERT INTO enfermedad_sintoma (id_enfermedad, id_sintoma) VALUES (enf_id, sint_id);
    END LOOP;

    -- Vasculitis
    SELECT id_enfermedad INTO enf_id FROM enfermedades WHERE nombre_enfermedad = 'Vasculitis';
    FOR sint_id IN (SELECT id_sintoma FROM sintomas WHERE nombre_sintoma IN ('manchas rojizas o moradas', 'petequias', 'úlceras cutáneas', 'dolor en la piel', 'inflamación localizada', 'fiebre', 'fatiga'))
    LOOP
        INSERT INTO enfermedad_sintoma (id_enfermedad, id_sintoma) VALUES (enf_id, sint_id);
    END LOOP;

    -- Herpes, VPH y Otras ETS
    SELECT id_enfermedad INTO enf_id FROM enfermedades WHERE nombre_enfermedad = 'Herpes, VPH y Otras ETS';
    FOR sint_id IN (SELECT id_sintoma FROM sintomas WHERE nombre_sintoma IN ('ampollas dolorosas', 'lesiones genitales', 'picazón', 'ardor al orinar', 'verrugas genitales', 'úlceras recurrentes', 'enrojecimiento'))
    LOOP
        INSERT INTO enfermedad_sintoma (id_enfermedad, id_sintoma) VALUES (enf_id, sint_id);
    END LOOP;

    -- Varicela
    SELECT id_enfermedad INTO enf_id FROM enfermedades WHERE nombre_enfermedad = 'Varicela';
    FOR sint_id IN (SELECT id_sintoma FROM sintomas WHERE nombre_sintoma IN ('ampollas llenas de líquido', 'picazón intensa', 'manchas rojas', 'fiebre', 'malestar general', 'costras al cicatrizar'))
    LOOP
        INSERT INTO enfermedad_sintoma (id_enfermedad, id_sintoma) VALUES (enf_id, sint_id);
    END LOOP;

    -- Enfermedades de la Luz y Trastornos de la Pigmentación
    SELECT id_enfermedad INTO enf_id FROM enfermedades WHERE nombre_enfermedad = 'Enfermedades de la Luz y Trastornos de la Pigmentación';
    FOR sint_id IN (SELECT id_sintoma FROM sintomas WHERE nombre_sintoma IN ('manchas blancas o oscuras', 'sensibilidad al sol', 'enrojecimiento', 'ardor al exponerse al sol', 'pérdida de pigmento', 'hiperpigmentación localizada'))
    LOOP
        INSERT INTO enfermedad_sintoma (id_enfermedad, id_sintoma) VALUES (enf_id, sint_id);
    END LOOP;

    -- Herpes Zóster (Culebrilla)
    SELECT id_enfermedad INTO enf_id FROM enfermedades WHERE nombre_enfermedad = 'Herpes Zóster (Culebrilla)';
    FOR sint_id IN (SELECT id_sintoma FROM sintomas WHERE nombre_sintoma IN ('dolor localizado', 'ampollas agrupadas', 'sensación de ardor', 'picazón', 'erupción unilateral', 'hormigueo previo a la erupción', 'costras al cicatrizar'))
    LOOP
        INSERT INTO enfermedad_sintoma (id_enfermedad, id_sintoma) VALUES (enf_id, sint_id);
    END LOOP;

    -- Lupus y Otras Enfermedades del Tejido Conectivo
    SELECT id_enfermedad INTO enf_id FROM enfermedades WHERE nombre_enfermedad = 'Lupus y Otras Enfermedades del Tejido Conectivo';
    FOR sint_id IN (SELECT id_sintoma FROM sintomas WHERE nombre_sintoma IN ('erupciones en mejillas y nariz', 'fatiga', 'dolor articular', 'fotosensibilidad', 'úlceras orales', 'caída de cabello', 'piel inflamada'))
    LOOP
        INSERT INTO enfermedad_sintoma (id_enfermedad, id_sintoma) VALUES (enf_id, sint_id);
    END LOOP;

    -- Verrugas, Molusco Contagioso y Otras Infecciones Virales
    SELECT id_enfermedad INTO enf_id FROM enfermedades WHERE nombre_enfermedad = 'Verrugas, Molusco Contagioso y Otras Infecciones Virales';
    FOR sint_id IN (SELECT id_sintoma FROM sintomas WHERE nombre_sintoma IN ('protuberancias elevadas', 'superficie rugosa (verrugas)', 'lesiones con centro umbilicado (molusco)', 'picazón', 'irritación local', 'crecimiento lento', 'distribución en grupos'))
    LOOP
        INSERT INTO enfermedad_sintoma (id_enfermedad, id_sintoma) VALUES (enf_id, sint_id);
    END LOOP;
END $$;
