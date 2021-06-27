package com.gro4t.redditclone.repository;

import com.gro4t.redditclone.model.Post;
import com.gro4t.redditclone.model.User;
import com.gro4t.redditclone.model.Vote;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface VoteRepository extends JpaRepository<Vote, Long> {
    Optional<Vote> findTopByPostAndUserOrderByVoteIdDesc(Post post, User currentUser);
}
