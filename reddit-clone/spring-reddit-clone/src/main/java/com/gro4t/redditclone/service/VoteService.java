package com.gro4t.redditclone.service;

import com.gro4t.redditclone.dto.VoteDto;
import com.gro4t.redditclone.exceptions.PostNotFoundException;
import com.gro4t.redditclone.exceptions.SpringRedditException;
import com.gro4t.redditclone.model.Post;
import com.gro4t.redditclone.model.Vote;
import com.gro4t.redditclone.repository.PostRepository;
import com.gro4t.redditclone.repository.VoteRepository;
import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.Optional;

import static com.gro4t.redditclone.model.VoteType.UPVOTE;

@Service
@AllArgsConstructor
public class VoteService {
    private final VoteRepository voteRepository;
    private final PostRepository postRepository;
    private final AuthService authService;

    @Transactional
    public void vote(VoteDto voteDto) {
        Post post = postRepository.findById(voteDto.getPostId())
                .orElseThrow(() -> new PostNotFoundException("Post Not Found with ID - " + voteDto.getPostId()));
        Optional<Vote> voteByPostAndUser = voteRepository.
                findTopByPostAndUserOrderByVoteIdDesc(post, authService.getCurrentUser());
        if (voteByPostAndUser.isPresent() &&
                voteByPostAndUser.get().getVoteType()
                        .equals(voteDto.getVoteType())) {
            throw new SpringRedditException("You have already "
                    + voteDto.getVoteType() + "'d for this post");
        }

        // update vote count (if user previously voted we must update vote count by 2
        if (UPVOTE.equals(voteDto.getVoteType())) {
            post.setVoteCount(
                    post.getVoteCount() + (voteByPostAndUser.isPresent() ? 2 : 1)
            );
        } else {
            post.setVoteCount(
                    post.getVoteCount() - (voteByPostAndUser.isPresent() ? 2 : 1)
            );
        }
        voteRepository.save(mapToVote(voteDto, post));
        postRepository.save(post);
    }

    private Vote mapToVote(VoteDto voteDto, Post post) {
        return Vote.builder()
                .voteType(voteDto.getVoteType())
                .post(post)
                .user(authService.getCurrentUser())
                .build();
    }
}
