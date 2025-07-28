import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { EnfermedadService, Enfermedad } from '../../services/enfermedad.service';

@Component({
  selector: 'app-enfermeades',
  imports: [CommonModule],
  templateUrl: './enfermeades.component.html',
  styleUrl: './enfermeades.component.css'
})
export class EnfermeadesComponent implements OnInit {
  enfermedades: Enfermedad[] = [];
  loading = true;

  constructor(private enfermedadService: EnfermedadService) { }

  ngOnInit(): void {
    this.loadEnfermedades();
  }

  loadEnfermedades(): void {
    this.enfermedadService.getEnfermedades().subscribe({
      next: (data) => {
        this.enfermedades = data;
        this.loading = false;
      },
      error: (error) => {
        console.error('Error al cargar enfermedades:', error);
        this.loading = false;
      }
    });
  }

  getIconClass(nombreEnfermedad: string): string {
    const nombre = nombreEnfermedad.toLowerCase();

    if (nombre.includes('acné') || nombre.includes('rosácea')) {
      return 'fas fa-circle text-6xl text-blue-500';
    } else if (nombre.includes('benigna') || nombre.includes('benign')) {
      return 'fas fa-check-circle text-6xl text-green-500';
    } else if (nombre.includes('eccema') || nombre.includes('dermatitis')) {
      return 'fas fa-allergies text-6xl text-orange-500';
    } else if (nombre.includes('infección') || nombre.includes('bacteriana') || nombre.includes('impétigo') || nombre.includes('celulitis')) {
      return 'fas fa-bug text-6xl text-red-400';
    } else if (nombre.includes('maligna') || nombre.includes('melanoma') || nombre.includes('cáncer') || nombre.includes('carcinoma')) {
      return 'fas fa-exclamation-triangle text-6xl text-red-600';
    } else if (nombre.includes('hongo') || nombre.includes('tiña') || nombre.includes('candidiasis')) {
      return 'fas fa-microscope text-6xl text-purple-500';
    } else if (nombre.includes('psoriasis') || nombre.includes('liquen')) {
      return 'fas fa-layer-group text-6xl text-indigo-500';
    } else if (nombre.includes('herpes') || nombre.includes('varicela') || nombre.includes('zóster')) {
      return 'fas fa-virus text-6xl text-red-500';
    } else if (nombre.includes('urticaria') || nombre.includes('ronchas')) {
      return 'fas fa-dot-circle text-6xl text-pink-500';
    } else if (nombre.includes('sana') || nombre.includes('healthy')) {
      return 'fas fa-heart text-6xl text-green-600';
    } else {
      return 'fas fa-stethoscope text-6xl text-gray-500';
    }
  }

  getColorClass(nombreEnfermedad: string): string {
    const nombre = nombreEnfermedad.toLowerCase();

    if (nombre.includes('maligna') || nombre.includes('melanoma') || nombre.includes('cáncer') || nombre.includes('carcinoma')) {
      return 'bg-red-50';
    } else if (nombre.includes('sana') || nombre.includes('healthy') || nombre.includes('benigna')) {
      return 'bg-green-50';
    } else if (nombre.includes('infección') || nombre.includes('bacteriana') || nombre.includes('herpes')) {
      return 'bg-red-50';
    } else {
      return 'bg-blue-50';
    }
  }
}
