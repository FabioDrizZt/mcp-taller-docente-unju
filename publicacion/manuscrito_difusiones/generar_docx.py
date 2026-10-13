import docx
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
import re
import os

doc = docx.Document()

# Anonimización estricta de metadatos del documento Word (evaluación a doble ciego):
doc.core_properties.author = ""
doc.core_properties.last_modified_by = ""
doc.core_properties.comments = ""
doc.core_properties.title = "Artículo Original - DIFUSIONES"

# Configuración de página A4 y márgenes requeridos por DIFUSIONES:
# Superior e inferior 2.5 cm; derecho e izquierdo 3.0 cm
section = doc.sections[0]
section.page_width = Cm(21.0)
section.page_height = Cm(29.7)
section.top_margin = Cm(2.5)
section.bottom_margin = Cm(2.5)
section.left_margin = Cm(3.0)
section.right_margin = Cm(3.0)

# Estilo Normal: Times New Roman, 12pt, interlineado sencillo
style = doc.styles['Normal']
style.font.name = 'Times New Roman'
style.font.size = Pt(12)
style.font.color.rgb = RGBColor(0, 0, 0)
style.paragraph_format.line_spacing = 1.0
style.paragraph_format.space_after = Pt(6)
style.paragraph_format.space_before = Pt(0)

script_dir = os.path.dirname(os.path.abspath(__file__))
md_path = os.path.join(script_dir, 'articulo_original.md')
fig_path = os.path.join(script_dir, 'Figura_1_Arquitectura_MCP_HITL.png')
out_docx = os.path.join(script_dir, 'articulo_original.docx')

with open(md_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

def set_cell_borders(cell, top=None, bottom=None):
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(
        r'<w:tcBorders xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        rf'<w:top w:val="{top if top else "none"}" w:sz="6" w:space="0" w:color="auto"/>'
        r'<w:left w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
        rf'<w:bottom w:val="{bottom if bottom else "none"}" w:sz="6" w:space="0" w:color="auto"/>'
        r'<w:right w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
        r'</w:tcBorders>'
    )
    tcPr.append(tcBorders)

def add_formatted_runs(paragraph, text, base_font_size=12):
    parts = re.split(r'(\*\*.*?\*\*|\*.*?\*|`.*?`)', text)
    for part in parts:
        if not part:
            continue
        if part.startswith('**') and part.endswith('**'):
            r = paragraph.add_run(part[2:-2])
            r.bold = True
        elif part.startswith('*') and part.endswith('*'):
            r = paragraph.add_run(part[1:-1])
            r.italic = True
        elif part.startswith('`') and part.endswith('`'):
            r = paragraph.add_run(part[1:-1])
            r.font.name = 'Consolas'
            r.font.size = Pt(base_font_size - 1.5)
            continue
        else:
            r = paragraph.add_run(part)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(base_font_size)

in_table = False
table_lines = []

for line in lines:
    raw = line.strip()
    
    # Manejo de tabla Markdown
    if raw.startswith('|') and raw.endswith('|'):
        in_table = True
        table_lines.append(raw)
        continue
    elif in_table:
        in_table = False
        rows_data = [r.strip('|').split('|') for r in table_lines if not re.match(r'^[\|\s:\-]+$', r)]
        table_lines = []
        if rows_data:
            t = doc.add_table(rows=len(rows_data), cols=len(rows_data[0]))
            t.alignment = WD_TABLE_ALIGNMENT.CENTER
            for r_idx, row in enumerate(rows_data):
                for c_idx, val in enumerate(row):
                    cell = t.cell(r_idx, c_idx)
                    p = cell.paragraphs[0]
                    p.text = ''
                    p.paragraph_format.line_spacing = 1.0
                    p.paragraph_format.space_after = Pt(3)
                    p.paragraph_format.space_before = Pt(3)
                    if c_idx > 0:
                        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT if r_idx > 0 else WD_ALIGN_PARAGRAPH.CENTER
                    else:
                        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                    add_formatted_runs(p, val.strip(), base_font_size=10)
                    if r_idx == 0:
                        for run in p.runs:
                            run.bold = True
                        set_cell_borders(cell, top='single', bottom='single')
                    elif r_idx == len(rows_data) - 1:
                        set_cell_borders(cell, bottom='single')
                    else:
                        set_cell_borders(cell)
            # No se agrega doc.add_paragraph() vacío para que la nota APA quede pegada inmediatamente debajo de la tabla

    if not raw or raw == '---':
        continue
        
    # Inserción de Figura 1 (reemplazo de marcador)
    if '[Insertar Figura 1 aquí]' in raw:
        if os.path.exists(fig_path):
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(6)
            run = p.add_run()
            run.add_picture(fig_path, width=Cm(15.2))
        continue

    # Título principal (Centrado, Mayúsculas, Negrita)
    if raw.startswith('# '):
        t_text = raw[2:].strip().replace('*', '')
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(8)
        run = p.add_run(t_text)
        run.bold = True
        run.font.size = Pt(12)
        run.font.name = 'Times New Roman'
        continue

    # Encabezados principales H2 (Mayúsculas, Negrita, Centrados según directrices DIFUSIONES)
    if raw.startswith('## '):
        t_text = raw[3:].strip()
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(6)
        run = p.add_run(t_text)
        run.bold = True
        run.font.size = Pt(12)
        run.font.name = 'Times New Roman'
        continue

    # Subtítulos H3 (Minúsculas, Negrita, Izquierda según directrices DIFUSIONES)
    if raw.startswith('### '):
        t_text = raw[4:].strip()
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run(t_text)
        run.bold = True
        run.font.size = Pt(12)
        run.font.name = 'Times New Roman'
        continue

    # Formato especial APA 7 para número de Figura y Tabla
    if raw in ('**Figura 1**', '**Tabla 1**'):
        p = doc.add_paragraph()
        p.paragraph_format.line_spacing = 1.0
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(2)
        run = p.add_run(raw[2:-2])
        run.bold = True
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)
        continue

    # Formato especial APA 7 para títulos de figuras y tablas (en cursiva justo después del número)
    if raw.startswith('*Arquitectura sociotécnica') or raw.startswith('*Participación de los asistentes') or raw.startswith('*Progresión de los participantes'):
        p = doc.add_paragraph()
        p.paragraph_format.line_spacing = 1.0
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(6)
        run = p.add_run(raw.strip('*'))
        run.italic = True
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)
        continue

    # Formato especial APA 7 para notas de figuras y tablas (*Nota.* ...)
    if raw.startswith('*Nota.*'):
        p = doc.add_paragraph()
        p.paragraph_format.line_spacing = 1.0
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(12)
        # 10 pt para notas según norma APA 7
        add_formatted_runs(p, raw, base_font_size=10)
        continue

    # Párrafo normal de texto
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.0
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.space_before = Pt(0)
    add_formatted_runs(p, raw, base_font_size=12)

doc.save(out_docx)
print(f"Éxito: Archivo Word generado y actualizado en {out_docx}")
