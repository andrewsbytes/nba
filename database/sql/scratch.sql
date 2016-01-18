\a

select
  p.player_id,
  c.display_last_comma_first,
  1.0*sum(p.pts)/sum(gp) ppg,
  1.0*sum(fgm)/sum(fga) fg_pct,
  sum(min)/sum(gp) min,
  count(distinct p.season_id) seasons
from playercareerstats p
join (select distinct person_id, display_last_comma_first from commonallplayers) c
on p.player_id = c.person_id
group by 1,2
having count(distinct p.season_id) >= 5
order by 3 desc
limit 20
;
