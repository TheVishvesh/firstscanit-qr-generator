import segno
import io

def generate_artistic_qr(data, style='geometric', scale=10, output_buffer=None):
    style_configs = {
        'geometric': {'dark': '#2c3e50', 'light': '#ecf0f1', 'border': 2},
        'tribal': {'dark': '#8b4513', 'light': '#fff8dc', 'border': 3},
        'royal': {'dark': '#4a148c', 'light': '#f3e5f5', 'border': 2},
        'minimal': {'dark': '#000000', 'light': '#ffffff', 'border': 1}
    }
    
    config = style_configs.get(style, style_configs['geometric'])
    qr = segno.make(data, error='h')
    
    if output_buffer:
        qr.save(
            output_buffer,
            kind='png',
            scale=scale,
            dark=config['dark'],
            light=config['light'],
            border=config['border']
        )
    
    return qr
