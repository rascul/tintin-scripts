create table chars (
  name text primary key
);

create table rent_locations (
  id integer primary key autoincrement,
  name text unique not null
);

create table rent_items (
  char text,
  rentid integer,
  name text not null,
  foreign key(char) references chars(name),
  foreign key(rentid) references rent_locations(id)
);
