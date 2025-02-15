class avaliacao:
    def __init__(self, avaliador, avaliado, nota, comentario):
        if not self.validar_nota_comentario(nota, comentario):
            return False
        self.avaliador = avaliador
        self.avaliado = avaliado
        self.nota = nota
        self.comentario = comentario
        self.avaliado.notas.append(self.nota)
        self.avaliado.comentarios.append(self.comentario)
        self.avaliado.calcular_avaliacao_media()
        
        
    def validar_nota_comentario(self, nota, comentario):
        if nota < 0 or nota > 5:
            raise ValueError("Nota inválida. A nota deve estar entre 0 e 5.")
        if not comentario:
            raise ValueError("Comentário inválido. O comentário não pode estar vazio.")
        return True