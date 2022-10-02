from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.core.audio import SoundLoader
import winsound

class Trup_Kits(Screen):
    pass
class Tribal_Kits(Screen):
    def kick(self):
        #winsound.PlaySound("wavs/kick.wav", winsound.SND_ASYNC)
        sound=SoundLoader.load("kick.wav")
        sound.play()
    def snare(self):
        winsound.PlaySound("wavs/snare.wav", winsound.SND_ASYNC)
        #sound=SoundLoader.load("snare.wav")
        #sound.play()
    def hat(self):
        winsound.PlaySound("wavs/hat.wav", winsound.SND_ASYNC)
        #sound=SoundLoader.load("hat.wav")
        #sound.play()
    def w_808(self):
        winsound.PlaySound("wavs/808.wav", winsound.SND_ASYNC)
        #sound=SoundLoader.load("808.wav")
        #sound.play()
    def cybal(self):
        winsound.PlaySound("wavs/cybal.wav", winsound.SND_ASYNC)
        #sound=SoundLoader.load("cybal.wav")
        #sound.play()
    def clap(self):
        winsound.PlaySound("wavs/clap.wav", winsound.SND_ASYNC)
        #sound=SoundLoader.load("clap.wav")
        #sound.play()
    def chant(self):
        winsound.PlaySound("wavs/chant.wav", winsound.SND_ASYNC)
        #sound=SoundLoader.load("chant.wav")
        #sound.play()

    def fx(self):
        winsound.PlaySound("wavs/fx.wav", winsound.SND_ASYNC)
        #sound=SoundLoader.load("fx.wav")
        #sound.play()
    
class Raggea_Kits(Screen):
    def v_kick(self):
        winsound.PlaySound("wavs/v_kick.wav", winsound.SND_ASYNC)
        #sound=SoundLoader.load("v_kick.wav")
        #sound.play()
    def v_snare(self):
        winsound.PlaySound("wavs/v_snare.wav", winsound.SND_ASYNC)
        #sound=SoundLoader.load("v_snare.wav")
        #sound.play()
    def v_hat(self):
        winsound.PlaySound("wavs/v_hat.wav", winsound.SND_ASYNC)
        #sound=SoundLoader.load("v_hat.wav")
        #sound.play()
    def perc(self):
        winsound.PlaySound("wavs/perc.wav", winsound.SND_ASYNC)
        #sound=SoundLoader.load("perc.wav")
        #sound.play()
    def loop3(self):
        winsound.PlaySound("wavs/loop3.wav", winsound.SND_ASYNC)
        #sound=SoundLoader.load("loop3.wav")
        #sound.play()
    def v_clap(self):
        winsound.PlaySound("wavs/v_clap.wav", winsound.SND_ASYNC)
        #sound=SoundLoader.load("v_clap.wav")
        #sound.play()
    def loop(self):
        winsound.PlaySound("wavs/loop.wav", winsound.SND_ASYNC)
        #sound=SoundLoader.load("loop.wav")
        #sound.play()
    def loop2(self):
        winsound.PlaySound("wavs/loop2.wav", winsound.SND_ASYNC)
        #sound=SoundLoader.load("loop2.wav")
        #sound.play()
    
class piano(Screen):
    def h_kick(self):
        winsound.PlaySound("wavs/h_kick.wav", winsound.SND_ASYNC)
        #sound=SoundLoader.load("h_kick.wav")
        #sound.play()
    def h_snare(self):
        winsound.PlaySound("wavs/h_snare.wav", winsound.SND_ASYNC)
        #sound=SoundLoader.load("h_snare.wav")
        #sound.play()
    def h_hat(self):
        winsound.PlaySound("wavs/h_hat.wav", winsound.SND_ASYNC)
        #sound=SoundLoader.load("h_hat.wav")
        #sound.play()
    def percussion(self):
        winsound.PlaySound("wavs/percussion.wav", winsound.SND_ASYNC)
        #sound=SoundLoader.load("percussion.wav")
        #sound.play()
    def h_tom(self):
        winsound.PlaySound("wavs/h_tom.wav", winsound.SND_ASYNC)
        #sound=SoundLoader.load("h_tom.wav")
        #sound.play()
    def h_clap(self):
        winsound.PlaySound("wavs/h_clap.wav", winsound.SND_ASYNC)
        #sound=SoundLoader.load("h_clap.wav")
        #sound.play()
    def h_cybal(self):
        winsound.PlaySound("wavs/h_cybal.wav", winsound.SND_ASYNC)
        #sound=SoundLoader.load("h_cybal.wav")
        #sound.play()
    def h_rim(self):
        winsound.PlaySound("wavs/h_rim.wav", winsound.SND_ASYNC)
        #sound=SoundLoader.load("h_rim.wav")
        #sound.play()

class final(Screen):
    def t_kick(self):
        winsound.PlaySound("wavs/t_kick.wav", winsound.SND_ASYNC)
        #sound=SoundLoader.load("t_kick.wav")
        #sound.play()
    def t_cybal(self):
        winsound.PlaySound("wavs/t_cybal.wav", winsound.SND_ASYNC)
        #sound=SoundLoader.load("t_cybal.wav")
        #sound.play()
    def conga(self):
        winsound.PlaySound("wavs/conga.wav", winsound.SND_ASYNC)
        #sound=SoundLoader.load("conga.wav")
        #sound.play()
    def shaker(self):
        winsound.PlaySound("wavs/shaker.wav", winsound.SND_ASYNC)
        #sound=SoundLoader.load("shaker.wav")
        #sound.play()
    def t_rim(self):
        winsound.PlaySound("wavs/t_rim.wav", winsound.SND_ASYNC)
        #sound=SoundLoader.load("t_rim.wav")
        #sound.play()
    def bongo(self):
        winsound.PlaySound("wavs/bongo.wav", winsound.SND_ASYNC)
        #sound=SoundLoader.load("bongo.wav")
        #sound.play()
    def loop(self):
        winsound.PlaySound("wavs/loop.wav", winsound.SND_ASYNC)
        #sound=SoundLoader.load("loop.wav")
        #sound.play()
    def loop2(self):
        winsound.PlaySound("wavs/loop3.wav", winsound.SND_ASYNC)
        #sound=SoundLoader.load("loop3.wav")
        #sound.play()
class Main_scren(ScreenManager):
    pass
plug_in=Builder.load_file("tribal.kv")
class My_App(App):
    title="Drum pad"
    def build(self):
        return plug_in 
if __name__=='__main__':
    My_App().run()
