// src/app/app.routes.ts

import { Routes } from "@angular/router";
import { ComoFuncionaComponent } from "./components/como-funciona/como-funciona.component";
import { EnfermeadesComponent } from "./components/enfermeades/enfermeades.component";
import { InicioComponent } from "./components/inicio/inicio.component";
import { ContactoComponent } from "./components/contacto/contacto.component";
import { EncontrarDermatologoComponent } from "./components/encontrar-dermatologo/encontrar-dermatologo.component";

export const appRoutes: Routes = [
  { path: '', component: InicioComponent },
  { path: 'inicio', component: InicioComponent },
  { path: 'como-funciona', component: ComoFuncionaComponent },
  { path: 'enfermedades', component: EnfermeadesComponent },
  { path: 'contacto', component: ContactoComponent },
  { path: 'encontrar-dermatologo', component: EncontrarDermatologoComponent},
  { path: '**', redirectTo: 'inicio' }
];
