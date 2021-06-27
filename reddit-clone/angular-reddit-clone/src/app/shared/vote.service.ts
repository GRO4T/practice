import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { VoteRequest } from './vote-button/vote-request';

@Injectable({
  providedIn: 'root'
})
export class VoteService {

  constructor(private http: HttpClient) { }

  vote(voteRequest: VoteRequest): Observable<any> {
    return this.http.post('http://localhost:8080/api/votes/', voteRequest);
  }
}
