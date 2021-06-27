package com.gro4t.redditclone.service;

import com.gro4t.redditclone.dto.SubredditDto;
import com.gro4t.redditclone.exceptions.SpringRedditException;
import com.gro4t.redditclone.model.Subreddit;
import com.gro4t.redditclone.repository.SubredditRepository;
import com.gro4t.redditclone.mapper.SubredditMapper;
import lombok.AllArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.stream.Collectors;

@Service
@AllArgsConstructor
@Slf4j
public class SubredditService {
    private final SubredditRepository subredditRepository;
    private final SubredditMapper subredditMapper;

    @Transactional
    public SubredditDto save(SubredditDto subredditDto){
        Subreddit savedSubreddit = subredditRepository.save(subredditMapper.mapDtoToSubreddit(subredditDto));
        subredditDto.setId(savedSubreddit.getId());
        return subredditDto;
    }


    @Transactional(readOnly = true)
    public List<SubredditDto> getAll() {
         return subredditRepository.findAll()
                 .stream()
                 .map(subredditMapper::mapSubredditToDto)
                 .collect(Collectors.toList());
    }

    public SubredditDto getSubreddit(Long id) {
        Subreddit subreddit = subredditRepository.findById(id)
                .orElseThrow(
                        () -> new SpringRedditException("No subreddit found with id : " + id)
                );
        return subredditMapper.mapSubredditToDto(subreddit);
    }
}
