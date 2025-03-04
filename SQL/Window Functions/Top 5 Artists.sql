with Top_10_Ranking_Frequency as (
select a.artist_id
      , count(*) as Ranking_Frequency
from artists a
join songs s
on a.artist_id = s.artist_id
join global_song_rank gsr
on s.song_id = gsr.song_id
where rank <= 10
group by a.artist_id),
song_appearance_ranking as (
select a.artist_name
      , dense_rank() over (order by trf.Ranking_Frequency desc) as artist_rank
from Top_10_Ranking_Frequency as trf
left join artists a
on a.artist_id = trf.artist_id)
select artist_name
      , artist_rank 
from song_appearance_ranking
where artist_rank <= 5
