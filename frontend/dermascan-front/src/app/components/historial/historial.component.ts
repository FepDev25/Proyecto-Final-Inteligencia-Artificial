import { Component, OnInit } from '@angular/core';
import { HistorialService, Prediccion } from '../../services/historial.service';
import { CommonModule } from '@angular/common';

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

  constructor(private historialService: HistorialService) { }

  ngOnInit(): void {
    this.loadHistorial();
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
}