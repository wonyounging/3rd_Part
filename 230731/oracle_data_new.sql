--drop table emp;
CREATE TABLE emp ( 
  empno     number primary key, 
  ename     varchar2(50), 
  job       varchar2(50), 
  mgr       number, 
  hiredate  date default sysdate, 
  sal       number,
  comm      number, 
  deptno    number);

insert into emp values (7369,'��ö��','���',7902,'2010-12-17',300,null,20);
insert into emp values (7499,'�̹μ�','�븮',7698,'2011-02-20',360,300,30);
insert into emp values (7521,'������','�븮',7698,'2012-02-22',425,500,30);
insert into emp values (7566,'�Ӽ���','����',7839,'2011-04-02',597,null,20);
insert into emp values (7654,'��ȣ��','�븮',7698,'2011-09-28',425,1400,30);
insert into emp values (7698,'�ڼ�ȯ','����',7839,'2021-05-01',585,null,30);
insert into emp values (7782,'�ձ�ö','����',7839,'2021-06-09',545,null,10);
insert into emp values (7788,'�ڱ�ȣ','����',7566,'2007-04-17',600,null,20);
insert into emp values (7839,'��ö��','��ǥ',null,'2011-11-17',900,null,10);
insert into emp values (7844,'�۸���','�븮',7698,'2011-09-08',450,0,30);
insert into emp values (7876,'Ȳ����','���',7788,'2017-05-23',310,null,20);
insert into emp values (7900,'�ڹ�ö','���',7698,'2011-12-03',395,null,30);
insert into emp values (7902,'����','����',7566,'2011-12-03',700,null,20);
insert into emp values (7934,'��ö��','���',7782,'2012-01-23',330,null,10);


--drop table dept;
CREATE TABLE dept (
  deptno   number primary key, 
  dname    varchar2(50));

insert into dept values (10,'������');
insert into dept values (20,'ȫ����');
insert into dept values (30,'��ȹ��');
insert into dept values (40,'������');




--drop table prof ;

create table prof(
 profno number primary key,
 pname  varchar2(10) not null, 
 position varchar2(20) not null,
 pay number(3) not null,
 hiredate  date not null,
 bonus number(4) ,
 majorno  number(3)
);

insert into prof
values(1001,'����ö','������',550,'2007-06-23',100,101);

insert into prof
values(1002,'��öȣ','�α���',380,'2016-01-30',60,101);

insert into prof
values (1003,'�۱⿵','������',270,'2019-03-22',null,101);

insert into prof
values (2001,'����','������',250,'2017-09-01',null,102);

insert into prof
values (2002,'�迵��','�α���',350,'2015-11-30',80,102);

insert into prof
values (2003,'�ֿ�ȣ','������',490,'2008-04-29',90,102);

insert into prof
values (3001,'�����','������',530,'2005-10-23',110,103);

insert into prof
values (3002,'������','������',330,'2018-07-01',50,103);

insert into prof
values (3003,'������','������',290,'2019-02-24',null,103);

insert into prof
values (4001,'�ɻ��','������',570,'2001-10-23',130,201);

insert into prof
values (4002,'�ּ���','������',330,'2019-08-30',null,201);

insert into prof
values (4003,'�ڿ���','������',310,'2019-12-01',50,202);

insert into prof
values (4004,'����ö','������',260,'2019-01-28',null,202);

insert into prof
values (4005,'������','������',500,'2005-09-18',80,203);

insert into prof 
values (4006,'����ȣ','������',220,'2020-06-28',null,301);

insert into prof
values (4007,'�㿵��','�α���',290,'2011-05-23',30,301);

#drop table major ;
create table major
( majorno number(3) primary key ,
  mname varchar2(30) not null
);

insert into major values (101,'��ǻ�Ͱ���');

insert into major values (102,'�����ͻ��̾�');

insert into major values (103,'����Ʈ�������');

insert into major values (201,'���ڰ���');

insert into major values (202,'������');

insert into major values (203,'ȭ�а���');

insert into major values (301,'����������');

#drop table stud ;

create table stud
( studno number primary key,
  sname   varchar2(10) not null,
  grade number ,
  majorno number,
  profno  number);

insert into stud values (201811,'������',4,101,1001);

insert into stud values (201812,'�����',4,102,2001);

insert into stud values (201813,'�̹ΰ�',4,103,3002);

insert into stud values (201814,'������',4,201,4001);

insert into stud values (201815,'�ڵ���',4,202,4003);

insert into stud values (201911,'�輱��',3,101,1002);

insert into stud values (201912,'�ſ���',3,102,2002);

insert into stud values (201913,'������',3,202,4003);

insert into stud values (201914,'���ڿ�',3,301,4007);

insert into stud values (201915,'�̼���',3,101,4001);

insert into stud values (202011,'������',2,101,1002);

insert into stud values (202012,'������',2,102,2001);

insert into stud values (202013,'�豤��',2,201,4002);

insert into stud values (202014,'�̹�ȣ',2,201,4003);

insert into stud values (202015,'����ȣ',2,301,4007);

insert into stud values (202111,'������',1,101,null);

insert into stud values (202112,'������',1,101,null);

insert into stud values (202113,'�ֿ���',1,201,null);

insert into stud values (202114,'������',1,102,null);

insert into stud values (202115,'������',1,101,null);



commit;
