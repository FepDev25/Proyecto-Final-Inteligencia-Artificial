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
      pregunta: '¿Qué tan confiable es DermaScan AI como herramienta de apoyo diagnóstico?',
      respuesta: 'Nuestro sistema tiene una precisión promedio del 92% en comparación con diagnósticos dermatológicos de especialistas, según estudios clínicos. Es una herramienta de apoyo que complementa el criterio clínico profesional, no lo reemplaza.',
      abierta: false
    },
    {
      pregunta: '¿Qué características deben tener las imágenes para obtener resultados óptimos?',
      respuesta: 'Para obtener los mejores resultados de análisis, las imágenes deben tener iluminación adecuada, enfoque nítido y mostrar claramente la lesión o área de interés. Evite imágenes con sombras excesivas, desenfoque o elementos que puedan interferir con la visualización de las características dermatológicas.',
      abierta: false
    },
    {
      pregunta: '¿Puede DermaScan AI detectar indicadores de cáncer de piel?',
      respuesta: 'Nuestro sistema puede identificar características morfológicas que podrían sugerir malignidad, proporcionando información valiosa para el análisis clínico. Sin embargo, el diagnóstico definitivo de cáncer debe basarse en la evaluación clínica completa y confirmación histopatológica.',
      abierta: false
    },
    {
      pregunta: '¿Cómo se manejan los datos de las imágenes y la privacidad de los pacientes?',
      respuesta: 'Todas las imágenes y datos se procesan de forma segura y encriptada, cumpliendo con estándares de privacidad médica. Los datos no se comparten con terceros y se pueden eliminar del sistema según las políticas de retención establecidas en su institución.',
      abierta: false
    }
  ];

  toggle(index: number): void {
    this.faqs[index].abierta = !this.faqs[index].abierta;
  }
}
