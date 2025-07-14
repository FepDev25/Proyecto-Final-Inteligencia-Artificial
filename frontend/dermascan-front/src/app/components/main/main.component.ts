import { CommonModule } from '@angular/common';
import { Component, ElementRef, ViewChild } from '@angular/core';
import { PrediccionService } from '../../services/prediccion.service';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-main',
  imports: [CommonModule],
  templateUrl: './main.component.html',
  styleUrl: './main.component.css'
})
export class MainComponent {

  constructor(private prediccionService: PrediccionService) { }


  @ViewChild('skinImageInput') skinImageInput!: ElementRef<HTMLInputElement>;
  @ViewChild('imagePreview') imagePreview!: ElementRef<HTMLImageElement>;
  @ViewChild('previewArea') previewArea!: ElementRef<HTMLDivElement>;
  @ViewChild('previewPlaceholder') previewPlaceholder!: ElementRef<HTMLDivElement>;
  @ViewChild('progressFill') progressFill!: ElementRef<HTMLDivElement>;

  diagnosticoPrincipal: string = '';
  probabilidadPrincipal: number = 0;
  resumenPrincipal: string = '';
  otrasCondiciones: { condicion: string; sigla: string; probabilidad: number; }[] = [];
  previewImageUrl: string = '';
  textoExplicacion: string = '';
  audioUrl: string = '';
  sintomas: string[] = [];

  showUploadSection: boolean = true;
  showLoadingSection: boolean = false;
  showResultsSection: boolean = false;
  showAnalysisOptions: boolean = false;

  openFilePicker() {
    this.skinImageInput.nativeElement.click();
  }

  onFileSelected(event: Event) {
    const file = (event.target as HTMLInputElement).files?.[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (e) => {
      const imageUrl = e.target?.result as string;
      this.imagePreview.nativeElement.src = imageUrl;
      this.previewImageUrl = imageUrl;
      this.imagePreview.nativeElement.classList.remove('hidden');
      this.previewPlaceholder.nativeElement.classList.add('hidden');
      this.previewArea.nativeElement.classList.remove('hidden');
      this.showAnalysisOptions = true;
    };

    reader.readAsDataURL(file);
  }

  analyzeImage() {
    this.showUploadSection = false;
    this.showLoadingSection = true;

    const file = this.skinImageInput.nativeElement.files?.[0];
    if (!file) return;

    this.prediccionService.predecir(file).subscribe({
      next: (respuesta) => {
        this.diagnosticoPrincipal = respuesta.diagnostico_principal.condicion;
        this.probabilidadPrincipal = Math.round(respuesta.diagnostico_principal.probabilidad * 100);
        this.resumenPrincipal = respuesta.diagnostico_principal.resumen;
        this.otrasCondiciones = respuesta.otras_posibles_condiciones;
        this.textoExplicacion = respuesta.diagnostico_principal.texto_completo;
        this.sintomas = respuesta.diagnostico_principal.sintomas;

        this.showLoadingSection = false;
        this.showResultsSection = true;
        window.scrollTo({ top: 0, behavior: 'smooth' });

        this.prediccionService.generarAudio(this.textoExplicacion).subscribe({
          next: (audioBlob) => {
            this.audioUrl = URL.createObjectURL(audioBlob);
          },
          error: (error) => {
            console.error('Error al generar audio:', error);
          }
        });
      },
      error: (error) => {
        console.error('Error al analizar la imagen:', error);
        this.showLoadingSection = false;
      }
    });
  }



  scrollToUpload(uploadSection: HTMLElement) {
    uploadSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  onDragOver(event: DragEvent) {
    event.preventDefault();
    event.stopPropagation();
  }

  onDrop(event: DragEvent) {
    event.preventDefault();
    if (event.dataTransfer?.files.length) {
      this.skinImageInput.nativeElement.files = event.dataTransfer.files;
      const changeEvent = new Event('change');
      this.skinImageInput.nativeElement.dispatchEvent(changeEvent);
    }
  }

  reset() {
    this.showResultsSection = false;
    this.showUploadSection = true;
    this.showAnalysisOptions = false;
  }

  abrirDermatologos() {
    window.open('/encontrar-dermatologo', '_blank');
  }


}

