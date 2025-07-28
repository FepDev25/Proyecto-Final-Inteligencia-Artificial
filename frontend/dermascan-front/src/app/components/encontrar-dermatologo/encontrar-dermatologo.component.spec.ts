import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EncontrarDermatologoComponent } from './encontrar-dermatologo.component';

describe('EncontrarDermatologoComponent', () => {
  let component: EncontrarDermatologoComponent;
  let fixture: ComponentFixture<EncontrarDermatologoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [EncontrarDermatologoComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(EncontrarDermatologoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
