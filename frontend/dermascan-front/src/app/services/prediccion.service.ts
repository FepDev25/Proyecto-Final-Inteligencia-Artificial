import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../environments/environment.prod';

export interface PosibleCondicion {
  id_posible_condicion: number;
  id_prediccion: number;
  nombre_condicion: string;
  nombre_interno?: string;
  porcentaje?: number;
}

export interface Prediccion {
  id_prediccion: number;
  id_enfermedad?: number;
  url_imagen: string;
  imagen_url?: string;
  url_audio?: string;
  resumen?: string;
  porcentaje_coincidencia?: number;
  fecha: string;
  enfermedad?: {
    id_enfermedad: number;
    nombre_enfermedad: string;
    descripcion?: string;
  };
  posibles_condiciones: PosibleCondicion[];
}

@Injectable({
  providedIn: 'root'
})
export class PrediccionService {

  private apiUrl = environment.apiUrl;

  constructor(private http: HttpClient) { }

  /**
   * Envía una imagen al backend y recibe el diagnóstico.
   */
  predecir(file: File): Observable<any> {
    const formData = new FormData();
    formData.append('file', file);

    return this.http.post(`${this.apiUrl}/predict`, formData);
  }

  /**
   * Envía un texto y recibe el audio generado (MP3).
   */
  generarAudio(texto: string): Observable<Blob> {
    return this.http.post(
      `${this.apiUrl}/tts`,
      { text: texto },
      { responseType: 'blob' }
    );
  }

  /**
   * Obtiene el historial de predicciones.
   */
  getPredicciones(): Observable<Prediccion[]> {
    return this.http.get<Prediccion[]>(`${this.apiUrl}/predicciones/`);
  }

  /**
   * Obtiene una predicción específica por ID.
   */
  getPrediccion(id: number): Observable<Prediccion> {
    return this.http.get<Prediccion>(`${this.apiUrl}/predicciones/${id}`);
  }

  /**
   * Genera la URL completa para acceder a una imagen.
   */
  getImagenUrl(nombreImagen: string): string {
    return `${this.apiUrl}/images/${nombreImagen}`;
  }
}
