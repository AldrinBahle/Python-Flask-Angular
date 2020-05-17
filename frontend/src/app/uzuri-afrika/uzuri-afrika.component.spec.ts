import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { UzuriAfrikaComponent } from './uzuri-afrika.component';

describe('UzuriAfrikaComponent', () => {
  let component: UzuriAfrikaComponent;
  let fixture: ComponentFixture<UzuriAfrikaComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ UzuriAfrikaComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(UzuriAfrikaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
