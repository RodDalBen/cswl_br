#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.90.1),
    on maio 07, 2018, at 09:44
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'Exp2'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1366, 768], fullscr=True, screen=1,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1,1,1], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "inst_initial"
inst_initialClock = core.Clock()
inst_1 = visual.TextStim(win=win, name='inst_1',
    text='Olá, seja bem vindo!\n\nPor favor, coloque o fone de ouvido\ne pressione a tecla "Enter”\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "inst_vol"
inst_volClock = core.Clock()
img_keyboard_1 = visual.ImageStim(
    win=win, name='img_keyboard_1',
    image='img/keyboard_1.jpg', mask=None,
    ori=0, pos=(0, 0), size=(1.5, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
music_1 = sound.Sound('audio/musica1.wav', secs=-1)
music_1.setVolume(1)

# Initialize components for Routine "inst_vol2"
inst_vol2Clock = core.Clock()
inst_2 = visual.TextStim(win=win, name='inst_2',
    text='Fique à vontade para ajustar o volume durante todo o experimento.\n\nPressione "Enter" para continuar\n\n\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "inst_training"
inst_trainingClock = core.Clock()
inst_3 = visual.TextStim(win=win, name='inst_3',
    text='A seguir você verá várias figuras e\nouvirá várias palavras.\n\nA sua tarefa é descobrir as relações \nentre as palavras e as figuras.\n\n\nPressione “Enter” para continuar\n\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "inst_training_2"
inst_training_2Clock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='As figuras e palavras aparecerão\nautomaticamente.\n\nVocê não precisa dar nenhum comando.\nApenas preste atenção.\n\nLembre-se: a sua tarefa é descobrir as\nrelações entre as palavras e as figuras.\n\nPressione "Enter" para continuar',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='.',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "training"
trainingClock = core.Clock()
sound_training_1 = sound.Sound('A', secs=0.90)
sound_training_1.setVolume(1)
sound_training_2 = sound.Sound('A', secs=0.90)
sound_training_2.setVolume(1)
img_training_1 = visual.ImageStim(
    win=win, name='img_training_1',
    image='sin', mask=None,
    ori=0, pos=(-0.5, 0), size=(0.7, 1.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
img_training_2 = visual.ImageStim(
    win=win, name='img_training_2',
    image='sin', mask=None,
    ori=0, pos=(0.5, 0), size=(0.7, 1.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "inst_test_fami_1"
inst_test_fami_1Clock = core.Clock()
inst_4 = visual.TextStim(win=win, name='inst_4',
    text='Muito bem! \n\nAgora, indique qual dentre as quatro\nfiguras corresponde à palavra\nque você ouvir.\n\nVamos começar treinando com\npalavras conhecidas.\n\nPressione “Enter” para continuar',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
sound_beep_1 = sound.Sound('audio/beep.wav', secs=1.0)
sound_beep_1.setVolume(1)

# Initialize components for Routine "inst_test_fami_2"
inst_test_fami_2Clock = core.Clock()
img_keyboard_2 = visual.ImageStim(
    win=win, name='img_keyboard_2',
    image='img/keyboard_2.jpg', mask=None,
    ori=0, pos=(0, 0), size=(1.5, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "inst_test_fami_3"
inst_test_fami_3Clock = core.Clock()
img_keyboard_3 = visual.ImageStim(
    win=win, name='img_keyboard_3',
    image='img/keyboard_3.jpg', mask=None,
    ori=0, pos=(0, 0), size=(1.5, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "inst_test_fami_4"
inst_test_fami_4Clock = core.Clock()
img_keyboard_4 = visual.ImageStim(
    win=win, name='img_keyboard_4',
    image='img/keyboard_4.jpg', mask=None,
    ori=0, pos=(0, 0), size=(1.5, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "inst_test_fami_5"
inst_test_fami_5Clock = core.Clock()
img_keyboard_5 = visual.ImageStim(
    win=win, name='img_keyboard_5',
    image='img/keyboard_5.jpg', mask=None,
    ori=0, pos=(0, 0), size=(1.5, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='.',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "test_familiar"
test_familiarClock = core.Clock()
sound_test_fami = sound.Sound('A', secs=0.9)
sound_test_fami.setVolume(1)
image_3 = visual.ImageStim(
    win=win, name='image_3',
    image='sin', mask=None,
    ori=0, pos=(-0.5, 0.5), size=(0.4, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image_4 = visual.ImageStim(
    win=win, name='image_4',
    image='sin', mask=None,
    ori=0, pos=(0.5, 0.5), size=(0.4, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
image_5 = visual.ImageStim(
    win=win, name='image_5',
    image='sin', mask=None,
    ori=0, pos=(-0.5, -0.5), size=(0.4, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
image_6 = visual.ImageStim(
    win=win, name='image_6',
    image='sin', mask=None,
    ori=0, pos=(0.5, -0.5), size=(0.4, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
label_1 = visual.TextStim(win=win, name='label_1',
    text='1',
    font='Arial',
    pos=(-0.85, 0.85), height=0.1, wrapWidth=None, ori=0, 
    color='grey', colorSpace='rgb', opacity=1,
    depth=-5.0);
label_2 = visual.TextStim(win=win, name='label_2',
    text='2',
    font='Arial',
    pos=(0.85, 0.85), height=0.1, wrapWidth=None, ori=0, 
    color='grey', colorSpace='rgb', opacity=1,
    depth=-6.0);
label_3 = visual.TextStim(win=win, name='label_3',
    text='3',
    font='Arial',
    pos=(-0.85, -0.85), height=0.1, wrapWidth=None, ori=0, 
    color='grey', colorSpace='rgb', opacity=1,
    depth=-7.0);
label_4 = visual.TextStim(win=win, name='label_4',
    text='4',
    font='Arial',
    pos=(0.85, -0.85), height=0.1, wrapWidth=None, ori=0, 
    color='grey', colorSpace='rgb', opacity=1,
    depth=-8.0);

# Initialize components for Routine "inst_teste_1"
inst_teste_1Clock = core.Clock()
inst_7 = visual.TextStim(win=win, name='inst_7',
    text='Ótimo! O treino acabou!\n\nAgora você vai ouvir as palavras e ver as figuras que você viu e ouviu anteriormente.\n\nPressione "Enter" para continuar\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "inst_teste_2"
inst_teste_2Clock = core.Clock()
inst_8 = visual.TextStim(win=win, name='inst_8',
    text='As tentativas terão o mesmo formato do treino.\n\nIndique a figura correspondente à palavra que você ouvir.\n\nSerão apresentadas 24 tentativas (+- 4 minutos).\n\n\nPressione "Enter" para continuar',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "fixation_2"
fixation_2Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='.',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "test_trials"
test_trialsClock = core.Clock()
sound_1 = sound.Sound('A', secs=0.9)
sound_1.setVolume(1)
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=(-0.5, 0.5), size=(0.6, 1.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image_2 = visual.ImageStim(
    win=win, name='image_2',
    image='sin', mask=None,
    ori=0, pos=(0.5, 0.5), size=(0.6, 1.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
image_7 = visual.ImageStim(
    win=win, name='image_7',
    image='sin', mask=None,
    ori=0, pos=(-0.5, -0.5), size=(0.6, 1.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
image_8 = visual.ImageStim(
    win=win, name='image_8',
    image='sin', mask=None,
    ori=0, pos=(0.5, -0.5), size=(0.6, 1.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
text_4 = visual.TextStim(win=win, name='text_4',
    text='1',
    font='Arial',
    pos=(-0.85, 0.85), height=0.1, wrapWidth=None, ori=0, 
    color='lightGrey', colorSpace='rgb', opacity=1,
    depth=-6.0);
text_6 = visual.TextStim(win=win, name='text_6',
    text='2',
    font='Arial',
    pos=(0.85, 0.85), height=0.1, wrapWidth=None, ori=0, 
    color='lightGrey', colorSpace='rgb', opacity=1,
    depth=-7.0);
text_7 = visual.TextStim(win=win, name='text_7',
    text='3',
    font='Arial',
    pos=(-0.85, -0.85), height=0.1, wrapWidth=None, ori=0, 
    color='lightGrey', colorSpace='rgb', opacity=1,
    depth=-8.0);
text_8 = visual.TextStim(win=win, name='text_8',
    text='4',
    font='Arial',
    pos=(0.85, -0.85), height=0.1, wrapWidth=None, ori=0, 
    color='lightGrey', colorSpace='rgb', opacity=1,
    depth=-9.0);
dados = []

tentativa = 0

# Initialize components for Routine "inst_self_evalu"
inst_self_evaluClock = core.Clock()
sound_beep_2 = sound.Sound('audio/beep.wav', secs=0.5)
sound_beep_2.setVolume(1)
inst_10 = visual.TextStim(win=win, name='inst_10',
    text='Muito bem!\nO estudo está quase no final!\n\nPor favor, indique qual a porcentagem de relações\nque você acha que conseguiu identificar.\n\nPressione "Enter" para continuar\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "self_evalu_response"
self_evalu_responseClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Pressione:\n\n1 = até 25%;\n\n2 = entre 25 e 50%;\n\n3 = entre 50 e 75%;\n\n4 = acima de 75%.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "inst_final"
inst_finalClock = core.Clock()
sound_beep_4 = sound.Sound('audio/beep.wav', secs=0.5)
sound_beep_4.setVolume(1)
inst_13 = visual.TextStim(win=win, name='inst_13',
    text='Muito bem!\nVocê terminou o estudo!\n\nVocê já pode tirar o fone de ouvido.\n\nPressione "Enter" para chamar o pesquisador',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "inst_initial"-------
t = 0
inst_initialClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_1 = event.BuilderKeyResponse()
# keep track of which components have finished
inst_initialComponents = [inst_1, key_resp_1]
for thisComponent in inst_initialComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "inst_initial"-------
while continueRoutine:
    # get current time
    t = inst_initialClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *inst_1* updates
    if t >= 0.0 and inst_1.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_1.tStart = t
        inst_1.frameNStart = frameN  # exact frame index
        inst_1.setAutoDraw(True)
    
    # *key_resp_1* updates
    if t >= 0.0 and key_resp_1.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_1.tStart = t
        key_resp_1.frameNStart = frameN  # exact frame index
        key_resp_1.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_1.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in inst_initialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "inst_initial"-------
for thisComponent in inst_initialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "inst_initial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "inst_vol"-------
t = 0
inst_volClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
inst_volComponents = [img_keyboard_1, music_1, key_resp_2]
for thisComponent in inst_volComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "inst_vol"-------
while continueRoutine:
    # get current time
    t = inst_volClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *img_keyboard_1* updates
    if t >= 0.0 and img_keyboard_1.status == NOT_STARTED:
        # keep track of start time/frame for later
        img_keyboard_1.tStart = t
        img_keyboard_1.frameNStart = frameN  # exact frame index
        img_keyboard_1.setAutoDraw(True)
    # start/stop music_1
    if t >= 0.0 and music_1.status == NOT_STARTED:
        # keep track of start time/frame for later
        music_1.tStart = t
        music_1.frameNStart = frameN  # exact frame index
        music_1.play()  # start the sound (it finishes automatically)
    frameRemains = 0.0 + 1000.00- win.monitorFramePeriod * 0.75  # most of one frame period left
    if music_1.status == STARTED and t >= frameRemains:
        music_1.stop()  # stop the sound (if longer than duration)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in inst_volComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "inst_vol"-------
for thisComponent in inst_volComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
music_1.stop()  # ensure sound has stopped at end of routine
# the Routine "inst_vol" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "inst_vol2"-------
t = 0
inst_vol2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()
# keep track of which components have finished
inst_vol2Components = [inst_2, key_resp_3]
for thisComponent in inst_vol2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "inst_vol2"-------
while continueRoutine:
    # get current time
    t = inst_vol2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *inst_2* updates
    if t >= 0.0 and inst_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_2.tStart = t
        inst_2.frameNStart = frameN  # exact frame index
        inst_2.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 1.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in inst_vol2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "inst_vol2"-------
for thisComponent in inst_vol2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "inst_vol2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "inst_training"-------
t = 0
inst_trainingClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()
# keep track of which components have finished
inst_trainingComponents = [inst_3, key_resp_4]
for thisComponent in inst_trainingComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "inst_training"-------
while continueRoutine:
    # get current time
    t = inst_trainingClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *inst_3* updates
    if t >= 0.0 and inst_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_3.tStart = t
        inst_3.frameNStart = frameN  # exact frame index
        inst_3.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 1.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in inst_trainingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "inst_training"-------
for thisComponent in inst_trainingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "inst_training" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "inst_training_2"-------
t = 0
inst_training_2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_6 = event.BuilderKeyResponse()
# keep track of which components have finished
inst_training_2Components = [text_5, key_resp_6]
for thisComponent in inst_training_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "inst_training_2"-------
while continueRoutine:
    # get current time
    t = inst_training_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if t >= 0.0 and text_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_5.tStart = t
        text_5.frameNStart = frameN  # exact frame index
        text_5.setAutoDraw(True)
    
    # *key_resp_6* updates
    if t >= 1.0 and key_resp_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_6.tStart = t
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_6.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in inst_training_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "inst_training_2"-------
for thisComponent in inst_training_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "inst_training_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('training.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fixation"-------
    t = 0
    fixationClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationComponents = [text_3]
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "fixation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixationClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if t >= 0.0 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t
            text_3.frameNStart = frameN  # exact frame index
            text_3.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_3.status == STARTED and t >= frameRemains:
            text_3.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation"-------
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "training"-------
    t = 0
    trainingClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    sound_training_1.setSound(audio1, secs=0.90)
    sound_training_2.setSound(audio2, secs=0.90)
    img_training_1.setImage(img1)
    img_training_2.setImage(img2)
    # keep track of which components have finished
    trainingComponents = [sound_training_1, sound_training_2, img_training_1, img_training_2]
    for thisComponent in trainingComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "training"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trainingClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_training_1
        if t >= 0.85 and sound_training_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_training_1.tStart = t
            sound_training_1.frameNStart = frameN  # exact frame index
            sound_training_1.play()  # start the sound (it finishes automatically)
        # start/stop sound_training_2
        if t >= 2.25 and sound_training_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_training_2.tStart = t
            sound_training_2.frameNStart = frameN  # exact frame index
            sound_training_2.play()  # start the sound (it finishes automatically)
        
        # *img_training_1* updates
        if t >= 0.0 and img_training_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            img_training_1.tStart = t
            img_training_1.frameNStart = frameN  # exact frame index
            img_training_1.setAutoDraw(True)
        frameRemains = 0.0 + 4.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if img_training_1.status == STARTED and t >= frameRemains:
            img_training_1.setAutoDraw(False)
        
        # *img_training_2* updates
        if t >= 0.0 and img_training_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            img_training_2.tStart = t
            img_training_2.frameNStart = frameN  # exact frame index
            img_training_2.setAutoDraw(True)
        frameRemains = 0.0 + 4.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if img_training_2.status == STARTED and t >= frameRemains:
            img_training_2.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trainingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "training"-------
    for thisComponent in trainingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_training_1.stop()  # ensure sound has stopped at end of routine
    sound_training_2.stop()  # ensure sound has stopped at end of routine
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "inst_test_fami_1"-------
t = 0
inst_test_fami_1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_5 = event.BuilderKeyResponse()
# keep track of which components have finished
inst_test_fami_1Components = [inst_4, sound_beep_1, key_resp_5]
for thisComponent in inst_test_fami_1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "inst_test_fami_1"-------
while continueRoutine:
    # get current time
    t = inst_test_fami_1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *inst_4* updates
    if t >= 0.0 and inst_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_4.tStart = t
        inst_4.frameNStart = frameN  # exact frame index
        inst_4.setAutoDraw(True)
    # start/stop sound_beep_1
    if t >= 0.0 and sound_beep_1.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_beep_1.tStart = t
        sound_beep_1.frameNStart = frameN  # exact frame index
        sound_beep_1.play()  # start the sound (it finishes automatically)
    
    # *key_resp_5* updates
    if t >= 2.0 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_5.tStart = t
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_5.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in inst_test_fami_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "inst_test_fami_1"-------
for thisComponent in inst_test_fami_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_beep_1.stop()  # ensure sound has stopped at end of routine
# the Routine "inst_test_fami_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "inst_test_fami_2"-------
t = 0
inst_test_fami_2Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
inst_test_fami_2Components = [img_keyboard_2]
for thisComponent in inst_test_fami_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "inst_test_fami_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = inst_test_fami_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *img_keyboard_2* updates
    if t >= 0.0 and img_keyboard_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        img_keyboard_2.tStart = t
        img_keyboard_2.frameNStart = frameN  # exact frame index
        img_keyboard_2.setAutoDraw(True)
    frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if img_keyboard_2.status == STARTED and t >= frameRemains:
        img_keyboard_2.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in inst_test_fami_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "inst_test_fami_2"-------
for thisComponent in inst_test_fami_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "inst_test_fami_3"-------
t = 0
inst_test_fami_3Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(1.500000)
# update component parameters for each repeat
# keep track of which components have finished
inst_test_fami_3Components = [img_keyboard_3]
for thisComponent in inst_test_fami_3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "inst_test_fami_3"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = inst_test_fami_3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *img_keyboard_3* updates
    if t >= 0.0 and img_keyboard_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        img_keyboard_3.tStart = t
        img_keyboard_3.frameNStart = frameN  # exact frame index
        img_keyboard_3.setAutoDraw(True)
    frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if img_keyboard_3.status == STARTED and t >= frameRemains:
        img_keyboard_3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in inst_test_fami_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "inst_test_fami_3"-------
for thisComponent in inst_test_fami_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "inst_test_fami_4"-------
t = 0
inst_test_fami_4Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(1.500000)
# update component parameters for each repeat
# keep track of which components have finished
inst_test_fami_4Components = [img_keyboard_4]
for thisComponent in inst_test_fami_4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "inst_test_fami_4"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = inst_test_fami_4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *img_keyboard_4* updates
    if t >= 0.0 and img_keyboard_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        img_keyboard_4.tStart = t
        img_keyboard_4.frameNStart = frameN  # exact frame index
        img_keyboard_4.setAutoDraw(True)
    frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if img_keyboard_4.status == STARTED and t >= frameRemains:
        img_keyboard_4.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in inst_test_fami_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "inst_test_fami_4"-------
for thisComponent in inst_test_fami_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "inst_test_fami_5"-------
t = 0
inst_test_fami_5Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_7 = event.BuilderKeyResponse()
# keep track of which components have finished
inst_test_fami_5Components = [img_keyboard_5, key_resp_7]
for thisComponent in inst_test_fami_5Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "inst_test_fami_5"-------
while continueRoutine:
    # get current time
    t = inst_test_fami_5Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *img_keyboard_5* updates
    if t >= 0.0 and img_keyboard_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        img_keyboard_5.tStart = t
        img_keyboard_5.frameNStart = frameN  # exact frame index
        img_keyboard_5.setAutoDraw(True)
    
    # *key_resp_7* updates
    if t >= 0.0 and key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_7.tStart = t
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_7.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in inst_test_fami_5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "inst_test_fami_5"-------
for thisComponent in inst_test_fami_5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "inst_test_fami_5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop_familiar = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('testFamiliar.xlsx'),
    seed=None, name='loop_familiar')
thisExp.addLoop(loop_familiar)  # add the loop to the experiment
thisLoop_familiar = loop_familiar.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_familiar.rgb)
if thisLoop_familiar != None:
    for paramName in thisLoop_familiar:
        exec('{} = thisLoop_familiar[paramName]'.format(paramName))

for thisLoop_familiar in loop_familiar:
    currentLoop = loop_familiar
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_familiar.rgb)
    if thisLoop_familiar != None:
        for paramName in thisLoop_familiar:
            exec('{} = thisLoop_familiar[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fixation"-------
    t = 0
    fixationClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationComponents = [text_3]
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "fixation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixationClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if t >= 0.0 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t
            text_3.frameNStart = frameN  # exact frame index
            text_3.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_3.status == STARTED and t >= frameRemains:
            text_3.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation"-------
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "test_familiar"-------
    t = 0
    test_familiarClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    sound_test_fami.setSound(audioTestFami, secs=0.9)
    image_3.setImage(imgTestFami1)
    image_4.setImage(imgTestFami2)
    image_5.setImage(imgTestFami3)
    image_6.setImage(imgTestFami4)
    key_resp_19 = event.BuilderKeyResponse()
    # keep track of which components have finished
    test_familiarComponents = [sound_test_fami, image_3, image_4, image_5, image_6, label_1, label_2, label_3, label_4, key_resp_19]
    for thisComponent in test_familiarComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "test_familiar"-------
    while continueRoutine:
        # get current time
        t = test_familiarClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_test_fami
        if t >= 1.0 and sound_test_fami.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_test_fami.tStart = t
            sound_test_fami.frameNStart = frameN  # exact frame index
            sound_test_fami.play()  # start the sound (it finishes automatically)
        
        # *image_3* updates
        if t >= 0.0 and image_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_3.tStart = t
            image_3.frameNStart = frameN  # exact frame index
            image_3.setAutoDraw(True)
        
        # *image_4* updates
        if t >= 0.0 and image_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_4.tStart = t
            image_4.frameNStart = frameN  # exact frame index
            image_4.setAutoDraw(True)
        
        # *image_5* updates
        if t >= 0.0 and image_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_5.tStart = t
            image_5.frameNStart = frameN  # exact frame index
            image_5.setAutoDraw(True)
        
        # *image_6* updates
        if t >= 0.0 and image_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_6.tStart = t
            image_6.frameNStart = frameN  # exact frame index
            image_6.setAutoDraw(True)
        
        # *label_1* updates
        if t >= 0.0 and label_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            label_1.tStart = t
            label_1.frameNStart = frameN  # exact frame index
            label_1.setAutoDraw(True)
        
        # *label_2* updates
        if t >= 0.0 and label_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            label_2.tStart = t
            label_2.frameNStart = frameN  # exact frame index
            label_2.setAutoDraw(True)
        
        # *label_3* updates
        if t >= 0.0 and label_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            label_3.tStart = t
            label_3.frameNStart = frameN  # exact frame index
            label_3.setAutoDraw(True)
        
        # *label_4* updates
        if t >= 0.0 and label_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            label_4.tStart = t
            label_4.frameNStart = frameN  # exact frame index
            label_4.setAutoDraw(True)
        
        # *key_resp_19* updates
        if t >= 1.0 and key_resp_19.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_19.tStart = t
            key_resp_19.frameNStart = frameN  # exact frame index
            key_resp_19.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_19.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_19.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_19.keys = theseKeys[-1]  # just the last key pressed
                key_resp_19.rt = key_resp_19.clock.getTime()
                # was this 'correct'?
                if (key_resp_19.keys == str(correctTestFami)) or (key_resp_19.keys == correctTestFami):
                    key_resp_19.corr = 1
                else:
                    key_resp_19.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test_familiarComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "test_familiar"-------
    for thisComponent in test_familiarComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_test_fami.stop()  # ensure sound has stopped at end of routine
    # check responses
    if key_resp_19.keys in ['', [], None]:  # No response was made
        key_resp_19.keys=None
        # was no response the correct answer?!
        if str(correctTestFami).lower() == 'none':
           key_resp_19.corr = 1  # correct non-response
        else:
           key_resp_19.corr = 0  # failed to respond (incorrectly)
    # store data for loop_familiar (TrialHandler)
    loop_familiar.addData('key_resp_19.keys',key_resp_19.keys)
    loop_familiar.addData('key_resp_19.corr', key_resp_19.corr)
    if key_resp_19.keys != None:  # we had a response
        loop_familiar.addData('key_resp_19.rt', key_resp_19.rt)
    # the Routine "test_familiar" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'loop_familiar'


# ------Prepare to start Routine "inst_teste_1"-------
t = 0
inst_teste_1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_10 = event.BuilderKeyResponse()
# keep track of which components have finished
inst_teste_1Components = [inst_7, key_resp_10]
for thisComponent in inst_teste_1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "inst_teste_1"-------
while continueRoutine:
    # get current time
    t = inst_teste_1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *inst_7* updates
    if t >= 0.0 and inst_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_7.tStart = t
        inst_7.frameNStart = frameN  # exact frame index
        inst_7.setAutoDraw(True)
    
    # *key_resp_10* updates
    if t >= 1.0 and key_resp_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_10.tStart = t
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_10.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in inst_teste_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "inst_teste_1"-------
for thisComponent in inst_teste_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "inst_teste_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "inst_teste_2"-------
t = 0
inst_teste_2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_11 = event.BuilderKeyResponse()
# keep track of which components have finished
inst_teste_2Components = [inst_8, key_resp_11]
for thisComponent in inst_teste_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "inst_teste_2"-------
while continueRoutine:
    # get current time
    t = inst_teste_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *inst_8* updates
    if t >= 0.0 and inst_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_8.tStart = t
        inst_8.frameNStart = frameN  # exact frame index
        inst_8.setAutoDraw(True)
    
    # *key_resp_11* updates
    if t >= 1.0 and key_resp_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_11.tStart = t
        key_resp_11.frameNStart = frameN  # exact frame index
        key_resp_11.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_11.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in inst_teste_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "inst_teste_2"-------
for thisComponent in inst_teste_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "inst_teste_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop_test = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('test.xlsx'),
    seed=None, name='loop_test')
thisExp.addLoop(loop_test)  # add the loop to the experiment
thisLoop_test = loop_test.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_test.rgb)
if thisLoop_test != None:
    for paramName in thisLoop_test:
        exec('{} = thisLoop_test[paramName]'.format(paramName))

for thisLoop_test in loop_test:
    currentLoop = loop_test
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_test.rgb)
    if thisLoop_test != None:
        for paramName in thisLoop_test:
            exec('{} = thisLoop_test[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fixation_2"-------
    t = 0
    fixation_2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixation_2Components = [text_2]
    for thisComponent in fixation_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "fixation_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixation_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if t >= 0.0 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_2.status == STARTED and t >= frameRemains:
            text_2.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixation_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation_2"-------
    for thisComponent in fixation_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "test_trials"-------
    t = 0
    test_trialsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    sound_1.setSound(audioTest, secs=0.9)
    image.setImage(imgTestA)
    image_2.setImage(imgTestB)
    image_7.setImage(imgTestC)
    image_8.setImage(imgTestD)
    key_resp_8 = event.BuilderKeyResponse()
    
    # keep track of which components have finished
    test_trialsComponents = [sound_1, image, image_2, image_7, image_8, key_resp_8, text_4, text_6, text_7, text_8]
    for thisComponent in test_trialsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "test_trials"-------
    while continueRoutine:
        # get current time
        t = test_trialsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_1
        if t >= 2.0 and sound_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_1.tStart = t
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.play()  # start the sound (it finishes automatically)
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        
        # *image_2* updates
        if t >= 0.0 and image_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_2.tStart = t
            image_2.frameNStart = frameN  # exact frame index
            image_2.setAutoDraw(True)
        
        # *image_7* updates
        if t >= 0.0 and image_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_7.tStart = t
            image_7.frameNStart = frameN  # exact frame index
            image_7.setAutoDraw(True)
        
        # *image_8* updates
        if t >= 0.0 and image_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_8.tStart = t
            image_8.frameNStart = frameN  # exact frame index
            image_8.setAutoDraw(True)
        
        # *key_resp_8* updates
        if t >= 2.0 and key_resp_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_8.tStart = t
            key_resp_8.frameNStart = frameN  # exact frame index
            key_resp_8.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_8.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_8.keys = theseKeys[-1]  # just the last key pressed
                key_resp_8.rt = key_resp_8.clock.getTime()
                # was this 'correct'?
                if (key_resp_8.keys == str(correctTest)) or (key_resp_8.keys == correctTest):
                    key_resp_8.corr = 1
                else:
                    key_resp_8.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *text_4* updates
        if t >= 0.0 and text_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_4.tStart = t
            text_4.frameNStart = frameN  # exact frame index
            text_4.setAutoDraw(True)
        
        # *text_6* updates
        if t >= 0.0 and text_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_6.tStart = t
            text_6.frameNStart = frameN  # exact frame index
            text_6.setAutoDraw(True)
        
        # *text_7* updates
        if t >= 0.0 and text_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_7.tStart = t
            text_7.frameNStart = frameN  # exact frame index
            text_7.setAutoDraw(True)
        
        # *text_8* updates
        if t >= 0.0 and text_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_8.tStart = t
            text_8.frameNStart = frameN  # exact frame index
            text_8.setAutoDraw(True)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test_trialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "test_trials"-------
    for thisComponent in test_trialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_1.stop()  # ensure sound has stopped at end of routine
    # check responses
    if key_resp_8.keys in ['', [], None]:  # No response was made
        key_resp_8.keys=None
        # was no response the correct answer?!
        if str(correctTest).lower() == 'none':
           key_resp_8.corr = 1  # correct non-response
        else:
           key_resp_8.corr = 0  # failed to respond (incorrectly)
    # store data for loop_test (TrialHandler)
    loop_test.addData('key_resp_8.keys',key_resp_8.keys)
    loop_test.addData('key_resp_8.corr', key_resp_8.corr)
    if key_resp_8.keys != None:  # we had a response
        loop_test.addData('key_resp_8.rt', key_resp_8.rt)
    tentativa = tentativa + 1
    
    la = 0
    le = 0
    
    if key_resp_8.corr == 1:
        la = key_resp_8.rt
    else:
        le = key_resp_8.rt
    
    dados.append([tentativa, key_resp_8.corr, la, le, parT, compA, compB, compC])
    # the Routine "test_trials" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'loop_test'


# ------Prepare to start Routine "inst_self_evalu"-------
t = 0
inst_self_evaluClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_14 = event.BuilderKeyResponse()
# keep track of which components have finished
inst_self_evaluComponents = [sound_beep_2, inst_10, key_resp_14]
for thisComponent in inst_self_evaluComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "inst_self_evalu"-------
while continueRoutine:
    # get current time
    t = inst_self_evaluClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop sound_beep_2
    if t >= 0.0 and sound_beep_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_beep_2.tStart = t
        sound_beep_2.frameNStart = frameN  # exact frame index
        sound_beep_2.play()  # start the sound (it finishes automatically)
    
    # *inst_10* updates
    if t >= 0.0 and inst_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_10.tStart = t
        inst_10.frameNStart = frameN  # exact frame index
        inst_10.setAutoDraw(True)
    
    # *key_resp_14* updates
    if t >= 1.0 and key_resp_14.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_14.tStart = t
        key_resp_14.frameNStart = frameN  # exact frame index
        key_resp_14.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_14.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in inst_self_evaluComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "inst_self_evalu"-------
for thisComponent in inst_self_evaluComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_beep_2.stop()  # ensure sound has stopped at end of routine
# the Routine "inst_self_evalu" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "self_evalu_response"-------
t = 0
self_evalu_responseClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_15 = event.BuilderKeyResponse()
# keep track of which components have finished
self_evalu_responseComponents = [text, key_resp_15]
for thisComponent in self_evalu_responseComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "self_evalu_response"-------
while continueRoutine:
    # get current time
    t = self_evalu_responseClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *key_resp_15* updates
    if t >= 0.0 and key_resp_15.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_15.tStart = t
        key_resp_15.frameNStart = frameN  # exact frame index
        key_resp_15.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_15.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_15.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', '2', '3', '4'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_15.keys = theseKeys[-1]  # just the last key pressed
            key_resp_15.rt = key_resp_15.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in self_evalu_responseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "self_evalu_response"-------
for thisComponent in self_evalu_responseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_15.keys in ['', [], None]:  # No response was made
    key_resp_15.keys=None
thisExp.addData('key_resp_15.keys',key_resp_15.keys)
if key_resp_15.keys != None:  # we had a response
    thisExp.addData('key_resp_15.rt', key_resp_15.rt)
thisExp.nextEntry()
# the Routine "self_evalu_response" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "inst_final"-------
t = 0
inst_finalClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_18 = event.BuilderKeyResponse()
# keep track of which components have finished
inst_finalComponents = [sound_beep_4, inst_13, key_resp_18]
for thisComponent in inst_finalComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "inst_final"-------
while continueRoutine:
    # get current time
    t = inst_finalClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop sound_beep_4
    if t >= 0.0 and sound_beep_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_beep_4.tStart = t
        sound_beep_4.frameNStart = frameN  # exact frame index
        sound_beep_4.play()  # start the sound (it finishes automatically)
    
    # *inst_13* updates
    if t >= 0.0 and inst_13.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_13.tStart = t
        inst_13.frameNStart = frameN  # exact frame index
        inst_13.setAutoDraw(True)
    
    # *key_resp_18* updates
    if t >= 1.0 and key_resp_18.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_18.tStart = t
        key_resp_18.frameNStart = frameN  # exact frame index
        key_resp_18.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_18.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in inst_finalComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "inst_final"-------
for thisComponent in inst_finalComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_beep_4.stop()  # ensure sound has stopped at end of routine
# the Routine "inst_final" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
np.savetxt(filename+".txt", dados,  delimiter = "\t")
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
