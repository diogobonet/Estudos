package test;

import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityManagerFactory;
import jakarta.persistence.EntityTransaction;
import jakarta.persistence.Persistence;
import model.Editora;


public class EditoraTest {

		public static void main(String[] args) {
			
			Editora editora = new Editora("Saraiva");
			
			//Vai validar a conexao com o banco no arquivo persistence.xml
			EntityManagerFactory emf = Persistence.createEntityManagerFactory("bibliotecaPU");
			EntityManager em = emf.createEntityManager();
			
			em.getTransaction().begin();
			em.persist(editora);
			em.getTransaction().commit();
			
			em.close();
			emf.close();
			 
			 
		}
		
}
