import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../environments/environment.prod';

export interface Enfermedad {
  id_enfermedad: number;
  nombre_enfermedad: string;
  descripcion?: string;
}

@Injectable({
  providedIn: 'root'
})
export class EnfermedadService {

  private apiUrl = `${environment.apiUrl}`;

  constructor(private http: HttpClient) { }

  getEnfermedades(): Observable<Enfermedad[]> {
    return this.http.get<Enfermedad[]>(`${this.apiUrl}/enfermedades/`);
  }

  getEnfermedad(id: number): Observable<Enfermedad> {
    return this.http.get<Enfermedad>(`${this.apiUrl}/enfermedades/${id}`);
  }
}
