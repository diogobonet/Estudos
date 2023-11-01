package test;


import java.util.Calendar;
import java.util.Date;
import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityManagerFactory;
import jakarta.persistence.Persistence;
import model.Cliente;
import model.Editora;
import model.Livro;
import model.Locacao;

public class LocacaoTest {
	
	public static void main(String[] args) {

		Calendar cal = Calendar.getInstance();
		cal.set(Calendar.YEAR, 2023);
		cal.set(Calendar.MONTH, Calendar.OCTOBER);
		cal.set(Calendar.DAY_OF_MONTH, 23);
		Date data = cal.getTime();
		
		Editora editora = new Editora("Editora Moderna");
		Livro livro = new Livro("E o vento levou", "E levou tudo mesmo", editora);
		
		Cliente cliente = new Cliente("Joao", "joao@gmail.com", "2323232", "3443-4434");
		
		Locacao locacao = new Locacao(data, livro, cliente); 
		
		EntityManagerFactory emf = Persistence.createEntityManagerFactory("bibliotecaPU");
		EntityManager em = emf.createEntityManager();
		
		em.getTransaction().begin();
		em.persist(editora);
		em.persist(livro);
		em.persist(cliente);
		em.persist(locacao);
		em.getTransaction().commit();
		
		em.close();
		emf.close();
		
	}

}
