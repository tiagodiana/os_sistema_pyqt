<?php
header("Access-Control-Allow-Origin: * ");

$conn = mysqli_connect('localhost', 'root', '1872', 'os');
mysqli_set_charset($conn, "utf8");

global $nome,$cpf,$telefone,$celular,$rua,$bairro,$cidade,$estado,$cep;

$tipo = isset($_POST['tipo'])?$_POST['tipo']:Null;

$data = date('o-m-d G:i:s');




//CADASTRANDO CLIENTE
if($tipo == "inserir"){
    $dados = receberDados($_POST);
	$sql = "INSERT INTO clientes VALUES(0, '".$dados['nome']."', '".$dados['cpf']."', '".$dados['telefone']."', '".$dados['celular']."', '".$dados['rua']."', '".$dados['bairro']."', '".$dados['cidade']."', '".$dados['estado']."', '".$dados['cep']."')";
	if(mysqli_query($conn, $sql)){
	    echo 1;
    }
    else{
	    echo 0;
    }
}

//Buscando Cliente
else if($tipo == "buscar_user"){
    $nome = empty($_POST['nome']) ? Null : $_POST['nome'];
    $cpf = empty($_POST['cpf']) ? Null: $_POST['cpf'];

    //Buscar por nome
    if(empty($cpf)){
        $sql = "SELECT * FROM clientes WHERE nome LIKE '$nome'";
        $result = mysqli_query($conn, $sql);
        $data = mysqli_fetch_assoc($result);
        //Selecionando todas as

        $json = json_encode($data, JSON_UNESCAPED_UNICODE);
        echo $json;
    }
    //BUSCANDO POR CPF
    else if(empty($nome)){
        $sql = "SELECT * FROM clientes WHERE cpf LIKE '$cpf'";
        $result = mysqli_query($conn, $sql);
        $data = mysqli_fetch_assoc($result);
        $json = json_encode($data, JSON_UNESCAPED_UNICODE);
        echo $json;
    }
}

else if($tipo == "alterar_user"){
    $dados = receberDados($_POST);
    $sql = "UPDATE clientes SET nome = '{$dados['nome']}', cpf = '{$dados['cpf']}', telefone='{$dados['telefone']}', celular = '{$dados['celular']}', rua = '{$dados['rua']}', bairro = '{$dados['bairro']}', cidade = '{$dados['cidade']}', estado ='{$dados['estado']}', cep = '{$dados['cep']}' WHERE id = {$dados['id']}";
    if(mysqli_query($conn, $sql)){
        echo 1;
    }
    else{
        echo 0;
    }
}

//Buscando Todos os usuarios
else if($tipo == "all_user"){
    $sql = "SELECT id, nome FROM clientes ORDER BY nome";
    $result = mysqli_query($conn, $sql);
    $dados =mysqli_fetch_all($result, MYSQLI_ASSOC);
    $json = json_encode($dados, JSON_UNESCAPED_UNICODE);
    echo $json;
}

//CRIANDO ORDEM DE SERVIÇO
else if($tipo == "nova_os"){
    $dados = receberDados($_POST);

    //PEGANDO ID DO CLIENTE ===================================================
    $sql_cliente = "SELECT id FROM clientes WHERE nome LIKE '{$dados['nome']}' ";
    $result = mysqli_query($conn, $sql_cliente);
    $id = mysqli_fetch_assoc($result);
    $id = $id['id'];
    //=============================================================

    //CRIANDO NOVA ORDEM DE SERVIÇO
    $sql = "INSERT INTO ordem VALUES(0,'{$dados['tipo']}','{$dados['marca']}','{$dados['modelo']}','{$dados['num_serie']}','{$dados['defeito']}','{$dados['solucao']}',{$dados['valor']},0, $id, '$data', null)";
    if(mysqli_query($conn, $sql)){
        $id_os = mysqli_insert_id($conn);
        //SELECIONANDO DADOS DA OS PARA IMPRESSAO
        $sql_print = "SELECT * FROM ordem INNER JOIN clientes on ordem.id_cliente = clientes.id WHERE ordem.id_os = $id_os";
        $result = mysqli_query($conn, $sql_print);
        $data = mysqli_fetch_assoc($result);
        $json_print = json_encode($data,JSON_UNESCAPED_UNICODE);

        $dados = "<iframe src='../include/dompdf.php?dados=$json_print' style='width: 100%; height: 585px'></iframe>";
        $dados .='<div class="text-center bg-dark py-3 fixed-bottom" >
                   <a href="index.html" class="btn btn-lg btn-primary ">Voltar ao Inicio</a>
              </div>';
        $array = array("imprimir"=>$dados, "mensagem"=>"Ordem de Serviço Cadastrado com sucesso \n Preparando Impressão" );
        $json = json_encode($array, JSON_UNESCAPED_UNICODE);
        echo $json;
    }
    else{
        echo "Erro Ao cadastrar";
        echo $sql . "<br>". mysqli_error($conn);
    }

}

