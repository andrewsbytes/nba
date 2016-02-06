------------------
-- Shot leaders --
------------------

\set table shotleaders

drop table if exists :table
;

create table :table as
select
  p.player_id,
  c.display_last_comma_first,
  round(1.0*sum(p.pts)/sum(p.gp),1) ppg,
  round(1.0*sum(p.fgm)/sum(p.fga),2) fg_pct,
  case
    when sum(p.fg3a) = 0 then 0
    else round(1.0*sum(p.fg3m)/sum(p.fg3a),2)
  end fg3_pct,
  -------------------------------------------
  -- sum(p.fg3a) fg3a, -- for 3 pt leaders --
  -------------------------------------------
  round(1.0*sum(p.ast)/sum(p.gp)) ast,
  round(1.0*sum(p.reb)/sum(p.gp)) reb,
  round(1.0*sum(p.stl)/sum(p.gp)) stl,
  round(1.0*sum(p.blk)/sum(p.gp)) blk,
  sum(p.min)/sum(p.gp) min,
  count(distinct p.season_id) seasons,
  min(split_part(season_id,'-',1)::int) season_start,
  max(split_part(season_id,'-',1)::int) season_end
from playercareerstats p
join (select distinct person_id, display_last_comma_first from commonallplayers) c
on p.player_id = c.person_id
group by 1,2
having count(distinct p.season_id) >= 5
-------------------------
-- For 3 point leaders --
-------------------------
-- and
-- case
--   when sum(p.fg3a) = 0 then 0
--   else round(1.0*sum(p.fg3m)/sum(p.fg3a),2)
-- end is not null
-- and sum(p.fg3a) > 99
-- order by fg3_pct desc
order by ppg desc
limit 20
;

\a

select
  s.*,
  rank() over (partition by player_id,display_last_comma_first order by season_id) season_no
from
( select
    p.player_id,
    c.display_last_comma_first,
    season_id,
    round(1.0*sum(p.pts)/sum(p.gp),1) ppg,
    round(1.0*sum(p.fgm)/sum(p.fga),2) fg_pct
  from playercareerstats p
  join (select distinct person_id, display_last_comma_first from commonallplayers) c
  on p.player_id = c.person_id
  join shotleaders s on p.player_id = s.player_id
  group by 1,2,3
) s
;

