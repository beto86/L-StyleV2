-- para a lista de Alunos: trazer todos usuarios = alunos que pertence a quele professor (o professor tem cadastrado por turmas, acredito que da para trazer pelas turmas cada aluno)
/* ALUNOS DO PROFESSOR */
WITH PROFESSOR AS (
SELECT UG.ID as prof_id, P.NOME_COMPLETO as professor,T.ID AS curso_id, T.NOME as turma, T.CURSO
  FROM AUTH_GROUP G
       INNER JOIN AUTH_USER_GROUPS UG ON G.ID = UG.GROUP_ID
       INNER JOIN USUARIOS_PERFIL P ON P.ID = UG.ID
       INNER JOIN CADASTROS_TURMA T ON T.USUARIO_ID = P.ID
 WHERE G.ID = 2   -- tras busca apenas professores
   AND UG.ID = 2   --seleciona id professor
 )
 SELECT P.PROF_ID, P.PROFESSOR, P.CURSO_ID, P.TURMA,P.ID as aluno_id,P.NOME_COMPLETO as aluno  
   FROM PROFESSOR P
        INNER JOIN CADASTROS_USER_TURMA UT ON UT.TURAMA_ID = P.CURSO_ID
        INNER JOIN USUARIOS_PERFIL P ON P.ID = UT.USER_ID
  -- verificar questao do 'ID do professor' pois como o 'usuario_id' do professor é o mesmo CAMPO do aluno, 
  -- da erro na hora de filtrar .. pois se filtrar para trazer um professor em especifico só vai trazer aquele id
  -- talvez se criar a tabela 'cadastro_user_turma' possa resolver
  
------------------------------------------------------------------------------------------------------------------------------  
--outra coisa se puder é:  trazer um atributo para o perfil informado qual Turma este perfil pertence
/* TURMAS DO ALUNO */    
SELECT P.ID, P.NOME_COMPLETO,UT.TURAMA_ID,T.NOME
  FROM USUARIOS_PERFIL P
       INNER JOIN CADASTROS_USER_TURMA UT ON UT.USER_ID = P.ID
       INNER JOIN CADASTROS_TURMA T ON T.ID = UT.turama_id
 WHERE P.ID = 5   
  -- nao tem como buscar turams dos alunos pois não tem um campo trazendo o id do aluno 
  --(acredito que o campo 'usuario_id' da tabela 'cadastros_turma' seja apenas pra ligar o professor )
  -- o ideal seria criar uma tabela 'cadastros_user_turma'

-------------------------------------------------------------------------------------------

/*
SELECT * FROM AUTH_GROUP
SELECT * FROM AUTH_USER_GROUPS
SELECT * FROM KOLBSTYLETESTE_TESTE
SELECT * FROM USUARIOS_PERFIL
SELECT * FROM CADASTROS_TURMA
SELECT * FROM CADASTROS_USER_TURMA
*/

/* PROFESSORES */
SELECT G.NAME, UG.ID, P.NOME_COMPLETO
  FROM AUTH_GROUP G
       INNER JOIN AUTH_USER_GROUPS UG ON G.ID = UG.GROUP_ID
       INNER JOIN USUARIOS_PERFIL P ON P.ID = UG.ID
 WHERE G.ID = 2

/* ALUNOS */
SELECT G.NAME, UG.ID, P.NOME_COMPLETO
  FROM AUTH_GROUP G
       INNER JOIN AUTH_USER_GROUPS UG ON G.ID = UG.GROUP_ID
       INNER JOIN USUARIOS_PERFIL P ON P.ID = UG.ID
 WHERE G.ID = 3
 
 /* TURMAS */
SELECT * FROM CADASTROS_TURMA    --verificar de que é esse usuario_id     (nao tem professor com id 2)

/* ALUNOS POR TURMA */
SELECT T.ID AS id_turma, T.NOME AS turma, UT.USER_ID, P.NOME_COMPLETO
  FROM CADASTROS_TURMA T
       INNER JOIN CADASTROS_USER_TURMA UT ON UT.TURAMA_ID = T.ID 
       INNER JOIN USUARIOS_PERFIL P ON P.ID = UT.USER_ID
 WHERE T.ID = 4


/* TRUMA PROFESOR */
SELECT P.ID, P.NOME_COMPLETO,T.ID AS curso_id, T.NOME, T.CURSO 
  FROM USUARIOS_PERFIL P 
       INNER JOIN CADASTROS_TURMA T ON T.USUARIO_ID = P.ID
 WHERE P.ID = 2 
  
------------------------------------------------------- 
CREATE TABLE cadastros_user_turma

  ( 
      id       INTEGER NOT NULL, 
      user_id  INTEGER NOT NULL, 
      turama_id INTEGER NOT NULL, 
      PRIMARY KEY (id), 
      FOREIGN KEY (user_id) REFERENCES "auth_user" , 
      FOREIGN KEY (turama_id) REFERENCES "cadastros_turma" 
      UNIQUE (id) 
  );
  
  INSERT INTO CADASTROS_USER_TURMA VALUES (4,1,4),(5,7,2),(6,5,4),(7,8,3),(8,5,2)
  
  SELECT * FROM CADASTROS_USER_TURMA

  
  


 