import { Component } from '@angular/core';
import { FooterComponent } from '../footer/footer.component';
import { HeroComponent } from '../hero/hero.component';
import { MainComponent } from '../main/main.component';
import { FaqComponent } from '../faq/faq.component';

@Component({
  selector: 'app-inicio',
  imports: [MainComponent, HeroComponent, FaqComponent],
  templateUrl: './inicio.component.html',
  styleUrl: './inicio.component.css'
})
export class InicioComponent {

}
