--SELECT * FROM KOLBSTYLETESTE_TENTATIVA
--SELECT * FROM KOLBSTYLETESTE_RESPOSTA
--SELECT * FROM KOLBSTYLETESTE_ESTILO
--SELECT * FROM KOLBSTYLETESTE_FORMAAPRENDIZAGEM
--SELECT * FROM KOLBSTYLETESTE_OPCAO
--SELECT * FROM KOLBSTYLETESTE_QUESTAO
--SELECT * FROM KOLBSTYLETESTE_TESTE
--SELECT * FROM USUARIOS_PERFIL
--SELECT * FROM AUTH_USER
--SELECT * FROM AUTH_USER_GROUPS
--SELECT * FROM CADASTROS_INSTITUICAO
--SELECT * FROM CADASTROS_TURMA

-- TENTATIVA ALUNO
SELECT * 
  FROM KOLBSTYLETESTE_TENTATIVA 
  WHERE 1=1
    AND USUARIO_ID = 3                          
    AND CONCLUIU =1
    
-- RESPOSTA TENTATIVA ALUNO
SELECT OP.DESCRICAO,
       R.VALOR,
       F.NOME
  FROM KOLBSTYLETESTE_RESPOSTA R
       INNER JOIN KOLBSTYLETESTE_OPCAO OP ON OP.ID = R.OPCAO_ID
       INNER JOIN KOLBSTYLETESTE_FORMAAPRENDIZAGEM F ON F.ID = OP.FORMA_APRENDIZAGEM_ID
  WHERE 1=1
    AND R.TENTATIVA_ID = 25
    
-- RESULTADO TENTATIVA
   SELECT SUM(VALOR) AS VALOR,
          NOME
     FROM (
        SELECT OP.DESCRICAO,
               R.VALOR,
               F.NOME
          FROM KOLBSTYLETESTE_RESPOSTA R
               INNER JOIN KOLBSTYLETESTE_OPCAO OP ON OP.ID = R.OPCAO_ID
               INNER JOIN KOLBSTYLETESTE_FORMAAPRENDIZAGEM F ON F.ID = OP.FORMA_APRENDIZAGEM_ID
          WHERE 1=1
            AND R.TENTATIVA_ID = 25
            ) X
            GROUP BY NOME

-- ESTILO PREDOMINANTE (TENTATIVA)
 WITH ESTILO AS (
      SELECT SUM(VALOR) AS VALOR,
             NOME,
             TENTATIVA_ID,
             USUARIO_ID,
             DATA
        FROM (
           SELECT OP.DESCRICAO, 
                  R.VALOR,
                  F.NOME,
                  R.TENTATIVA_ID,
                  T.USUARIO_ID,
                  T.DATA
             FROM KOLBSTYLETESTE_TENTATIVA T
                  INNER JOIN KOLBSTYLETESTE_RESPOSTA R ON R.TENTATIVA_ID = T.ID
                  INNER JOIN KOLBSTYLETESTE_OPCAO OP ON OP.ID = R.OPCAO_ID
                  INNER JOIN KOLBSTYLETESTE_FORMAAPRENDIZAGEM F ON F.ID = OP.FORMA_APRENDIZAGEM_ID
             WHERE 1=1
               AND R.TENTATIVA_ID = 25
               --AND T.USUARIO_ID = 2
               ) X
               GROUP BY NOME, TENTATIVA_ID, USUARIO_ID, DATA
             )    
 SELECT MAX(VALOR) AS VALOR, 
        ESTILO,
        TENTATIVA_ID,
        USUARIO_ID,
        DATA
   FROM (
      SELECT SUM(VALOR) AS VALOR, 'ASSIMILADOR' AS ESTILO, TENTATIVA_ID, USUARIO_ID, DATA FROM ESTILO  WHERE NOME IN ('Observação Reflexiva','Conceituação Abstrato')
      UNION 
      SELECT SUM(VALOR) AS VALOR, 'CONVERGENTE' AS ESTILO, TENTATIVA_ID, USUARIO_ID, DATA FROM ESTILO  WHERE NOME IN ('Conceituação Abstrato','Experimentação Ativa')
      UNION 
      SELECT SUM(VALOR) AS VALOR, 'DIVERGENTE ' AS ESTILO, TENTATIVA_ID, USUARIO_ID, DATA FROM ESTILO  WHERE NOME IN ('Experiência Concreta','Observação Reflexiva')
      UNION 
      SELECT SUM(VALOR) AS VALOR, 'ACOMODADOR ' AS ESTILO, TENTATIVA_ID, USUARIO_ID, DATA FROM ESTILO  WHERE NOME IN ('Experimentação Ativa','Experiência Concreta')
      )  
      
      
 -- ESTILO PREDOMINANTE OUTRA FORMA (USUARIO)
 WITH ESTILO AS (
      SELECT SUM(VALOR) AS VALOR,
             NOME,
             TENTATIVA_ID,
             USUARIO_ID,
             DATA
        FROM (
           SELECT OP.DESCRICAO, 
                  R.VALOR,
                  F.NOME,
                  R.TENTATIVA_ID,
                  T.USUARIO_ID,
                  T.DATA
             FROM KOLBSTYLETESTE_TENTATIVA T
                  INNER JOIN KOLBSTYLETESTE_RESPOSTA R ON R.TENTATIVA_ID = T.ID
                  INNER JOIN KOLBSTYLETESTE_OPCAO OP ON OP.ID = R.OPCAO_ID
                  INNER JOIN KOLBSTYLETESTE_FORMAAPRENDIZAGEM F ON F.ID = OP.FORMA_APRENDIZAGEM_ID
             WHERE 1=1
               --AND R.TENTATIVA_ID = 25
               AND T.USUARIO_ID = 2
               ) X
               GROUP BY NOME, TENTATIVA_ID, USUARIO_ID, DATA
             )    

  SELECT OR_ + CA AS ASSIMILADOR, 
         CA + EA  AS CONVERGENTE,
         EC + OR_ AS DIVERGENTE,
         EA + EC  AS ACOMODADOR,
         TENTATIVA_ID,
         DATA 
    FROM (      
        SELECT SUM(CASE WHEN (NOME = 'Conceituação Abstrato') THEN VALOR ELSE 0 END) AS CA,
               SUM(CASE WHEN (NOME = 'Experimentação Ativa')  THEN VALOR ELSE 0 END) AS EA,
               SUM(CASE WHEN (NOME = 'Experiência Concreta')  THEN VALOR ELSE 0 END) AS EC,
               SUM(CASE WHEN (NOME = 'Observação Reflexiva')  THEN VALOR ELSE 0 END) AS OR_,
               TENTATIVA_ID,
               DATA
        FROM ESTILO
        GROUP BY  TENTATIVA_ID, DATA
        ) A

               