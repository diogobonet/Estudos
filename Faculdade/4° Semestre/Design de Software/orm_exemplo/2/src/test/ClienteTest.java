package test;

import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityManagerFactory;
import jakarta.persistence.Persistence;
import model.Cliente;

public class ClienteTest {

		public static void main(String[] args) {
			
			//Vai criar a tabela automaticamente e inserir o registro
			//Se a tabela ja estiver criada vai apenas inserir o registro nela
			Cliente cliente = new Cliente("Joao", "joao@gmail.com", "2323232", "3443-4434");
			
			//Vai validar a conexao com o banco no arquivo persistence.xml
			EntityManagerFactory emf = Persistence.createEntityManagerFactory("bibliotecaPU");
			EntityManager em = emf.createEntityManager();
			
			em.getTransaction().begin();
			em.persist(cliente);
			em.getTransaction().commit();
			
			em.close();
			emf.close();
			 
		}
		
}
