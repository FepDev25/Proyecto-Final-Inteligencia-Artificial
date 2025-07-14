import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';

@Component({
  selector: 'app-faq',
  imports: [CommonModule],
  templateUrl: './faq.component.html',
  styleUrl: './faq.component.css'
})
export class FaqComponent {
  faqs = [
    {
      pregunta: '¿Qué tan preciso es el diagnóstico de DermaScan AI?',
      respuesta: 'Nuestro sistema tiene una precisión promedio del 92% en comparación con diagnósticos dermatológicos profesionales, según estudios clínicos. Sin embargo, el diagnóstico final siempre debe ser confirmado por un médico especialista.',
      abierta: false
    },
    {
      pregunta: '¿Qué tipo de imágenes debo subir para obtener los mejores resultados?',
      respuesta: 'Para obtener los mejores resultados, sube fotos con buena iluminación, enfoque claro y que muestren claramente el área afectada. Evita fotos borrosas, con sombras fuertes o con maquillaje/cremas que puedan ocultar las características de la piel.',
      abierta: false
    },
    {
      pregunta: '¿DermaScan AI puede diagnosticar cáncer de piel?',
      respuesta: 'Nuestro sistema puede identificar características sospechosas que podrían indicar cáncer de piel, pero no debe usarse como herramienta de diagnóstico definitivo. Cualquier lesión sospechosa debe ser evaluada inmediatamente por un dermatólogo.',
      abierta: false
    },
    {
      pregunta: '¿Cómo protege DermaScan AI mi privacidad y datos médicos?',
      respuesta: 'Todas las imágenes y datos personales se almacenan de forma segura y encriptada. No compartimos información personal con terceros sin tu consentimiento explícito. Puedes eliminar tus datos en cualquier momento desde la configuración de tu cuenta.',
      abierta: false
    }
  ];

  toggle(index: number): void {
    this.faqs[index].abierta = !this.faqs[index].abierta;
  }
}
