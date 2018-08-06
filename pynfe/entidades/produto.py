# -*- coding: utf-8 -*-
from .base import Entidade
from pynfe.utils.flags import ICMS_TIPOS_TRIBUTACAO, ICMS_ORIGENS, ICMS_MODALIDADES

from decimal import Decimal

class Produto(Entidade):
    """XXX: E provavel que esta entidade sera descartada."""

    # Dados do Produto
    # - Descricao (obrigatorio)
    descricao = str()
    # - Informacoes adicionais do produto
    informacoes_adicionais_produto = str()
    # - Codigo (obrigatorio) - nao pode ser alterado quando em edicao
    codigo = str()

    # - EAN
    ean = str()

    # - EAN Unid. Tributavel
    ean_unidade_tributavel = str()

    # - EX TIPI
    ex_tipi = str()

    # - Genero
    genero = str()

    # - NCM
    ncm = str()

    # - CEST - Código especificador da substituição tributária
    # NT2015/003 http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=uXFlhOSgUZc=
    # Tabela https://www.confaz.fazenda.gov.br/anexo-i.pdf
    cest = str()

    # - Unid. Com.
    unidade_comercial = str()

    # - Valor Unitario Com.
    valor_unitario_comercial = Decimal()

    # - Unid. Trib.
    unidade_tributavel = str()

    # - Qtd. Trib.
    quantidade_tributavel = Decimal()

    # - Valor Unitario Trib.
    valor_unitario_tributavel = Decimal()

    # - indica se valor do item entra no valor total da nota fiscal 
    # 0=Valor do item (vProd) não compõe o valor total da NF-e 
    # 1=Valor do item (vProd) compõe o valor total da NF-e (vProd)
    ind_total = int()
    
    # # Impostos

    # - IPI
    #  - Classe de Enquadramento (cigarros e bebidas)
    ipi_classe_enquadramento = str()

    #  - Codigo de Enquadramento Legal
    ipi_codigo_enquadramento_legal = str()

    #  - CNPJ do Produtor
    ipi_cnpj_produtor = str()

    # ICMS (Informar apenas um grupo por produto)
    """
    ICMS 00 - Tributada integralmente
    ICMS 10 - Tributada e com cobrança do ICMS por substituição tributária
    ICMS 20 - Tributada e com cobrança do ICMS por substituição tributária
    ICMS 30 - Tributação Isenta ou não tributada e com cobrança do ICMS por substituição tributária
    ICMS 30 - Isenta ou nao tributada e com cobranca do ICMS por substituicao tributaria
    ICMS 40 - Isenta
    ICMS 41 - Nao tributada
    ICMS 50 - Suspensao
    ICMS 51 - Diferimento
    ICMS 60 - Cobrado anteriormente por substituicao tributaria
    ICMS 70 - Com reducao da base de calculo e cobranca do ICMS por substituicao tributaria
    ICMS 90 - Outras
    """

    # Tributos aproximados por item
    valor_tributos_aprox = str()

    icms_modalidade = str()
    icms_origem = int()
    icms_csosn = str()
    icms_aliquota = Decimal()
    icms_credito= Decimal()
    icms_valor = Decimal()
    icms_valor_base_calculo = Decimal()
    
    # - Valora da base de calculo retido no remetente
    icms_valor_base_retido_fonte_st = Decimal()
    # - Percentual do FCP
    icms_percentual_fcp = Decimal()
    # - Valor do ICMSST Retido
    icms_valor_icms_st_retido = Decimal()
    # - Valor da base de calculo do FCP retido
    icms_valor_base_calculo_fcp_retido = Decimal()
    # - Pecentual do FCP retido
    icms_percentual_fcp_retido = Decimal()
    # - Valor do FCP retido
    icms_valor_fcp_retido = Decimal()
    #icms 40 Valor da desoneracao
    icms_40valor_desoneracao = Decimal()
    #icms 40 Motivo da desoneracao
    icms_40valor_desoneracao_motivo = str()

    # - Difal { Partilha do ICMS CFP }
    difal_basec_uf_destino = Decimal() # vBCUFDest
    difal_fcp_basec_uf_destino = Decimal() # vBCFCPUFDest
    difal_fcp_aliquota_inserido_uf_destino = Decimal() # pFCPUFDest
    difal_aliquota_uf_destino = Decimal() # pICMSUFDest
    difal_aliquota_interestadual = Decimal() # pICMSInter
    difal_percentual_partilha_uf_destino = Decimal() # pICMSInterPart
    difal_valor_icms_fcp_uf_destino = Decimal() # vFCPUFDest
    difal_valor_partilha_icms_uf_destino = Decimal() # vICMSUFDest
    difal_valor_partilha_icms_uf_origem = Decimal() # vICMSUFRemet

    # # PIS
    pis_modalidade = str()
    pis_valor_base_calculo = str()
    pis_aliquota_percentual = str()
    pis_valor = str()

    # # COFINS
    cofins_modalidade = str()
    cofins_valor_base_calculo = str()
    cofins_aliquota_percentual = str()
    cofins_valor = str()
 
    """ ICMS 70 """
    icms_70modbc = str()
    icms_70predbc = str()
    icms_70vbc = str()
    icms_70picms = str()
    icms_70vicms = str()
    icms_70vbcfcp = str()
    icms_70pfcp = str()
    icms_70vfcp = str()
    icms_70mdbcst = str()
    icms_70pmvast = str()
    icms_70predbcst = str()
    icms_70vbcst = str()
    icms_70picmsst = str()
    icms_70vicmsst = str()
    icms_70vbcfcpst = str()
    icms_70pfcpst = str()
    icms_70vfcpst = str()
    icms_70vicmsdeson = str()
    icms_70motdesicms = str()

    # # - ICMS (lista 1 para * / ManyToManyField)
    icms = None
    def adicionar_icms(self, **kwargs):
        """Adiciona uma instancia de ICMS a lista de ICMS do produto"""
        self.icms.append(ProdutoICMS(**kwargs))

    def __init__(self, *args, **kwargs):
        self.icms = []

        super(Produto, self).__init__(*args, **kwargs)

    def __str__(self):
        return ' '.join([self.codigo, self.descricao])

class ProdutoICMS(Entidade):
    #  - Tipo de Tributacao (seleciona de lista) - ICMS_TIPOS_TRIBUTACAO
    tipo_tributacao = str()

    #  - Origem (seleciona de lista) - ICMS_ORIGENS
    origem = str()

    #  - Modalidade de determinacao da Base de Calculo (seleciona de lista) - ICMS_MODALIDADES
    modalidade = str()

    #  - Aliquota ICMS
    aliquota = Decimal()

    #  - Percentual de reducao da Base de Calculo
    percentual_reducao = Decimal()

    #  - Modalidade de determinacao da Base de Calculo do ICMS ST (seleciona de lista) - ICMS_MODALIDADES
    st_modalidade = str()

    #  - Aliquota ICMS ST
    st_aliquota = Decimal()

    #  - Percentual de reducao do ICMS ST
    st_percentual_reducao = Decimal()

    #  - Percentual da margem de Valor Adicionado ICMS ST
    st_percentual_margem_valor_adicionado = Decimal()

    # - Percentual do FCP
    #st_percentual_fcp = Decimal()	
    
    # - Valor da base de calculo do FCP retido
    #st_valor_base_calculo_fcp_retido = Decimal()
    
    # - Pecentual do FCP retido
    #st_percentual_fcp_retido = Decimal()
    
    # - Valor do FCP retido
    #st_valor_cpf_retido = Decimal()
    