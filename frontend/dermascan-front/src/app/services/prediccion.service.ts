import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../environments/environment';

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
}
