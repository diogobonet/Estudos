<?php
    class IRPF {
        private $income; // Salário
        private $nDep; //  Número de dependentes
        private $otherDeductions; // Deduções
        private $alimony; // Pensão alimenticia (inicialmente R$0.00)
        private $discByDep; // Valor do desconto por dependente (inicialmente R$189,59)
        private $tax; // Taxa de imposto da faixa que se enquadra
        private $realTax; // Taxa efetiva de imposto
        private $valueTax; // Valor do imposto a ser pago

        private function calcTaxValue() {

        }

        private function calcRealTax(){

        }

        public function __construct($income, $nDep, $otherDeductions, $alimony, $discByDep, $tax, $realTax, $valueTax)
        {
            $this->income = $income;
            $this->nDep = $nDep;
            $this->otherDeductions = array($otherDeductions);
            $this->alimony= $alimony;
            $this->discByDep = $discByDep;
            $this->tax = $tax;
            $this->realTax = $realTax;
            $this->valueTax = $valueTax;
        }

        public function setAlimony($pensao) {
            $this->alimony = $pensao;
        }
        public function addDeductions() {

        }

        public function setDiscByDep() {

        }

        public function getIRPF() {

        }

        public function getTax() {

        }

        public function realTax() {

        }
    }
?>