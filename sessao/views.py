from django.utils.translation import ugettext_lazy as _

from sapl.crud import build_crud

from .models import (ExpedienteMateria, OrdemDia, RegistroVotacao,
                     SessaoPlenaria, TipoExpediente, TipoResultadoVotacao,
                     TipoSessaoPlenaria)

tipo_sessao_crud = build_crud(
    TipoSessaoPlenaria, '',

    [_('Tipo de Sessão Plenária'),
     [('nome', 6), ('quorum_minimo', 6)]],
)

sessao_crud = build_crud(
    SessaoPlenaria, '',

    [_('Dados Básicos'),
     [('numero', 3),
      ('tipo', 3),
      ('legislatura', 3),
      ('sessao_legislativa', 3)],
     [('data_inicio', 12)],
     [('data_fim', 12)],
     [('dia', 2),
      ('hora_inicio', 2),
      ('hora_fim', 2),
      ('tipo_expediente', 6)],
     [('url_audio', 6), ('url_video', 6)]],
)

expediente_materia_crud = build_crud(
    ExpedienteMateria, '',

    [_('Cadastro de Matérias do Expediente'),
     [('data_ordem', 4), ('tip_sessao_FIXME', 4), ('numero_ordem', 4)],
     [('tip_id_basica_FIXME', 4),
      ('num_ident_basica_FIXME', 4),
      ('ano_ident_basica_FIXME', 4)],
     [('tipo_votacao', 12)],
     [('observacao', 12)]],
)

ordem_dia_crud = build_crud(
    OrdemDia, '',

    [_('Cadastro de Matérias da Ordem do Dia'),
     [('data_ordem', 4), ('tip_sessao_FIXME', 4), ('numero_ordem', 4)],
     [('tip_id_basica_FIXME', 4),
      ('num_ident_basica_FIXME', 4),
      ('ano_ident_basica_FIXME', 4)],
     [('tipo_votacao', 12)],
     [('observacao', 12)]],
)

tipo_resultado_votacao_crud = build_crud(
    TipoResultadoVotacao, '',

    [_('Tipo de Resultado da Votação'),
     [('nome', 12)]],
)

tipo_expediente_crud = build_crud(
    TipoExpediente, '',

    [_('Tipo de Expediente'),
     [('nome', 12)]],
)

registro_votacao_crud = build_crud(
    RegistroVotacao, '',

    [_('Votação Simbólica'),
     [('numero_votos_sim', 3),
      ('numero_votos_nao', 3),
      ('numero_abstencoes', 3),
      ('nao_votou_FIXME', 3)],
     [('votacao_branco_FIXME', 6),
      ('ind_votacao_presidente_FIXME', 6)],
     [('tipo_resultado_votacao', 12)],
     [('observacao', 12)]],
)


class ExpedienteView(sessao_crud.CrudDetailView):
    template_name = 'sessao/expediente.html'
    # TODO ...
