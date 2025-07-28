import { Component, OnInit } from '@angular/core';
import { HistorialService, Prediccion } from '../../services/historial.service';
import { CommonModule } from '@angular/common';
import { environment } from '../../environments/environment.prod';

@Component({
  selector: 'app-historial',
  imports: [CommonModule],
  templateUrl: './historial.component.html',
  styleUrls: ['./historial.component.css']
})
export class HistorialComponent implements OnInit {
  historial: Prediccion[] = [];
  page = 0;
  limit = 20;
  loading = false;
  expandedItems: Set<number> = new Set();

  constructor(private historialService: HistorialService) { }

  ngOnInit(): void {
    this.loadHistorial();
  }

  getImageUrl(imageUrl: string): string {
    if (!imageUrl) return '';
    return `${environment.apiUrl}${imageUrl}`;
  }

  onImageError(event: any): void {
    console.error('Error loading image:', event);
    // La imagen por defecto se manejará con el atributo onerror del HTML
  }

  loadHistorial(): void {
    this.loading = true;
    this.historialService.getHistorial(this.page, this.limit).subscribe(data => {
      this.historial = [...this.historial, ...data];
      this.page++;
      this.loading = false;
    });
  }

  onScroll(): void {
    if (!this.loading) {
      this.loadHistorial();
    }
  }

  toggleExpanded(index: number): void {
    if (this.expandedItems.has(index)) {
      this.expandedItems.delete(index);
    } else {
      this.expandedItems.add(index);
    }
  }

  isExpanded(index: number): boolean {
    return this.expandedItems.has(index);
  }

  getTruncatedText(text: string | null, maxLength: number = 150): string {
    if (!text) return '';
    return text.length > maxLength ? text.substring(0, maxLength) + '...' : text;
  }
}
