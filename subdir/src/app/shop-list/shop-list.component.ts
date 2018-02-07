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

  ngOnInit(): void {
    // this.http.get<Sample>('/api/3').subscribe(data => {
    //   this.sample = data;
    //   console.log(this.sample);
    // });
  }
  add(input): void {
    if (input) {
      this.http.get<Sample>('/api/' + input).subscribe(data => {
        this.sample = data;
        console.log(input + 'の人');
      });
    }
}

}

// 登録、全員分の表示
