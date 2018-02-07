import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

export class Sample {
  public id: number;
  public name: string;
}

@Component( {
  selector: 'app-shop-list',
  templateUrl: './shop-list.component.html',
  styleUrls: ['./shop-list.component.css']
})

@Injectable()
export class ShopListComponent implements OnInit {
  constructor(private http: HttpClient) { }
  sample: Sample;
  public obj: any;

  ngOnInit(): void { }
  add(input): void {
    if (input) {
      this.http.get<Sample>('/api/' + input).subscribe(data => {
        this.sample = data;
        console.log(input + 'の人');
      });
    } else {
      console.log('値をいれんか！');
    }
  }

  addUser(id , name) {
    console.log(id, name);
    return false;
  }
}

// 登録、全員分の表示
