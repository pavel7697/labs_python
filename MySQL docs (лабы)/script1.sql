use first_db;
ALTER TABLE grow_teacher
CHANGE COLUMN phone phone bigint(11);
insert into teacher values( 2, 'Славик', 'Тоноян', 'Анушаванович', 89997775544, 'ton@hasagi.ru');
insert into teacher values( 3, 'Юрий', 'Гапанюк', 'Евгеньевич', 89997771133, 'y.gapanyk@hasagi.ru');

insert into pulpit values( 1, 'RT', 1890);
insert into pulpit values( 2, 'IU', 1968);