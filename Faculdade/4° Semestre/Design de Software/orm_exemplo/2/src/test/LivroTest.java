package test;

import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityManagerFactory;
import jakarta.persistence.Persistence;
import model.Livro;
import model.Editora;

public class LivroTest {
	
	public static void main(String[] args) {
		
		Editora editora = new Editora("Editora Moderna");
		Livro livro = new Livro("E o vento levou", "E levou tudo mesmo", editora);
		
		EntityManagerFactory emf = Persistence.createEntityManagerFactory("bibliotecaPU");
		EntityManager em = emf.createEntityManager();
		
		em.getTransaction().begin();
		em.persist(editora);
		em.persist(livro);
		em.getTransaction().commit();
		
		em.close();
		emf.close();
		
	}

}
