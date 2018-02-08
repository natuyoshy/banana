import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { AgmCoreModule } from '@agm/core';



import { AppComponent } from './app.component';
import { ShopListComponent } from './shop-list/shop-list.component';


@NgModule({
  declarations: [
    AppComponent,
    ShopListComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule,
    AgmCoreModule.forRoot({
      apiKey: 'AIzaSyBwOAd5LOBQsAAqxqwleDyRKnnN_hDgKZ0'
    })
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
