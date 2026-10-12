from PIL import Image, ImageDraw, ImageFont
import os

width = 1800
height = 1260
img = Image.new('RGB', (width, height), color='#FFFFFF')
draw = ImageDraw.Draw(img)

# Paleta de colores sobria, moderna y de estándar académico
bg_header = '#1E293B'
c_capa1_bg = '#F8FAFC'
c_capa1_border = '#2563EB'
c_capa2_bg = '#F0FDF4'
c_capa2_border = '#059669'
c_capa3_bg = '#FEF2F2'
c_capa3_border = '#DC2626'
text_dark = '#0F172A'
text_muted = '#334155'

try:
    font_title = ImageFont.truetype('arial.ttf', 36)
    font_box_title = ImageFont.truetype('arialbd.ttf', 28)
    font_badge = ImageFont.truetype('arialbd.ttf', 22)
    font_col_head = ImageFont.truetype('arialbd.ttf', 24)
    font_regular = ImageFont.truetype('arial.ttf', 22)
    font_arrow = ImageFont.truetype('arialbd.ttf', 22)
except Exception:
    font_title = font_box_title = font_badge = font_col_head = font_regular = font_arrow = ImageFont.load_default()

# 1. Encabezado principal del diagrama
draw.rectangle([(60, 40), (1740, 125)], fill=bg_header)
draw.text((900, 82), 'ARQUITECTURA SOCIOTÉCNICA DE EVALUACIÓN CONTINUA ASISTIDA POR IA', fill='#FFFFFF', font=font_title, anchor='mm')

def draw_card(y_top, h, title, items, fill_c, border_c, badge_text):
    draw.rounded_rectangle([(60, y_top), (1740, y_top + h)], radius=14, fill=fill_c, outline=border_c, width=3)
    
    # Badge lateral
    badge_w = 260
    draw.rounded_rectangle([(80, y_top + 18), (80 + badge_w, y_top + 62)], radius=6, fill=border_c)
    draw.text((80 + badge_w / 2, y_top + 40), badge_text, fill='#FFFFFF', font=font_badge, anchor='mm')
    
    # Título de la capa
    draw.text((80 + badge_w + 25, y_top + 40), title, fill=text_dark, font=font_box_title, anchor='lm')
    
    # Línea divisoria
    draw.line([(80, y_top + 76), (1720, y_top + 76)], fill='#CBD5E1', width=2)
    
    # Columnas internas (3 módulos por capa)
    x_col_w = 520
    for idx, (head, desc) in enumerate(items):
        col_x = 90 + idx * (x_col_w + 30)
        draw.rounded_rectangle([(col_x, y_top + 92), (col_x + x_col_w, y_top + h - 22)], radius=8, fill='#FFFFFF', outline='#E2E8F0', width=2)
        draw.text((col_x + 20, y_top + 116), head, fill=border_c, font=font_col_head, anchor='la')
        
        lines = desc.split('\n')
        cur_y = y_top + 154
        for l in lines:
            draw.text((col_x + 20, cur_y), l, fill=text_muted, font=font_regular, anchor='la')
            cur_y += 30

# Capa 1: Gobernanza
items_c1 = [
    ('1.1 Identidad y Tono', '• AGENTS.md versionable\n• Rol pedagógico socrático\n• Prohibición de resolver tareas\n• Exigencia de evidencias'),
    ('1.2 Memoria y Cátedra', '• MEMORY.md persistente\n• Convenciones sintácticas\n• Criterios de compilación\n• Contexto curricular estable'),
    ('1.3 Rúbricas y Skills', '• Rúbricas en Markdown\n• Delimitadores XML/YAML\n• Procedimiento pericial\n• Salida estructurada JSON')
]
draw_card(155, 305, 'CAPA 1: GOBERNANZA CONTEXTUAL EN TEXTO PLANO', items_c1, c_capa1_bg, c_capa1_border, 'GOBERNANZA')

# Flecha conectora 1 -> 2
draw.text((900, 485), '▼  Directivas contextuales y restricciones operativas  ▼', fill='#2563EB', font=font_arrow, anchor='mm')

# Capa 2: Protocolo MCP
items_c2 = [
    ('2.1 Agente de Razonamiento', '• Modelo de lenguaje (LLM)\n• Invocación de herramientas\n• Planificación estructurada\n• Auditoría de contratos SDD'),
    ('2.2 Protocolo MCP Local', '• Estándar abierto (Anthropic)\n• Servidor Filesystem seguro\n• Directorios permitidos\n• Principio de mínimo privilegio'),
    ('2.3 Entorno de Inspección', '• Lectura pericial de código\n• Ejecución de scripts/tests\n• Trazabilidad de operaciones\n• Sandbox local sin nube')
]
draw_card(515, 305, 'CAPA 2: INTEROPERABILIDAD PROTOCOLIZADA (MCP)', items_c2, c_capa2_bg, c_capa2_border, 'PROTOCOLO MCP')

# Flecha conectora 2 -> 3
draw.text((900, 845), '▼  Prediagnóstico técnico con cita de evidencias observables  ▼', fill='#059669', font=font_arrow, anchor='mm')

# Capa 3: HITL
items_c3 = [
    ('3.1 Auditoría Docente', '• Verificación de citas\n• Neutralización de alucinaciones\n• Detección de falsos positivos\n• Control de rigor académico'),
    ('3.2 Juicio Pedagógico', '• Modulación comunicativa\n• Preguntas socráticas activas\n• Andamiaje personalizado\n• Autoridad humana indelegable'),
    ('3.3 Devolución Formativa', '• Devolución no punitiva\n• Oportunidad de refactorización\n• Retroalimentación continua\n• Trazabilidad para el alumno')
]
draw_card(875, 305, 'CAPA 3: SUPERVISIÓN HUMANA ACTIVA (HUMAN-IN-THE-LOOP - HITL)', items_c3, c_capa3_bg, c_capa3_border, 'SUPERVISIÓN HITL')

# Guardar a 300 DPI
script_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(script_dir, 'Figura_1_Arquitectura_MCP_HITL.png')
img.save(out_path, 'PNG', dpi=(300, 300))
print('Figura generada con éxito en:', out_path)