import { Component, OnInit, Input } from '@angular/core';
import { faArrowUp, faArrowDown } from '@fortawesome/free-solid-svg-icons';
import { PostModel } from '../post-model';
import { VoteService } from '../../shared/vote.service';
import { AuthService } from 'src/app/auth/shared/auth.service';
import { PostService } from '../post.service';
import { ToastrService } from 'ngx-toastr';
import { VoteRequest } from './vote-request';
import { VoteType } from './vote-type';
import { throwError } from 'rxjs';

@Component({
  selector: 'app-vote-button',
  templateUrl: './vote-button.component.html',
  styleUrls: ['./vote-button.component.css']
})
export class VoteButtonComponent implements OnInit {
  @Input() post: PostModel;
  voteRequest: VoteRequest;
  faArrowUp = faArrowUp;
  faArrowDown = faArrowDown;
  upvoteColor: string;
  downvoteColor: string;

  constructor(private voteService: VoteService, private authService: AuthService,
              private postService: PostService, private toastr: ToastrService) {
    this.voteRequest = {
      voteType: undefined,
      postId: undefined
    };
  }

  ngOnInit(): void {
    this.updateVoteDetails();
  }

  downvotePost(): void {
    this.voteRequest.voteType = VoteType.DOWNVOTE;
    this.vote();
    this.upvoteColor = '';
  }

  upvotePost(): void {
    this.voteRequest.voteType = VoteType.UPVOTE;
    this.vote();
    this.downvoteColor = '';
  }

  private vote(): void {
    this.voteRequest.postId = this.post.id;
    this.voteService.vote(this.voteRequest).subscribe(() => {
      this.updateVoteDetails();
    }, error => {
      if (error.status === 409) {
        if (this.voteRequest.voteType === VoteType.UPVOTE) {
          this.toastr.error('You\'ve already upvoted this post');
        }
        else {
          this.toastr.error('You\'ve already downvoted this post');
        }
      }
      else {
        this.toastr.error(error.message);
      }
      throwError(error);
    });
  }

  private updateVoteDetails(): void {
    this.postService.getPost(this.post.id).subscribe(post => {
      this.post = post;
    });
  }

}
