import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';


export class Sample {
  public id: number;
  public name: string;
}
export class Rs {
  public name: string;
  public latitude: number;
  public longitude: number;
  public category: string;
  public url : string;
  public address: string;
}

@Component( {
  selector: 'app-shop-list',
  templateUrl: './shop-list.component.html',
  styleUrls: ['./shop-list.component.css']
})

export class ShopListComponent implements OnInit {
  constructor(private http: HttpClient) { }
  sample: Sample;
  rs : Rs[];
  public obj: any;
  zoom: number = 8;
  lat: number = 35.681382;
  lng: number = 139.76608399999998;

  markers: Narker[] = [
  {
    lat: 35.675069,
    lng: 139.763328,
    draggable: true
  },
];

  ngOnInit(): void { }
  add(input): void {
    if (input) {
      // this.http.get<Sample>('/api/' + input).subscribe(data => {
      //   this.sample = data;
      //   console.log(input + 'の人');
      // });
      this.http.get<Rs>('/api/' + input).subscribe((data : any) => {
        this.rs = data.rest;
        for (let i = 0; i < data.rest.length; i++) {
            this.lat = parseFloat(data.rest[i].latitude);
            this.lng = parseFloat(data.rest[i].longitude);
            this.markers.push({
            lat: this.lat,
            lng: this.lng,
            draggable: true
          });
        }
        console.log(this.lat);
      });
    } else {
      console.log('値をいれんか！');
    }
  }

  addUser(id , name) : void {
     this.obj = { id: id, name: name };
     console.log(JSON.stringify(this.obj));
      this.http.post<any>('/api/', this.obj).subscribe((res: Response) => {});
   }
  }

 interface Narker {
    lat: number;
    lng: number;
    draggable: boolean;
  }
