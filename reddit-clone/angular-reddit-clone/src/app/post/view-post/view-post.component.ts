import { Component, OnInit } from '@angular/core';
import { PostModel } from 'src/app/shared/post-model';
import { PostService } from 'src/app/shared/post.service';
import { ActivatedRoute, Router } from '@angular/router';
import { throwError } from 'rxjs';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { CommentRequest } from '../../comment/comment-request';
import { CommentService } from '../../comment/comment.service';

@Component({
  selector: 'app-view-post',
  templateUrl: './view-post.component.html',
  styleUrls: ['./view-post.component.css']
})
export class ViewPostComponent implements OnInit {
  postId: number;
  post: PostModel;
  commentForm: FormGroup;
  commentRequest: CommentRequest;
  comments: CommentRequest[];

  constructor(private postService: PostService, private activatedRoute: ActivatedRoute,
              private commentService: CommentService, private router: Router) {
    this.postId = this.activatedRoute.snapshot.params.id;
    this.commentForm = new FormGroup({
      text: new FormControl('', Validators.required)
    });
    this.commentRequest = {
      text: '',
      postId: this.postId
    };
  }

  ngOnInit(): void {
    this.getPostById();
  }

  postComment(): void {
    this.commentRequest.text = this.commentForm.get('text').value;
    this.commentService.postComment(this.commentRequest).subscribe(data => {
      this.commentForm.get('text').setValue('');
      this.getCommentsForPost();
    }, error => {
      throwError(error);
    });
  }

  private getPostById(): void {
    this.postService.getPost(this.postId).subscribe(data => {
      this.post = data;
    }, error => {
      throwError(error);
    });
  }

  private getCommentsForPost(): void {
    this.commentService.getAllCommentsForPost(this.postId).subscribe(data => {
      this.comments = data;
    }, error => {
      throwError(error);
    });
  }

}
