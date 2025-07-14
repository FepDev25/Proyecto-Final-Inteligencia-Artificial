import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EnfermeadesComponent } from './enfermeades.component';

describe('EnfermeadesComponent', () => {
  let component: EnfermeadesComponent;
  let fixture: ComponentFixture<EnfermeadesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [EnfermeadesComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(EnfermeadesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