// BUSCANDO ORDEM DE SERVIÇO
else if($tipo == "buscar_os"){
    $dados = receberDados($_POST);
    $sql = "SELECT * FROM ordem INNER JOIN clientes on ordem.id_cliente = clientes.id WHERE ordem.id_os = {$dados['id_os']}";
    $result = mysqli_query($conn,$sql);
    $dados = mysqli_fetch_assoc($result);
    $json = json_encode($dados,JSON_UNESCAPED_UNICODE);
    echo $json;
}

// FINALIZANDO ORDEM DE SERVIÇO
else if($tipo == "finalizar_os"){
    $dados = receberDados($_POST);
    $sql = "UPDATE ordem SET status = 1, data_saida=now() WHERE id_os = {$dados['id_os']}";
    //verficando se foi cadastrado
    if(mysqli_query($conn, $sql)){
        //SELECIONANDO DADOS DA OS PARA IMPRESSAO
        $sql_print = "SELECT * FROM ordem INNER JOIN clientes on ordem.id_cliente = clientes.id WHERE ordem.id_os = {$dados['id_os']}";
        $result = mysqli_query($conn, $sql_print);
        $data = mysqli_fetch_assoc($result);
        $json_print = json_encode($data,JSON_UNESCAPED_UNICODE);

        $dados = "<iframe src='../include/dompdf.php?dados=$json_print' style='width: 100%; height: 585px'></iframe>";
        $dados .='<div class="text-center bg-dark py-3 fixed-bottom" >
                   <a href="index.html" class="btn btn-lg btn-primary ">Voltar ao Inicio</a>
              </div>';
        $array = array("imprimir"=>$dados, "ok"=> 1, "jsonPrint" => $json_print );
        $json = json_encode($array, JSON_UNESCAPED_UNICODE);
        echo $json;
    }
    else{
        echo 0;
    }
}


// ALTERANDO ORDEM DE SERVIÇO
else if($tipo == "alterar_os"){
    $dados = receberDados($_POST);

    //PEGANDO ID DO CLIENTE ===================================================
    $sql_cliente = "SELECT id FROM clientes WHERE nome LIKE '{$dados['nome']}' ";
    $result = mysqli_query($conn, $sql_cliente);
    $id = mysqli_fetch_assoc($result);
    $id = $id['id'];
    //=============================================================

    $sql = "UPDATE ordem SET tipo='{$dados['tipo']}', marca='{$dados['marca']}', modelo='{$dados['modelo']}',num_serie='{$dados['num_serie']}', defeito = '{$dados['defeito']}', solucao='{$dados['solucao']}',valor='{$dados['valor']}' WHERE id_os = {$dados['id_os']} ";
    if(mysqli_query($conn,$sql)){
        echo 1;
    }
    else{
        echo 0;
    }

}

//DELETANDO ORDEM DE SERVIÇO
else if($tipo == "deletar_os"){
    $dados = receberDados($_POST);
    $sql = "DELETE FROM ordem WHERE id_os = {$dados['id_os']}";
    if(mysqli_query($conn, $sql)){
        echo 1;
    }
    else{
        echo 0;
    }
}

//ENVIANDO E-MAIL DE CONTATO
else if($tipo == "msg_contato"){


}



// RECEBENDO DADOS
function receberDados($POST){
    $lista['id'] = empty($POST['id']) ? Null : $POST['id'];
    $lista['nome'] = empty($POST['nome']) ? Null : $POST['nome'];
    $lista['cpf'] = empty($POST['cpf']) ? Null : $POST['cpf'];
    $lista['telefone'] = empty($POST['telefone']) ? Null : $POST['telefone'];
    $lista['celular'] = empty($POST['celular']) ? Null : $POST['celular'];
    $lista['rua'] = empty($POST['rua']) ? Null : $POST['rua'];
    $lista['bairro'] = empty($POST['bairro']) ? Null : $POST['bairro'];
    $lista['cidade'] = empty($POST['cidade']) ? Null : $POST['cidade'];
    $lista['estado'] = empty($POST['estado']) ? Null : $POST['estado'];
    $lista['cep'] = empty($POST['cep']) ? Null : $POST['cep'];
    $lista['id_os'] = empty($POST['id_os']) ? Null : $POST['id_os'];
    $lista['tipo'] = empty($POST['hardware']) ? Null : $POST['hardware'];
    $lista['marca'] = empty($POST['marca']) ? Null : $POST['marca'];
    $lista['modelo'] = empty($POST['modelo']) ? Null : $POST['modelo'];
    $lista['num_serie'] = empty($POST['num_serie']) ? Null : $POST['num_serie'];
    $lista['defeito'] = empty($POST['defeito']) ? Null : $POST['defeito'];
    $lista['solucao'] = empty($POST['solucao']) ? Null : $POST['solucao'];
    $lista['valor'] = empty($POST['valor']) ? Null : $POST['valor'];
    $lista['nome_contato'] = empty($POST['nome_contato']) ? Null : $POST['nome_contato'];
    $lista['email_contato'] = empty($POST['email_contato']) ? Null : $POST['email_contato'];
    $lista['msg_contato'] = empty($POST['msg_contato']) ? Null : $POST['msg_contato'];

    return $lista;

}