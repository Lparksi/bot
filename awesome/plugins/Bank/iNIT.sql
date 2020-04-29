create table Bank
(
	ID BIGINT auto_increment,
	Balance BIGINT default 0 null ,
	QQ VARCHAR(20) not null unique,
	BAN BOOL default False null,
	constraint Bank_pk
		primary key (ID)
);
