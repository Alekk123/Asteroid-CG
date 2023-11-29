class Hit:
  def __init__(self, enemy_rect, player_rect):
    self.bullet_rect = bullet_rect
    self.enemy_rect = enemy_rect
    self.player_rect = player_rect

  def hit(self, bullet_rect):
    if self.bullet_rect.colliderect(self.enemy_rect):
      print("Acertou o inimigo!")
    print("Não acertou o inimigo!")
