package com.gro4t.redditclone.repository;

import com.gro4t.redditclone.model.Comment;
import com.gro4t.redditclone.model.Post;
import com.gro4t.redditclone.model.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface CommentRepository extends JpaRepository<Comment, Long> {
    List<Comment> findByPost(Post post);

    List<Comment> findAllByUser(User user);
}
