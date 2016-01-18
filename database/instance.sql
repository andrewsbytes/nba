
    \set table commonallplayers

    copy :table
    from '/Users/andrew/nba/parse/commonallplayers/commonallplayers_2014-15.csv'
    delimiter ','
    header
    quote '"'
    csv
    ;
  