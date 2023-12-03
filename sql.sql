drop table usuarios;
CREATE TABLE `usuarios` (
  `id` integer primary key AUTOINCREMENT ,
  `usuario` varchar(255) default NULL,
  `telefone` varchar(100) default NULL,
  `apikey` varchar(255)

);

CREATE TABLE `registros` (
  `id` integer primary key AUTOINCREMENT ,
  `usuario_id` varchar(255) default NULL,
  `registro` datetime default NULL,
  `created_at` datetime default null
);

INSERT INTO `usuarios` (`usuario`,`telefone`,`apikey`)
VALUES
  ("Lucas Suchy","555198742477","5376026");

INSERT INTO `usuarios` (`usuario`,`telefone`,`apikey`)
VALUES
  ("Krishna Eduardo","555198097732","2160075");

INSERT INTO `usuarios` (`usuario`,`telefone`,`apikey`)
VALUES
  ("Gabriel Varysco","555185741156","2212690");

select usuario, telefone, apikey from usuarios where usuario = 'Lucas Suchy';

update usuarios set apikey = 5376026 where id = 1;


truncate registros;
INSERT INTO `registros` (`usuario_id`,`registro`,`created_at`)
VALUES
  ("1",datetime('now', 'localtime'),datetime('now', 'localtime'));

SELECT datetime('now', 'localtime')
;
(col, 'PDT')

;
select * from registros where created_At < datetime('now', 'localtime', '-600 seconds') and usuario_id = ?