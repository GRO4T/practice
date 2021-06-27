import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { SignupRequest } from '../sign-up/signup-request';
import { LoginRequest } from '../login/login-request';
import { LoginResponse } from '../login/login-response';
import { Observable, throwError } from 'rxjs';
import { LocalStorageService } from 'ngx-webstorage';
import { map, tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  refreshTokenPayload = {
    refreshToken: this.getRefreshToken(),
    username: this.getUserName()
  };

  constructor(private httpClient: HttpClient,
              private localStorage: LocalStorageService) { }

  signup(signupRequest: SignupRequest): Observable<any>{
    return this.httpClient.post(
        'http://localhost:8080/api/auth/signup',
        signupRequest,
        { responseType: 'text'}
      );
  }

  login(loginRequest: LoginRequest): Observable<boolean> {
    return this.httpClient.post<LoginResponse>(
      'http://localhost:8080/api/auth/login',
      loginRequest
    ).pipe(map(data => {
      this.localStorage.store('authenticationToken', data.authenticationToken);
      this.localStorage.store('username', data.username);
      this.localStorage.store('refreshToken', data.refreshToken);
      this.localStorage.store('expiresAt', data.expiresAt);

      return true;
    }));
  }

  getJwtToken(): any {
    return this.localStorage.retrieve('authenticationToken');
  }

  refreshToken(): any {
    return this.httpClient.post<LoginResponse>('http://localhost:8080/api/auth/refresh/token',
      this.refreshTokenPayload)
      .pipe(tap(response => {
        this.localStorage.clear('authenticationToken');
        this.localStorage.clear('expiresAt');

        this.localStorage.store('authenticationToken',
          response.authenticationToken);
        this.localStorage.store('expiresAt', response.expiresAt);
      }));
  }

  getUserName(): any {
    return this.localStorage.retrieve('username');
  }

  getRefreshToken(): any {
    return this.localStorage.retrieve('refreshToken');
  }

  isLoggedIn(): boolean {
    return this.getJwtToken() != null;
  }

  logout(): void {
    this.httpClient.post(
      'http://localhost:8080/api/auth/logout',
      this.refreshTokenPayload,
      { responseType: 'text' }).subscribe(data => {
        console.log(data);
      }, error => {
        throwError(error);
      });

    this.localStorage.clear('authenticationToken');
    this.localStorage.clear('username');
    this.localStorage.clear('refreshToken');
    this.localStorage.clear('expiresAt');
  }
}
