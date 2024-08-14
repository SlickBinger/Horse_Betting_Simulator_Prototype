import pygame

class Button:
    def __init__(self, xy_pos: (int, int), wh_len: (int, int),
                 img_scaler: float, img_sheet: pygame.Suraface,
                 frame_steps=1, cooldown=0, delta_time=0) -> None:
        
        # Rect attributes
        self.x_pos = xy_pos[0]
        self.y_pos = xy_pos[1]
        self.width = wh_len[0]
        self.height = wh_len[1]
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width * img_scaler, self.height * img_scaler)
        
        # Image attributes
        self.img_scaler = img_sclaer
        self.img_sheet = self.set_alpha(img_sheet)
        
        # Animation attributes
        self.frame = 0
        self.frame_steps: int = frame_steps
        self.cooldown: float = cooldown
        self.last_update: int = delta_time
        
        self.activated = False
    
    def set_alpha(self, img_sheet: pygame.Surface) -> pygame.Surface:
        if self.alpha_check: 
            return pygame.transform.scale_by(pygame.image.load(self.img_sheet).convert_alpha(), self.img_scaler)
        return pygame.transform.scale_by(pygame.image.load(self.img_sheet), self.img_scaler)
    
    def render_button(self, screen: pygame.Surface, position: (int, int), current_time: int):
        if frame_steps > 1:
            self.update_frame(current_time)
            
        if self.rect.collidepoint(position):
            self.rect = pygame.rect.Rect(self.x_pos, self.y_pos - 5, self.width * self.img_scaler, self.height * self.img_scaler)
            screen.blit(self.img_sheet, (self.x_pos, self.y_pos - 5), ((self.width * self.img_scaler) * self.frame, self.height * self.img_scaler, self.width * self.img_scaler, self.height * self.img_scaler))
            self.activated = True
        else:
            self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width * self.img_scaler, self.height * self.img_scaler)
            screen.blit(self.img_sheet, (self.x_pos, self.y_pos - 5), ((self.width * self.img_scaler) * self.frame, 0, self.width * self.img_scaler, self.height * self.img_scaler))
            self.activated = False

    def update_frame(self, current_time: int) -> None:
        if self.last_update - current_time >= self.cooldown:
            self.last_update = 0
            self.frame += 1
            if self.frame == self.frame_steps:
                self.frame = 0
        else:
            self.last_update += current_time
    
    def check_for_input(self) -> bool:
        return self.activated

            
        
        
        