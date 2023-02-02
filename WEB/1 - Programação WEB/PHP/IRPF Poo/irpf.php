<?php
    class IRPF{
        private $income;
        private $nDep;
        private $otherDeductions = array();
        private $alimony = 0;
        private $discByDep = 189.59;
        private $tax = 0; 
        private $realTax = 0; 
        private $valueTax = 0; 

        public function __construct($income, $nDep){
            $this->income = $income;
            $this->nDep = $nDep;
        }

        public function __destruct(){
        }
        
        public function setAlimony($pensao){ 
            $this->alimony = $pensao;
        }

        public function addDeductions($deducoes){ 
            $this->otherDeductions[] = $deducoes;
        }

        public function setDiscByDep($desconto){ 
            $this->discByDep = $desconto;
        }

        public function getIRPF(){ 
            return $this->calcTaxValue();
        }

        public function getTax(){ 
            return $this->tax * 100;
        }

        public function getRealTax(){ 
            $this->calcRealTax();
            return $this->realTax;
        }

        private function calcTaxValue(){ 
            $faixas = array(); // Array 0
            $faixas[1] = array(1903.98, 0);  // Array 1
            $faixas[2] = array(2826.65, 0.075); // Array 2
            $faixas[3] = array(3751.05, 0.15); // Array 3
            $faixas[4] = array(4664.68, 0.225); // Array 4
            $faixas[5] = array(4664.68, 0.275); // Array 5
            
            $deducoes = 0; // Valor das deduções é setada 0!!!!

            foreach ($this->otherDeductions as $value){ 
                $deducoes += $value;

            }

            $base_do_calculo = $this->income - (($this->discByDep * $this->nDep) + $this->alimony + $deducoes);

            for($i = count($faixas); $i > 0; $i--){ 

                if($base_do_calculo > $faixas[$i][0]){
                    if($base_do_calculo > 4664.68){
                        $this->tax = $faixas[$i][1];
                        $imposto = ($base_do_calculo - $faixas[$i][0]) * $faixas[$i][1];
                    }

                    else{
                        $this->tax = $faixas[$i+1][1];
                        $imposto = ($base_do_calculo - $faixas[$i][0]) * $faixas[$i+1][1];
                    }

                    for($j = $i; $j > 0; $j--){ 
                        if($j == 1){
                            break 2;
                        }
                        $adicional = ($faixas[$j][0] - $faixas[$j-1][0]) * $faixas[$j][1];
                        $imposto = $imposto + $adicional;
                    }
                }

                else if($base_do_calculo <= 1903.98){
                    $this->tax = $faixas[$i][1];
                    $imposto = 0;
                }
            }

            $this->valueTax = $imposto;
            return $imposto;
        }

        private function calcRealTax(){ 
            if($this->tax = 0){
                $this->realTax = 0;
            }
            
            else{
                $deducoes = 0;
                foreach ($this->otherDeductions as $value){
                    $deducoes += $value;
                }
                $base_do_calculo = $this->income - (($this->discByDep * $this->nDep) + $this->alimony + $deducoes);
                $this->realTax = ($this->valueTax / $base_do_calculo) * 100;
            }
        }
    }
?>