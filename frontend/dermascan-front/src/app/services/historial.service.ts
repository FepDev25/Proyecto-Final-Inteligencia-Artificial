import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../environments/environment';

export interface Prediccion {
  id_prediccion: number;
  id_enfermedad: number | null;
  url_imagen: string;
  url_audio: string | null;
  resumen: string | null;
  porcentaje_coincidencia: number | null;
  fecha: string;
  enfermedad?: {
    nombre_enfermedad: string;
  };
}

@Injectable({
  providedIn: 'root'
})
export class HistorialService {

  private apiUrl = `${environment.apiUrl}`;

  constructor(private http: HttpClient) { }

  getHistorial(page: number, limit: number): Observable<Prediccion[]> {
    const params = new HttpParams()
      .set('skip', page.toString())
      .set('limit', limit.toString());
    return this.http.get<Prediccion[]>(`${this.apiUrl}/predicciones`, { params });
  }
}
