import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { CommentRequest } from './comment-request';

@Injectable({
  providedIn: 'root'
})
export class CommentService {

  constructor(private httpClient: HttpClient) { }

  getAllCommentsForPost(postId: number): Observable<any> {
    return this.httpClient.get('http://localhost:8080/api/comments/by-post/' + postId);
  }

  postComment(commentRequest: CommentRequest): Observable<any> {
    return this.httpClient.post('http://localhost:8080/api/comments', commentRequest);
  }

  getAllCommentsByUser(username: string): Observable<any> {
    return this.httpClient.get('http://localhost:8080/api/comments/by-user/' + username);
  }
}
