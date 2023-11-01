package model;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;

@Entity
public class Livro {
    //O ID identifica a chave primaria
	@Id
	//A opcao IDENTITY é para o MySQL
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	private Long id;
	
	private String titulo;
	
	private String resumo;
	
	//vou usar o ManyToOne pois esta é a "tabela do muitos" que vai
	//fazer referencia a 1(one) na outra tabela
	@ManyToOne
	//O Join Column vai dizer qual coluna estará recebendo esta chave
	@JoinColumn(name="editora_id")
	private Editora editora;
	
	public Livro() {
		
	}
	
	public Livro(String titulo, String resumo, Editora editora) {
		this.titulo = titulo;
		this.resumo = resumo;
		this.editora = editora;
	}
	
	public Long getId() {
		return id;
	}
	
	public void setId(Long id) {
		this.id = id;
	}
	
	public String getTitulo() {
		return titulo;
	}
	
	public void setTitulo(String titulo) {
		this.titulo = titulo;
	}
	
	public String getResumo() {
		return resumo;
	}
	
	public void setResumo(String resumo) {
		this.resumo = resumo;
	}
	
	public Editora getEditora() {
		return editora;
	}
	
	public void setEditora(Editora editora) {
		this.editora = editora;
	}
	
}
