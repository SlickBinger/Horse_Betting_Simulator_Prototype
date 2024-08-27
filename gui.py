import pygame


"""
    CRITICAL - Howver state must be directly below NOT to the right on the sprite sheet 
"""
class Button:
    def __init__(self, xy_pos: (int, int), wh_len: (int, int),
                 img_scaler: float, alpha_check: bool, img_sheet: pygame.Surface) -> None:
        
        # Rect attributes
        self.x_pos = xy_pos[0]
        self.y_pos = xy_pos[1]
        self.width = wh_len[0]
        self.height = wh_len[1]
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width * img_scaler, self.height * img_scaler)
        
        # Image attributes
        self.img_scaler = img_scaler
        self.selection_movement = selection_movement
        self.img_sheet = self.set_alpha(alpha_check, img_sheet)
        
        self.activated = False
    
    def set_alpha(self, alpha_check: bool, img_sheet: pygame.Surface) -> pygame.Surface:
        if alpha_check: 
            return pygame.transform.scale_by(pygame.image.load(img_sheet).convert_alpha(), self.img_scaler)
        return pygame.transform.scale_by(pygame.image.load(img_sheet), self.img_scaler)
    
    def render_button(self, screen: pygame.Surface, position: (int, int)):
        if self.rect.collidepoint(position):
            screen.blit(self.img_sheet, (self.x_pos, self.y_pos - self.selection_movement), (self.width * self.img_scaler, self.height * self.img_scaler, self.width * self.img_scaler, self.height * self.img_scaler))
            self.activated = True
        else:
            screen.blit(self.img_sheet, (self.x_pos, self.y_pos), (self.width * self.img_scaler, 0, self.width * self.img_scaler, self.height * self.img_scaler))
            self.activated = False
    
    def check_for_input(self) -> bool:
        return self.activated
    
class StaticText:
    def __init__(self, screen: pygame.Surface, x:int, y: int, pos: str,
                 font: str, fontsize: int, colour: str, text: str) -> None:
        self.length = len(text)
        self.text = pygame.font.Font("fonts/" + font + ".ttf", fontsize).render(text, False, colour)
        self.render_text(screen, x, y, pos)
    def render_text(self, screen, x, y, pos=''):
        if pos == "center":
            screen.blit(self.text, (x - text.get_width()/2, y))
        else:
            screen.blit(self.text, (x, y))
            

            
        
        
        