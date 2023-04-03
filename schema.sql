create table Films;
use Films;
create table FilmsRevenue(
    Id int  AUTO_INCREMENT primary key ,
    RankFilm int ,
    ReleaseDate datetime ,
    MovieTitle nvarchar(100) not null ,
    ProductionBudget double not null ,
    WorldwideGross double not null ,
    DomesticGross double not null
);