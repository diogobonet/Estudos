package Atividade05;
public class ContaPrimosThread extends Thread{
	private int limiteMin, limiteMax;
	
	
	public ContaPrimosThread(int limiteMin, int limiteMax) {
		this.limiteMin = limiteMin;
		this.limiteMax = limiteMax;
		
	}
	
	@Override
	public void run() {
		for(int i = limiteMin; i < limiteMax; i++) {
			if(ehPrimo(i))
			{
				System.out.println(i + " " + this.getName());
			}
		}
	}
	
	private boolean ehPrimo(int valor)
	{
		for(int d = 2; d < valor ; d++) {
			if(valor % d == 0)
			{
				return false;
			}
		}
	return true;
}
}
