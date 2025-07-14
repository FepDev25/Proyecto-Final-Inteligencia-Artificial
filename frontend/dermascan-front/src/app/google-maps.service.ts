import { Injectable } from '@angular/core';
import { environment } from './environments/environment';

@Injectable({
  providedIn: 'root'
})
export class GoogleMapsService {
  private apiKey = environment.googleApiKey;
  private mapsLoaded = false;

  constructor() { }

  loadScript(): Promise<void> {
    return new Promise((resolve, reject) => {
      if (this.mapsLoaded) {
        resolve();
        return;
      }

      const script = document.createElement('script');
      script.src = `https://maps.googleapis.com/maps/api/js?key=${this.apiKey}&libraries=places`;
      script.async = true;
      script.defer = true;
      script.onload = () => {
        this.mapsLoaded = true;
        resolve();
      };
      script.onerror = (error) => reject(error);
      document.head.appendChild(script);
    });
  }
}
