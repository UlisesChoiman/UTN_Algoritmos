<?php
class foo
{
    public $foo;
    public $bar;

    function __construct()
    {
        $this->foo = 'Foo';
        $this->bar = array('Bar1', 'Bar2', 'Bar3');
    }
}

$foo = new foo();
$name = 'MyName';

echo <<<'EOT'
Mi nombre es "$name". Estoy imprimiendo $foo->foo.
Ahora, estoy imprimiendo {$foo->bar[1]}.
Esto no debería imprimir una 'A' mayúscula: \x41
EOT;
?>