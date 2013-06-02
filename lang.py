# -*- coding: utf-8 -*-
SET_TIME = 'Alterar tempo (%d segs)'
RESET_TIME = 'Resetar tempo'
NO_RUNNING = u"Nenhum projeto em execução"
PAUSE = 'Pausar'
START = 'Reproduzir'
TIME_IS_UP = 'Your time is up!'
TIME_IS_UP_UNSTOPPABLE = ('Your time is up!\n'
                          '\n'
                          'time won`''t stop and wait for you!\n'
                          'RUN!'
)
WRITE_TIME = 'Escolha o tempo (em segundos)!'
VALUE_ERROR = u"Caracter inválido. Suas alterações não foram salvas"

KILL = "Matar %s"

ARDUINO_ERROR = u'Algum erro de comunicação com o Arduino ocorreu!'

INTERRUPTED_EXECUTION = u"Execução interrompida"

PATTERNS_NOT_FOUND = 'Could not find %s. Patterns will not be ignored\n' 

PYNOTIFY_IMPORT_ERROR1 = '\n\n*** Could not import pynotify. '
PYNOTIFY_IMPORT_ERROR2 = ('Make sure it is installed so you '
                          'can see the notifications ***\n\n\n')

GIT_ERROR1 = 'Impossible to commit to repository. '
GIT_ERROR2 = 'Make sure git is installed and this is a valid repository'

DESCRIPTION = """
    %prog watches a directory for changes. As soon as there are any changes
    to the files being watched, it runs the commands specified as positional
    arguments. You can specify as many commands as you wish, but don't forget
    to use quotes if you command has spaces in it.
""".replace('  ', '')
GENERATOR_DESCRIPTION = """
    %prog is a tool that generates a folder structure to start a Dojo. To
    generate the Dojo files, both the language and problem name parameters
    must be specified. The extra name parameter is optional. The generated
    folder will have the name in the following format:
    "[yearmonthday]_[extraname]_[language]_[problemname]"
""".replace('  ', '')
GIT_HELP = ('if this flag is used, a git commit will '
            'be issued whenever the files change')
DIRECTORY_HELP = 'Watch DIRECTORY'
PATTERNS_HELP = 'Defines the file with patterns to ignore. '
TIME_HELP = 'Define the time of each round'
ARDUINO_HELP = 'If this flag is used an interface with Arduino will be used'
MULTITHREAD_HELP = 'If this flag is used the program will run in a thread'
BEFORE_HELP = ('Run this command before running tests.'
               'WARNING: It will not run in thread, so be careful with your commands'
)
UNSTOPPABLE_HELP = ("if this flag is used, the time won't stop after the end of a round")
GENERATE_HELP = ("generate a folder with files for coding dojo. "
                 "GENERATE: '(language) (problem) (modifiers)'"
)
WHO_HELP = ("if this flag is used, dojotools will ask who is the pilot before each session")
LANG_HELP = ("specifies the language to be used. Available languages: c, coffeescript, haskell, java, javascript, lua, moonscript, pascal, python, ruby")
PROBLEM_NAME_HELP = ("specifies the name of the problem")
EXTRA_NAME_HELP = ("specifies an extra name that will be used to name the problem folder. Optional.")

RUN_FILE_WARNING = "Dojotools couldn't find run.dojo. Now it's just a timer!" 

MONITORING = 'Monitoring files in %s'
IGNORING = 'ignoring files in %s'
QUIT = 'press ^C to quit'

LEAVING = '\nleaving...'


GENERATOR_ERROR = 'Generator failed to generate files'
GENERATING_MESSAGE = "Generating Folder..."
LANGUAGE_FOUND = "Language found: %s"
LANGUAGE_GENERATOR_ERROR = "%s generator wasn't found"
DOJO_PATH_EXISTS_ERROR = "Dojo path already exists! Dojotools will try to run this code!"

GENERATOR_MESSAGES = {
    'error': GENERATOR_ERROR,
    'message': GENERATING_MESSAGE,
    'lang': LANGUAGE_FOUND,
    'lang_error': LANGUAGE_GENERATOR_ERROR,
    'exists': DOJO_PATH_EXISTS_ERROR,
}

WRITE_WHO = 'Who plays?'



