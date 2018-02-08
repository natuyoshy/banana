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
  title: string = 'My first AGM project';
  lat: number = 51.678418;
  lng: number = 7.809007;

  ngOnInit(): void { }
  add(input): void {
    if (input) {
      // this.http.get<Sample>('/api/' + input).subscribe(data => {
      //   this.sample = data;
      //   console.log(input + 'の人');
      // });
      this.http.get<Rs>('/api/' + input).subscribe(data => {
        this.rs = data.rest;
        console.log(data);
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
