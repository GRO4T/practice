package com.gro4t.redditclone.repository;

import com.gro4t.redditclone.model.Post;
import com.gro4t.redditclone.model.Subreddit;
import com.gro4t.redditclone.model.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface PostRepository extends JpaRepository<Post, Long> {
    List<Post> findAllBySubreddit(Subreddit subreddit);

    List<Post> findByUser(User user);
}
